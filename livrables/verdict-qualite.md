# Verdict qualité — 2026-08-23

Vérificateur distinct de l'agent de veille du jour. 14 fiches contrôlées (celles citées par
`livrables/audit-qualite.md`, relancé en début de passage). 73 alertes actives au total, 95
fiches au dossier ; les fiches non citées par l'audit n'ont pas été touchées.

`python3 site/build_site.py` → **OK (QA passée)** (73 actives, 22 clôturées, 95 fichiers).
`python3 site/audit_qualite.py` → **0 BLOQUANT sur les fiches touchées** (1 BLOQUANT restant,
Creta-Samaria, hors périmètre de correction — voir plus bas).
`python3 site/verif_faits.py` → 1 point relevé, expliqué et jugé non problématique (voir
« Corrections appliquées », fiche Creta-Samaria).

## Constat le plus important : troncature silencieuse du frontmatter multi-ligne

`site/build_site.py::parse_alerte` ne lit qu'une ligne par champ de frontmatter
(`cle, sep, val = ligne.partition(":")` puis boucle sans accumulation). Toute ligne de
continuation sans `:` est silencieusement ignorée — le champ est tronqué à sa première ligne,
**sans erreur, sans avertissement**, y compris pour des champs PUBLICS (`itin:`, `validite:`,
`sev:`, `type:`) affichés tels quels sur le site. Le format documenté dans `agent-prompt.md`
(« un champ par ligne ») l'interdit déjà, mais rien ne le fait respecter.

Conséquence vérifiée sur 3 fiches de ce lot : `validite:`/`itin:` coupés en plein mot,
et — pour Malerweg — deux dates de tempête (18/08, 19-20/08) mal réparties dans le texte
tronqué, ce qui a produit un faux « validité expirée » dans l'audit. Corrigé (voir plus bas).

**17 fiches au total** ont un champ public tronqué de cette façon (3 corrigées ici, **14
autres non citées par l'audit du jour, donc non touchées** — hors périmètre) :
`acces--calanques-13--risque-feu-4couleurs`, `fermeture--drome-omblese--sentiers-pas-du-
gouillat-pas-de-comberoufle`, `incendie--aude-conques-sur-orbiel--feu-fixe-50ha`,
`incendie--drome-justin-die--foret-fermee`, `incendie--es-and-niebla--feu-hors-capacite-
extincion-20000ha`, `incendie--es-ara-huesca-riglos--feu-camino-aragones...`, `incendie--es-
cyl-hermisende-sanabria--feu-igr2...`, `incendie--gr34-capfrehel--fermeture-lande-fort-la-
latte`, `incendie--hautesalpes-boisnoir--gr54a-ferme...`, `incendie--herault-34-pegairolles-
escalette--feu-a75-200ha`, `incendie--savoie-maurienne-belleville--feux-vegetation...`,
`incendie--savoie-planay-pralognan--rd915-refuges-vanoise`, `incendie--uk-cairngorms-
glenmore--wildfire-strathnethy-c7-fermee`, `risque-feu--gard-30--fermetures-5-secteurs-
rouges`. **Action recommandée, hors mon périmètre (code, pas fiche)** : soit le parseur
apprend à accumuler les lignes de continuation d'un champ frontmatter, soit l'agent de veille
cesse d'y écrire des valeurs multi-lignes (le format l'exige déjà). Tant que ce n'est pas fait,
tout champ public wrappé sur plusieurs lignes est silencieusement corrompu sur le site.

## Corrections appliquées (dans mon périmètre)

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — CONCORDANCE
  (contrôle 2, FAIL) : « Portion concernée » citait « la vérification du 07/08 » alors que
  `verif:` est au 14/08 et que `statut:` décrit une recherche du 14/08 restée sans résultat.
  Réécrit d'après le `statut:` déjà présent (aucun fait nouveau) ; chronologie de « Zone
  (détails) » complétée par l'entrée MAJ 14/08, en langage lecteur (le jargon de `statut:` —
  « recherche bilingue dédiée », « non confirmable en autonome » — n'a pas été recopié).
  `verif_faits.py` signale un nombre « inventé » (14) sur cette fiche : c'est la date 14/08,
  déjà présente dans `verif:`/`statut:` avant ma correction, déplacée dans la prose publique —
  exactement le mouvement statut→chronologie que mon périmètre autorise, pas une invention.
- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — CONCORDANCE (contrôle 2,
  FAIL, 11 j d'écart signalé par l'audit) : « Portion concernée » ne mentionnait que la liste
  PNR du 12/08, alors que `statut:` venait de la revérifier en direct le 23/08 (inchangée) et
  connaît désormais le numéro d'arrêté de La Charce (n°16-2026). Les deux informations,
  déjà connues du fichier, ont été ajoutées à la phrase d'ouverture de « Portion concernée ».
  Le constat d'écart a disparu du nouvel audit.
- **`fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Kohlichtgraben-Bergsteig-scolytes|
  2026-08-18`** — défaut de frontmatter (`itin:`, `validite:`, `statut:` étalés sur plusieurs
  lignes, tronqués par le parseur). Rejoints sur une ligne chacun, aucun mot perdu. `validite:`
  reformulée de « sans échéance annoncée » à « fermés jusqu'à nouvel ordre… aucune échéance
  annoncée » : même fait (aucune date de fin publiée), formulation plus claire pour le lecteur.
  Le faux constat « validité expirée » de l'audit a disparu.
- **`incendie|Drome-Bellegarde-en-Diois|feu-massif-Claps-400ha|2026-08-03`** — même défaut,
  `validite:` et `statut:` rejoints sur une ligne (le texte s'arrêtait avant sur « pas
  encore »). Aucune reformulation de fond : contrairement à Malerweg, cette fiche décrit un
  statut d'incendie (fixé/non éteint), pas une fermeture à échéance — je n'ai pas ajouté de
  formule « jusqu'à nouvel ordre » qui aurait suggéré une interdiction d'accès inexistante.
- **`incendie|Lozere-La-Bastide-Puylaurent|feu-252ha|2026-08-19`** — même défaut, `itin:`,
  `validite:` et `statut:` rejoints sur une ligne (le texte coupait « aucun arrêté
  d'interdiction d'accès » en plein milieu).

## Constats de l'audit non corrigés, laissés à l'agent de veille

FRAÎCHEUR (contrôle 1, hors périmètre : exige une nouvelle recherche, pas une réécriture) :
- **`fermeture|GR-E4-Creta-Samaria|…`** — ⛔ BLOQUANT persistant : vérifiée il y a 9 j alors
  que sa propre validité annonce une décision au jour le jour (seuil 2 j). Action : contrôler
  samaria.gr le jour même du prochain passage sur la zone Crète.
- **`fermetures-sentiers|Réunion-974|AP-2026-693|…`** — vérifiée il y a 17 j (seuil 12 j).
  Action : recouper directement la carte ONF interactive (piste déjà notée en `statut:`).
- **`fermeture|CH-EST-Trubbach|…`** et **`fermeture|CH-Europaweg-Randa-Zermatt|…`** — jamais
  revérifiées depuis leur détection il y a 12 j. Action : relire le flux
  data.geo.admin.ch et tenter la couverture presse déjà notée comme non tentée.
- **`refuge|GR221-222-Mallorca|refuges-Consell-fermes|…`** — vérifiée il y a 16 j (seuil 12 j)
  ET validité (15/08) passée — mais déjà posée en clair dans les 4 champs publics et `statut:`
  (contrôle 3 HONNÊTETÉ : PASS, rien à réécrire). Action : confirmer ou infirmer la réouverture
  sur caminsdepedra.conselldemallorca.es.

VALIDITÉ EXPIRÉE (contrôle 3) — 6 fiches signalées par l'audit, deux situations distinctes :
- **`infrastructure|Matosinhos-PT|pont-levadizo-fermé|…`** — échéance du 14/08 réellement
  dépassée, mais **déjà posée en clair** dans les 4 champs publics (« cette échéance est
  désormais dépassée et aucune source postérieure ne confirme… ») : contrôle 3 PASS, rien à
  réécrire. Action : chercher une source postérieure au 14/08 confirmant la réouverture.
- **`incendie|Aude-Montseret-Corbieres|…`**, **`incendie|Lozere-Massegros-Causses-Gorges|…`**,
  **`incendie|Var-Ginasservis|…`**, **`incendie|Drome-Bellegarde-en-Diois|…`** — **faux
  positifs de l'heuristique de l'audit** : ces fiches suivent un statut d'incendie (date de
  « fixé », date de dernière vérification), pas une fermeture à échéance annoncée ; l'audit
  prend la date la plus récente citée dans `validite:` pour une échéance expirée alors qu'aucune
  échéance n'est réellement annoncée. Rien à corriger sur le fond (contrôle 3 déjà PASS, le
  texte ne prétend aucune interdiction en cours au-delà des routes déjà citées). Recommandation
  PERTINENCE (contrôle 4, non appliquée) : Montséret (feu fixé depuis 17 j) et Massegros
  (13 j) sont mûrs pour une vérification de clôture au prochain passage sur l'Aude/la Lozère
  si aucune fermeture de sentier n'a jamais été documentée ; Ginasservis (feu confirmé éteint,
  seule la RD30 reste incertaine) de même.

SÉVÉRITÉ (contrôle 5, recommandation seulement — la règle des 14 jours ne s'applique pas, ces
deux alertes reposent sur des arrêtés datés et non expirés, pas sur un « à confirmer ») :
- **`fermeture|FR-Baronnies-GR9|…`** — alerte rouge appuyée sur une liste PNR datée du 12/08
  (11 j), mais revérifiée en direct et inchangée le 23/08, et chaque commune y porte un
  arrêté propre daté. Contrôle 7 (sources) : PASS, `baronnies-provencales.fr` et
  `gervanne-sye.com` répondent (200). Pas de dégradation recommandée en l'état ; action :
  retenter une liste PNR postérieure au 12/08 au prochain passage.
- **`risque-feu|Alberes-66|fermeture-massif-GR10|…`** — alerte rouge appuyée sur un article de
  presse du 29/07 (25 j), mais la fiche documente déjà (MAJ 12/08) que la base légale est deux
  arrêtés municipaux datés et non expirés (Sorède jusqu'au 13/09, Argelès « jusqu'à nouvel
  ordre »), pas la fraîcheur de l'article. Contrôle 7 : PASS, `ouillade.eu` et
  `mapetiterando.fr` répondent (200). Décision de sévérité déjà motivée et défendable, pas de
  dégradation recommandée. Action : la fiche note elle-même (MAJ 12/08) que l'accès direct aux
  pages officielles de Sorède/Argelès a été bloqué par le proxy réseau de l'environnement de
  veille — à retenter au prochain passage.

## Récapitulatif des contrôles

| # | Contrôle | Résultat |
|---|---|---|
| 1 | Fraîcheur | 1 FAIL bloquant non corrigeable (Creta-Samaria, besoin d'une source neuve) ; 4 FAIL non bloquants signalés (Réunion-974, CH-Trubbach, CH-Europaweg, Mallorca) |
| 2 | Concordance interne | 2 FAIL corrigés (Creta-Samaria, Baronnies-GR9) ; PASS ailleurs |
| 3 | Honnêteté sur l'incertain | PASS partout, y compris les échéances passées déjà posées en clair (Matosinhos, Mallorca) |
| 4 | Pertinence | PASS ; 3 recommandations de clôture à vérifier (Montséret, Massegros, Ginasservis) |
| 5 | Sévérité juste | PASS motivé sur les 2 alertes rouges du lot (Baronnies-GR9, Albères-66) |
| 6 | Ton | PASS, aucun jargon détecté dans les champs publics des 14 fiches |
| 7 | Source vivante | PASS sur les sources rouges contrôlées (baronnies-provencales.fr, gervanne-sye.com, ouillade.eu, mapetiterando.fr — 200) |

Carte : 0 alerte perdue — l'alias `Lozere-La-Bastide-Puylaurent → FR-30-48` ajouté par l'agent
de veille est bien pris en compte, la ligne « carte » a disparu de l'audit.