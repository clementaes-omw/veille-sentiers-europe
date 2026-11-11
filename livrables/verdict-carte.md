# Verdict carte · 2026-11-11

Agent : Vérificateur Carte. Périmètre : correspondance zone d'alerte → marqueur (`zones-coords.csv` + `ALIAS_ZONE`). Je ne juge pas le fond des alertes.

## Verdict global : CONFORME. Nouveau marqueur Lancieux validé ; 2 centroïdes douteux signalés (PT-CENTRO-SUL, FR-BRE)

- Audit déterministe (`python3 site/audit_qualite.py`, sans `--ecrire`) relancé le 2026-11-11 : **0 alerte perdue**, 0 `⚠ carte`. Les 61 constats bloquants viennent tous du registre (fraîcheur, validités échues), hors périmètre carte.
- `python3 site/build_site.py` : « OK (QA passée) », 103 alertes actives, 48 clôturées (état du registre au moment du contrôle, l'autre agent travaille encore sur `livrables/alertes/`).
- Fichier modifié : `referentiel/zones-coords.csv`. La ligne `Cotes-Armor-Lancieux` (coordonnées inchangées) a été **déplacée** de la fin du fichier vers le bloc « FRANCE (T2/T3) », juste après `Cotes-Armor-Trebeurden`, comme le prévoit la règle de classement par grande région. Le marqueur n'a pas bougé.
- Recherches web utilisées : 1 sur 8.

## 1. Zone prioritaire : Cotes-Armor-Lancieux (ajoutée aujourd'hui)

- Alerte : `fermeture|Cotes-Armor-Lancieux|GR34-digue-La-Roche-travaux|2026-10-29` (fiche `fermeture--cotes-armor-lancieux--gr34-digue-la-roche-travaux--2026-10-29.md`).
- Résolution : correspondance exacte avec le code CSV `Cotes-Armor-Lancieux`, sans alias. La zone a son propre marqueur.
- Centroïde : 48.61 ; -2.15. Repères :
  - bourg de Lancieux ≈ 48.607 ; -2.150 ;
  - la digue de La Roche (XVIIIᵉ s.) ferme les polders de Lancieux, côté estuaire du Frémur. Le point de départ « Pont du Frémur » d'un topo local est à 48.616 ; -2.137, soit **≈ 1 km** du centroïde.
- Verdict : **PLAUSIBLE.** Le marqueur est à la bonne échelle (commune) et dans le bon département (22, Côte d'Émeraude, limite avec l'Ille-et-Vilaine).
- Remarque de cohérence : les alertes GR®34 voisines `Ille-et-Vilaine-Saint-Briac-sur-Mer` (≈ 2 km de Lancieux) et `Ille-et-Vilaine-Dinard` (≈ 7 km) restent rattachées par alias à `FR-BRE` (48.20 ; -3.20), dans le centre de la Bretagne, à **92 et 97 km**. La carte montre donc Lancieux à sa place, tandis que ses voisines immédiates apparaissent à près de 100 km de là. Voir la recommandation n° 2.

## 2. Compte de marqueurs

- Attendu : `zones_carte()` sur les 103 actives donne **45** zones uniques résolues et 0 non mappée.
- Affiché : `site/index.html` (régénéré) annonce « **45** zones en alerte active ». Les deux comptes concordent.
- Variation par rapport au 2026-11-02 (44) : +1 Roncesvalles (ligne ajoutée depuis) +1 Lancieux −1 Trébeurden. L'alerte Trébeurden a été clôturée le 11/11, son marqueur disparaît, ce qui est normal. Sa ligne CSV reste en place sans effet, et rien n'oblige à la supprimer.

## 3. Plausibilité des centroïdes (45 zones contrôlées)

Les distances sont calculées entre le lieu de l'alerte et le centroïde de la zone (repères connus, à ±5 km près).

| Zone | Verdict |
|---|---|
| Cotes-Armor-Lancieux | Plausible (≈ 1 km de la digue). |
| **PT-CENTRO-SUL** (37.90 ; -8.55, Rota Vicentina) | **DOUTEUX** pour 2 alertes sur 3. Odemira-Saboia à ≈ 34 km : correct. Mais **Arganil-Piódão** (Serra do Açor, ≈ 40.23 ; -7.82) est à **≈ 267 km** et **Proença-a-Nova** (≈ 39.75 ; -7.93) à **≈ 213 km**. Ces deux alertes de la région Centro s'affichent sur la côte de l'Alentejo. |
| **FR-BRE** (48.20 ; -3.20) | **DOUTEUX** comme repère d'un sentier littoral : le centroïde tombe à l'intérieur des terres (secteur de Rostrenen). Distances aux alertes : Cap Fréhel ≈ 84 km, Saint-Briac ≈ 92 km, Dinard ≈ 97 km, Piriac ≈ 104 km, Plérin ≈ 47 km. Plomodiern, la rade de Brest et le Finistère restent dans la zone. |
| ES-CENTRO (39.60 ; -4.20) | Limite : Guadalajara / La Mierla (≈ 40.93 ; -3.20) à ≈ 170 km, mais dans la zone nommée (Castilla-La Mancha). À surveiller. |
| ES-NAV-RIO-ARA-Roncesvalles (43.01 ; -1.32) | Plausible. La recommandation du 02/11 a été appliquée. NB : le validateur signale que la validité de l'alerte (01/11) est échue, ce qui relève du fond, pas de mon périmètre. |
| ES-NAV-RIO-ARA (Riglos), ES-GAL, ES-CANARIAS | Plausible. |
| ES-AND | Plausible à l'échelle de l'Andalousie (Igualeja ≈ 107 km, Sierra Nevada ≈ 125 km). Un seul marqueur pour 3 massifs. |
| FR-PYR-O, FR-SO | Plausible pour des zones étendues (Etsaut ≈ 91 km, Mijanes ≈ 123 km ; Landes ≈ 120 km). |
| CH-EST | Limite, comme le 02/11 : Kandersteg / Frutigen, dans l'Oberland, à ≈ 95 km. |
| AT, IT-NO, SCAND-SE | Limite mais dans la zone : Silvretta ≈ 105 km, Val Grande ≈ 88 km, Padjelanta ≈ 98 km. |
| IT-CENTRE | Limite : Carrara ≈ 100 km, dans la zone nommée. |
| CH-VALAIS-VAUD, CH-Valais-Arolla, CH-Valais-Randa, VS-Orsieres-ValFerret, DE-SACHSEN, DE-SW, PL-SK-TATRAS, SI-HR, GR-E4, IS, UK-SCOTLAND, UK-Devon, UK-Cornwall, IT-DOLOMITES, IT-Liguria-CinqueTerre | Plausible. |
| FR-04-05, FR-06, FR-13, FR-83, FR-CORSE, FR-974, FR-30-48, FR-34-11, FR-66, FR-84-26-07, FR-ALPES-N, FR-EST, FR-IDF-CVL, FR-NOR | Plausible. |

## Actions à porter (recommandations, non appliquées)

1. **PT-CENTRO-SUL : centroïde douteux.** Je ne déplace pas l'entrée existante, qui est juste pour Odemira. Il faudrait ajouter dans le bloc « ESPAGNE extension / PT sud » une ligne par alerte du Centro, ce qui ne demande aucune modification de `build_site.py` (une correspondance exacte l'emporte sur le préfixe) :
   - `PT-CENTRO-SUL-Arganil-Piodao;Piódão & Serra do Açor (Arganil);40.23;-7.82` (repère : village de Piódão) ;
   - `PT-CENTRO-SUL-ProencaANova;Proença-a-Nova (Beira Baixa);39.75;-7.93` (repère : bourg de Proença-a-Nova).
   Effet : 47 marqueurs.
2. **Côte d'Émeraude : alias à revoir dans `build_site.py`** (je ne l'ai pas modifié). Pour que les alertes GR®34 voisines s'affichent au même endroit que Lancieux, il faudrait :
   - `"Ille-et-Vilaine-Saint-Briac-sur-Mer": "Cotes-Armor-Lancieux"` (≈ 2 km) ;
   - `"Ille-et-Vilaine-Dinard": "Cotes-Armor-Lancieux"` (≈ 7 km).
   Variante plus propre : renommer le code en `FR-BRE-Emeraude` (« Côte d'Émeraude (Lancieux, Saint-Briac, Dinard) » ; 48.62 ; -2.10) pour éviter qu'un code de commune des Côtes-d'Armor porte des alertes d'Ille-et-Vilaine. Ce choix revient au responsable de `build_site.py`.
3. **FR-BRE** : envisager un centroïde littoral, ou des entrées par secteur (Cap Fréhel, Piriac). Aucune urgence : les alertes restent visibles et dans la bonne région.
4. Centroïdes « limite » (ES-CENTRO, CH-EST, AT, IT-NO, IT-CENTRE, SCAND-SE) : aucune action requise aujourd'hui.

## Bug du générateur

Aucun dans la résolution des zones.

## Point d'indépendance

Je n'ai écrit aucune des alertes contrôlées, ni la ligne Lancieux (je l'ai seulement déplacée dans le bon bloc).

Source du repère Lancieux : topo « Pont du Frémur », point de départ 48.616059 ; -2.136879 (randogps.net, Côtes-d'Armor), et circuit « Autour de Lancieux » n° 14 (cdt35.media.tourinsoft.eu), qui situe la digue de La Roche en bordure des polders.
