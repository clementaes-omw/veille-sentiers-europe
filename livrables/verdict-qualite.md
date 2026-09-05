# Verdict qualité — 2026-09-05

Agent Vérificateur Qualité, distinct de l'agent de veille qui a produit le run du jour
(4 nouvelles alertes, plusieurs fiches mises à jour, 2 alias `ALIAS_ZONE` ajoutés à
`site/build_site.py`). Je n'ai écrit aucune des fiches contrôlées ci-dessous : audit
indépendant.

Périmètre : les 7 constats de `livrables/audit-qualite.md` (généré le jour même par
`python3 site/audit_qualite.py --ecrire`, 0 bloquant / 7 alerte / 0 info sur 80 fiches
actives). Aucune fiche hors de cette liste n'a été touchée. Aucune recherche web nouvelle
n'a été effectuée (hors périmètre de ce rôle sur ce passage) : le contrôle 7 (source
vivante) s'appuie sur ce que les fiches documentent déjà, pas sur un re-fetch des URLs.

**7 fiches contrôlées.** 2 corrections appliquées (réécritures à information constante,
aucun fait créé). 0 dégradation de sévérité appliquée (les deux cas où l'audit
soupçonnait une hypothèse vieillissante reposent en fait sur un fait de terrain ou un
arrêté en vigueur, pas sur un « à confirmer » — la règle des 14 jours ne se déclenche
donc pas). 4 actions laissées à l'agent de veille (3 fiches MOYENNE hors cadence du jour
à revérifier avec une source fraîche, plus le remplacement d'une source rouge tombée en
404, déjà noté par la veille elle-même).

---

## 1. `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | PASS — vérifiée le jour même (05/09) |
| Concordance interne | PASS (constat de l'audit : faux positif, voir ci-dessous) |
| Honnêteté sur ce qu'on ne sait pas | PASS |
| Pertinence | PASS |
| Sévérité | PASS |
| Ton | PASS |
| Source vivante | non re-testée (pas de recherche web sur ce passage) |

- **Faux positif de l'audit déterministe** : le script signale un écart de 11 jours entre
  la date la plus récente antérieure à aujourd'hui citée dans « Portion concernée »
  (25/08, début du chantier héliporté) et celle citée dans `statut:` (05/09, date de la
  revérification). Le script prend la première comme un signe de gel du texte. Ce n'est
  pas le cas ici : la date du 25/08 est la date de DÉBUT d'une opération en cours, encore
  valide au 05/09 (« jusqu'au 18/09/2026 environ », date future donc ignorée par l'outil
  qui ne compare qu'aux dates passées). L'entrée `MAJ 05/09` de « Zone (détails) » («
  re-vérification complète… le périmètre reste inchangé ») dit exactement ce que dit la
  « Portion concernée » (Amselsee rouvert, bas de l'Amselgrund fermé, chantier héliporté
  du Gamrig en cours). Aucun décrochage réel : le texte affiché correspond à l'état
  constaté aujourd'hui. Aucune correction nécessaire.

---

## 2. `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | PASS — vérifiée le jour même (05/09) |
| Concordance interne | FAIL (champ `validite:`) → **corrigé** |
| Honnêteté sur ce qu'on ne sait pas | PASS |
| Pertinence | PASS |
| Sévérité | PASS — pas de dégradation |
| Ton | PASS |
| Source vivante | non re-testée (pas de recherche web sur ce passage) |

- **Sévérité** : l'audit signale une source rouge datée du 18/08 (18 j). Vérifié : la
  sévérité HAUTE de cette fiche repose sur un fait de terrain confirmé et sourcé trois
  fois indépendamment (France 3 Occitanie 04/08, ruralites2024.fr 03/08, radiocouserans.fr
  02/08) — la fermeture du GR®10 entre l'étang d'Ayès et le Cap des Lauses pour risque de
  chutes de pierres — et non sur un « à confirmer »/« probable » concernant l'arrêté
  d'interdiction du feu, qui est un second sujet, distinct, déjà traité en toute
  transparence (« aucune 5e reconduction ni levée… publiée à ce jour »). La règle des 14
  jours ne s'applique donc pas : **aucune dégradation recommandée**, conforme à ce que
  `statut:` affirme déjà lui-même.
- **Concordance interne** : le champ `validite:` (non affiché sur le site mais partie du
  front-matter) affirmait encore « 6 jours de silence au 30/08 » sur l'échéance du 24/08,
  alors que `statut:` porte la donnée à jour (« 12 jours de silence » à la vérification du
  05/09). Réécriture à information constante : la mise à jour était déjà arrivée dans
  `statut:` sans être répercutée dans `validite:`. **Corrigé.**

---

## 3. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | PASS — vérifiée le 04/09 (veille de la revue), verif à jour |
| Concordance interne | PASS |
| Honnêteté sur ce qu'on ne sait pas | PASS |
| Pertinence | PASS |
| Sévérité | PASS — pas de dégradation |
| Ton | PASS (champs publics) |
| Source vivante | non re-testée (pas de recherche web sur ce passage) |

- **Sévérité** : l'audit signale une source rouge datée du 21/08 (15 j). Vérifié : cette
  source (ici.fr, 21/08, citant la préfecture de la Drôme) rapporte un arrêté préfectoral
  officiel toujours en vigueur, sans échéance calendaire (la levée dépend d'une étude de
  risque en cours), confirmé et daté précisément par une seconde source (mairie-die.fr,
  28/08, citant le texte de l'arrêté et sa clause d'abrogation). C'est un acte
  administratif en vigueur, pas une hypothèse « à confirmer »/« probable » : la règle des
  14 jours ne se déclenche pas. **Aucune dégradation recommandée**, conforme à `statut:`.
- **Observation, non corrigée** : le champ `itin:` porte depuis le 03/08 la mention que le
  rattachement au GR®9/GR®93 est « affaibli », la FFRandonnée Drôme (source faisant
  autorité) ne listant aucune modification d'itinéraire pour ce secteur et suggérant que
  le sentier réellement concerné serait le GR®95 (hors périmètre du référentiel). Le
  moteur de badges du site (`itin_badges`) extrait néanmoins « GR®9 » et « GR®93 » de ce
  texte et les affiche comme itinéraires impactés, sans transmettre le doute au lecteur.
  Trancher quel sigle badge afficher demande un jugement sur un point que la fiche
  elle-même documente encore comme non confirmé : je le signale plutôt que de le corriger
  d'autorité. **Recommandation à l'agent de veille** : au prochain passage sur cette zone,
  soit confirmer/infirmer le rattachement GR®9/GR®93 (une recherche déjà tentée sans
  succès trois fois), soit reformuler `itin:` sans citer GR®9/GR®93 tant que ce n'est pas
  tranché, pour que les badges publics n'affichent pas des sentiers dont l'atteinte reste
  douteuse.

---

## 4. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | PASS — vérifiée le jour même (05/09) |
| Concordance interne | FAIL mineur (écart d'un jour) → **corrigé** |
| Honnêteté sur ce qu'on ne sait pas | PASS |
| Pertinence | PASS |
| Sévérité | PASS — pas de dégradation |
| Ton | PASS |
| Source vivante | FAIL sur une source déjà identifiée comme morte (voir ci-dessous) |

- **Sévérité** : l'audit signale une source rouge datée du 24/08 (12 j). Vérifié :
  `statut:` justifie explicitement le maintien HAUTE sur l'arrêté municipal du 15/08/2026,
  toujours en vigueur (confirmé le 02/09 par une lecture directe de la page de la mairie
  de L'Argentière-la-Bessée), pas sur une hypothèse non tranchée. La règle des 14 jours ne
  s'applique pas ici. **Aucune dégradation recommandée.**
- **Concordance interne** : « Portion concernée » se terminait sur « Vérifié à nouveau le
  04/09/2026 » alors que `verif:` et `statut:` de cette même fiche portent la date du
  05/09 (jour de la revérification qui a produit ce fichier). Écart d'un jour, réécriture
  à information constante (le constat rapporté — aucun changement — reste identique).
  **Corrigé.**
- **Source vivante — à traiter au prochain run** : `statut:` note déjà que
  `paysdesecrins.com/vigileance-feu-en-cours/`, citée deux fois en source, renvoie
  désormais une erreur 404. C'est un FAIL de contrôle 7 sur une alerte rouge : le lecteur
  ne peut plus vérifier ce point par lui-même. La veille l'a déjà identifié et propose
  `cc-paysdesecrins.fr` en remplacement ; je ne peux pas retrouver ni valider une URL de
  remplacement sans recherche web, donc je ne touche pas à la section Source. **Action
  laissée à l'agent de veille** : remplacer la source mortes par une source vivante
  équivalente au prochain passage sur cette zone.

---

## 5. `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | FAIL — vérifiée il y a 13 j (seuil 12 j, MOYENNE) |
| Concordance interne | PASS |
| Honnêteté sur ce qu'on ne sait pas | PASS |
| Pertinence | PASS (rien n'indique une réouverture ni une caducité) |
| Sévérité | PASS |
| Ton | PASS |
| Source vivante | non testée (zone hors périmètre du jour) |

- Zone hors cadence T2 aujourd'hui, donc non re-vérifiable par moi (pas de recherche
  web). « Portion concernée », `statut:` et « Zone (détails) » racontent la même chose
  (Panoramaweg et Rosi-Rotkehlchen-Weg fermés jusqu'à nouvel ordre, réouvertures
  partielles du 31/07 déjà actées) : pas de décrochage, pas de jargon dans les champs
  publics. **À traiter au prochain run** : revérifier `oppenau.de/…/wegsperrungen.html`
  (et sa page « Aufhebung ») pour une éventuelle évolution depuis le 31/07/2026.

## 6. `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | FAIL — vérifiée il y a 14 j (seuil 12 j, MOYENNE) |
| Concordance interne | PASS |
| Honnêteté sur ce qu'on ne sait pas | PASS |
| Pertinence | PASS |
| Sévérité | PASS (dégradée à raison le 22/08, cohérente aujourd'hui) |
| Ton | PASS |
| Source vivante | non testée (zone hors périmètre du jour) |

- Zone hors cadence du jour. Fiche interne cohérente : les 80 % rouverts et les parcelles
  encore fermées sont décrits de façon identique dans `statut:`, « Portion concernée » et
  « Alternative ». **À traiter au prochain run** : revérifier
  `seine-et-marne.gouv.fr/Actualites/…` pour une actualisation du détail cartographique
  des parcelles brûlées, resté non publié depuis le 22/08.

## 7. `incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | FAIL — vérifiée il y a 17 j (seuil 12 j, MOYENNE) |
| Concordance interne | PASS |
| Honnêteté sur ce qu'on ne sait pas | PASS |
| Pertinence | PASS |
| Sévérité | PASS |
| Ton | PASS |
| Source vivante | non testée (zone hors périmètre du jour) |

- Zone hors cadence du jour, fiche récente (créée le 12/08, un seul passage depuis).
  Cohérence interne correcte, rien à corriger. **À traiter au prochain run** :
  revérifier la déviation FFRandonnée Côtes-d'Armor et l'arrêté municipal du 15/07/2026
  (aucune échéance annoncée à ce stade — vérifier qu'il n'a pas été levé depuis).

---

## Corrections appliquées

- `livrables/alertes/incendie--ariege-bordes-uchentein--gr10-ferme-esbintz-valier--2026-07-10.md` :
  `validite:` recalé sur l'état du 05/09 (12 j de silence, au lieu de 6 j au 30/08).
- `livrables/alertes/incendie--hautesalpes-boisnoir--gr54a-ferme-argentiere-freissinieres--2026-07-19.md` :
  « Portion concernée » recalée du 04/09 au 05/09 (date de la revérification qui a produit
  ce fichier).

## Actions laissées à l'agent de veille

1. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` —
   remplacer la source `paysdesecrins.com/vigileance-feu-en-cours/` (404) par
   `cc-paysdesecrins.fr` ou une source vivante équivalente.
2. `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28` —
   revérifier avec une source fraîche (13 j sans nouvelle).
3. `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` —
   revérifier avec une source fraîche (14 j sans nouvelle), en particulier le détail
   cartographique des parcelles encore fermées.
4. `incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15` — revérifier avec
   une source fraîche (17 j sans nouvelle).
5. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — trancher le rattachement au
   GR®9/GR®93 (probablement GR®95) pour que les badges d'itinéraire publics reflètent
   un fait confirmé plutôt qu'une hypothèse affaiblie depuis le 03/08.

## Vérification finale

- `python3 site/build_site.py` → `OK (QA passée)` (80 actives, 29 clôturées, 48 digests ;
  registre 666145 car. / 109 fichiers).
- `python3 site/audit_qualite.py` → 0 bloquant, 7 alerte(s) (inchangé en nombre : les 7
  constats sont soit des faux positifs documentés ci-dessus, soit des dégradations
  couvertes par l'exception de la règle des 14 jours, soit des zones hors cadence dont la
  fraîcheur ne peut être rétablie que par une nouvelle recherche — donc non « corrigibles »
  au sens de ce rôle). Aucun nouveau bloquant introduit par les corrections appliquées.
