# Audit qualité du registre — 2026-08-15

70 alertes actives · 7 fiches avec au moins un constat · **0 bloquant(s)**, 6 alerte(s), 1 info(s).

Carte : **5 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10`** — la validité annoncée s'arrête au 10/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — la validité annoncée s'arrête au 12/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10`** — la validité annoncée s'arrête au 04/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.
- **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** — alerte rouge appuyée sur une source datée du 29/07 (17 j) — retrouver une publication récente ou dégrader la sévérité.
- **`risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01`** — « Portion concernée » parle du 07/08 alors que le suivi connaît la situation au 15/08 (8 j d'écart) — la mise à jour n'est pas arrivée jusqu'au texte affiché.
- **`risque-feu|Hérault-34|fermetures-massifs-quotidiennes|2026-07-02`** — « Portion concernée » parle du 07/08 alors que le suivi connaît la situation au 15/08 (8 j d'écart) — la mise à jour n'est pas arrivée jusqu'au texte affiché.

## · Dette de forme

- **`incendie|ES-CYL-Fermoselle-Sayago|feu-record-11000ha-800evacues|2026-07-29`** — « Zone (détails) » contient encore du jargon de veille (recherche ciblee) au lieu de l'état du terrain.

## 🗺 Cohérence carte / registre

### ⛔ Alertes actives invisibles sur la carte / compte incohérent

- **`(carte)`** — regroupement incohérent : 66 alerte(s) réparties sur 35 marqueur(s) pour 70 active(s) — 4 alerte(s) hors carte.
- **`incendie|Aude-Conques-sur-Orbiel|feu-fixe-50ha|2026-08-13`** — zone « Aude-Conques-sur-Orbiel » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`incendie|Drome-Bellegarde-en-Diois|feu-massif-Claps-400ha|2026-08-03`** — zone « Drome-Bellegarde-en-Diois » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`incendie|Herault-34-Pegairolles-Escalette|feu-A75-200ha|2026-08-14`** — zone « Herault-34-Pegairolles-Escalette » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.
- **`incendie|Var-Ginasservis|feu-30ha-RD30-coupee|2026-08-14`** — zone « Var-Ginasservis » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.

