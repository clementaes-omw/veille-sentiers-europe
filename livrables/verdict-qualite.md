# Verdict qualité du registre — 2026-09-13

Agent : `agents/verificateur-alertes.md`, distinct de l'agent de veille du jour. Aucune des
fiches ci-dessous n'a été écrite par moi : audit réel, pas relecture de complaisance.

`python3 site/audit_qualite.py --ecrire` relancé en préambule (résultat identique à celui déjà
annoncé par la veille : 9 constats non bloquants, 0 bloquant, avant mes corrections).

**9 fiches contrôlées en profondeur** (les seules avec un `verif:` du 13/09/2026, périmètre
du jour) + **4 fiches supplémentaires** traitées partiellement (constats de l'audit non liés
au périmètre du jour, corrigées sur le seul point « validité », sans audit complet des 7
contrôles). Aucune autre fiche du dossier (105 restantes) n'a été ouverte ni modifiée.

Après corrections : `python3 site/build_site.py` → **OK (QA passée)** (88 actives, 30
clôturées, 118 fichiers). `python3 site/audit_qualite.py` → **0 bloquant**, 7 constats
restants (tous hors de mon périmètre, détaillés plus bas).

## PASS / FAIL par contrôle — 9 fiches du périmètre du jour

| Fiche | 1 Fraîcheur | 2 Concordance | 3 Honnêteté | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante |
|---|---|---|---|---|---|---|---|
| `fermeture\|DE-Sachsen-SaechsischeSchweiz\|…\|2026-08-01` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| `incendie\|Ariege-Bordes-Uchentein\|…\|2026-07-10` | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| `incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS |
| `incendie\|ES-CENTRO-Guadalajara-LaMierla\|…\|2026-07-16` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS |
| `incendie\|HautesAlpes-BoisNoir\|…\|2026-07-19` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS |
| `incendie\|Pyrenees-Atlantiques-Etsaut\|…\|2026-09-02` | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL → corrigé** |
| `risque-feu\|PO-66\|vigilance-rouge-…\|2026-07-26` | PASS | PASS | PASS | PASS | PASS (dégradation du jour validée) | PASS | PASS |
| `risque-feu\|Vaucluse-84\|fermeture-8-massifs\|2026-07-01` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS |

Détail des FAIL et de leur traitement :

- **Contrôle 7 (source vivante), `incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`** :
  la dernière citation de la section Source (lasemainedespyrenees.fr, 10/09, « le feu fixé et
  sous surveillance, survols de nouveau autorisés, accès au sol toujours strictement
  interdit ») n'avait pas d'URL — un lien markdown non fermé, invérifiable pour le lecteur.
  Recherche et vérification directe : l'article existe bien
  (`https://www.lasemainedespyrenees.fr/pyrenees-atlantiques-vallee-daspe-le-feu-fixe-la-zone-reste-interdite-dacces`,
  daté du 10/09/2026, contenu conforme au fait cité). URL ajoutée. Ce n'était pas une source à
  chercher, seulement une citation à compléter : dans mon périmètre.
- **Contrôle 2 (concordance), 5 fiches** : la « Portion concernée » portait une date de
  dernière constatation (« situation au 06/09 », « à ce jour (12/09/2026) », « vérifié
  jusqu'au 12/09 ») restée en retard d'un jour sur `verif: 2026-09-13`, alors que le `statut:`
  documente une re-vérification du jour donnant le même résultat. Écart sous le seuil
  bloquant de l'audit (7 j), mais c'est exactement le défaut n°1 du registre (portion
  périmée pendant que le fichier est à jour) : corrigé par réécriture à information
  constante, aucun fait ajouté ni supprimé — Sachsen, Drôme-Justin, ES-Centro-Guadalajara,
  Hautes-Alpes-Bois Noir, Vaucluse-84. `fermeture|FR-Baronnies-GR9|…` n'a PAS été touchée sur
  ce point : sa date du 12/09 est la bonne, la tentative de re-vérification du jour (page PNR
  Baronnies) a échoué à s'ouvrir, donc rien de plus récent n'a réellement été confirmé
  aujourd'hui.
- **Contrôle 5 (sévérité), `risque-feu|PO-66|…`** : dégradation HAUTE→MOYENNE appliquée par
  la veille aujourd'hui, motivée (10 jours sans communiqué nommant un massif en rouge +
  indice général repassé en orange, méthode déjà appliquée deux fois sur cette même fiche en
  août). Vérifiée : les deux articles titrespresse.com cités (12/09, 04/09) sont en ligne et
  disent bien ce que la fiche rapporte. Dégradation validée, rien à corriger.

## Autres constats de l'audit traités (hors périmètre du jour, temps disponible)

Deux fermetures récentes signalées par l'audit comme « validité expirée » étaient en réalité
un faux positif de l'outil : le seul chiffre présent dans `validite:` était la date de
l'événement lui-même (l'éboulement/la fermeture du 10/09), pas une échéance, faute d'un
marqueur de validité ouverte reconnu par le script. Corrigé par reformulation factuelle
(« jusqu'à nouvel ordre »), sans invention :
- `eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`
- `fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10`

## Corrections appliquées — récapitulatif par clé

1. `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01` — date de tête de « Portion concernée » 06/09→13/09 (situation confirmée inchangée).
2. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — date de vérification citée en fin de portion 12/09→13/09.
3. `incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16` — idem, 12/09→13/09.
4. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` — idem, 12/09→13/09.
5. `risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01` — idem, 12/09→13/09.
6. `incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02` — URL de source manquante retrouvée et ajoutée (contenu vérifié conforme).
7. `eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10` — `validite:` reformulée (faux positif « échéance dépassée »).
8. `fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10` — idem.

Aucune fiche n'a été clôturée, aucune sévérité changée par moi, aucune section « Zone
(détails) » ni « Source » réduite (garde-fou d'intégrité du build : 0 déclenchement).

## À traiter au prochain run de veille (nécessite une source nouvelle, hors de mon périmètre)

- `fermeture|DE-Sachsen-SaechsischeSchweiz|…|2026-08-01` — dernière source datée du 26/08
  (18 j). Rechercher une publication postérieure sur Kurort Rathen (nationalpark-saechsische-schweiz.de,
  saechsische-schweiz.de/aktuelles) avant l'échéance annoncée du chantier héliporté (~18/09) :
  vérifier si le Gamrig et la Rathener Straße rouvrent à cette date.
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — dernière source datée du 01/09
  (12 j). Rouvrir la liste de référence PNR Baronnies Provençales (échec de connexion
  aujourd'hui) pour confirmer si elle a évolué depuis. Rappel : la restriction municipale
  court structurellement jusqu'au 30/09, échéance de fin de saison à surveiller.
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — dernière source
  datée du 31/08 (13 j, arrêté préfectoral). Recherche ciblée d'un arrêté plus récent ou d'une
  levée sur ariege.gouv.fr/bordesuchentein.fr.
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — dernière source datée du 21/08 (23 j).
  Recherche ciblée sur mairie-die.fr/drome.gouv.fr d'un résultat de l'étude de risque en
  cours ou d'une échéance.
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` — dernière
  source datée du 24/08 (20 j). Recherche ciblée d'une suite à l'arrêté municipal du 15/08 sur
  ville-argentiere.fr/paysdesecrins.com.
- `fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04`
  — jamais revérifiée depuis sa détection (8 j). Revisiter il Dolomiti / CAI FVG.
- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — vérifiée il y a 14 j (seuil 12
  j). Le contenu détaillé de l'arrêté n°2026-1415 (PDF ONF, jamais lu) reste à recouper avec
  le tracé du GR® R2 : c'est la piste ouverte depuis le 30/08, toujours non tranchée.

Aucun de ces 7 constats n'est bloquant ; aucune correction de sévérité n'est recommandée au-delà
de celle déjà appliquée par la veille sur PO-66 (validée ci-dessus).
