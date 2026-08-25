# Verdict qualité — 2026-08-25

Vérificateur qualité, agent distinct de la veille (voir `agents/verificateur-alertes.md`).
Périmètre : les 6 fiches citées par `livrables/audit-qualite.md` du jour, plus 1 fiche
signalée par l'opérateur pour vérification d'un correctif déjà appliqué en amont
(`incendie|Drome-Justin-Die`). **7 fiches contrôlées** sur 98 (le reste du dossier n'a pas
été relu, conformément au périmètre).

Contrôles appliqués : les 7 de `agents/verificateur-alertes.md`
(1 FRAÎCHEUR, 2 CONCORDANCE INTERNE, 3 HONNÊTETÉ, 4 PERTINENCE, 5 SÉVÉRITÉ JUSTE, 6 TON,
7 SOURCE VIVANTE).

## Résultat par fiche

### `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`
1 FRAÎCHEUR **FAIL** — vérifiée il y a 11 j, seuil 2 j (fermetures décidées au jour le jour).
2 CONCORDANCE **PASS** · 3 HONNÊTETÉ **PASS** · 4 PERTINENCE **PASS** · 5 SÉVÉRITÉ **PASS**
(MOYENNE cohérente) · 6 TON **PASS** · 7 non requis (MOYENNE).
→ Hors périmètre du run du jour (zone Crète = lot T2 du vendredi). Aucune source nouvelle
disponible pour trancher si la gorge est ouverte ou fermée aujourd'hui : **signalé, non
corrigé**, cf. « à traiter au prochain run ».

### `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`
1 FRAÎCHEUR **FAIL** — vérifiée il y a 19 j, seuil 12 j.
2 CONCORDANCE **PASS** · 3 HONNÊTETÉ **PASS** · 4 PERTINENCE **PASS** · 5 SÉVÉRITÉ **PASS**
· 6 TON **PASS** · 7 source ONF testée, répond (200), non requis à ce niveau de sévérité.
→ Hors périmètre du jour. **Signalé, non corrigé.**

### `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`
1 FRAÎCHEUR **PASS** (`verif:` du jour même). 2 CONCORDANCE **PASS** · 3 HONNÊTETÉ **PASS**
(le texte dit explicitement quelles communes ne sont pas confirmées) · 4 PERTINENCE **PASS**
· 6 TON **PASS** · 7 SOURCE VIVANTE **PASS** (les 6 URL de la section Source répondent 200,
testées ce jour).
5 SÉVÉRITÉ **PASS — verdict indépendant.** L'audit signale une source datée du 12/08 (13 j)
sous une alerte rouge ; relecture complète de la fiche : ce qui fait foi n'est pas un article
de presse mais la **liste officielle du PNR Baronnies Provençales**, qui recense nommément
26 communes sous arrêté municipal daté (le plus récent, La Charce, du 10/08), et qui a été
**revérifiée en direct le 24/08/2026** (hier), sans changement. L'ancienneté affichée (« MAJ
12/08 ») est la date de dernière modification du contenu de la page, pas la date de la
dernière vérification par la veille. Aucun arrêté cité n'a d'échéance dépassée. Sévérité HAUTE
maintenue, aucune dégradation appliquée.

### `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`
1 FRAÎCHEUR **PASS** (`verif:` du 22/08, 3 j). 2 CONCORDANCE **PASS** · 3 HONNÊTETÉ **PASS**
· 4 PERTINENCE **PASS** (fermeture résiduelle réelle, 20 % du massif) · 5 SÉVÉRITÉ **PASS**
(MOYENNE cohérente) · 6 TON **PASS** · 7 non requis (MOYENNE), sources contrôlées vivantes.
Constat initial de l'audit : « validité expirée le 22/08 ». **Vérification directe** : le
22/08 est la date de RÉOUVERTURE de 80 % du massif (déjà passée par construction), pas une
échéance de fermeture — la fermeture résiduelle des parcelles brûlées n'a « aucune échéance
annoncée ». C'est une ambiguïté de formulation qui a fait lire au script déterministe une date
de réouverture comme une date d'expiration, exactement le type de faux positif déjà rencontré
sur `Drome-Justin-Die`. Aucune source nouvelle n'était nécessaire : **corrigé moi-même**
(champ `validite:` reformulé, aucun fait ajouté ni retiré). Confirmé : ne réapparaît plus dans
l'audit après correction.

### `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`
1 FRAÎCHEUR **FAIL** — vérifiée il y a 18 j, seuil 12 j ; l'échéance de fermeture annoncée
(15/08) est elle-même dépassée sans confirmation de réouverture.
2 CONCORDANCE **PASS** · 3 HONNÊTETÉ **PASS** (la fiche dit explicitement que la réouverture
n'est pas confirmée) · 4 PERTINENCE — signal, cf. ci-dessous · 5 SÉVÉRITÉ **PASS** · 6 TON
**PASS** · 7 source testée, répond (200).
→ Hors périmètre du jour. **Signalé, non corrigé** : nécessite de revérifier si les refuges
ont rouvert après le 15/08, information que seule une nouvelle lecture de la source peut
donner.

### `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`
1 FRAÎCHEUR **PASS** (`verif:` du jour même). 2 CONCORDANCE **PASS** · 3 HONNÊTETÉ **PASS**
· 4 PERTINENCE **PASS** · 6 TON **PASS**.
5 SÉVÉRITÉ **PASS — verdict indépendant.** Même raisonnement que Baronnies-GR9 : l'audit
signale une source de presse du 29/07 (27 j) sous une alerte rouge, mais ce qui fonde
l'interdiction est **deux arrêtés municipaux datés et non expirés** : Sorède (n°26.216,
jusqu'au 13/09/2026, échéance explicite non atteinte) et Argelès-sur-Mer (ARR2026-024PM,
« jusqu'à nouvel ordre », donc par construction sans republication à attendre). Dégrader sur
la seule ancienneté de l'article de presse ferait dire au site qu'une réouverture est
possible alors qu'aucune source ne l'atteste et que les textes réglementaires restent
en vigueur. Sévérité HAUTE maintenue, aucune dégradation appliquée.
7 SOURCE VIVANTE **PASS avec réserve** : sur les 4 sources citées, 3 répondent (200) —
dont les deux textes réglementaires eux-mêmes (arrêté PDF, rnnmassane.fr) qui portent la
base légale de l'alerte. La 4e, ouillade.eu (29/07), renvoie 403 à la fois en curl (avec et
sans en-tête navigateur) et via l'outil de récupération web : plus probablement un blocage
anti-robot (Cloudflare) qu'une page réellement supprimée, et ce n'est de toute façon pas la
source qui fait foi ici. Non bloquant ; à retester au prochain passage.

### `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`
Hors liste de l'audit du jour (l'audit ne la signale plus) — contrôlée sur demande explicite
pour vérifier la correction déjà appliquée en amont (champ `validite:` réécrit pour restaurer
« jusqu'à nouvel ordre » après une lecture erronée d'une date isolée comme échéance passée).
Les 7 contrôles **PASS** : concordance interne cohérente avec la remontée HAUTE du jour
(nouvel arrêté préfectoral du 21/08 retrouvé via presse, motif chutes de pierres/arbres),
sévérité justifiée et documentée dans le raisonnement des `MAJ` successives, ton propre,
aucun jargon de veille en champ public, les 6 sources de la section Source répondent toutes
(200). **Confirmé : le correctif tient, aucune action supplémentaire nécessaire.**

## Corrections appliquées (dans mon périmètre, sans nouvelle source)

- **`incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`** : champ
  `validite:` reformulé (« restent fermés **jusqu'à nouvel ordre**, sans échéance de
  réouverture annoncée » au lieu de « sans échéance annoncée ») — aucun fait ajouté ni
  retiré, seule la formulation change pour lever l'ambiguïté entre date de réouverture (déjà
  passée, normal) et date d'expiration (qui n'existe pas). Vérifié : ne réapparaît plus dans
  `audit_qualite.py` après correction.

Aucune autre fiche n'a été modifiée.

## Vérification post-correction

`python3 site/build_site.py` → `OK (QA passée)` (74 actives, 24 clôturées, 98 fichiers).
`python3 site/audit_qualite.py --ecrire` → passe de 6 à 5 constats registre (le constat
Fontainebleau a disparu) ; toujours 1 bloquant, mais sur une fiche non touchée par ce
passage (voir ci-dessous). 0 alerte carte.

## Actions laissées à l'agent de veille (prochain run concerné)

- **`fermeture|GR-E4-Creta-Samaria|...`** (BLOQUANT) : revérifier le statut du jour sur
  samaria.gr au prochain passage T2 (vendredi) — la fiche est vérifiée depuis 11 jours sur
  une restriction qui se décide au jour le jour.
- **`fermetures-sentiers|Réunion-974|AP-2026-693|...`** : revérifier la carte ONF interactive
  au prochain passage sur La Réunion (19 j depuis la dernière vérification, seuil 12 j).
- **`refuge|GR221-222-Mallorca|...`** : revérifier caminsdepedra.conselldemallorca.es/en/refuges
  au prochain passage — l'échéance de fermeture annoncée (15/08) est dépassée sans
  confirmation de réouverture ; si la page confirme que les refuges ont rouvert, clôturer
  l'alerte plutôt que de simplement remettre `verif:` à jour.
- **`fermeture|FR-Baronnies-GR9|...`** : PASS confirmé aujourd'hui, aucune action urgente.
  L'audit déterministe continuera de signaler « source datée du 12/08 » tant que le PNR
  n'actualise pas sa page — c'est attendu, pas une anomalie. Au prochain passage T1 sur la
  zone, revérifier simplement que la liste des 26 communes n'a pas bougé.
- **`risque-feu|Alberes-66|...`** : PASS confirmé aujourd'hui, aucune action urgente. Point de
  vigilance : ouillade.eu (source de presse du 29/07) renvoie 403 — à retester au prochain
  passage ; si la source est bien morte, chercher une source de presse plus récente pour
  desserrer le flag résiduel de l'audit (non bloquant, la base légale des deux arrêtés reste
  intacte).
