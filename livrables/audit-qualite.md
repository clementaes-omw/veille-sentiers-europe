# Audit qualité du registre — 2026-09-14

90 alertes actives · 13 fiches avec au moins un constat · **0 bloquant(s)**, 11 alerte(s), 4 info(s).

Carte : **2 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — vérifiée il y a 15 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`** — alerte rouge appuyée sur une source datée du 26/08 (19 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — alerte rouge appuyée sur une source datée du 01/09 (13 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — vérifiée il y a 3 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04`** — jamais revérifiée depuis sa détection il y a 9 j.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 31/08 (14 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (24 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|ES-NAV-Roncal-Urzainki|feu-longue-duree-Pena-Gazpar|2026-08-14`** — la validité annoncée s'arrête au 04/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — alerte rouge appuyée sur une source datée du 24/08 (21 j) — retrouver une publication récente ou dégrader la sévérité.
- **`risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01`** — vérifiée il y a 3 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.
- **`risque-feu|Herault-34|fermetures-massifs-quotidiennes|2026-07-02`** — vérifiée il y a 3 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.

## · Dette de forme

- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — « Zone (détails) » contient encore du jargon de veille (recherche ciblee) au lieu de l'état du terrain.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — « Zone (détails) » contient encore du jargon de veille (en autonome) au lieu de l'état du terrain.
- **`incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`** — « Zone (détails) » contient encore du jargon de veille (recherche ciblee) au lieu de l'état du terrain.
- **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`** — « Zone (détails) » contient encore du jargon de veille (indexation) au lieu de l'état du terrain.

## 🗺 Cohérence carte / registre

### ⛔ Alertes actives invisibles sur la carte / compte incohérent

- **`(carte)`** — regroupement incohérent : 89 alerte(s) réparties sur 38 marqueur(s) pour 90 active(s) — 1 alerte(s) hors carte.
- **`incendie|ES-NAV-Roncal-Urzainki|feu-longue-duree-Pena-Gazpar|2026-08-14`** — zone « ES-NAV-Roncal-Urzainki » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.

