# Verdict qualité — 2026-08-15

Vérificateur qualité, agent distinct de la veille du jour. Je n'ai pas écrit les fiches
contrôlées : je les audite, je ne les refais pas. Périmètre de travail = les 7 constats
communiqués (audit `livrables/audit-qualite.md` régénéré le jour même, 70 alertes actives,
0 bloquant, 6 alertes, 1 info avant ce passage ; la section « Cohérence carte / registre »,
5 bloquants au moment où la mission m'a été confiée, s'est révélée déjà résolue par le
commit `bf8cd20` de la veille au moment où j'ai relancé l'audit — hors de mon périmètre de
toute façon, elle relève de `agents/verificateur-carte.md`, non de moi).

**7 fiches contrôlées.** Trois sources d'alertes ROUGE citées ont été vérifiées en direct
(contrôle 7, SOURCE VIVANTE, via WebFetch) : ouillade.eu (Albères, 29/07),
drome-cestmanature.com (Justin/Die, MAJ 12/08) et gard.gouv.fr (Gard, vendredi 07/08)
répondent toutes les trois et portent exactement l'information annoncée dans les fiches.

## Résumé PASS/FAIL par contrôle

| Contrôle | Résultat |
|---|---|
| 1. FRAÎCHEUR | PASS sur les 7 fiches (toutes vérifiées le jour même, `verif: 2026-08-15`) |
| 2. CONCORDANCE INTERNE | FAIL corrigé sur 2 fiches (Gard-30, Hérault-34 : « Portion concernée » figée au 07/08 alors que le suivi savait le 14-15/08) ; PASS sur les 5 autres |
| 3. HONNÊTETÉ | PASS sur les 7 fiches : chaque silence de source ou incertitude est déclaré en clair au lecteur (« aucun point de situation depuis le 16/07 », « aucun avis officiel du parc retrouvé », etc.) |
| 4. PERTINENCE | PASS formel sur les 7 (aucune n'a perdu son sens) ; aucune clôture recommandée — pour chacune des 3 fiches à échéance dépassée, le fait matériel qui la fonde (arrêté non levé, versant instable, fermeture parc) reste établi |
| 5. SÉVÉRITÉ JUSTE | PASS sur les 7 ; note motivée Albères-66 ci-dessous (règle des 14 jours vérifiée, jugée non applicable) |
| 6. TON | FAIL corrigé sur 1 fiche (ES-CYL-Fermoselle-Sayago : jargon de veille dans « Zone (détails) ») |
| 7. SOURCE VIVANTE | Vérifié en direct sur les 3 alertes ROUGE de la liste (Albères, Drôme-Justin, Gard) : les trois répondent et confirment le contenu cité, aucune levée mentionnée |

## Corrections appliquées (dans mon périmètre, à information constante)

- `fermeture|IT-Dolomites-Pelmo|frana-versante-nordovest-borca-di-cadore|2026-08-10` —
  RIEN À CORRIGER : le correctif manuel signalé en amont (`validite:` reformulée en
  « fermeture jusqu'à nouvel ordre… aucune date de levée annoncée ») tient toujours ;
  l'audit ne la signale plus.
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — VALIDITÉ : le champ `validite:`
  citait « une source datée du 12/08 » sans autre précision, que le contrôle déterministe
  lisait comme une échéance expirée. Réécrit d'après la source déjà présente dans le
  fichier (l'arrêté du 17/07, sans échéance calendaire connue, toujours cité actif au
  12/08) : « … en vigueur jusqu'à nouvel ordre : aucune échéance calendaire ni date de
  levée n'est publiée… ». Aucun fait nouveau, seule la formulation change. Contrôle 7
  effectué en direct : drome-cestmanature.com répond toujours, contenu inchangé.
- `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — VALIDITÉ : même
  défaut, le « 04/08 » de l'orage était lisible comme échéance dépassée. Réécrit en
  « fermeture jusqu'à nouvel ordre sur les deux volets, aucune date de levée annoncée pour
  l'un ni pour l'autre », sans toucher au détail déjà présent (volet incendie 17/07, volet
  orage 04/08).
- `risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01` — CONCORDANCE INTERNE :
  « Portion concernée » s'arrêtait au 07/08 alors que `statut:` savait déjà, au 15/08,
  qu'aucune page n'avait reparu depuis (8 jours d'écart, seuil de 7 dépassé). Complétée
  avec le fait déjà connu du fichier (l'entrée du 14/08 de « Zone (détails) ») : « … du 8
  au 13 août inclus, toujours vrai au 14/08 ». Écart ramené à 1 jour.
- `risque-feu|Hérault-34|fermetures-massifs-quotidiennes|2026-07-02` — même défaut, même
  correction : ajout de « toujours vrai au 14/08 », fait déjà présent dans la chronologie
  de « Zone (détails) » (entrée MAJ 14/08).
- `incendie|ES-CYL-Fermoselle-Sayago|feu-record-11000ha-800evacues|2026-07-29` — TON :
  jargon de veille « recherche ciblée » dans « Zone (détails) » (MAJ 14/08) reformulé en
  « aucune source postérieure au 03/08 n'a été retrouvée (zamoranews.com, cope.es,
  tribunazamora.com, elDiario.es consultés) ». Même fait, sans vocabulaire de veille.

`python3 site/verif_faits.py` (garde-fou anti-perte/invention de fait) confirmé propre sur
les 6 fiches modifiées après ajustement des reformulations : 0 perte, 0 invention.

## Note motivée — Albères-66, signalé et non corrigé sur le fond

`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` reste signalé par l'audit : alerte
rouge appuyée sur une source de presse (ouillade.eu) datée du 29/07, 17 jours.

Vérifié en direct (WebFetch) : ouillade.eu répond toujours et confirme exactement le
contenu cité (interdiction municipale d'Argelès-sur-Mer, dérogation VTT du 24/07, aucune
mention de levée) ; le PDF de l'arrêté 26.238 répond également (200, contenu image
illisible en extraction automatique mais lien non mort). Contrôle 7 = PASS : la source
n'est pas morte, elle est seulement ancienne. Trouver une publication de presse plus
récente que le 29/07 est hors de mon périmètre (recherche web nouvelle, pas relecture) :
signalé pour le prochain run plutôt que corrigé moi-même.

Règle des 14 jours (`agent-prompt.md` § DURÉE DE VIE D'UNE HYPOTHÈSE) vérifiée et jugée non
applicable : elle vise une « Portion concernée » encore adossée à « à confirmer »,
« probable », « non localisé » ou « recoupement en cours ». Ce n'est pas le cas ici — la
« Portion concernée » s'appuie sur deux arrêtés municipaux nommés et datés (Sorède
n°26.216 du 17/06/2026, jusqu'au 13/09/2026 ; Argelès-sur-Mer du 10/07/2026 renforcé par
l'ARR2026-024PM du 13/07/2026, « jusqu'à nouvel ordre »), pas sur une hypothèse. Ces textes
ont leur propre validité, indépendante de l'âge de l'article de presse qui les rapporte, et
aucun des deux n'est expiré. Aucune dégradation appliquée ; sévérité maintenue HAUTE.

## À traiter au prochain run (hors périmètre du vérificateur — nécessite une source neuve)

- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — retrouver une publication de
  presse ou une source officielle postérieure au 29/07/2026 sur l'état d'accès au massif
  des Albères (ou une levée). Voir note motivée ci-dessus : les arrêtés eux-mêmes ne sont
  pas périmés, seule la couverture presse l'est.
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — la préfecture (drome.gouv.fr) n'a
  publié aucun point de situation depuis le 16/07/2026 ; seule une source touristique
  (drome-cestmanature.com) confirme, au 12/08, que l'arrêté du 17/07 reste actif. Chercher
  une confirmation ou une levée directement à la source préfectorale, ou tout acte de
  reconduction/levée publié ailleurs (mairie-die.fr, presse locale).
- `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — le volet orage
  (traversée Malesco↔Colloro via Lut/La Piana, dégâts du 04/08) n'est sourcé que par la
  presse (La Prealpina, ~08/08) ; aucun avis officiel du parc (parcovalgrande.it) retrouvé.
  Chercher la publication du parc pour confirmer le périmètre exact et une éventuelle date
  de réouverture.

## Vérifications techniques après corrections

- `python3 site/audit_qualite.py --ecrire` : **1 constat restant** (Albères-66, source de
  presse vieillie, signalé ci-dessus, hors périmètre), **0 bloquant**, contre 6 alertes +
  1 info sur ces 7 fiches avant ce passage. Section carte : 0 bloquant (déjà résolue en
  amont, hors de mon périmètre).
- `python3 site/build_site.py` : **OK (QA passée)** → `site/index.html` (70 actives, 16
  clôturées, 86 fichiers, registre 456 446 car.). Le « ⚠ ton » résiduel (2 fiches, jargon
  « indexation » sur des fiches ES-CYL-Castropodame et ES-CYL-Bierzo) ne concerne pas les
  fiches de ce passage et n'est pas touché (règle : une fiche non citée par l'audit ne se
  touche pas).
- `python3 site/verif_faits.py` : **0 perte(s)/invention(s) de fait** sur les 6 fiches
  modifiées.
- Aucune fiche n'a perdu de texte : les 6 fichiers corrigés ont tous grandi (ajouts, jamais
  de résumé) ; le garde-fou d'intégrité du build (perte > 45 % par fiche) n'a jamais été
  approché.
