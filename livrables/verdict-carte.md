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
ligne 6725) — les deux correctifs du 12/08 semblent tenus. Je n'ai pas revérifié le contraste
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