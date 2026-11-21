# Audit qualité du registre — 2026-11-21

76 alertes actives · 12 fiches avec au moins un constat · **7 bloquant(s)**, 5 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⛔ Bloquants — à corriger avant le prochain run

- **`fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`** — vérifiée il y a 42 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|PO-66-Argeles-Cerbere|sentier-littoral-E12-effondrement|2026-01-19`** — vérifiée il y a 54 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`** — vérifiée il y a 42 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24`** — vérifiée il y a 55 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18`** — vérifiée il y a 55 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** — vérifiée il y a 57 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`réglementation|PN-Pyrénées|baignade-lacs-interdite|2026-06-15`** — vérifiée il y a 68 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## ⚠️ À traiter

- **`fermeture|Cotes-Armor-Lancieux|GR34-digue-La-Roche-travaux|2026-10-29`** — jamais revérifiée depuis sa détection il y a 10 j.
- **`fermeture|ES-AND-Malaga-DesfiladeroGaitanes|senderos-Los-Embalses-Gaitanejo-fermes-risque-desembalse|2026-02-12`** — vérifiée il y a 48 j (seuil 45 j — sévérité info). Le site présente cette restriction comme actuelle.
- **`fermeture|FR-13-Sainte-Victoire|gr9-prieure-croix-de-provence|2026-10-01`** — vérifiée il y a 15 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|PN-Pyrenees-Moundelhs|travaux-forestiers-cirque|2026-07-15`** — vérifiée il y a 54 j (seuil 45 j — sévérité info). Le site présente cette restriction comme actuelle.
- **`reroutage|GR10-Luchon-Superbagnères|nouveau-tracé-pérenne|2024-05-30`** — vérifiée il y a 68 j (seuil 45 j — sévérité info). Le site présente cette restriction comme actuelle.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

