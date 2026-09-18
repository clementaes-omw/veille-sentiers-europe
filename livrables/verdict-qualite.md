# Verdict qualité du registre — 2026-09-18

Vérificateur qualité distinct de l'agent de veille du jour (confirmé : `git log` sur
`livrables/alertes/` et `livrables/digest_2026-09-18.md` montre uniquement des commits
« veille: … » antérieurs à mon intervention ; aucune des 16 fiches examinées n'a été
écrite par cette session).

Périmètre : les 16 fiches citées par `livrables/audit-qualite.md` du 2026-09-18
(0 bloquant, 16 avertissements, 0 info avant intervention). Aucune autre fiche du
registre (96 actives) n'a été ouverte ni modifiée.

## PASS / FAIL par contrôle (sur les 16 fiches auditées)

1. **FRAÎCHEUR** — FAIL sur 9 fiches (revérification au-delà du seuil de leur propre
   sévérité) : `CH-EST-Kandersteg` (jamais revérifiée, 10 j depuis détection) et 8 fiches
   MOYENNE vérifiées à 13 j pour un seuil de 12 j (`IT-Centre-Carrara`,
   `IT-DOLOMITES-Brenta`, `IT-Dolomites-Pelmo`, `IT-NO-Biellese`, `IT-ValGrande`,
   `Lot-Cieurac-Flaujac-Poujols`, `VF-Lazio-Prato-La-Corte`, `IS-HautesTerres`). Non
   corrigeable sans nouvelle source : signalé au prochain run. PASS sur les 7 autres.
2. **CONCORDANCE INTERNE** — FAIL initial sur 1 fiche : `Pyrenees-Atlantiques-Etsaut`
   (Portion concernée figée sur le point du 10/09 alors que `statut:` connaissait déjà
   le 18/09). **Corrigé** (réécriture à information constante). PASS sur les 15 autres,
   y compris après correction.
3. **HONNÊTETÉ SUR CE QU'ON NE SAIT PAS** — PASS sur les 16 : chaque incertitude
   documentée (communes disparues des listes PNR Baronnies, statut du Camino Aragónés
   post-incendie, tronçon Seix/Auzat en Ariège…) est formulée en clair pour le lecteur,
   pas présentée comme un fait acquis.
4. **PERTINENCE** — FAIL sur 1 fiche : `Drome-Omblese` (les deux bases réglementaires
   citées — arrêté municipal n°12-2026 et arrêté préfectoral DDT-SEF-2026-0176 — sont
   désormais toutes deux échues, sans reconduction retrouvée). **Recommandation de
   clôture au prochain passage**, non appliquée d'autorité (hors périmètre de
   correction directe). PASS sur les 15 autres.
5. **SÉVÉRITÉ JUSTE** — FAIL signalé par l'audit sur 4 fiches ROUGE dont la source de
   presse datée dépasse 10 j (`FR-Baronnies-GR9` 17 j, `Ariege-Bordes-Uchentein` 18 j,
   `Drome-Justin-Die` 28 j, `HautesAlpes-BoisNoir` 25 j). Examen des 4 fiches : dans
   chaque cas la fermeture repose sur un **arrêté daté « jusqu'à nouvel ordre »**, pas
   sur une hypothèse à recouper (aucune de ces 4 fiches n'active le déclencheur
   BLOQUANT « hypothèse jamais tranchée » de l'audit — 0 bloquant sur l'ensemble du
   run). **Recommandation : maintenir HAUTE**, l'âge de la source de presse ne rend pas
   l'arrêté caduc ; rechercher une publication plus récente reste utile mais la
   dégradation n'est pas justifiée en l'état. Pas de fiche ne relevant de la règle des
   14 jours (aucun marqueur « à confirmer »/« probable » porté par ces portions).
6. **TON** — PASS sur les 16 : aucun jargon de veille (« ce run », « recherche ciblée »,
   « au registre »…) dans les sections publiques ; confirmé par 0 info à l'audit avant
   et après intervention.
7. **SOURCE VIVANTE** — contrôlé sur les 5 fiches ROUGE du lot (`FR-Baronnies-GR9`,
   `Ariege-Bordes-Uchentein`, `Drome-Justin-Die`, `HautesAlpes-BoisNoir`,
   `Pyrenees-Atlantiques-Etsaut`) : sources principales citées (baronnies-provencales.fr,
   bordesuchentein.fr, mairie-die.fr, ville-argentiere.fr, hautes-alpes.fr,
   lasemainedespyrenees.fr) toutes répondent (200 ; un 403 initial sur hautes-alpes.fr
   n'était qu'un blocage anti-bot lié au user-agent, confirmé vivant en 200 avec un
   en-tête standard). PASS sur les 5.

## Corrections appliquées (dans le périmètre, à information constante)

- **`incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`**
  — Portion concernée réécrite pour porter l'état du 18/09 (déjà connu de `statut:`) au
  lieu de rester figée sur le point du 10/09.
- **`fermeture|Drome-Omblese|sentiers-pas-du-gouillat-pas-de-comberoufle|2026-07-07`**
  — `validite:`, Portion concernée, `statut:` et chronologie de Zone (détails) réécrits :
  les deux échéances citées (31/08 municipal, 15/09 préfectoral) sont désormais toutes
  deux dépassées sans reconduction retrouvée dans les sources déjà citées ; le constat
  est posé en clair pour le lecteur.
- **`incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`**
  — `validite:`, Portion concernée, Alternative, `statut:` et chronologie réécrits :
  l'échéance du 15/09/2026 pour la route A-1603 est désormais dépassée sans confirmation
  de levée ; posé en clair, sans invention de fait nouveau.

Après ces 3 corrections : `python3 site/audit_qualite.py` passe de 16 à 15 constats
(la concordance Etsaut a disparu), toujours **0 bloquant**. `python3 site/build_site.py`
rend `OK (QA passée)` (96 actives, 31 clôturées, 127 fichiers). Aucune fiche n'a perdu de
texte (les 3 diffs sont des insertions nettes, +18/+12/+2 lignes).

## Actions laissées à l'agent de veille (prochain run, hors mon périmètre)

Ces 13 fiches exigent une source nouvelle ou une recherche ciblée ; je ne les ai pas
modifiées :

1. `fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08` — jamais
   revérifiée depuis détection (10 j) : relire le flux data.geo.admin.ch (id 2596765).
2. `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — source PNR datée du
   01/09 (17 j) : rechercher une mise à jour plus récente de la liste PNR Baronnies
   Provençales ou de la préfecture. Maintien HAUTE recommandé en l'absence de nouveau
   signal (fondement = arrêtés nommés et datés).
3. `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — arrêté du
   31/08 (18 j) : rechercher un acte plus récent (ariege.gouv.fr, bordesuchentein.fr).
   Maintien HAUTE recommandé (arrêté « jusqu'à nouvel ordre » toujours en vigueur).
4. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — arrêté du 21/08 (28 j) : idem,
   surveiller l'issue de l'étude de risque en cours.
5. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` —
   arrêté municipal du 15/08 (25 j) : idem, surveiller les avis des autorités
   compétentes en vue d'une réouverture.
6. `fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024` —
   revérifier (13 j / seuil 12 j MOYENNE).
7. `fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07` —
   revérifier (13 j / seuil 12 j).
8. `fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10` —
   revérifier (13 j / seuil 12 j).
9. `incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`
   — revérifier (13 j / seuil 12 j).
10. `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — revérifier
    (13 j / seuil 12 j).
11. `reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25` — revérifier
    (13 j / seuil 12 j).
12. `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30` — revérifier
    (13 j / seuil 12 j).
13. `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08` —
    revérifier (13 j / seuil 12 j).

Et une recommandation de fond, non appliquée d'autorité :
- `fermeture|Drome-Omblese|sentiers-pas-du-gouillat-pas-de-comberoufle|2026-07-07` —
  **clôture recommandée** au prochain passage si aucune source de reconduction n'est
  trouvée (les deux bases réglementaires citées sont désormais échues).
- `incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`
  — nouvelle source nécessaire pour trancher trois points restés ouverts : réouverture
  de la route A-1603 (échéance du 15/09 dépassée), statut du monastère au public, état
  du Camino Aragónés lui-même.

## Fiches contrôlées

16 fiches contrôlées (liste ci-dessus), 3 corrigées, 13 signalées au prochain run, dont
1 avec recommandation de clôture et 1 avec recommandation de maintien de sévérité
malgré l'âge de la source (×4, cf. contrôle 5).
