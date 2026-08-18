# Verdict qualité — 2026-08-18

Contrôle mené par l'agent Vérificateur Qualité (agent distinct de la veille : aucune des
fiches ci-dessous n'a été écrite par ce contrôle). Périmètre : les 5 fiches citées par
`livrables/audit-qualite.md` du 2026-08-18 (6 constats, 0 bloquant, sur 92 fiches / 73
actives). Après corrections, `python3 site/build_site.py` rend « OK (QA passée) » et
`python3 site/audit_qualite.py` ne signale plus aucun BLOQUANT sur les fiches touchées
(0 bloquant avant comme après ; 6 constats ALERTE ramenés à 5, tous non bloquants).

## 1. `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`

- **FRAÎCHEUR** : FAIL. Vérifiée il y a 4 j, seuil 2 j (fermetures décidées au jour le
  jour, sans calendrier fixe). Corriger cela exige une lecture fraîche de samaria.gr — une
  source nouvelle, hors périmètre du contrôle qualité.
- **CONCORDANCE INTERNE** : PASS. Portion concernée, statut et zone racontent la même
  chose.
- **HONNÊTETÉ** : PASS. Le texte dit explicitement qu'aucune source postérieure au 31/07
  n'a été trouvée et renvoie le lecteur à samaria.gr avant l'étape.
- Aucune correction appliquée. **À traiter au prochain run** : revérifier le statut du jour
  (samaria.gr, cretalive.gr, inewsgr.com) avant publication.

## 2. `infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15`

- **FRAÎCHEUR** : PASS (vérifiée le 17/08, hier).
- **validité échue alors que fiche ACTIVE** : FAIL déterministe (échéance 14/08 dépassée).
  **Corrigé** : `validite:` et `statut:` réécrits pour dire en clair que l'échéance de
  réouverture annoncée par l'APDL est dépassée et que la réouverture effective n'est
  confirmée par aucune source postérieure — sans l'un ni l'autre affirmer une clôture non
  établie. Aucun fait ajouté, aucun supprimé.
- Reste **signalé, pas corrigé** (demande une source nouvelle) : confirmer si la
  circulation a effectivement repris le 14/08 ou reste bloquée (chantier connu pour ses
  retards) ; clôturer si confirmé.

## 3. `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`

- **validité échue alors que fiche ACTIVE** : FAIL déterministe (échéance 15/08 dépassée).
  **Corrigé** : `validite:`, `statut:`, « Portion concernée » et « Alternative » réécrits
  pour dire en clair que la fenêtre annoncée (01-15/08) est dépassée et que la réouverture
  n'est confirmée par aucune source. Pas de clôture appliquée : je n'ai pas de source
  postérieure au 15/08 attestant d'une réouverture (ou de sa prolongation), et la clôture
  n'est pas listée dans mon périmètre de correction directe pour une validité échue — seule
  la reformulation l'est.
- Reste **signalé, pas corrigé** : vérifier caminsdepedra.conselldemallorca.es pour
  confirmer réouverture ou prolongation ; clôturer selon le résultat.

## 4. `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`

- **CONCORDANCE INTERNE** : FAIL déterministe (Portion concernée datée du 10/08, statut/zone
  à jour au 18/08, 8 j d'écart). **Corrigé** : phrase ajoutée en fin de « Portion
  concernée » portant le constat au 18/08 (aucun signal de levée, deux arrêtés toujours en
  vigueur), sans rien retirer du texte existant.
- **Règle des 14 jours (hypothèse non tranchée)** : vérifiée, NE S'APPLIQUE PAS. La
  « Portion concernée » ne repose sur aucun des marqueurs d'hypothèse (« à confirmer »,
  « probable », « non localisé », « recoupement en cours ») : l'alerte s'appuie sur deux
  arrêtés municipaux datés et non expirés (Sorède jusqu'au 13/09/2026, Argelès « jusqu'à
  nouvel ordre »), pas sur une allégation en attente de preuve. Détection le 20/07 (29 j),
  mais rien à trancher : les actes sont déjà trouvés.
- **SÉVÉRITÉ (source de 20 j)** : PASS motivé, pas de dégradation recommandée. La sévérité
  HAUTE repose sur les arrêtés eux-mêmes, non sur l'ancienneté de la couverture presse.
  Recommandation non appliquée : poursuivre la recherche ciblée d'une publication plus
  récente pour rafraîchir la source, sans quoi rien ne change au fond.
- **SOURCE VIVANTE** : PASS. Les 4 URLs de source répondent (HTTP 200 vérifié ce contrôle).

## 5. `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`

- **FRAÎCHEUR / CONCORDANCE** : PASS (vérifiée aujourd'hui, aucun décrochage détecté).
- **Règle des 14 jours** : ne s'applique pas encore — détection 09/08, seuil atteint le
  23/08 seulement, et le texte ne repose sur aucun marqueur d'hypothèse non tranchée (fait
  matériel établi : fermetures quasi quotidiennes documentées jusqu'au 06/08).
- **SÉVÉRITÉ (source de 13 j)** : PASS motivé, pas de dégradation recommandée à ce stade.
  Aucune correction appliquée.
- **SOURCE VIVANTE** : PASS. Les 5 URLs de source répondent (HTTP 200).
- **À surveiller au prochain run** : si aucune source postérieure au 06/08 n'est trouvée
  d'ici le 23/08, la règle des 14 jours s'appliquera d'autorité (dégradation MOYENNE +
  mention explicite de l'absence d'acte).

## Corrections appliquées (fichiers touchés)

- `livrables/alertes/infrastructure--matosinhos-pt--pont-levadizo-ferme--2026-06-15.md`
- `livrables/alertes/refuge--gr221-222-mallorca--refuges-consell-fermes--2026-08-01.md`
- `livrables/alertes/risque-feu--alberes-66--fermeture-massif-gr10--2026-07-10.md`

Aucune fiche non citée par l'audit n'a été modifiée. Aucune fiche n'a été supprimée ni
clôturée.

## Actions laissées à l'agent de veille (prochain run)

1. `fermeture|GR-E4-Creta-Samaria|…` — revérifier le statut du jour (samaria.gr et
   presse grecque), fraîcheur en FAIL depuis 4 j sur un seuil de 2 j.
2. `infrastructure|Matosinhos-PT|…` — confirmer ou infirmer la réouverture effective du
   pont annoncée pour le 14/08 ; clôturer si confirmée.
3. `refuge|GR221-222-Mallorca|…` — confirmer réouverture ou prolongation de la fermeture
   des refuges (échéance 15/08 dépassée) ; clôturer selon le résultat.
4. `risque-feu|Alberes-66|…` — recherche ciblée d'une publication de presse postérieure
   au 29/07 pour rafraîchir la source (la sévérité reste justifiée par les arrêtés en
   attendant).
5. `risque-feu|FR-06-AlpesMaritimes|…` — recherche ciblée d'une publication postérieure au
   06/08 ; à défaut, dégradation MOYENNE d'autorité si le seuil des 14 j (23/08) est atteint
   sans nouvelle source.
