# Verdict carte · 2026-11-16

Agent : Vérificateur Carte (passage hebdomadaire du lundi). Périmètre : correspondance zone d'alerte → marqueur (`zones-coords.csv` + `ALIAS_ZONE`). Je ne juge pas le fond des alertes.

## Verdict global : CONFORME. Aucune alerte perdue, 38 marqueurs attendus et affichés ; 2 centroïdes douteux (FR-BRE, IT-CENTRE pour le Latium) et 3 alias à revoir

- Audit déterministe (`python3 site/audit_qualite.py`, sans `--ecrire`) relancé le 2026-11-16 : **0 alerte perdue**, 0 constat carte. Les 15 constats bloquants viennent tous du registre, hors périmètre carte.
- Aucun fichier modifié hormis ce verdict. `referentiel/zones-coords.csv` est inchangé : aucune zone perdue, donc aucune ligne à ajouter.
- `python3 site/build_site.py` **non relancé** : il n'est exigé qu'après un ajout au CSV, et il aurait réécrit `site/index.html` pendant que le vérificateur d'alertes modifie encore `livrables/alertes/`. La résolution des zones a été recalculée en mémoire avec les fonctions du générateur (`load_alertes`, `zones_carte`), sans rien écrire.
- État du registre au moment du contrôle : 153 fiches, 74 actives. Il peut encore bouger d'ici la fin du passage de l'autre agent.
- Recherches web utilisées : 0. Tous les repères sont des lieux connus (communes, sommets, parcs).

## 1. Zones perdues

Aucune. Les 74 alertes actives se résolvent toutes vers un code de `zones-coords.csv`.

## 2. Compte de marqueurs

- Attendu : `zones_carte()` sur les 74 actives donne **38** zones uniques résolues, 0 non mappée.
- Affiché : `site/index.html` annonce « **38** zones en alerte active ». Les deux comptes concordent.
- Variation par rapport au 2026-11-11 (45) : sept zones n'ont plus d'alerte active (PT-CENTRO-SUL, ES-GAL, FR-83, FR-30-48, FR-EST, SI-HR, GR-E4). Leurs marqueurs disparaissent, ce qui est normal ; aucune zone nouvelle.

## 3. Plausibilité des centroïdes (38 zones contrôlées)

Distances à vol d'oiseau entre le lieu de l'alerte et le centroïde de la zone (repères connus, à ±5 km près).

| Zone | Verdict |
|---|---|
| **FR-BRE** (48.20 ; -3.20) | **DOUTEUX**, inchangé depuis le 11/11. Le centroïde tombe à l'intérieur des terres (secteur de Rostrenen) pour 8 alertes toutes littorales : Plérin ≈ 49 km, Plomodiern ≈ 76 km, Cap Fréhel ≈ 84 km, Saint-Briac ≈ 92 km, rade de Brest ≈ 94 km, Dinard ≈ 97 km, Piriac ≈ 103 km. |
| **IT-CENTRE** (43.50 ; 11.20) | **DOUTEUX pour 1 alerte sur 2** (nouveau constat). `VF-Lazio-Prato-La-Corte` concerne le tronçon Formello → La Storta, dans le Parco di Veio aux portes de Rome (≈ 42.07 ; 12.40), soit **≈ 175 km** du marqueur, qui tombe dans le Chianti. Carrara ≈ 109 km : limite, dans la zone nommée. |
| ES-CENTRO (39.60 ; -4.20) | Limite : La Mierla (Guadalajara, ≈ 40.93 ; -3.24) à ≈ 169 km, dans la zone nommée. À surveiller. |
| ES-AND (37.50 ; -4.60) | Limite : Sierra Nevada / Sulayr ≈ 125 km, Desfiladero de los Gaitanes ≈ 66 km. Un seul marqueur pour deux massifs. |
| FR-SO, FR-PYR-O | Plausible pour des zones étendues : Landes-Gironde ≈ 106 km, Cieurac (Lot) ≈ 85 km ; vallée d'Aspe ≈ 91 km, Bordes-Uchentein ≈ 37 km. |
| AT, CH-EST, SCAND-SE, IT-NO | Limite mais dans la zone : Silvretta ≈ 104 km, Kandersteg / Frutigen ≈ 95 km, Padjelanta ≈ 95 km, Val Grande ≈ 89 km (Biellese ≈ 59 km). |
| IS (64.30 ; -19.00) | Plausible : Fimmvörðuháls ≈ 78 km, au sud des Hautes Terres. |
| ES-CANARIAS (28.35 ; -16.20) | Plausible à l'échelle de l'archipel : Teide ≈ 44 km. Le point tombe en mer, au large de la côte est de Tenerife, entre Tenerife et Gran Canaria. Voir la recommandation n° 5. |
| CH-VALAIS-VAUD (46.15 ; 7.30) | Plausible, mais incohérent avec deux codes voisins : l'alerte Europaweg Randa-Zermatt s'y affiche à ≈ 37 km de Randa alors que `CH-Valais-Randa` a son propre marqueur sur place ; l'alerte TMB Orsières s'y affiche à ≈ 18 km alors que `VS-Orsieres-ValFerret` est à ≈ 14 km. Voir la recommandation n° 3. |
| IT-DOLOMITES | Plausible : Brenta ≈ 73 km, Val Cimoliana (Dolomites frioulanes) ≈ 52 km, Pelmo, Borca di Cadore et Cortina à moins de 40 km. |
| PL-SK-TATRAS | Plausible : TANAP (Hautes Tatras slovaques) ≈ 10 km. |
| Cotes-Armor-Lancieux, ES-NAV-RIO-ARA-Roncesvalles, ES-NAV-RIO-ARA (Riglos, San Juan de la Peña), CH-Valais-Arolla, CH-Valais-Randa, VS-Orsieres-ValFerret, IT-Liguria-CinqueTerre, DE-SACHSEN, DE-SW, UK-SCOTLAND, UK-Devon, UK-Cornwall | Plausible. |
| FR-04-05, FR-06, FR-13 (Sainte-Victoire ≈ 22 km), FR-34-11, FR-66, FR-84-26-07 (Die ≈ 53 km), FR-974, FR-ALPES-N, FR-CORSE (Bavella ≈ 40 km), FR-IDF-CVL, FR-NOR | Plausible. |

## Actions à porter (recommandations, non appliquées)

1. **Latium / Via Francigena (nouveau).** L'alias `"VF-Lazio-Prato-La-Corte": "IT-CENTRE"` de `build_site.py` passe avant toute correspondance CSV : la correction exige donc de toucher l'alias, ce que je ne fais pas. Proposition : ajouter au bloc « ALPES & Europe du Nord-Ouest » la ligne `IT-CENTRE-Lazio;Latium (Via Francigena, Parco di Veio, Rome);42.07;12.40` (repère : Formello / La Storta) et pointer l'alias vers `IT-CENTRE-Lazio`. Effet : 39 marqueurs.
2. **Côte d'Émeraude : alias à revoir dans `build_site.py`** (reconduit du 11/11, non appliqué). Saint-Briac est à ≈ 2 km du marqueur Lancieux et Dinard à ≈ 7 km, mais les deux s'affichent à plus de 90 km :
   - `"Ille-et-Vilaine-Saint-Briac-sur-Mer": "Cotes-Armor-Lancieux"` ;
   - `"Ille-et-Vilaine-Dinard": "Cotes-Armor-Lancieux"`.
   Variante plus propre : renommer le code en `FR-BRE-Emeraude` (« Côte d'Émeraude (Lancieux, Saint-Briac, Dinard) » ; 48.62 ; -2.10).
3. **Valais : alias à revoir dans `build_site.py`** (nouveau) :
   - `"CH-Europaweg-Randa-Zermatt": "CH-Valais-Randa"` (le code existe déjà, 46.10 ; 7.78, sur le lieu même) ;
   - `"TMB-CH-Orsieres": "VS-Orsieres-ValFerret"` (gain faible, mais une seule épingle pour Orsières).
   Effet : le marqueur CH-VALAIS-VAUD disparaît tant qu'aucune autre alerte ne le porte, soit 37 marqueurs.
4. **FR-BRE** (reconduit) : envisager un centroïde littoral ou des entrées par secteur (Cap Fréhel, rade de Brest, Piriac). Les alertes restent visibles et en Bretagne.
5. **ES-CANARIAS** : si les alertes Tenerife se répètent, une ligne `ES-CANARIAS-Tenerife;Tenerife (Teide, Corona Forestal);28.27;-16.64` (repère : pic du Teide) placerait le marqueur sur l'île, sans toucher `build_site.py` (le préfixe le plus long l'emporte). Non ajoutée : la zone n'est pas perdue, et je n'ajoute une ligne que pour une alerte sans marqueur.
6. **PT-CENTRO-SUL** (recommandation du 11/11) : sans objet aujourd'hui, la zone ne porte plus d'alerte active. Elle redeviendra utile si une alerte de la région Centro (Arganil, Proença-a-Nova) est rouverte.
7. Centroïdes « limite » (ES-CENTRO, ES-AND, CH-EST, AT, IT-NO, SCAND-SE) : aucune action requise.

## Bug du générateur

Aucun dans la résolution des zones.

## Point d'indépendance

Je n'ai écrit aucune des alertes contrôlées, ni aucune ligne de `zones-coords.csv` lors de ce passage.
