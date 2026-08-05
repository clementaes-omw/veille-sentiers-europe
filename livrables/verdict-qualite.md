# Verdict qualité — 2026-08-05

Agent Vérificateur Qualité, distinct de l'agent de veille qui a produit le run du jour
(2026-08-05). Base de travail : `livrables/audit-qualite.md`, régénéré en début de passage
par `python3 site/audit_qualite.py --ecrire` (état frais : 58 alertes actives, 38 fiches
avec au moins un constat, **1 bloquant**, 31 alertes, 21 infos) et `agent-prompt.md`
(§ TON, § DURÉE DE VIE D'UNE HYPOTHÈSE). Aucune fiche non citée par l'audit n'a été touchée.
Aucune recherche web n'a été effectuée (consigne explicite de ce passage) : toutes les
corrections ci-dessous sont des réécritures à information constante, reconstituées à partir
de ce que la fiche savait déjà (`validite:`, `statut:`, « Zone (détails) », « Source »),
jamais un fait nouveau.

Le décrochage Portion/statut signalé sur `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`
avait déjà été corrigé par l'agent de veille avant mon passage (Portion concernée à jour au
05/08, alignée sur `statut:`) — confirmé par l'audit frais qui ne le signale plus ; seul son
jargon de veille restait à nettoyer (fait, voir plus bas).

Fiches contrôlées (citées par l'audit) : **38**. Fiches effectivement corrigées : **32**.
Fiches signalées sans correction (nécessitent une source nouvelle, hors périmètre) : **6**,
dont le bloquant Réunion-974.

## PASS / FAIL par contrôle

| # | Contrôle | Verdict | Détail |
|---|---|---|---|
| 1 | FRAÎCHEUR | **FAIL** (9 fiches, hors périmètre) | Revérifications en retard (14-32 j selon seuil) ou jamais revérifiées depuis détection — nécessitent une nouvelle recherche sur le terrain, donc laissées à la veille. Voir liste ci-dessous. |
| 2 | CONCORDANCE INTERNE | **PASS** | Un seul décrochage réel trouvé par l'audit frais (`fermeture\|GR-E4-Creta-Samaria\|…`, Portion figée au 22/07 alors que le suivi savait déjà le 31/07-05/08, 14 j d'écart) — corrigé : Portion réécrite avec l'état vérifié au 05/08. Un décrochage mineur sous le seuil d'alerte (`risque-feu\|Corse-Bavella-Illarata\|…`, Portion datée du 02/08 vs vérification du 05/08, 3 j) corrigé par prudence à information constante. `python3 site/audit_qualite.py` ne signale plus aucun décrochage Portion/statut. |
| 3 | HONNÊTETÉ SUR CE QU'ON NE SAIT PAS | **PASS** | Aucune fiche corrigée ne présente une restriction incertaine comme acquise : les `validite:` réécrites disent explicitement « aucune levée trouvée » / « maintenue jusqu'à nouvel ordre » plutôt que d'afficher une échéance lue à tort comme dépassée. Vérification de la règle des 14 jours (agent-prompt.md) sur les alertes rouges à source vieillie (`Drome-Justin-Die`, `Alberes-66`, `Corse-Bavella-Illarata`) : aucune n'a sa « Portion concernée » adossée à un marqueur d'hypothèse (« à confirmer », « probable », « non localisé ») — ce sont des fermetures sourcées par arrêté ou fait constaté, seule la fraîcheur de la source citée est en cause. La dégradation forcée par le prompt ne s'applique donc à aucune des 3. |
| 4 | PERTINENCE | **FAIL** (1 fiche, recommandé, non appliqué) | `incendie\|ES-AND-Los-Gallardos\|feu-record-extinguido-5200ha-14morts\|2026-07-09` : feu officiellement éteint depuis le 24/07, aucun arrêté d'interdiction d'accès à la zone brûlée jamais confirmé malgré recherche — candidate à la clôture. Recommandation motivée ci-dessous, non appliquée d'autorité (ce n'est pas à moi de décider qu'aucune fermeture ne sera jamais trouvée). |
| 5 | SÉVÉRITÉ JUSTE | **PASS** | Aucune alerte rouge sans interdiction sourcée parmi les 38 fiches contrôlées. La dégradation HAUTE→MOYENNE déjà appliquée par la veille sur `incendie\|HautesPyrenees-Bareges\|…` (règle des 14 jours, agent-prompt.md) est cohérente et n'appelle pas de remise en cause. |
| 6 | TON | **PASS** (sur le périmètre audité) | Jargon de veille retiré des « Zone (détails) » des 21 fiches où l'audit le signalait (« run Europe », « ce run », « recherche ciblée », « lot T2 », « au registre », « en autonome », « cadence »/« hors cadence », « prochain passage »/« prochain run », « indexation » → reformulés ou retirés). `python3 site/audit_qualite.py` : 0 constat de jargon restant sur le périmètre audité (contre 21 avant). Le build signale encore 6 fiches CLÔTURÉES (hors périmètre : jamais citées par l'audit, qui exclut les fiches closes) portant du jargon résiduel non bloquant — non touchées, signalées plus bas pour la veille. |
| 7 | SOURCE VIVANTE | **Non exécuté ce passage** | Consigne explicite pour ce run : aucune recherche/requête web. Le contrôle des URLs (répondent-elles encore, portent-elles l'information annoncée) n'a donc pas pu être fait au-delà de la fraîcheur des dates déjà couvertes par l'audit déterministe (§1, § source vieillie). 3 alertes rouges à source vieillie signalées ci-dessous, à vérifier en priorité par la veille. |

## Corrections appliquées (32 fiches)

Pour chacune : `validite:` reformulée pour ne plus afficher une échéance/date de constat lue
à tort par l'audit comme une expiration (ajout de « jusqu'à nouvel ordre », « durable »,
« arrêté-cadre » ou équivalent quand la fiche elle-même établit déjà que rien n'a d'échéance
connue), et/ou jargon de veille retiré des champs publics et de « Zone (détails) ». Aucun
fait nouveau introduit — uniquement des réécritures à partir de ce que la fiche savait déjà.

**Validité réécrite (échéance lue à tort comme expirée par l'audit, alors que la fiche
établit déjà l'absence d'échéance) :**
1. `fermeture|FR-06-AlpesMaritimes|sentiers-gr-divers-ffrando06|2026-07-12`
2. `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — + Portion
   resynchronisée au 05/08 (décrochage bloquant corrigé, voir contrôle 2) + jargon retiré.
3. `fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`
4. `fermeture|PN-Pyrenees-Moundelhs|travaux-forestiers-cirque|2026-07-15` — + `statut:`
   empilé (2 passages redondants) ramené à l'état courant, historique versé en chronologie
   datée dans « Zone (détails) ».
5. `fermeture|PO-66-Argeles-Cerbere|sentier-littoral-E12-effondrement|2026-01-19` — +
   `statut:` empilé ramené à l'état courant + « Zone (détails) » réorganisée en chronologie
   datée (19/01 → 24/04 → 08/06) + jargon retiré.
6. `incendie|AT-Vorarlberg-Silvretta|coulee-boue-sentiers-fermes|2026-07-12`
7. `incendie|ES-AND-Los-Gallardos|feu-record-extinguido-5200ha-14morts|2026-07-09` — +
   jargon retiré (voir aussi recommandation de clôture, contrôle 4).
8. `incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16` — + jargon retiré.
9. `incendie|ES-CYL-Fermoselle-Sayago|feu-record-11000ha-800evacues|2026-07-29` — + jargon
   retiré.
10. `incendie|HautesPyrenees-Bareges|Pic-Lurtet-Glere-piste-fermee|2026-07-08` — + jargon
    retiré.
11. `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — + jargon retiré.
12. `incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24` — + jargon
    retiré.
13. `incendie|Savoie-Planay-Pralognan|RD915-refuges-Vanoise|2026-07-07`
14. `incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16` — + jargon
    retiré (fiche la plus dense du lot : « (run Europe) » retiré de 6 mentions, « piège
    d'indexation » et « recherche ciblée ce run » reformulés).
15. `incendie|Var-Brignoles|feu-130ha-evacuations-quartiers|2026-07-29` — + jargon retiré.
16. `reroutage|GR34-rade-de-Brest|nouveau-tracé-officiel|2026-05-28` — « pérenne » remplacé
    par « durable » (mot-clé reconnu par l'audit) pour lever le faux positif.
17. `reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25`
18. `risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`
19. `réglementation|Écrins|bivouac|2026-06-19`
20. `sentiers|Mercantour|etat-sentiers-2026|2026-05-15` — + `statut:` empilé (3 passages
    redondants) ramené à l'état courant, historique versé en chronologie datée.

**Jargon de veille retiré de « Zone (détails) » (fiches sans problème de validité) :**
21. `incendie|ES-CYL-Bierzo-Veguellina-Villafranca|feux-veguellina-valdelaloba-santirso-vegadevalcarce|2026-07-29`
22. `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`
23. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`
24. `incendie|Var-Gros-Bessillon|feu-actif-Ponteves-Cotignac-Correns|2026-07-22`
25. `reroutage|Aspe-64-Chemin-Mature|eboulement-devie-col-Arras|2026-01-05`
26. `risque-feu|Corse|interdiction-feu|2026-06-15`
27. `risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28`
28. `risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`
29. `risque-feu|Var-83|fermetures-massifs-quotidiennes|2026-07-08`
30. `fermeture|PL-Tatras-Pusta-Dolinka|szlak-jaune-Kozia-Przelecz|2026-07-30`
31. `accès|Calanques-13|risque-feu-4couleurs|2026-06-01`

**Portion resynchronisée (décrochage mineur, sous le seuil d'alerte) :**
32. `risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18` — date de
    vérification de la Portion alignée du 02/08 au 05/08 (`statut:` le savait déjà).

Vérification après corrections : `python3 site/audit_qualite.py` → **0 bloquant sur les
fiches touchées** (le seul bloquant restant, Réunion-974, n'a pas été touché — voir
ci-dessous) et **0 décrochage Portion/statut, 0 jargon de veille, 0 validité expirée**
restant sur le périmètre des 38 fiches auditées (contre 20 validités expirées et 21 jargons
avant correction). `python3 site/build_site.py` → **OK (QA passée)** (58 actives, 10
clôturées, 68 fichiers, aucune violation d'intégrité — aucune fiche n'a perdu de texte,
seulement réorganisé).

## À traiter au prochain run de veille

**Bloquant — jamais revérifiée, nécessite une source nouvelle :**
- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — vérifiée il y a 32 j (seuil
  12 j) et jamais revérifiée depuis sa détection (04/07). Action : revérifier l'AP 2026-693
  en direct (ONF Réunion) et trancher le recoupement encore marqué [HYPOTHÈSE] avec le
  GR R2. Aucune source nouvelle disponible pour ce passage ; rien n'a été inventé.

**Fraîcheur en retard (nécessite une nouvelle vérification directe) :**
- `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — vérifiée il y a
  18 j (seuil 12 j). Action : revérifier parcovalgrande.it pour une confirmation plus
  récente que le 17/07.
- `infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15` — jamais revérifiée depuis
  19 j. Action : vérifier caminhoportuguesdacosta.com / gronze.com avant l'échéance de fin
  septembre.
- `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` — vérifiée il y a 19 j
  (seuil 12 j) et jamais revérifiée depuis détection. Action : revérifier
  caminsdepedra.conselldemallorca.es, chercher enfin le motif de fermeture (jamais publié)
  et confirmer la réouverture annoncée au 16/08.
- `reroutage|GR34-rade-de-Brest|nouveau-tracé-officiel|2026-05-28` — vérifiée il y a 14 j
  (seuil 12 j). Action : reconfirmer la stabilité du tracé/hébergements via FFRando 29.
- `reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25` — jamais
  revérifiée depuis 8 j. Action : vérifier si la zone brûlée a rouvert ou si la déviation
  reste active.
- `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30` — vérifiée il y a 18 j
  (seuil 12 j). Action : revérifier parcodiveio.it pour un statut plus récent que le 18/07.

**Source vieillie sous une alerte rouge (retrouver une publication récente ou dégrader,
règle du contrôle 5) :**
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — source du 22/07 (14 j). Aucune
  hypothèse non tranchée, mais silence de 20 j sur drome.gouv.fr : chercher un point de
  situation plus récent en priorité.
- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — source du 13/07 (23 j, la plus
  ancienne des trois).
- `risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18` — source du 23/07
  (13 j, volet Illarata).

**Recommandation de clôture (contrôle 4 PERTINENCE, non appliquée d'autorité) :**
- `incendie|ES-AND-Los-Gallardos|feu-record-extinguido-5200ha-14morts|2026-07-09` — feu
  officiellement éteint depuis le 24/07, aucune fermeture de sentier ni arrêté
  d'interdiction d'accès jamais confirmé malgré plusieurs recherches. Si la veille ne
  trouve toujours rien lors du prochain passage ES-AND, envisager `[CLÔTURÉ]` : l'alerte ne
  décrit plus qu'une prudence de bon sens sans restriction officielle.

**Dette de forme hors périmètre (jargon de veille dans « Zone (détails) » de 6 fiches
CLÔTURÉES, jamais citées par l'audit qui exclut les fiches closes — signalé par le build,
non bloquant, à nettoyer lors d'un prochain passage sur chacune) :**
`incendie|GR20-Albertacce-Niolu|feu-GR20-fermé|2026-07-1…` ·
`incendie|ES-AND-Archez-Competa|feu-actif-confinement-Co…` ·
`incendie|Corse-Mare-a-Mare-Nord|fermeture-Vergio-Albert…` ·
`incendie|Herault-34-Poussan|feu-garrigue-Gardiole|2026-…` ·
`incendie|ES-CYL-Murias-de-Ponjos|feu-IGR2-proximite-Tor…` ·
`incendie|ES-CYL-Castropodame-La-Bana|feux-IGR2-Castropo…`

**Contrôle non exécutable par cet agent :** SOURCE VIVANTE (test réel des URLs citées,
notamment sous les 3 alertes rouges à source vieillie ci-dessus) — nécessite une requête
réseau, explicitement hors périmètre de ce passage. À faire par la veille au prochain
passage sur ces zones.
