# Audit qualité du registre — 2026-09-18

96 alertes actives · 16 fiches avec au moins un constat · **0 bloquant(s)**, 16 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08`** — jamais revérifiée depuis sa détection il y a 10 j.
- **`fermeture|Drome-Omblese|sentiers-pas-du-gouillat-pas-de-comberoufle|2026-07-07`** — la validité annoncée s'arrête au 15/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — alerte rouge appuyée sur une source datée du 01/09 (17 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 31/08 (18 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (28 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`** — la validité annoncée s'arrête au 15/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — alerte rouge appuyée sur une source datée du 24/08 (25 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`** — « Portion concernée » parle du 10/09 alors que le suivi connaît la situation au 18/09 (8 j d'écart) — la mise à jour n'est pas arrivée jusqu'au texte affiché.
- **`reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.
