# Verdict qualité — 2026-08-16

Vérificateur qualité, agent distinct de la veille du jour : je n'ai écrit aucune des fiches
contrôlées (~25 fiches mises à jour aujourd'hui par 10 agents de veille distincts), je les
audite, je ne les refais pas. Périmètre = les 7 constats de `livrables/audit-qualite.md`
régénéré ce jour (87 alertes actives, 0 bloquant, 4 alertes, 3 infos avant ce passage).

**6 fiches contrôlées** (une fiche, Esterel-Tanneron FR-06, portait deux constats) :
- `incendie|AT-Vorarlberg-Silvretta|coulee-boue-sentiers-fermes|2026-07-12`
- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`
- `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`
- `risque-feu|Hérault-34|fermetures-massifs-quotidiennes|2026-07-02`
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`
- `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`

## Résumé PASS/FAIL par contrôle

| Contrôle | Résultat |
|---|---|
| 1. FRAÎCHEUR | PASS sur les 6 fiches (`verif: 2026-08-16` sur 5 ; Silvretta `2026-08-13`, 3 j, sous le seuil MOYENNE de 12 j) |
| 2. CONCORDANCE INTERNE | PASS sur les 6. Hérault-34 déclenchait l'audit (9 j d'écart apparent) mais c'est un faux positif du parseur de dates, détaillé ci-dessous — la fiche concorde réellement |
| 3. HONNÊTETÉ | PASS sur les 6 : chaque silence de source est déclaré en clair (« aucune échéance annoncée », « aucun communiqué à ce jour », « la préfecture n'a publié aucun point de situation depuis le 16/07 ») |
| 4. PERTINENCE | PASS. Silvretta n'est pas expirée : c'est une fermeture indéfinie mal formulée (corrigée), pas une échéance dépassée. Aucune clôture à faire |
| 5. SÉVÉRITÉ JUSTE | PASS. Albères-66 et Esterel-Tanneron : interdictions sourcées par arrêtés/communiqués datés, non expirées sur le fond — seule la fraîcheur de la source de presse est en cause, pas l'existence de l'interdiction. Sévérité maintenue HAUTE sur les deux, aucune dégradation d'autorité (règle des 14 jours vérifiée et jugée non applicable, voir note) |
| 6. TON | FAIL corrigé sur 3 fiches (Esterel-Tanneron « piège d'indexation », Drôme-Justin « recherche ciblée » / « règle d'escalade », Fontainebleau « au prochain passage ») |
| 7. SOURCE VIVANTE | Vérifié en direct (WebFetch) sur les 4 sources les plus récentes des fiches HAUTE : ouillade.eu (Albères, 29/07), presseagence.fr (Esterel, 05/08), drome-cestmanature.com (Justin, MAJ affichée désormais 14/08 contre 12/08 cité dans la fiche — même contenu, pas une perte), seine-et-marne.gouv.fr (Fontainebleau, MAJ 14/08). Les 4 répondent et portent exactement l'information citée |

## Corrections appliquées (dans mon périmètre, à information constante)

- `incendie|AT-Vorarlberg-Silvretta|coulee-boue-sentiers-fermes|2026-07-12` — VALIDITÉ :
  le champ `validite:` se terminait par « restent fermés au 13/08/2026 », lu par l'audit
  déterministe comme une échéance dépassée alors que c'est une fermeture indéfinie (aucune
  date de réouverture des sentiers n'est publiée par aucune des sources déjà citées dans la
  fiche). Réécrit en clarifiant : « maintenue jusqu'à nouvel ordre : aucune source ne
  documente d'échéance de réouverture […] (dernière confirmation directe de leur fermeture :
  13/08/2026) ». Aucun fait nouveau, seule l'ambiguïté de formulation est levée.
- `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17` — TON : « Zone
  (détails) » disait qu'un article francebleu.fr « s'est révélée être un piège
  d'indexation » (jargon de veille). Reformulé pour le lecteur : « semblait au premier abord
  apporter une confirmation récente, mais porte en réalité sur une autre année », le constat
  de fond (jour de semaine incohérent, article de 2023) restant identique au caractère près.
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — TON : « recherche ciblée […]
  conformément à la règle d'escalade » (vocabulaire de mécanique de veille) reformulé en
  « vérification élargie aux sources officielles autres que drome.gouv.fr », même fait, sans
  jargon.
- `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` — TON :
  « à rechercher spécifiquement au prochain passage » (banni explicitement par
  `agent-prompt.md`) reformulé en « son état après le 16/08 reste à confirmer » — dit au
  lecteur ce qui n'est pas su, sans référence à la mécanique de la veille.

`python3 site/verif_faits.py` vs HEAD est inexploitable tel quel aujourd'hui : il compare au
dernier commit, qui précède les ~25 mises à jour non commitées des 10 agents de veille du
jour, et signale donc en masse des « nombres inventés » qui sont en réalité le contenu ajouté
ce matin (dates du 16/08, numéros d'arrêtés, etc.), sur des fiches que je n'ai pas touchées.
Vérification faite à la place par comparaison directe avant/après sur chacun de mes 4 edits :
aucun nombre, date, URL ou nom propre perdu ni ajouté — seule la formulation change.

## Hérault-34 : faux positif de l'audit, aucune correction

`risque-feu|Hérault-34|fermetures-massifs-quotidiennes|2026-07-02` était signalé « Portion
concernée parle du 07/08 alors que le suivi connaît la situation au 16/08 (9 j d'écart) ».
Relecture : la « Portion concernée » décrit bien l'état courant (« au dernier classement
connu, publié […] pour le samedi 15 août 2026, aucun secteur n'est classé en rouge […] 7 des
9 secteurs […] en orange ») et ne cite le 07/08 que comme point de comparaison historique
(« C'est une décrue par rapport au classement du 07/08 »). Le parseur de dates de l'audit ne
lit que les dates au format chiffré (dd/mm) et ignore les dates en toutes lettres (« samedi
15 août ») : il retient donc le 07/08 comme date la plus récente de la portion alors que le
texte est à jour. Concordance réelle avec `statut:` et « Zone (détails) » (MAJ 16/08, même
lecture de la carte @Prefet34) : PASS. Aucune fiche modifiée.

## Note motivée — sévérité non dégradée sur Albères-66 et Esterel-Tanneron

Les deux fiches sont signalées pour une source de presse vieillissante (29/07 et 05/08) sous
une alerte ROUGE. Dans les deux cas, l'interdiction elle-même repose sur un texte daté et non
expiré (arrêtés Sorède/Argelès pour les Albères ; classement quotidien préfectoral pour
l'Esterel, dont le motif — épisode de canicule et risque très sévère — reste en vigueur sans
signal de fin), pas sur une hypothèse à confirmer. La règle des 14 jours de
`agent-prompt.md` (dégradation HAUTE→MOYENNE) vise spécifiquement une « Portion concernée »
encore adossée à « à confirmer »/« probable »/« non localisé » : ce n'est le cas d'aucune des
deux. Elle ne s'applique donc pas ; aucune dégradation appliquée d'autorité. Les deux fiches
documentent déjà elles-mêmes cette tension et se sur-vérifient à chaque run (« zone en
escalade »).

## À traiter au prochain run (nécessite une source neuve, hors de mon périmètre)

- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — retrouver une publication de
  presse ou officielle postérieure au 29/07/2026 sur l'état d'accès au massif des Albères.
- `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17` — confirmer le
  classement du jour (aucune publication postérieure au 06/08 trouvée par la veille malgré
  plusieurs tentatives) ; si l'écart continue de croître sans confirmation, réexaminer la
  sévérité au prochain passage.
- `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` — la mesure
  distincte sur les bois et forêts de l'Essonne (hors Trois-Pignons) arrivait à échéance le
  16/08 ; aucun communiqué sur sa suite (prolongation ou levée) n'a été trouvé à ce jour.
  Volet Seine-et-Marne (5 massifs, jusqu'au 21/08) non concerné, déjà confirmé par source
  officielle.

## Recommandations de sévérité non appliquées d'autorité

Aucune. Les deux dégradations envisageables (Albères-66, Esterel-Tanneron) ont été examinées
et jugées non fondées à ce stade (voir note motivée ci-dessus) : recommandation = maintenir
HAUTE sur les deux, à réexaminer si l'écart de fraîcheur de source continue de croître sans
qu'une confirmation ne soit trouvée.

## Vérifications techniques après corrections

- `python3 site/audit_qualite.py --ecrire` : **3 constats restants** (Albères-66 et
  Esterel-Tanneron, sources de presse vieillies, signalées ci-dessus, hors périmètre ;
  Hérault-34, faux positif documenté ci-dessus), **0 bloquant**, contre 4 alertes + 3 infos
  sur ces 6 fiches avant ce passage. Section carte : 0 bloquant, 0 alerte perdue.
- `python3 site/build_site.py` : **OK (QA passée)** → `site/index.html` (69 actives, 18
  clôturées, 87 fichiers, registre 474 447 car.). Le « ⚠ ton » résiduel (2 fiches ES-CYL,
  jargon « indexation ») ne concerne pas les fiches de ce passage et n'a pas été touché
  (non citées par l'audit).
- Garde-fou d'intégrité (perte > 45 % par fiche) : non approché, mes 4 corrections sont des
  reformulations ponctuelles d'une à deux phrases, jamais des réécritures de section.
