# Verdict qualité — 2026-09-28

Vérificateur qualité des alertes publiées (rôle distinct de la veille du jour). Aucune des
fiches contrôlées ici n'a été écrite par cette session : audit du run de veille du
2026-09-28 (agrégateurs + zones T1 saison feux + lot T2 du lundi + zones en escalade
DE-Sachsen/FR-974) et du reste du registre, exactement comme n'importe quel autre jour.

Périmètre : les 40 constats de `livrables/audit-qualite.md` tel que généré ce jour par
`python3 site/audit_qualite.py --ecrire` (111 alertes actives, 36 fiches distinctes citées,
0 bloquant, 40 alertes). **36 fiches contrôlées** (celles citées par l'audit, et elles
seules).

## Résultat global après correction

`python3 site/audit_qualite.py` (relancé avec `--ecrire`) : **0 bloquant(s)**, 37 constats
(contre 40 avant intervention) sur 146 fiches. `python3 site/build_site.py` rend
« OK (QA passée) » après chaque correction. 3 fiches sont sorties de la liste de travail
(défaut de CONCORDANCE/HONNÊTETÉ corrigé) ; les 33 fiches restantes portent des FAILS de
fraîcheur hors périmètre (nouvelle source requise) ou des faux positifs du script
déterministe déjà correctement traités dans le texte (détail ci-dessous).

## PASS / FAIL par contrôle (sur les 36 fiches auditées)

1. **FRAÎCHEUR** — FAIL sur 20 fiches MOYENNE vérifiées au-delà du seuil de 12 jours (13 à
   23 j) et 1 fiche journalière (GR-E4 Creta Samaria, vérifiée à 3 j pour un seuil de 2 j),
   + plusieurs « jamais revérifiées depuis la détection ». Hors périmètre du vérificateur
   (aucune de ces corrections n'existe sans consulter une source non encore lue) : listées
   en actions pour le prochain run, ci-dessous.
2. **CONCORDANCE INTERNE** — PASS sur les 36 fiches contrôlées : dans chaque cas relu en
   entier, « Portion concernée », `statut:` et « Zone (détails) » racontent la même chose.
   Aucun décrochage du type « défaut du 02/08 » trouvé aujourd'hui, y compris sur les fiches
   touchées par la veille du jour (Baronnies, Ariège-Bordes-Uchentein, Drôme-Justin-Die,
   Hautes-Alpes-Bois-Noir, Pyrénées-Atlantiques-Etsaut) : agent distinct, travail propre.
3. **HONNÊTETÉ SUR CE QU'ON NE SAIT PAS** — FAIL initial sur 2 fiches où `validite:`
   présentait une date de constat (feu « controlado »/« dominado ») sans dire clairement
   qu'aucune extinction officielle n'était encore publiée à la date de vérification.
   **Corrigé** (voir ci-dessous). PASS partout ailleurs, y compris sur les 6 alertes ROUGE à
   arrêté sans échéance (voir contrôle 5) et sur `reroutage|Pierrefiques-76|...`, qui pose
   déjà l'échéance dépassée en clair sans fabriquer de prolongation.
4. **PERTINENCE** — aucune clôture appliquée (hors périmètre sans nouvelle source). Deux
   recommandations motivées : voir « Recommandations » ci-dessous
   (ES-GAL-Quiroga, PT-CENTRO-SUL-Arganil-Piodao — feux contrôlés/maîtrisés depuis 8 à 10
   jours sans qu'aucune fermeture de sentier n'ait jamais été documentée).
5. **SÉVÉRITÉ JUSTE** — FAIL apparent du script sur 6 alertes ROUGE (Baronnies-GR9, Ariège-
   Bordes-Uchentein, Drôme-Justin-Die, Hautes-Alpes-Bois-Noir, Pyrénées-Atlantiques-Etsaut,
   Vaucluse-84), appuyées sur une source vieille de 14 à 38 jours. Vérifié fiche par fiche :
   dans chacune, le fondement de la sévérité HAUTE est un arrêté officiel déjà publié, sans
   échéance calendaire (« jusqu'à nouvel ordre », « jusqu'à la fin des opérations d'étude »),
   pas une hypothèse « à confirmer »/« probable » — le build lui-même ne signale aucune de
   ces 6 fiches comme hypothèse non tranchée (0 bloquant « [hypothèse] »). La règle des 14
   jours (dégradation obligatoire) ne s'applique donc à aucune : elle vise les alertes rouges
   fondées sur une hypothèse non recoupée, pas celles fondées sur un acte publié que la
   veille revérifie chaque jour sans y trouver de levée. **PASS, aucune dégradation.**
   Sources officielles spot-vérifiées en direct ce jour (voir contrôle 7) : toutes les 5
   testées confirment le texte de la fiche.
6. **TON** — PASS. Aucun jargon de veille dans « Portion concernée », « Alternative » ou
   « Zone (détails) » sur les 36 fiches (0 info remonté par l'audit sur le lot, build sans
   violation `[ton]`).
7. **SOURCE VIVANTE** — contrôlé en direct (WebFetch) sur les 6 alertes ROUGE citées par
   l'audit : baronnies-provencales.fr, mairie-die.fr, ville-argentiere.fr et
   lasemainedespyrenees.fr répondent et confirment le contenu de la fiche. **FAIL** sur
   `risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01` : l'URL du communiqué
   vaucluse.gouv.fr du 02/09 (seule source officielle du massif encore nommément fermé)
   répond en 503 au moment du contrôle — panne déjà documentée par la veille elle-même dans
   `statut:` ce jour, pas une découverte nouvelle. Reporté ci-dessous, non bloquant au sens
   du build (la fiche cite d'autres sources secondaires convergentes).

## Corrections appliquées (clés)

- `incendie|ES-GAL-Quiroga|feu-pacios-da-serra-420ha|2026-09-15` — `validite:` réécrite :
  l'ancienne formulation datait le constat du feu « contrôlé » (18/09) sans dire si une
  extinction avait depuis été publiée, ce que le script lisait comme une échéance expirée.
  Nouvelle formulation, à information constante (source déjà citée, contenu déjà dans
  `statut:`) : « ... à la dernière vérification (27/09/2026), aucune déclaration
  d'extinction totale n'a été retrouvée. »
- `incendie|PT-CENTRO-SUL-Arganil-Piodao|feu-murganheira-evacuation-aldeias-historicas|2026-09-19`
  — même correction : `validite:` précise désormais que l'API officielle api.fogos.pt ne
  recense plus de foyer actif au 27/09, mais qu'aucune déclaration formelle d'extinction
  n'est publiée. Aucun fait ajouté au-delà de ce qui figurait déjà dans `statut:`.
- `risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21` — deux défauts
  corrigés dans la même fiche : (a) `validite:` se terminait sur une date de vérification
  (18/09) lue par le script comme une échéance expirée, alors que le niveau ORANGE des
  Landes n'a par nature pas de terme fixe (il tient jusqu'au prochain arrêté préfectoral,
  comme documenté dans toute la chronologie de la fiche) — précisé en clair
  (« maintenu jusqu'à nouvel ordre du préfet des Landes ») ; (b) le `statut:` portait encore
  la pastille « CHANGÉ 18/09 » alors qu'une vérification ultérieure (verif: 2026-09-25) sans
  changement de fond avait eu lieu depuis — pastille retirée conformément à la règle
  (« le compteur de changé doit disparaître au passage suivant »), aucune information
  supprimée.

Note de correction en cours d'audit : la première tentative sur cette dernière fiche avait
introduit une nouvelle date (25/09) dans `validite:`, ce qui aurait fait réapparaître le même
faux positif du script sous une autre date. Revert immédiat puis nouvelle formulation sans
date terminale — vérifié par un nouveau passage `audit_qualite.py` (0 régression).

## Recommandations (contrôle 4, non appliquées)

- `incendie|ES-GAL-Quiroga|feu-pacios-da-serra-420ha|2026-09-15` — feu « contrôlé » depuis
  10 jours (18 au 27/09), ~460 ha, et aucune source consultée (9 sources citées) n'a jamais
  documenté de fermeture ou de dégradation du Camino de Invierno lui-même. À envisager pour
  clôture dès qu'une extinction officielle est publiée, ou à reformuler explicitement comme
  alerte de contexte (pas de restriction de sentier) si la veille confirme qu'aucune ne
  viendra.
- `incendie|PT-CENTRO-SUL-Arganil-Piodao|feu-murganheira-evacuation-aldeias-historicas|2026-09-19`
  — même profil : feu « maîtrisé » depuis 8 jours, api.fogos.pt ne recense plus de foyer
  actif, aucune fermeture du GR®22 jamais documentée. Même recommandation.
- `incendie|PT-CENTRO-SUL-Odemira-Saboia|feu-nave-redonda|2026-09-24` — pas encore mûr pour
  une recommandation (détection il y a 3 j, verif du jour même), mais même trajectoire à
  surveiller si le statut « Vigilância » se maintient sans fermeture documentée.

## Faux positifs du script déterministe (aucune correction nécessaire au-delà de ce qui précède)

Le contrôle « validité expirée » de `site/audit_qualite.py` prend la date la plus tardive
citée dans `validite:`, sans distinguer une échéance réglementaire d'une simple date de
constat ou de vérification. Sur les 5 fiches qu'il a signalées ce jour :
- `incendie|ES-GAL-Quiroga|...` et `incendie|PT-CENTRO-SUL-Arganil-Piodao|...` — corrigées
  ci-dessus (le flou méritait d'être levé même si le script se trompait de raison).
- `incendie|PT-CENTRO-SUL-Odemira-Saboia|feu-nave-redonda|2026-09-24` — même mécanisme
  (date du « dominado », 25/09, lue comme échéance), mais `verif:` est daté d'aujourd'hui et
  le texte est déjà limpide (statut « Vigilância » confirmé par api.fogos.pt le 27/09).
  PASS, aucune action : une réécriture aurait été un geste cosmétique sans fait nouveau à
  apporter.
- `reroutage|Pierrefiques-76|déviation|2025-05-18` — la « validité » 18/09 détectée est une
  vraie échéance de travaux, dépassée. Le texte le dit déjà noir sur blanc (« aucune source
  ne confirme à ce jour que le chantier est terminé »), sans fabriquer de prolongation ni
  clôturer sans preuve. PASS, aucune action.
- `risque-feu|FR-Landes-Gironde|...` — corrigée ci-dessus.

## Actions laissées à l'agent de veille pour le prochain run

### Sources (contrôle 7)

- `risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01` — l'URL du communiqué
  vaucluse.gouv.fr du 02/09 (Vallée du Rhône) répond en 503 ce jour. Retrouver une copie
  active (cache, recherche du titre exact) ou revérifier l'accessibilité au prochain passage
  avant de la citer comme seule preuve d'une fermeture nommée.

### Fraîcheur (contrôle 1), toutes MOYENNE sauf mention contraire — nouvelle source requise, aucune correction interne possible sans elle :

- `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25` (16 j, jamais revérifiée)
- `eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10` (16 j, jamais revérifiée)
- `fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08` (jamais revérifiée, 20 j — sévérité INFO, faible priorité)
- `fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26` (20 j)
- `fermeture|CH-Europaweg-Randa-Zermatt|fermeture-deviation-seg-27.3|2024-07-03` (13 j)
- `fermeture|CH-Valais-Arolla|Bertol-Haut-Glacier-deviation|2026-05-11` (13 j)
- `fermeture|CH-Valais-Arolla|Pas-de-Chevre-chemin-impraticable|2026-08-24` (13 j)
- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` (3 j pour un seuil de
  2 j — restriction décidée au jour le jour ; épisode de pluie en cours depuis le 22/09,
  revérifier le statut du jour avant toute étape)
- `fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024` (23 j)
- `fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07` (23 j)
- `fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04` (14 j)
- `fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10` (23 j)
- `fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10` (16 j, jamais revérifiée)
- `fermeture|TMB-CH-Orsieres|fermeture-deviation-seg-6.35|2026-07-11` (13 j)
- `fermeture|VS-Orsieres-ValFerret|Saleinaz-cabane-eboulement|2026-07-29` (13 j)
- `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28` (18 j)
- `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` (18 j)
- `incendie|HautesPyrenees-Bareges|Pic-Lurtet-Glere-piste-fermee|2026-07-08` (14 j)
- `incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03` (23 j)
- `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` (23 j)
- `refuge|IT-Dolomites-Friuli-Cimoliana|bivacco-gervasutti-amianto-inagibile|2026-09-09` (14 j, jamais revérifiée)
- `reroutage|Aspe-64-Chemin-Mature|eboulement-devie-col-Arras|2026-01-05` (14 j)
- `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30` (23 j)
- `réglementation|PN-Pyrénées|baignade-lacs-interdite|2026-06-15` (14 j)
- `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08` (23 j)

Action attendue pour chacune : nouvelle vérification directe de la ou des sources citées (ou
recherche de remplacement si la source est devenue muette/morte), mise à jour de `verif:`
et, si le fond a changé, de « Portion concernée ». Pas de dégradation automatique : juger au
cas par cas si la restriction tient toujours sur le seul fait déjà établi.

## Note de méthode

Aucune fiche listée ci-dessus n'a été rédigée par cette session : rôle de vérification
distinct de la veille du 2026-09-28 (5 zones T1 + agrégateurs + lot T2 lundi + escalades
DE-Sachsen/FR-974, dont ce vérificateur n'a corrigé aucune fiche — leurs alertes n'étaient
pas citées par l'audit). `python3 site/build_site.py` relancé après chaque lot de
corrections : « OK (QA passée) » à chaque fois (111 actives, 35 clôturées, 146 fichiers).
`python3 site/audit_qualite.py --ecrire` relancé deux fois après corrections pour rafraîchir
`livrables/audit-qualite.md` (40 → 38 après une correction incomplète détectée et corrigée →
37 constats, 0 bloquant du début à la fin), puis reconfirmé par un appel final.
