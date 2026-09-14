# Verdict qualité du registre — 2026-09-14

Agent : `agents/verificateur-alertes.md`, distinct des 6 agents de recherche qui ont produit
ou modifié les fiches du jour (incendies Espagne/Corse/Var/Aude/Hérault/
Pyrénées-Orientales, remontée de sévérité Réunion). Aucune des fiches contrôlées ci-dessous
n'a été écrite par moi : audit indépendant, pas relecture de complaisance.

`python3 site/audit_qualite.py --ecrire` relancé en préambule : **8 constats, 0 bloquant**,
sur 121 fiches (90 actives). Périmètre de contrôle = ces 8 fiches, et elles seules (le
dossier complet n'a pas été relu).

Après corrections : `python3 site/build_site.py` → **OK (QA passée)** (90 actives, 31
clôturées, 121 fichiers). `python3 site/audit_qualite.py` relancé → **0 bloquant**, **6
constats résiduels** (5 faux positifs documentés ci-dessous + 1 fraîcheur réelle laissée à
la veille). Garde-fou d'intégrité du build (perte de texte) : 0 déclenchement.

## PASS / FAIL par contrôle — 8 fiches citées par l'audit

| Fiche | 1 Fraîcheur | 2 Concordance | 3 Honnêteté | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante |
|---|---|---|---|---|---|---|---|
| `fermetures-sentiers\|Réunion-974\|AP-2026-693\|2026-05-21` | PASS | PASS | PASS | PASS | PASS | PASS (corrigé) | PASS (vérifié) |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié) |
| `fermeture\|GR-E4-Creta-Samaria\|fermetures-meteo-repetees\|2026-07-16` | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| `incendie\|Ariege-Bordes-Uchentein\|GR10-ferme-Esbintz-Valier\|2026-07-10` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (source réachable, PDF non OCRisable) |
| `incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS |
| `incendie\|ES-NAV-Roncal-Urzainki\|feu-longue-duree-Pena-Gazpar\|2026-08-14` | PASS | PASS | PASS (corrigé) | PASS | PASS | PASS | n/a (pas de fermeture sourcée) |
| `incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié) |
| `risque-feu\|Gard-30\|fermetures-5-secteurs-rouges\|2026-07-01` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS |

Détail :

- **5 fiches rouges « source datée » (Réunion, Baronnies, Ariège, Drôme-Justin,
  Hautes-Alpes-Bois Noir)** : l'audit déterministe signale une source de plus de 10 jours
  sous une alerte HAUTE. Dans les 5 cas, la source la plus ancienne citée n'est pas la source
  réelle de l'interdiction : chacune repose sur un **arrêté (préfectoral ou municipal) « jusqu'à
  nouvel ordre »**, qui ne se republie pas tant qu'il n'est ni abrogé ni prolongé — les 5
  fiches documentent une revérification directe **le 14/09** (même jour) sans texte plus
  récent trouvé. Contrôle 7 vérifié par mes soins par récupération directe des pages :
  onf.fr (Réunion, arrêté n°2026-1415 confirmé en ligne), baronnies-provencales.fr (Baronnies,
  toujours datée du 01/09, 12 communes confirmées), ville-argentiere.fr (Bois Noir, arrêté du
  15/08 confirmé en ligne). Le PDF Ariège (bordesuchentein.fr) se télécharge (3,5 Mo) mais
  n'a pas pu être OCRisé par l'outil de vérification : source vivante, pas morte. Aucune
  correction requise ; ces 5 constats sont des faux positifs de l'heuristique d'audit, non de
  vrais défauts du registre.
- **`GR-E4-Creta-Samaria` — FAIL réel sur le contrôle 1** : `validite:` annonce des fermetures
  décidées AU JOUR LE JOUR (seuil 2 j), mais `verif: 2026-09-11` a 3 jours. Corriger exige de
  consulter le statut du 12, 13 ou 14/09 sur samaria.gr / crete.gov.gr — une source nouvelle,
  hors de mon périmètre (je ne fais pas de veille). Inscrit ci-dessous pour le prochain
  passage.
- **`ES-NAV-Roncal-Urzainki` — contrôle 3, corrigé** : le champ `validite:` citait une date
  d'échéance (07/09) qui, lue seule, donnait l'impression fausse d'une restriction expirée,
  alors qu'il n'y a jamais eu de fermeture officielle, seulement une consigne générale
  d'éloignement. Reformulé pour dire le constat en clair (aucune fermeture en vigueur), sans
  ajouter ni retirer un fait.
- **`Drome-Justin-Die` et `Gard-30` — contrôle 2, corrigés** : la « Portion concernée »
  affichait un état antérieur (vérification du 13/09 pour l'une, aucune mention du 04-14/09
  pour l'autre) pendant que `statut:`/« Zone (détails) » de la même fiche connaissaient déjà
  la situation du jour (erreur 503 sur drome.gouv.fr ; confirmation de presse du 10/09 +
  feu agricole isolé du 04/09 sur le Gard). Réécriture à information constante : aucun fait
  ajouté, seulement déplacé de « Zone (détails) » vers « Portion concernée ».

## Corrections appliquées — récapitulatif par clé

1. `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — « Zone (détails) » : suppression
   de la mention interne « 1ère ligne du registre pour le 974 », sans valeur pour le lecteur ;
   sigle « AP » développé en « arrêté préfectoral ».
2. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — « Portion concernée » : date de
   vérification 13/09→14/09, et mention de l'erreur 503 rencontrée ce jour sur drome.gouv.fr
   (au lieu de répéter la date de MAJ du 16/07, périmée).
3. `risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01` — « Portion concernée » :
   ajout de la confirmation de presse du 10/09 (Gard toujours en vigilance orange) et du feu
   agricole isolé du 04/09, déjà connus de « Zone (détails) » mais absents du texte affiché.
4. `incendie|ES-NAV-Roncal-Urzainki|feu-longue-duree-Pena-Gazpar|2026-08-14` — `validite:`
   reformulée pour énoncer d'abord l'absence de fermeture officielle, plutôt qu'une date
   d'échéance lue comme expirée.

Aucune fiche clôturée, aucune sévérité modifiée par moi, aucune section réduite (garde-fou
d'intégrité : 0 déclenchement).

## À traiter au prochain run de veille (nécessite une source nouvelle, hors de mon périmètre)

- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — **FAIL fraîcheur** :
  `verif: 2026-09-11` (3 j) sur une restriction décidée au jour le jour (seuil 2 j). Revérifier
  le statut du jour sur samaria.gr et auprès de la Région de Crète avant publication d'une
  nouvelle « Dernière vérif ».
- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — point non tranché déjà noté en
  `statut:` par la veille : le rattachement du Bras des Merles au GR® R2 repose sur des sites
  tiers (AllTrails, trails-viewer.com), pas sur le topo-guide FFRandonnée (page ffrandonnee.fr
  en 404 au dernier essai). À retenter pour confirmer ou infirmer le tracé exact.
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — Saillans, Montclar-sur-Gervanne,
  Beauvoisin et Bénivay-Ollon restent sans source directe malgré des mois de tentatives ;
  l'échéance structurelle de fin de saison (30/09) approche pour les 12 communes actives, à
  surveiller au prochain passage.

Aucun de ces 3 constats n'est bloquant ; aucune dégradation ni clôture de sévérité n'est
recommandée au-delà de ce que la veille a déjà appliqué aujourd'hui (remontée Réunion, motivée
par la lecture intégrale de l'arrêté n°2026-1415).
