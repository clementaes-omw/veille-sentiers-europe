# Verdict carte — 2026-08-12

Contrôle de `agents/verificateur-carte.md` exécuté sur la carte issue de la PR #39.
**34 zones contrôlées** (celles portant au moins une alerte active), sur 45 zones
présentes dans `referentiel/zones-coords.csv`.

- Alertes perdues (BLOQUANT) : **0** — aucune ligne à ajouter au CSV.
- Compte de marqueurs : **34 attendus / 34 affichés** — vérifié dans un vrai navigateur,
  le libellé public dit « 34 zones en alerte active. »
- Centroïdes contrôlés : 34 — **2 à revoir**, 9 acceptables mais larges, 23 plausibles.

Aucune entrée existante n'a été modifiée (le périmètre de l'agent l'interdit) : tout ce qui
suit est une recommandation.

Méthode : pour chaque zone, distance orthodromique entre le marqueur publié et un repère
géographique connu du terrain réellement visé par ses alertes. Le repère utilisé est cité à
chaque fois — aucune coordonnée n'a été inventée.

## ⛔ Centroïdes à revoir

- **`DE`** — Allemagne (Forêt-Noire, Saxe, Rhin), marqueur `49.80;9.50` (Basse-Franconie).
  Le code est un fourre-tout national dont les deux alertes actives sont aux antipodes l'une
  de l'autre : la **rouge** (Malerweg / Sächsische Schweiz, repère Bastei `50.96;14.07`) est
  affichée à **349 km** de son massif, l'orange (Westweg, repère Oppenau `48.47;8.17`) à
  **177 km**. Le marqueur ne désigne aucun des deux terrains — il tombe dans une région que
  ni l'une ni l'autre alerte ne concerne. C'est le cas d'école décrit par la spec de l'agent.
  *Recommandation* : scinder en deux codes — `DE-SW` (Forêt-Noire, repère Fribourg-en-Brisgau
  ≈ `48.00;8.10`) et `DE-SACHSEN` (Suisse saxonne, repère Bastei ≈ `50.95;14.07`) — puis
  aliaser `DE-Schwarzwald-Oppenau → DE-SW` et `DE-Sachsen-SaechsischeSchweiz → DE-SACHSEN`
  dans `ALIAS_ZONE`. Priorité : c'est la seule alerte **rouge** mal placée du lot.
- **`UK-IE`** — Îles Britanniques & Irlande, marqueur `54.50;-3.50` (Cumbria / Lake District).
  L'unique alerte active porte sur **Glenmore, dans les Cairngorms** (repère `57.10;-3.67`),
  soit **289 km** au nord. Un code couvrant deux nations et l'Irlande ne peut pas produire un
  marqueur juste. *Recommandation* : créer `UK-SCOTLAND` (repère Aviemore ≈ `57.19;-3.83`) et
  aliaser `UK-Cairngorms-Glenmore` dessus.

## ⚠️ Acceptables, mais larges — à surveiller

Marqueur régionalement correct, mais la zone est si vaste que le repère s'éloigne du terrain.
Aucune action tant que la zone ne porte qu'une alerte ; à scinder si elle en accumule.

| Zone | Marqueur | Terrain réel de l'alerte (repère) | Écart |
|---|---|---|---|
| `ES-AND` | 37.50;-4.60 | Niebla, Huelva (37.36;-6.68) | 184 km |
| `ES-CENTRO` | 39.60;-4.20 | La Mierla, Guadalajara (40.95;-3.25) | 170 km |
| `ES-CYL` | 42.35;-5.70 | Fermoselle, Zamora (41.32;-6.40) | 128 km |
| `IT-CENTRE` | 43.50;11.20 | Carrare, Apuanes (44.08;10.10) | 109 km |
| `AT` | 47.20;11.40 | Silvretta, Vorarlberg (46.90;10.10) | 104 km |
| `IT-NO` | 45.70;7.40 | PN Val Grande, Verbano (46.05;8.45) | 90 km |
| `IT-DOLOMITES` | 46.40;11.80 | Dolomites de Brenta (46.17;10.88) | 75 km |
| `CH-EST` | 46.60;8.90 | Trübbach, vallée du Rhin SG (47.07;9.48) | 68 km |
| `FR-NOR` | 49.35;0.35 | Étretat / Les Loges (49.71;0.20) | 41 km |

Deux remarques de fond sur ce tableau :

- **`FR-NOR`** est le plus facile à améliorer : la zone s'intitule « Normandie (GR21, côte
  d'Albâtre) » et ses deux alertes sont sur la côte, mais le marqueur est posé **au sud de
  l'estuaire de la Seine**, hors de la côte d'Albâtre. Repère attendu ≈ `49.70;0.35` (entre
  Fécamp et Étretat). Recommandé, non appliqué.
- **`CH-EST`** : Trübbach est dans la vallée du Rhin saint-galloise, hors des trois régions
  que le code annonce (Oberland, Grisons, Tessin). Le marqueur reste plausible à l'échelle
  suisse ; c'est le rattachement de la zone qui est discutable, pas la coordonnée.

## ✅ Centroïdes plausibles (23)

`CH-VALAIS-VAUD` (Sion, alertes Europaweg/TMB à ≤40 km) · `ES-BALEARES` (centre de Majorque)
· `ES-CANARIAS` (côte est de Tenerife) · `FR-04-05` (Embrun/Guillestre, GR54) · `FR-06`
(haute Vésubie, Mercantour) · `FR-13` (entre Aix et les Calanques) · `FR-30-48` (Florac /
mont Lozère) · `FR-34-11` (milieu exact Hérault–Aude) · `FR-66` (Canigou, 42.55;2.45) ·
`FR-83` (centre du Var) · `FR-84-26-07` (Vaucluse/Drôme/Ardèche) · `FR-974` (centre de La
Réunion, exact) · `FR-ALPES-N` (Vanoise) · `FR-BRE` (centre du corridor GR34 ; un sentier en
boucle littorale a par construction son centroïde à l'intérieur des terres — le moins mauvais
choix) · `FR-CORSE` (centre de l'île, GR20) · `FR-EST` (Vosges, 88) · `FR-IDF-CVL`
(Fontainebleau) · `FR-PYR-O` (Luchonnais, milieu du 64–09) · `FR-SO` (Agenais, milieu
Landes–Lot) · `GR-E4` (Crète ouest, Samaria) · `PL-SK-TATRAS` (Tatras, exact : Rysy et Kriváň
à moins de 10 km) · `PT-NORTE` (milieu Porto–Valença) · `SI-HR` (Alpes juliennes, 30 km de
Triglav).

## Hors périmètre « coordonnées » — deux défauts de la vue

Signalés ici parce qu'ils rendent des marqueurs faux ou inutilisables, mais ils relèvent de
`site/build_site.py`, que cet agent ne modifie pas.

1. **Le marqueur de La Réunion est inatteignable.** Sa coordonnée est pourtant exacte. Le
   `maxBounds` de la carte s'arrête à la longitude **40° E** alors que La Réunion est à
   **55,52° E**. Vérifié au navigateur : demander à centrer dessus aux zooms 4 à 8 recale le
   centre à la longitude 37,92° et le marqueur **reste hors écran** ; il n'apparaît qu'aux
   zooms ≤ 3, en vue monde. L'alerte GRR2 (orange, fermetures de sentiers) est donc publiée
   sur une carte qui interdit d'y accéder. Correctif : porter la limite est à ≈ 60° E.
2. **Popups illisibles en thème sombre.** Contraste mesuré du nom de sentier : **1,27:1**
   (seuil AA : 4,5:1). Cause : `leaflet.css` est injecté *après* le `<style>` de la page, donc
   les règles à une seule classe de la feuille du site (`.leaflet-popup-content-wrapper`,
   `.leaflet-bar a`, `.leaflet-control-attribution`) perdent la cascade et le fond redevient
   blanc, tandis que les couleurs de texte (sélecteurs à deux classes) restent claires.

## Suite donnée — 2026-08-12, même jour

Les trois recommandations de centroïdes ont été appliquées, et les deux défauts de la vue
corrigés. Écarts mesurés après coup, aux mêmes repères :

| Zone | Avant | Après | Alerte concernée |
|---|---|---|---|
| `DE-SACHSEN` (neuf) | 349 km | **4 km** | Malerweg, **rouge** |
| `DE-SW` (neuf) | 177 km | **19 km** | Westweg |
| `UK-SCOTLAND` (neuf) | 289 km | **23 km** | Cairngorms |
| `FR-NOR` (déplacé) | 41 km | **11 km** | GR21 |

`DE` et `UK-IE` restent au référentiel mais ne portent plus aucune alerte : ils ne servent
plus que de **repli** pour un massif encore sans code propre. C'est un choix de prudence
plutôt que de rigueur — les retirer ferait tomber la prochaine alerte allemande ou
britannique non aliasée en « alerte perdue », donc en BLOQUANT, ce qui la rendrait visible
tout de suite ; les garder la fera atterrir en silence sur un centroïde national faux. À
trancher si un jour la carte devient la porte d'entrée principale du site.

Le compte de marqueurs passe de 34 à **35** (l'Allemagne compte désormais pour deux).

## Recommandations laissées

1. Scinder `DE` en `DE-SW` / `DE-SACHSEN` + 2 alias — **alerte rouge concernée**.
2. Créer `UK-SCOTLAND` + alias `UK-Cairngorms-Glenmore`.
3. Déplacer `FR-NOR` sur la côte d'Albâtre (≈ 49.70;0.35).
4. Étendre le `maxBounds` de la carte à la longitude 60° E (sinon La Réunion reste hors d'accès).
5. Charger `leaflet.css` avant le `<style>` de la page, ou renforcer les sélecteurs du thème.
