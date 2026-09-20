# Verdict qualité — 2026-09-20

Vérificateur qualité, agent distinct de la veille : aucune des 24 fiches contrôlées n'a été
rédigée par cette session. Périmètre : les 24 constats de `livrables/audit-qualite.md`
généré le jour même (0 bloquant, 21 alerte(s), 3 info(s), 0 carte). Aucune recherche web
n'a été effectuée par ce vérificateur ; les corrections ci-dessous sont des réécritures à
information constante, à partir de ce que chaque fiche contenait déjà. Aucune fiche hors de
cette liste n'a été ouverte ni modifiée.

## Corrections appliquées (8 fiches)

**Ton — jargon de veille retiré de « Zone (détails) » (3 fiches, sans perte de fait) :**

- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — « (piège d'indexation, écarté) »
  → reformulé en clair : un article homonyme daté du 15/04/2023, sans lien avec l'épisode
  suivi, écarté après vérification de sa date. Même fait, vocabulaire de veille retiré.
- `incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16` — « nouvelle
  recherche ciblée sur l'acte manquant » → « toujours aucun calendrier de réouverture publié »
  (le reste de la phrase, qui liste les sources consultées, est inchangé).
- `reroutage|Pierrefiques-76|déviation|2025-05-18` — « à revérifier au prochain passage
  FR-NOR » → « en l'absence de toute confirmation de fin de chantier ».

**Validité — champ `validite:` réécrit (5 fiches) :**

En creusant les 5 constats « validité annoncée dépassée » de l'audit, j'ai trouvé la cause
commune : `parse_alerte()` (site/build_site.py) ne lit QUE la première ligne d'un champ de
frontmatter quand sa valeur est répartie sur plusieurs lignes indentées (`cle, sep, val =
ligne.partition(":")`, appliqué ligne par ligne, sans fusion). Résultat : le mot-clé
« durable » ou la date de dernière vérification, écrits sur une ligne de continuation,
étaient invisibles à la fois pour `audit_qualite.py` ET pour le site lui-même — pas
seulement un faux positif de l'audit, un vrai trou d'information côté lecteur. J'ai donc
réécrit ces 5 champs sur une seule ligne, en y intégrant la date de vérification déjà
connue de la fiche (celle du champ `verif:`, jamais une date inventée) plutôt que de me
contenter d'un correctif cosmétique qui aurait laissé le défaut de lecture actif :

- `crue|Écrins-GR54|sentiers-refuges-endommages-crues-27-28-aout|2026-08-27` — validité
  refondue en une ligne, mot-clé « durable » réintégré, vérification du 20/09 explicitée
  (aucune source postérieure au 07/09 retrouvée).
- `incendie|Corse-Calvi|feu-aeroport-D81-28ha|2026-09-17` — idem, vérification du 20/09
  explicitée (feu fixé le 17/09, D81 et aéroport rouverts le jour même, aucune reprise).
- `incendie|ES-AND-Benahavis|feu-actif-confinement-9500-habitants|2026-09-13` — idem,
  vérification du 20/09 explicitée (contrôlé depuis le 17/09, rien de nouveau).
- `incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`
  — idem, en restituant la vérification déjà réalisée le 18/09 (`verif:` n'a pas bougé,
  aucune nouvelle recherche faite par moi).
- `risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21` — idem,
  vérification déjà réalisée le 18/09 restituée.

Ce défaut de `parse_alerte()` affecte probablement aussi d'autres champs multi-lignes
(`itin`, `statut`, `sev`) sur d'autres fiches non touchées ici : signalé pour information,
correctif de code hors périmètre de cet agent.

Aucune autre fiche du lot ne présentait de correction relevant du périmètre du vérificateur
(pas de « Portion concernée » figée sur un état antérieur alors que `statut:`/« Zone » étaient
à jour, pas de `statut:` empilé en journal à raccourcir).

## Contrôles — résultat par fiche

Note méthodologique sur le contrôle 5 (sévérité) : quatre alertes rouges reposent sur une
source vieille de 19 à 30 jours (constat « source vieillie », contrôle 4 du script). Les
quatre documentent déjà, noir sur blanc dans leur propre `statut:`, une recherche ciblée de
l'acte manquant datée du jour même (20/09) et le fait que leur sévérité HAUTE repose sur un
**acte officiel daté et confirmé** (arrêté municipal ou préfectoral republié), pas sur une
hypothèse en attente de recoupement — donc hors du champ de la règle des 14 jours, qui ne vise
que les portions encore accrochées à « à confirmer »/« probable »/« non localisé ». Vérifié
fiche par fiche avant de conclure : aucune dégradation à appliquer ni à recommander sur ce
point ; seule la fraîcheur de la source reste, structurellement, un point de vigilance pour
le prochain passage (hors périmètre : nécessite une source nouvelle).

| Clé | 1 Fraîcheur | 2 Concordance | 3 Honnêteté | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante | Verdict |
|---|---|---|---|---|---|---|---|---|
| `conditions\|IS-Hautes-Terres\|traversee-deconseillee-fimmvorduhals-glacier\|2026-08-25` | FAIL (jamais revérifiée, 8 j) | PASS | PASS | PASS | PASS (MOYENNE) | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `crue\|Écrins-GR54\|sentiers-refuges-endommages-crues-27-28-aout\|2026-08-27` | PASS (verif 20/09, aujourd'hui) | PASS | PASS | PASS (dégâts réels non résorbés, route non reconstruite : alerte toujours pertinente) | PASS (MOYENNE) | PASS | non rouge, non contrôlée | **Corrigé** (`validite:`) |
| `eboulement\|IT-Dolomites-BorcaDiCadore\|frana-passo-staulanza-route-rifugio-citta-di-fiume\|2026-09-10` | FAIL (jamais revérifiée, 8 j) | PASS | PASS | PASS | PASS (MOYENNE) | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `fermeture\|CH-EST-Kandersteg\|Spitze-Stei-deviation-seg-1.13\|2023-05-08` | FAIL (jamais revérifiée, 12 j) | PASS | PASS | PASS (déviation stable, 3 ans) | PASS (INFO) | PASS | non contrôlée (INFO) | **À traiter au prochain run** |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` | PASS (verif 20/09) | PASS | PASS | PASS (12 communes actives, arrêtés datés) | PASS — fondement = arrêtés municipaux datés, recherche du 20/09 documentée dans `statut:`, hors règle des 14 j | PASS | vérifiée par lecture : liste PNR au 01/09 citée nommément, cohérente | **PASS** — source vieillie signalée, non corrigible sans recherche nouvelle |
| `fermeture\|IT-Centre-Carrara\|via-francigena-nazzano-bonascola-frana\|2024` | FAIL (15 j, seuil 12 j, MOYENNE) | PASS | PASS (source unique assumée) | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `fermeture\|IT-DOLOMITES-Brenta\|Cima-Falkner-Bocchette-sentieri-chiusi\|2025-07` | FAIL (15 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `fermeture\|IT-Dolomites-Pelmo\|frana-versante-nordovest-borca-di-cadore\|2026-08-10` | FAIL (15 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `fermeture\|IT-Liguria-CinqueTerre\|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso\|2026-09-10` | FAIL (jamais revérifiée, 8 j) | PASS | PASS | PASS | PASS (MOYENNE) | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `fermetures-sentiers\|Réunion-974\|AP-2026-693\|2026-05-21` | PASS (verif 20/09) | PASS | PASS (lecture intégrale de l'arrêté 1617 documentée) | PASS | PASS (HAUTE, texte officiel lu en entier) | FAIL → **corrigé** | vérifiée : PDF de l'arrêté 1617 cité et lu en entier | **Corrigé** (jargon) |
| `incendie\|Ariege-Bordes-Uchentein\|GR10-ferme-Esbintz-Valier\|2026-07-10` | PASS (verif 20/09) | PASS | PASS | PASS | PASS — fondement = arrêté du 31/08, recherche du 20/09 documentée, hors règle des 14 j | PASS | vérifiée par lecture : arrêté du 31/08 cité, cohérent | **PASS** — source vieillie signalée, non corrigible sans recherche nouvelle |
| `incendie\|Corse-Calvi\|feu-aeroport-D81-28ha\|2026-09-17` | PASS (verif 20/09) | PASS | PASS | FAIL faible (feu fixé, D81/aéroport rouverts le jour même, aucun sentier jamais fermé : la fiche le dit elle-même « à reconfirmer avant clôture ») | PASS (INFO) | PASS | non rouge (INFO), non contrôlée | **Corrigé** (`validite:`) + recommandation ci-dessous |
| `incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02` | PASS (verif 20/09) | PASS | PASS | PASS | PASS — fondement = arrêté du 21/08 (abroge celui du 24/07), recherche du 20/09 documentée, hors règle des 14 j | PASS | vérifiée par lecture : arrêté du 21/08 cité, cohérent | **PASS** — source vieillie signalée, non corrigible sans recherche nouvelle |
| `incendie\|ES-AND-Benahavis\|feu-actif-confinement-9500-habitants\|2026-09-13` | PASS (verif 20/09) | PASS | PASS | FAIL faible (contrôlé depuis le 17/09, plus aucun évacué, aucune fermeture de sentier jamais documentée) | PASS (déjà dégradée HAUTE→MOYENNE le 18/09) | PASS | non rouge (MOYENNE), non contrôlée | **Corrigé** (`validite:`) + recommandation ci-dessous |
| `incendie\|ES-ARA-Huesca-Riglos\|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee\|2026-08-10` | PASS (verif 18/09, restitué) | PASS | PASS (dit explicitement que rien ne documente la réouverture de la route/du monastère) | PASS (3 points non confirmés : alerte reste pertinente) | PASS (MOYENNE) | PASS | non rouge, non contrôlée | **Corrigé** (`validite:`) |
| `incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19` | PASS (verif 20/09) | PASS | PASS | PASS | PASS — fondement = arrêté municipal du 15/08 republié et confirmé, recherche du 20/09 documentée, hors règle des 14 j | PASS | vérifiée par lecture : page mairie de L'Argentière-la-Bessée citée, cohérente | **PASS** — source vieillie signalée, non corrigible sans recherche nouvelle |
| `incendie\|IT-NO-Biellese\|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio\|2026-08-03` | FAIL (15 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `incendie\|IT-ValGrande\|interdiction-acces-sentiers-parc\|2026-07-10` | FAIL (15 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `reroutage\|Lot-Cieurac-Flaujac-Poujols\|GR65-devie-incendie\|2026-07-25` | FAIL (15 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `reroutage\|Pierrefiques-76\|déviation\|2025-05-18` | PASS (verif 20/09) | PASS | PASS (dit explicitement que rien ne confirme la fin de chantier) | PASS | PASS (MOYENNE) | FAIL → **corrigé** | non rouge, non contrôlée | **Corrigé** (jargon) |
| `reroutage\|VF-Lazio-Prato-La-Corte\|frana-deviation\|2026-01-30` | FAIL (15 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `risque-feu\|FR-Landes-Gironde\|vigilance-rouge-bivouac-interdit\|2026-07-21` | PASS (verif 18/09, restitué) | PASS | PASS (dit explicitement que le statut du GR®8 dans le secteur brûlé n'est pas confirmé) | PASS | PASS (MOYENNE Gironde / MOYENNE Landes en orange) | PASS | non rouge, non contrôlée | **Corrigé** (`validite:`) |
| `terrain\|IS-HautesTerres\|Fimmvorduhals-recul-glaciaire-crevasses\|2026-08` | FAIL (15 j, seuil 12 j, MOYENNE) | PASS | PASS | PASS | PASS | PASS | non rouge, non contrôlée | **À traiter au prochain run** |
| `incendie\|ES-CENTRO-Guadalajara-LaMierla\|feu-record-32000ha\|2026-07-16` | PASS (verif 20/09) | PASS | PASS | PASS (2 tronçons GR® réellement fermés, balisage détruit) | PASS (HAUTE, fait établi) | FAIL → **corrigé** | vérifiée par lecture : avis de fermeture GR®167/GR®10-ES cités et datés | **Corrigé** (jargon) |

## Recommandations (non appliquées, à la main de l'agent de veille)

- `incendie|Corse-Calvi|feu-aeroport-D81-28ha|2026-09-17` — sev INFO, feu fixé le 17/09, D81
  et aéroport rouverts le jour même, aucune fermeture de sentier jamais documentée par aucune
  des 6 sources consultées : candidate à la clôture dès la prochaine confirmation (la fiche
  le dit elle-même : « à reconfirmer avant clôture, sur le modèle des feux mineurs déjà
  clôturés cet été sur ce secteur »). Contrôle PERTINENCE en FAIL faible ; je ne clôture pas
  moi-même (hors périmètre, pas de nouvelle source consultée par ce vérificateur).
- `incendie|ES-AND-Benahavis|feu-actif-confinement-9500-habitants|2026-09-13` — sev MOYENNE,
  feu contrôlé depuis le 17/09, plus aucun évacué depuis le 15/09, aucune fermeture de
  sentier jamais documentée : à reconfirmer l'extinction totale (plan Infoca) au prochain
  passage sur la zone Andalousie, pour clôture ou dégradation en INFO.
- Les 4 alertes rouges en escalade (Baronnies-GR9, Ariège-Bordes-Uchentein, Drôme-Justin-Die,
  Hautes-Alpes-Bois-Noir) : rien à corriger sur la forme, mais la fraîcheur de la source
  reste un point de vigilance structurel — chacune mérite une tentative de recoupement sur
  un canal plus rapide que le silence des sites officiels (recueil des actes administratifs,
  presse locale) au prochain passage, comme le fait déjà chaque fiche depuis plusieurs jours.

## À traiter au prochain run (nécessite une source nouvelle, hors périmètre de cet agent)

1. `conditions|IS-Hautes-Terres|traversee-deconseillee-fimmvorduhals-glacier|2026-08-25` —
   jamais revérifiée depuis la détection (8 j) : revisiter safetravel.is.
2. `terrain|IS-HautesTerres|Fimmvorduhals-recul-glaciaire-crevasses|2026-08` — vérifiée il y a
   15 j (seuil 12 j) : revisiter safetravel.is / Iceland Review. Ces deux fiches (1 et 2)
   couvrent le même secteur et le même risque (recul glaciaire, Fimmvörðuháls) sous deux clés
   distinctes : à recouper par l'agent de veille, un doublon thématique est probable.
3. `eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`
   — jamais revérifiée (8 j) : revisiter la presse locale (ladige.it, Radio Cortina).
4. `fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08` — jamais revérifiée
   (12 j) : revisiter le flux data.geo.admin.ch (id 2596765).
5. `fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024` — vérifiée il y a
   15 j : revisiter La Voce Apuana ou une source municipale de Carrara (source unique à ce
   jour).
6. `fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07` — vérifiée il
   y a 15 j : revisiter sat.tn.it.
7. `fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10` —
   vérifiée il y a 15 j : revisiter il Dolomiti / Corriere delle Alpi.
8. `fermeture|IT-Liguria-CinqueTerre|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso|2026-09-10`
   — jamais revérifiée (8 j) : revisiter parks.it.
9. `incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03` —
   vérifiée il y a 15 j : revisiter la presse locale (Valsesianotizie, Newsbiella).
10. `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — vérifiée il y a 15 j :
    revisiter parcovalgrande.it/nov.php (4 fermetures distinctes à recouper).
11. `reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25` — vérifiée il y a
    15 j : revisiter ffrandonnee.fr / mairies de Limogne-en-Quercy et Flaujac-Poujols.
12. `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30` — vérifiée il y a 15 j :
    revisiter parcodiveio.it.

## Build et audit après corrections

- `python3 site/build_site.py` → `OK (QA passée)` (96 actives, 32 clôturées, 128 fichiers).
- `python3 site/audit_qualite.py --ecrire` → 16 constats, **0 bloquant** (contre 24 constats,
  0 bloquant au départ) : les 8 constats résolus sont exactement les 8 fiches corrigées
  ci-dessus. Les 16 constats restants demandent tous une source nouvelle (hors périmètre) ou
  sont déjà documentés en clair par la fiche elle-même (source vieillie sur alerte rouge
  fondée sur un acte daté).
- Garde-fou anti-corruption (perte de texte > 45 % sur une fiche) : non déclenché sur les 8
  fiches modifiées.

**24 fiches contrôlées, 8 corrections appliquées (3 jargon de ton, 5 champs `validite:`),
2 recommandations motivées non appliquées (Corse-Calvi, ES-AND-Benahavis), 4 faux signaux de
« source vieillie » sur alertes rouges confirmés comme non dégradables (fondement = actes
datés, hors règle des 14 jours), 12 actions renvoyées à la veille faute de source nouvelle
disponible sans recherche en ligne. Un défaut de lecture multi-lignes du frontmatter
(`parse_alerte()`) a été identifié comme cause commune des 5 corrections de `validite:` et
signalé pour un correctif de code ultérieur, hors périmètre de cet agent.**

VERIFICATEUR QUALITE COMPLETE