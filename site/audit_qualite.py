#!/usr/bin/env python3
"""
Audit de fraîcheur et de pertinence du registre d'alertes.

Le build (site/build_site.py) contrôle la FORME de ce qui est publié. Ce script
contrôle la VÉRITÉ dans le temps : une alerte peut être parfaitement formée et
raconter la situation d'il y a trois semaines. C'est le défaut le plus coûteux
du site — un randonneur qui lit « massif interdit » sur la foi d'une page
préfectorale périmée fait demi-tour pour rien, et l'inverse est pire.

Depuis l'onglet Carte (commit carte-zones-alertes), il contrôle aussi la
COHÉRENCE carte/registre : une alerte active dont la zone ne se résout vers aucun
code de referentiel/zones-coords.csv est publiée mais n'apparaît sur AUCUN
marqueur — le build ne le signale que sur stderr, sans bloquer. L'audit en fait un
constat BLOQUANT (« alerte perdue »), vérifie que le compte de marqueurs couvre
toutes les actives, et signale (non bloquant) toute zone-source du référentiel
encore dépourvue de coordonnées.

Tout est déterministe et hors-ligne : aucune clé d'API, aucun appel réseau. Ce
qui relève du jugement (la source dit-elle vraiment ça ? l'alerte a-t-elle encore
un sens ? le centroïde d'une zone est-il plausible ?) est le travail des agents
relecteurs — agents/verificateur-alertes.md et agents/verificateur-carte.md.

Sortie : livrables/audit-qualite.md + un résumé sur stdout.
Code retour : 1 s'il reste au moins un constat BLOQUANT, 0 sinon.

Usage : python3 site/audit_qualite.py [--ecrire]
"""
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import (  # noqa: E402  (import après ajustement du sys.path)
    JARGON_INTERNE, HYPO_MARQUEURS, HYPO_DELAI_JOURS, LIVRABLES, MOIS,
    fold_txt, load_alertes, sev_class, _age_jours,
    load_zones_coords, zones_carte,
)

RAPPORT = LIVRABLES / "audit-qualite.md"
ZONES_SOURCES_MD = LIVRABLES.parent / "referentiel" / "zones-sources.md"

# Un code de zone-source tel qu'il paraît en 1re cellule des tableaux de
# zones-sources.md : deux majuscules ou plus, puis au moins un segment « -XXX »
# (le format « XX-… » du référentiel). Le tiret exigé écarte volontairement les
# codes atomiques (IS, AT, DE, BENELUX) et l'ancien « SCAND » subdivisé depuis en
# SCAND-NO/SCAND-SE — tous déjà présents dans zones-coords.csv, donc sans objet.
CODE_ZONE = re.compile(r"^[A-Z]{2,}(?:-[A-Z0-9]+)+$")

# Fraîcheur attendue d'une revérification, en jours, selon ce que l'alerte prétend.
# Une fermeture décidée au jour le jour et vérifiée il y a six jours n'est plus une
# information : c'est un souvenir.
FRAICHEUR = {"journaliere": 2, "haute": 4, "moyenne": 12, "info": 45}
# Au-delà de ce multiple du seuil, ce n'est plus un retard mais une donnée morte.
FACTEUR_BLOQUANT = 2.5
# Écart toléré entre ce que la veille sait (statut:) et ce que le site affiche (portion).
DECROCHAGE_JOURS = 7
DECROCHAGE_BLOQUANT = 14

DATE_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
DATE_FR = re.compile(r"\b(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?\b")


def dates_citees(txt: str, annee_defaut: int) -> list:
    """Toutes les dates lisibles d'un texte (2026-07-23, 23/07/2026, 23/07)."""
    out = []
    for a, m, j in DATE_ISO.findall(txt or ""):
        try:
            out.append(date(int(a), int(m), int(j)))
        except ValueError:
            pass
    for j, m, a in DATE_FR.findall(txt or ""):
        an = annee_defaut if not a else (int(a) if len(a) == 4 else 2000 + int(a))
        try:
            out.append(date(an, int(m), int(j)))
        except ValueError:
            pass          # 32/13 et autres numéros de version pris pour des dates
    return out


def plus_recente(txt: str, annee_defaut: int):
    d = [x for x in dates_citees(txt, annee_defaut) if x <= date.today()]
    return max(d) if d else None


def seuil_fraicheur(c) -> tuple:
    """(seuil en jours, motif) — la validité prime sur la sévérité."""
    val = fold_txt(c["validite"])
    if any(m in val for m in ("journalier", "journaliere", "quotidien", "jour le jour")):
        return FRAICHEUR["journaliere"], "restriction décidée au jour le jour"
    sev = sev_class(c["sev"])
    return FRAICHEUR.get(sev, FRAICHEUR["info"]), f"sévérité {sev}"


def auditer(cards) -> list:
    """Renvoie une liste de constats (niveau, clé, message)."""
    constats = []
    auj = date.today()

    def ajoute(niveau, c, msg):
        constats.append((niveau, c["cle"], msg))

    for c in cards:
        if "CLÔTURÉ" in c["statut"].upper():
            continue
        sev = sev_class(c["sev"])
        age_verif = _age_jours(c["verif"])
        annee = int(c["verif"][:4]) if re.match(r"\d{4}", c["verif"] or "") else auj.year

        # 1. Fraîcheur de la revérification -----------------------------------
        seuil, motif = seuil_fraicheur(c)
        if age_verif is not None and age_verif > seuil:
            niveau = "BLOQUANT" if age_verif > seuil * FACTEUR_BLOQUANT else "ALERTE"
            ajoute(niveau, c,
                   f"vérifiée il y a {age_verif} j (seuil {seuil} j — {motif}). "
                   f"Le site présente cette restriction comme actuelle.")

        # 2. La description publique a-t-elle décroché de ce que la veille sait ?
        # Contrôle réservé aux restrictions à cycle court : un reroutage consécutif à un
        # éboulement de janvier cite légitimement janvier six mois plus tard, alors qu'une
        # fermeture décidée au jour le jour qui affiche une date d'il y a trois semaines
        # ment au lecteur.
        cycle_court = motif.startswith("restriction") or sev == "haute"
        d_statut = plus_recente(c["statut"], annee)
        d_portion = plus_recente(c["portion"], annee)
        if cycle_court and d_statut and d_portion \
                and (d_statut - d_portion).days > DECROCHAGE_JOURS:
            ecart = (d_statut - d_portion).days
            niveau = "BLOQUANT" if ecart > DECROCHAGE_BLOQUANT else "ALERTE"
            ajoute(niveau, c,
                   f"« Portion concernée » parle du {d_portion:%d/%m} alors que le suivi "
                   f"connaît la situation au {d_statut:%d/%m} ({ecart} j d'écart) — "
                   f"la mise à jour n'est pas arrivée jusqu'au texte affiché.")

        # 3. Validité expirée mais alerte toujours ouverte ---------------------
        # On regarde la date la PLUS TARDIVE du champ : « 15/06→30/09 » est une plage
        # encore ouverte, pas une échéance passée. Et on ne juge pas les validités
        # ouvertes par nature (revue quotidienne, « jusqu'à levée de l'arrêté »).
        val = fold_txt(c["validite"])
        ouverte = any(m in val for m in (
            "quotidien", "journalier", "journaliere", "jusqu'a levee", "jusqu a levee",
            "nouvel ordre", "prolongation", "durable", "arrete-cadre", "arrete cadre"))
        # « du 15/06 à fin septembre » : l'échéance est écrite en toutes lettres et
        # échappe aux formats numériques — la compter, sinon on clôture à tort.
        for i, nom in enumerate(MOIS, start=1):
            if nom in val:
                an = int(m2.group(1)) if (m2 := re.search(
                    rf"{nom}\s+(\d{{4}})", val)) else annee
                if date(an, i, 28) >= auj:
                    ouverte = True
                    break
        d_val = dates_citees(c["validite"], annee)
        if not ouverte and d_val and max(d_val) < auj and (auj - max(d_val)).days > 2:
            ajoute("ALERTE", c,
                   f"la validité annoncée s'arrête au {max(d_val):%d/%m/%Y}, désormais "
                   f"passé : clôturer l'alerte, ou réécrire la validité si elle est "
                   f"prolongée.")

        # 4. Source vieillie sous une alerte qui se veut quotidienne -----------
        d_src = plus_recente(c["source"], annee)
        if sev == "haute" and d_src and (auj - d_src).days > 10:
            ajoute("ALERTE", c,
                   f"alerte rouge appuyée sur une source datée du {d_src:%d/%m} "
                   f"({(auj - d_src).days} j) — retrouver une publication récente "
                   f"ou dégrader la sévérité.")

        # 5. Hypothèse jamais tranchée ----------------------------------------
        plie_p = fold_txt(c["portion"])
        marq = next((m for m in HYPO_MARQUEURS if m in plie_p), None)
        age_det = _age_jours(c["detection"])
        if sev == "haute" and marq and age_det and age_det > HYPO_DELAI_JOURS:
            ajoute("BLOQUANT", c,
                   f"alerte rouge encore adossée à « {marq} » {age_det} j après détection.")

        # 6. Jamais revérifiée depuis la détection ----------------------------
        if age_det and age_verif is not None and c["verif"][:10] == c["detection"][:10] \
                and age_det > 7:
            ajoute("ALERTE", c,
                   f"jamais revérifiée depuis sa détection il y a {age_det} j.")

        # 7. Alerte rouge sans source consultable ------------------------------
        if sev == "haute" and "http" not in c["source"]:
            ajoute("BLOQUANT", c, "alerte rouge sans aucune URL de source vérifiable.")

        # 8. Ton — jargon de veille dans le narratif public --------------------
        hits = sorted({f.strip() for f in JARGON_INTERNE if f in fold_txt(c["zone"])})
        if hits:
            ajoute("INFO", c,
                   f"« Zone (détails) » contient encore du jargon de veille "
                   f"({', '.join(hits)}) au lieu de l'état du terrain.")

    ordre = {"BLOQUANT": 0, "ALERTE": 1, "INFO": 2}
    constats.sort(key=lambda x: (ordre[x[0]], x[1]))
    return constats


def codes_zones_sources() -> set:
    """Codes de zones-sources déclarés dans referentiel/zones-sources.md.

    Lus en 1re cellule des tableaux (le référentiel liste chaque zone-source sur
    une ligne « | CODE | … »). On ne balaie pas la prose : les mêmes codes y
    reviennent en gras et se mêleraient aux noms de GR (« GR-E4 » vs « GR10 »)."""
    codes = set()
    if not ZONES_SOURCES_MD.exists():
        return codes
    for ligne in ZONES_SOURCES_MD.read_text(encoding="utf-8").splitlines():
        s = ligne.strip()
        if not s.startswith("|"):
            continue
        premiere = s.strip("|").split("|")[0].strip().strip("*").strip()
        if CODE_ZONE.match(premiere):
            codes.add(premiere)
    return codes


def auditer_carte(cards, coords) -> list:
    """Cohérence entre le registre et la vue Carte du site.

    La carte n'affiche qu'UN marqueur par zone-source résolue (site/build_site.py,
    zones_carte). Une alerte active dont la zone ne se résout vers aucun code de
    zones-coords.csv est publiée mais INVISIBLE sur la carte : le build ne l'écrit
    que sur stderr, sans bloquer. C'est le défaut le plus silencieux de la vue.

    Renvoie une liste de constats (niveau, clé, message), même forme que auditer().
    On réutilise zones_carte() : aucune logique de résolution n'est redupliquée ici."""
    constats = []
    actives = [c for c in cards if "CLÔTURÉ" not in c["statut"].upper()]
    liste, non_mappees = zones_carte(actives, coords)

    # 1. Aucune alerte active ne doit tomber hors de la carte -----------------
    for zone_str, cle in non_mappees:
        z = zone_str or "(zone vide)"
        constats.append((
            "BLOQUANT", cle,
            f"zone « {z} » non résolue vers referentiel/zones-coords.csv : l'alerte "
            f"est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le "
            f"code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de "
            f"build_site.py."))

    # 2. Le compte de marqueurs doit couvrir toutes les actives ---------------
    n_couvertes = sum(len(g["alertes"]) for g in liste)
    if actives and not liste:
        constats.append((
            "BLOQUANT", "(carte)",
            f"{len(actives)} alerte(s) active(s) mais AUCUN marqueur sur la carte — "
            f"la vue Carte est vide alors que le registre ne l'est pas."))
    if n_couvertes != len(actives):
        perdues = len(actives) - n_couvertes
        constats.append((
            "BLOQUANT", "(carte)",
            f"regroupement incohérent : {n_couvertes} alerte(s) réparties sur "
            f"{len(liste)} marqueur(s) pour {len(actives)} active(s) — {perdues} "
            f"alerte(s) hors carte."))

    # 3. Complétude du référentiel de coordonnées (non bloquant) --------------
    # Une zone sans alerte n'a pas besoin d'un marqueur, mais le référentiel doit
    # rester complet pour la première alerte qui la touchera.
    for code in sorted(codes_zones_sources() - set(coords)):
        constats.append((
            "ALERTE", code,
            f"zone-source déclarée dans referentiel/zones-sources.md mais sans "
            f"coordonnées dans zones-coords.csv : aucune alerte de cette zone ne "
            f"pourrait apparaître sur la carte. Compléter le CSV (code;nom;lat;lon)."))

    ordre = {"BLOQUANT": 0, "ALERTE": 1, "INFO": 2}
    constats.sort(key=lambda x: (ordre[x[0]], x[1]))
    return constats


def rapport_md(cards, constats, constats_carte=()) -> str:
    auj = date.today().isoformat()
    n = {k: sum(1 for x in constats if x[0] == k) for k in ("BLOQUANT", "ALERTE", "INFO")}
    actives = [c for c in cards if "CLÔTURÉ" not in c["statut"].upper()]
    touchees = len({x[1] for x in constats})
    nc = {k: sum(1 for x in constats_carte if x[0] == k)
          for k in ("BLOQUANT", "ALERTE", "INFO")}
    lignes = [
        f"# Audit qualité du registre — {auj}",
        "",
        f"{len(actives)} alertes actives · {touchees} fiches avec au moins un constat · "
        f"**{n['BLOQUANT']} bloquant(s)**, {n['ALERTE']} alerte(s), {n['INFO']} info(s).",
        "",
        f"Carte : **{nc['BLOQUANT']} bloquant(s)**, {nc['ALERTE']} alerte(s) "
        f"(cohérence carte/registre, voir la section dédiée).",
        "",
        "Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le "
        "fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le "
        "terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des "
        "centroïdes de la carte, de `agents/verificateur-carte.md`.",
        "",
    ]
    if not constats:
        lignes.append("Aucun constat de fraîcheur : le registre est à jour.")
        lignes.append("")
    for niveau, titre in (("BLOQUANT", "⛔ Bloquants — à corriger avant le prochain run"),
                          ("ALERTE", "⚠️ À traiter"),
                          ("INFO", "· Dette de forme")):
        lot = [x for x in constats if x[0] == niveau]
        if not lot:
            continue
        lignes += [f"## {titre}", ""]
        for _, cle, msg in lot:
            lignes.append(f"- **`{cle}`** — {msg}")
        lignes.append("")
    lignes += rapport_carte_md(constats_carte)
    return "\n".join(lignes) + "\n"


def rapport_carte_md(constats_carte) -> list:
    """Section « Cohérence carte / registre » du rapport."""
    lignes = ["## 🗺 Cohérence carte / registre", ""]
    if not constats_carte:
        lignes += [
            "0 alerte perdue : chaque alerte active se résout vers un marqueur de la "
            "carte, le compte de marqueurs couvre toutes les actives, et toute "
            "zone-source du référentiel a ses coordonnées.",
            "",
        ]
        return lignes
    for niveau, titre in (
            ("BLOQUANT", "⛔ Alertes actives invisibles sur la carte / compte incohérent"),
            ("ALERTE", "⚠️ Référentiel de coordonnées à compléter"),
            ("INFO", "· Divers")):
        lot = [x for x in constats_carte if x[0] == niveau]
        if not lot:
            continue
        lignes += [f"### {titre}", ""]
        for _, cle, msg in lot:
            lignes.append(f"- **`{cle}`** — {msg}")
        lignes.append("")
    return lignes


def main() -> int:
    cards = load_alertes()
    constats = auditer(cards)
    coords = load_zones_coords()
    constats_carte = auditer_carte(cards, coords)
    txt = rapport_md(cards, constats, constats_carte)
    if "--ecrire" in sys.argv:
        RAPPORT.write_text(txt, encoding="utf-8")
        print(f"rapport écrit → {RAPPORT}")
    marque = {"BLOQUANT": "⛔", "ALERTE": "⚠️ ", "INFO": "· "}
    bloquants = [x for x in constats + constats_carte if x[0] == "BLOQUANT"]
    for niveau, cle, msg in constats:
        print(f"{marque[niveau]} {cle[:52]:54s} {msg}")
    print("\n— carte —")
    if constats_carte:
        for niveau, cle, msg in constats_carte:
            print(f"{marque[niveau]} {cle[:52]:54s} {msg}")
    else:
        print("· 0 alerte perdue (carte cohérente avec le registre).")
    print(f"\n{len(constats)} constat(s) registre + {len(constats_carte)} carte "
          f"sur {len(cards)} fiches — {len(bloquants)} bloquant(s).")
    return 1 if bloquants else 0


if __name__ == "__main__":
    sys.exit(main())
