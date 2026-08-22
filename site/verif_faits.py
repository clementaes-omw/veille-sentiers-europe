#!/usr/bin/env python3
"""
Garde-fou de réécriture : aucun fait ne doit disparaître ni apparaître.

Réécrire la prose d'une alerte pour qu'elle sonne humaine est une chose ; perdre
« 36 communes » ou transformer 4 900 ha en 5 000 ha en est une autre. Sur un site
qui annonce des interdictions d'accès, la seconde n'est pas un défaut de style,
c'est une information fausse donnée à quelqu'un qui part marcher.

Ce script compare l'état de travail à une référence git et refuse toute réécriture
qui perd un nombre, une date, une URL ou un nom propre, ou qui en invente un. Il ne
juge pas le style : c'est le rôle de la skill humanizer. Il juge les faits.

Usage :
    python3 site/verif_faits.py [ref-git]        # défaut : HEAD
    python3 site/verif_faits.py HEAD --seuil 30  # tolérance de raccourcissement, %
"""
import collections
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
ALERTES = "livrables/alertes"

# Sections dont la prose est réécrite. « Source » est exclue : elle porte les URLs
# et les intitulés de publication, qui se citent, ne se reformulent pas.
SECTIONS_PROSE = ("Portion concernée", "Alternative", "Zone (détails)")

NOMBRE = re.compile(r"\d[\d   ]*(?:[.,]\d+)?")
URL = re.compile(r"https?://[^\s)\]]+")
# Nom propre : capitale initiale, au moins 3 lettres, éventuellement composé
# (Saint-Julien-de-Peyrolas, Ille-sur-Têt, Bagnols-sur-Cèze).
PROPRE = re.compile(r"\b[A-ZÀ-ÖØ-Þ][\wÀ-ÖØ-öø-ÿ]{2,}(?:[-'][\wÀ-ÖØ-öø-ÿ]+)*")

# Mots à capitale qui ne sont pas des noms propres : ils ouvrent une phrase ou
# balisent le registre. Leur disparition n'est pas une perte d'information.
BANALS = {
    "aucun", "aucune", "avant", "cette", "chaque", "dans", "depuis", "elle", "elles",
    "entre", "faire", "fermeture", "fermetures", "interdiction", "interdit", "jusqu",
    "leur", "mais", "massif", "massifs", "meme", "pour", "pendant", "plus", "raison",
    "reste", "sans", "sentier", "sentiers", "seul", "seule", "sous", "sur", "toujours",
    "tous", "tout", "toute", "toutes", "une", "vers", "voir", "zone", "zones",
    "alternative", "attention", "aucunes", "apres", "acces", "arrete", "arretes",
    "note", "nouveau", "nouvelle", "point", "risque", "secteur", "secteurs", "source",
    "sources", "situation", "portion", "detail", "details", "validite", "statut",
    "conditions", "consulter", "eviter", "verifier", "contourner", "prendre",
}


def plie(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def sections(txt: str) -> str:
    """Concatène la prose des sections réécrites, hors frontmatter et hors Source."""
    corps = txt.split("\n---\n", 2)[-1]
    out = []
    for nom in SECTIONS_PROSE:
        m = re.search(rf"^##\s+{re.escape(nom)}\s*$(.*?)(?=^##\s|\Z)", corps,
                      re.M | re.S)
        if m:
            out.append(m.group(1))
    return "\n".join(out)


def faits(txt: str) -> dict:
    """Les trois familles de faits qu'une réécriture ne doit jamais toucher.

    Le ® de « GR® » est retiré d'abord : c'est une mention de marque, pas un fait.
    Sans ce retrait il coupe le nom propre pour PROPRE (« GR®10 » ne rend plus le
    jeton `gr10`), et le passage du registre à la marque déposée remontait en 50
    pertes de noms de sentiers qui étaient pourtant tous encore là."""
    txt = txt.replace("®", "")
    nombres = {re.sub(r"[   ]", "", n).rstrip(".,") for n in NOMBRE.findall(txt)}
    urls = set(URL.findall(txt))
    propres = {plie(p) for p in PROPRE.findall(txt)}
    propres = {p for p in propres if p not in BANALS}
    return {"nombres": nombres - {""}, "urls": urls, "noms propres": propres}


def version_git(chemin: str, ref: str):
    r = subprocess.run(["git", "-C", str(REPO), "show", f"{ref}:{chemin}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def controle_gras(ref: str) -> int:
    """Mode --gras : la seule chose autorisée à bouger, ce sont les marqueurs `**`.

    Déplacer une emphase est un geste éditorial (sur une fiche de sécurité, le gras
    doit tomber sur l'état d'accès, pas sur le nom du massif déjà porté par le badge).
    Mais c'est aussi l'occasion rêvée de « corriger » une phrase au passage. D'où ce
    contrôle brutal : texte débarrassé de ses `**`, avant et après, à l'identique.
    """
    pbs, controles = [], 0
    for f in sorted((REPO / ALERTES).glob("*.md")):
        rel = f"{ALERTES}/{f.name}"
        avant = version_git(rel, ref)
        if avant is None:
            continue
        apres = f.read_text(encoding="utf-8")
        if avant == apres:
            continue
        controles += 1
        nu_av, nu_ap = avant.replace("**", ""), apres.replace("**", "")
        if nu_av != nu_ap:
            pbs.append(f"⛔ {f.name}\n     le texte lui-même a changé, pas seulement "
                       f"l'emphase : ce passage ne doit déplacer que des `**`")
        # Compter sur la prose seule : le champ `statut:` porte parfois du gras hérité,
        # mais il n'est pas rendu sur le site et ne pèse donc sur aucune lecture.
        n_ap = sections(apres).count("**") // 2
        if n_ap > 1:
            pbs.append(f"⚠️  {f.name}\n     {n_ap} emphases dans la prose : "
                       f"une seule est attendue")
    for p in pbs:
        print(p)
    bloquants = sum(1 for p in pbs if p.startswith("⛔"))
    print(f"\n{controles} fiche(s) modifiée(s) vs {ref} — {bloquants} fiche(s) dont le "
          f"texte a bougé, {len(pbs) - bloquants} avertissement(s).")
    return 1 if bloquants else 0


def controle_digests(ref: str) -> int:
    """Mode --digests : un rapport daté peut changer de style, jamais de contenu.

    Les digests portent en plus une dépendance fonctionnelle : le site lit les clés
    entre accents graves du digest le plus récent pour décider quelles cartes portent
    la pastille « changé ». Une clé reformatée casse silencieusement cet affichage.
    """
    CLE = re.compile(r"`([^`]+\|[^`]+)`")
    TITRE = re.compile(r"^#{1,3} .*$", re.M)
    SEV = re.compile(r"\b(HAUTE|MOYENNE|INFO)\b")
    pbs, controles = [], 0
    for f in sorted((REPO / "livrables").glob("digest_*.md")):
        rel = f"livrables/{f.name}"
        av = version_git(rel, ref)
        if av is None:
            continue
        ap = f.read_text(encoding="utf-8")
        if av == ap:
            continue
        controles += 1
        for nom, motif in (("clés d'alerte", CLE), ("titres", TITRE), ("sévérités", SEV)):
            a, b = collections.Counter(motif.findall(av)), collections.Counter(motif.findall(ap))
            perdus = a - b
            if perdus:
                pbs.append(f"⛔ {f.name}\n     {nom} PERDU(S)/MODIFIÉ(S) : "
                           f"{', '.join(str(x)[:70] for x in list(perdus)[:6])}")
        fa, fp = faits(av), faits(ap)
        for famille in ("nombres", "urls"):
            perdus = fa[famille] - fp[famille]
            if perdus:
                pbs.append(f"⛔ {f.name}\n     {famille} PERDU(S) : "
                           f"{', '.join(sorted(perdus)[:10])}")
        reste = re.findall(r"\s[—–]|[—–]\s", ap)
        if reste:
            pbs.append(f"⚠️  {f.name}\n     {len(reste)} tiret(s) ponctuant(s) restant(s)")
    for p in pbs:
        print(p)
    bloquants = sum(1 for p in pbs if p.startswith("⛔"))
    print(f"\n{controles} digest(s) modifié(s) vs {ref} — {bloquants} perte(s), "
          f"{len(pbs) - bloquants} avertissement(s).")
    return 1 if bloquants else 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ref = args[0] if args else "HEAD"
    if "--gras" in sys.argv:
        return controle_gras(ref)
    if "--digests" in sys.argv:
        return controle_digests(ref)
    seuil = 30
    if "--seuil" in sys.argv:
        seuil = int(sys.argv[sys.argv.index("--seuil") + 1])

    fichiers = sorted((REPO / ALERTES).glob("*.md"))
    pbs, controles = [], 0
    for f in fichiers:
        rel = f"{ALERTES}/{f.name}"
        avant_txt = version_git(rel, ref)
        if avant_txt is None:
            continue                      # fiche nouvelle : rien à comparer
        apres_txt = f.read_text(encoding="utf-8")
        if avant_txt == apres_txt:
            continue
        controles += 1
        av, ap = sections(avant_txt), sections(apres_txt)
        fa, fp = faits(av), faits(ap)
        for famille in fa:
            perdus = fa[famille] - fp[famille]
            ajoutes = fp[famille] - fa[famille]
            if perdus:
                pbs.append(f"⛔ {f.name}\n     {famille} PERDU(S) : "
                           f"{', '.join(sorted(perdus)[:12])}")
            if ajoutes and famille != "noms propres":
                pbs.append(f"⛔ {f.name}\n     {famille} INVENTÉ(S) : "
                           f"{', '.join(sorted(ajoutes)[:12])}")
        if av and len(ap) < len(av) * (1 - seuil / 100):
            pct = round((1 - len(ap) / len(av)) * 100)
            pbs.append(f"⚠️  {f.name}\n     prose réduite de {pct}% "
                       f"({len(av)}→{len(ap)} car.) — vérifier qu'aucun constat n'a sauté")
        # Même critère que le build : seul le tiret PONCTUANT (espacé d'au moins un
        # côté) trahit l'écriture IA. Celui qui est collé entre deux mots appartient à
        # un nom propre ou à un intitulé de source, et le déformer serait un faux fait.
        reste = re.findall(r"\s[—–]|[—–]\s", ap)
        if reste:
            pbs.append(f"⚠️  {f.name}\n     {len(reste)} tiret(s) cadratin(s) "
                       f"restant(s) dans la prose")

    for p in pbs:
        print(p)
    bloquants = sum(1 for p in pbs if p.startswith("⛔"))
    print(f"\n{controles} fiche(s) modifiée(s) contrôlée(s) vs {ref} — "
          f"{bloquants} perte(s)/invention(s) de fait, "
          f"{len(pbs) - bloquants} avertissement(s).")
    return 1 if bloquants else 0


if __name__ == "__main__":
    sys.exit(main())
