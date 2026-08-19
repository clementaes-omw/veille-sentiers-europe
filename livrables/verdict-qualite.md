# Verdict qualité — 2026-08-19

Contrôle mené par l'agent Vérificateur Qualité (agent distinct de la veille : aucune des
fiches ci-dessous n'a été écrite par ce contrôle). Périmètre : les 10 fiches citées par
`livrables/audit-qualite.md` du 2026-08-19 (10 constats, 0 bloquant, sur 93 fiches / 73
actives), plus 1 fiche supplémentaire (`accès|Calanques-13|…`) révélée bloquante par
`python3 site/build_site.py` (jargon de veille en champ public), corrigée pour permettre
le build. Après corrections, `python3 site/build_site.py` rend « OK (QA passée) » et
`python3 site/audit_qualite.py` ne signale plus aucun BLOQUANT (0 avant comme après ; 10
constats ALERTE ramenés à 8, tous non bloquants — les 2 retirés étaient des faux positifs
de formulation, corrigés à information constante).

## 1. `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`

- **FRAÎPCHEUR** : FAIL. Vérifiée il y a 13 j, seuil 12 j (sévérité MOYENNE). Corriger
  exige de recouper l'AP 2026-693 avec la carte ONF interactive — une source nouvelle,
  hors périmètre du contrôle qualité.
- **CONCORDANCE INTERNE / HONNÊTETÉ** : PASS. Portion concernée, statut et zone
  racontent la même chose, et le texte dit déjà explicitement que le recoupement précis
  avec le GR R2 reste à faire.
- Aucune correction appliquée. **À traiter au prochain run.**

## 2. `fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26`

- **FRAÎPCHEUR** : FAIL déterministe (jamais revérifiée depuis sa détection, 8 j,
  `verif` = `detection`). C'est une fiche NOUVEAU de ce run : la revérification exige un
  nouveau passage sur le flux data.geo.admin.ch, hors périmètre.
- **CONCORDANCE / HONNÊTETÉ** : PASS. Le texte cite une source officielle unique et le
  dit sans détour (« aucune couverture presse trouvée à ce jour »).
- Aucune correction appliquée. **À traiter au prochain run.**

## 3. `fermeture|CH-Europaweg-Randa-Zermatt|fermeture-deviation-seg-27.3|2024-07-03`

- **FRAÎPCHEUR** : même FAIL déterministe et même cause que la fiche précédente
  (`verif` = `detection`, fiche NOUVEAU de ce run malgré une fermeture vieille de deux
  ans, déjà revalidée par Suisse Rando le 29/07/2026 selon la fiche elle-même).
- **CONCORDANCE / HONNÊTETÉ** : PASS.
- Aucune correction appliquée. **À traiter au prochain run** (revérification qui, cette
  fois, remettra `verif` à jour et purgera ce FAIL mécanique).

## 4. `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`

- **FRAÎPCHEUR** : FAIL. Vérifiée il y a 5 j, seuil 2 j (fermetures décidées au jour le
  jour). Corriger exige une lecture fraîche de samaria.gr — source nouvelle, hors
  périmètre.
- **CONCORDANCE / HONNÊTETÉ** : PASS. Le texte affiche déjà en clair qu'aucune source
  datée d'août n'a été trouvée et renvoie le lecteur à samaria.gr avant l'étape.
- Aucune correction appliquée. **À traiter au prochain run.**

## 5. `incendie|ES-AND-Niebla|feu-hors-capacite-extincion-20000ha|2026-08-06`

- **Validité mal formulée, FAUX POSITIF de l'audit confirmé** : le champ `validite:`
  commençait par « feu déclaré stabilisé […] depuis le 16/08/2026 », une date de DÉBUT
  d'état lue à tort par l'audit comme une échéance dépassée. Vérification du fond faite
  (lecture de la fiche + fetch de la source El Español du 17/08 : le feu est bien
  « estabilizado […] sin frentes activos », Copernicus confirme 33 000 ha) : aucune
  clôture n'est due, le feu n'est pas éteint formellement.
- **Corrigé** : `validite:` réécrit pour ouvrir sur « statut maintenu jusqu'à nouvel
  ordre, dans l'attente d'une déclaration d'extinction formelle non encore publiée »,
  puis reprend les mêmes faits (stabilisation 16/08, Copernicus 33 000 ha). Aucun fait
  ajouté ni retiré ; l'audit ne signale plus cette fiche après correction (vérifié par
  relance).
- **SOURCE VIVANTE** (alerte HAUTE) : PASS, source El Español du 17/08 vérifiée en
  ligne, contenu conforme au texte de la fiche.

## 6. `incendie|Savoie-Maurienne-Belleville|feux-vegetation-lachapelle-saintpierredebelleville|2026-08-14`

- **Validité mal formulée, FAUX POSITIF de l'audit confirmé** : même mécanisme que la
  fiche précédente, « stabilisé depuis le 16/08 » lu comme échéance passée. Le fond
  (sévérité INFO, aucune fermeture de sentier documentée) ne demande aucune clôture.
- **Corrigé** : `validite:` réécrit pour ouvrir sur « statut maintenu jusqu'à nouvel
  ordre en l'absence de source plus récente », reste du texte inchangé. L'audit ne
  signale plus cette fiche après correction.

## 7. `infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15`

- **Validité échue (14/08), FAIL déterministe réel, pas un artefact.** Vérification
  faite : la fiche pose déjà le constat en clair (« cette échéance est désormais
  dépassée et aucune source postérieure ne confirme… ») dans `validite:`, `statut:` et
  « Portion concernée » — c'est exactement l'une des deux corrections autorisées par mon
  périmètre, et elle est déjà appliquée par le run précédent. Rien à réécrire de plus
  sans invente un fait.
- **CONCORDANCE / HONNÊTETÉ** : PASS.
- Aucune correction supplémentaire appliquée. **Reste signalé, pas corrigé** (demande une
  source nouvelle) : confirmer si le pont a rouvert le 14/08 comme annoncé par l'APDL, ou
  reste fermé ; clôturer si confirmé.

## 8. `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`

- **Validité échue (15/08), FAIL déterministe réel, pas un artefact.** Même constat que
  la fiche précédente : le texte dit déjà en clair que l'échéance 01→15/08 est dépassée
  et qu'aucune source ne confirme la réouverture (« les sentiers eux-mêmes restent
  ouverts, prévoir au besoin des hébergements privés »).
- **CONCORDANCE / HONNÊTETÉ** : PASS.
- Aucune correction supplémentaire appliquée. **Reste signalé, pas corrigé** : confirmer
  réouverture ou prolongation sur caminsdepedra.conselldemallorca.es ; clôturer selon le
  résultat.

## 9. `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`

- **SÉVÉRITÉ (source de 21 j)** : vérifié le fond avant de conclure, comme demandé.
  PAS de dégradation. La sévérité HAUTE ne repose pas sur la fraîcheur de la presse mais
  sur deux arrêtés municipaux DATÉS et NON EXPIRÉS (Sorède n°26.216 jusqu'au 13/09/2026 ;
  Argelès-sur-Mer ARR2026-024PM « jusqu'à nouvel ordre », sans clause de republication
  périodique attendue). La fiche le dit déjà noir sur blanc (MAJ 12/08 et 18/08).
- **Règle des 14 jours (hypothèse non tranchée)** : NE S'APPLIQUE PAS. « Portion
  concernée » ne repose sur aucun marqueur d'hypothèse (« à confirmer », « probable »,
  « non localisé », « recoupement en cours ») : les actes sont déjà trouvés et cités.
- **SOURCE VIVANTE** : PASS. Fetch fait sur ouillade.eu (29/07) : article toujours en
  ligne, confirme l'arrêté d'Argelès-sur-Mer et la dérogation VTT du 24/07.
- Aucune correction appliquée.

## 10. `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`

- **Règle des 14 jours** : vérifiée avec jugement, comme demandé. Contrairement à la
  fiche précédente, aucun arrêté daté et non expiré ne fonde cette alerte : elle
  documente une fermeture quasi quotidienne sans confirmation du jour précis. Mais le
  seuil des 14 j se compte depuis la DÉTECTION (09/08) : il n'est atteint que le 23/08,
  soit 4 j après ce contrôle (aujourd'hui : 10 j écoulés). La fiche elle-même a déjà
  fait ce calcul dans `statut:` et documente une zone en ESCALADE avec recherche ciblée
  reconduite à chaque run (10/08 → 18/08, 8 vérifications). **Pas de dégradation
  appliquée** : le seuil n'est pas encore atteint.
- **SOURCE VIVANTE** : PASS. Fetch fait sur presseagence.fr (05/08) : article toujours en
  ligne, confirme la fermeture du massif le 6 août.
- **À surveiller au prochain run** : si aucune source postérieure au 06/08 n'est trouvée
  d'ici le 23/08, la règle des 14 j s'appliquera d'autorité (dégradation MOYENNE +
  mention explicite de ce qui n'est pas publié pour le lecteur).

## 11. `accès|Calanques-13|risque-feu-4couleurs|2026-06-01` — hors liste initiale de l'audit

- Non signalée par `audit_qualite.py`, mais bloquait `python3 site/build_site.py` (QA
  ton) : jargon de veille « à confirmer au prochain passage » dans « Portion concernée ».
- **Corrigé** : phrase reformulée pour le lecteur (« vérifier la carte avant de
  partir ») à information constante — aucun fait ajouté ni retiré.

## Corrections appliquées (fichiers touchés)

- `livrables/alertes/incendie--es-and-niebla--feu-hors-capacite-extincion-20000ha--2026-08-06.md`
- `livrables/alertes/incendie--savoie-maurienne-belleville--feux-vegetation-lachapelle-saintpierredebelleville--2026-08-14.md`
- `livrables/alertes/acces--calanques-13--risque-feu-4couleurs--2026-06-01.md`

Aucune fiche non citée (par l'audit ou par le build) n'a été modifiée. Aucune fiche n'a
été supprimée ni clôturée.

## Actions laissées à l'agent de veille (prochain run)

1. `fermetures-sentiers|Réunion-974|…` — revérifier l'AP 2026-693 / carte ONF ; fraîcheur
   en FAIL depuis 13 j sur un seuil de 12 j.
2. `fermeture|CH-EST-Trubbach|…` — première revérification du flux data.geo.admin.ch
   depuis la détection (8 j écoulés).
3. `fermeture|CH-Europaweg-Randa-Zermatt|…` — idem, première revérification depuis la
   détection (8 j écoulés).
4. `fermeture|GR-E4-Creta-Samaria|…` — revérifier le statut du jour (samaria.gr et presse
   grecque), fraîcheur en FAIL depuis 5 j sur un seuil de 2 j.
5. `infrastructure|Matosinhos-PT|…` — confirmer ou infirmer la réouverture effective du
   pont annoncée pour le 14/08 ; clôturer si confirmée.
6. `refuge|GR221-222-Mallorca|…` — confirmer réouverture ou prolongation de la fermeture
   des refuges (échéance 15/08 dépassée) ; clôturer selon le résultat.
7. `risque-feu|Alberes-66|…` — recherche ciblée d'une publication de presse postérieure
   au 29/07 pour rafraîchir la source (la scévérité reste justifiée par les arrêtés en
   attendant).
8. `risque-feu|FR-06-AlpesMaritimes|…` — recherche ciblée d'une publication postérieure
   au 06/08 ; à défaut, dégradation MOYENNE d'autorité si le seuil des 14 j (23/08) est
   atteint sans nouvelle source.
