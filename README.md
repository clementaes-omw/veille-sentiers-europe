# Veille Sentiers Europe

**Site public : https://www.alertes-rando.info** (GitHub Pages, domaine vérifié).
Dépôt canonique du projet depuis le 2026-07-17. Le site est reconstruit et déployé à chaque
fusion sur main (`.github/workflows/pages.yml`, boucle QA en garde-fou : un build non
conforme ne se déploie pas). La veille quotidienne tourne en **routine cloud claude.ai**
(7h Europe/Paris) qui publie par PR via les outils GitHub MCP — voir `ROUTINE-PROMPT.md`.
Tous les chemins d'`agent-prompt.md` sont relatifs à la racine du dépôt.

Site de veille terrain **indépendant de l'app OMW** : état des grands sentiers (incendies,
fermetures, reroutages, réglementation). Périmètre v2 (depuis le 17/07/2026) : **Europe de
l'Ouest** — France + Réunion, péninsule Ibérique complète, arc alpin (CH/IT/AT), Allemagne,
Benelux, îles Britanniques, Scandinavie, Islande. 32 zones-sources, cadence étagée.

Créé le 2026-07-17. Même mécanique que la veille OMW (`../veille-critique` + agent 07),
avec deux différences structurantes :
1. **L'unité de veille est la zone-source**, pas le sentier (un arrêté du Var couvre d'un
   coup GR51/GR98/GR9/GR49…) — voir `referentiel/zones-sources.md`.
2. **Cadence étagée** pour contenir le coût : T1 quotidien en saison (zones à risque),
   T2 hebdo en rotation (6 lots), T3 mensuel, escalade → quotidien si alerte HAUTE.

## Structure

- `referentiel/zones-sources.md` — périmètre, cadences, sources par zone, contournements
  éprouvés (hérités de l'été 2026 OMW) ; sources ES vérifiées le 17/07/2026.
- `referentiel/sentiers-db.csv` — **base de données sentiers complète** (582 itinéraires :
  192 GR, 331 GRP, 37 GRT transfrontaliers, 18 caminos, hautes routes ; priorités P1/P2/P3).
  Construite le 2026-07-17 depuis les listes FFRandonnée/Wikipédia + couches curées ;
  script rejouable : `referentiel/outils/build_db.py` (+ dumps wikitext sources).
- `referentiel/sentiers.md` — vue lisible des itinéraires prioritaires (P1).
- `agent-prompt.md` — prompt du run de veille (dédoublonnage par clé, digest, registre).
- `livrables/alertes-actives.md` — registre persistant. **Amorcé par import du registre OMW**
  (mêmes alertes France). Schéma de colonnes = celui du site, ne pas changer.
- `livrables/digest_AAAA-MM-JJ.md` — un digest par run (aucun encore : produit par les runs).
- `site/build_site.py` — génère `site/index.html` (autonome, publié en Artifact Claude).

## Lancer un run de veille

Coller le contenu d'`agent-prompt.md` dans une session Claude Code (ou en faire une tâche
planifiée quand le coût/run sera validé). Le run lit le registre + le référentiel, couvre
T1 + lot T2 du jour + escalades, écrit digest + registre + log, puis reconstruit le site :

    python3 "…/veille-europe/site/build_site.py"

Déploiement : automatique via GitHub Pages à chaque fusion sur main.

## Métriques du pilote (à surveiller sur les 5 premiers runs)

- Nombre de recherches/lectures par run (l'agent le logge dans `_veille-log.md`) —
  cible ≈ 25-35 en haute saison.
- Alertes manquées vs presse (contrôle ponctuel) ; faux positifs.
- Lisibilité réelle des sources ES marquées [à confirmer au 1er run].

## Décisions en attente (Clément & Audrey)

- Nom définitif du site (placeholder actuel : « Veille Sentiers Europe »).
- Planification du run quotidien (après mesure du coût réel sur 2-3 runs manuels).
- Extension du périmètre v2 (Suisse/Italie pour TMB & Francigena en premier ?).
