# Verdict qualité — 2026-09-09

Vérificateur distinct de l'agent de veille (aucune des fiches contrôlées n'a été écrite par
cet agent). Base de travail : `livrables/audit-qualite.md` du 2026-09-09 (9 constats, 0
bloquant, sur 118 fiches / 88 actives).

**9 fiches contrôlées**, une par une, texte complet (toutes les lignes physiques du
front-matter, pas seulement ce que l'audit — qui relit le même parseur tronqué que
`build_site.py` — en a extrait) :

- `conditions|Ecrins-GR54|crue-degats-vallouise-oisans-valgaudemar|2026-08-27`
- `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`
- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`
- `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`
- `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`
- `risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`

Après corrections : `python3 site/build_site.py` → **OK (QA passée)**. `python3
site/verif_faits.py` sur les 2 fiches touchées → **0 perte/invention de fait**.
`python3 site/audit_qualite.py --ecrire` → passe de 9 à **7 constats, toujours 0
bloquant** (2 constats résolus par des corrections de forme, aucune fiche vidée de son
contenu).

## 1. Corrections appliquées (dans mon périmètre)

### `conditions|Ecrins-GR54|crue-degats-vallouise-oisans-valgaudemar|2026-08-27`
**Constat audit :** « la validité annoncée s'arrête au 28/08/2026, désormais passé ».
**Vérification :** le champ `validite:` de cette fiche est écrit sur 2 lignes physiques
(retour à la ligne indenté). Le parseur de `build_site.py`/`audit_qualite.py` tronque à la
première ligne et perd silencieusement la suite — ici, la mention « réparations
complémentaires annoncées mi-septembre » disparaissait de ce que l'audit lisait, qui ne
voyait plus que la date de l'événement (27-28/08) et la prenait pour une échéance passée.
Le texte réellement écrit dans le fichier était déjà correct : la crue est un fait daté, pas
une échéance de validité, et les réparations en cours sont annoncées pour la mi-septembre.
**Correction :** fusion des champs `itin:` et `validite:` en une seule ligne physique
chacun (même texte, aucune perte de fait, confirmé par `verif_faits.py`), et précision
« mi-septembre 2026 » pour lever toute ambiguïté d'année. Pas de changement de fond : la
fiche reste ACTIF/MOYENNE, à juste titre — le PASSAGE dégâts→réparations est bien couvert
et honnête sur ce qui reste en cours.
**Verdict par contrôle :** FRAÎCHEUR PASS (vérif 09/09) · CONCORDANCE PASS · HONNÊTETÉ
PASS · PERTINENCE PASS · SÉVÉRITÉ PASS (MOYENNE : impact réel, contournements en place,
pas de blocage total) · TON PASS · SOURCE VIVANTE PASS (ecrins-parcnational.fr et
ffrandonnee.fr répondent).

### `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`
**Constat audit :** « Portion concernée parle du 01/09 alors que le suivi connaît la
situation au 09/09 (8 j d'écart) ».
**Vérification :** le contenu factuel de `statut:` (« revérifiée sans changement, toujours
12 communes, toujours datée 01/09 ») et celui de « Portion concernée » (les mêmes 12
communes, la même liste PNR du 01/09) sont IDENTIQUES sur le fond — l'écart de date vient
seulement du fait que la Portion citait la date de mise à jour de la source (01/09) sans
dire qu'une revérification avait eu lieu depuis, sans changement. C'est exactement le
défaut structurel visé par ce contrôle : une mise à jour qui reste dans `statut:` (invisible)
au lieu d'atteindre le texte public.
**Correction :** ajout de « revérifiée sans changement le 09/09/2026 » dans la Portion
concernée, à information constante — aucun fait ajouté, la revérification est déjà
documentée dans `statut:` et dans la chronologie « Zone (détails) ».
**Verdict par contrôle :** FRAÎCHEUR PASS · CONCORDANCE désormais PASS (corrigée) ·
HONNÊTETÉ PASS (les 4 communes non tranchées — Saillans, Montclar, Beauvoisin,
Bénivay-Ollon — restent présentées comme telles, pas comme levées) · PERTINENCE PASS ·
SÉVÉRITÉ PASS (HAUTE justifiée par des arrêtés municipaux datés et nommés) · TON PASS ·
SOURCE VIVANTE PASS (baronnies-provencales.fr répond, 200).

## 2. Constats maintenus après vérification — pas une hypothèse, pas d'action de ma part

Quatre alertes HAUTE restent signalées par l'audit pour une source vieillie (règle
mécanique : source de plus de 10 jours sous une alerte rouge). J'ai relu intégralement,
dans chaque fichier, le texte complet de `statut:` et de « Zone (détails) » (pas seulement
la première ligne que l'audit prend en compte) et vérifié en direct que la source
principale répond toujours (curl, code 200 sur les quatre — `hautes-alpes.fr` renvoie 403
à un user-agent nu mais 200 à un navigateur, donc vivante, pas mort) :

- **`fermeture|DE-Sachsen-SaechsischeSchweiz|…|2026-08-01`** (source du 26/08, 14 j) —
  la sévérité HAUTE repose sur une Allgemeinverfügung en vigueur « bis auf Widerruf »
  (jusqu'à révocation), sans échéance calendaire : ce n'est pas une hypothèse « à
  confirmer »/« probable », c'est un acte administratif republié et confirmé le 09/09 par
  recoupement croisé sur 4 sources (aucune n'a de contenu plus récent parce qu'il n'y a
  rien de nouveau à publier, pas parce que la veille n'a pas cherché). La règle des 14
  jours de `agent-prompt.md` s'applique aux hypothèses non tranchées, pas aux fermetures
  confirmées sans terme. Pas de dégradation.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** (source du 21/08, 19 j) — l'arrêté
  préfectoral du 21/08/2026 (interdiction de fait ET de droit, motif désormais le risque de
  chute de pierres/arbres, pas l'incendie) n'a ni échéance ni levée publiée ; la fermeture
  de la chasse sur ce massif au 13/09 (source du 07/09, hors du champ `## Source` structuré
  mais présente dans la chronologie) corrobore le maintien. Revérifié le 09/09
  (mairie-die.fr, drome.gouv.fr) sans texte plus récent : c'est l'échec de recherche
  attendu en ESCALADE, pas une négligence. Pas de dégradation.
- **`incendie|HautesAlpes-BoisNoir|…|2026-07-19`** (source du 24/08, 16 j) — l'arrêté
  municipal du 15/08/2026 est explicitement présenté par la mairie comme en vigueur « en
  attendant l'ensemble des avis des autorités compétentes », sans date ; revérifié le
  08/09 et le 09/09 sur 2 pages distinctes de la mairie sans reconduction ni levée trouvée.
  Fait établi, pas une hypothèse. Pas de dégradation.
- **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`** (source du
  28/08, 12 j) — le classement rouge des Corbières/Roussillon du 03/09 est le dernier acte
  connu et la fiche dit explicitement, sans ambiguïté, que le statut des 7 autres massifs
  n'est « pas tranché » plutôt que de le présenter comme actif par défaut : c'est le
  comportement honnête attendu. Revérifié le 09/09 sans texte plus récent. Pas de
  dégradation.

Sur ces quatre fiches : FRAÎCHEUR PASS (vérif = 09/09 dans les quatre cas), CONCORDANCE
PASS, HONNÊTETÉ PASS, PERTINENCE PASS, SÉVÉRITÉ PASS (HAUTE justifiée par un acte sourcé,
pas par une supposition), TON PASS, SOURCE VIVANTE PASS. Le constat d'audit reste correct
littéralement (la source citée a bien cet âge) mais ne signale pas un défaut de fond : je
recommande de ne pas changer le seuil mécanique de l'audit pour autant, ces quatre cas
restent l'exception documentée, pas la règle.

## 3. À traiter au prochain run (agent de veille — nécessite une nouvelle recherche)

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — FRAÎCHEUR
  FAIL réel : `validite:` annonce des fermetures décidées au jour le jour (seuil 2 j),
  dernière vérif le 04/09 (5 j). Le site présente comme actuel un statut vieux de 5 jours
  pour une restriction qui change quotidiennement. Action attendue : revérifier le statut
  du jour de la gorge de Samaria et des tronçons E4 (samaria.gr, crete.gov.gr, Région de
  Crète) avant republication.
- **`incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`** —
  FRAÎCHEUR FAIL réel : sévérité MOYENNE, seuil 12 j, dernière vérif le 23/08 (17 j).
  Action attendue : revérifier oppenau.de (« Wegsperrungen ») pour confirmer si le
  Panoramaweg et le Rosi-Rotkehlchen-Weg sont toujours fermés ou si une réouverture a eu
  lieu depuis le 07/08.
- **`incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`** —
  FRAÎCHEUR FAIL réel : sévérité MOYENNE, seuil 12 j, dernière vérif le 22/08 (18 j).
  Action attendue : revérifier seine-et-marne.gouv.fr pour confirmer si les parcelles
  brûlées et leur périmètre de sécurité (les 20 % encore fermés) ont évolué depuis la
  réouverture des 80 % du massif le 22/08.

Ces trois FAIL portent sur le contrôle FRAÎCHEUR (1) et exigent une source nouvelle ; ce
n'est pas mon rôle de la chercher, c'est celui de l'agent de veille au prochain passage sur
ces zones.

## Résumé des contrôles (9 fiches)

| Contrôle | PASS | FAIL |
|---|---|---|
| 1. Fraîcheur | 6 | 3 (Samaria, Oppenau, Fontainebleau — signalés ci-dessus) |
| 2. Concordance interne | 9 (dont 1 corrigée : Baronnies-GR9) | 0 |
| 3. Honnêteté sur l'incertain | 9 | 0 |
| 4. Pertinence | 9 | 0 |
| 5. Sévérité juste | 9 | 0 |
| 6. Ton | 9 | 0 |
| 7. Source vivante (HAUTE) | 5/5 HAUTE contrôlées, toutes vivantes | 0 |

Aucune fiche supprimée, aucune fiche clôturée d'autorité, aucune fiche non citée par
l'audit n'a été touchée.
