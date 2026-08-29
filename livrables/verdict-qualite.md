# Verdict qualité du registre — 2026-08-29

Agent Vérificateur Qualité, distinct des 4 sous-agents de veille du jour (FR-CORSE/FR-13/
FR-83/FR-06/FR-04-05 ; FR-30-48/FR-34-11/FR-66/FR-84-26-07 ; ES-GAL/ES-CYL/ES-AND/
PT-CENTRO-SUL ; IT-NO/IT-DOLOMITES/IT-CENTRE/IS/DE-Sachsen) : aucune des fiches
contrôlées ci-dessous n'a été rédigée par cet agent, la condition d'indépendance est
respectée, y compris pour les trois fiches touchées aujourd'hui par la veille (Var-83,
Drôme-Justin-Die, IT-ValGrande) — je les contrôle, je ne les relis pas comme mon propre
travail.

Périmètre de travail : les 7 constats de `livrables/audit-qualite.md` (généré le jour
même par `python3 site/audit_qualite.py --ecrire` avant mon passage — relancé une
deuxième fois par moi pour confirmer, résultat identique) — 0 bloquant, 5 alertes,
2 dettes de forme. Aucune autre fiche du registre (101 fichiers, 76 actives) n'a été
ouverte ni touchée.

## Fiches contrôlées (7)

1. `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — alerte fraîcheur
2. `fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06` — alerte fraîcheur
3. `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — alerte source vieillie (rouge)
4. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — alerte décrochage Portion/suivi
5. `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` — alerte fraîcheur
6. `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — dette de forme (jargon)
7. `risque-feu|Var-83|fermetures-massifs-quotidiennes|2026-07-08` — dette de forme (jargon)

## PASS / FAIL par contrôle

| Contrôle | Résultat |
|---|---|
| 1. FRAÎCHEUR | FAIL sur #1 (23 j, seuil 12 j), #2 (jamais revuérifiée depuis la détection, 10 j) et #5 (22 j, seuil 12 j) : les trois nécessitent une source nouvelle (carte ONF, comité FFRandonnée 22, site Camins de Pedra) que seule la veille peut apporter au prochain passage sur ces zones. PASS sur #3, #4, #6, #7 : toutes revuérifiées ce jour même (`verif: 2026-08-29`) ou dans le délai de leur sévérité. |
| 2. CONCORDANCE INTERNE | FAIL initial sur #4 (Drôme) : « Portion concernée » citait comme dernière date le 21/08 alors que `statut:` savait déjà, au 29/08, qu'aucune levée n'était intervenue et que drome.gouv.fr restait figé au 16/07 — c'est le défaut n°1 du registre. Corrigé (voir ci-dessous), PASS après correction. PASS sur #3 : « Portion concernée », `statut:` et « Zone (détails) » racontent la même chose (fermeture Ayès↔Cap des Lauses au 02/08, silence de l'arrêté feu depuis le 24/08), aucune divergence. Non applicable à #1, #2, #5 (aucun décrochage relevé par l'audit sur ces fiches, seulement de la fraîcheur). |
| 3. HONNÊTETÉ SUR CE QU'ON NE SAIT PAS | PASS sur #3 (Ariège) : le texte dit noir sur blanc au lecteur qu'aucune 5e reconduction ni levée de l'arrêté feu n'est publiée à ce jour, sans le présenter comme probable. PASS sur #4 (Drôme) après correction : « aucune levée de l'arrêté du 21/08 n'a été annoncée » est maintenant explicite dans le texte public. PASS sur #5 (Mallorca) : la fiche dit explicitement que l'échéance du 15/08 est dépassée sans confirmation de réouverture. |
| 4. PERTINENCE | PASS sur les 7 : aucune n'a plus lieu d'être (aucun signal de levée, de réouverture ou de tracé redevenu officiel n'a été trouvé dans les fiches elles-mêmes) ; aucune clôture recommandée. |
| 5. SÉVÉRITÉ JUSTE | PASS sur #3 (Ariège, HAUTE) — voir motivation détaillée ci-dessous, § « Ariège : décision sur la sévérité ». PASS sur #4 (Drôme, HAUTE, arrêté du 21/08 confirmé par source officielle relayée par la mairie de Die). PASS sur #1, #2, #5, #6, #7 (MOYENNE, cohérente avec des restrictions réelles sans interdiction rouge injustifiée). |
| 6. TON | FAIL initial sur #6 (IT-ValGrande, « piège d'indexation ») et #7 (Var-83, « piège d'indexation »), jargon de veille dans « Zone (détails) ». Corrigés, PASS après correction. Non applicable à #1-#5. |
| 7. SOURCE VIVANTE (alerte rouge #3 uniquement) | PASS. Les deux sources les plus citées ont été re-fetchées indépendamment : pyreneesfm.com (18/08, reconduction du feu jusqu'au 24/08, aucune mention GR10) et France3 Occitanie (04/08, ferme la portion Ayès↔Cap des Lauses depuis le 02/08 pour chutes de pierres) répondent toutes deux et portent bien l'information annoncée dans la fiche. Aucune source morte sous cette alerte rouge. |

## Ariège : décision sur la sévérité (constat #3, traitement prioritaire)

L'audit signale une alerte ROUGE appuyée sur une source datée du 18/08 (11 j). J'ai
vérifié `detection: 2026-07-20` (40 j) et testé l'applicabilité de la règle des 14 jours
de `agent-prompt.md` (§ DURÉE DE VIE D'UNE HYPOTHÈSE).

Cette règle vise une « Portion concernée » qui repose encore sur « à confirmer » /
« probable » / « non localisé » plus de 14 jours après détection. Ce n'est pas le cas
ici : le contrôle déterministe #5 de l'audit (hypothèse jamais tranchée) ne s'est
d'ailleurs pas déclenché sur cette fiche, faute de marqueur d'hypothèse dans « Portion
concernée ». Le fait qui porte la sévérité HAUTE — la fermeture du GR®10 entre l'étang
d'Ayès et le Cap des Lauses depuis le 02/08, pour chutes de pierres sur un sol
déstabilisé par l'incendie — est établi par trois sources de presse indépendantes et
datées (France 3 Occitanie 04/08, ruralites2024.fr 03/08, radiocouserans.fr 02/08),
toutes deux re-vérifiées vivantes par moi ce jour pour au moins la première. C'est un
fait constaté, pas une hypothèse en attente de confirmation.

Ce que l'audit détecte réellement, c'est que le texte du « Source » ne contient aucune
URL datée après le 18/08 : la source la plus récente qui y est citée porte sur l'arrêté
préfectoral d'interdiction totale de l'usage du feu (distinct de la fermeture du GR10),
dont la veille documente elle-même l'absence de 5e reconduction depuis 4 jours de
recherches ciblées répétées. Dégrader la sévérité par prudence excessive reviendrait à
punir une fiche qui a déjà correctement isolé ce qui est confirmé (fermeture GR10) de ce
qui ne l'est pas (statut de l'arrêté feu), et qui le dit en clair au lecteur.

**Décision : je ne dégrade PAS la sévérité.** Je signale la source vieillissante comme
action à traiter au prochain passage FR-PYR-O (voir ci-dessous), sans appliquer la règle
des 14 jours qui ne s'applique pas à cette situation.

## Corrections appliquées (dans mon périmètre, à information constante)

- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — décrochage entre « Portion
  concernée » (dernière date citée : 21/08) et `statut:` (qui sait, au 29/08, qu'aucune
  levée n'est intervenue et que drome.gouv.fr n'a pas bougé depuis le 16/07). Ajouté en
  fin de « Portion concernée » : « Situation inchangée à la vérification du 29/08/2026 :
  aucune levée de l'arrêté du 21/08 n'a été annoncée, et drome.gouv.fr reste daté du
  16/07/2026 sans mise à jour. » Réécriture à information constante : rien n'est ajouté
  qui ne figurait déjà dans `statut:` et « Zone (détails) ».
- **`incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10`** — dans « Zone
  (détails) », remplacé « Piège d'indexation signalé : une page … » par « Précision :
  une autre page du même site … », en gardant intacts la page citée, sa date réelle
  (03/05/2022) et la conclusion (source non retenue). Jargon retiré, aucun fait modifié.
- **`risque-feu|Var-83|fermetures-massifs-quotidiennes|2026-07-08`** — dans « Zone
  (détails) », remplacé « … (probablement 2025, où le 29 août était un vendredi) ;
  piège d'indexation, non retenu. » par « … (probablement 2025, où le 29 août était un
  vendredi), donc non retenu. » Jargon retiré, aucun fait modifié.

Après ces trois corrections : `python3 site/build_site.py` rend **OK (QA passée)**
(76 actives, 25 clôturées, 41 digests, 101 fichiers). `python3 site/audit_qualite.py`
ne signale plus aucun bloquant ni aucune dette de forme sur les fiches touchées : il
reste 4 constats, tous en dehors de mon périmètre (voir section suivante), 0 bloquant.

## Actions laissées à l'agent de veille (nécessitent une source nouvelle)

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — vérifiée il y a 23
  jours (seuil 12 j, sévérité moyenne). Action : consulter la carte ONF interactive
  (recommandation déjà notée dans `statut:`) pour confirmer le maintien de l'AP
  2026-693, une recherche texte simple ayant déjà échoué à le faire au 06/08.
- **`fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06`** — jamais
  revuérifiée depuis sa détection (10 j). Action : confirmer auprès du comité
  FFRandonnée 22 (ou de la mairie de Trébeurden) si la déviation balisée et la fermeture
  du tronçon Pors Mabo↔Goas Lagorn sont toujours en place.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — source la
  plus récente citée datée du 18/08 (11 j). Action pour le prochain passage FR-PYR-O :
  recherche ciblée d'une publication plus récente que le 18/08, sur deux fronts
  distincts — (a) l'état du tronçon Ayès↔Cap des Lauses lui-même (une réouverture a-t-elle
  été annoncée ?) et (b) le sort de l'arrêté préfectoral d'interdiction totale du feu,
  échu depuis le 24/08 sans 5e reconduction ni levée retrouvée à ce jour. Ne pas
  dégrader par défaut : voir ma motivation ci-dessus, la sévérité HAUTE repose sur le
  fait de fermeture (établi), pas sur cet arrêté.
- **`refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`** — vérifiée il y a 22
  jours (seuil 12 j, sévérité moyenne), échéance annoncée (15/08) dépassée depuis 14
  jours. Action : relire caminsdepedra.conselldemallorca.es/en/refuges pour trancher la
  réouverture effective des refuges du Consell de Mallorca.

Aucune suppression, aucune clôture, aucune dégradation ou remontée de sévérité n'a été
appliquée d'autorité par cet agent.
