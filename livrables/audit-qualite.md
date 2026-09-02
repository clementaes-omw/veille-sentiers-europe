# Audit qualité du registre — 2026-09-02

76 alertes actives · 4 fiches avec au moins un constat · **0 bloquant(s)**, 4 alerte(s), 0 info(s).

Carte : **4 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — vérifiée il y a 5 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 18/08 (15 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (12 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## 🗺 Cohérence carte / registre

### ⛔ Alertes actives invisibles sur la carte / compte incohérent

- **`(carte)`** — regroupement incohérent : 73 alerte(s) réparties sur 35 marqueur(s) pour 76 active(s) — 3 alerte(s) hors carte.
- **`fermeture|Ille-et-Vilaine-Dinard|GR34-Port-Vicomte-Port-Bernard|2026-04-20`** — zone « Ille-et-Vilaine-Dinard » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`fermeture|Ille-et-Vilaine-Saint-Briac-sur-Mer|GR34-Petite-Salinette-Grande-Salinette|2026-02-09`** — zone « Ille-et-Vilaine-Saint-Briac-sur-Mer » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`fermeture|Loire-Atlantique-Piriac-sur-Mer|GR34-Pointe-du-Castelli|2026-02-22`** — zone « Loire-Atlantique-Piriac-sur-Mer » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.

