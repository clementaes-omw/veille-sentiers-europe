# Audit qualité du registre — 2026-09-14

89 alertes actives · 9 fiches avec au moins un constat · **0 bloquant(s)**, 8 alerte(s), 2 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — alerte rouge appuyée sur une source datée du 27/08 (18 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — alerte rouge appuyée sur une source datée du 01/09 (13 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — vérifiée il y a 3 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 31/08 (14 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (24 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|ES-NAV-Roncal-Urzainki|feu-longue-duree-Pena-Gazpar|2026-08-14`** — la validité annoncée s'arrête au 04/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — alerte rouge appuyée sur une source datée du 24/08 (21 j) — retrouver une publication récente ou dégrader la sévérité.
- **`risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01`** — « Portion concernée » parle du 03/09 alors que le suivi connaît la situation au 14/09 (11 j d'écart) — la mise à jour n'est pas arrivée jusqu'au texte affiché.

## · Dette de forme

- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — « Zone (détails) » contient encore du jargon de veille (en autonome) au lieu de l'état du terrain.
- **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`** — « Zone (détails) » contient encore du jargon de veille (indexation) au lieu de l'état du terrain.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

