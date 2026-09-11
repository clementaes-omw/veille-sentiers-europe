# Verdict qualité — 2026-09-11

Vérificateur Qualité, distinct de l'agent de veille qui a produit le run du jour (digest
2026-09-11). Aucune des fiches contrôlées n'est de ma main : le contrôle est valide.

Périmètre : les 13 fiches citées par `livrables/audit-qualite.md` généré avant mon passage
(12 constats « À traiter » + 1 « Dette de forme »). Aucune autre fiche du dossier n'a été
touchée.

## Résultat après corrections

`python3 site/build_site.py` → **OK (QA passée)** (84 actives, 114 fichiers).
`python3 site/audit_qualite.py --ecrire` (relancé après corrections) → **0 bloquant(s)**,
5 alerte(s) restantes, 0 dette de forme (contre 12 alertes + 1 dette de forme avant mon
passage).

## PASS / FAIL par contrôle, fiche par fiche

| Fiche | 1 Fraîcheur | 2 Concordance | 3 Honnêteté hypothèse | 4 Pertinence | 5 Sévérité | 6 Ton | 7 Source vivante |
|---|---|---|---|---|---|---|---|
| `fermeture\|DE-Sachsen…Sturmschaeden` (Malerweg Bastei) | PASS (verif du jour) | PASS | n/a | PASS | PASS | PASS | PASS — source `eilmeldung-waldsperrung` vérifiée en direct, périmètre confirmé identique |
| `fermeture\|Ille-et-Vilaine-Dinard…` | FAIL→corrigé | PASS | n/a | PASS | PASS | PASS | PASS — page FFRandonnée 35 revérifiée, inchangée |
| `fermeture\|Ille-et-Vilaine-Saint-Briac…` | FAIL→corrigé | PASS | n/a | PASS | PASS | PASS | PASS — idem |
| `fermeture\|Loire-Atlantique-Piriac…` | FAIL→corrigé | PASS | n/a | PASS | PASS | PASS | PASS — idem |
| `incendie\|Ariege-Bordes-Uchentein…` | PASS (verif du jour) | PASS | n/a | PASS | PASS | PASS | PASS — arrêté du 31/08 accessible (PDF 3,5 Mo récupéré) |
| `incendie\|Drome-Justin-Die…` | PASS (verif du jour) | PASS | PASS (dit explicitement « rattachement affaibli ») | PASS | PASS | PASS | PASS — page mairie-die.fr vivante, texte conforme |
| `incendie\|FR-34-11-Puilaurens-Axat…` | PASS | PASS | n/a | PASS | PASS | PASS | n/a (MOYENNE) |
| `incendie\|FR-84-26-07-LesVans-Malbosc…` | PASS | PASS | n/a | PASS | PASS | PASS | n/a (MOYENNE) |
| `incendie\|HautesAlpes-BoisNoir…` | PASS (verif du jour) | PASS | n/a | PASS | PASS | PASS | PASS — page ville-argentiere.fr vivante, texte conforme |
| `incendie\|Pyrenees-Atlantiques-Etsaut…` | FAIL(artefact)→corrigé | PASS | n/a | PASS | PASS | PASS | PASS — dernière source du 10/09 récente |
| `risque-feu\|FR-Landes-Gironde…` | FAIL(artefact)→corrigé | PASS | n/a | PASS | PASS | PASS | PASS — communiqué gironde.gouv.fr du 08/09 |
| `risque-feu\|PO-66…` | PASS (verif du jour) | PASS | PASS | PASS | PASS | PASS | PASS — titrespresse.com vivant, article du 03/09 conforme |
| `risque-feu\|ES-CANARIAS…` | PASS | PASS | n/a | PASS | PASS | FAIL→corrigé | n/a (MOYENNE) |

## Corrections appliquées (dans `livrables/alertes/*.md`)

1. **`fermeture|Ille-et-Vilaine-Dinard|GR34-Port-Vicomte-Port-Bernard|2026-04-20`** — source
   FFRandonnée 35 revérifiée en direct (toujours affichée à l'identique, aucune mention de
   réouverture) ; `verif:` passé au 2026-09-11, `statut:` mis à jour, MAJ 11/09 versée en
   « Zone (détails) ».
2. **`fermeture|Ille-et-Vilaine-Saint-Briac-sur-Mer|GR34-Petite-Salinette-Grande-Salinette|2026-02-09`**
   — même correction, même source revérifiée vivante et inchangée.
3. **`fermeture|Loire-Atlantique-Piriac-sur-Mer|GR34-Pointe-du-Castelli|2026-02-22`** — même
   correction, article FFRandonnée national revérifié vivant et inchangé.
4. **`incendie|FR-34-11-Puilaurens-Axat|feu-150ha-Camperie|2026-09-04`** — `validite:`
   réécrite (information constante, d'après le `statut:` déjà versé) pour lever
   l'ambiguïté « depuis le 08/09 » lue comme échéance : « surveillance active maintenue
   jusqu'à nouvel ordre, aucune levée annoncée à ce jour ».
5. **`incendie|FR-84-26-07-LesVans-Malbosc|feu-50ha|2026-09-03`** — même correction :
   « surveillance en cours jusqu'à nouvel ordre » ajouté d'après le `statut:`.
6. **`incendie|Pyrenees-Atlantiques-Etsaut|feu-pas-ourtasse-gr10-evacuation|2026-09-02`** —
   même correction : « secteur toujours strictement interdit … jusqu'à nouvel ordre ».
7. **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** — même
   correction sur le volet Landes : « toujours en ORANGE jusqu'à nouvel ordre ».
8. **`risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`**
   — jargon de veille retiré de « Zone (détails) » : « non extraite en autonome » →
   « contenu dynamique non consultable ». Aucune perte de fait.

### Constat technique (hors périmètre fiches, signalé pour le mainteneur de l'outillage)

Sur 4, 5 et 6 ci-dessus, la première correction (ajout de « jusqu'à nouvel ordre » sur une
ligne de continuation du champ `validite:`) n'a *pas* suffi à faire disparaître le constat
de l'audit : `site/build_site.py::load_alertes()` ne charge que la **première ligne
physique** d'un champ frontmatter replié sur plusieurs lignes — les lignes de continuation
(indentées) sont perdues pour `audit_qualite.py` (et potentiellement pour tout autre
consommateur de `c["validite"]`). Contournement appliqué ici : regrouper ces trois champs
`validite:` sur une seule ligne physique, comme le sont déjà `Ariège` et `FR-Landes-Gironde`.
Cela n'entre pas dans mon périmètre de correction (c'est du code, pas une fiche) mais mérite
un correctif dans `build_site.py` : d'autres fiches du dossier ont un `validite:` replié sur
plusieurs lignes (ex. `HautesAlpes-BoisNoir`) et échappent donc, sans le savoir, au contrôle
n°3 de l'audit (échéance passée).

## Actions laissées à l'agent de veille (constats non corrigibles dans mon périmètre)

Les 5 fiches suivantes restent signalées « alerte rouge appuyée sur une source vieillissante »
par `audit_qualite.py` (contrôle déterministe sur l'âge de la date la plus récente citée en
`source:`). Vérification faite aujourd'hui (fetch direct de la source primaire de chacune) :
toutes sont **vivantes et conformes** au texte de la fiche, aucune n'annonce de levée. Le
défaut de fraîcheur de la donnée SOURCE (pas de la vérification, qui est du jour) tient au
fait que ce sont des arrêtés/Allgemeinverfügung sans échéance calendaire, activement
revérifiés sans qu'aucun texte plus récent n'existe pour l'instant. Ce n'est pas un signe de
péremption de l'alerte, et la règle des 14 jours (hypothèses non tranchées) ne s'applique
PAS ici : ce sont des FAITS confirmés par un acte publié, pas des hypothèses « à confirmer ».
Aucune dégradation recommandée. Action laissée au prochain passage : continuer la recherche
CIBLÉE d'un texte plus récent (reconduction, levée) sur chacune :
- `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`
  (source du 26/08, 16 j)
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` (source du 31/08, 11 j)
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` (source du 21/08, 21 j)
- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` (source du
  24/08, 18 j)
- `risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26` (source du 03/09,
  cité 28/08 dans le classement massif par massif ; statut des 7 massifs hors
  Corbières/Roussillon toujours non tranché — piste déjà ouverte en `statut:`)

## Fiches contrôlées : bilan

13 fiches contrôlées (les 12 « À traiter » + 1 « Dette de forme » de l'audit du jour).
8 corrections appliquées et vérifiées par un nouveau build + audit. 5 constats laissés à la
veille, aucun bloquant, aucune fiche clôturée ou dégradée d'autorité (règle des 14 jours non
applicable à aucune des fiches vues aujourd'hui).
