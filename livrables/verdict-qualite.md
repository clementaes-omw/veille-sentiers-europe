# Verdict qualité — 2026-09-07

Vérificateur distinct de l'agent de veille qui a produit ce run (5 agents parallèles,
44 fichiers touchés dans `livrables/alertes/`, dont une nouvelle alerte). Périmètre : les
9 fiches citées par `livrables/audit-qualite.md` régénéré ce jour (0 bloquant, 9 alertes,
2 infos). Les 2 infos (jargon « recherche ciblée » sur Ariège-Bordes-Uchentein et
ES-CENTRO-Guadalajara-LaMierla) ont été revérifiées : le terme n'existe plus que dans le
champ `statut:` (invisible), pas dans « Zone (détails) » — déjà réglées avant mon passage,
conformément à la consigne. Aucune autre fiche du dossier n'a été ouverte ni modifiée.

## Fiches contrôlées (9)

1. `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01` — HAUTE
2. `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — MOYENNE
3. `fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04` — MOYENNE
4. `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` — HAUTE
5. `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28` — MOYENNE
6. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — HAUTE
7. `incendie|FR-84-26-07-LesVans-Malbosc|feu-50ha|2026-09-03` — MOYENNE
8. `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12` — MOYENNE
9. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` — HAUTE

## PASS / FAIL par contrôle

### Groupe A — 4 alertes rouges, « source vieillie » signalée par l'audit (#1, #4, #6, #9)

Pour chacune, l'audit déterministe signale une source vieillie (12 à 20 j) sous une alerte
rouge et suggère « retrouver une publication récente ou dégrader la sévérité ». Diagnostic
demandé : la « Portion concernée » de ces 4 fiches est-elle encore adossée à une formule
« à confirmer »/« probable »/« non localisé » (→ règle des 14 jours, dégradation MOYENNE),
ou décrit-elle déjà un fait établi indépendant de l'acte administratif manquant (→ pas de
dégradation) ?

| # | Fraîcheur | Concordance interne | Honnêteté | Pertinence | Sévérité juste | Ton | Source vivante |
|---|---|---|---|---|---|---|---|
| Malerweg | FAIL (audit, voir note) | PASS | PASS | PASS | PASS | PASS | PASS |
| Ariège Esbintz-Valier | FAIL (audit, voir note) | PASS | PASS | PASS | PASS | PASS | PASS |
| Drôme Justin | FAIL (audit, voir note) | PASS | PASS | PASS | PASS | PASS | PASS |
| Bois Noir | FAIL (audit, voir note) | PASS | PASS | PASS | PASS | PASS | PASS |

Détail :
- **Diagnostic fait établi vs hypothèse** : dans les 4 cas, la « Portion concernée » n'énonce
  ni « à confirmer », ni « probable », ni « non localisé », ni « recoupement en cours ». Elle
  décrit un fait sourcé indépendamment de la question du texte manquant : Malerweg
  (Allgemeinverfügung en vigueur « bis auf Widerruf », jusqu'à révocation, pas d'échéance à
  renouveler), Ariège (fermeture de terrain — chutes de pierres — confirmée par 3 sources de
  presse citant l'ONF, distincte de l'arrêté feu dont la 5e reconduction manque), Drôme
  (arrêté préfectoral du 21/08 en vigueur pour risque de chutes de pierres/arbres, motif
  désormais distinct de l'incendie), Bois Noir (arrêté municipal du 15/08 en vigueur, motif
  chutes de pierres/arbres/éboulements). **La règle des 14 jours ne s'applique à aucune des
  4 : aucune dégradation appliquée.** Pour Ariège, Drôme et Bois Noir, ce diagnostic et cette
  décision étaient déjà documentés en clair dans `statut:` par le run du jour lui-même — je
  les confirme, je ne les répète pas comme nouveaux. Pour Malerweg, la fiche ne portait pas
  encore cette justification explicite : je l'ai ajoutée à `statut:` (voir Corrections).
- **Fraîcheur (constat de l'audit)** : le signal reste affiché volontairement — il pousse la
  veille à rechercher un texte plus récent (arrêté renouvelé, communiqué) au prochain passage
  sur ces 4 zones. Ce n'est pas un défaut de rédaction de la fiche, donc pas une correction
  qui m'incombe : reste en actions laissées à l'agent de veille, sans effet sur la sévérité.
- **Honnêteté** : les 4 fiches disent explicitement au lecteur ce qui n'est pas publié
  (« aucune 5e reconduction ni levée publiée à ce jour », « aucune date de levée n'est
  communiquée », etc.) plutôt que de le présenter comme tranché. PASS.
- **Source vivante (contrôle 7)** : vérifiée en direct par fetch des 4 sources qui portent le
  fait central de chaque fiche — toutes répondent et confirment le texte de la fiche :
  `nationalpark-saechsische-schweiz.de/warnungen/eilmeldung-waldsperrung` (Amselsee/Amselgrund
  toujours dans l'état décrit), `pyreneesfm.com/departement/ariege` (dernier article connu sur
  l'interdiction du feu reste celui du 10/08, aucune 5e reconduction publiée — cohérent avec le
  constat de la fiche), `mairie-die.fr/acces-interdit-forets-justin-laup-solaure/` (arrêté du
  21/08 confirmé, sans échéance), `ville-argentiere.fr/feu-bois-noir-informations` (arrêté du
  15/08 confirmé, sans date de levée annoncée). PASS pour les 4.

### Groupe B — 2 validités passées, corrigées (#3, #7)

| # | Fraîcheur | Concordance interne | Honnêteté | Pertinence | Sévérité juste | Ton | Source vivante |
|---|---|---|---|---|---|---|---|
| Montasio (via ferrata Amalia) | PASS | PASS | FAIL→corrigé | PASS | PASS | PASS | n/a (MOYENNE) |
| Les Vans-Malbosc | PASS | PASS | FAIL→corrigé | PASS | PASS | PASS | n/a (MOYENNE) |

- **Montasio** : `validite:` disait « fermée depuis le 04/09/2026, aucune échéance de
  réouverture annoncée » — le tour de phrase, sans marqueur d'ouverture reconnu, faisait lire
  le 04/09 comme une échéance dépassée alors que la fermeture est indéfinie (le CAI n'a fixé
  aucune date). Réécrit à information constante : « fermée depuis le 04/09/2026, jusqu'à
  nouvel ordre : le CAI n'annonce aucune échéance de réouverture ». Aucune fiche à clôturer,
  aucune source nouvelle nécessaire.
- **Les Vans-Malbosc** : `validite:` avait été rédigée sur deux lignes de frontmatter ; le
  générateur ne lit que la première ligne d'un champ multi-ligne du frontmatter (limite
  connue de `site/build_site.py`, hors de mon périmètre de correction), ce qui coupait la
  phrase juste avant la date du 06/09 et faisait lire le 04/09 comme la seule échéance,
  passée. Fusionné sur une seule ligne, à information constante (la fiche a déjà été
  revérifiée aujourd'hui même par l'agent de veille) : « foyer des Vans contenu depuis le
  04/09 mi-journée ; foyer de Malbosc actif mais en nette amélioration au 06/09/2026
  (110 pompiers contre 250 au pic, camping du Moulin de Gournier rouvert) ; aucune date de
  fixation ni d'extinction confirmée à ce jour. » Je n'ai PAS clôturé l'alerte : le foyer de
  Malbosc reste actif sans preuve d'extinction, conformément à la « Zone (détails) » déjà à
  jour.

### Groupe C — 3 fraîcheurs en retard, hors périmètre du run (#2, #5, #8)

| # | Fraîcheur | Concordance interne | Honnêteté | Pertinence | Sévérité juste | Ton |
|---|---|---|---|---|---|---|
| Creta-Samaria | **FAIL** (3 j, seuil 2 j) | PASS | PASS | PASS | PASS | PASS |
| Schwarzwald-Oppenau | **FAIL** (15 j, seuil 12 j) | PASS | PASS | PASS | PASS | PASS |
| Fontainebleau | **FAIL** (16 j, seuil 12 j) | PASS | PASS | PASS | PASS | PASS |

Les 3 fiches restent honnêtes sur ce qu'elles savent (Creta-Samaria dit explicitement « à
vérifier sur samaria.gr avant l'étape » ; Oppenau et Fontainebleau ne prétendent rien de plus
récent que leur dernière source citée) et aucune « Portion concernée » n'est décrochée du
`statut:`/de la « Zone (détails) » de la même fiche. Il n'y a rien à reformuler à information
constante : ce qui manque, c'est une vérification neuve sur des zones hors du périmètre de ce
run (Crète T2/T3, Forêt-Noire et Île-de-France T3). Ce n'est pas mon rôle de produire cette
source — inscrit ci-dessous comme actions laissées à l'agent de veille.

## Corrections appliquées

- `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01` :
  ajout à `statut:` (champ interne) de la justification explicite du maintien HAUTE (fait
  établi — Allgemeinverfügung en vigueur — vs hypothèse non tranchée). Aucun fait ajouté ni
  supprimé.
- `fermeture|IT-Dolomites-Friuli-Montasio|via-ferrata-amalia-frana-tratti-9-10-11|2026-09-04` :
  `validite:` réécrite pour porter un marqueur d'échéance ouverte (« jusqu'à nouvel ordre »)
  au lieu de laisser lire le 04/09 comme une date dépassée. Information constante.
- `incendie|FR-84-26-07-LesVans-Malbosc|feu-50ha|2026-09-03` : `validite:` fusionnée sur une
  ligne et mise en cohérence avec la « Zone (détails) » du jour (foyer de Malbosc actif, pas
  de date de fixation/extinction confirmée). Alerte maintenue ACTIVE, pas clôturée.

Après ces corrections : `python3 site/build_site.py` → « OK (QA passée) » (80 actives, 30
clôturées, 110 fichiers) ; `python3 site/audit_qualite.py --ecrire` → 7 constats restants,
**0 bloquant** (les 2 constats de validité expirée ont disparu ; les 7 constats de fraîcheur
des groupes A et C restent volontairement affichés, voir ci-dessus).

## Actions laissées à l'agent de veille (à traiter au prochain run)

1. **Malerweg** — retrouver une source postérieure au 01/09 sur le bas de l'Amselgrund/
   Ziegenrücken, ou confirmer explicitement qu'aucune n'est parue. Sans effet sur la
   sévérité HAUTE (fait établi, pas hypothèse).
2. **Creta-Samaria** — FAIL fraîcheur (3 j, seuil 2 j, restriction décidée au jour le jour) :
   revérifier samaria.gr et crete.gov.gr pour le statut du jour.
3. **Ariège Esbintz-Valier** — poursuivre la recherche ciblée d'une 5e reconduction ou d'une
   levée de l'arrêté feu (14 j de silence au 07/09) ; sans effet sur la sévérité HAUTE, déjà
   justifiée par la fermeture de terrain (chutes de pierres).
4. **Schwarzwald-Oppenau** — FAIL fraîcheur (15 j, seuil 12 j) : revérifier oppenau.de
   (« Wegsperrungen » et « Aufhebung Wegsperrungen ») pour confirmer maintien ou levée.
5. **Drôme Justin** — rechercher une mise à jour de l'étude de risque ONF ou une date de
   levée ; sévérité HAUTE déjà justifiée par l'arrêté du 21/08 en vigueur.
6. **Fontainebleau** — FAIL fraîcheur (16 j, seuil 12 j) : revérifier seine-et-marne.gouv.fr
   pour le détail cartographique des parcelles encore fermées et leur recoupement GR®.
7. **Bois Noir** — remplacer si possible la source `paysdesecrins.com/vigileance-feu-en-cours/`
   (toujours 404 au 07/09, deux pistes de remplacement testées sans succès par la veille) ;
   rechercher une mise à jour sur la levée éventuelle de l'arrêté municipal du 15/08.

Aucune suppression, aucune clôture et aucune dégradation de sévérité appliquée : les
9 fiches restent ACTIVES, les 4 alertes rouges restent HAUTE (justifiées par un fait établi,
pas par une hypothèse non tranchée), les 5 alertes orange restent MOYENNE.
