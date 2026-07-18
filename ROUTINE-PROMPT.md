# Prompt de la routine cloud quotidienne (claude.ai/code)

À coller tel quel dans la routine « Veille Sentiers Europe — run quotidien »
(planification : tous les jours à 07h00 Europe/Paris, environnement = ce dépôt, branche main).

---

Tu es à la racine du dépôt veille-sentiers-europe. Exécute le run de veille quotidien
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
6. Commit + push sur main : `git add livrables referentiel site/index.html` puis
   `git commit -m "veille: digest du <date>"` puis `git push`.
   Le push déclenche le déploiement GitHub Pages (workflow pages.yml, qui re-vérifie la QA).
7. Termine par un résumé : alertes nouvelles/changées/levées (avec clés), zones couvertes,
   décompte de recherches.
