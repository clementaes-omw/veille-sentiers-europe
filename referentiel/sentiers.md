# Référentiel sentiers — Veille Sentiers Europe (PILOTE) — vue prioritaire

**⚠ La base complète est `sentiers-db.csv`** (582 itinéraires : 192 GR + 331 GRP + 37 GRT +
18 caminos + hautes routes ; colonnes `code;nom;type;pays;zones_sources;priorite;source;notes`,
priorités P1 = à citer nommément dans les alertes / P2 = GR secondaires / P3 = GRP-GRT /
HP = hors périmètre). Construite le 2026-07-17 depuis les listes FFRandonnée relayées par
Wikipédia (script : `outils/build_db.py`, rejouable) + couches curées Caminos/Hautes Routes.
Le mapping sentier→zone est dérivé des départements (affectation : `zones-sources.md` §6) —
fiable pour les P1 (calés GPX/tracés connus), estimé pour le reste.

Ce fichier-ci reste la **vue lisible des prioritaires** : mapping des itinéraires qu'on cite
dans les alertes. **Principe de couverture** : la veille surveille des zones-sources — tout
GR®/GRP/camino qui traverse une zone surveillée est couvert de fait, même hors de cette vue.

Périmètre pilote : France + Réunion + Compostelle (Espagne, + tramo portugais en bonus).
⭐ = itinéraire présent dans l'app OMW (héritage de la veille existante).

## 1. France — grands itinéraires

| Itinéraire | Nom usuel | Zones-sources |
|------------|-----------|---------------|
| GR5 ⭐ | Sentier de l'Europe / Grande Traversée des Alpes | FR-EST, FR-ALPES-N, FR-04-05, FR-06 |
| GR10 ⭐ | Traversée des Pyrénées | FR-PYR-O, FR-66 |
| HRP ⭐ | Haute Route Pyrénéenne | FR-PYR-O, FR-66, ES-NAV-RIO-ARA, ES-CAT |
| HRMP ⭐ | Haute Route des Monts Perdus | FR-PYR-O, ES-NAV-RIO-ARA |
| GR20 ⭐ | Traversée de la Corse (Fra li monti) | FR-CORSE |
| GR21 ⭐ | Sentier des falaises (Normandie) | FR-NOR |
| GR34 ⭐ | Sentier des douaniers (Bretagne) | FR-BRE |
| GR36 ⭐ | Manche → Méditerranée | FR-NOR, FR-SO, FR-MC, FR-34-11, FR-66 |
| GR51 ⭐ | Balcons de la Méditerranée | FR-06, FR-83, FR-13 |
| GR52 ⭐ | Traversée du Mercantour | FR-06 |
| GR54 ⭐ | Tour de l'Oisans et des Écrins | FR-04-05, FR-ALPES-N |
| GR55 | Traversée de la Vanoise | FR-ALPES-N |
| GR56 ⭐ | Tour de l'Ubaye | FR-04-05 |
| GR58 ⭐ | Tour du Queyras | FR-04-05 |
| GR65 ⭐ | Via Podiensis (Le Puy) | FR-MC, FR-SO, FR-PYR-O, FR-30-48 (bordure) |
| GR70 ⭐ | Chemin de Stevenson | FR-30-48, FR-MC |
| GR78 ⭐ | Chemin du Piémont Pyrénéen | FR-PYR-O, FR-34-11, FR-66 |
| GR98 ⭐ | Calanques / littoral provençal | FR-13, FR-83 |
| GR101 ⭐ | Chemin de Lourdes | FR-PYR-O |
| GR145 ⭐ | Via Francigena (France) | FR-EST |
| GR653 ⭐ | Via Tolosana (Arles) | FR-13, FR-34-11, FR-30-48, FR-SO, FR-PYR-O |
| GR654 ⭐ | Voie de Vézelay | FR-SO, FR-MC, FR-EST (nord) |
| GR655 ⭐ | Via Turonensis (Tours) | FR-EST (nord), FR-IDF-CVL, FR-SO, FR-PYR-O |
| TMB ⭐ | Tour du Mont-Blanc | FR-ALPES-N (+ IT/CH hors pilote) |
| GR R1 / R2 / R3 ⭐(R2) | La Réunion (tour du volcan, traversée, Mafate) | FR-974 |

## 2. France — extension pilote (hors app OMW)

| Itinéraire | Nom usuel | Zones-sources |
|------------|-----------|---------------|
| GR1 | Tour de l'Île-de-France | FR-IDF-CVL |
| GR2 | Sentier de la Seine | FR-IDF-CVL, FR-NOR |
| GR3 | Sentier de la Loire | FR-IDF-CVL, FR-MC |
| GR4 | Royan → Grasse (Ventoux, gorges du Verdon) | FR-SO, FR-MC, FR-84-26-07, FR-04-05, FR-06 |
| GR6 | Alpes → Océan (Aubrac, Lot) | FR-04-05, FR-30-48, FR-MC, FR-SO |
| GR7 | Ligne de partage des eaux (Vosges → Andorre) | FR-EST, FR-84-26-07, FR-30-48, FR-34-11 |
| GR8 | Littoral atlantique (Landes) | FR-SO |
| GR9 | Jura → Méditerranée (Vercors, Ventoux, Luberon, Sainte-Baume) | FR-ALPES-N, FR-84-26-07, FR-83, FR-13 |
| GR13 | Fontainebleau → Morvan | FR-IDF-CVL, FR-EST |
| GR14 | Sentier des Ardennes | FR-EST |
| GR22 | Paris → Mont-Saint-Michel | FR-IDF-CVL, FR-NOR |
| GR37 / GR38 / GR39 | Bretagne intérieure & Mont-St-Michel → Guérande | FR-BRE |
| GR42 / GR420 | Balcons du Rhône / Tour des Monts d'Ardèche | FR-84-26-07 |
| GR44 | Cévennes (Chassezac) | FR-30-48 |
| GR49 / GR90 | Verdon → mer / Lubéron | FR-83 |
| GR53 / GR531 / GR532 | Vosges (Club Vosgien) | FR-EST |
| GR59 | Jura / Revermont | FR-EST |
| GR69 | La Routo (transhumance Provence → Alpes) | FR-13, FR-04-05 |
| GR77 | Minervois / Haut-Languedoc | FR-34-11 |
| GR91 | Vercors → Ventoux | FR-ALPES-N, FR-84-26-07 |
| GR120 / GR121 | Côte d'Opale / Artois | FR-EST |
| GR223 | Tour du Cotentin | FR-NOR |
| GR30 | Tour des lacs d'Auvergne | FR-MC |
| GR400 | Tour des volcans du Cantal | FR-MC |
| GR441 | Tour de la Chaîne des Puys | FR-MC |
| GR652 | Rocamadour → Agen (variante Podiensis) | FR-MC, FR-SO |
| GR738 | Haute traversée de Belledonne | FR-ALPES-N |
| GR2013 | Marseille-Provence métropole | FR-13 |
| GTJ | Grande Traversée du Jura | FR-EST, FR-ALPES-N |
| Mare a Mare N/C/S, Mare e Monti | Corse transversales | FR-CORSE |
| GRP majeurs Alpes | Tour du Beaufortain, des Aiguilles Rouges, du Mont Thabor, GTV (Vercors) | FR-ALPES-N, FR-04-05 |

## 3. Espagne / Portugal — chemins de Compostelle (+ GR11)

| Itinéraire | Tronçon | Zones-sources |
|------------|---------|---------------|
| Camino Francés ⭐ | SJPP → Santiago | ES-NAV-RIO-ARA, ES-CYL, ES-GAL |
| Camino Aragonés | Somport → Puente la Reina | ES-NAV-RIO-ARA |
| Camino del Norte ⭐ | Irún → Santiago | ES-NORTE, ES-GAL |
| Camino Primitivo | Oviedo → Santiago | ES-NORTE, ES-GAL |
| Camino Inglés | Ferrol/A Coruña → Santiago | ES-GAL |
| Camino Portugués ⭐ (Central + da Costa) | Porto → Santiago | PT-NORTE, ES-GAL |
| Vía de la Plata / Camino Sanabrés | Sevilla → Santiago (pilote : tronçon CyL + Galicia) | ES-CYL, ES-GAL |
| Camino de Invierno | Ponferrada → Santiago | ES-CYL, ES-GAL |
| Camino del Baztán ⭐ | Bayonne → Pamplona | FR-PYR-O, ES-NAV-RIO-ARA |
| Finisterre – Muxía | Santiago → côte | ES-GAL |
| GR11 (Senda Transpirenaica) | Cap Higuer → Cap de Creus | ES-NAV-RIO-ARA, ES-CAT, ES-NORTE (départ) |

---
*v1 pilote — 2026-07-17. Zones des sentiers ⭐ héritées du référentiel OMW v2 (calé sur GPX) ;
zones des extensions estimées de connaissance générale — affiner au fil des alertes réelles
(pas de géocodage GPX pour l'extension à ce stade).*
