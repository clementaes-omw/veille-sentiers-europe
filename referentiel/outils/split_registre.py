#!/usr/bin/env python3
"""
Migration : registre monolithique → un fichier par alerte.

AVANT : livrables/alertes-actives.md = 1 fichier (~122 Ko) contenant
        - un tableau markdown de 12 colonnes (une ligne = une alerte)
        - 4 sections d'annexes (mémoire interne de l'agent)
APRÈS : livrables/alertes/<slug>.md   = 1 fichier par alerte (~1,5 Ko)
        livrables/memoire-interne/*.md = 1 fichier par section d'annexe

Pourquoi : l'agent de veille réécrit le fichier en entier à chaque run (les outils
GitHub remplacent le fichier, pas de patch ligne à ligne). Sur 122 Ko il ne peut pas
reproduire le texte verbatim → il résume → perte de contenu (incident 2026-07-25 :
125 Ko → 27 Ko). Des fichiers de 1,5 Ko se réécrivent sans perte.

Sans dépendance. Rejouable. Usage : python3 referentiel/outils/split_registre.py
"""
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
LIVRABLES = ROOT / "livrables"
MONOLITHE = LIVRABLES / "alertes-actives.md"
DEST_ALERTES = LIVRABLES / "alertes"
DEST_MEMOIRE = LIVRABLES / "memoire-interne"

# ordre des colonnes du tableau historique → noms de champs internes
COLS = ["cle", "type", "portion", "alternative", "zone", "itin", "sev",
        "validite", "detection", "verif", "source", "statut"]
# champs longs → rendus en sections markdown (le contenu riche à protéger)
SECTIONS = [("portion", "Portion concernée"), ("alternative", "Alternative"),
            ("zone", "Zone (détails)"), ("source", "Source")]
# champs courts → front-matter (une ligne chacun)
ENTETE = ["cle", "type", "itin", "sev", "validite", "detection", "verif", "statut"]

SEP_RE = re.compile(r"^:?-{2,}:?$")


def split_row(row: str):
    row = row.strip().strip("|").replace("\\|", "\x00")
    return [c.strip().replace("\x00", "|") for c in row.split("|")]


def slugify(cle: str) -> str:
    """Clé `type|zone|objet|date` → nom de fichier stable, ASCII, lisible."""
    parts = [p.strip() for p in cle.split("|")]
    out = []
    for p in parts:
        p = unicodedata.normalize("NFD", p)
        p = "".join(ch for ch in p if not unicodedata.combining(ch))
        p = re.sub(r"[^A-Za-z0-9]+", "-", p).strip("-").lower()
        out.append(p)
    return "--".join(filter(None, out))[:120]


def rendre_alerte(champs: dict, ordre: int) -> str:
    """Fichier d'une alerte : front-matter (champs courts) + sections (texte riche)."""
    lignes = ["---"]
    for k in ENTETE:
        lignes.append(f"{k}: {champs.get(k, '').strip()}")
    lignes.append(f"ordre: {ordre}")
    lignes.append("---")
    for k, titre in SECTIONS:
        lignes.append("")
        lignes.append(f"## {titre}")
        lignes.append("")
        lignes.append(champs.get(k, "").strip())
    return "\n".join(lignes).rstrip() + "\n"


def main():
    if not MONOLITHE.exists():
        print(f"déjà migré (ou introuvable) : {MONOLITHE}", file=sys.stderr)
        return 1
    md = MONOLITHE.read_text(encoding="utf-8")
    lignes = md.splitlines()

    DEST_ALERTES.mkdir(exist_ok=True)
    DEST_MEMOIRE.mkdir(exist_ok=True)

    # ---- 1) tableau → un fichier par alerte
    entete_vue = False
    ordre = 0
    ecrits = []
    for ligne in lignes:
        s = ligne.strip()
        if not s.startswith("|"):
            continue
        cells = split_row(s)
        if all(SEP_RE.match(c) for c in cells if c):
            continue
        if not entete_vue:
            entete_vue = True          # ligne d'en-tête
            continue
        if len(cells) < 12:
            print(f"  ⚠ ligne à {len(cells)} colonnes ignorée : {s[:70]}", file=sys.stderr)
            continue
        champs = dict(zip(COLS, cells))
        ordre += 1
        nom = slugify(champs["cle"]) + ".md"
        (DEST_ALERTES / nom).write_text(rendre_alerte(champs, ordre), encoding="utf-8")
        ecrits.append(nom)

    # ---- 2) annexes → un fichier par section (mémoire interne, jamais rendue sur le site)
    idx = [i for i, l in enumerate(lignes) if l.startswith("## ")]
    memo = []
    for n, deb in enumerate(idx):
        fin = idx[n + 1] if n + 1 < len(idx) else len(lignes)
        titre = lignes[deb][3:].strip()
        corps = "\n".join(lignes[deb:fin]).rstrip() + "\n"
        nom = slugify(titre) + ".md"
        (DEST_MEMOIRE / nom).write_text(corps, encoding="utf-8")
        memo.append(nom)

    # ---- 3) préambule du registre conservé comme README du dossier
    fin_preambule = next((i for i, l in enumerate(lignes) if l.startswith("|")), 0)
    (DEST_ALERTES / "README.md").write_text(
        "\n".join(lignes[:fin_preambule]).rstrip()
        + "\n\nUne alerte = un fichier `<clé slugifiée>.md` dans ce dossier.\n"
          "Front-matter = champs courts, sections `##` = texte riche (portion, alternative,\n"
          "détails, sources). Ne JAMAIS réécrire tout le dossier : un run ne touche que les\n"
          "fichiers des alertes nouvelles ou modifiées.\n", encoding="utf-8")

    MONOLITHE.unlink()
    print(f"OK — {len(ecrits)} alertes → {DEST_ALERTES.relative_to(ROOT)}/")
    print(f"     {len(memo)} sections de mémoire interne → {DEST_MEMOIRE.relative_to(ROOT)}/")
    print(f"     monolithe supprimé ({len(md)} octets) ; historique conservé par git")
    return 0


if __name__ == "__main__":
    sys.exit(main())
