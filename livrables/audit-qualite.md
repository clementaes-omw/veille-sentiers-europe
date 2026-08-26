# Audit qualité du registre — 2026-08-26

74 alertes actives · 5 fiches avec au moins un constat · **1 bloquant(s)**, 4 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⛔ Bloquants — à corriger avant le prochain run

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — vérifiée il y a 12 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.

## ⚠️ À traiter

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — vérifiée il y a 20 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — alerte rouge appuyée sur une source datée du 12/08 (14 j) — retrouver une publication récente ou dégrader la sévérité.
- **`refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** — alerte rouge appuyée sur une source datée du 29/07 (28 j) — retrouver une publication récente ou dégrader la sévérité.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

