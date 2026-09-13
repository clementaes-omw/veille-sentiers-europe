# Audit qualité du registre — 2026-09-13

88 alertes actives · 7 fiches avec au moins un constat · **0 bloquant(s)**, 7 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — vérifiée il y a 14 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`** — alerte rouge appuyée sur une source datée du 26/08 (18 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — alerte rouge appuyée sur une source datée du 01/09 (12 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04`** — jamais revérifiée depuis sa détection il y a 8 j.
- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 31/08 (13 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (23 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — alerte rouge appuyée sur une source datée du 24/08 (20 j) — retrouver une publication récente ou dégrader la sévérité.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

