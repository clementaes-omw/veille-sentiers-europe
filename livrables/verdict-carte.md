# Verdict carte · 2026-11-17

Agent : Vérificateur Carte (passage hors lundi, déclenché par l'ajout de `CH-Valais-Gondo` au CSV). Périmètre : zone d'alerte → marqueur. Je ne juge pas le fond des alertes.

## Verdict global : CONFORME côté référentiel, 38 marqueurs attendus ; `site/index.html` en affiche 37 car il date d'avant l'ajout Gondo : rebuild à faire

- Audit déterministe (`python3 site/audit_qualite.py`, sans `--ecrire`) relancé le 2026-11-17 : **0 alerte perdue**, 0 constat carte. Les 14 constats (10 bloquants) viennent du registre, hors périmètre carte.
- Registre au moment du contrôle : 156 fiches, 75 actives (l'agent de veille peut encore le faire bouger).
- Résolution recalculée en mémoire (`load_alertes`, `zones_carte`), sans rien écrire. `build_site.py` non lancé (consigne). Recherches web : 0.
- Fichier modifié : ce verdict seulement. La ligne `CH-Valais-Gondo` du CSV est juste, je ne l'ai pas touchée.

## 1. Zones perdues

Aucune : les 75 actives se résolvent toutes. La ligne `CH-Valais-Gondo` (ajoutée aujourd'hui par un autre agent) raccroche bien `fermeture|CH-Valais-Gondo|stockalperweg-fort-gondo-fermeture-hivernale|2026-11-09`, qui sans elle n'aurait aucun marqueur (pas d'alias, et `CH-VALAIS-VAUD` ne préfixe pas `CH-Valais-Gondo`).

## 2. Compte de marqueurs

- Attendu : **38** zones uniques résolues, 0 non mappée. Par rapport au 16/11 (38) : IS sort (deux fiches Fimmvörðuháls clôturées, plus d'alerte active en Islande), CH-Valais-Gondo entre.
- Affiché : `site/index.html` (06:14 UTC) annonce « **37** zones en alerte active ». Il a été généré une minute avant l'ajout de la ligne au CSV (06:15) : la fiche Gondo y est dans la liste mais **sans marqueur**. Écart attendu, résorbé par le prochain build ; à vérifier (voir action n° 1).

## 3. Plausibilité des centroïdes

| Zone | Verdict |
|---|---|
| **CH-Valais-Gondo** (46.20 ; 8.14), nouveau | **Plausible.** Repère : village de Gondo (≈ 46.196 ; 8.139), à moins de 1 km ; Fort Gondo / Alte Kaserne dans la gorge ≈ 3 km à l'ouest. Bien sur le versant sud du Simplon, en Valais, à la frontière italienne. |
| FR-ALPES-N (45.50 ; 6.50) | Plausible mais éloigné pour la nouvelle alerte : Dent de Crolles (Chartreuse, Isère, ≈ 45.31 ; 5.86) à ≈ 55 km d'un marqueur placé en Tarentaise / Vanoise. Dans la zone nommée (38/73/74/01). Pralognan ≈ 20 km. |
| ES-CANARIAS (28.35 ; -16.20) | Plausible à l'échelle de l'archipel, inchangé : Teide ≈ 44 km, point en mer à l'est de Tenerife. Porte désormais 2 alertes, toutes deux `ES-CANARIAS-Tenerife`. Voir action n° 2. |
| IS | Sans objet : plus d'alerte active, marqueur retiré. |
| FR-BRE, IT-CENTRE (Latium) | **DOUTEUX**, constats du 16/11 inchangés (8 alertes littorales à 49-103 km ; Formello / La Storta à ≈ 175 km). |
| Les 33 autres zones | Constats du 16/11 reconduits sans recalcul (mêmes zones, mêmes coordonnées) : plausibles, dont limites ES-CENTRO, ES-AND, CH-EST, AT, IT-NO, SCAND-SE. |

## Actions à porter (non appliquées)

1. **Rebuild du site** une fois `livrables/alertes/` stabilisé : `python3 site/build_site.py` doit rendre « OK (QA passée) », sans `⚠ carte`, et afficher **38** zones (si le registre ne bouge plus).
2. **Tenerife (renforcé).** Le cas prévu le 16/11 se réalise (2 alertes Teide). Ligne proposée, bloc « ESPAGNE extension » : `ES-CANARIAS-Tenerife;Tenerife (Teide, Corona Forestal);28.27;-16.64` (repère : pic du Teide). Aucun alias à toucher, le préfixe le plus long l'emporte ; compte inchangé (38). Non ajoutée : zone non perdue, hors de mon périmètre du jour.
3. **Chartreuse (nouveau, facultatif).** Si les alertes Isère se répètent : `FR-ALPES-N-Chartreuse;Chartreuse (Dent de Crolles, Isère);45.31;5.86`. Effet : 39 marqueurs.
4. Reconduites du 16/11, inchangées : alias Latium (`VF-Lazio-Prato-La-Corte` → `IT-CENTRE-Lazio` 42.07 ; 12.40), alias Côte d'Émeraude (Saint-Briac, Dinard → `Cotes-Armor-Lancieux`), alias Valais (`CH-Europaweg-Randa-Zermatt` → `CH-Valais-Randa`, `TMB-CH-Orsieres` → `VS-Orsieres-ValFerret`), centroïde FR-BRE.

## Point d'indépendance

Je n'ai écrit aucune des alertes contrôlées, ni la ligne `CH-Valais-Gondo` du CSV.
