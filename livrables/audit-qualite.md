# Audit qualité du registre — 2026-11-22

75 alertes actives · 8 fiches avec au moins un constat · **6 bloquant(s)**, 2 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⛔ Bloquants — à corriger avant le prochain run

- **`fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`** — vérifiée il y a 43 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|PO-66-Argeles-Cerbere|sentier-littoral-E12-effondrement|2026-01-19`** — vérifiée il y a 55 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|IT-NO-Biellese|Monte-Barone-Valsessera-sentieri-chiusi-post-incendio|2026-08-03`** — vérifiée il y a 43 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24`** — vérifiée il y a 56 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18`** — vérifiée il y a 56 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** — vérifiée il y a 58 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## ⚠️ À traiter

- **`fermeture|Cotes-Armor-Lancieux|GR34-digue-La-Roche-travaux|2026-10-29`** — jamais revérifiée depuis sa détection il y a 11 j.
- **`reglementation|ES-NAV-RIO-ARA-Roncesvalles|fermeture-hivernale-Lepoeder-Ruta-Napoleon|2026-11-01`** — vérifiée il y a 13 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

