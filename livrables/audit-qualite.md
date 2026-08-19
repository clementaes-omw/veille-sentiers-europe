# Audit qualité du registre — 2026-08-19

73 alertes actives · 8 fiches avec au moins un constat · **0 bloquant(s)**, 8 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26`** — jamais revérifiée depuis sa détection il y a 8 j.
- **`fermeture|CH-Europaweg-Randa-Zermatt|fermeture-deviation-seg-27.3|2024-07-03`** — jamais revérifiée depuis sa détection il y a 8 j.
- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — vérifiée il y a 5 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.
- **`infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15`** — la validité annoncée s'arrête au 14/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`** — la validité annoncée s'arrête au 15/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** — alerte rouge appuyée sur une source datée du 29/07 (21 j) — retrouver une publication récente ou dégrader la sévérité.
- **`risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`** — alerte rouge appuyée sur une source datée du 05/08 (14 j) — retrouver une publication récente ou dégrader la sévérité.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.
