# Verdict qualité du registre — 2026-09-16

Agent : `agents/verificateur-alertes.md`, distinct de l'agent qui a mené la veille du jour
(4 fiches créées, 2 fiches modifiées matériellement, 40 dates `verif:` rafraîchies). Aucune
des fiches contrôlées ci-dessous n'a été écrite par moi : audit indépendant, pas relecture de
complaisance.

`livrables/audit-qualite.md` (déjà généré par `python3 site/audit_qualite.py --ecrire`,
2026-09-16) : **9 constats, 0 bloquant**, sur 125 fiches (94 actives). Périmètre de contrôle
= ces 9 fiches, et elles seules ; le dossier complet `livrables/alertes/` n'a pas été relu.
Les 9 constats portent sur des sources vieillissantes / dates de vérification en retard pour
des zones déjà en escalade (recherche ciblée de l'acte manquant déjà tentée par la veille du
jour, sans résultat) : conformément au périmètre de cet agent, ces gaps ne sont pas comblés
ici (il faudrait une source nouvelle), seulement vérifiés pour concordance et honnêteté.

`python3 site/build_site.py` → **OK (QA passée)** (94 actives, 31 clôturées, 58 digests, 125
fichiers, registre 801 165 car.). Garde-fou d'intégrité du build (perte de texte) : 0
déclenchement — logique, aucune fiche n'a été modifiée ce passage.

`python3 site/audit_qualite.py` relancé après contrôle : toujours **9 constats, 0 bloquant**
(inchangé, aucune correction n'était nécessaire ni applicable dans mon périmètre).

## PASS / FAIL par contrôle — 9 fiches citées par l'audit

| Fiche | 1 Fraîcheur | 2 Concordance | 3 Honnêteté | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante |
|---|---|---|---|---|---|---|---|
| `fermetures-sentiers\|Réunion-974\|AP-2026-693\|2026-05-21` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `fermeture\|CH-EST-Kandersteg\|Spitze-Stei-deviation-seg-1.13\|2023-05-08` | PASS (INFO, 8 j < seuil 45 j) | PASS | PASS | PASS | PASS | PASS | n/a (INFO, non vérifié) |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `fermeture\|GR-E4-Creta-Samaria\|fermetures-meteo-repetees\|2026-07-16` | **FAIL** (5 j, seuil 2 j) | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE, non vérifié) |
| `incendie\|Ariege-Bordes-Uchentein\|GR10-ferme-Esbintz-Valier\|2026-07-10` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `incendie\|AT-Vorarlberg-Silvretta\|coulee-boue-sentiers-fermes\|2026-07-12` | **FAIL** (13 j, seuil 12 j) | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE, non vérifié) |
| `incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `risque-feu\|FR-EST-Vosges-88\|interdiction-feu-vigilance-severe\|2026-07-28` | **FAIL** (13 j, seuil 12 j) | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE, non vérifié) |

9 fiches contrôlées. 0 correction appliquée ce passage : les 3 FAIL sont tous des retards de
revérification (contrôle 1) qui exigent une source nouvelle du jour (samaria.gr/crete.gov.gr,
montafon.at, vosges.gouv.fr) — hors de mon périmètre, transmis à la veille ci-dessous. 0 FAIL
sur les contrôles 2 à 7.

### Détail — les 5 alertes ROUGES « source vieillissante » : vérifiées en direct, pas de défaut

L'audit déterministe signale une source de plus de 10 jours sous une alerte HAUTE pour
Réunion, Baronnies, Ariège, Drôme-Justin et Hautes-Alpes-Bois-Noir. Dans les 5 cas, la
sévérité HAUTE repose sur un **arrêté (préfectoral ou municipal) « jusqu'à nouvel ordre »**
déjà lu en entier par la veille, pas sur une hypothèse (« à confirmer », « probable »,
« non localisé »… absents des 5 « Portion concernée ») — la règle des 14 jours ne s'applique
donc pas ici. J'ai vérifié
en direct (contrôle 7, WebFetch + curl) les sources citées :
- `onf.fr` (Réunion) : page vivante, propose toujours le téléchargement de l'arrêté
  n°2026-1415 (27/08/2026) comme document de référence.
- `baronnies-provencales.fr` (Baronnies) : page vivante, toujours « mis à jour le 01/09/26 »,
  12 communes nommées — identique à ce qu'affiche la fiche.
- `bordesuchentein.fr` (Ariège) : le PDF de l'arrêté du 31/08/2026 répond HTTP 200
  (3,6 Mo, `application/pdf` ; illisible par l'outil de résumé automatique faute d'OCR, mais
  bien en ligne et de la taille attendue — pas une source morte).
- `mairie-die.fr` (Drôme-Justin) : page vivante, confirme l'arrêté du 21/08/2026 (forêts de
  Justin/Laup/Solaure), motif chutes de pierres, aucune date de levée annoncée — conforme à
  la fiche.
- `ville-argentiere.fr` (Hautes-Alpes-Bois-Noir) : page vivante, confirme l'arrêté municipal
  du 15/08/2026 toujours en vigueur, sans date de réouverture — conforme à la fiche.

Sur ces 5 fiches, honnêteté déjà correcte : chacune dit au lecteur, en clair, ce qui n'est
*pas* publié (date de levée non fixée pour Drôme-Justin et Hautes-Alpes-Bois-Noir ; communes
sans arrêté retrouvé listées nommément pour Baronnies ; identification GR®R2 non confirmée
par un topo-guide officiel pour Réunion). Aucune correction requise.

## Corrections appliquées — aucune ce passage

Les 9 fiches citées par l'audit sont, sur le fond, correctement écrites : « Portion
concernée » reflète déjà l'état le plus récent connu par `statut:`/« Zone (détails) », aucun
jargon de veille (« ce run », « recherche ciblée », « en autonome »…) dans les champs
publics, aucune validité expirée à réécrire, aucun `statut:` empilé à ramener à l'état
courant. Rien dans mon périmètre à corriger ce passage.

## À traiter au prochain run de veille (nécessite une source nouvelle, hors de mon périmètre)

- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — `verif: 2026-09-11`
  (5 j, seuil 2 j : restriction décidée au jour le jour). Revérifier le statut du jour sur
  samaria.gr et crete.gov.gr avant toute nouvelle publication de « Dernière vérif ».
- `incendie|AT-Vorarlberg-Silvretta|coulee-boue-sentiers-fermes|2026-07-12` — `verif:
  2026-09-03` (13 j, seuil 12 j moyenne). Revisiter montafon.at (Bielerhöhe Seerundweg) pour
  confirmer que le sentier du tour du lac et la liaison Partenen↔Bielerhöhe restent fermés.
- `risque-feu|FR-EST-Vosges-88|interdiction-feu-vigilance-severe|2026-07-28` — `verif:
  2026-09-03` (13 j, seuil 12 j moyenne). Revisiter vosges.gouv.fr / clickalert.org pour un
  bulletin de vigilance incendie plus récent que le 17/08, et confirmer qu'aucune fermeture
  de sentier n'est apparue depuis.
- `fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08` — `verif:
  2026-09-08`, jamais revérifiée depuis sa détection (8 j ; non bloquant, INFO, seuil réel
  45 j). Sans urgence : à revisiter (data.geo.admin.ch) à la prochaine couverture de la
  Suisse plutôt qu'en priorité.

**Confirmation de maintien souhaitable (faux positifs vérifiés vivants par mes soins, non
urgents, arrêtés « jusqu'à nouvel ordre » qui ne se republient pas tant qu'ils ne sont ni
abrogés ni prolongés) :**

- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`

Aucune dégradation ni clôture de sévérité n'est recommandée sur les 9 fiches ci-dessus : dans
les 9 cas, le fond de l'alerte reste correctement établi et honnêtement présenté au lecteur.
