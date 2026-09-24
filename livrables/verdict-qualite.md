# Verdict qualité — 2026-09-24

Vérificateur qualité (agent distinct de la veille du jour, cf. `agents/verificateur-alertes.md`).
Source de la liste de travail : `livrables/audit-qualite.md` du 2026-09-24
(`python3 site/audit_qualite.py --ecrire`), relancé en tête de ce contrôle puis en fin
de contrôle pour vérifier l'effet des corrections.

**30 fiches contrôlées** (toutes celles citées par l'audit : 1 constat bloquant + 29
fiches avec un constat ⚠️). Aucune de ces fiches n'a été écrite par cet agent : audit
indépendant de la production du run du jour, conformément au mandat.

## ⛔ À traiter au prochain run couvrant la zone

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — FAIL contrôle 1
  (fraîcheur) : `verif: 2026-09-18`, soit 6 jours avant ce contrôle, alors que sa propre
  `validite:` annonce une décision « au jour le jour » (seuil de fraîcheur : 2 jours). La
  fiche est par ailleurs cohérente en interne (contrôle 2 PASS) et honnête sur son incertitude
  (contrôle 3 PASS) : rien dans son texte actuel ne permet de corriger la formulation à
  information constante, la seule correction possible est une revérification sur source.
  **Action attendue** : revérification ciblée du statut du jour de la gorge de Samaria
  (samaria.gr, Région de Crète / OFYPEKA-NECCA) par la prochaine veille couvrant la zone
  Grèce/Crète.

## Corrections appliquées (dans mon périmètre, à information constante)

1. **`fermeture|CH-EST-Frutigen|Kander-Uferweg-impraticable|2026-08-17`** — FAIL contrôle 1
   (`verif: 2026-09-08`, 16 j, seuil 12 j) et FAIL contrôle 3 (la « Portion concernée »
   présentait comme actuelle une échéance du 21/09/2026 déjà dépassée au moment du contrôle,
   sans le dire au lecteur). Correction : `validite:`, `statut:` et « Portion concernée »
   réécrits pour dire explicitement que l'échéance du 21/09 est dépassée et qu'aucune
   relecture du flux officiel (data.geo.admin.ch, id 2600749) n'a eu lieu depuis le 08/09.
   Aucun fait ajouté ni supprimé (vérifié par `site/verif_faits.py`, 0 écart après correction).
   **Action laissée à la veille** : relire directement le flux officiel lors de la prochaine
   couverture de la zone CH-EST.
2. **`fermeture|UK-Cornwall-Tintagel|SWCP-effondrement-inondation|2025-12-18`** — l'audit
   signalait « validité désormais passée au 18/12/2025 », mais ce 18/12/2025 est la date de
   **début** de la fermeture (« fermé et dévié depuis le 18/12/2025 »), pas une échéance : faux
   positif de l'heuristique de dates du script sur une fiche déjà honnête (« aucune date de
   réouverture annoncée »). Correction légère de `validite:` pour expliciter « jusqu'à nouvel
   ordre » et lever l'ambiguïté pour les futurs passages de l'audit, sans changer le fond.

## Contrôles 1 à 7 — synthèse sur les 30 fiches

| # | Contrôle | Résultat |
|---|----------|----------|
| 1 | Fraîcheur | 1 FAIL bloquant (Creta-Samaria, non corrigeable en périmètre) ; 17 FAIL non bloquants (liste ci-dessous, échéance de fraîcheur dépassée sans que le contenu soit devenu incohérent ou malhonnête) ; 12 PASS |
| 2 | Concordance interne (Portion/statut/Zone/source) | 30 PASS — aucun décrochage constaté entre les champs sur les 30 fiches lues |
| 3 | Honnêteté sur l'incertitude | 2 FAIL corrigés (Frutigen, Tintagel) ; 28 PASS, dont plusieurs déjà exemplaires (Sainte-Croix-Baulmes, Pierrefiques-76, Riglos, Quiroga, Arganil-Piódão, Landes-Gironde : toutes disent déjà en clair que l'échéance annoncée est dépassée et non reconfirmée) |
| 4 | Pertinence | 30 PASS — aucune des 30 fiches ne décrit une restriction manifestement obsolète ; aucune clôture recommandée |
| 5 | Sévérité juste | 30 PASS. 5 alertes HAUTE dans le lot (Baronnies-GR9, Ariège-Bordes-Uchentein, Drôme-Justin-Die, HautesAlpes-BoisNoir, Pyrénées-Atlantiques-Etsaut) : toutes reposent sur un acte officiel daté (arrêté préfectoral/municipal ou consigne préfectorale active « jusqu'à nouvel ordre »), aucune sur une hypothèse non tranchée. Vérification explicite de la règle des 14 jours (alerte rouge sur hypothèse) demandée en consigne : **aucune des alertes HAUTE actuelles du registre n'est adossée à « à confirmer »/« probable » au-delà de 14 j** — confirmé à la fois par ma lecture des 5 fiches et par le contrôle 5 d'`audit_qualite.py` (`HYPO_MARQUEURS`), qui ne remonte aucun constat de ce type sur l'ensemble du registre. La règle des 14 jours ne s'applique donc à aucune fiche aujourd'hui |
| 6 | Ton | 30 PASS — aucun jargon de veille (« ce run », « lot T2 », « en autonome », etc.) trouvé dans les champs publics des 30 fiches lues |
| 7 | Source vivante | non testé par requête HTTP dans ce passage (hors mandat : je ne requête pas le web, cf. consigne reçue pour Creta-Samaria, appliquée par prudence à l'ensemble du contrôle). Les 5 sources des alertes HAUTE citées ont toutes été relues et confirmées en texte par la veille dans les 24 h précédentes ce contrôle ; une revérification HTTP réelle reste à faire par le prochain passage sur chaque zone |

### Fiches en FAIL contrôle 1 (fraîcheur) laissées à la veille, sans autre défaut trouvé

Revérification simple à faire lors du prochain passage sur la zone concernée (aucune
incohérence de fond, aucune correction de texte possible sans nouvelle source) :

- `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25` (safetravel.is)
- `eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`
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
- `reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25`
- `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30`
- `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08`
- `fermeture|CH-EST-Frutigen|Kander-Uferweg-impraticable|2026-08-17` (fraîcheur restant en
  FAIL malgré la correction de texte ci-dessus : seule une relecture du flux officiel la lève)

### Alertes HAUTE avec source datée vieillissante (contrôle 5 PASS, recommandation de veille uniquement)

Ces 5 fiches reposent sur un acte officiel toujours en vigueur, pas sur une hypothèse : pas de
dégradation à appliquer d'autorité. Je recommande à la prochaine veille couvrant chaque zone une
recherche ciblée d'un acte plus récent (reconduction, levée) plutôt qu'une simple relecture :

- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` (arrêtés municipaux les plus
  anciens du 08/07, échéance structurelle de fin de saison le 30/09 — à surveiller de près)
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` (arrêté du 31/08)
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` (arrêté du 21/08)
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` (arrêté du 15/08)
- `incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02` (dernier
  point préfectoral daté du 10/09)

## Hors périmètre — signalé, non corrigé

- **Carte** : `audit_qualite.py` et `build_site.py` signalent 6 constats (regroupement
  incohérent 98 alertes/41 marqueurs pour 103 actives, et 5 zones non résolues vers
  `referentiel/zones-coords.csv` : Finistère-Plomodiern, UK-Cornwall-Newquay,
  UK-Cornwall-Tintagel, UK-Cornwall-Tregonhawke-Whitsand-Bay,
  UK-Cornwall-St-Martins-Millendreath). Je n'ai touché ni à `referentiel/zones-coords.csv` ni
  à `site/build_site.py` : c'est le périmètre de `agents/verificateur-carte.md` (déclenché le
  lundi ou après ajout d'une zone au CSV).
- **Doublon probable repéré en lisant les fiches, non signalé par l'audit** :
  `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25` et
  `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08` décrivent la même
  alerte safetravel.is (recul glaciaire, crevasses, ponts de neige sur le Fimmvörðuháls entre
  Baldvinsskáli/Skógar et Fimmvörðuhálsskáli/Þórsmörk) sous deux clés distinctes (préfixes
  `conditions` vs `terrain`, zone `IS-Hautes-Terres` vs `IS-HautesTerres`). Le choix de la clé
  canonique et la fusion des chronologies relèvent du protocole de dédoublonnage de la veille
  (`agent-prompt.md`), pas d'une réécriture à information constante : signalé, non fusionné.
- **`python3 site/verif_faits.py`** (lancé par prudence après mes propres corrections, qui
  passent à 0 écart) signale, sur des fiches modifiées aujourd'hui par la veille mais **non
  citées par l'audit qualité** donc hors de mon mandat de correction : pertes/inventions de
  faits possibles sur `fermetures-sentiers--reunion-974--ap-2026-693--2026-05-21.md`,
  `incendie--es-and-benahavis--feu-actif-confinement-9500-habitants--2026-09-13.md` et
  `reroutage--sk-tatras-krivan--fermeture-tri-studnicky--2026.md`. Signalement en clair pour
  action immédiate avant tout commit du run du jour : je n'ai pas ouvert ni corrigé ces trois
  fiches.

## Vérification finale du build

`python3 site/build_site.py` après corrections : **`OK (QA passée)`**
(103 actives, 34 clôturées, 66 digests, 137 fichiers) — seul avertissement restant, le
regroupement carte déjà signalé ci-dessus (hors périmètre). `python3 site/audit_qualite.py`
relancé après corrections : toujours 1 bloquant registre (Creta-Samaria, cf. ci-dessus, non
corrigeable sans nouvelle source) + 6 bloquants carte (hors périmètre) ; aucun bloquant
nouveau introduit par mes corrections. `python3 site/verif_faits.py` : 0 écart sur les 2
fiches que j'ai modifiées.
