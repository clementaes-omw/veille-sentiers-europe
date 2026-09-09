# Audit qualité du registre — 2026-09-09

88 alertes actives · 9 fiches avec au moins un constat · **0 bloquant(s)**, 9 alerte(s), 0 info(s).

Carte : **0 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`conditions|Ecrins-GR54|crue-degats-vallouise-oisans-valgaudemar|2026-08-27`** — la validité annoncée s'arrête au 28/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`** — alerte rouge appuyée sur une source datée du 26/08 (14 j) — retrouver une publication récente ou dégrader la sévérité.
- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — « Portion concernée » parle du 01/09 alors que le suivi connaît la situation au 09/09 (8 j d'écart) — la mise à jour n'est pas arrivée jusqu'au texte affiché.
- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — vérifiée il y a 5 j (seuil 2 j — restriction décidée au jour le jour). Le site présente cette restriction comme actuelle.
- **`incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`** — vérifiée il y a 17 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — alerte rouge appuyée sur une source datée du 21/08 (19 j) — retrouver une publication récente ou dégrader la sévérité.
- **`incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`** — vérifiée il y a 18 j (seuil 12 j — sévérité moyenne). Le site présente cette restriction comme actuelle.
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — alerte rouge appuyée sur une source datée du 24/08 (16 j) — retrouver une publication récente ou dégrader la sévérité.
- **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`** — alerte rouge appuyée sur une source datée du 28/08 (12 j) — retrouver une publication récente ou dégrader la sévérité.

## 🗺 Cohérence carte / registre

0 alerte perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs couvre toutes les actives, et toute zone-source du référentiel a ses coordonnées.

