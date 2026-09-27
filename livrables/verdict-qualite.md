# Verdict qualité — 2026-09-27

Vérificateur qualité des alertes publiées (rôle distinct de la veille du jour). Aucune des
fiches contrôlées ici n'a été écrite par cette session : audit externe au travail des 5
agents de veille parallèles.

Périmètre : les 36 constats de `livrables/audit-qualite.md` (généré par
`python3 site/audit_qualite.py --ecrire`, 141 fiches, 0 bloquant, 38 alertes avant
corrections). **31 fiches distinctes contrôlées** (celles citées par l'audit).

## Résultat global après correction

`python3 site/audit_qualite.py` (sans --ecrire) : **0 bloquant(s)**, 36 constats (contre 38
avant intervention) sur 141 fiches. Les 2 défauts de CONCORDANCE INTERNE et le 1 défaut de
TON signalés par l'audit sont résolus. Les 33 constats restants sont soit des FAILS de
fraîcheur hors périmètre (recherche nouvelle requise), soit des faux positifs du script
déterministe déjà correctement traités dans le texte (détail ci-dessous).

## PASS / FAIL par contrôle (sur les fiches auditées)

1. **FRAÎCHEUR** — FAIL sur 21 fiches MOYENNE vérifiées au-delà du seuil de 12 jours (13 à
   22 j), + 2 fiches « jamais revérifiées » (CH-EST-Kandersteg, IT-Dolomites-Friuli-Cimoliana
   figurant déjà dans le compte ci-dessus). Hors périmètre du vérificateur (recherche web
   requise) : listées en actions pour le prochain run, ci-dessous.
2. **CONCORDANCE INTERNE** — FAIL initial sur 2 fiches (Baronnies GR9, Hautes-Alpes Bois
   Noir) : « Portion concernée » figée au 18/09 pendant que `statut:` et « Zone (détails) »
   savaient déjà l'état du 27/09. **Corrigé** (réécriture à information constante, aucun
   fait ajouté ni supprimé). Un 3e cas trouvé en cours d'audit, non listé par le script
   (Vaucluse-84, « à ce jour (23/09/2026) » au lieu de 27/09) : **corrigé** de même. PASS
   partout ailleurs dans le lot audité.
3. **HONNÊTETÉ SUR CE QU'ON NE SAIT PAS** — PASS sur les 5 fiches à `validite:` en apparence
   expirée (voir détail plus bas) : chacune pose déjà en clair ce qui n'est pas confirmé,
   sans fabriquer de prolongation ni clôturer sans preuve.
4. **PERTINENCE** — aucune clôture recommandée dans le lot audité, à une exception near-miss
   signalée en action prioritaire (Aspe-64-Chemin-Mature, voir ci-dessous).
5. **SÉVÉRITÉ JUSTE** — FAIL apparent du script sur 6 alertes ROUGE (Baronnies, Ariège-
   Bordes-Uchentein, Drôme-Justin-Die, Hautes-Alpes-Bois-Noir, Pyrénées-Atlantiques-Etsaut,
   Vaucluse-84) appuyées sur une source vieille de 13 à 37 jours. Vérifié fiche par fiche :
   dans chacune, le fondement de la sévérité HAUTE est un FAIT établi (arrêté préfectoral ou
   municipal déjà publié, toujours en vigueur faute de levée), pas une hypothèse à
   confirmer — la règle des 14 jours ne s'applique donc PAS. **PASS, aucune dégradation**,
   conforme au texte déjà présent dans `statut:` de chacune. Aucun cas de la liste ne
   relevait de la règle des 14 jours au sens strict.
6. **TON** — FAIL initial sur DE-Sachsen-SaechsischeSchweiz (Malerweg), jargon de veille
   « recherche ciblée » dans « Zone (détails) », entrée du 27/09. **Corrigé** (reformulé
   « nouvelle vérification »), chronologie historique intacte, aucune entrée ni date
   supprimée.
7. **SOURCE VIVANTE** — non systématiquement re-testée (hors périmètre sans navigateur web) ;
   aucune source citée sous alerte ROUGE n'a été signalée morte par l'audit déterministe
   dans ce lot.

## Corrections appliquées (clés)

- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — Portion concernée : date de
  vérification 18/09 → 27/09 (les 12 communes et leurs arrêtés sont inchangés depuis le
  04/09, confirmés à nouveau le 27/09 dans Zone détails) ; ajout d'une phrase sur l'échéance
  de fin de saison (30/09, à 3 jours), déjà connue de la fiche.
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` — Portion
  concernée : date de vérification 18/09 → 27/09 ; source « PN Écrins » remplacée par
  « recueil des actes administratifs des Hautes-Alpes » (celle réellement consultée au
  27/09, cf. Zone détails).
- `risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01` — Portion concernée : date de
  vérification 23/09 → 27/09 (même écart, trouvé en cours d'audit, non listé par le script).
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — Portion concernée : date de
  vérification 23/09 → 27/09 (même écart).
- `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`
  — Zone (détails), entrée du 27/09 : « nouvelle recherche ciblée » → « nouvelle
  vérification » (jargon de veille banni du champ public). Chronologie non touchée.

## Faux positifs du script déterministe (aucune correction nécessaire)

Le contrôle « validité expirée » du script (`site/audit_qualite.py`, fonction autour de
`dates_citees`) prend la date la plus tardive citée dans le champ `validite:`, sans
distinguer une échéance réglementaire d'une simple date de vérification. Sur 5 cas
signalés, 4 sont des faux positifs : la date « expirée » qu'il détecte est en fait la date
du dernier point de situation, pas un terme annoncé.
- `incendie|ES-ARA-Huesca-Riglos|...` — la « validité » 18/09 détectée est la date de la
  dernière vérification ; le texte pose déjà correctement que l'échéance réelle (route
  A-1603, 15/09) est dépassée sans confirmation de levée. PASS, aucune action.
- `incendie|ES-GAL-Quiroga|...` — la « validité » 18/09 détectée est la date où le feu a été
  déclaré « controlado », pas une échéance. Statut déjà à jour au 27/09 (fiche distincte
  Calvos-de-Randín bien séparée). PASS.
- `incendie|PT-CENTRO-SUL-Arganil-Piodao|...` — la « validité » 20/09 détectée est la date
  où le feu a été déclaré « dominado ». Statut vérifié au 27/09 via l'API fogos.pt. PASS.
- `risque-feu|FR-Landes-Gironde|...` — la « validité » 18/09 détectée est une date de
  vérification citée dans le champ, pas une échéance. PASS.
Le 5e cas est une vraie échéance dépassée, déjà traitée correctement :
- `reroutage|Pierrefiques-76|déviation|2025-05-18` — déviation annoncée jusqu'au 18/09,
  échéance dépassée sans confirmation de fin de chantier. Le texte le dit déjà en clair
  (« aucune source ne confirme à ce jour que le chantier est terminé »), sans fabriquer de
  prolongation ni clôturer sans preuve. PASS, aucune action de ma part (au-delà de refléter
  la même échéance déjà correctement posée).

## Action prioritaire trouvée en cours d'audit (à vérifier au prochain run)

- **`reroutage|Aspe-64-Chemin-Mature|eboulement-devie-col-Arras|2026-01-05`** — la fiche
  `incendie|Pyrenees-Atlantiques-Etsaut|...` (vérifiée aujourd'hui par la veille) cite le
  site du gestionnaire CDRP64/gr10.org mentionnant que « le Chemin de la Mâture [est]
  rouverte en mars 2026 après travaux ». Cette fiche-ci reste pourtant FERMÉ sur la seule foi
  de refuges.info (point 6895), non actualisé depuis le 03/02/2026. Signal fort de clôture
  possible, mais je n'ai pas vérifié moi-même la page CDRP64/gr10.org (source citée par une
  autre fiche, pas consultée directement par moi) : **à confirmer par la veille au prochain
  passage sur cette zone**, avant de clôturer. Ne pas clôturer sans avoir consulté la source
  primaire.

## Actions laissées à l'agent de veille pour le prochain run (fraîcheur, hors périmètre)

Toutes MOYENNE, vérifiées au-delà du seuil de 12 jours — nouvelle recherche requise, aucune
n'a de correction interne possible sans nouvelle source (vérifié : Portion concernée et
`statut:` déjà mutuellement cohérents, juste tous deux datés) :
- `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25` (15 j, jamais revérifiée)
- `eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10` (15 j, jamais revérifiée)
- `fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08` (jamais revérifiée, 19 j — sévérité INFO, faible priorité)
- `fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26` (19 j)
- `fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024` (22 j)
- `fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07` (22 j)
- `fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04` (13 j)
- `fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10` (22 j)
- `fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10` (15 j, jamais revérifiée)
- `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28` (17 j)
- `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` (17 j)
- `incendie|HautesPyrenees-Bareges|Pic-Lurtet-Glere-piste-fermee|2026-07-08` (13 j)
- `incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03` (22 j)
- `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` (22 j)
- `refuge|IT-Dolomites-Friuli-Cimoliana|bivacco-gervasutti-amianto-inagibile|2026-09-09` (13 j, jamais revérifiée)
- `reroutage|Aspe-64-Chemin-Mature|eboulement-devie-col-Arras|2026-01-05` (13 j — voir aussi
  l'action prioritaire ci-dessus : signal de réouverture à vérifier en priorité)
- `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30` (22 j)
- `risque-feu|HauteGaronne-31|vigilance-rouge-camping-sauvage-interdit|2026-07-09` (13 j)
- `risque-feu|HautesPyrenees-65|interdiction-feu-massifs-forestiers|2026-07-27` (13 j)
- `réglementation|PN-Pyrénées|baignade-lacs-interdite|2026-06-15` (13 j)
- `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08` (22 j)

Action attendue pour chacune : nouvelle vérification directe de la ou des sources citées
(ou recherche de remplacement si la source est devenue muette/morte), mise à jour de
`verif:` et, si le fond a changé, de « Portion concernée ». Pas de dégradation automatique :
juger au cas par cas si la restriction tient toujours sur le seul fait déjà établi.

## Note de méthode

Aucune fiche listée ci-dessus n'a été rédigée par cette session (rôle de vérification
distinct de la veille). `python3 site/build_site.py` n'a pas été lancé (rôle de
l'orchestrateur). `python3 site/audit_qualite.py --ecrire` a été relancé une fois après
corrections pour rafraîchir `livrables/audit-qualite.md` (39 → 36 constats, 0 bloquant
inchangé), puis reconfirmé par un appel sans `--ecrire`.
