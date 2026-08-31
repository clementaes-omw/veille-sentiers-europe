# Verdict qualité du registre — 2026-08-31

Agent Vérificateur Qualité, distinct de l'agent de veille dont le run du jour a mis à
jour `livrables/alertes/`. Aucune des 7 fiches contrôlées ci-dessous n'a été rédigée
par moi, y compris les 4 dont le `statut:`/`verif:` ont été rafraîchis aujourd'hui
même (Ariège-Bordes-Uchentein, Corse-Calenzana, PO-66, Vaucluse-84) : je les contrôle,
je ne relis pas mon propre travail.

Périmètre : les 7 constats de `livrables/audit-qualite.md`, généré le jour même par
`python3 site/audit_qualite.py --ecrire` avant mon passage — 0 bloquant, 6 alertes,
1 dette de forme, sur 5 fiches distinctes (2 fiches en portaient 2 chacune) parmi les
7 clés listées ci-dessous. Aucune autre fiche du registre (102 fichiers, 75 actives)
n'a été ouverte ni touchée.

## Corrections appliquées (périmètre : information constante, source déjà citée)

1. **`incendie|Corse-Calenzana|feu-Montegrosso-64ha|2026-08-27`** — `validite:`
   citait comme dernière date « 28/08 », lue par l'audit comme une échéance dépassée
   (contrôle 3, FAIL). Réécrite d'après les faits déjà sourcés (feu fixé nuit du
   27-28/08, « sous contrôle » depuis le 28/08 après-midi, aucune restriction de
   sentier jamais confirmée) avec la formule « situation suivie jusqu'à nouvel ordre »
   pour ne plus lire comme une échéance figée. Contrôle 3 → PASS.
2. **`risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`**
   — même défaut : `validite:` citait la date de la dernière *vérification*
   (« nouvelle recherche dédiée le 28/08 ») que l'audit prenait pour une échéance.
   Réécrite : la restriction Gran Canaria est « en vigueur jusqu'à levée officielle »,
   la date de vérification déplacée hors du champ validité. Contrôle 3 → PASS.
3. **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`** — même
   défaut (échéance lue au 27/08). Réécrite avec « en vigueur jusqu'à levée
   officielle ». Profité de la correction pour recomposer le champ en UNE seule
   ligne physique : le `validite:` d'origine tenait sur 3 lignes indentées, or
   `parse_alerte()` (site/build_site.py) ne lit que la première ligne d'un champ de
   front-matter — les deux lignes de continuation (« des 9 massifs… », « massifs…non
   tranché ») n'étaient jamais chargées par le parseur. Voir « Défaut d'outillage »
   ci-dessous. Contrôle 3 → PASS.
4. **`risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01`** — « Zone (détails) »
   contenait le jargon de veille « recherche ciblée » (contrôle 6/TON, INFO).
   Reformulé en « nouveau contrôle direct du site de la préfecture », dates et
   décompte (30/08, 18/08, 12 jours de silence officiel) conservés à l'identique.
   Contrôle 6 → PASS.

Après ces 4 corrections : `python3 site/build_site.py` rend **OK (QA passée)**
(75 actives, 27 clôturées, registre 619 413 car.) ; `python3 site/audit_qualite.py
--ecrire` ne signale plus aucun constat sur ces 4 fiches (0 bloquant avant et après).
`python3 site/verif_faits.py HEAD` confirme qu'aucun fait n'a été perdu ni inventé
sur les 4 fiches touchées.

## Signalé, non corrigé — nécessite une source nouvelle (prochain passage de veille)

1. **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — FRAÎCHEUR
   (contrôle 1) FAIL : vérifiée il y a 3 j, seuil 2 j pour une restriction « décidée au
   jour le jour ». Concordance interne par ailleurs bonne (Portion/statut/Zone
   racontent la même chose). **Action attendue** : revérifier samaria.gr et le site
   de la Région de Crète le jour de la prochaine étape couverte ; ce n'est pas une
   réécriture à information constante, c'est un fait à établir.
2. **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** —
   SOURCE VIVANTE (contrôle 7) : la source la plus récente citée date du 18/08
   (13 j). J'ai vérifié en direct que ce n'est **pas** une alerte rouge adossée à
   « à confirmer »/« probable » : la fermeture du GR®10 (Ayès↔Cap des Lauses) est
   établie par 3 sources indépendantes datées (France 3 04/08, ruralites2024.fr
   03/08, Office de tourisme des Pyrénées Ariégeoises, MAJ 11/08 — **rouverte et
   contrôlée aujourd'hui : toujours en ligne, toujours à jour, confirme la
   déviation**), donc la règle des 14 jours (agent-prompt.md) ne s'applique pas
   ici : pas de dégradation à appliquer d'autorité. Ce qui reste flottant est
   l'arrêté préfectoral d'interdiction du feu (4e reconduction jusqu'au 24/08,
   aucune 5e reconduction ni levée trouvée depuis). **Recommandation** : au
   prochain passage sur l'Ariège, chercher spécifiquement le sort de cet arrêté
   (ariege.gouv.fr) ; si le silence se prolonge sans lien avec la fermeture GR®10
   elle-même, aucune dégradation de sévérité n'est nécessaire puisque HAUTE repose
   sur la fermeture de sentier, pas sur l'arrêté-feu.
3. **`reroutage|Lot-Cieurac-Flaujac-Poujols|GR65-devie-incendie|2026-07-25`** —
   FRAÎCHEUR (contrôle 1) FAIL : vérifiée il y a 13 j, seuil 12 j (sévérité MOYENNE).
   **Action attendue** : recontrôler ffrandonnee.fr / mairies de Limogne-en-Quercy
   pour confirmer que la déviation balisée du 25/07 est toujours en place.

## Contrôle 7 (SOURCE VIVANTE) — vérification directe des sources rouges

Sources vérifiées en direct aujourd'hui pour les 3 fiches HAUTE de ce lot :
- PO-66 : `torderes.unblog.fr` (communiqué préfectoral du 27/08) — **PASS**, contenu
  confirmé mot pour mot (« LES MASSIFS SONT EN VIGILANCE ROUGE », 5 massifs nommés).
  Un premier essai via l'outil de fetch a renvoyé une 503 ; un second essai en direct
  (curl) a confirmé un 200 et le contenu exact — traité comme faux positif transitoire,
  pas comme source morte.
- Vaucluse-84 : `vaucluse.gouv.fr` (communiqué du 16/08, pour le 17/08) — **PASS**,
  page accessible, 11 massifs nommés confirmés.
- Ariège : page de l'Office de tourisme des Pyrénées Ariégeoises (MAJ 11/08) —
  **PASS**, accessible, déviation Bassiès/Saleix confirmée.

## Défaut d'outillage relevé (hors périmètre de correction, signalé pour le pilote)

`site/build_site.py::parse_alerte()` lit le front-matter ligne à ligne et n'associe
un champ (`validite:`, `statut:`…) qu'à sa **première** ligne physique : toute
ligne de continuation indentée (pratique courante pour `statut:` sur ce registre)
est silencieusement ignorée par le parseur, y compris par `audit_qualite.py` qui
réutilise `load_alertes()`. Sans conséquence constatée aujourd'hui pour `statut:`
(la date-clé du jour figure toujours en 1re ligne, par habitude d'écriture), mais
`validite:|PO-66` en a été la victime directe. Recommandation : soit le parseur
apprenne les lignes de continuation indentées, soit la consigne d'écriture impose
`validite:`/`statut:` en une seule ligne physique.

## Note annexe — hors périmètre de cet audit

`python3 site/verif_faits.py HEAD` signale par ailleurs 4 fiches modifiées aujourd'hui
par la veille et **non citées** par `audit-qualite.md` (donc hors périmètre de
correction ici) avec des nombres perdus/inventés au sens du script : `incendie|Cap-
Corse-Cagnano|feu-RD132-fermee|2026-08-29`, `incendie|HautesPyrenees-Bareges|Pic-
Lurtet-Glere-piste-fermee|2026-07-08`, `risque-feu|FR-06-AlpesMaritimes|fermeture-
Esterel-Tanneron|2026-07-17`, `risque-feu|Herault-34|fermetures-massifs-
quotidiennes|2026-07-02`. Les nombres en cause (30, 31, 02, 16, 8) sont
vraisemblablement des dates de MAJ légitimement nouvelles plutôt que des faits
inventés, mais je ne les ai pas rouvertes en détail (hors périmètre du jour) : à
vérifier par un prochain passage de ce même agent une fois qu'elles remonteront,
le cas échéant, dans `audit-qualite.md`.

## Bilan des 7 contrôles sur les 7 fiches auditées

| Contrôle | Résultat |
|---|---|
| 1. Fraîcheur | FAIL sur 2 fiches (Creta-Samaria, Lot-Cieurac) — signalées, source nouvelle requise |
| 2. Concordance interne | PASS sur les 7 (écarts Portion/statut ≤ 4 j, sous le seuil de 7 j) |
| 3. Honnêteté sur l'incertain | PASS — aucune restriction présentée comme probable sans le dire |
| 4. Pertinence | PASS sur les 7 ; Corse-Calenzana à surveiller (aucun impact sentier confirmé, feu contrôlé) si le silence persiste, pas encore un FAIL |
| 5. Sévérité juste | PASS sur les 7 |
| 6. Ton | 1 FAIL corrigé (Vaucluse-84, jargon), PASS sur les 6 autres |
| 7. Source vivante | PASS sur les 3 fiches HAUTE vérifiées en direct (Ariège, PO-66, Vaucluse-84) ; source Ariège vieillissante (18/08) signalée en recommandation |

7 fiches contrôlées, 4 corrections appliquées, 3 actions laissées au prochain passage
de veille, 4 fiches hors périmètre signalées en note annexe.
