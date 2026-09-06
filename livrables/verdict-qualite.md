# Verdict qualité — 2026-09-06

Vérificateur distinct de l'agent de veille du jour. Périmètre : les 6 fiches citées par
`livrables/audit-qualite.md` (régénéré ce jour, 0 bloquant, 6 avertissements). Aucune autre
fiche du dossier n'a été ouverte ni modifiée.

## Fiches contrôlées (6)

1. `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`
2. `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`
3. `incendie|DE-Schwarzwald-Oppenau|Panoramaweg-Rosi-Rotkehlchenweg-fermes|2026-07-28`
4. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`
5. `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`
6. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`

## PASS / FAIL par contrôle

### 1, 2, 4, 6 — zones revérifiées aujourd'hui (verif: 2026-09-06)

| # | Fraîcheur | Concordance interne | Honnêteté | Pertinence | Sévérité juste | Ton | Source vivante |
|---|---|---|---|---|---|---|---|
| Malerweg | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Ariège Esbintz-Valier | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Drôme Justin | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Bois Noir | PASS | PASS | PASS (FAIL mineur corrigé) | PASS | PASS | PASS | PASS* |

Détail :
- **Fraîcheur** : les 4 fiches portent `verif: 2026-09-06`, à jour du jour même. PASS.
- **Concordance interne** : dans les 4 cas, « Portion concernée » reflète exactement l'état
  décrit par `statut:` et « Zone (détails) » (fermeture réelle en vigueur, dernière source
  citée). Aucune divergence trouvée.
- **Honnêteté sur ce qu'on ne sait pas** : les 4 fiches disent explicitement au lecteur ce
  qui n'est pas publié plutôt que de le présenter comme probable — Malerweg (« bis auf
  Widerruf, sans date de fin fixe »), Ariège (« n'a fait l'objet d'aucune 5e reconduction ni
  levée publiée à ce jour »), Drôme (« aucune date de levée n'est précisée, la sortie
  dépendant d'une étude de risque en cours »), Bois Noir (« mesure … en attendant l'ensemble
  des avis des autorités compétentes … sans date annoncée »). PASS.
- **Sévérité juste (contrôle 5, appliqué avec prudence)** : dans les 4 cas, la HAUTE ne
  repose PAS sur une hypothèse non tranchée logée dans la « Portion concernée » — elle
  repose sur un fait établi et sourcé indépendamment de la question de l'arrêté feu/de la
  date de son texte : fermeture de terrain confirmée par 3 sources de presse citant l'ONF
  pour l'Ariège (chutes de pierres), arrêté préfectoral du 21/08 en vigueur (motif chutes de
  pierres/arbres, distinct de l'incendie) pour la Drôme, arrêté municipal du 15/08 en
  vigueur pour Bois Noir, Allgemeinverfügung toujours en vigueur avec chantier héliporté en
  cours pour le Malerweg. La règle des 14 jours (§ DURÉE DE VIE D'UNE HYPOTHÈSE) ne
  s'applique à aucune des 4 : leur « Portion concernée » n'est adossée ni à « à confirmer »,
  ni à « probable », ni à « non localisé » — elle énonce des faits. Aucune dégradation
  appliquée. Recommandation : maintenir HAUTE pour les 4, l'audit re-signalera tant que la
  source datée la plus récente vieillit, ce qui est le comportement voulu (pousser la veille
  à rechercher un texte plus récent), pas un défaut de la fiche elle-même.
- **Ton** : aucun jargon de veille (« ce run », « réindexation », etc.) trouvé dans
  « Portion concernée » ou « Alternative » des 4 fiches ; le build le confirme (aucune
  violation `[ton]`).
- **Source vivante (contrôle 7)** : vérifié en direct par fetch des sources portant le fait
  central de chaque fiche :
  - Malerweg : `nationalpark-saechsische-schweiz.de/warnungen/eilmeldung-waldsperrung`
    répond, confirme le bas de l'Amselgrund fermé et l'Amselsee mentionné dans le texte
    (nuance : la page que le fetch a rendue affiche encore l'Amselsee comme fermé alors que
    la fiche le dit rouvert depuis le 01/09 sur la foi de la FAQ dédiée — à surveiller au
    prochain passage, sans être un FAIL : deux pages du même site peuvent être à des états
    de mise à jour différents, la fiche cite sa source précise pour ce fait).
  - Ariège : `pyreneesfm.com/…-interdictions-prolongees-face-au-risque-d-i` (18/08) répond et
    confirme la 4e reconduction jusqu'au 24/08 telle que citée.
  - Drôme : `mairie-die.fr/acces-interdit-forets-justin-laup-solaure/` répond et confirme
    l'arrêté du 21/08, l'absence d'échéance calendaire, et l'abrogation de l'arrêté du 24/07,
    conformes au texte de la fiche.
  - Bois Noir : `ville-argentiere.fr/feu-bois-noir-informations` répond et confirme l'arrêté
    municipal du 15/08 et l'absence de date de levée. En revanche
    `paysdesecrins.com/vigileance-feu-en-cours/` (citée deux fois en Source, et à l'appui de
    la réouverture des parcours 22/23 dans « Portion concernée ») renvoie une 404 confirmée
    par fetch direct. Ce point était déjà identifié dans `statut:` par le run du jour lui-même
    (« Source à corriger … au prochain passage ») — je ne l'ai pas re-signalé comme nouveau,
    je le fais remonter formellement ci-dessous. Il n'invalide pas la sévérité HAUTE : le
    fait qui la justifie (arrêté municipal du 15/08 sur le cœur de massif) est sourcé
    ailleurs et vérifié vivant.

**Correction appliquée** : `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`
— le champ `statut:` (invisible sur le site) portait une phrase dupliquée par accident
(« renvoie désormais une erreur 404 » répétée sur deux passages consécutifs, laissant une
phrase orpheline « désormais une erreur 404. »). Fusionné en une seule phrase, aucune
information supprimée ni ajoutée. C'est un nettoyage de forme sur un champ interne, pas une
correction de fond.

### 3, 5 — zones hors périmètre du jour (Allemagne / Île-de-France, T3, non escaladées)

| # | Fraîcheur | Concordance interne | Honnêteté | Pertinence | Sévérité juste | Ton | Source vivante |
|---|---|---|---|---|---|---|---|
| Schwarzwald-Oppenau | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |
| Fontainebleau | **FAIL** | PASS | PASS | PASS | PASS | PASS | n/a (MOYENNE) |

- **Fraîcheur** : Oppenau `verif: 2026-08-23` (14 jours), Fontainebleau `verif: 2026-08-22`
  (15 jours) ; seuil 12 jours pour une sévérité MOYENNE. FAIL sur les deux, confirmé par
  l'audit déterministe.
- Le reste des contrôles est PASS : dans les deux fiches, « Portion concernée » correspond
  exactement à `statut:` et « Zone (détails) », le texte dit clairement ce qui n'est pas
  encore publié (détail cartographique fin pour Fontainebleau, absence de déviation balisée
  pour Oppenau) plutôt que de le présenter comme tranché, aucune des deux ne s'appuie sur
  « à confirmer »/« probable » dans la Portion concernée, aucun jargon de veille dans les
  champs publics, sévérité MOYENNE cohérente avec des fermetures locales/partielles sans
  blocage d'étape.
- **Correction que j'aurais pu faire moi-même** : aucune trouvée. Rien à reformuler, aucune
  « Portion concernée » décrochée de `statut:`/« Zone (détails) », pas de `validite:`
  échue à réécrire d'après une source déjà citée.
- **Ce qui manque relève d'une source nouvelle** (confirmer si la fermeture résiduelle est
  toujours en vigueur ou levée) : hors de mon périmètre. Inscrit ci-dessous comme action
  laissée à l'agent de veille ; ces deux zones entrent en escalade au prochain run qui les
  couvre (Allemagne / Île-de-France).

## Corrections appliquées

- `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` : fusion
  d'une phrase dupliquée dans `statut:` (champ interne, aucun fait modifié).

Après cette correction : `python3 site/build_site.py` → « OK (QA passée) » (79 actives, 30
clôturées, 109 fichiers) ; `python3 site/audit_qualite.py` → 6 constats, **0 bloquant**
(inchangé : la correction ne portait pas sur les critères de l'audit déterministe).

## Actions laissées à l'agent de veille (à traiter au prochain run)

1. **Malerweg** (`fermeture|DE-Sachsen-…|2026-08-01`) — retrouver une source postérieure au
   01/09 sur le bas de l'Amselgrund/Ziegenrücken, ou confirmer explicitement qu'aucune n'est
   parue. Pas de dégradation requise : la Portion concernée repose sur un fait (fermeture
   active, chantier héliporté en cours), pas sur une hypothèse.
2. **Ariège Esbintz-Valier** (`incendie|Ariege-Bordes-Uchentein|…`) — poursuivre la
   recherche ciblée d'une 5e reconduction/levée de l'arrêté feu (13 jours de silence au
   06/09) ; sans effet sur la sévérité HAUTE, déjà justifiée par la fermeture de terrain.
3. **Drôme Justin** (`incendie|Drome-Justin-Die|…`) — même remarque : rechercher une mise à
   jour de l'étude de risque ONF ou une date de levée ; sévérité HAUTE déjà justifiée par
   l'arrêté du 21/08 en vigueur.
4. **Bois Noir** (`incendie|HautesAlpes-BoisNoir|…`) — remplacer la source morte
   `paysdesecrins.com/vigileance-feu-en-cours/` (404 confirmée) par `cc-paysdesecrins.fr` ou
   une source équivalente pour le détail des parcours 22/23 ; rechercher aussi une mise à
   jour sur la levée éventuelle de l'arrêté municipal du 15/08.
5. **Schwarzwald-Oppenau** (`incendie|DE-Schwarzwald-Oppenau|…`) — FAIL fraîcheur (14 j,
   seuil 12 j) : revérifier oppenau.de (pages « Wegsperrungen » et « Aufhebung
   Wegsperrungen ») pour confirmer le maintien ou la levée de la fermeture du Panoramaweg et
   du Rosi-Rotkehlchen-Weg.
6. **Fontainebleau** (`incendie|FR-IDF-Fontainebleau|…`) — FAIL fraîcheur (15 j, seuil 12 j) :
   revérifier seine-et-marne.gouv.fr pour le détail cartographique des parcelles encore
   fermées et leur recoupement avec les GR® (GR®1/2/3/11/13/655), toujours non publié au
   22/08.

Aucune suppression, aucune clôture et aucune dégradation de sévérité appliquée : les 6
fiches restent ACTIVES, les 4 alertes rouges restent HAUTE (justifiées par un fait établi,
pas par une hypothèse non tranchée), les 2 alertes orange restent MOYENNE.
