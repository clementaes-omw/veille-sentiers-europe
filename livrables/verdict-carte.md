# Verdict carte — 2026-09-08

Contrôle DÉCLENCHÉ (pas le contrôle périodique du lundi) : deux lignes ont été ajoutées à
`referentiel/zones-coords.csv` par l'opérateur humain (pas par l'agent de veille) pour
raccrocher deux zones nouvellement créées le 08/09 et jusque-là perdues de la carte —
`CH-Valais-Arolla` (46.03;7.48) et `VS-Orsieres-ValFerret` (45.90;7.15). Conformément à
`agents/verificateur-carte.md` (mission 1, dernier paragraphe : un centroïde ajouté à la main
ne peut être jugé juste par aucun test automatique), je vérifie ces deux centroïdes de façon
autonome, sans les prendre pour acquis. Base : `livrables/audit-qualite.md` régénéré le
08/09 (`python3 site/audit_qualite.py --ecrire`, section carte : 0 alerte perdue), les trois
fiches d'alerte concernées, `referentiel/zones-sources.md` (§ tableau Alpes, ligne
CH-VALAIS-VAUD), et un recoupement géographique externe (Wikipédia / offices de tourisme
locaux) pour les coordonnées réelles des lieux cités.

**2 zones contrôlées** (les deux ajouts du jour), sur 51 zones désormais présentes dans
`referentiel/zones-coords.csv` (49 préexistantes + les 2 vérifiées ici).

Je n'ai pas rédigé les fiches d'alerte que je contrôle (agent de veille du run du 08/09, pas
moi) : rien à signaler sur la règle « pas de fond ». Je n'ai pas non plus ajouté ces deux
lignes CSV — elles étaient déjà posées avant mon passage par l'opérateur humain — mais je les
ai vérifiées avec la même rigueur que si je les avais créées moi-même (mission 1).

## `CH-Valais-Arolla` — 46.03;7.48 — CONFIRMÉ, repère fiable

- **Repère utilisé** : le village d'Arolla lui-même (commune d'Évolène, Valais), coordonnées
  publiques ≈ **46.0254;7.4836** (recoupement Wikipédia/geoview.info). Écart avec le
  centroïde du CSV : ≈ **0,7 km**. Quasi exact.
- **Cohérence avec les deux fiches concernées** :
  - `fermeture|CH-Valais-Arolla|Pas-de-Chevre-chemin-impraticable|2026-08-24` — secteur du
    Pas de Chèvre, entre le glacier de Cheilon et Arolla : le col est sur l'itinéraire
    Arolla → cabane des Dix, à quelques km au nord-ouest du village. Bien dans le même
    versant que le marqueur.
  - `fermeture|CH-Valais-Arolla|Bertol-Haut-Glacier-deviation|2026-05-11` — accès à la
    cabane de Bertol depuis Arolla par le haut glacier : la cabane de Bertol est à
    ≈ 46.006;7.528 (repère public), soit **≈ 4,3 km** du marqueur. Bien dans le même massif.
  - Les deux fiches situent explicitement l'incident « commune d'Évolène » et « val
    d'Hérens » : cohérent avec le nom donné à la zone dans le CSV.
- **Cohérence avec `zones-sources.md`** : la ligne CH-VALAIS-VAUD (§ tableau Alpes) couvre
  nominalement tout le Valais, y compris la Haute Route Chamonix-Zermatt — Arolla en fait
  bien partie administrativement — mais son centroïde générique (46.15;7.30) est posé dans
  la vallée du Rhône (axe Martigny–Sion), à **≈ 19 km** du village d'Arolla, qui se trouve
  dans le val d'Hérens, une vallée latérale distincte débouchant sur le Rhône à Sion/Euseigne
  (pas la même vallée que Martigny/Sembrancher). Un marqueur distinct est donc justifié :
  pas de doublon, la localisation réelle est significativement différente du repère
  générique. Verdict : **coordonnées confirmées, aucune correction nécessaire**.

## `VS-Orsieres-ValFerret` — 45.90;7.15 — CONFIRMÉ, repère fiable

- **Repères utilisés** : commune d'Orsières ≈ **46.033;7.150** (Wikipédia) et La Fouly, à
  l'autre bout du val Ferret (frontière italienne) ≈ **45.933;7.099** (Wikipédia/registre
  cadastral). Le centroïde du CSV (45.90;7.15) est légèrement au sud du milieu de ce corridor
  (qui serait plutôt ≈ 45.98;7.12) mais reste dans la même vallée, à l'écart le plus
  défavorable d'environ **9-10 km** du point médian théorique du corridor — bien en-deçà du
  seuil de correction (« plusieurs dizaines de km »).
- **Cohérence avec la fiche concernée** :
  `fermeture|VS-Orsieres-ValFerret|Saleinaz-cabane-eboulement|2026-07-29` situe l'incident
  au « chemin de Praz-de-Fort à la cabane de Saleinaz », au lieu-dit Petit Clocher des
  Planereuses, val Ferret, commune d'Orsières. Praz-de-Fort est à ≈ 45.989;7.125 (repère
  public), donc **≈ 8 km** du marqueur — le point tombe bien dans le corridor du val Ferret,
  pas dans une autre vallée.
- **Cohérence avec `zones-sources.md`** : même lecture que pour Arolla — CH-VALAIS-VAUD
  couvre nominalement le Valais et cite le TMB parmi ses sentiers, mais son centroïde
  générique (46.15;7.30) est à **≈ 30 km** du marqueur du val Ferret, dans la vallée
  principale du Rhône plutôt que dans le val d'Entremont/val Ferret qui s'en détache à
  Sembrancher. Écart plus marqué que pour Arolla : un marqueur distinct est d'autant plus
  justifié. Verdict : **coordonnées confirmées, aucune correction nécessaire**.

## Vérification anti-doublon avec `CH-VALAIS-VAUD` (46.15;7.30)

Recalcul direct de `zones_carte()` sur le registre du 08/09 (84 alertes actives) : les trois
zones concernées se résolvent bien séparément, sans collision ni chevauchement —
- `CH-Valais-Arolla` → 2 alertes (Pas-de-Chèvre, Bertol) ;
- `VS-Orsieres-ValFerret` → 1 alerte (Saleinaz) ;
- `CH-VALAIS-VAUD` → 3 alertes distinctes, toutes différentes (`TMB-CH-Orsieres`
  Prayon-Branche via alias `ALIAS_ZONE`, `CH-Europaweg-Randa-Zermatt` via alias,
  `CH-Vaud-Sainte-Croix-Baulmes` via alias).
Aucune des trois alertes historiquement rattachées à `CH-VALAIS-VAUD` ne concerne Arolla ou
le val Ferret : pas de doublon, pas de perte d'alerte par confusion de zone.

**Observation, non bloquante, hors du périmètre d'aujourd'hui** : l'alerte
`TMB-CH-Orsieres|fermeture-deviation-seg-6.35|2026-07-11` (secteur Treutsebo, Prayon↔Branche,
« rive droite de la Dranse de Ferret ») est elle aussi géographiquement dans le val Ferret /
commune d'Orsières — donc dans la même vallée que le nouveau code `VS-Orsieres-ValFerret` —
mais reste alias vers `CH-VALAIS-VAUD` (à ≈ 17 km de son terrain réel, un écart comparable à
celui qui a justifié la création du marqueur Arolla). Je ne touche pas à `ALIAS_ZONE`
(mission 2 = signalement, jamais correction d'autorité, et cet alias est antérieur à mon
passage) : *recommandation* à considérer par l'agent de veille ou un futur passage — si une
prochaine confirmation situe bien Treutsebo/Prayon-Branche dans le corridor val Ferret plutôt
que dans un tronçon distinct côté Champex, ré-aliaser
`TMB-CH-Orsieres → VS-Orsieres-ValFerret` rapprocherait son marqueur de son terrain réel.
Point de style mineur, également non bloquant : les deux nouveaux codes (`CH-Valais-Arolla`,
`VS-Orsieres-ValFerret`) sont en casse mixte alors que les codes existants du référentiel sont
en majuscules (`CH-EST`, `FR-PYR-O`…) ; `resolve_zone()` compare en `fold_txt` (insensible à
la casse) donc cela ne casse rien fonctionnellement, mais une harmonisation en majuscules
serait plus propre si le référentiel est retouché à l'occasion.

## Compte de marqueurs — confirmé

`site/index.html` (ligne 5943) : « **36 zones en alerte active.** » — identique au calcul
direct de `zones_carte(actives, coords)` sur les 84 fiches actives du registre du 08/09
(`len(zones_liste) == 36`, `non_mappées == []`). Le nombre de marqueurs n'a pas bougé malgré
+10 alertes actives depuis le 24/08 et les 2 nouveaux codes : cohérent (les nouvelles alertes
se répartissent sur des zones déjà comptées, et les 2 nouveaux marqueurs remplacent ce qui
aurait sinon été des alertes perdues, sans en ajouter au compte visible avant elles).

## Build & audit — statut final

- `python3 site/audit_qualite.py --ecrire` → section carte : **0 alerte perdue**, 0
  bloquant côté carte (7 constats registre sans lien avec la carte, hors périmètre).
- `python3 site/build_site.py` → **`OK (QA passée)`** (84 actives, 30 clôturées, 51 digests,
  114 fiches), aucune nouvelle `⚠ carte` sur stderr.
- Aucune modification appliquée à `referentiel/zones-coords.csv` par moi : les deux lignes de
  l'opérateur sont confirmées telles quelles, aucune correction n'était nécessaire (écarts de
  moins d'1 km et moins de 10 km respectivement, très en-deçà du seuil de correction).

## Recommandations laissées

1. **`TMB-CH-Orsieres` (alias → `CH-VALAIS-VAUD`)** : à réévaluer pour un ré-aliasage vers
   `VS-Orsieres-ValFerret` si une confirmation situe bien son terrain (Treutsebo,
   Prayon↔Branche) dans le corridor val Ferret plutôt que sur un tronçon distinct. Non
   appliqué (hors périmètre, alias antérieur à mon passage, mission 2 = signalement).
2. Casse des codes `CH-Valais-Arolla` / `VS-Orsieres-ValFerret` : harmoniser en majuscules
   (`CH-VALAIS-AROLLA` / `CH-VALAIS-ORSIERES-FERRET`) par cohérence de style avec le reste du
   référentiel, sans urgence fonctionnelle (le fold insensible à la casse évite tout bug).
3. Recommandations non appliquées du 24/08 toujours valables si le nombre d'alertes augmente
   sur ces zones : `CH-EST` (scission `CH-EST-RHIN`/`CH-OBERLAND`), `IT-CENTRE` (scission
   `IT-TOSCANE-NO`/`IT-LAZIO`), `IT-DOLOMITES` (à surveiller), `ES-CENTRO`, `ES-CYL`, `AT`,
   `IT-NO` — non revuérifiées aujourd'hui, hors périmètre du déclenchement du 08/09 qui ne
   portait que sur les deux zones perdues.

---

# Verdict carte — 2026-08-24

Contrôle de `agents/verificateur-carte.md`, contrôle périodique du lundi. Base : registre du
jour (74 alertes actives, dont 2 zones nouvellement créées le 24/08 — `HauteGaronne-31` et
`HautesPyrenees-65` — déjà raccrochées par l'agent de veille via alias `ALIAS_ZONE → FR-PYR-O`
avant mon passage), `livrables/audit-qualite.md` du 24/08, et le verdict précédent du 12/08
(PR #41).

**36 zones contrôlées** (celles portant au moins une alerte active aujourd'hui), sur 45 zones
présentes dans `referentiel/zones-coords.csv`.

- Alertes perdues (BLOQUANT) : **0** — confirmé par `site/audit_qualite.py`
  (« 0 alerte perdue (carte cohérente avec le registre) ») et par un calcul direct de
  `zones_carte()` : `bs.zones_carte(actives, coords)` renvoie `non_mappées = []` sur les 74
  actives. Rien à ajouter au CSV.
- Compte de marqueurs : **36 attendus / 36 affichés** — `site/index.html` ligne 5170 affiche
  « 36 zones en alerte active. », et `len(zones_carte(...))` = 36. Cohérent.
- `python3 site/build_site.py` → `OK (QA passée)` (aucune nouvelle `⚠ carte`).
  `python3 site/audit_qualite.py` → section carte : `0 alerte perdue`, 0 bloquant côté carte.

Aucune entrée existante de `zones-coords.csv` n'a été modifiée (mission 2 = signalement
seulement, jamais correction d'autorité). Aucune ligne n'a été ajoutée (mission 1 sans objet
aujourd'hui, voir ci-dessous).

Je n'ai pas rédigé les alertes que je contrôle : ce contrôle porte sur des fiches écrites par
l'agent de veille, pas par moi. Rien à signaler sur ce point (règle « pas de fond »).

## Mission 1 — nouvelle zone perdue : rien à traiter

Vérifié moi-même plutôt que pris sur la foi de l'audit : `HauteGaronne-31` et
`HautesPyrenees-65` figurent bien dans `ALIAS_ZONE` (`site/build_site.py` lignes 599-600),
toutes deux → `FR-PYR-O` (départements 31 et 65, cohérent avec `zones-sources.md` §5b :
FR-PYR-O = 64, 65, 31, 09). Un calcul direct confirme que les 74 alertes actives se résolvent
toutes vers un code présent dans `zones-coords.csv` (`non_mappées = []`). Aucune ligne CSV,
aucun alias supplémentaire à recommander.

## Mission 2 — plausibilité des centroïdes existants

### Réévaluation du lot « à surveiller » du 12/08

Le verdict du 12/08 listait 9 zones « acceptables mais larges » avec la consigne « à scinder
si elle en accumule ». Situation au 24/08 :

| Zone | Alertes actives 24/08 | Évolution depuis le 12/08 | Verdict |
|---|---|---|---|
| `ES-AND` | **0** (les 3 alertes actives du 12/08 sont closes : Cómpeta, Los Gallardos, Niebla) | sort du lot | sans objet — plus aucune alerte à placer |
| `ES-CENTRO` | 1 (Guadalajara-LaMierla, même alerte) | inchangé | acceptable mais large, à surveiller (repère La Mierla ≈ 40.95;-3.25, ~170 km du marqueur 39.60;-4.20) |
| `ES-CYL` | 1 (Barjas-Quintela — nouvelle, l'alerte Fermoselle du 12/08 est close) | alerte différente, distance comparable | acceptable mais large, à surveiller (repère Barjas, León ≈ 42.60;-6.97, ~108 km du marqueur 42.35;-5.70) |
| `AT` | 1 (Silvretta, même alerte) | inchangé | acceptable mais large, à surveiller (~104 km) |
| `IT-NO` | 1 (Val Grande, même alerte) | inchangé | acceptable mais large, à surveiller (~90 km) |
| `FR-NOR` | 2 (Loges-Bénouville, Pierrefiques-76) | **déjà corrigé le 12/08** (marqueur déplacé sur la côte d'Albâtre, 49.70;0.35) | plausible — sort du lot, les deux alertes sont à ≤15 km du marqueur |
| `IT-DOLOMITES` | **2** (Brenta + Pelmo, nouvelle) | **accumulée** | voir ci-dessous — reste « à surveiller », pas d'escalade |
| `CH-EST` | **2** (Trübbach + Frutigen, nouvelle) | **accumulée** | **⛔ escalade — à scinder** |
| `IT-CENTRE` | **2** (Carrara + Prato-La-Corte/Veio, nouvelle) | **accumulée** | **⛔ escalade — à scinder** |

### ⛔ Escalade — deux zones ont accumulé une deuxième alerte aux antipodes l'une de l'autre

- **`CH-EST`** — marqueur `46.60;8.90`. Porte désormais deux alertes actives :
  - `CH-EST-Trubbach` (fermeture, déviation seg. 1.1) : Trübbach, vallée du Rhin
    saint-galloise, repère `47.07;9.47` → **68 km** du marqueur (déjà signalé le 12/08).
  - `CH-EST-Frutigen` (fermeture, Kander-Uferweg impraticable, détectée le 18/08) :
    Frutigen, Oberland bernois, repère `46.59;7.65` → **96 km** du marqueur, à l'**opposé**
    de Trübbach (**148 km** séparent les deux localités).
  Le code couvre nominalement « Oberland, Grisons & Tessin » ; les deux alertes actuelles
  sont toutes deux en périphérie de cette zone (Rhin saint-gallois et Oberland bernois), sur
  des versants opposés, et le marqueur ne désigne vraiment ni l'une ni l'autre. C'est le même
  schéma que le cas `DE` tranché le 12/08 (deux terrains éloignés, un centroïde qui ne sert
  aucun des deux). *Recommandation, non appliquée* : si une troisième alerte confirme que
  `CH-EST` sert de fourre-tout, scinder en `CH-EST-RHIN` (repère Sargans/Trübbach ≈
  `47.05;9.45`) et `CH-OBERLAND` (repère Frutigen/Kandersteg ≈ `46.55;7.70`), avec alias
  `CH-EST-Trubbach → CH-EST-RHIN` et `CH-EST-Frutigen → CH-OBERLAND` dans `ALIAS_ZONE`. Les
  deux alertes sont de sévérité MOYENNE (pas d'urgence rouge comme pour le cas DE) : l'action
  peut attendre une troisième occurrence sans induire le randonneur en erreur dans
  l'intervalle — le marqueur reste dans le bon pays et le bon massif alpin, seule la
  localisation fine à l'intérieur de la Suisse orientale est approximative.

- **`IT-CENTRE`** — marqueur `43.50;11.20` (« Toscane, Latium & Émilie »). Porte désormais
  deux alertes actives :
  - `IT-Centre-Carrara` (fermeture, Via Francigena, Nazzano-Bonascola, éboulement) :
    Carrare, Alpes apuanes, repère `44.08;10.10` → **110 km** du marqueur (déjà signalé le
    12/08).
  - `VF-Lazio-Prato-La-Corte` (reroutage, Via Francigena, Formello → La Storta) : Parco di
    Veio / Formello, Latium, aux portes de Rome, repère `42.15;12.41` → **180 km** du
    marqueur, à l'**opposé** de Carrare (**285 km** séparent les deux localités — plus loin
    que Trübbach-Frutigen, du même ordre que Malerweg-Westweg avant la scission du 12/08).
  Le code regroupe tout le tracé italien de la Via Francigena de la Toscane au Latium : les
  deux alertes actuelles sont à ses deux extrémités, et le marqueur (posé entre Florence et
  Sienne) ne représente ni la Toscane du nord ni le Latium. *Recommandation, non appliquée* :
  scinder en `IT-TOSCANE-NO` (repère Carrare ≈ `44.08;10.10`, tronçon Cisa → Lucca/Apuanes)
  et `IT-LAZIO` (repère Formello/Veio ≈ `42.15;12.41`, tronçon Viterbe → Rome), avec alias
  `IT-Centre-Carrara → IT-TOSCANE-NO` et `VF-Lazio-Prato-La-Corte → IT-LAZIO`. Sévérité
  MOYENNE des deux côtés — même remarque que `CH-EST` : pas d'urgence rouge, mais l'écart de
  285 km entre les deux terrains rend la scission plus justifiée ici que pour `CH-EST`.

### ⚠️ Accumulée mais pas aux antipodes — pas d'escalade

- **`IT-DOLOMITES`** — marqueur `46.40;11.80` (« Dolomites, Trentin-Haut-Adige, Vénétie »).
  Porte deux alertes actives :
  - `IT-DOLOMITES-Brenta` (fermeture, Cima Falkner/Bocchette) : Dolomites de Brenta, repère
    `46.17;10.88` → **75 km** du marqueur (déjà signalé le 12/08, à l'ouest).
  - `IT-Dolomites-Pelmo` (fermeture, versant NO du Monte Pelmo, Borca di Cadore, Belluno) :
    repère `46.43;12.14` → **26 km** du marqueur seulement, à l'est.
  Contrairement à `CH-EST` et `IT-CENTRE`, les deux alertes ne sont pas aux extrémités
  opposées d'une zone démesurée : le marqueur reste proche (26 km) de l'alerte la plus
  récente, et l'alerte de Brenta, bien qu'à 75 km, reste dans la même chaîne montagneuse
  contiguë (Trentin). Reste « acceptable mais large, à surveiller » ; pas de scission
  recommandée tant qu'une troisième alerte ne confirme pas un massif tiers (ex. Sella,
  Sesto) qui étirerait encore le centroïde.

### Zones non listées « à surveiller » le 12/08 — contrôle de cohérence rapide

Pour les 27 zones restantes portant une alerte active aujourd'hui, j'ai vérifié que le
département/la province/le massif de chaque nouvelle alerte correspond bien au périmètre
déclaré de son code dans `zones-sources.md` (§1 T1/T2/T3, §2/2b/2c, §5b) :
`FR-PYR-O` (8 alertes : 64/65/31/09, cohérent), `FR-66` (6 : Pyrénées-Orientales, cohérent),
`FR-84-26-07`, `FR-06`, `FR-34-11`, `FR-30-48`, `FR-04-05`, `FR-83`, `FR-BRE`, `FR-CORSE`,
`FR-ALPES-N`, `FR-EST`, `FR-SO`, `FR-13`, `FR-974`, `FR-IDF-CVL`, `DE-SACHSEN`, `DE-SW`,
`UK-SCOTLAND` (codes créés le 12/08, alertes toujours cohérentes avec leur repère de
fondation), `CH-VALAIS-VAUD`, `ES-BALEARES`, `ES-CANARIAS`, `ES-NAV-RIO-ARA`, `PT-NORTE`,
`SI-HR`, `PL-SK-TATRAS`, `GR-E4`, `Cotes-Armor-Trebeurden`. Aucune anomalie : rien ne pointe
vers un pays ou un massif que l'alerte ne concerne pas. Verdict : **plausibles**, sans
recalcul de distance individuel (pas de changement de marqueur ni de nouvelle alerte
« limite » depuis le 12/08 pour ces zones).

## Mission 3 — compte de marqueurs

`site/index.html` (ligne 5170) : « **36 zones en alerte active.** » — confirmé identique au
calcul direct de `zones_carte(actives, coords)` sur les 74 fiches actives du registre
(`site/build_site.py`). Compte juste.

## Hors périmètre — rappel, non retouché

Les deux défauts de vue signalés le 12/08 restent hors du périmètre de cet agent
(`build_site.py` au sens visuel) : vérification rapide, non exhaustive, pour information —
`maxBounds` de la carte va bien jusqu'à 60° E (`site/index.html`, commentaire « La limite EST
doit englober La Réunion ») et `leaflet.css` est chargé dynamiquement (`site/index.html`
ligne 6725) — les deux correctifs du 12/08 semblent tenus. Je n'ai pas revuérifié le contraste
des popups en conditions réelles de navigateur : hors périmètre, non ré-audité ici.

## Recommandations laissées

1. **`CH-EST`** — scinder en `CH-EST-RHIN` (repère Trübbach/Sargans ≈ `47.05;9.45`) et
   `CH-OBERLAND` (repère Frutigen ≈ `46.55;7.70`) + alias `CH-EST-Trubbach` /
   `CH-EST-Frutigen`, si une 3ᵉ alerte confirme l'usage fourre-tout du code. Sévérité MOYENNE
   des deux alertes actuelles : pas d'urgence.
2. **`IT-CENTRE`** — scinder en `IT-TOSCANE-NO` (repère Carrare ≈ `44.08;10.10`) et `IT-LAZIO`
   (repère Formello/Veio ≈ `42.15;12.41`) + alias `IT-Centre-Carrara` /
   `VF-Lazio-Prato-La-Corte`. Écart de 285 km entre les deux terrains actuels — la plus
   fondée des deux recommandations de ce verdict.
3. **`IT-DOLOMITES`** — à surveiller : une 3ᵉ alerte dans un massif tiers (Sella, Sesto,
   Civetta) justifierait de revoir le découpage.
4. Recommandations non appliquées du 12/08 toujours valables si le nombre d'alertes
   augmente sur ces zones : `ES-AND` (sans objet aujourd'hui, plus d'alerte active),
   `ES-CENTRO`, `ES-CYL`, `AT`, `IT-NO` — un seul repère à surveiller par zone, rien
   d'urgent.