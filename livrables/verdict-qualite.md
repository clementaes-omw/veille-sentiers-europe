# Verdict qualité — 2026-09-12

Vérificateur Qualité, distinct de l'agent de veille qui a produit le run du jour (4 nouvelles
alertes créées, 9 alertes HAUTE mises à jour en escalade, ligne IT-Liguria-CinqueTerre ajoutée
à `referentiel/zones-coords.csv`). Aucune des fiches contrôlées ci-dessous n'est de ma main :
le contrôle est valide.

Périmètre : les 7 fiches citées par `livrables/audit-qualite.md` du jour (7 constats « À
traiter », 0 bloquant). Aucune autre fiche du dossier n'a été touchée.

## Résultat après corrections

`python3 site/build_site.py` → **OK (QA passée)** (88 actives, 30 clôturées, 118 fichiers).
`python3 site/audit_qualite.py --ecrire` (relancé après corrections) → **0 bloquant(s)**,
7 alerte(s) restantes (inchangé en nombre : les 6 constats « source vieillie » ne sont pas
des défauts, cf. plus bas ; le 7e — Réunion-974 — demande une source nouvelle hors de mon
périmètre).
`python3 site/verif_faits.py` → 4 fiches modifiées contrôlées vs HEAD, **0 perte(s)/invention(s)
de fait**.

## PASS / FAIL par contrôle, fiche par fiche

| Fiche | 1 Fraîcheur | 2 Concordance | 3 Honnêteté hypothèse | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante |
|---|---|---|---|---|---|---|---|
| `fermetures-sentiers\|Réunion-974\|AP-2026-693\|2026-05-21` | **FAIL** (13 j, seuil 12 j) → signalé | PASS | PASS | PASS | PASS (MOYENNE justifiée par le recoupement non fait) | FAIL(jargon)→corrigé | n/a (MOYENNE) |
| `fermeture\|DE-Sachsen-SaechsischeSchweiz…Sturmschaeden` (Malerweg Bastei) | PASS (verif du jour) | PASS | n/a (fondement = arrêté daté, pas une hypothèse) | PASS | PASS | PASS | PASS — `eilmeldung-waldsperrung` répond (200), périmètre fermé conforme au texte |
| `fermeture\|FR-Baronnies-GR9\|arretes-municipaux` | PASS (verif du jour) | FAIL(date décrochée)→corrigé | PASS | PASS | PASS | FAIL(jargon)→corrigé | PASS — page PNR Baronnies Provençales répond (200), 12 communes conformes |
| `incendie\|Ariege-Bordes-Uchentein…GR10-ferme-Esbintz-Valier` | PASS (verif du jour) | PASS | PASS | PASS | PASS | PASS | PASS — `bordesuchentein.fr` répond (200), arrêté du 31/08 conforme |
| `incendie\|Drome-Justin-Die\|foret-fermee` | PASS (verif du jour) | FAIL(date décrochée)→corrigé | PASS (rattachement GR®9/GR®93 dit « affaibli » en clair) | PASS | PASS | FAIL(jargon)→corrigé | PASS — `mairie-die.fr` répond (200), arrêté du 21/08 conforme |
| `incendie\|HautesAlpes-BoisNoir…GR54A-ferme-Argentiere-Freissinieres` | PASS (verif du jour) | FAIL(date décrochée)→corrigé | PASS | PASS | PASS | FAIL(jargon)→corrigé | PASS — `ville-argentiere.fr` répond (200), arrêté du 15/08 conforme |
| `risque-feu\|PO-66\|vigilance-rouge-fermeture-tous-massifs` | PASS (verif du jour) | PASS | PASS (statut des 7 massifs dit « non tranché » en clair) | PASS | PASS | PASS | PASS — `titrespresse.com` répond (200), article du 03/09 conforme |

## Corrections appliquées (dans `livrables/alertes/*.md`)

1. **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — jargon de veille retiré de
   « Portion concernée » : « n'a pas pu être consulté à distance ce jour […] n'est pas lisible
   en fetch automatisé » → « n'est pas accessible en ligne à ce jour […] ne s'ouvre pas depuis
   ce site ». Aucune perte de fait.
2. **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — « Portion concernée »
   recollée à l'état du jour (réécriture à information constante : le `statut:` du jour
   confirme la même liste de 12 communes) : « confirmée à l'identique ce jeudi 10/09/2026 » →
   « confirmée à l'identique le 12/09/2026 ». Jargon de veille retiré de « Zone (détails) » :
   « fetch direct de mairiedesaillans26.fr tenté » → « consultation directe de
   mairiedesaillans26.fr tentée ».
3. **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — « Portion concernée » recollée à
   l'état du jour (même règle : le `statut:` confirme le même constat) : « à la vérification
   du 08/09/2026 » → « à la vérification du 12/09/2026 ». Jargon retiré de « Zone (détails) »
   (2 occurrences) : « fetch direct de la page … » → « consultation directe de la page … ».
4. **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** —
   « Portion concernée » recollée à l'état du jour : « Revuérifié le 08/09/2026 » →
   « Revuérifié à plusieurs reprises jusqu'au 12/09/2026 ». Jargon retiré de « Zone
   (détails) » : « le fetch direct est impossible (… 403 x2 … 503 x2 …) » → « la consultation
   directe est impossible (… renvoie une erreur 403 à deux reprises … renvoient chacune une
   erreur 503 à deux reprises) ».

Correction envisagée puis écartée : sur `DE-Sachsen…Sturmschaeden`, avancer la date « situation
au 06/09/2026 » à ce jour aurait introduit dans la prose un nombre (« 12 ») absent du texte
d'origine, ce que `site/verif_faits.py` refuse à raison (aucun fait ne doit apparaître sans
preuve) — le champ `statut:` et « Zone (détails) » (MAJ 10/09) portent déjà la confirmation la
plus récente ; « Portion concernée » n'est pas en contradiction de contenu avec eux, seulement
d'un intitulé de date, ce qui reste un PASS sur le contrôle Concordance. Laissé en l'état.

## Actions laissées à l'agent de veille (constats non corrigibles dans mon périmètre)

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — **FRAÎCHEUR, FAIL.** Vérifiée
  il y a 13 jours (30/08), seuil 12 jours pour une sévérité MOYENNE. Nécessite une source
  nouvelle : ouvrir le PDF de l'arrêté n°2026-1415 (ou trouver un relais qui en détaille le
  contenu) pour trancher si le GR® R2/Mafate est concerné, et rafraîchir `verif:`. Hors de mon
  périmètre (jugement de fond sur une recherche à mener), pas une correction de forme.

- **6 alertes rouges appuyées sur une source datée de 11 à 22 jours**
  (`DE-Sachsen-SaechsischeSchweiz…Sturmschaeden`, `FR-Baronnies-GR9`,
  `Ariege-Bordes-Uchentein…GR10-ferme-Esbintz-Valier`, `Drome-Justin-Die`,
  `HautesAlpes-BoisNoir…GR54A-ferme-Argentiere-Freissinieres`, `PO-66`) — signalé par l'audit
  déterministe (contrôle mécanique sur l'âge de la date la plus récente citée en `source:`),
  mais **ce n'est pas un défaut de qualité** après vérification de fond : dans chacune des 6,
  la sévérité HAUTE repose sur un arrêté (ou une Allgemeinverfügung) officiel et daté, sans
  échéance calendaire propre (« jusqu'à nouvel ordre », « bis auf Widerruf », ou en attente
  d'une étude de risque) — ce n'est pas une hypothèse « à confirmer »/« probable », donc la
  règle des 14 jours (dégradation obligatoire) ne s'applique pas. Chaque fiche documente une
  recherche CIBLÉE de l'acte de levée effectuée aujourd'hui (12/09), sans résultat. Les 6
  sources primaires citées répondent toujours (HTTP 200, vérifié ce jour) et portent bien le
  texte annoncé. Aucune dégradation recommandée. Action laissée au prochain passage : la
  zone reste en ESCALADE, poursuivre la recherche ciblée de l'acte de reconduction ou de
  levée manquant sur chacune — c'est déjà noté dans le `statut:` de chaque fiche.

## Fiches contrôlées : bilan

7 fiches contrôlées (les 7 constats de l'audit du jour). 4 corrections de forme appliquées
(concordance interne + jargon de veille) et vérifiées par un nouveau build + audit + contrôle
de faits (0 perte/invention). 1 constat de fraîcheur laissé à la veille (Réunion-974, source
nouvelle nécessaire). 6 constats « source vieillie » examinés et jugés non fondés au vu du
texte des fiches (arrêtés sans échéance, pas des hypothèses) : aucune dégradation, la règle
des 14 jours ne s'applique à aucune des fiches vues aujourd'hui. Aucune fiche clôturée.
