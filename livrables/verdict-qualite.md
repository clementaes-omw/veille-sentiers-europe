# Verdict qualité — 2026-08-14

Vérificateur qualité, agent distinct de la veille du jour (5 sous-agents parallèles ont mis
à jour le registre aujourd'hui). Je n'ai pas écrit les fiches contrôlées : je les audite, je
ne les refais pas. Périmètre de travail = les 7 constats de `livrables/audit-qualite.md`
régénéré ce jour (`python3 site/audit_qualite.py --ecrire`, 81 fiches, 0 bloquant, 5 alertes,
2 infos avant ce passage).

**7 fiches contrôlées**, toutes citées par l'audit-qualite.md du jour. Deux sources
d'alertes ROUGE citées ont été vérifiées en direct (contrôle 7, SOURCE VIVANTE) :
pyreneesfm.com (Ariège, 10/08) et ouillade.eu (Albères, 29/07) répondent toutes deux et
portent bien l'information annoncée.

## Résumé PASS/FAIL par contrôle

| Contrôle | Résultat |
|---|---|
| 1. FRAÎCHEUR | PASS sur les 7 fiches (toutes revérifiées dans le délai de leur propre validité) |
| 2. CONCORDANCE INTERNE | FAIL corrigé sur 1 fiche (Ariège : « Portion concernée » figée au 02/08 alors que le suivi savait le 14/08) ; PASS sur les 6 autres |
| 3. HONNÊTETÉ | PASS sur les 7 fiches : chaque silence de source ou incertitude est déclaré en clair au lecteur |
| 4. PERTINENCE | PASS formel (aucune n'a perdu tout son sens) ; 2 recommandations de vigilance ci-dessous (Aude, Lozère) |
| 5. SÉVÉRITÉ JUSTE | PASS sur les 7 ; note motivée Albères-66 ci-dessous (règle des 14 jours vérifiée, non applicable) |
| 6. TON | FAIL corrigé sur 2 fiches (jargon de veille dans « Zone (détails) ») |
| 7. SOURCE VIVANTE | Vérifié sur les 2 alertes ROUGE de la liste (Ariège, Albères) : les deux répondent et confirment le contenu cité |

## Corrections appliquées (dans mon périmètre, à information constante)

- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — CONCORDANCE
  INTERNE : « Portion concernée » ne portait aucune date postérieure au 02/08 alors que
  `statut:` savait déjà, au 14/08, qu'aucune réouverture n'avait été annoncée depuis.
  Ajouté en fin de section : « Situation inchangée à la vérification du 14/08/2026 : aucune
  réouverture n'a été annoncée entre l'étang d'Ayès et le Cap des Lauses. » Aucun fait
  nouveau créé, seul le texte affiché rattrape ce que le fichier savait déjà.
- `incendie|Aude-Montseret-Corbieres|feu-fixe-100ha|2026-08-06` — `validite:` se lisait
  comme une échéance périmée (06/08, 8 j). Réécrite d'après `statut:` déjà présent dans le
  fichier (« INCHANGÉ 14/08 : aucune source postérieure au 07/08 retrouvée ») : « … situation
  stable et revérifiée le 14/08/2026 (aucune source postérieure au 07/08 retrouvée) … ».
- `incendie|Lozere-Massegros-Causses-Gorges|feu-fixe-153ha|2026-08-09` — même défaut,
  échéance du 10/08 lue comme expirée (4 j). Réécrite d'après la propre date `verif:` du
  fichier (13/08/2026, déjà établie, aucune recherche neuve) : « … situation stable à la
  dernière vérification du 13/08/2026 … ».
- `incendie|Var-Gros-Bessillon|feu-actif-Ponteves-Cotignac-Correns|2026-07-22` — échéance du
  11/08 lue comme expirée alors que « Zone (détails) » MAJ 14/08 documente déjà la suite
  (réunion post-incendie du 13/08 à Montfort-sur-Argens). `validite:` réécrite pour
  intégrer ce fait déjà sourcé et daté au 14/08.
- `incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24` — jargon de
  veille « recherche ciblée » dans « Zone (détails) » (MAJ 14/08) reformulé en « Aucun
  communiqué postérieur au CP n°9 n'a été retrouvé », même fait (silence officiel de 15
  jours), sans vocabulaire de veille.
- `risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18` — jargon « runs » et
  « recherche ciblée » dans « Zone (détails) » (MAJ 14/08) reformulés en « nouvelle
  vérification, plus large que les précédentes » / « vérification d'un éventuel nouveau
  départ de feu ». Même contenu, même chronologie datée conservée intégralement.

## Note motivée — Albères-66, signalé et non corrigé

`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` reste signalé par l'audit :
alerte rouge appuyée sur une source de presse (ouillade.eu) datée du 29/07, 16 jours.

J'ai d'abord vérifié qu'aucune fiche plus récente ne recouvre cette clé (une seule fiche
existe dans le registre pour Albères-66). Le fichier a bien été revérifié aujourd'hui
(`verif: 2026-08-14`, statut « INCHANGÉ 14/08 : nouvelle vérification ciblée, aucune levée
ni republication trouvée ») ; c'est bien la SOURCE citée qui reste datée du 29/07, pas la
fiche elle-même — deux fraîcheurs distinctes. J'ai vérifié en direct (WebFetch) que
ouillade.eu répond toujours et confirme exactement le contenu cité (interdiction municipale
d'Argelès-sur-Mer, dérogation VTT du 24/07). Trouver une publication plus récente est hors
de mon périmètre (nécessite une recherche web nouvelle, pas une relecture) : je le signale
donc pour le prochain run plutôt que de le corriger moi-même.

Règle des 14 jours (`agent-prompt.md` § DURÉE DE VIE D'UNE HYPOTHÈSE) vérifiée et jugée non
applicable : elle vise une « Portion concernée » encore adossée à « à confirmer »,
« probable », « non localisé » ou « recoupement en cours ». Ce n'est pas le cas ici — la
« Portion concernée » affirme des faits déjà noyautés dans deux arrêtés municipaux nommés et
datés (Sorède n°26.216 du 17/06/2026, jusqu'au 13/09/2026 ; Argelès-sur-Mer du 10/07/2026
renforcé par l'ARR2026-024PM du 13/07/2026, « jusqu'à nouvel ordre »). Ces textes ont leur
propre validité, indépendante de l'âge de l'article de presse qui les rapporte, et aucun des
deux n'est expiré. Aucune dégradation appliquée.

Point à recouper (observation, pas une action, hors périmètre) : le lien PDF cité dans
« Source » porte le numéro « arrêté 26.238 », alors que le texte de la fiche (MAJ 10/08)
cite « arrêté n°26.216 » pour Sorède. Les deux nombres ne se recoupent pas explicitement
dans le texte actuel — à clarifier au prochain passage sur la zone (peut-être deux arrêtés
distincts, à confirmer par une source).

## À traiter au prochain run (hors périmètre du vérificateur — nécessite une source neuve)

- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — retrouver une publication de
  presse ou une source officielle postérieure au 29/07/2026 confirmant que l'accès au
  massif des Albères reste interdit (ou signale une levée). Voir note motivée ci-dessus :
  les arrêtés eux-mêmes ne sont pas périmés, mais la couverture presse l'est.
- `incendie|Aude-Montseret-Corbieres|feu-fixe-100ha|2026-08-06` (recommandation PERTINENCE,
  non appliquée d'autorité) — feu fixé depuis 8 jours, aucune fermeture de sentier jamais
  documentée, routes départementales 61/123/423 dont l'état de réouverture n'est pas
  reconfirmé depuis le 07/08. Si une source confirme la réouverture des routes et l'absence
  de reprise, cette fiche est mûre pour `[CLÔTURÉ]`.
- `incendie|Lozere-Massegros-Causses-Gorges|feu-fixe-153ha|2026-08-09` (recommandation
  PERTINENCE, non appliquée d'autorité) — feu fixé depuis 4 jours, D67 toujours donnée comme
  coupée sans confirmation récente de réouverture. Revérifier avant la prochaine échéance de
  fraîcheur (seuil MOYENNE = 12 j).
- `incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24` — silence
  officiel de la préfecture désormais à 15 jours (dernier CP le 30/07). Chercher un CP n°10
  ou toute annonce de levée de l'interdiction d'accès aux gorges de la Caranca.
- `risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18` — écart à 22 jours
  depuis la dernière source datée (23/07) sur Illarata. Sévérité déjà dégradée en MOYENNE le
  06/08 pour ce motif ; chercher une republication ou une levée de l'arrêté
  n°2A-2026-07-20-00007.

## Vérifications techniques après corrections

- `python3 site/audit_qualite.py --ecrire` : **1 constat restant** (Albères-66, source
  vieillie, signalé ci-dessus, hors périmètre), **0 bloquant**, contre 7 constats sur ces 7
  fiches avant ce passage.
- `python3 site/build_site.py` : **OK (QA passée)** → `site/index.html` (65 actives, 16
  clôturées, 81 fichiers). Le « ⚠ ton » résiduel (2 fiches, jargon « indexation » sur des
  fiches ES-CYL) ne concerne pas les fiches de ce passage et n'est pas touché (règle : une
  fiche non citée par l'audit ne se touche pas).
- Aucune fiche n'a perdu de texte : les 6 fichiers corrigés ont tous grandi (ajouts, jamais
  de résumé), le garde-fou d'intégrité du build (perte > 45 % par fiche) n'a jamais été
  approché.
