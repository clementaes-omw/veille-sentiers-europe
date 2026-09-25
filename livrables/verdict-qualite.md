# Verdict qualité — 2026-09-25

Vérificateur qualité (agent distinct de la veille du jour, cf. `agents/verificateur-alertes.md`).
Source de la liste de travail : `livrables/audit-qualite.md`, relancé (`python3
site/audit_qualite.py --ecrire`) en tête de ce contrôle puis en fin de contrôle pour vérifier
l'effet des corrections.

**34 fiches contrôlées** : les 29 fiches citées par la section registre de l'audit (28 avec un
constat ⚠️/·, une comptant double avec le lot carte) + les 5 fiches citées par la section carte
(zones perdues). Aucune de ces 34 fiches n'a été écrite par cet agent : audit indépendant de la
production du run du jour, conformément au mandat.

## ⛔ Corrections bloquantes appliquées (carte)

L'audit du jour signalait 6 constats BLOQUANT sur la carte (regroupement incohérent 99/41 pour
104 actives, 5 alertes sans marqueur). Mandat explicite reçu pour ce passage : les corriger
moi-même en complétant `referentiel/zones-coords.csv` ou `ALIAS_ZONE` (ce point relève en temps
normal de `agents/verificateur-carte.md`, non sollicité aujourd'hui).

1. **`fermeture|Finistere-Plomodiern|GR34-Ty-Mark-Kervijen|2026-09-18`** — zone non résolue.
   Plomodiern (Finistère) est sur le GR®34 littoral, déjà couvert par le code régional `FR-BRE`
   (comme `GR34-Finistère`). Ajout d'un alias `"Finistere-Plomodiern": "FR-BRE"` dans
   `ALIAS_ZONE` (`site/build_site.py`).
2. **`fermeture|UK-Cornwall-Newquay|...`**, **`fermeture|UK-Cornwall-Tintagel|...`**,
   **`fermeture|UK-Cornwall-Tregonhawke-Whitsand-Bay|...`**,
   **`reroutage|UK-Cornwall-St-Martins-Millendreath|...`** — 4 zones non résolues, toutes des
   sections du South West Coast Path en Cornouailles, sans code régional existant (seul
   `UK-Devon` existait, pour le Devon voisin). Ajout d'un nouveau code de zone-source
   `UK-Cornwall;Cornouailles (South West Coast Path);50.45;-4.65` dans
   `referentiel/zones-coords.csv` (centroïde approximatif de la Cornouailles, à mi-chemin entre
   Newquay/Tintagel au nord-ouest et Whitsand Bay/Millendreath au sud-est). Les 4 zones se
   résolvent automatiquement par préfixe (`resolve_zone`), sans entrée `ALIAS_ZONE`
   supplémentaire.

Effet vérifié : `python3 site/audit_qualite.py` → **0 alerte perdue, 0 bloquant carte** (était
6). `python3 site/build_site.py` → **`OK (QA passée)`** (104 actives, 34 clôturées, 138
fichiers).

## Correction appliquée (ton, jargon de veille)

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — « Zone (détails) »
  contenait « à recouper au prochain passage », jargon de veille banni des champs publics.
  Reformulé en « URL précise non retrouvée à ce jour », à information constante (le fait — une
  URL exacte non conservée — est gardé, seule la mécanique de veille disparaît).
  `python3 site/verif_faits.py` confirmé après coup : 1 fiche modifiée contrôlée, **0
  perte/invention de fait**.

## Alertes ROUGES à source vieillie (règle des 14 jours) — 6 fiches, AUCUNE dégradation

L'audit signale ces 6 alertes HAUTE pour une source la plus récente âgée de 11 à 35 jours.
Vérification fiche par fiche demandée : dans les six cas, la fermeture repose sur un **acte
officiel déjà établi et daté** (pas une hypothèse « à confirmer »/« probable » en attente), et
chaque fiche le dit explicitement dans son propre `statut:`. La règle des 14 jours (dégradation
HAUTE→MOYENNE) ne s'applique donc à aucune d'entre elles ; aucun `HYPO_MARQUEUR` n'est du reste
détecté par le contrôle 5 d'`audit_qualite.py` sur l'ensemble du registre. Aucune correction
appliquée, sévérité HAUTE maintenue partout :

- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — 12 communes sous arrêtés
  municipaux datés (le plus récent 10/08), liste PNR Baronnies confirmée identique le 25/09.
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — arrêté préfectoral
  du 31/08/2026 (« jusqu'à nouvel ordre »), reconfirmé en vigueur le 24/09.
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — arrêté préfectoral du 21/08/2026
  (« jusqu'à la fin des opérations d'étude et de sécurisation »), reconfirmé le 24/09.
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` — arrêté
  municipal du 15/08/2026, reconfirmé le 25/09 ; la fiche note elle-même que la règle des 14
  jours ne s'applique pas au sens strict, seule la source vieillit, pas le fondement.
- `incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02` — accès au
  sol interdit par consigne préfectorale directe (secteur du Pas d'Ourtasse), reconfirmée le
  25/09, vingt-trois jours après le départ de feu, sans date de levée.
- `risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01` — communiqué officiel vaucluse.gouv.fr
  du 02/09 (Vallée du Rhône), toujours le seul massif fermé par texte daté, reconfirmé le 25/09.

**Recommandation à la veille** (pas une dégradation) : ces 5 zones HAUTE méritent une recherche
ciblée de l'acte suivant (reconduction ou levée) plutôt qu'une simple relecture, en particulier
Baronnies-GR9 dont l'échéance structurelle de fin de saison (30/09) arrive dans 5 jours.

## Validités à échéance passée — 6 fiches, AUCUNE correction nécessaire

- **Déjà honnêtes en l'état (contrôle 3 PASS), rien à réécrire** — les trois échéances
  suivantes sont réelles et bien dépassées, mais chaque fiche le dit déjà noir sur blanc au
  lecteur sans confirmer à tort une reconduction ou une levée :
  - `fermeture|CH-Vaud-Sainte-Croix-Baulmes|Gorges-Covatannaz-travaux|2026-08-17` (déviation
    17/08→18/09, dernière lecture du flux le 15/09)
  - `incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`
    (route A-1603 réglementée « jusqu'au 15/09 au moins », dépassé sans confirmation)
  - `reroutage|Pierrefiques-76|déviation|2025-05-18` (travaux annoncés jusqu'au 18/09, dépassé
    sans confirmation)
- **Faux positifs de l'heuristique de dates du script** — la date que l'audit lit comme une
  « échéance dépassée » est en réalité la date d'un fait (contrôle/maîtrise du feu), pas une
  date de fin annoncée ; rien à corriger dans le texte, aucune échéance n'y est promise :
  - `incendie|ES-GAL-Quiroga|feu-pacios-da-serra-420ha|2026-09-15` (18/09 = date de passage au
    statut « contrôlé », pas une échéance)
  - `incendie|PT-CENTRO-SUL-Arganil-Piodao|feu-murganheira-evacuation-aldeias-historicas|2026-09-19`
    (20/09 = date de passage au statut « maîtrisé/dominado », fiche NOUVELLE du jour)
  - `risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21` (18/09 = date de
    la dernière vérification du niveau de vigilance, pas une échéance)

## Contrôles 1 à 7 — synthèse sur les 34 fiches

| # | Contrôle | Résultat |
|---|----------|----------|
| 1 | Fraîcheur | 1 FAIL réel non corrigeable en périmètre (Creta-Samaria, `verif` à 7 j sur un seuil de 2 j pour une décision « au jour le jour ») ; ~16 FAIL non bloquants sur zones T2/T3 hors périmètre du jour (liste ci-dessous) ; le reste PASS |
| 2 | Concordance interne | 34 PASS — aucun décrochage Portion/statut/Zone/source constaté sur les fiches lues |
| 3 | Honnêteté sur l'incertitude | 34 PASS, dont les 6 fiches à échéance passée listées ci-dessus, déjà exemplaires |
| 4 | Pertinence | 34 PASS — aucune fiche ne décrit une restriction manifestement obsolète ; aucune clôture recommandée |
| 5 | Sévérité juste | 34 PASS. Les 6 alertes HAUTE du lot reposent toutes sur un acte officiel daté ; règle des 14 jours vérifiée fiche par fiche, applicable à aucune |
| 6 | Ton | 33 PASS, 1 FAIL corrigé (Creta-Samaria, jargon « prochain passage ») |
| 7 | Source vivante | non testé par requête HTTP (hors mandat de ce passage : aucune recherche web). Structurellement, `audit_qualite.py` (contrôle 7 interne) ne signale aucune alerte HAUTE sans URL ; vérification réelle des liens laissée au prochain passage |

### Fiches en FAIL contrôle 1 (fraîcheur), zones T2/T3 hors périmètre du jour — signalées, non touchées

Aucune incohérence de fond trouvée sur ces fiches ; seule une revérification sur source réglerait
le FAIL de fraîcheur, qui n'est pas de mon ressort sans nouvelle information. **Action attendue :
revérification directe par le prochain passage sur chacune de ces zones (CH/IT/DE hors cadence
du jour)** :

- `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25`
- `eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`
- `fermeture|CH-EST-Frutigen|Kander-Uferweg-impraticable|2026-08-17` (déjà réécrite honnêtement
  par le contrôle qualité du 24/09 ; seule une relecture du flux data.geo.admin.ch, id 2600749,
  lève à la fois le FAIL de fraîcheur et l'échéance du 21/09 désormais passée)
- `fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08`
- `fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26`
- `fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`
- `fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07`
- `fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10`
- `fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10`
- `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`
- `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`
- `incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`
- `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10`
- `refuge|IT-Dolomites-Friuli-Cimoliana|bivacco-gervasutti-amianto-inagibile|2026-09-09`
- `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30`
- `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08`

## Hors périmètre — signalé, non corrigé

- **Doublon probable** (déjà signalé au contrôle du 24/09, toujours présent) :
  `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25` et
  `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08` décrivent la même
  restriction safetravel.is (recul glaciaire, crevasses, ponts de neige sur le Fimmvörðuháls
  entre Baldvinsskáli/Skógar et Fimmvörðuhálsskáli/Þórsmörk) sous deux clés distinctes
  (`conditions` vs `terrain`, `IS-Hautes-Terres` vs `IS-HautesTerres`). Fusion/choix de clé
  canonique = protocole de dédoublonnage de la veille, pas une réécriture à information
  constante : signalé, non fusionné.
- **Levée éventuelle non tranchée sans nouvelle source** : les 6 alertes HAUTE listées plus haut
  et les 6 échéances passées listées plus haut demandent toutes une recherche ciblée
  (reconduction/levée) que je ne peux pas faire (aucune recherche web dans mon mandat) : laissées
  à la veille.

## Vérification finale du build

`python3 site/build_site.py` après corrections : **`OK (QA passée)`** →
`/home/user/veille-sentiers-europe/site/index.html` (104 actives, 34 clôturées, 67 digests,
registre 138 fichiers). `python3 site/audit_qualite.py` relancé après corrections : **0
bloquant** (registre et carte), 32 alerte(s), 0 info(s) — l'unique info restante (jargon
Creta-Samaria) a été corrigée dans la foulée. `python3 site/verif_faits.py` : 1 fiche modifiée
contrôlée vs HEAD, 0 perte/invention de fait.
