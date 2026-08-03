# Verdict qualité — 2026-08-03

Agent Vérificateur Qualité, distinct de l'agent de veille qui a produit le run du jour. Base
de travail : `livrables/audit-qualite.md` (généré par `python3 site/audit_qualite.py
--ecrire` avant mon passage : 59 alertes actives, 45 fiches avec au moins un constat, **4
bloquants**, 41 alertes, 28 infos) et `agent-prompt.md` (§ TON, § DURÉE DE VIE D'UNE
HYPOTHÈSE). Aucune fiche non citée par l'audit n'a été touchée. Aucune recherche web n'a été
effectuée (hors périmètre de cet agent) : toutes les corrections ci-dessous sont des
réécritures à information constante, reconstituées à partir de ce que la fiche savait déjà
(`statut:`, `Zone (détails)`, `Source`), jamais un fait nouveau.

Fiches contrôlées (lues contre l'audit) : 45. Fiches effectivement corrigées : **10**.

## PASS / FAIL par contrôle

| # | Contrôle | Verdict | Détail |
|---|---|---|---|
| 1 | FRAÎcHEUR | **FAIL** (7 fiches, hors périmètre) | Revérifications en retard (12-30 j selon seuil) — nécessitent une nouvelle recherche, donc laissées à la veille. Voir liste ci-dessous. |
| 2 | CONCORDANCE INTERNE | **PASS** (10/10 corrigées) | Les 4 bloquants + 6 alertes de décrochage « Portion concernée » listés par l'audit ont tous été résolus. `python3 site/audit_qualite.py` ne signale plus aucun décrochage Portion/statut. |
| 3 | HONNÊTETÉ SUR CE QU'ON NE SAIT PAS | **PASS** (sur les fiches contrôlées) | Vérification explicite de la règle des 14 jours (agent-prompt.md) sur les 4 bloquants HAUTE/rouge : aucun n'a sa « Portion concernée » adossée à un marqueur d'hypothèse (« à confirmer », « probable », « non localisé »…) — les fermetures sont sourcées par arrêté ou fait constaté, seule la reconduction/l'échéance exacte reste incertaine et déjà formulée en clair au lecteur. La dégradation MOYENNE forcée par le prompt n'a donc lieu d'être sur aucun des 4 (`incendie\|Ariege-Bordes-Uchentein`, `incendie\|Drome-Justin-Die`, `risque-feu\|Alberes-66`, `risque-feu\|Hérault-34`). Non ré-audité fiche par fiche au-delà des signaux de l'audit déterministe. |
| 4 | PERTINENCE | **FAIL** (19 fiches, recommandé, non appliqué) | Validité expirée sans confirmation de prolongation. Recommandation de clôture ou de réécriture de validité — voir liste, aucune clôture appliquée d'autorité faute de source. |
| 5 | SÉVÉRITÉ JUSTE | **PASS** | Aucun cas trouvé de rouge sans interdiction sourcée parmi les fiches auditées ; les tensions de sévérité déjà documentées (ex. `risque-feu\|Vaucluse-84`, HAUTE maintenue « par prudence » malgré un signal non officiel de désescalade) sont déjà correctement explicitées dans les fiches, pas de recommandation supplémentaire. |
| 6 | TON | **PASS partiel** | Jargon de veille retiré des champs publics des 10 fiches corrigées (« run Europe », « ce run », « au registre », « en autonome », « recherche ciblée », « piège d'indexation » → reformulés). Le compteur d'INFO « Zone (détails) contient du jargon » est passé de 28 à 20 (fiches restantes non touchées, hors périmètre des bloquants du jour — voir liste). |
| 7 | SOURCE VIVANTE | **Non vérifiable par cet agent** | Contrôler qu'une URL répond encore suppose une requête réseau ; l'agent Vérificateur a pour consigne explicite de n'effectuer aucune recherche/requête web. Le seul proxy disponible est la fraîcheur de la date citée dans « Source » (déjà couvert par l'audit déterministe, cf. liste « source ancienne » ci-dessous) — pas un test HTTP réel. À faire par la veille ou un outillage dédié. |

## Corrections appliquées (10 fiches)

Pour chacune : Portion concernée resynchronisée sur l'état le plus récent connu du
`statut:` (réécriture à information constante), `statut:` ramené à 1-3 lignes, historique
non encore présent versé dans la chronologie de « Zone (détails) », jargon de veille retiré
des champs publics.

1. `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — **bloquant
   audit** (écart 16 j). Portion mentionnait le 18/07 ; réécrite avec l'état vérifié au
   03/08 (reconduction AP jusqu'au 10/08 via Pyrénées FM, aucune réouverture annoncée).
   Chronologie Zone complétée (29/07, 31/07, 01/08, 03/08, absents jusqu'ici).
2. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — **bloquant audit** (écart 18 j).
   Portion réécrite avec l'état au 03/08 (interdiction toujours en vigueur, diagnostic ONF
   en cours). Chronologie Zone complétée (31/07 reprise de feu Pinède, 01/08 affaiblissement
   du rattachement GR9/GR93).
3. `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — **bloquant audit** (écart
   18 j). Portion réécrite avec l'état vérifié au 31/07 (toujours interdit, recouvert par
   la vigilance rouge PO-66). Entrée Zone 31/07 ajoutée.
4. `risque-feu|Hérault-34|fermetures-massifs-quotidiennes|2026-07-02` — **bloquant audit**
   (écart 23 j). Portion réécrite (état au 31/07) ; contradiction interne corrigée (le champ
   `itin` disait le recoupement GR653/Carlencas déjà résolu 22/07, la Portion parlait encore
   d'un recoupement « en cours ») ; jargon « en autonome » reformulé.
5. `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — alerte audit (écart 8 j).
   Portion resynchronisée au 03/08 ; `validite:` réécrite (l'échéance globale du 26/07 était
   dépassée, remplacée par l'état réel : la plupart des communes sans échéance connue au-delà,
   Montclar-sur-Gervanne annoncée au 07/08). Chronologie Zone complétée (31/07, 01/08).
6. `incendie|HautesPyrenees-Bareges|Pic-Lurtet-Glere-piste-fermee|2026-07-08` — alerte audit
   (écart 12 j). Portion resynchronisée (03/08, silence de 6 jours sur un statut en tension
   depuis le 28/07) ; `validite:` reformulée pour ne plus afficher une échéance fixe dépassée.
   Chronologie Zone complétée (31/07, 03/08).
7. `risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18` — alerte audit
   (écart 12 j). Portion resynchronisée au 02/08 (Bavella rouvert, Illarata rouvert
   partiellement). Chronologie Zone complétée (24/07, 29/07, 31/07, 02/08, absente jusqu'ici).
8. `risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01` — alerte audit (écart
   11 j). Fiche déjà globalement à jour ; ajout d'une phrase « vérifié au 03/08 » en Portion.
9. `risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26` — alerte audit
   (écart 8 j) + validité expirée (28/07). Portion resynchronisée, `validite:` reformulée en
   ouverte (jusqu'à nouvel ordre). Chronologie Zone complétée (29/07, 31/07).
10. `risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01` — alerte audit (écart 11 j).
    Portion resynchronisée au 03/08 (désescalade non officielle Luberon vs Dentelles de
    Montmirail toujours à risque). `statut:` (11 passages empilés) ramené à 6 lignes ;
    deux entrées manquantes (31/07, 01/08) versées dans la chronologie de Zone.

Vérification après corrections : `python3 site/audit_qualite.py` → **0 bloquant** (contre 4
avant, et 0 décrochage Portion/statut restant, contre 10 avant, tous niveaux confondus) ;
`python3 site/build_site.py` → **OK (QA passée)** (59 actives, 9 clôturées, 68 fichiers,
aucune violation d'intégrité — aucune fiche n'a perdu de texte, seulement réorganisé).

## À traiter au prochain run de veille

**Fraîcheur en retard (nécessite une nouvelle vérification directe) :**
- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — vérifiée il y a 30 j (seuil
  12 j) et jamais revérifiée depuis détection : revérifier AP-2026-693 en direct.
- `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — vérifiée il y a 16 j
  (seuil 12 j) ; validité aussi expirée (17/07).
- `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` — vérifiée il y a 17 j (seuil
  12 j) et jamais revérifiée depuis détection.
- `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30` — vérifiée il y a 16 j
  (seuil 12 j).
- `infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15` — jamais revérifiée depuis
  17 j.

**Source vieillie sous une alerte rouge (retrouver une publication récente ou dégrader) :**
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — source du 23/07 (11 j).
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — source du 20/07
  (14 j) — à surveiller en priorité : au prochain jour sans nouvelle source, tombe sous la
  règle des 14 jours si la « Portion concernée » venait à retomber sur une hypothèse non
  tranchée (ce n'est pas le cas aujourd'hui, la fermeture reste sourcée par arrêté).
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — source du 22/07 (12 j).
- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — source du 13/07 (21 j, la plus
  ancienne des 4).
- `risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18` — source du 23/07
  (11 j).

**Validité expirée — clôturer si non prolongée, sinon réécrire avec une source datée
(recommandation, non appliquée faute de source) :**
`fermeture|FR-06-AlpesMaritimes|sentiers-gr-divers-ffrando06|2026-07-12` ·
`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` ·
`fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024` ·
`fermeture|PN-Pyrenees-Moundelhs|travaux-forestiers-cirque|2026-07-15` ·
`fermeture|PO-66-Argeles-Cerbere|sentier-littoral-E12-effondrement|2026-01-19` ·
`incendie|AT-Vorarlberg-Silvretta|coulee-boue-sentiers-fermes|2026-07-12` ·
`incendie|ES-AND-Los-Gallardos|feu-record-extinguido-5200ha-14morts|2026-07-09` ·
`incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16` ·
`incendie|ES-CYL-Fermoselle-Sayago|feu-record-11000ha-800evacues|2026-07-29` ·
`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` ·
`incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24` ·
`incendie|Savoie-Planay-Pralognan|RD915-refuges-Vanoise|2026-07-07` ·
`incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16` ·
`incendie|Var-Brignoles|feu-130ha-evacuations-quartiers|2026-07-29` ·
`reroutage|GR34-rade-de-Brest|nouveau-tracé-officiel|2026-05-28` ·
`reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25` ·
`risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05` ·
`réglementation|Écrins|bivouac|2026-06-19` ·
`sentiers|Mercantour|etat-sentiers-2026|2026-05-15`

**Dette de forme restante (jargon de veille dans « Zone (détails) », non bloquant, 18
fiches — à nettoyer au passage sur chacune, priorité aux HAUTE) :**
`accès|Calanques-13|risque-feu-4couleurs|2026-06-01` ·
`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` ·
`fermeture|PL-Tatras-Pusta-Dolinka|szlak-jaune-Kozia-Przelecz|2026-07-30` ·
`fermeture|PO-66-Argeles-Cerbere|sentier-littoral-E12-effondrement|2026-01-19` ·
`incendie|Corse-Mare-a-Mare-Nord|fermeture-Vergio-Albertacce|2026-07-19` ·
`incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16` ·
`incendie|ES-CYL-Bierzo|feux-veguellina-valdelaloba-san-tirso-vega-de-valcarce|2026-07-29` ·
`incendie|ES-CYL-Fermoselle-Sayago|feu-record-11000ha-800evacues|2026-07-29` ·
`incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` ·
`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` ·
`incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` ·
`incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24` ·
`incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16` ·
`incendie|Var-Brignoles|feu-130ha-evacuations-quartiers|2026-07-29` ·
`incendie|Var-Gros-Bessillon|feu-actif-Ponteves-Cotignac-Correns|2026-07-22` ·
`reroutage|Aspe-64-Chemin-Mature|eboulement-devie-col-Arras|2026-01-05` ·
`risque-feu|Corse|interdiction-feu|2026-06-15` ·
`risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28` ·
`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21` ·
`risque-feu|Var-83|fermetures-massifs-quotidiennes|2026-07-08`

**Contrôle non exécutable par cet agent :** SOURCE VIVANTE (test HTTP réel des URLs citées,
notamment sous les alertes rouges) — nécessite une requête réseau, hors périmètre de
l'agent Vérificateur qui n'effectue aucune recherche web. À faire par la veille au prochain
passage, en priorité sur les 5 fiches « source vieillie » listées ci-dessus.
