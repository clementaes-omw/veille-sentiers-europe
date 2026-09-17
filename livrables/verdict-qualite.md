# Verdict qualité du registre — 2026-09-17

Agent : `agents/verificateur-alertes.md`, distinct de l'agent qui a mené la veille du jour.
Aucune des fiches contrôlées ci-dessous n'a été écrite par moi : audit indépendant, pas
relecture de complaisance.

`livrables/audit-qualite.md` (généré par `python3 site/audit_qualite.py --ecrire`,
2026-09-17) : **9 constats, 1 bloquant**, sur 125 fiches (94 actives). Périmètre de contrôle
= les 9 fiches citées, et elles seules (8 clés distinctes + `GR-E4-Creta-Samaria` désigné
bloquant) ; le dossier complet `livrables/alertes/` n'a pas été relu.

`python3 site/build_site.py`, relancé après corrections → **OK (QA passée)** (94 actives, 31
clôturées, 59 digests, 125 fichiers, registre 806 380 car.). Garde-fou d'intégrité du build
(perte de texte) : 0 déclenchement.

`python3 site/audit_qualite.py`, relancé après corrections : **7 constats, 1 bloquant**
(contre 9 constats / 1 bloquant au départ, puis brièvement 9/2 avant correction du
phrasé — voir note sous le tableau). Les 3 fiches corrigées (Réunion, ES-AND-Benahavis,
PO-66) ne portent plus de constat déterministe évitable ; les 4 fiches « source
vieillissante » restantes (Baronnies, Ariège, Drôme-Justin, Hautes-Alpes-Bois-Noir) et
Kandersteg sont des faux positifs du contrôle déterministe ou des retards hors de mon
périmètre, documentés ci-dessous. Le bloquant Creta-Samaria subsiste : hors de mon
périmètre (nécessite une source nouvelle du jour).

## PASS / FAIL par contrôle — 9 fiches citées par l'audit

| Fiche | 1 Fraîcheur | 2 Concordance | 3 Honnêteté | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante |
|---|---|---|---|---|---|---|---|
| `fermeture\|GR-E4-Creta-Samaria\|fermetures-meteo-repetees\|2026-07-16` | **FAIL** (6 j, seuil 2 j) | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE, non vérifié) |
| `fermetures-sentiers\|Réunion-974\|AP-2026-693\|2026-05-21` | PASS | PASS | PASS (corrigée) | PASS | PASS | PASS | **FAIL détecté** → corrigé en partie (caveat honnête ajouté), reste à traiter |
| `fermeture\|CH-EST-Kandersteg\|Spitze-Stei-deviation-seg-1.13\|2023-05-08` | **FAIL** (9 j, INFO, sans urgence) | PASS | PASS | PASS | PASS | PASS | n/a (INFO, non vérifié) |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `incendie\|Ariege-Bordes-Uchentein\|GR10-ferme-Esbintz-Valier\|2026-07-10` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct, PDF en ligne) |
| `incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19` | PASS | PASS | PASS | PASS | PASS | PASS | PASS (vérifié en direct) |
| `incendie\|ES-AND-Benahavis\|feu-actif-confinement-9500-habitants\|2026-09-13` | PASS | PASS | PASS (corrigée) | PASS | PASS | PASS | PASS (vérifié en direct) |
| `risque-feu\|PO-66\|vigilance-rouge-fermeture-tous-massifs\|2026-07-26` | PASS | PASS | PASS (corrigée) | PASS | PASS (MOYENNE, correctement prudente) | PASS | n/a (MOYENNE, source secondaire vérifiée en direct) |

9 fiches contrôlées. 3 corrections appliquées (Réunion, ES-AND-Benahavis, PO-66). 1 FAIL
bloquant hors périmètre (Creta-Samaria, contrôle 1). 1 FAIL non bloquant hors périmètre
(Kandersteg, contrôle 1). 0 FAIL restant sur les contrôles 2 à 6.

## Corrections appliquées

- **`incendie|ES-AND-Benahavis|feu-actif-confinement-9500-habitants|2026-09-13`**
  (contrôle 1/3, `validite:`) — le champ mélangeait un fait daté (« stabilisé le
  14/09/2026 ») avec l'absence d'échéance réelle, ce que le contrôle déterministe lisait à
  tort comme une validité expirée le 14/09. Réécrit à information constante : « en vigueur
  jusqu'à confirmation de l'extinction complète (aucune échéance fixe) », en gardant tous
  les faits déjà sourcés (stabilisation du 14/09, préemergence, surface, moyens).
- **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`**
  (contrôle 1/3, `validite:`) — même défaut de lecture (date du 14/09 pour le retour en
  rouge du Roussillon, prise pour une échéance). Réécrit avec les échéances réelles déjà
  citées dans la fiche (MAJ 17/09, source mawebtv.fr, vérifiée en direct ce jour) :
  restrictions d'accès aux massifs prolongées jusqu'au 25/09/2026, usage du feu par les
  particuliers interdit jusqu'au 01/10/2026, écobuage reporté au 30/09/2026 ; la mention
  « Roussillon repassé en rouge le 14/09, source unique non corroborée » est conservée
  telle quelle.
- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`**
  (contrôle 7, `Portion concernée` + `statut:`) — en vérifiant en direct la source ONF
  citée par la fiche (onf.fr), j'ai constaté qu'elle ne mentionne plus l'arrêté
  n°2026-1415 du 26/08/2026 sur lequel repose toute la fiche, mais un texte plus récent,
  l'**arrêté n°2026-1617 du 16/09/2026** (la veille du jour, dont le `verif:` a été
  rafraîchi au 17/09, ne l'a pas repéré). Correction à information constante : j'ai ajouté
  au texte public un constat honnête de ce que je viens d'observer (existence du nouveau
  texte, non lu, remplacement probable de l'ancien selon le fonctionnement documenté de ces
  arrêtés), sans inventer le contenu du nouvel arrêté ni changer la sévérité. Voir action
  prioritaire ci-dessous.

## À traiter au prochain run de veille (nécessite une source nouvelle, hors de mon périmètre)

- **PRIORITAIRE — `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** : lire
  l'arrêté n°2026-1617 du 16/09/2026 (lien PDF présent sur la page ONF Réunion, section
  « sentiers de randonnée ») et vérifier s'il maintient, modifie ou lève la fermeture du
  Bras des Merles (Deux Bras ↔ Aurère, GR® R2) et des 48 autres sentiers actuellement
  listés d'après l'arrêté n°2026-1415, devenu probablement caduc. Ce n'est pas seulement un
  retard de fraîcheur : la source qui fonde toute la fiche a changé.
- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — `verif:
  2026-09-11` (6 j, seuil 2 j : restriction décidée au jour le jour). Revérifier le statut
  du jour sur samaria.gr et crete.gov.gr (catégorie de risque incendie du 17/09) avant toute
  nouvelle publication de « Dernière vérif ».
- `fermeture|CH-EST-Kandersteg|Spitze-Stei-deviation-seg-1.13|2023-05-08` — `verif:
  2026-09-08`, jamais revérifiée depuis sa détection (9 j ; non bloquant, INFO). Sans
  urgence : à revisiter (data.geo.admin.ch, id 2596765) à la prochaine couverture de la
  Suisse plutôt qu'en priorité.

**Confirmation de maintien souhaitable (faux positifs du contrôle déterministe, vérifiés
vivants par mes soins, non urgents ; arrêtés « jusqu'à nouvel ordre » qui ne se republient
pas tant qu'ils ne sont ni abrogés ni prolongés) :**

- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — baronnies-provencales.fr
  vivante, toujours « mise à jour le 01/09/26 », 12 communes nommées, identique à la fiche.
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — le PDF de
  l'arrêté du 31/08/2026 sur bordesuchentein.fr répond, 3,5 Mo, en ligne (illisible par
  l'outil de résumé automatique faute d'OCR, pas une source morte).
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — mairie-die.fr vivante, confirme
  l'arrêté du 21/08/2026 (Justin/Laup/Solaure), aucune échéance annoncée.
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` —
  ville-argentiere.fr vivante, confirme l'arrêté municipal du 15/08/2026 toujours en
  vigueur, sans date de réouverture.

Sur ces 4 fiches, la sévérité HAUTE repose sur un arrêté déjà lu en entier par la veille,
pas sur une hypothèse (« à confirmer », « probable », « non localisé »… absents des 4
« Portion concernée ») : la règle des 14 jours ne s'applique pas, et le signal « source de
plus de 10 j » du contrôle déterministe est un faux positif pour ces 4 cas précis. Aucune
dégradation ni clôture de sévérité n'est recommandée sur les 9 fiches contrôlées : dans les
9 cas, le fond de l'alerte est correctement établi ; seule la fiche Réunion appelle une
action non différable, documentée ci-dessus.
