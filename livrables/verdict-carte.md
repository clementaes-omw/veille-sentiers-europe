# Verdict carte · 2026-11-23

Agent : Vérificateur Carte (passage hebdomadaire du lundi). Périmètre : correspondance zone d'alerte → marqueur (`zones-coords.csv` + `ALIAS_ZONE`). Je ne juge pas le fond des alertes.

## Verdict global : CONFORME côté référentiel. Aucune alerte perdue, 38 marqueurs attendus ; compte affiché NON VÉRIFIÉ (pas de `site/index.html` local, build interdit ce jour) ; 2 centroïdes douteux reconduits (FR-BRE, IT-CENTRE pour le Latium), 1 nouveau cas limite (FR-EST pour les Vosges du Nord)

- Audit déterministe : `livrables/audit-qualite.md` du 2026-11-23 lu, puis `python3 site/audit_qualite.py` relancé sans `--ecrire` : **0 alerte perdue**, 0 constat carte. Les 10 constats (2 bloquants) viennent du registre, hors périmètre carte.
- Registre au moment du contrôle : 158 fiches, **73 actives**. Un autre agent y travaille encore : le compte peut bouger.
- Résolution recalculée en mémoire avec les fonctions du générateur (`load_alertes`, `load_zones_coords`, `zones_carte`), sans rien écrire. `build_site.py` non lancé (consigne). Recherches web : 0.
- Fichier modifié : ce verdict seulement. `referentiel/zones-coords.csv` inchangé : aucune zone perdue, donc aucune ligne à ajouter.

## Actions à porter (non appliquées), par ordre de priorité

1. **Rebuild et contrôle du compte affiché** (reconduit du 17/11, toujours ouvert). `site/index.html` n'existe pas dans cette copie de travail (fichier ignoré par git, régénéré par la CI). Une fois `livrables/alertes/` stabilisé : `python3 site/build_site.py` doit rendre « OK (QA passée) », sans avertissement carte sur stderr, et afficher « **38** zones en alerte active » si le registre ne bouge plus. Voir le point 2 pour les variations prévisibles.
2. **Tenerife** (reconduit du 16/11 et du 17/11). Ligne proposée, bloc « ESPAGNE extension » : `ES-CANARIAS-Tenerife;Tenerife (Teide, Corona Forestal);28.27;-16.64` (repère : pic du Teide). Aucun alias à toucher, le préfixe le plus long l'emporte ; compte inchangé. Non ajoutée : zone non perdue. À noter : l'audit signale que la validité des deux alertes Tenerife s'arrêtait au 20/11 ; si le vérificateur d'alertes les clôt, le marqueur ES-CANARIAS disparaît et le compte attendu passe à **37**.
3. **Latium / Via Francigena** (reconduit du 16/11). Ajouter `IT-CENTRE-Lazio;Latium (Via Francigena, Parco di Veio, Rome);42.07;12.40` (repère : Formello / La Storta) et pointer l'alias `"VF-Lazio-Prato-La-Corte"` vers `IT-CENTRE-Lazio` dans `build_site.py`. Effet : +1 marqueur.
4. **Côte d'Émeraude** (reconduit du 11/11). Alias à revoir dans `build_site.py` : `"Ille-et-Vilaine-Saint-Briac-sur-Mer"` et `"Ille-et-Vilaine-Dinard"` → `Cotes-Armor-Lancieux` (≈ 2 km et ≈ 7 km du marqueur, contre plus de 90 km aujourd'hui). Compte inchangé.
5. **Valais** (reconduit du 16/11). Alias à revoir dans `build_site.py` : `"CH-Europaweg-Randa-Zermatt"` → `CH-Valais-Randa` ; `"TMB-CH-Orsieres"` → `VS-Orsieres-ValFerret`. Effet aujourd'hui : le marqueur CH-VALAIS-VAUD ne porte plus que ces deux alertes (la fiche Sainte-Croix / Baulmes n'est plus active), il disparaîtrait donc, soit -1 marqueur.
6. **Vosges du Nord (nouveau, facultatif).** L'alerte `fermeture|FR-EST-BasRhin-Obersteinbach|GR53-lavoir-gabelfels-tornade|2026-08-04` s'affiche sur le centroïde FR-EST, dans les Hautes-Vosges (secteur de Gérardmer), à ≈ 122 km d'Obersteinbach. Ligne proposée, bloc « FRANCE (T2/T3) » : `FR-EST-BasRhin;Vosges du Nord (GR53, Bas-Rhin);49.03;7.69` (repère : commune d'Obersteinbach). Aucun alias à toucher (préfixe). Compte inchangé tant que FR-EST ne porte que cette alerte. Non ajoutée : zone non perdue.
7. **Chartreuse** (reconduit du 17/11, facultatif). `FR-ALPES-N-Chartreuse;Chartreuse (Dent de Crolles, Isère);45.31;5.86`. La zone `FR-ALPES-N-Chartreuse` est bien celle de la fiche active, le préfixe suffirait. Effet : +1 marqueur. Non ajoutée : zone non perdue.
8. **Lot / GR65 (nouveau, pour information).** L'alias `"Lot-Cieurac-Flaujac-Poujols": "FR-SO"` contredit le rattachement du §5b de `zones-sources.md` (département 46 → FR-MC). Depuis la clôture de Landes-Gironde, le marqueur FR-SO (Lot-et-Garonne) ne porte plus que cette alerte, à ≈ 85 km. Je ne recommande PAS de suivre le §5b : le centroïde FR-MC (Cantal) est à ≈ 134 km de Cieurac, donc plus loin. Si l'on veut un point juste : ligne `FR-SO-Lot;Quercy (GR65, Cahors, Lot);44.45;1.44` (repère : Cahors) et alias pointé dessus. Sinon, aucune action.
9. **FR-BRE** (reconduit) : centroïde à l'intérieur des terres pour 8 alertes littorales ; envisager un centroïde littoral ou des entrées par secteur.
10. **Rangement du CSV (nouveau, mineur).** La ligne `ES-NAV-RIO-ARA-Roncesvalles` est en fin de fichier, sous le bloc « Extension v3 (Scandinavie, Balkans, Grèce, Tatras) », au lieu du bloc « ESPAGNE & PORTUGAL nord ». Sans effet sur la carte. Entrée existante : je ne la déplace pas.

## 1. Zones perdues

Aucune. Les 73 alertes actives se résolvent toutes vers un code de `zones-coords.csv` (0 zone non mappée). Aucune ligne ajoutée au CSV.

## 2. Compte de marqueurs

- Attendu : `zones_carte()` sur les 73 actives donne **38** zones uniques résolues.
- Affiché : **non vérifiable ce jour**. `site/index.html` est absent du dépôt local et le build est suspendu par consigne. Le contrôle du texte « N zones en alerte active » reste à faire après le build (action n° 1).
- Variation par rapport au 17/11 (38) : **FR-13 sort** (Sainte-Victoire clôturée, plus d'alerte active dans les Bouches-du-Rhône), **FR-EST entre** (fiche Obersteinbach créée le 19/11). Les trois autres clôtures ne retirent aucun marqueur : FR-SO garde l'alerte du Lot, FR-PYR-O garde 5 alertes (Luchon et Haute-Garonne n'étaient pas seules sur leur zone).

## 3. Plausibilité des centroïdes (38 zones contrôlées)

Distances à vol d'oiseau entre le lieu de l'alerte et le centroïde, repères connus, à ±5 km près.

| Zone | Verdict |
|---|---|
| **FR-BRE** (48.20 ; -3.20), 8 alertes | **DOUTEUX**, inchangé : centroïde dans les terres (secteur de Rostrenen), alertes littorales à 49-103 km. Action n° 9, et n° 4 pour Saint-Briac et Dinard. |
| **IT-CENTRE** (43.50 ; 11.20), 2 alertes | **DOUTEUX pour 1 alerte sur 2**, inchangé : Formello / La Storta (Latium) à ≈ 175 km du marqueur, qui tombe dans le Chianti. Carrara ≈ 109 km : limite. Action n° 3. |
| **FR-EST** (48.10 ; 6.80), 1 alerte, zone revenue sur la carte | **Limite** (nouveau). Obersteinbach (Vosges du Nord, Bas-Rhin, ≈ 49.03 ; 7.69) à ≈ 122 km d'un marqueur placé dans les Hautes-Vosges. Dans la zone nommée (67) et dans le massif vosgien, mais à l'autre extrémité. Action n° 6. |
| FR-SO (44.10 ; 0.50), 1 alerte | Limite : Cieurac (Lot, ≈ 44.37 ; 1.50) à ≈ 85 km, seule alerte restante. Action n° 8. |
| FR-ALPES-N (45.50 ; 6.50), 2 alertes | Plausible : Pralognan ≈ 20 km ; Dent de Crolles (Chartreuse) ≈ 55 km, éloigné mais dans la zone. Action n° 7. |
| ES-CANARIAS (28.35 ; -16.20), 2 alertes | Plausible à l'échelle de l'archipel, inchangé : Teide ≈ 44 km, point en mer à l'est de Tenerife. Action n° 2. |
| CH-VALAIS-VAUD (46.15 ; 7.30), 2 alertes | Plausible, mais ne porte plus que les deux alertes mieux servies par des codes voisins (Randa ≈ 37 km, Orsières ≈ 18 km). Action n° 5. |
| ES-CENTRO, ES-AND, CH-EST, AT, IT-NO, SCAND-SE | Limite mais dans la zone, inchangé : La Mierla ≈ 169 km ; Sierra Nevada ≈ 125 km et Gaitanes ≈ 66 km ; Kandersteg / Frutigen ≈ 95 km ; Silvretta ≈ 104 km ; Val Grande ≈ 89 km et Biellese ≈ 59 km ; Padjelanta ≈ 95 km. |
| FR-PYR-O (42.85 ; 0.55), 5 alertes | Plausible pour un corridor étendu : vallée d'Aspe ≈ 91 km, Bordes-Uchentein ≈ 37 km. Composition allégée (Luchon et Haute-Garonne clôturées), centroïde toujours central. |
| IT-DOLOMITES (46.40 ; 11.80), 5 alertes | Plausible : Brenta ≈ 73 km, Val Cimoliana ≈ 52 km, Pelmo, Borca di Cadore et Cortina à moins de 40 km. |
| IT-Liguria-CinqueTerre (44.13 ; 9.68), 1 alerte | Plausible : Corniglia, Volastra et Vernazza à moins de 5 km. La fiche active est désormais celle des sentiers 587 / 586. |
| ES-NAV-RIO-ARA-Roncesvalles (43.01 ; -1.32) | Plausible : sur le village de Roncesvalles, col de Lepoeder à ≈ 3 km. |
| ES-NAV-RIO-ARA (42.55 ; -0.70), 1 alerte | Plausible : San Juan de la Peña ≈ 5 km, Riglos ≈ 22 km. |
| CH-Valais-Gondo, CH-Valais-Arolla, CH-Valais-Randa, VS-Orsieres-ValFerret, Cotes-Armor-Lancieux, DE-SACHSEN, DE-SW, UK-SCOTLAND, UK-Devon, UK-Cornwall, PL-SK-TATRAS | Plausible : marqueur sur le lieu ou à moins de 35 km. |
| FR-04-05, FR-06, FR-34-11, FR-66 (Cerbère ≈ 60 km), FR-84-26-07 (Die ≈ 53 km), FR-974, FR-CORSE (Bavella ≈ 40 km), FR-IDF-CVL (Fontainebleau ≈ 13 km), FR-NOR (Bénouville ≈ 8 km) | Plausible. |

Sorties depuis le 17/11 : FR-13 (sans objet, plus d'alerte active).

## Bug du générateur

Aucun dans la résolution des zones.

## Point d'indépendance

Je n'ai écrit aucune des alertes contrôlées, ni aucune ligne de `zones-coords.csv`. Aucune fiche, aucun script et aucun journal touchés.
