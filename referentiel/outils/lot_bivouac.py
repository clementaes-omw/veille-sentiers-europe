#!/usr/bin/env python3
"""
Sélectionne le lot de fiches bivouac à revérifier cette semaine (veille estivale).

La base referentiel/bivouac.csv (96 fiches) n'était mise à jour que par ricochet, quand
une alerte « réglementation » touchait un espace déjà fiché. Or les règles de bivouac
bougent surtout en été (arrêtés saisonniers, quotas, restrictions feu) : d'où un lot
hebdomadaire, le dimanche du 1er juin au 30 septembre.

Priorité (déterministe, sans état à stocker — la rotation s'auto-entretient puisque
vérifier une fiche remet sa date_verif à aujourd'hui, ce qui la renvoie en fin de file) :
  1. date_verif la plus ancienne  → garantit que TOUTE la base finit par passer
  2. à date égale, statut HYPOTHESE d'abord (règle non confirmée : une info fausse = une
     amende pour le marcheur) — c'est ce qui les fait traiter en premier au démarrage
  3. puis les règles issues d'arrêtés (interdit / toléré) avant le droit commun
     (variable / autorisé), qui ne bouge quasiment jamais
  4. nom (départage stable)

La date_verif prime volontairement sur le statut : sinon une fiche qui RESTE HYPOTHESE
(source officielle introuvable) serait resélectionnée toutes les semaines et bloquerait la
rotation sur les 82 fiches confirmées.

Usage : python3 referentiel/outils/lot_bivouac.py [-n 12] [--tous]
"""
import argparse
import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CSV = ROOT / "referentiel" / "bivouac.csv"
COLS = ["pays", "zone", "nom", "type", "regle", "conditions", "feu", "sentiers",
        "source_url", "date_source", "date_verif", "statut", "notes"]
# les règles issues d'un arrêté d'espace protégé bougent ; le droit commun non
REGLE_MOUVANTE = {"interdit": 0, "tolere": 0, "autorise": 1, "variable": 1}
DEFAUT_LOT = 12          # ~8 semaines pour couvrir les 96 fiches, 2 tours par saison
SAISON = ((6, 1), (9, 30))   # 1er juin → 30 septembre


def charger():
    with CSV.open(encoding="utf-8") as f:
        lignes = list(csv.reader(f, delimiter=";"))
    return [dict(zip(COLS, r)) for r in lignes[1:] if len(r) >= 13 and r[0].strip()]


def tri(fiche):
    return (fiche["date_verif"],
            0 if fiche["statut"].upper().startswith("HYPO") else 1,
            REGLE_MOUVANTE.get(fiche["regle"], 1),
            fiche["nom"])


def en_saison(jour: date) -> bool:
    (m1, j1), (m2, j2) = SAISON
    return (m1, j1) <= (jour.month, jour.day) <= (m2, j2)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-n", type=int, default=DEFAUT_LOT, help="taille du lot")
    ap.add_argument("--tous", action="store_true", help="ignorer le filtre de saison")
    args = ap.parse_args()

    jour = date.today()
    if not args.tous and not en_saison(jour):
        print(f"Hors saison bivouac ({jour}) — pas de lot cette semaine "
              f"(veille active du 1er juin au 30 septembre). --tous pour forcer.")
        return 0

    fiches = sorted(charger(), key=tri)
    lot = fiches[:args.n]
    hypo = sum(1 for f in lot if f["statut"].upper().startswith("HYPO"))
    print(f"LOT BIVOUAC du {jour} — {len(lot)} fiches sur {len(fiches)} "
          f"({hypo} HYPOTHESE à confirmer en priorité)\n")
    for f in lot:
        marque = " ⚠HYPOTHESE" if f["statut"].upper().startswith("HYPO") else ""
        print(f"- [{f['pays']}] {f['nom']} — règle actuelle : {f['regle']}{marque}")
        print(f"  vérifiée le {f['date_verif']} · source : {f['source_url'] or '—'}")
    print("\nPour chaque fiche : relire la source, puis mettre à jour dans bivouac.csv "
          "date_verif (toujours), et conditions/feu/source_url/date_source/statut SI la "
          "règle a changé. Un changement réel → une ligne dans le digest du jour.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
