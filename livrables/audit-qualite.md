# Audit qualité du registre — 2026-09-24

103 alertes actives · 29 fiches avec au moins un constat · **1 bloquant(s)**, 29 alerte(s), 0 info(s).

Carte : **6 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⛔ Bloquants — à corriger avant le prochain run

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — vérifiée il y a 6 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.

## ⚠️ À traiter

- **`conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25`** — jamais revérifiée depuis sa détection il y a 12 j.
- **`eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`** — jamais revérifiée depuis sa détection il y a 12 j.
- **`fermeture|CH-EST-Frutigen|Kander-Uferweg-impraticable|2026-08-17`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|CH-EST-Frutigen|Kander-Uferweg-impraticable|2026-08-17`** — la validité annoncée s'arrête au 21/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08`** — jamais revérifiée depuis sa détection il y a 16 j.
- **`fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|CH-Vaud-Sainte-Croix-Baulmes|Gorges-Covatannaz-travaux|2026-08-17`** — la validité annoncée s'arrête au 18/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — alerte rouge appuyée sur une source datée du 01/09 (23 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10`** — jamais revérifiée depuis sa détection il y a 12 j.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 31/08 (24 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (34 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`** — la validité annoncée s'arrête au 18/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|ES-GAL-Quiroga|feu-pacios-da-serra-420ha|2026-09-15`** — la validité annoncée s'arrête au 18/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — alerte rouge appuyée sur une source datée du 24/08 (31 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|PT-CENTRO-SUL-Arganil-Piodao|feu-murganheira-evacuation-aldeias-historicas|2026-09-19`** — la validité annoncée s'arrête au 20/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`** — alerte rouge appuyée sur une source datée du 10/09 (14 j) — retrouver une publication récente ou dégrader la sévérité.
- **`refuge|IT-Dolomites-Friuli-Cimoliana|bivacco-gervasutti-amianto-inagibile|2026-09-09`** — jamais revérifiée depuis sa détection il y a 10 j.
- **`reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|Pierrefiques-76|déviation|2025-05-18`** — la validité annoncée s'arrête au 18/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** — la validité annoncée s'arrête au 18/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08`** — vérifiée il y a 19 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## 🗺 Cohérence carte / registre

### ⛔ Alertes actives invisibles sur la carte / compte incohérent

- **`(carte)`** — regroupement incohérent : 98 alerte(s) réparties sur 41 marqueur(s) pour 103 active(s) — 5 alerte(s) hors carte.
- **`fermeture|Finistere-Plomodiern|GR34-Ty-Mark-Kervijen|2026-09-18`** — zone « Finistere-Plomodiern » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`fermeture|UK-Cornwall-Newquay|SWCP-North-Pier-glissement|2026-02`** — zone « UK-Cornwall-Newquay » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`fermeture|UK-Cornwall-Tintagel|SWCP-effondrement-inondation|2025-12-18`** — zone « UK-Cornwall-Tintagel » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`fermeture|UK-Cornwall-Tregonhawke-Whitsand-Bay|SWCP-instabilite-cotiere|2026-03`** — zone « UK-Cornwall-Tregonhawke-Whitsand-Bay » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`reroutage|UK-Cornwall-St-Martins-Millendreath|SWCP-deviation-glissement|2026-02`** — zone « UK-Cornwall-St-Martins-Millendreath » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.

