# Verdict carte · 2026-11-25

Agent : Vérificateur Carte (passage ciblé). Périmètre : correspondance zone d'alerte → marqueur (`zones-coords.csv` + `ALIAS_ZONE`). Je ne juge pas le fond des alertes. Je n'ai pas écrit l'alerte contrôlée ni la ligne CSV contrôlée.

## Verdict global : CONFORME. 0 alerte perdue, 39 marqueurs attendus = 39 affichés. Repère Brière plausible, conservé tel quel.

- `python3 site/audit_qualite.py` (sans `--ecrire`) : 162 fiches, **0 alerte perdue**, 0 constat carte. Les 13 constats (2 bloquants) relèvent du registre, hors périmètre carte.
- `python3 site/build_site.py` : « OK (QA passée) », 77 actives, **aucun `⚠ carte`** sur stderr.
- Recalcul en mémoire (`load_alertes`, `load_zones_coords`, `zones_carte`) : 77 actives, 39 zones résolues uniques, 0 non mappée.
- Recherches web : 0 (repères connus suffisants). Fichiers modifiés : ce verdict seulement. `zones-coords.csv` et `build_site.py` inchangés par moi. `site/index.html` régénéré par le build (fichier ignoré par git).
- Un autre agent modifie `livrables/alertes/` en parallèle : le compte peut bouger.

## 1. Zone contrôlée : `Loire-Atlantique-Briere`

Alerte : `fermeture|Loire-Atlantique-Briere|GRP-Tour-de-Briere-travaux-passerelles|2026-06-24` (active, MOYENNE).

Ligne ajoutée avant mon passage (bloc « FRANCE (T2/T3) », sous FR-BRE) :
`Loire-Atlantique-Briere;Marais de Brière (GRP Tour de Brière, Loire-Atlantique);47.36;-2.25`

- **Résolution** : correspondance exacte du code → marqueur propre. OK.
- **Plausibilité : PLAUSIBLE.** Repère : centre de la Grande Brière (marais entre Saint-Joachim 47.38/-2.19, Saint-Lyphard 47.40/-2.30, La Chapelle-des-Marais 47.45/-2.24, Saint-André-des-Eaux 47.32/-2.31 et Saint-Nazaire 47.27/-2.21). Le point est à l'intérieur de la boucle du GRP (67 km) et à moins de 10 km des lieux cités par l'alerte (Bréca, Fossés Blancs, Rozé, Loncé).
- **Écart à la règle « préférer un alias »** : selon le §5b de `zones-sources.md`, le 44 relève de **FR-BRE**, et la règle invite à un alias `ALIAS_ZONE` plutôt qu'à une ligne CSV neuve. Je ne le recommande pas ici : le centroïde FR-BRE (48.20 ; -3.20, centre Bretagne) est à environ 117 km de la Brière et déjà jugé douteux. Un alias vers FR-BRE dégraderait la position. La ligne dédiée suit le précédent `Cotes-Armor-Trebeurden` / `Cotes-Armor-Lancieux`. Le nom du code sort de la convention `XX-…` (on aurait pu écrire `FR-BRE-Briere`, qui se résout aussi par préfixe), mais c'est sans effet sur la carte. Je ne renomme pas une entrée existante.
- **Effet sur le compte** : +1 marqueur. La zone ne se fond dans aucun autre code.

## 2. Compte de marqueurs

Attendu (zones uniques actives résolues) : **39**. Affiché dans `site/index.html` : « **39** zones en alerte active ». **Conforme.**
(Le 23/11, 38 étaient attendus ; le +1 vient de la Brière, et les autres mouvements du registre se compensent.)

## 3. Recommandations laissées (non appliquées)

Aucune nouvelle. Les actions 2 à 10 du verdict du 23/11 sont reconduites sans réexamen dans ce passage ciblé : Tenerife (ligne `ES-CANARIAS-Tenerife`), Latium (`IT-CENTRE-Lazio` + alias), Côte d'Émeraude (alias Dinard et Saint-Briac → `Cotes-Armor-Lancieux`), Valais (alias Randa et Orsières), Vosges du Nord, Chartreuse, Lot / GR65, FR-BRE (centroïde dans les terres) et le rangement de la ligne Roncesvalles. L'action 1 du 23/11 (rebuild et compte affiché) est **close** : le build est passé et le compte a été vérifié.

Facultatif : si l'on souhaite un jour aligner le code sur la convention, renommer `Loire-Atlantique-Briere` en `FR-BRE-Briere` dans le CSV. La résolution reste correcte par préfixe (`FR-BRE-Briere` est plus long que `FR-BRE`), à condition de renommer aussi la zone de la fiche. Ce renommage est hors de mon périmètre.
