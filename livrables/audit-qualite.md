# Audit qualité du registre — 2026-08-30

76 alertes actives · 3 fiches avec au moins un constat · **0 bloquant(s)**, 2 alerte(s), 1 info(s).

Carte : **2 bloquant(s)**, 0 alerte(s) (cohérence carte/registre, voir la section dédiée).

Généré par `site/audit_qualite.py` (déterministe, hors ligne). Le jugement sur le fond — la source dit-elle vraiment cela, l'alerte a-t-elle encore un sens sur le terrain — relève de `agents/verificateur-alertes.md` ; la plausibilité des centroïdes de la carte, de `agents/verificateur-carte.md`.

## ⚠️ À traiter

- **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — alerte rouge appuyée sur une source datée du 18/08 (12 j) — retrouver une publication récente ou dégrader la sévérité.
- **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`** — la validité annoncée s'arrête au 27/08/2026, désormais passé : clôturer l'alerte, ou réécrire la validité si elle est prolongée.

## · Dette de forme

- **`risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01`** — « Zone (détails) » contient encore du jargon de veille (recherche ciblee) au lieu de l'état du terrain.

## 🗺 Cohérence carte / registre

### ⛔ Alertes actives invisibles sur la carte / compte incohérent

- **`(carte)`** — regroupement incohérent : 75 alerte(s) réparties sur 35 marqueur(s) pour 76 active(s) — 1 alerte(s) hors carte.
- **`incendie|Cap-Corse-Cagnano|feu-RD132-fermee|2026-08-29`** — zone « Cap-Corse-Cagnano » non résolue vers referentiel/zones-coords.csv : l'alerte est publiée mais n'apparaît sur AUCUN marqueur de la carte. Ajouter le code de zone au CSV, ou une entrée dans la table ALIAS_ZONE de build_site.py.

