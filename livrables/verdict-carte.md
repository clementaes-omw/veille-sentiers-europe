# Verdict carte — 2026-11-02

Agent : Vérificateur Carte. Périmètre : mapping zone d'alerte → marqueur (`zones-coords.csv` + `ALIAS_ZONE`). Aucun jugement de fond sur les alertes.

## Verdict global : CONFORME, 1 centroïde DOUTEUX signalé (Roncesvalles)

- Audit déterministe relancé le 2026-11-02 : 0 alerte perdue, 0 `⚠ carte`.
- `python3 site/build_site.py` : « OK (QA passée) », 106 alertes actives, 44 clôturées.
- Fichiers modifiés : aucun (`zones-coords.csv` inchangé : aucune zone perdue, donc aucun ajout autorisé).

## Compte de marqueurs
- Attendu (zones-sources uniques résolues parmi les 106 actives) : **44**.
- Affiché (`site/index.html`, « 44 zones en alerte active ») : **44**. Concordant.

## Action à porter (recommandation, non appliquée)

**ES-NAV-RIO-ARA — alerte `reglementation|ES-NAV-RIO-ARA-Roncesvalles|fermeture-hivernale-Lepoeder-Ruta-Napoleon|2026-11-01` (fiche du jour).**
- Résolution : préfixe de code → `ES-NAV-RIO-ARA` (42.55 ; -0.70). Marqueur présent, pas de perte.
- Plausibilité : **douteuse**. Roncesvalles / col de Lepoeder ≈ 43.02 N ; -1.32 O. Le centroïde est à **≈ 73 km** (sud-est), au niveau de la Jaca / Huesca pyrénéenne (repère : Riglos ≈ 42.34 ; -0.72). Il tombe dans la zone déclarée mais pas près du Camino Francés navarrais. Il porte déjà l'alerte `ES-ARA-Huesca-Riglos` : le randonneur lit la fermeture de la Route Napoléon sur un marqueur placé en Aragon.
- Correction proposée (à valider, non faite : la zone n'est pas « perdue », et on ne déplace pas une entrée existante) : ajouter à `zones-coords.csv`, bloc Espagne, la ligne
  `ES-NAV-RIO-ARA-Roncesvalles;Roncesvalles & Lepoeder (Camino Francés, Navarre);43.01;-1.32`
  (repère : Roncesvalles / Orreaga). Un code identique à la zone d'alerte se résout par correspondance exacte, plus long que le préfixe `ES-NAV-RIO-ARA`, donc sans toucher à `build_site.py`. Effet : 45 marqueurs au lieu de 44, Riglos reste sur le centroïde.

## Verdicts par zone active (44 zones contrôlées)

Plausible = les alertes de la zone tombent dans la région du centroïde (écart modéré, cohérent avec « centre indicatif de zone »).

| Zone | Verdict |
|---|---|
| AT, CH-EST*, CH-VALAIS-VAUD, CH-Valais-Arolla, CH-Valais-Randa, VS-Orsieres-ValFerret | Plausible. *CH-EST (46.60 ; 8.90) : Frutigen / Kandersteg sont en Oberland bernois (≈ 46.5 ; 7.7), ≈ 90 km à l'ouest : limite, à revoir si une entrée dédiée devient utile. |
| Cotes-Armor-Trebeurden, FR-BRE* | Plausible. *FR-BRE : Piriac (Loire-Atlantique, ≈ 47.4 ; -2.5) à ≈ 100 km du centroïde : limite. |
| DE-SACHSEN, DE-SW, PL-SK-TATRAS, SI-HR, SCAND-SE, IS, GR-E4, UK-SCOTLAND, UK-Devon, UK-Cornwall | Plausible. |
| ES-AND, ES-CANARIAS, ES-CENTRO, ES-GAL | Plausible. |
| ES-NAV-RIO-ARA | Doubtful pour Roncesvalles (voir ci-dessus) ; plausible pour Riglos. |
| FR-04-05, FR-06, FR-13, FR-83, FR-CORSE, FR-974, FR-30-48, FR-66 | Plausible. |
| FR-34-11, FR-84-26-07, FR-PYR-O, FR-ALPES-N, FR-EST, FR-IDF-CVL, FR-NOR, FR-SO | Plausible (FR-84-26-07 : Dompnac / Les Vans en Ardèche méridionale ≈ 80 km du centroïde, acceptable ; FR-PYR-O couvre 12 alertes sur une zone étendue, un seul marqueur). |
| IT-NO, IT-DOLOMITES, IT-Liguria-CinqueTerre | Plausible. |
| IT-CENTRE | Limite : Carrara (≈ 44.1 ; 10.1) à ≈ 100 km du centroïde, mais dans la zone nommée. |
| PT-CENTRO-SUL | Plausible. |

## Recommandations laissées
1. Ajouter la ligne `ES-NAV-RIO-ARA-Roncesvalles` (ci-dessus), à valider par le responsable du référentiel.
2. Centroïdes « limite » (CH-EST, FR-BRE, IT-CENTRE) : pas d'action requise aujourd'hui, à reconsidérer si une entrée plus fine est ajoutée.
3. Alias `build_site.py` : aucun besoin.

## Bug du générateur
Aucun constaté sur la résolution de zones. Le build affiche seulement les avertissements de fraîcheur de l'audit (hors périmètre carte : validités passées, alertes rouges sur source ancienne).

## Point d'indépendance
Je n'ai écrit aucune des alertes contrôlées.

VERIFICATEUR CARTE COMPLETE
