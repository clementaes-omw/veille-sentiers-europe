# Audit qualité du registre — 2026-10-09

105 alertes actives · 69 fiches avec au moins un constat · **8 bloquant(s)**, 74 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⛔ Bloquants — à corriger avant le prochain run

- **`fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`** — vérifiée il y a 34 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07`** — vérifiée il y a 34 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10`** — vérifiée il y a 34 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`** — vérifiée il y a 34 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10`** — vérifiée il y a 34 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30`** — vérifiée il y a 34 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|Var-83|fermetures-massifs-quotidiennes|2026-07-08`** — vérifiée il y a 9 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.
- **`terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08`** — vérifiée il y a 34 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## ⚠️ À traiter

- **`conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25`** — vérifiée il y a 27 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25`** — jamais revérifiée depuis sa détection il y a 27 j.
- **`conditions|Écrins-GR54|enneigement-conditions|2026-06-24`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`crue|Écrins-GR54|sentiers-refuges-endommages-crues-27-28-aout|2026-08-27`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`** — vérifiée il y a 27 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`** — jamais revérifiée depuis sa détection il y a 27 j.
- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — alerte rouge appuyée sur une source datée du 28/09 (11 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08`** — jamais revérifiée depuis sa détection il y a 31 j.
- **`fermeture|CH-Europaweg-Randa-Zermatt|fermeture-deviation-seg-27.3|2024-07-03`** — vérifiée il y a 24 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|CH-Valais-Arolla|Bertol-Haut-Glacier-deviation|2026-05-11`** — vérifiée il y a 24 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|CH-Valais-Arolla|Pas-de-Chevre-chemin-impraticable|2026-08-24`** — vérifiée il y a 24 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|Cotes-Armor-Plerin|GR34-Port-Martin-Les-Rosaires|2026-07-20`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|ES-AND-Malaga-DesfiladeroGaitanes|senderos-Los-Embalses-Gaitanejo-fermes-risque-desembalse|2026-02-12`** — la validité annoncée s'arrête au 12/02/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`fermeture|Finistere-Plomodiern|GR34-Ty-Mark-Kervijen|2026-09-18`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|Finistere-Plomodiern|GR34-Ty-Mark-Kervijen|2026-09-18`** — jamais revérifiée depuis sa détection il y a 16 j.
- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — la validité annoncée s'arrête au 04/10/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04`** — vérifiée il y a 25 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10`** — vérifiée il y a 27 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10`** — jamais revérifiée depuis sa détection il y a 27 j.
- **`fermeture|Ille-et-Vilaine-Dinard|GR34-Port-Vicomte-Port-Bernard|2026-04-20`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|Ille-et-Vilaine-Saint-Briac-sur-Mer|GR34-Petite-Salinette-Grande-Salinette|2026-02-09`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|Loire-Atlantique-Piriac-sur-Mer|GR34-Pointe-du-Castelli|2026-02-22`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|SI-Julijske-Alpe|severni-pristop-Bavski-Grintavec-Kanja-podor|2026-09-17`** — vérifiée il y a 15 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|SI-Julijske-Alpe|severni-pristop-Bavski-Grintavec-Kanja-podor|2026-09-17`** — jamais revérifiée depuis sa détection il y a 15 j.
- **`fermeture|TMB-CH-Orsieres|fermeture-deviation-seg-6.35|2026-07-11`** — vérifiée il y a 24 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|UK-Cornwall-Newquay|SWCP-North-Pier-glissement|2026-02`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|UK-Cornwall-Newquay|SWCP-North-Pier-glissement|2026-02`** — jamais revérifiée depuis sa détection il y a 16 j.
- **`fermeture|UK-Cornwall-Tintagel|SWCP-effondrement-inondation|2025-12-18`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|UK-Cornwall-Tintagel|SWCP-effondrement-inondation|2025-12-18`** — jamais revérifiée depuis sa détection il y a 16 j.
- **`fermeture|UK-Cornwall-Tregonhawke-Whitsand-Bay|SWCP-instabilite-cotiere|2026-03`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|UK-Cornwall-Tregonhawke-Whitsand-Bay|SWCP-instabilite-cotiere|2026-03`** — jamais revérifiée depuis sa détection il y a 16 j.
- **`fermeture|UK-Devon-Branscombe|SWCP-Under-Hooken-Branscombe-Beer|2026-03`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|VS-Orsieres-ValFerret|Saleinaz-cabane-eboulement|2026-07-29`** — vérifiée il y a 24 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|AT-Vorarlberg-Silvretta|coulee-boue-sentiers-fermes|2026-07-12`** — vérifiée il y a 15 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|Ardeche-Dompnac|feu-40ha-Valgorge|2026-09-26`** — la validité annoncée s'arrête au 27/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 31/08 (39 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Ariege-Mijanes-Donezan|feu-station-Donezan|2026-09-25`** — la validité annoncée s'arrête au 30/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|Ariege-Saurat|Rocher-de-Batail-GRP-fermes|2026-08-16`** — la validité annoncée s'arrête au 01/10/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`** — vérifiée il y a 29 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|Drome-Bellegarde-en-Diois|feu-massif-Claps-400ha|2026-08-03`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (49 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|ES-AND-Igualeja-Parauta|feu-Serrania-de-Ronda-Sierra-de-las-Nieves|2026-09-27`** — la validité annoncée s'arrête au 28/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`** — vérifiée il y a 29 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — « Portion concernée » parle du 27/09 alors que le suivi connaît la situation au 06/10 (9 j d'écart) — la mise à jour n'est pas arrivée jusqu'au texte affiché.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — alerte rouge appuyée sur une source datée du 24/08 (46 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|HautesPyrenees-Bareges|Pic-Lurtet-Glere-piste-fermee|2026-07-08`** — vérifiée il y a 25 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|PT-CENTRO-SUL-Arganil-Piodao|feu-murganheira-evacuation-aldeias-historicas|2026-09-19`** — la validité annoncée s'arrête au 27/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|PT-CENTRO-SUL-Odemira-Saboia|feu-nave-redonda|2026-09-24`** — la validité annoncée s'arrête au 25/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`** — alerte rouge appuyée sur une source datée du 10/09 (29 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`infrastructure|SCAND-SE-Norrbotten-Padjelantaleden|pont-Mielladno-retire|2026-04`** — jamais revérifiée depuis sa détection il y a 16 j.
- **`refuge|IT-Dolomites-Friuli-Cimoliana|bivacco-gervasutti-amianto-inagibile|2026-09-09`** — vérifiée il y a 25 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`refuge|IT-Dolomites-Friuli-Cimoliana|bivacco-gervasutti-amianto-inagibile|2026-09-09`** — jamais revérifiée depuis sa détection il y a 25 j.
- **`reglementation|ES-GAL|periode-haut-risque-incendie-prolongee|2026-09-24`** — jamais revérifiée depuis sa détection il y a 11 j.
- **`reroutage|Aspe-64-Chemin-Mature|eboulement-devie-col-Arras|2026-01-05`** — vérifiée il y a 25 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|GR21-Loges-Bénouville|glissement-fermeture|2026-02-17`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|GR34-Finistère|fermetures-érosion-2026|2026-S1`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|GR34-rade-de-Brest|nouveau-tracé-officiel|2026-05-28`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|Pierrefiques-76|déviation|2025-05-18`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|Pierrefiques-76|déviation|2025-05-18`** — la validité annoncée s'arrête au 18/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`reroutage|SI-Julijske-Alpe|deviation-Trnovo-Srpenica|2025-10`** — vérifiée il y a 22 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|SK-Tatras-Krivan|fermeture-Tri-studnicky|2026`** — vérifiée il y a 15 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|UK-Cornwall-St-Martins-Millendreath|SWCP-deviation-glissement|2026-02`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|UK-Cornwall-St-Martins-Millendreath|SWCP-deviation-glissement|2026-02`** — jamais revérifiée depuis sa détection il y a 16 j.
- **`reroutage|UK-Devon-Shaldon|SWCP-The-Ness-deviation|2026-04`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28`** — vérifiée il y a 15 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28`** — la validité annoncée s'arrête au 30/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`réglementation|PN-Pyrénées|baignade-lacs-interdite|2026-06-15`** — vérifiée il y a 25 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`réglementation|Écrins|bivouac|2026-06-19`** — vérifiée il y a 16 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

