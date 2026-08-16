# Audit qualité du registre — 2026-08-16

69 alertes actives · 3 fiches avec au moins un constat · **0 bloquant(s)**, 3 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** — alerte rouge appuyée sur une source datée du 29/07 (18 j) — retrouver une publication récente ou dégrader la sévérité.
- **`risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`** — alerte rouge appuyée sur une source datée du 05/08 (11 j) — retrouver une publication récente ou dégrader la sévérité.
- **`risque-feu|Hérault-34|fermetures-massifs-quotidiennes|2026-07-02`** — « Portion concernée » parle du 07/08 alors que le suivi connaît la situation au 16/08 (9 j d'écart) — la mise à jour n'est pas arrivée jusqu'au texte affiché.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.
