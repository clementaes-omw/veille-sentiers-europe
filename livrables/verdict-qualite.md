# Verdict qualité — 2026-08-07

Vérificateur distinct de l'agent de veille du jour. Périmètre de travail : les 7 fiches
citées par `livrables/audit-qualite.md` (généré le 2026-08-07 par
`python3 site/audit_qualite.py --ecrire`, avant correction : 71 fiches, 0 bloquant,
2 alertes, 5 infos). Aucune autre fiche du registre n'a été ouverte ni modifiée.

## Fiches contrôlées : 7

| Clé | 1 Fraîcheur | 2 Concordance | 3 Honnêteté | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante |
|---|---|---|---|---|---|---|---|
| `fermeture\|IT-DOLOMITES-Brenta\|Cima-Falkner-Bocchette-sentieri-chiusi\|2025-07` | **FAIL** (13 j, seuil 12 j) | PASS | PASS | PASS | PASS | PASS | n/a (sev MOYENNE) |
| `risque-feu\|FR-Landes-Gironde\|vigilance-rouge-bivouac-interdit\|2026-07-21` | PASS | PASS | PASS | PASS | PASS | PASS | n/a (sev MOYENNE) |
| `accès\|Calanques-13\|risque-feu-4couleurs\|2026-06-01` | PASS | PASS | PASS | PASS | PASS | **FAIL→corrigé** | PASS (cg13.eway.fr, 07/08, contenu conforme) |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` | PASS | PASS | PASS | PASS | PASS | **FAIL→corrigé** | PASS (gervanne-sye.com, contenu conforme) |
| `incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19` | PASS | PASS | PASS | PASS | PASS | **FAIL→corrigé** | PASS (ecrins-parcnational.fr, 28/07, contenu conforme) |
| `risque-feu\|ES-CANARIAS-GranCanaria-Tenerife\|interdiction-pistes-sentiers-forestiers\|2026-07-05` | PASS | PASS | PASS | PASS | PASS | **FAIL→corrigé** | n/a (sev MOYENNE) |
| `risque-feu\|Vaucluse-84\|fermeture-8-massifs\|2026-07-01` | PASS | PASS | PASS | PASS | PASS | **FAIL→corrigé** | PASS (vaucluse.gouv.fr, 05/08, contenu conforme) |

Note sur la fiche Landes-Gironde : l'audit l'avait signalée pour une `validite:` en apparence
expirée au 04/08 (contrôle 1/3, échéance passée). À la lecture, ce n'était pas une échéance
mais la date du déclassement rouge→orange déjà passée par nature ; le champ manquait
seulement d'une formulation explicite « sans échéance de levée annoncée ». Corrigé sous
contrôle 3 (honnêteté sur ce qu'on ne sait pas / clarté de la validité), à information
constante d'après le `statut:` et la « Zone (détails) » déjà présents dans la fiche.

Contrôle 7 (source vivante) : les 4 sources primaires des fiches HAUTE contrôlées ont été
relues en direct ce jour (cg13.eway.fr, gervanne-sye.com, ecrins-parcnational.fr,
vaucluse.gouv.fr) — toutes répondent et portent bien l'information citée par la fiche.
Aucune source morte détectée dans ce périmètre.

## Corrections appliquées (dans mon périmètre, à information constante)

- `risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21` — `validite:`
  reformulée pour dire explicitement que l'interdiction bivouac/zones brûlées reste en
  vigueur « jusqu'à nouvel ordre, sans échéance de levée annoncée », au lieu de laisser la
  date du 04/08 (date du déclassement rouge→orange) se lire comme une échéance expirée.
  Aucun fait ajouté ou retiré ; le contenu de `statut:` et « Zone (détails) » le disait déjà.
- `accès|Calanques-13|risque-feu-4couleurs|2026-06-01` — « Zone (détails) » : « Piège
  d'indexation déjoué » → « Point de vigilance sur la date » (même fait : incohérence
  jour/date écartant un article probablement antérieur).
- `risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`
  — « Zone (détails) » : « piège d'indexation déjoué » → « confusion de dates écartée »
  (même fait : deux articles de 2023/2019 écartés comme non datés de 2026).
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — « Zone (détails) » : « à
  vérifier au prochain passage » → « reste à confirmer » (même fait, formulé pour le
  lecteur plutôt que pour la veille).
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` —
  « Zone (détails) » : « à clarifier au prochain passage » → « reste à confirmer » (même
  correction que ci-dessus) ; et champ `itin:` : suppression de la parenthèse-journal
  (« CORRECTION 27/07 : la contradiction n'est PAS résolue, voir statut/ligne dédiée… »)
  qui dupliquait, dans un champ public affiché en badge, un récit déjà présent et complet
  dans la chronologie datée de « Zone (détails) » (§ « Correction de fond (27/07) »).
  Rien n'est perdu : l'explication reste dans « Zone (détails) », seule la parenthèse
  interne au champ `itin` a été retirée. `itin:` redevient « GR54A (fermé) ; GR54
  (itinéraire de repli, praticable) ».
- `risque-feu|Vaucluse-84|fermeture-8-massifs|2026-07-01` — « Zone (détails) » : « la
  reconduction du week-end reste à vérifier au prochain passage » → « la reconduction de
  l'interdiction au-delà du week-end n'est pas encore confirmée » (même fait).

Après ces corrections : `python3 site/build_site.py` → **OK (QA passée)** (60 actives,
11 clôturées, 21 digests). `python3 site/audit_qualite.py --ecrire` → **0 bloquant, 1
alerte, 0 info** sur 71 fiches (la seule alerte restante est ci-dessous, hors périmètre de
correction directe).

## Laissé à l'agent de veille — à traiter au prochain run

- **`fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07`**
  (contrôle 1, FRAÎCHEUR — FAIL). Dernière vérification le 25/07/2026, soit 13 jours,
  au-delà du seuil de 12 jours pour une alerte MOYENNE. Aucune réécriture possible à
  information constante : la fiche ne contient aucune source plus récente que celle déjà
  citée (il Dolomiti, 09/07/2026) permettant de confirmer que « la plupart des sentiers »
  du réseau Bocchette del Brenta restent fermés. **Action attendue au prochain passage
  couvrant la zone IT-DOLOMITES** : rechercher une source postérieure (il Dolomiti, SAT
  Trentino, gestionnaire du refuge/sentier) confirmant soit le maintien de la fermeture,
  soit une réouverture partielle du réseau depuis l'éboulement de juillet 2025, et mettre
  à jour `verif:` et, si la situation a changé, « Portion concernée ».

Aucune autre fiche du registre n'a été ouverte. Aucune suppression, aucune clôture, aucune
dégradation/remontée de sévérité appliquée d'autorité — la règle des 14 jours sur les
hypothèses non tranchées ne s'est déclenchée sur aucune des 7 fiches contrôlées.
