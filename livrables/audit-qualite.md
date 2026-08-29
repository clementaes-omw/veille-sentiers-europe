# Audit qualité du registre — 2026-08-29

76 alertes actives · 4 fiches avec au moins un constat · **0 bloquant(s)**, 4 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — vérifiée il y a 23 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06`** — jamais revuérifiée depuis sa détection il y a 10 j.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 18/08 (11 j) — retrouver une publication récente ou dégrader la sévérité.
- **`refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`** — vérifiée il y a 22 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.
