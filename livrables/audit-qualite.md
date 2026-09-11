# Audit qualité du registre — 2026-09-11

84 alertes actives · 13 fiches avec au moins un constat · **0 bloquant(s)**, 12 alerte(s), 1 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`** — alerte rouge appuyée sur une source datée du 26/08 (16 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|Ille-et-Vilaine-Dinard|GR34-Port-Vicomte-Port-Bernard|2026-04-20`** — jamais revérifiée depuis sa détection il y a 9 j.
- **`fermeture|Ille-et-Vilaine-Saint-Briac-sur-Mer|GR34-Petite-Salinette-Grande-Salinette|2026-02-09`** — jamais revérifiée depuis sa détection il y a 9 j.
- **`fermeture|Loire-Atlantique-Piriac-sur-Mer|GR34-Pointe-du-Castelli|2026-02-22`** — jamais revérifiée depuis sa détection il y a 9 j.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 31/08 (11 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (21 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|FR-34-11-Puilaurens-Axat|feu-150ha-Camperie|2026-09-04`** — la validité annoncée s'arrête au 08/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|FR-84-26-07-LesVans-Malbosc|feu-50ha|2026-09-03`** — la validité annoncée s'arrête au 07/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — alerte rouge appuyée sur une source datée du 24/08 (18 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`** — la validité annoncée s'arrête au 02/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** — la validité annoncée s'arrête au 08/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`** — alerte rouge appuyée sur une source datée du 28/08 (14 j) — retrouver une publication récente ou dégrader la sévérité.

## · Dette de forme

- **`risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`** — « Zone (détails) » contient encore du jargon de veille (en autonome) au lieu de l'état du terrain.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

