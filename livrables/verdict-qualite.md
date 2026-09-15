# Verdict qualité du registre — 2026-09-15

Agent : `agents/verificateur-alertes.md`, distinct de l'agent qui a mené la veille du jour.
Aucune des fiches contrôlées ci-dessous n'a été écrite par moi : audit indépendant, pas
relecture de complaisance.

`livrables/audit-qualite.md` (déjà généré par `python3 site/audit_qualite.py --ecrire`) :
**15 constats, 0 bloquant**, sur 121 fiches (90 actives). Périmètre de contrôle = ces 15
fiches, et elles seules ; le dossier complet `livrables/alertes/` n'a pas été relu.

Après corrections : `python3 site/audit_qualite.py --ecrire` relancé → **0 bloquant, 12
constats résiduels** (tous des demandes de source nouvelle ou de revérification, transmises
ci-dessous à la veille). `python3 site/build_site.py` → **OK (QA passée)** (90 actives, 31
clôturées, 121 fichiers, registre 793 802 car.). Garde-fou d'intégrité du build (perte de
texte) : 0 déclenchement.

Note indépendante du périmètre : `python3 site/verif_faits.py` signale par ailleurs 3 fiches
avec des nombres apparemment « inventés » vs le dernier commit git (dont
`risque-feu|PO-66|…`) — vérification faite, ces écarts viennent de contenu ajouté par la
veille du jour (ex. le nouveau feu d'Opoul-Périllos, jamais présent au commit précédent), pas
d'une reformulation de ma part : je n'ai touché que le champ `validite:` de cette fiche, pas
sa prose « Zone (détails) ». Signalé pour mémoire, sans action de mon ressort.

## PASS / FAIL par contrôle — 15 fiches citées par l'audit

| Fiche | 1 Fraîcheur | 2 Concordance | 3 Honnêteté | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante |
|---|---|---|---|---|---|---|---|
| `conditions\|IS-Hautes-Terres\|traversee-deconseillee-fimmvorduhals-glacier\|2026-08-25` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS |
| `fermetures-sentiers\|Réunion-974\|AP-2026-693\|2026-05-21` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `fermeture\|Cotes-Armor-Trebeurden\|GR34-Pors-Mabo-Goas-Lagorn\|2026-08-06` | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `fermeture\|GR-E4-Creta-Samaria\|fermetures-meteo-repetees\|2026-07-16` | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| `incendie\|Ariege-Bordes-Uchentein\|GR10-ferme-Esbintz-Valier\|2026-07-10` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `incendie\|Pyrenees-Atlantiques-Etsaut\|feu-pas-ourtasse-gr10-evacuation\|2026-09-02` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | PASS (fiche du jour) |
| `incendie\|UK-Cairngorms-Glenmore\|wildfire-Strathnethy-C7-fermee\|2026-07-16` | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| `reroutage\|GR21-Loges-Bénouville\|glissement-fermeture\|2026-02-17` | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| `reroutage\|GR34-Finistère\|fermetures-érosion-2026\|2026-S1` | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| `reroutage\|GR34-rade-de-Brest\|nouveau-tracé-officiel\|2026-05-28` | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| `reroutage\|Pierrefiques-76\|déviation\|2025-05-18` | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| `risque-feu\|PO-66\|vigilance-rouge-fermeture-tous-massifs\|2026-07-26` | PASS | PASS (corrigé) | PASS | PASS | PASS | PASS | n/a (MOYENNE) |

15 fiches contrôlées. 3 FAIL corrigés par mes soins (concordance interne / validité
trompeuse). 7 FAIL de fraîcheur laissés à la veille (hors de mon périmètre : ils exigent une
revérification de source, pas une réécriture). 0 FAIL sur les contrôles 3, 4, 5 et 6.

### Détail — 5 alertes ROUGES « source datée de plus de 10 jours » : faux positifs vérifiés

L'audit déterministe signale une source de plus de 10 jours sous une alerte HAUTE pour
Réunion, Baronnies, Ariège, Drôme-Justin et Hautes-Alpes-Bois Noir. Dans les 5 cas, ce n'est
pas la fiche qui est en défaut : chacune repose sur un **arrêté (préfectoral ou municipal)
« jusqu'à nouvel ordre »**, qui ne se republie pas tant qu'il n'est ni abrogé ni prolongé — le
texte lui-même, pas sa date de republication, est la source de vérité. J'ai vérifié en direct
(contrôle 7, WebFetch) les 5 URL citées :
- `onf.fr` (Réunion) : l'arrêté n°2026-1415 du 27/08/2026 est toujours en ligne, téléchargeable.
- `baronnies-provencales.fr` (Baronnies) : page toujours datée « mise à jour le 01/09/26 »,
  12 communes nommément listées, cohérent avec la fiche.
- `bordesuchentein.fr` (Ariège) : l'arrêté du 31/08/2026 (Cap des Lauzes ↔ étang d'Ayes) est
  cité et disponible.
- `mairie-die.fr` (Drôme) : l'arrêté du 21/08/2026 est présenté comme applicable jusqu'à la
  fin des opérations d'étude et de sécurisation, donc toujours en vigueur.
- `ville-argentiere.fr` (Hautes-Alpes) : l'arrêté municipal du 15/08/2026 est cité comme la
  mesure en vigueur, réouverture conditionnée aux avis des autorités compétentes.

Sources vivantes, contenu conforme à ce que chaque fiche affiche : aucune correction requise.
Ces 5 constats sont des faux positifs de l'heuristique d'audit (elle ne sait pas distinguer
un arrêté « jusqu'à nouvel ordre » d'une alerte qui se serait tue), pas de vrais défauts du
registre. Transmis malgré tout ci-dessous, car une confirmation plus récente reste utile au
lecteur si l'occasion se présente.

## Corrections appliquées — récapitulatif par clé

1. `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25` —
   `validite:` reformulée : le champ citait « toujours actif au 12/09/2026 » comme unique
   repère temporel, lu par l'audit comme une échéance dépassée alors que l'avertissement
   safetravel.is reste actif sans levée annoncée. Réécrit « reste actif jusqu'à nouvel ordre »
   en tête de champ, à information constante (aucune date ni fait ajouté ou retiré).
2. `incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02` —
   « Portion concernée » réalignée sur le suivi déjà à jour : le texte affiché s'arrêtait au
   point du 07/09 (« stabilisé... 130 hectares ») alors que `statut:`/« Zone (détails) »
   documentaient déjà, au 15/09, un feu fixé et sous surveillance (reconnaissance drone du
   09/09 sans reprise) et un accès au sol toujours strictement interdit sans date de
   réouverture. Réécriture à information constante : rien n'est ajouté, l'état le plus récent
   déjà connu de la fiche est simplement remonté dans le texte public.
3. `risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26` — `validite:`
   reformulée : les dates du 11-12/09 citées comme dernier repère laissaient croire à une
   échéance dépassée, alors que le classement orange reste la donnée de référence faute de
   publication plus récente (déjà dit dans `statut:`). Ajout de « qui reste en vigueur
   jusqu'à nouvel ordre faute de publication plus récente », à information constante.

Aucune fiche clôturée, aucune sévérité modifiée par moi, aucune section réduite (garde-fou
d'intégrité du build : 0 déclenchement).

## À traiter au prochain run de veille (nécessite une source nouvelle ou une revérification, hors de mon périmètre)

**Revérification de fraîcheur (pas de doute sur le fond, juste une date à rafraîchir) :**

- `fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06` — `verif:
  2026-09-02` (13 j, seuil 12 j moyenne). Revisiter la page du comité FFRandonnée 22 pour
  confirmer que la déviation reste la seule information disponible.
- `incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16` — `verif:
  2026-09-02` (13 j). Revérifier cairngorms.co.uk / firescotland.gov.uk pour une éventuelle
  levée des dernières fermetures localisées (Ryvoan Trail, Lodge Trail, Green Lochan).
- `reroutage|GR21-Loges-Bénouville|glissement-fermeture|2026-02-17` — `verif: 2026-09-02`
  (13 j). Retenter une source 2026 postérieure à février (déjà signalé infructueux au run du
  05/08 ; recherche ciblée à refaire).
- `reroutage|GR34-Finistère|fermetures-érosion-2026|2026-S1` — `verif: 2026-09-02` (13 j).
  Revisiter finistere.ffrandonnee.fr pour confirmer qu'aucune des 15+ fermetures n'a évolué.
- `reroutage|GR34-rade-de-Brest|nouveau-tracé-officiel|2026-05-28` — `verif: 2026-09-02`
  (13 j). Confirmer que le reroutage pérenne reste stable (faible risque, mais la date de
  vérification doit être rafraîchie).
- `reroutage|Pierrefiques-76|déviation|2025-05-18` — `verif: 2026-09-02` (13 j). La validité
  annoncée court jusqu'au 18/09/2026 : revérifier avant cette échéance.
- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — `verif: 2026-09-11`
  (4 j, seuil 2 j : restriction décidée au jour le jour). Revérifier le statut du jour sur
  samaria.gr et crete.gov.gr avant toute nouvelle publication de « Dernière vérif ».

**Confirmation de maintien souhaitable (faux positifs vérifiés vivants par mes soins, non
urgents) :**

- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`

Pour ces 5, j'ai confirmé en direct (WebFetch, contrôle 7) que l'arrêté cité par chaque fiche
est toujours en ligne et toujours présenté comme en vigueur (voir détail ci-dessus) : aucune
dégradation ni action urgente. Une prochaine visite de zone peut simplement rafraîchir la date
si une publication plus récente existe, sans quoi l'audit continuera de les signaler par
construction (heuristique sur l'âge de la source, pas sur son contenu).

Aucune dégradation ni clôture de sévérité n'est recommandée sur les 12 fiches ci-dessus : dans
les 12 cas, le fond de l'alerte reste correctement établi par les fiches elles-mêmes.
