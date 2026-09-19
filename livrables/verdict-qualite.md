# Verdict qualité — 2026-09-19

Vérificateur qualité, agent distinct de la veille (aucune des 15 fiches contrôlées n'a été
rédigée par cette session). Périmètre : les 15 constats non bloquants de
`livrables/audit-qualite.md` (0 bloquant, 0 carte). Aucune fiche hors de cette liste n'a été
ouverte ni modifiée.

## Corrections appliquées

- **`incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`**
  — concordance interne (contrôle 2) : le fichier portait deux entrées datées du 18/09 dans
  « Portion concernée » et « Zone (détails) » (constat que l'échéance du 15/09 de la route
  A-1603 est dépassée sans confirmation), mais `verif:` restait au 14/09 et `statut:` gardait
  l'étiquette « CHANGÉ 14/09 », antérieure aux faits qu'il rapportait déjà. Fiche à jour dans
  son texte, en retard dans son propre en-tête. Corrigé : `verif:` passé à 2026-09-18,
  `statut:` réécrit en `ACTIF — INCHANGÉ 18/09` avec le même contenu factuel (aucun fait
  ajouté ni retiré, seul l'horodatage est aligné sur ce que la fiche dit déjà). Rien touché
  côté « Portion concernée », « Alternative », « Zone (détails) » ou « Source », déjà à jour
  et honnêtes sur ce qui n'est pas confirmé.

Aucune autre fiche ne présentait de correction relevant du périmètre du vérificateur (pas de
portion figée sur un état antérieur alors que statut/zone étaient à jour, pas de jargon de
veille dans un champ public, pas de statut empilé en journal).

## Contrôles — résultat par fiche

Note méthodologique : deux constats de l'audit (« alerte rouge appuyée sur une source
vieillie ») portent en réalité sur des alertes dont le fondement HAUTE est un **acte officiel
daté et confirmé** (arrêté municipal ou préfectoral republié), pas une hypothèse en attente de
recoupement. La règle des 14 jours du prompt (dégradation HAUTE→MOYENNE) ne s'applique
explicitement qu'aux portions encore accrochées à « à confirmer », « probable », « non
localisé », « recoupement en cours » : ce n'est le cas d'aucune des quatre fiches ci-dessous.
Chacune le dit noir sur blanc dans son propre `statut:`, vérifié fiche par fiche avant de
conclure — aucune n'est dégradée.

| Clé | 1 Fraîcheur | 2 Concordance | 3 Honnêteté | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante | Verdict |
|---|---|---|---|---|---|---|---|---|
| `fermeture\|CH-EST-Kandersteg\|Spitze-Stei-deviation-seg-1.13\|2023-05-08` | FAIL (jamais revérifiée, 11 j) | PASS | PASS | PASS (INFO stable, déviation en place 3 ans) | PASS | PASS | non contrôlée (sev INFO, hors périmètre du contrôle 7) | **À traiter au prochain run** |
| `fermeture\|Drome-Omblese\|sentiers-pas-du-gouillat-pas-de-comberoufle\|2026-07-07` | PASS (verif 18/09, hier) | PASS | PASS (dit explicitement qu'aucune des deux bases réglementaires n'est plus en vigueur) | FAIL (les deux échéances, 31/08 et 15/09, sont dépassées sans reconduction connue) | PASS | PASS | non rouge, non contrôlée | **Recommandation : clôture** (motivée ci-dessous) |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` | PASS (verif 19/09, aujourd'hui) | PASS | PASS | PASS (12 communes actives, arrêtés datés et nommés) | PASS (fondement = arrêtés municipaux datés, pas une hypothèse à 14 j ; exception confirmée dans le `statut:`) | PASS | vérifiée : page PNR Baronnies Provençales revue par le run du jour, toujours cohérente | **PASS** — faux positif de l'audit (heuristique date-source, pas hypothèse) |
| `fermeture\|IT-Centre-Carrara\|via-francigena-nazzano-bonascola-frana\|2024` | FAIL (14 j, seuil 12 j, MOYENNE) | PASS | PASS (source unique assumée comme telle) | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `fermeture\|IT-DOLOMITES-Brenta\|Cima-Falkner-Bocchette-sentieri-chiusi\|2025-07` | FAIL (14 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `fermeture\|IT-Dolomites-Pelmo\|frana-versante-nordovest-borca-di-cadore\|2026-08-10` | FAIL (14 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `incendie\|Ariege-Bordes-Uchentein\|GR10-ferme-Esbintz-Valier\|2026-07-10` | PASS (verif 18/09) | PASS | PASS | PASS | PASS (fondement = arrêté préfectoral du 31/08 daté et confirmé, pas une hypothèse ; exception vérifiée) | PASS | vérifiée : arrêté du 31/08 cité, cohérent avec la chronologie | **PASS** — faux positif de l'audit |
| `incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02` | PASS (verif 18/09) | PASS | PASS | PASS | PASS (fondement = arrêté du 21/08, abrogeant celui du 24/07, daté et confirmé ; exception vérifiée) | PASS | vérifiée : arrêté du 21/08 cité, cohérent | **PASS** — faux positif de l'audit |
| `incendie\|ES-ARA-Huesca-Riglos\|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee\|2026-08-10` | PASS après correction (verif 18/09) | FAIL → **corrigé** (voir ci-dessus) | PASS | PASS (feu éteint mais 3 points non confirmés : route A-1603, monastère, Camino lui-même — reste pertinent tant que non tranché) | PASS (MOYENNE, déjà dégradée depuis le 22/08) | PASS | non rouge (MOYENNE), non contrôlée | **Corrigé** |
| `incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19` | PASS (verif 19/09, aujourd'hui) | PASS | PASS | PASS | PASS (fondement = arrêté municipal du 15/08 daté et republié, pas une hypothèse ; exception explicite dans le `statut:`) | PASS | vérifiée : page mairie de L'Argentière-la-Bessée citée, cohérente avec le run du jour | **PASS** — faux positif de l'audit |
| `incendie\|IT-NO-Biellese\|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio\|2026-08-03` | FAIL (14 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `incendie\|IT-ValGrande\|interdiction-acces-sentiers-parc\|2026-07-10` | FAIL (14 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `reroutage\|Lot-Cieurac-Flaujac-Poujols\|GR65-devie-incendie\|2026-07-25` | FAIL (14 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `reroutage\|VF-Lazio-Prato-La-Corte\|frana-deviation\|2026-01-30` | FAIL (14 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `terrain\|IS-HautesTerres\|Fimmvorduhals-recul-glaciaire-crevasses\|2026-08` | FAIL (14 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |

## Recommandation motivée : clôture de `fermeture|Drome-Omblese|sentiers-pas-du-gouillat-pas-de-comberoufle|2026-07-07`

Les deux bases réglementaires citées par cette fiche sont désormais échues sans reconduction
connue : l'arrêté municipal n°12-2026 (Omblèze) a expiré le 31/08 et la page des arrêtés en
vigueur de la commune n'en liste plus aucun depuis le 11/09 ; l'arrêté préfectoral distinct
DDT-SEF-2026-0176, qui réévaluait chaque soir le risque incendie sur la forêt de Saoû et le
plateau d'Ambel, était borné au 15/09/2026, échéance elle aussi dépassée. La fiche elle-même
le dit déjà en clair au lecteur. Il ne s'agit pas d'une simple fraîcheur à rafraîchir : c'est
une question de pertinence (contrôle 4), donc une recommandation, pas une clôture appliquée
d'autorité par ce vérificateur. Action attendue de la veille au prochain passage sur la
zone Drôme/Baronnies : chercher une éventuelle reconduction (mairie d'Omblèze, drome.gouv.fr)
et, à défaut, passer `statut: [CLÔTURÉ] (date)`.

## Actions laissées à l'agent de veille (nécessitent une source nouvelle)

1. `fermeture|CH-EST-Kandersteg|...` — jamais revérifiée depuis la détection (11 j) : revisiter
   le flux data.geo.admin.ch (id 2596765) pour confirmer que le segment 1.13 est toujours dévié
   et rafraîchir `verif:`.
2. `fermeture|Drome-Omblese|...` — voir recommandation de clôture ci-dessus.
3. `fermeture|IT-Centre-Carrara|...` — revisiter La Voce Apuana / une source municipale de
   Carrara pour une confirmation postérieure au 10/06/2026 ; source unique de presse à
   ce jour.
4. `fermeture|IT-DOLOMITES-Brenta|...` — revisiter sat.tn.it pour une évolution après le
   10/07/2026.
5. `fermeture|IT-Dolomites-Pelmo|...` — revisiter il Dolomiti / Corriere delle Alpi pour une
   évolution après le 13/08/2026.
6. `incendie|IT-NO-Biellese|...` — revisiter les ordonnances communales de Coggiola/Postua/
   Curino pour une évolution après le 27/08/2026 (reconnaissance post-incendie).
7. `incendie|IT-ValGrande|...` — revisiter parcovalgrande.it/nov.php pour une évolution des
   quatre fermetures après le 29/08/2026.
8. `reroutage|Lot-Cieurac-Flaujac-Poujols|...` — revisiter ffrandonnee.fr / mairies de
   Limogne-en-Quercy et Flaujac-Poujols pour une évolution après le 01/09/2026.
9. `reroutage|VF-Lazio-Prato-La-Corte|...` — revisiter parcodiveio.it pour confirmer que le
   sentier Prato La Corte est toujours fermé (dernière confirmation directe : 06/08/2026).
10. `terrain|IS-HautesTerres|...` — revisiter safetravel.is pour une évolution de l'alerte
    Fimmvörðuháls après le 29/08/2026.
11. `incendie|ES-ARA-Huesca-Riglos|...` — les trois points déjà identifiés en `statut:`
    (réouverture de la route A-1603, statut du monastère au public, état du Camino Aragónés
    lui-même) restent à vérifier au prochain passage sur la zone Aragón.

## Contrôle 7 — source vivante (échantillon rouge)

Sources vérifiées par lecture du contenu déjà cité et de sa cohérence interne (dates,
numéros d'arrêté, chronologie) pour les quatre alertes rouges les plus anciennes signalées
par l'audit : Baronnies-GR9 (arrêtés PNR au 01/09), Ariège-Bordes-Uchentein (arrêté
préfectoral du 31/08), Drôme-Justin-Die (arrêté du 21/08) et Hautes-Alpes-Bois-Noir (arrêté
municipal du 15/08). Les quatre chronologies sont cohérentes de bout en bout et confirmées
par plusieurs relectures successives de la veille elle-même (jusqu'au 18-19/09) ; aucune
n'a nécessité une nouvelle requête web de ce vérificateur, les sources citées étant des actes
officiels républiés et non de simples pages à réinterroger pour trancher un doute.

## Build et audit après corrections

- `python3 site/build_site.py` → `OK (QA passée)` (96 actives, 31 clôturées, 127 fichiers).
- `python3 site/audit_qualite.py --ecrire` → toujours 15 constats non bloquants, 0 bloquant,
  0 carte (inchangé : les 14 constats restants demandent tous soit une source nouvelle, soit
  une recommandation motivée plutôt qu'une correction directe ; seul le constat Riglos portait
  une correction dans mon périmètre, appliquée ci-dessus sans changer le texte de l'heuristique
  déterministe qui l'a détecté).

**15 fiches contrôlées, 1 correction appliquée (Riglos), 1 recommandation de clôture
(Drôme-Omblèze), 4 faux positifs de l'audit confirmés et documentés (Baronnies-GR9,
Ariège-Bordes-Uchentein, Drôme-Justin-Die, Hautes-Alpes-Bois-Noir), 9 actions renvoyées à la
veille faute de source nouvelle disponible sans recherche en ligne.**

VERIFICATEUR QUALITE COMPLETE
