# Verdict qualité — 2026-09-08

Vérificateur distinct des 5 agents de veille parallèles qui ont produit le run du jour. Je
n'ai écrit aucune des fiches auditées. Périmètre : les **12 fiches** citées par
`livrables/audit-qualite.md` régénéré ce jour à l'ouverture (0 bloquant, 11 alertes,
3 infos). Aucune autre fiche du dossier n'a été ouverte ni modifiée.

## ⚠️ Constat transversal prioritaire — bug de parsing du frontmatter multi-ligne

En creusant deux des « validités expirées » signalées par l'audit, j'ai trouvé la cause
réelle : `parse_alerte()` dans `site/build_site.py` (partagé par `audit_qualite.py`) ne lit
que la **première ligne physique** d'un champ de frontmatter. Une valeur écrite sur deux
lignes selon la convention `champ: texte…\n  suite du texte` — utilisée dans une bonne partie
du registre pour `validite:`/`statut:` — perd silencieusement tout ce qui suit la première
ligne pour la lecture programmatique (le rendu du site n'en souffre pas : `validite` n'est
jamais affiché, et `statut` n'est testé que pour la sous-chaîne `CLÔTURÉ`, toujours en tête).
Conséquence concrète aujourd'hui : `VS-Orsieres-ValFerret` et `FR-84-26-07-LesVans-Malbosc`
étaient signalées « validité expirée le 29/07 » et « le 04/09 » alors que la suite, coupée à
la lecture, portait respectivement une validité Suisse Rando jusqu'au 31/01/2027 et la
mention que le foyer de Malbosc n'était pas encore éteint au 07/09. **Ce n'est pas un cas
isolé** : un balayage du dossier montre des dizaines de fichiers avec ce même motif de
continuation, et le risque n'est pas seulement le faux positif observé ici — un champ
`validite:` dont l'échéance réelle tomberait sur la ligne de continuation resterait, lui,
invisible à l'audit (faux négatif). J'ai retrouvé la même remarque, avec le même luxe de
précaution (« hors de mon périmètre de correction »), dans le verdict du 2026-09-07 : le
correctif appliqué ce jour-là (fusionner le champ sur une ligne) a été repris sans le savoir
par la veille du jour, qui a réécrit `validite:` en deux lignes sur ces mêmes fiches — le
palliatif fiche par fiche ne tient pas dans la durée. **Je n'ai pas touché au générateur**
(hors de mon rôle de vérificateur de contenu) : j'ai seulement refusionné les deux champs
concernés sur une ligne, à information constante, pour lever le faux signal du jour. Le
correctif structurel (faire lire `parse_alerte()` sur les lignes indentées de continuation,
comme un scalaire replié YAML) reste à faire une fois pour toutes dans `site/build_site.py` —
je le signale au pilote plutôt que de le coder moi-même.

De même, l'alerte rouge PO-66 était signalée sur une source « vieille de 28/08 » alors que la
fiche cite en réalité une source du 03/09 : celle-ci est datée en toutes lettres (« ce jeudi
3 septembre ») dans la section Source, un format que la regex de dates de l'audit ne
reconnaît pas (elle ne lit que les dates chiffrées). Pas un défaut de la fiche : à corriger
dans `audit_qualite.py` si on veut fiabiliser ce contrôle particulier.

## Fiches contrôlées (12)

1. `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01` — HAUTE
2. `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — MOYENNE
3. `fermeture|VS-Orsieres-ValFerret|Saleinaz-cabane-eboulement|2026-07-29` — MOYENNE
4. `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — HAUTE
5. `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28` — MOYENNE
6. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — HAUTE
7. `incendie|FR-84-26-07-LesVans-Malbosc|feu-50ha|2026-09-03` — MOYENNE
8. `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` — MOYENNE
9. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` — HAUTE
10. `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17` — MOYENNE
11. `risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26` — HAUTE
12. `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — MOYENNE

## PASS / FAIL par contrôle

### Groupe A — 4 alertes rouges « source vieillie », établies par un fait, pas une hypothèse (#1, #6, #9, #11)

Diagnostic demandé par la consigne : la fermeture repose-t-elle encore sur « à confirmer »/
« probable », ou sur un acte/fait sourcé indépendamment ? Dans les 4 cas la « Portion
concernée » ne porte aucun marqueur d'hypothèse et cite un texte daté et en vigueur :
Malerweg (Allgemeinverfügung « bis auf Widerruf », sans échéance à renouveler), Drôme Justin
(arrêté préfectoral du 21/08, motif désormais distinct de l'incendie — chutes de pierres),
Bois Noir (arrêté municipal du 15/08, chutes de pierres/arbres/éboulements), PO-66 (classement
officiel du 03/09 sur Corbières/Roussillon). **La règle des 14 jours ne s'applique à aucune
des 4 : aucune dégradation appliquée.** Ce diagnostic était déjà écrit en clair dans `statut:`
par la veille du jour elle-même pour Drôme, Bois Noir et PO-66 — je le confirme, sans le
répéter comme nouveau.

| # | Fraîcheur | Concordance | Honnêteté | Pertinence | Sévérité | Ton | Source vivante |
|---|---|---|---|---|---|---|---|
| Malerweg | FAIL (audit, attendu) | PASS | PASS | PASS | PASS | PASS | PASS (200) |
| Drôme Justin | FAIL (audit, attendu) | PASS→corrigé | PASS | PASS | PASS | PASS | PASS (200) |
| Bois Noir | FAIL (audit, attendu) | PASS | PASS | PASS | PASS | FAIL→corrigé | PASS (200) |
| PO-66 | FAIL (audit, faux positif regex) | PASS | PASS | PASS | PASS | PASS | PASS (200) |

- **Bois Noir** : « Portion concernée » contenait le jargon interne banni « recherche ciblée »
  — le build QA **échouait déjà** avant mon passage (`[ton] jargon de veille « recherche
  ciblee » dans portion`, bloquant, site NON généré). Corrigé (voir Corrections). C'est le
  seul vrai bloquant technique du jour.
- **Source vivante** : les 4 sources qui portent le fait central de chaque fiche répondent en
  HTTP 200 et portent le contenu cité : `nationalpark-saechsische-schweiz.de/warnungen/
  eilmeldung-waldsperrung`, `mairie-die.fr/acces-interdit-forets-justin-laup-solaure/`,
  `ville-argentiere.fr/feu-bois-noir-informations`, `titrespresse.com/…/feu-pyrenees-
  orientales`.
- **Fraîcheur** : le signal audit reste affiché volontairement (recherche d'une publication
  plus récente à retenter au prochain passage) ; ce n'est pas un défaut de rédaction, donc pas
  une correction qui m'incombe.

### Groupe B — décrochage Portion/statut, corrigé (#4, #10)

| # | Fraîcheur | Concordance | Honnêteté | Pertinence | Sévérité | Ton |
|---|---|---|---|---|---|---|
| Ariège Esbintz-Valier | PASS | FAIL→corrigé | PASS | PASS | PASS | PASS |
| Esterel-Tanneron (06) | PASS | FAIL→corrigé | FAIL→corrigé | PASS | PASS | FAIL→corrigé |

- **Ariège** : « Portion concernée » citait l'arrêté du 31/08 sans dire qu'il venait d'être
  retrouvé le 08/09 sur le site de la mairie (absent des relectures directes de
  ariege.gouv.fr) — écart de 8 j entre la date citée et la date de vérification. La fermeture
  du GR®10 est un fait établi par ce texte propre, indépendant de l'arrêté feu (dont la
  5e reconduction manque toujours, sans effet sur cette fermeture-ci) : pas la règle des
  14 jours, une simple mise en concordance. Corrigé.
- **Esterel-Tanneron** : restriction **journalière** (décidée jour par jour), silence des
  sources depuis le 31/08 (8 j). Contrairement au Groupe A, un acte ancien ne vaut *rien* ici
  sur le statut du jour même : la « Portion concernée » présentait le 31/08 sans le dire au
  lecteur → FAIL honnêteté, corrigé en ajoutant explicitement l'absence de confirmation
  depuis et le renvoi à la préfecture avant de partir. Jargon « recherche ciblée » retiré de
  « Zone (détails) ».

### Groupe C — jargon seul, corrigé (#12)

`Alberes-66` : « Zone (détails) » contenait « recherche ciblée sur les deux communes non
tranchées » (jargon de veille, INFO à l'audit, non bloquant). Reformulé pour le lecteur.
Aucun autre contrôle en défaut sur cette fiche (les 4 arrêtés communaux distincts — Argelès
levé, Sorède/Villelongue/Cerbère actifs — sont tous datés et sourcés, la concordance est déjà
bonne).

### Groupe D — validités « expirées », faux positifs de parsing, corrigés sans changer un fait (#3, #7)

| # | Fraîcheur | Concordance | Honnêteté | Pertinence | Sévérité | Ton |
|---|---|---|---|---|---|---|
| VS-Orsières Saleinaz | PASS | PASS | PASS | PASS | PASS | PASS |
| Les Vans-Malbosc | PASS | PASS | PASS | PASS | PASS | PASS |

Voir le constat transversal ci-dessus : `validite:` était coupée par le parseur au premier
retour à la ligne. Le contenu réel (validité Suisse Rando jusqu'au 31/01/2027 ; foyer de
Malbosc fixé le 07/09 mais pas encore éteint) n'appelait ni clôture ni réécriture de fond —
seule la mise en forme frontmatter était en cause. Fusionné sur une ligne, aucun fait
modifié.

### Groupe E — fraîcheurs en retard, hors de mon périmètre de correction (#2, #5, #8)

| # | Fraîcheur | Concordance | Honnêteté | Pertinence | Sévérité | Ton |
|---|---|---|---|---|---|---|
| Creta-Samaria | **FAIL** (4 j, seuil 2 j) | PASS | PASS | PASS | PASS | PASS |
| Schwarzwald-Oppenau | **FAIL** (16 j, seuil 12 j) | PASS | PASS | PASS | PASS | PASS |
| Fontainebleau | **FAIL** (17 j, seuil 12 j) | PASS | PASS | PASS | PASS | PASS |

Les 3 fiches restent honnêtes sur ce qu'elles savent et aucune « Portion concernée » n'est
décrochée de son propre `statut:`/« Zone (détails) ». Rien à reformuler à information
constante : il manque une vérification neuve sur des zones hors périmètre du run du jour
(Crète, Forêt-Noire, Fontainebleau/IDF). Ce n'est pas mon rôle de produire cette source —
inscrit ci-dessous.

## Corrections appliquées

- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` : jargon
  « recherche ciblée » retiré de « Portion concernée » (bloquant le build) et de « Zone
  (détails) », reformulé pour le lecteur. Aucun fait changé.
- `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17` : « Portion
  concernée » complétée pour dire explicitement au lecteur qu'aucune publication n'est
  parue depuis le 31/08 (8 j) et qu'il doit se renseigner avant de partir ; jargon
  « recherche ciblée » retiré de « Zone (détails) ».
- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` : jargon « recherche ciblée »
  retiré de « Zone (détails) ».
- `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` : « Portion
  concernée » précisée pour dire que l'arrêté du 31/08 a été retrouvé le 08/09 sur le site de
  la mairie, absent jusque-là des relectures directes de ariege.gouv.fr (concordance avec
  `statut:`).
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` : « Portion concernée » — date de
  vérification remise à jour (04/09→08/09) et ajout de la confirmation indirecte par
  l'exclusion du massif de l'ouverture de la chasse au 13/09 (déjà connue en « Zone
  (détails) »).
- `fermeture|VS-Orsieres-ValFerret|Saleinaz-cabane-eboulement|2026-07-29` : `validite:`
  refusionnée sur une ligne (faux positif de parsing, aucun fait changé).
- `incendie|FR-84-26-07-LesVans-Malbosc|feu-50ha|2026-09-03` : `validite:` refusionnée sur
  une ligne (faux positif de parsing, aucun fait changé). Alerte maintenue ACTIVE, pas
  clôturée : le foyer de Malbosc n'est pas déclaré éteint.

Après ces corrections : `python3 site/build_site.py` → **OK (QA passée)** (84 actives,
30 clôturées, 114 fichiers) ; `python3 site/audit_qualite.py --ecrire` → **7 constats
restants, 0 bloquant** (contre 14 constats, 0 bloquant au départ — le build lui-même était en
échec avant ma correction du jargon Bois Noir). Les 7 constats restants sont volontairement
laissés affichés (Groupes A et E ci-dessus) : ils poussent la veille à re-chercher une source
plus récente, ce n'est pas un défaut de rédaction des fiches.

## Actions laissées à l'agent de veille (à traiter au prochain run)

1. **Corriger le générateur** (`site/build_site.py`, fonction `parse_alerte`) : les champs de
   frontmatter multi-lignes (`validite:`, `statut:`…) doivent accumuler leurs lignes de
   continuation indentées au lieu de s'arrêter à la première ligne. Ce n'est pas une tâche de
   veille de contenu, mais elle conditionne la fiabilité de l'audit qualité lui-même
   (faux positifs constatés ce jour, risque de faux négatif non exclu sur une autre fiche).
   Accessoirement, `audit_qualite.py` (`dates_citees`) ne reconnaît que les dates chiffrées :
   la source PO-66 du « jeudi 3 septembre » n'a pas été comptée.
2. **Malerweg** — retrouver une source postérieure au 26/08 sur le bas de l'Amselgrund/
   Ziegenrücken, ou confirmer explicitement qu'aucune n'est parue. Sans effet sur la sévérité
   HAUTE (fait établi, pas hypothèse).
3. **Creta-Samaria** — FAIL fraîcheur (4 j, seuil 2 j, restriction décidée au jour le jour) :
   revérifier samaria.gr et crete.gov.gr pour le statut du jour.
4. **Ariège Esbintz-Valier** — poursuivre la recherche d'une 5e reconduction ou d'une levée de
   l'arrêté feu séparé (15 j de silence au 08/09) ; sans effet sur la sévérité HAUTE, déjà
   justifiée par la fermeture de terrain (arrêté du 31/08, chutes de pierres).
5. **Schwarzwald-Oppenau** — FAIL fraîcheur (16 j, seuil 12 j) : revérifier oppenau.de
   (« Wegsperrungen » et « Aufhebung Wegsperrungen »).
6. **Drôme Justin** — rechercher une mise à jour de l'étude de risque ONF ou une date de
   levée ; sévérité HAUTE déjà justifiée par l'arrêté du 21/08 en vigueur.
7. **Fontainebleau** — FAIL fraîcheur (17 j, seuil 12 j) : revérifier seine-et-marne.gouv.fr
   pour le détail cartographique des parcelles encore fermées.
8. **Bois Noir** — remplacer si possible la source `paysdesecrins.com/vigileance-feu-en-
   cours/` (toujours 404) ; rechercher une mise à jour sur la levée éventuelle de l'arrêté
   municipal du 15/08.
9. **PO-66** — les 7 massifs hors Corbières/Roussillon restent non tranchés depuis le
   communiqué du 27/08 ; poursuivre le recoupement au prochain passage.
10. **Esterel-Tanneron (06)** — le classement du jour est inconnu depuis 8 jours (restriction
    journalière) : revérifier presseagence.fr/alpes-maritimes.gouv.fr.

Aucune suppression, aucune clôture et aucune dégradation de sévérité appliquée : les
12 fiches restent ACTIVES, les 4 alertes rouges restent HAUTE (justifiées par un fait établi,
pas par une hypothèse non tranchée), les 8 alertes orange restent MOYENNE.
