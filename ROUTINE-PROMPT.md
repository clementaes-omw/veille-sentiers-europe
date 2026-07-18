# Prompt de la routine cloud quotidienne (claude.ai/code)

À coller tel quel dans la routine « Veille Sentiers Europe — run quotidien »
(planification : tous les jours à 07h00 Europe/Paris, environnement = ce dépôt, branche main).

---

0. BOOTSTRAP — si le dépôt n'est pas déjà présent dans le répertoire de travail, clone-le
   (il est public) : `git clone https://github.com/clementaes-omw/veille-sentiers-europe.git
   && cd veille-sentiers-europe`. Tous les chemins ci-dessous sont relatifs à la racine.
   (Le clone en lecture peut se faire en git ; la PUBLICATION, elle, passe par les outils
   GitHub MCP — étape 6.)

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
6. PUBLICATION — via les outils GitHub MCP de la session (l'intégration officielle scopée
   sur ce dépôt ; méthode validée le 18/07 par la PR #1). Pas de git push, aucun jeton :
   a. Crée la branche `claude/veille-<date>` depuis main (outil MCP create branch).
   b. Committe sur cette branche TOUS les fichiers modifiés du run (livrables/digest_<date>.md,
      livrables/alertes-actives.md, livrables/_veille-log.md, site/index.html, et
      referentiel/* si modifié) — commit « veille: digest du <date> » (outil MCP push files /
      create or update file).
   c. Ouvre la PR vers main (« veille: digest du <date> », body = résumé en 2 lignes) puis
      fusionne-la en squash (outils MCP create/merge pull request).
   d. Fusion impossible → laisser la PR ouverte et signaler « PR OUVERTE : <url> » ;
      échec de publication → terminer par « PUBLICATION ÉCHOUÉE » + erreurs verbatim +
      résumé du digest. Ne jamais forcer.
   La fusion sur main déclenche le déploiement GitHub Pages (pages.yml, re-vérifie la QA).
7. Termine par un résumé : alertes nouvelles/changées/levées (avec clés), zones couvertes,
   décompte de recherches, statut de la publication (fusionnée / PR ouverte / échec).
