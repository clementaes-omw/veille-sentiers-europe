# Audit qualité du registre — 2026-09-03

76 alertes actives · 8 fiches avec au moins un constat · **1 bloquant(s)**, 5 alerte(s), 2 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⛔ Bloquants — à corriger avant le prochain run

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — vérifiée il y a 6 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.

## ⚠️ À traiter

- **`fermeture|Drome-Omblese|sentiers-pas-du-gouillat-pas-de-comberoufle|2026-07-07`** — la validité annoncée s'arrête au 31/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 18/08 (16 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (13 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`** — vérifiée il y a 15 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|HauteGaronne-31|vigilance-rouge-camping-sauvage-interdit|2026-07-09`** — la validité annoncée s'arrête au 09/07/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.

## · Dette de forme

- **`risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18`** — « Zone (détails) » contient encore du jargon de veille (recherche ciblee) au lieu de l'état du terrain.
- **`risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`** — « Zone (détails) » contient encore du jargon de veille (recherche ciblee) au lieu de l'état du terrain.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

