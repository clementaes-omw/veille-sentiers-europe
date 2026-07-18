# Prompt de la routine cloud quotidienne (claude.ai/code)

À coller tel quel dans la routine « Veille Sentiers Europe — run quotidien »
(planification : tous les jours à 07h00 Europe/Paris, environnement = ce dépôt, branche main).

---

0. BOOTSTRAP — l'environnement démarre parfois vide : si le dépôt n'est pas déjà présent
   dans le répertoire de travail, clone-le (il est public) :
   `git clone https://github.com/clementaes-omw/veille-sentiers-europe.git && cd veille-sentiers-europe`,
   puis `git config user.name "veille-bot" && git config user.email "veille-bot@users.noreply.github.com"`.
   Tous les chemins ci-dessous sont relatifs à la racine du dépôt.

Tu es l'agent Veille Sentiers Europe. Exécute le run de veille quotidien
défini dans agent-prompt.md, à la lettre :

1. Lis d'abord agent-prompt.md, referentiel/zones-sources.md et livrables/alertes-actives.md.
2. Couvre le périmètre du jour : agrégateurs transversaux + zones T1 de saison + lot T2 du
   jour de la semaine + zones en escalade (alerte HAUTE active). Budget ~35-50 recherches.
3. Applique le protocole de dédoublonnage par clé ; écris livrables/digest_<date>.md
   (uniquement le NOUVEAU/CHANGÉ/LEVÉ) et mets à jour livrables/alertes-actives.md
   (12 colonnes, Portion concernée + Alternative obligatoires, aucune référence OMW).
4. Ajoute la ligne de log dans livrables/_veille-log.md (résumé, zones, nb de recherches).
5. Boucle qualité : `python3 site/build_site.py` — corrige les DONNÉES jusqu'à
   « OK (QA passée) ». Jamais de publication en échec ; bug du générateur → signale-le
   sans le modifier.
6. PUBLICATION (flux PR — le push direct sur main est interdit aux routines cloud) :
   a. `git checkout -b claude/veille-<date>`, commit (`veille: digest du <date>`), push de la branche.
   b. `gh pr create --base main --title "veille: digest du <date>"` puis fusion immédiate
      `gh pr merge --squash --delete-branch`. Fusion impossible → laisser la PR ouverte et
      signaler « PR OUVERTE NON FUSIONNÉE : <url> ».
   c. Push de branche en 403 → signaler « PUSH ÉCHOUÉ — vérifier l'installation de l'app
      GitHub Claude sur le repo ». Ne jamais forcer.
   La fusion sur main déclenche le déploiement GitHub Pages (pages.yml, re-vérifie la QA).
7. Termine par un résumé : alertes nouvelles/changées/levées (avec clés), zones couvertes,
   décompte de recherches, statut de la publication (fusionnée / PR ouverte / échec).
