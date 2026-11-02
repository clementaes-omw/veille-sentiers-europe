# Verdict qualité du registre, 2026-11-02

Vérificateur : agents/verificateur-alertes.md. Entrée : livrables/audit-qualite.md (118 constats, 67 bloquants, 95 fiches distinctes citées). Aucune fiche créée, supprimée ni clôturée. La fiche `reglementation|ES-NAV-Rio-Ara-Roncesvalles|...|2026-11-01` (créée aujourd'hui) n'a pas été touchée. Aucun script ni `site/build_site.py` modifié, rien commité.

## Résultat en chiffres

- Fiches contrôlées : 95.
- Fiches corrigées : 16 (10 revérifiées sur source officielle, 6 réécritures de texte), voir ci-dessous.
- Fiches clôturées : 0 (voir « Pertinence » : recommandations seulement, sans source nouvelle).
- Fiches renvoyées « à traiter au prochain run » : 86 (champ `statut:`, liste en fin de document).
- Bloquants restants après correction : 66 sur 67 (tous des défauts de FRAÎCHEUR, qui exigent une source nouvelle). Le seul bloquant levé est `fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26`. Le défaut de concordance (HautesAlpes-BoisNoir) est levé.
- `python3 site/build_site.py` : OK (QA passée). `python3 site/verif_faits.py` : 0 perte, 0 invention.

## PASS / FAIL par contrôle

| Contrôle | Résultat |
| --- | --- |
| 1. Fraîcheur | FAIL sur 86 fiches (10 fiches suisses corrigées). Cause commune : dernière vérification du 05/09 au 28/09 pour des restrictions à seuil de 12 jours (2 jours pour Samaria et Var-83, 4 jours pour les alertes rouges). |
| 2. Concordance interne | 1 FAIL corrigé (HautesAlpes-BoisNoir). Plus aucun écart portion/suivi détecté. |
| 3. Honnêteté sur ce qu'on ne sait pas | PASS sur le périmètre audité. Les fiches sans acte retrouvé le disent déjà au lecteur. |
| 4. Pertinence | Recommandations de clôture ci-dessous, non appliquées. |
| 5. Sévérité juste | PASS. Aucune alerte rouge adossée à « à confirmer » ou « probable » : la règle des 14 jours ne s'applique pas. Les cinq alertes rouges reposent sur un arrêté daté. Recommandation pour HautesAlpes-BoisNoir ci-dessous. |
| 6. Ton | 3 fiches reformulées (jargon dans « Zone (détails) »). Aucun tiret cadratin ni emoji dans les champs publics des fiches citées (les tirets restants sont dans le frontmatter ou des composés sans espace, tolérés). |
| 7. Source vivante (alertes rouges) | FAIL partiel, voir détail. |

## Corrections appliquées

### Revérifiées sur source officielle (statut et `verif:` mis à jour au 2026-11-02)

Source : flux data.geo.admin.ch (couche `ch.astra.wanderland-sperrungen_umleitungen`, fichier daté du 01/11/2026, téléchargé le 02/11). Chaque identifiant cité par la fiche est toujours présent avec les mêmes dates de début et de fin ; aucune levée.

- `fermeture--ch-est-frutigen--kander-uferweg-impraticable--2026-08-17`
- `fermeture--ch-est-kandersteg--spitze-stei-deviation-seg-1-13--2023-05-08`
- `fermeture--ch-est-trubbach--fermeture-deviation-seg-1-1--2026-05-26`
- `fermeture--ch-europaweg-randa-zermatt--fermeture-deviation-seg-27-3--2024-07-03`
- `fermeture--ch-valais-arolla--bertol-haut-glacier-deviation--2026-05-11`
- `fermeture--ch-valais-arolla--pas-de-chevre-chemin-impraticable--2026-08-24`
- `fermeture--ch-valais-randa--alte-kantonsstrasse-guggigrabe-gross-kastel-glacier--2026-06-27`
- `fermeture--ch-vaud-sainte-croix-baulmes--gorges-covatannaz-travaux--2026-08-17`
- `fermeture--tmb-ch-orsieres--fermeture-deviation-seg-6-35--2026-07-11`
- `fermeture--vs-orsieres-valferret--saleinaz-cabane-eboulement--2026-07-29`

### Réécritures sans création de fait

- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` : « Portion concernée » ramenée de l'état du 27/09 à celui du 06/10 déjà connu du suivi (arrêté municipal du 15/08 toujours présenté comme en vigueur, aucune levée) ; entrée « MAJ 06/10 » ajoutée à la chronologie.
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`, `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`, `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` : jargon de veille remplacé (« run précédent », « dernier passage ») dans « Zone (détails) ».
- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` : « ce 2 octobre » devenu « au 2 octobre » dans la portion (la phrase datait un état passé comme présent).
- `fermeture|ES-AND-Malaga-DesfiladeroGaitanes|senderos-Los-Embalses-Gaitanejo-fermes-risque-desembalse|2026-02-12` : `validite:` reformulée, la date du 12/02/2026 est le début de la fermeture, pas une échéance (avis « hasta nuevo aviso », sans date de fin).

## Source vivante, alertes rouges (contrôle HTTP du 02/11)

- `incendie|HautesAlpes-BoisNoir|...|2026-07-19` : FAIL bloquant sur la source principale. `ville-argentiere.fr/feu-bois-noir-informations` et `paysdesecrins.com/vigileance-feu-en-cours` répondent 404. La page `ville-argentiere.fr/vie-pratique/.../infos-feu-du-bois-noir` répond mais son texte lisible ne mentionne pas l'arrêté. Communiqué de la préfecture (hautes-alpes.gouv.fr) accessible. Action ajoutée au `statut:`. Recommandation : si l'arrêté consultable n'est pas retrouvé au prochain run, passer en MOYENNE avec la mention « aucun arrêté consultable n'est publié ».
- `incendie|Ariege-Bordes-Uchentein|...|2026-07-10` : PASS. Les deux arrêtés préfectoraux en PDF répondent. Un seul lien secondaire (pyreneesfm.com) est mort.
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` : PASS partiel. La page de la mairie de Die sur l'interdiction d'accès répond ; un lien secondaire de la mairie est en 404 et la page drome.gouv.fr ne répond pas.
- `incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02` : PASS (sources de presse en ligne). Dernière source datée du 10/09 : à rafraîchir.
- `fermeture|DE-Sachsen-SaechsischeSchweiz|...|2026-08-01` : PASS (sources du Nationalpark en ligne ; fiche vérifiée aujourd'hui).

## Pertinence (recommandations, non appliquées)

Clôture à envisager dès que le prochain run confirme l'état, car la fiche elle-même écrit qu'aucune restriction n'est en vigueur ou que le feu est éteint :
- `incendie|Aude-Montseret-Corbieres|feu-fixe-100ha|2026-08-06`, `incendie|Lozere-La-Bastide-Puylaurent|feu-252ha|2026-08-19`, `incendie|Corse-Calenzana|feu-Montegrosso-64ha|2026-08-27` : feu fixé, aucune restriction en vigueur.
- `incendie|Drome-Bellegarde-en-Diois|feu-massif-Claps-400ha|2026-08-03`, `incendie|FR-84-26-07-LesVans-Malbosc|feu-50ha|2026-09-03` : même constat.
- `incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16` : incendie déclaré éteint le 04/09 ; ne garder que si la fermeture du GR®167 est confirmée par source.
- `incendie|HautesPyrenees-Bareges|Pic-Lurtet-Glere-piste-fermee|2026-07-08` : feu éteint, seule la piste de la Glère était en cause.
- `risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28` : restrictions échues au 30/09, aucune fermeture documentée.
- `reroutage|GR34-rade-de-Brest|nouveau-tracé-officiel|2026-05-28` : reroutage pérenne devenu tracé officiel, ne relève plus de l'alerte.
- `reroutage|Pierrefiques-76|déviation|2025-05-18` : travaux annoncés jusqu'au 18/09, échéance dépassée.
- Validités échues de feux mineurs (Ardèche-Dompnac, Ariege-Mijanes-Donezan, ES-AND-Igualeja-Parauta, PT-Arganil-Piodao, PT-Odemira-Saboia) : feux maîtrisés fin septembre sans fermeture de sentier documentée ; clôturer si aucune restriction n'apparaît au prochain relevé.
- Aucune dégradation ni remontée de sévérité à appliquer.

## À traiter au prochain run (86 fiches)

Chaque fiche porte dans son `statut:` une ligne « À TRAITER AU PROCHAIN RUN » avec l'action précise (source à relire, puis levée, prolongation ou clôture). Ces zones entrent en escalade au périmètre du run suivant. Les cinq alertes rouges (Bordes-Uchentein, Drome-Justin-Die, HautesAlpes-BoisNoir, Etsaut, et la fiche saxonne revérifiée aujourd'hui) sont à traiter en premier ; Samaria et Var-83 se rattachent à la source du jour.

- `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25`
- `conditions|Écrins-GR54|enneigement-conditions|2026-06-24`
- `crue|Écrins-GR54|sentiers-refuges-endommages-crues-27-28-aout|2026-08-27`
- `eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`
- `fermeture|Cotes-Armor-Plerin|GR34-Port-Martin-Les-Rosaires|2026-07-20`
- `fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06`
- `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`
- `fermeture|ES-AND-Malaga-DesfiladeroGaitanes|senderos-Los-Embalses-Gaitanejo-fermes-risque-desembalse|2026-02-12`
- `fermeture|ES-AND-SierraNevada-Sulayr|GR240-tramos-2-13-14-17-fermes|2026-09-16`
- `fermeture|FR-06-AlpesMaritimes|sentiers-gr-divers-ffrando06|2026-07-12`
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`
- `fermeture|Finistere-Plomodiern|GR34-Ty-Mark-Kervijen|2026-09-18`
- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`
- `fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`
- `fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07`
- `fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04`
- `fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10`
- `fermeture|Ille-et-Vilaine-Dinard|GR34-Port-Vicomte-Port-Bernard|2026-04-20`
- `fermeture|Ille-et-Vilaine-Saint-Briac-sur-Mer|GR34-Petite-Salinette-Grande-Salinette|2026-02-09`
- `fermeture|Loire-Atlantique-Piriac-sur-Mer|GR34-Pointe-du-Castelli|2026-02-22`
- `fermeture|PO-66-Argeles-Cerbere|sentier-littoral-E12-effondrement|2026-01-19`
- `fermeture|SI-Julijske-Alpe|severni-pristop-Bavski-Grintavec-Kanja-podor|2026-09-17`
- `fermeture|UK-Cornwall-Newquay|SWCP-North-Pier-glissement|2026-02`
- `fermeture|UK-Cornwall-Tintagel|SWCP-effondrement-inondation|2025-12-18`
- `fermeture|UK-Cornwall-Tregonhawke-Whitsand-Bay|SWCP-instabilite-cotiere|2026-03`
- `fermeture|UK-Devon-Branscombe|SWCP-Under-Hooken-Branscombe-Beer|2026-03`
- `incendie|AT-Vorarlberg-Silvretta|coulee-boue-sentiers-fermes|2026-07-12`
- `incendie|Ardeche-Dompnac|feu-40ha-Valgorge|2026-09-26`
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`
- `incendie|Ariege-Mijanes-Donezan|feu-station-Donezan|2026-09-25`
- `incendie|Ariege-Orlu-PerlesEtCastelet|feux-multiples-Ax-les-Thermes|2026-09-14`
- `incendie|Ariege-Saurat|Rocher-de-Batail-GRP-fermes|2026-08-16`
- `incendie|Aude-Montseret-Corbieres|feu-fixe-100ha|2026-08-06`
- `incendie|Corse-Calenzana|feu-Montegrosso-64ha|2026-08-27`
- `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`
- `incendie|Drome-Bellegarde-en-Diois|feu-massif-Claps-400ha|2026-08-03`
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`
- `incendie|ES-AND-Igualeja-Parauta|feu-Serrania-de-Ronda-Sierra-de-las-Nieves|2026-09-27`
- `incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`
- `incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16`
- `incendie|FR-34-11-Puilaurens-Axat|feu-150ha-Camperie|2026-09-04`
- `incendie|FR-84-26-07-LesVans-Malbosc|feu-50ha|2026-09-03`
- `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`
- `incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`
- `incendie|HautesPyrenees-Bareges|Pic-Lurtet-Glere-piste-fermee|2026-07-08`
- `incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`
- `incendie|Lozere-La-Bastide-Puylaurent|feu-252ha|2026-08-19`
- `incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24`
- `incendie|PO-66-Trévillach|feu-4900ha-zone-interdite|2026-07-04`
- `incendie|PT-CENTRO-SUL-Arganil-Piodao|feu-murganheira-evacuation-aldeias-historicas|2026-09-19`
- `incendie|PT-CENTRO-SUL-Odemira-Saboia|feu-nave-redonda|2026-09-24`
- `incendie|PT-CENTRO-SUL-ProencaANova|feu-alvito-da-beira-sobreiraformosa|2026-09-14`
- `incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`
- `incendie|Savoie-Maurienne-Belleville|feux-vegetation-lachapelle-saintpierredebelleville|2026-08-14`
- `incendie|Savoie-Planay-Pralognan|RD915-refuges-Vanoise|2026-07-07`
- `incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16`
- `infrastructure|SCAND-SE-Norrbotten-Padjelantaleden|pont-Mielladno-retire|2026-04`
- `refuge|Canigou-Cortalets|fermeture-travaux|2026-05`
- `refuge|IT-Dolomites-Friuli-Cimoliana|bivacco-gervasutti-amianto-inagibile|2026-09-09`
- `reglementation|ES-GAL|periode-haut-risque-incendie-prolongee|2026-09-24`
- `reroutage|Aspe-64-Chemin-Mature|eboulement-devie-col-Arras|2026-01-05`
- `reroutage|GR10-Luchon-Superbagnères|nouveau-tracé-pérenne|2024-05-30`
- `reroutage|GR21-Loges-Bénouville|glissement-fermeture|2026-02-17`
- `reroutage|GR34-Finistère|fermetures-érosion-2026|2026-S1`
- `reroutage|GR34-rade-de-Brest|nouveau-tracé-officiel|2026-05-28`
- `reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25`
- `reroutage|Pierrefiques-76|déviation|2025-05-18`
- `reroutage|SI-Julijske-Alpe|deviation-Trnovo-Srpenica|2025-10`
- `reroutage|SK-Tatras-Krivan|fermeture-Tri-studnicky|2026`
- `reroutage|UK-Cornwall-St-Martins-Millendreath|SWCP-deviation-glissement|2026-02`
- `reroutage|UK-Devon-Shaldon|SWCP-The-Ness-deviation|2026-04`
- `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30`
- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`
- `risque-feu|Aude-11|fermeture-5-massifs-saison|2026-07-03`
- `risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18`
- `risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`
- `risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28`
- `risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`
- `risque-feu|HauteGaronne-31|vigilance-rouge-camping-sauvage-interdit|2026-07-09`
- `risque-feu|HautesPyrenees-65|interdiction-feu-massifs-forestiers|2026-07-27`
- `risque-feu|Var-83|fermetures-massifs-quotidiennes|2026-07-08`
- `réglementation|PN-Pyrénées|baignade-lacs-interdite|2026-06-15`
- `réglementation|Écrins|bivouac|2026-06-19`
- `sentiers|Mercantour|etat-sentiers-2026|2026-05-15`
- `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08`

## Non traité, à signaler

- Statuts empilés sur plusieurs passages : `fermeture|IT-Dolomites-Friuli-Montasio|...`, `incendie|Savoie-Planay-Pralognan|...`, `risque-feu|FR-Landes-Gironde|...` ont un `statut:` de 800 à 1000 caractères ; non ramenés à l'état courant pour ne pas condenser sans source nouvelle (les passages qu'ils contiennent sont de l'information, à verser dans la chronologie au prochain run qui les touche).
- `livrables/audit-qualite.md` n'a pas été régénéré (`--ecrire` non lancé) : le rapport d'origine reste la référence de ce verdict. Rapport recalculé hors fichier : 66 bloquants, aucun défaut de concordance.
