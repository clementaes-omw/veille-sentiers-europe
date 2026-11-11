# Verdict qualité du registre, 2026-11-11

Vérificateur : agents/verificateur-alertes.md (agent distinct de l'agent de veille, qui a écrit les fiches modifiées aujourd'hui). Entrée : livrables/audit-qualite.md du 11/11 (61 bloquants, 25 alertes, 70 fiches citées). Budget web limité à environ 10 lectures : priorité donnée aux alertes rouges et aux restrictions « au jour le jour » que le site affiche comme actuelles. Aucune fiche créée, supprimée ni clôturée ; aucun script, digest ni journal de veille modifié ; rien commité.

## À traiter au prochain run (agent de veille)

Constats bloquants restants : 57, tous de FRAÎCHEUR (dernière vérification entre le 28/09 et le 07/10 pour des seuils de 2 à 12 jours). Ils exigent une source nouvelle, hors du périmètre du vérificateur. Par ordre de priorité :

1. `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` : établir si la gorge a rouvert après l'alerte du 01-04/10 ou si elle est fermée pour l'hiver (samaria-tickets.necca.gov.gr), puis clôturer ou réécrire. Une recherche le 11/11 n'a rien donné de daté.
2. `risque-feu|Var-83|fermetures-massifs-quotidiennes|2026-07-08` : la source déjà citée (varactu.fr, 29/09) annonce la carte du 30/09 comme la dernière de la saison. Vérifier qu'aucune carte n'a été republiée, puis CLÔTURER.
3. `risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28` : toutes les échéances (01/09, 30/09) sont passées. CLÔTURER après vérification d'une absence de prolongation sur vosges.gouv.fr.
4. Alertes rouges (contrôle 7, sources datées de plus de 60 jours) : Bordes-Uchentein (AP du 31/08), Justin (AP du 21/08), Bois Noir (AM du 15/08), Etsaut (presse du 10/09). Retrouver un acte ou une publication récente ; à défaut, la veille doit statuer sur une dégradation en MOYENNE (recommandation, non appliquée : ces alertes reposent sur un acte daté, la règle des 14 jours ne s'applique pas).
5. Bois Noir en particulier : la page « Infos feu du Bois noir » de ville-argentiere.fr (200) ne reproduit plus le texte de l'arrêté du 15/08 ; seuls des points de situation à la population sont téléchargeables. Retrouver une URL consultable de l'arrêté, sinon dégrader en MOYENNE en le disant au lecteur.
6. Feux MOYENNE éteints ou maîtrisés depuis six semaines, sans fermeture de sentier documentée : Ardèche-Dompnac, Ariège-Mijanes-Donezan, ES-AND-Igualeja-Parauta, PT Arganil-Piodão, PT Odemira-Saboia (validités échues). Recommandation : CLÔTURE après une vérification d'extinction. Ariège-Saurat (feu couvant au 01/10) : revérifier.
7. Les 47 autres fiches à fraîcheur échue listées dans livrables/audit-qualite.md (Écrins, Dolomites, Pyrénées-Orientales, Aude, Corse, Espagne, Portugal, Slovénie, Tatras, etc.) : revérification standard.
8. Faux positifs probables de l'audit (validité « passée ») : `fermeture|DE-Sachsen-SaechsischeSchweiz|...` (la date du 07/11 est celle d'une levée partielle déjà intégrée) et `reglementation|ES-NAV-RIO-ARA-Roncesvalles|...` (régime du 01/11 au 31/03). Pas d'action sur le fond.

## Résultat par contrôle

| Contrôle | Résultat |
| --- | --- |
| 1. Fraîcheur | FAIL sur 57 fiches (voir ci-dessus). PASS pour les 5 alertes rouges (revérifiées par la veille le 11/11). |
| 2. Concordance interne | 4 FAIL bloquants (Bordes-Uchentein, Justin, Bois Noir, Etsaut) et 1 alerte (Réunion) : « Portion concernée » datée du 06/10 ou du 31/10 alors que la veille avait revérifié le 11/11. Corrigés. 1 FAIL interne invisible corrigé (Bois Noir, `statut:` citait un arrêté du « 12/08 » au lieu du 15/08). Plus aucun écart portion/suivi signalé par l'audit. |
| 3. Honnêteté | 3 fiches au contenu échu (Samaria, Var, Vosges) présentaient au présent un état de septembre ou d'octobre : constat posé en clair (dernière information vérifiée, échéance passée). Bois Noir : la portion affirmait que la page de la mairie présente l'arrêté, ce qui n'est plus le cas au 11/11 : corrigé. |
| 4. Pertinence | FAIL (recommandation de clôture) : Var-83, Vosges-88, et les cinq feux MOYENNE du point 6. Non appliqué. |
| 5. Sévérité juste | PASS sur la règle : les 5 rouges reposent sur un acte daté. Recommandation de réexamen pour Bois Noir (acte non consultable en ligne). |
| 6. Ton | PASS sur les fiches touchées : aucun jargon de veille, aucun tiret cadratin ni demi-cadratin ajouté dans les sections publiques. |
| 7. Source vivante (rouges) | PASS pour Justin (mairie-die.fr, texte de l'arrêté du 21/08 lisible), Bordes-Uchentein (PDF de l'AP du 31/08), Etsaut (lasemainedespyrenees.fr, 10/09), Réunion (page ONF). FAIL partiel pour Bois Noir (page vivante, arrêté absent). |

## Corrections appliquées

Réécritures à information constante (aucun fait nouveau hors des lectures ci-dessous), ancien état versé dans la chronologie de « Zone (détails) » :

- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` : portion remise au 11/11 ; entrées 06/10 et 11/11 ajoutées à la chronologie (l'entrée du 06/10 reprend l'ancien `statut:`, effacé par la veille sans report).
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` : idem (portion au 11/11, entrées 06/10 et 11/11).
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` : portion au 11/11 et corrigée sur la page de la mairie ; `statut:` 12/08 corrigé en 15/08 ; entrée 11/11.
- `incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02` : portion au 11/11 (« soixante-dix jours après le départ de feu ») ; entrées 06/10 et 11/11.
- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` : portion au 11/11 ; entrée 11/11.
- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` : portion au passé avec constat en clair, validité complétée (échéance du 04/10 passée) ; ancienne portion versée dans la chronologie.
- `risque-feu|Var-83|fermetures-massifs-quotidiennes|2026-07-08` : portion reformulée (dispositif quotidien terminé le 30/09) ; ancienne portion versée dans la chronologie. L'« Alternative » parle encore au présent des massifs orange : à reprendre à la clôture.
- `risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28` : portion reformulée (échéances passées), validité complétée ; ancienne portion versée dans la chronologie.

Lectures web : 8 (1 recherche, 7 lectures de sources). `python3 site/build_site.py` : OK (QA passée). `python3 site/verif_faits.py` : sur les fiches touchées, seuls la date du 11/11 (« 11 » inventé) et le mot « cet » (perdu) sont signalés, sans perte de fait.
