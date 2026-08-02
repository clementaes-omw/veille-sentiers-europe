#!/usr/bin/env python3
"""
Audit de fraîcheur et de pertinence du registre d'alertes.

Le build (site/build_site.py) contrôle la FORME de ce qui est publié. Ce script
contrôle la VÉRITÉ dans le temps : une alerte peut être parfaitement formée et
raconter la situation d'il y a trois semaines. C'est le défaut le plus coûteux
du site — un randonneur qui lit « massif interdit » sur la foi d'une page
préfectorale périmée fait demi-tour pour rien, et l'inverse est pire.

Tout est déterministe et hors-ligne : aucune clé d'API, aucun appel réseau. Ce
qui relève du jugement (la source dit-elle vraiment ça ? l'alerte a-t-elle encore
un sens ?) est le travail de l'agent relecteur — agents/verificateur-alertes.md.

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
)

RAPPORT = LIVRABLES / "audit-qualite.md"

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


def rapport_md(cards, constats) -> str:
    auj = date.today().isoformat()
    n = {k: sum(1 for x in constats if x[0] == k) for k in ("BLOQUANT", "ALERTE", "INFO")}
    actives = [c for c in cards if "CLÔTURÉ" not in c["statut"].upper()]
    touchees = len({x[1] for x in constats})
    lignes = [
        f"# Audit qualité du registre — {auj}",
        "",
        f"{len(actives)} alertes actives · {touchees} fiches avec au moins un constat · "
        f"**{n['BLOQUANT']} bloquant(s)**, {n['ALERTE']} alerte(s), {n['INFO']} info(s).",
        "",
        "Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le "
        "fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le "
        "terrain — relève de `agents/verificateur-alertes.md`.",
        "",
    ]
    if not constats:
        lignes.append("Aucun constat : le registre est à jour.")
        return "\n".join(lignes) + "\n"
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
    return "\n".join(lignes) + "\n"


def main() -> int:
    cards = load_alertes()
    constats = auditer(cards)
    txt = rapport_md(cards, constats)
    if "--ecrire" in sys.argv:
        RAPPORT.write_text(txt, encoding="utf-8")
        print(f"rapport écrit → {RAPPORT}")
    bloquants = [x for x in constats if x[0] == "BLOQUANT"]
    for niveau, cle, msg in constats:
        marque = {"BLOQUANT": "⛔", "ALERTE": "⚠️ ", "INFO": "· "}[niveau]
        print(f"{marque} {cle[:52]:54s} {msg}")
    print(f"\n{len(constats)} constat(s) sur {len(cards)} fiches — "
          f"{len(bloquants)} bloquant(s).")
    return 1 if bloquants else 0


if __name__ == "__main__":
    sys.exit(main())
