# Audit qualité du registre — 2026-11-14

72 alertes actives · 22 fiches avec au moins un constat · **16 bloquant(s)**, 7 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⛔ Bloquants — à corriger avant le prochain run

- **`crue|Écrins-GR54|sentiers-refuges-endommages-crues-27-28-aout|2026-08-27`** — vérifiée il y a 50 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`eboulement|IT-Dolomites-BorcaDiCadore|frana-passo-staulanza-route-rifugio-citta-di-fiume|2026-09-10`** — vérifiée il y a 35 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`** — vérifiée il y a 35 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10`** — vérifiée il y a 35 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|PO-66-Argeles-Cerbere|sentier-littoral-E12-effondrement|2026-01-19`** — vérifiée il y a 47 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`** — vérifiée il y a 35 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24`** — vérifiée il y a 48 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|Aspe-64-Chemin-Mature|eboulement-devie-col-Arras|2026-01-05`** — vérifiée il y a 61 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25`** — vérifiée il y a 50 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18`** — vérifiée il y a 48 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** — vérifiée il y a 50 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|HauteGaronne-31|vigilance-rouge-camping-sauvage-interdit|2026-07-09`** — vérifiée il y a 47 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|HautesPyrenees-65|interdiction-feu-massifs-forestiers|2026-07-27`** — vérifiée il y a 47 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`réglementation|PN-Pyrénées|baignade-lacs-interdite|2026-06-15`** — vérifiée il y a 61 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`réglementation|Écrins|bivouac|2026-06-19`** — vérifiée il y a 52 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`sentiers|Mercantour|etat-sentiers-2026|2026-05-15`** — vérifiée il y a 47 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## ⚠️ À traiter

- **`eboulement|IT-Dolomites-Cortina|frana-tofana-di-dentro-sentier-401-val-travenanzes|2026-10-04`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|PN-Pyrenees-Moundelhs|travaux-forestiers-cirque|2026-07-15`** — vérifiée il y a 47 j (seuil 45 j — sévérité info). Le site présente cette restriction comme actuelle.
- **`infrastructure|SCAND-SE-Norrbotten-Padjelantaleden|pont-Mielladno-retire|2026-04`** — vérifiée il y a 52 j (seuil 45 j — sévérité info). Le site présente cette restriction comme actuelle.
- **`infrastructure|SCAND-SE-Norrbotten-Padjelantaleden|pont-Mielladno-retire|2026-04`** — jamais revérifiée depuis sa détection il y a 52 j.
- **`reroutage|GR10-Luchon-Superbagnères|nouveau-tracé-pérenne|2024-05-30`** — vérifiée il y a 61 j (seuil 45 j — sévérité info). Le site présente cette restriction comme actuelle.
- **`reroutage|Pierrefiques-76|déviation|2025-05-18`** — la validité annoncée s'arrête au 18/09/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`réouverture|Boréon-Mercantour|post-Alex|2026`** — vérifiée il y a 47 j (seuil 45 j — sévérité info). Le site présente cette restriction comme actuelle.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

