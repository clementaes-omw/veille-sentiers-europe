# Audit qualité du registre — 2026-08-13

65 alertes actives · 4 fiches avec au moins un constat · **0 bloquant(s)**, 4 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — « Portion concernée » parle du 02/08 alors que le suivi connaît la situation au 13/08 (11 j d'écart) — la mise à jour n'est pas arrivée jusqu'au texte affiché.
- **`incendie|Aude-Montseret-Corbieres|feu-fixe-100ha|2026-08-06`** — la validité annoncée s'arrête au 06/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|Lozere-Massegros-Causses-Gorges|feu-fixe-153ha|2026-08-09`** — la validité annoncée s'arrête au 10/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** — alerte rouge appuyée sur une source datée du 29/07 (15 j) — retrouver une publication récente ou dégrader la sévérité.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

