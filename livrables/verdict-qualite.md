# Verdict qualité du registre — 2026-09-01

Agent Vérificateur Qualité, distinct de l'agent de veille dont le run du jour a mis à
jour `livrables/alertes/` (~35 fiches touchées, dont Gard-30 clôturée, Aude-11 changée,
Drôme-Omblèze changée, Haute-Savoie Vuache clôturée, Savoie-Planay-Pralognan changée,
Malerweg Bastei-Rathen changée). Aucune des 13 fiches contrôlées ci-dessous n'a été
rédigée par moi, y compris les 4 corrigées aujourd'hui malgré un `verif:` du jour même
(Savoie-Planay-Pralognan, Aude-11, HautesAlpes-BoisNoir, Alberes-66) : je les contrôle,
je ne relis pas mon propre travail.

Périmètre : les 13 constats de `livrables/audit-qualite.md`, régénéré en tout début de
passage par `python3 site/audit_qualite.py --ecrire` (0 bloquant, 13 alertes), portant
sur 13 fiches distinctes (un constat par fiche). Aucune autre fiche du registre
(102 fichiers, 73 actives) n'a été ouverte ni touchée.

## Corrections appliquées (périmètre : information constante, source déjà citée)

1. **`incendie|Savoie-Planay-Pralognan|RD915-refuges-Vanoise|2026-07-07`** —
   « validité expirée » signalée par l'audit (échéance lue au 08/08/2026, désormais
   passée). **Faux positif d'outillage, pas un décrochage réel** : `validite:`
   s'étalait sur 6 lignes physiques ; `parse_alerte()` (site/build_site.py) ne charge
   que la première ligne d'un champ de front-matter, donc l'audit ne voyait que
   « RD915 en circulation normale depuis le 08/08 » — une date de *reprise*, pas une
   échéance — et ratait la vraie donnée en cours, le chantier anti-chute de blocs
   jusqu'au 18/09/2026 et les gardiennages de refuges (08/09, 30/08, 19/09), tous
   situés sur les lignes 2 à 6, jamais lues. Recollé en une seule ligne physique,
   sans changer un mot de fond. Contrôle 3 → PASS.
2. **`risque-feu|Aude-11|fermeture-5-massifs-saison|2026-07-03`** — même mécanisme :
   « validité expirée au 03/07/2026 » signalée, alors que 03/07 est la date de
   *début* de la fermeture des quatre massifs (Fontfroide, Crémade, Clape,
   Lézignanaise), citée sur la première ligne du champ ; la vraie échéance en cours
   (île Sainte-Lucie jusqu'au 15/09, Ribaute jusqu'à levée d'arrêté) était sur les
   lignes 2 et 3, non lues par le parseur. Recollé en une seule ligne, réordonné pour
   mettre en tête ce qui reste actif. Aucun fait ajouté ni retiré : la fiche
   elle-même documentait déjà, dans « Portion concernée » et `statut:`, que les
   quatre massifs sont traités comme rouverts faute de prolongation. Contrôle 3 →
   PASS.
3. **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`**
   — CONCORDANCE INTERNE (contrôle 2) FAIL : « Portion concernée » s'arrêtait au
   24/08 alors que `statut:` porte une vérification du 01/09 sans rien de nouveau
   (« INCHANGÉ »). Ajouté en fin de « Portion concernée » : « Vérifié à nouveau le
   01/09/2026 (…) : aucun communiqué plus récent que celui du 24/08/2026, situation
   inchangée. » Fait déjà établi par `statut:`, simplement rendu visible au lecteur.
   Contrôle 2 → PASS.
4. **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** — même défaut
   (Portion arrêtée au 24/08, statut à jour au 01/09). Complété : « Vérifié à
   nouveau le 24/08/2026 puis le 01/09/2026 (…) ; le communiqué préfectoral du
   27/08/2026 place toujours les Albères parmi les massifs en vigilance rouge. »
   Contrôle 2 → PASS.

Après ces 4 corrections : `python3 site/build_site.py` rend **OK (QA passée)**
(73 actives, 29 clôturées, registre 624 091 car., 102 fichiers) ; `python3
site/audit_qualite.py --ecrire` ne signale plus aucun constat sur ces 4 fiches
(9 constats restants, tous hors périmètre, voir ci-dessous ; 0 bloquant avant et
après).

### Réserve sur `verif_faits.py`

`python3 site/verif_faits.py HEAD` signale 2 fiches sur les 4 avec des « nombres
inventés » : `01, 09` sur HautesAlpes-BoisNoir et `01, 27` sur Alberes-66. Vérifié un
par un : ce sont les jetons de la date `01/09/2026` que je viens d'ajouter à
« Portion concernée » (nécessaire pour corriger le contrôle 2, ci-dessus), plus `27`
pour Alberes-66, qui reprend le communiqué du 27/08 déjà cité dans `statut:` et dans
« Source ». Le script ne compare que les trois sections publiques entre elles ;
une date qui n'existait jusqu'ici que dans `statut:` (invisible sur le site) et que
je fais remonter dans une section publique se lit donc comme « nouvelle » à ses yeux,
alors qu'elle est déjà un fait établi de la même fiche, pas une invention. Aucun
nombre n'a en réalité disparu ni été inventé sur le fond. Signalé pour information,
pas un blocage : ce script est pensé pour les réécritures de style, pas pour ce type
de correction qui doit précisément faire remonter une date de `statut:` vers le
public.

## Signalé, non corrigé — nécessite une source nouvelle (prochain passage de veille)

1. **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** —
   FRAÎCHEUR (contrôle 1) FAIL : vérifiée il y a 4 j, seuil 2 j pour une restriction
   « décidée au jour le jour ». Concordance interne bonne (Portion/statut/Zone datent
   tous du 28/08). **Action attendue** : revérifier samaria.gr et crete.gov.gr avant
   la prochaine étape couverte sur ce secteur. (Déjà signalée au 31/08, toujours non
   couverte.)
2. **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** —
   SOURCE VIVANTE (contrôle 7) : source la plus récente du champ `source:` datée du
   18/08 (14 j, il s'agit de l'arrêté anti-feu, pas de la fermeture GR®10 elle-même).
   Vérifié en direct aujourd'hui : la page de l'Office de tourisme des Pyrénées
   Ariégeoises (MAJ 11/08, déviation Bassiès/Saleix) et l'article France 3 Occitanie
   du 04/08 (fermeture Ayès↔Cap des Lauses) sont tous deux **en ligne et confirment
   mot pour mot** le contenu cité. La règle des 14 jours ne s'applique pas : la
   sévérité HAUTE repose sur la fermeture de sentier (3 sources indépendantes
   convergentes), pas sur l'arrêté-feu resté sans 5e reconduction. **Recommandation
   inchangée depuis le 31/08** : chercher spécifiquement le sort de cet arrêté
   (ariege.gouv.fr) au prochain passage sur l'Ariège.
3. **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — SOURCE VIVANTE
   (contrôle 7) : source la plus récente datée du 21/08 (11 j). Vérifié en direct
   aujourd'hui : mairie-die.fr et ici.fr (21/08, 15h40) sont tous deux **en ligne et
   confirment** l'arrêté préfectoral du 21/08/2026 (interdiction Justin/Laup/Solaure
   pour risque de chutes de pierres/arbres, sans échéance calendaire, subordonnée à
   une étude de risque). Ce n'est pas une hypothèse « à confirmer » : c'est un texte
   réglementaire déjà confirmé par 2 sources indépendantes le 28/08. Pas de
   dégradation à appliquer. **Action attendue** : au prochain passage, seulement
   vérifier qu'aucune levée n'a été publiée depuis.
4. **`incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`** —
   FRAÎCHEUR FAIL : vérifiée il y a 13 j, seuil 12 j (MOYENNE). Concordance interne
   bonne, validité « jusqu'à nouvel ordre ». **Action attendue** : recontrôler
   l'arrêté municipal de Plévenon.
5. **`incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16`** —
   FRAÎCHEUR FAIL : vérifiée il y a 13 j, seuil 12 j (MOYENNE). **Action attendue** :
   recontrôler cairngorms.co.uk / firescotland.gov.uk pour le secteur Abernethy
   (Ryvoan Trail, Lodge Trail toujours fermés à la dernière donnée).
6. **`reroutage|GR21-Loges-Bénouville|glissement-fermeture|2026-02-17`** — FRAÎCHEUR
   FAIL : vérifiée il y a 13 j, seuil 12 j (MOYENNE). **Action attendue** :
   rechercher une source 2026 postérieure à février (aucune trouvée à ce jour selon
   `statut:`).
7. **`reroutage|GR34-Finistère|fermetures-érosion-2026|2026-S1`** — FRAÎCHEUR FAIL :
   vérifiée il y a 13 j, seuil 12 j (MOYENNE). **Action attendue** : recontrôler
   finistere.ffrandonnee.fr pour les 15+ sites listés.
8. **`reroutage|GR34-rade-de-Brest|nouveau-tracé-officiel|2026-05-28`** — FRAÎCHEUR
   FAIL : vérifiée il y a 13 j, seuil 12 j (MOYENNE). Reroutage pérenne, faible
   enjeu. **Action attendue** : simple revérification de routine.
9. **`reroutage|Pierrefiques-76|déviation|2025-05-18`** — FRAÎCHEUR FAIL : vérifiée
   il y a 13 j, seuil 12 j (MOYENNE). Validité `jusqu'au 18/09/2026` toujours
   ouverte. **Action attendue** : simple revérification de routine.

## Contrôle 7 (SOURCE VIVANTE) — vérification directe des sources rouges

Sources vérifiées en direct aujourd'hui pour les 2 fiches HAUTE signalées par
l'audit sur ce contrôle :
- Ariège (Bordes-Uchentein) : Office de tourisme des Pyrénées Ariégeoises (MAJ
  11/08, déviation Saleix) — **PASS**, page accessible, contenu confirmé mot pour
  mot. France 3 Occitanie (04/08, fermeture Ayès↔Cap des Lauses) — **PASS**,
  accessible, contenu confirmé.
- Drôme (Justin-Die) : mairie-die.fr (arrêté du 21/08 abrogeant celui du 24/07) —
  **PASS**, accessible, contenu confirmé. ici.fr (21/08 15h40) — **PASS**,
  accessible, contenu confirmé mot pour mot (« La préfecture de la Drôme a
  reconduit un arrêté préfectoral ce vendredi 21 août »).

Aucune source morte trouvée sous une alerte rouge aujourd'hui.

## Défaut d'outillage relevé (hors périmètre de correction, signalé pour le pilote)

Confirmation du défaut déjà noté le 31/08 : `site/build_site.py::parse_alerte()`
n'associe un champ de front-matter (`validite:`, `statut:`…) qu'à sa **première**
ligne physique ; toute ligne de continuation indentée est silencieusement ignorée,
y compris par `audit_qualite.py` qui réutilise `load_alertes()`. Deux nouvelles
victimes directes aujourd'hui (Savoie-Planay-Pralognan, Aude-11), corrigées en
recollant `validite:` sur une seule ligne. Recommandation inchangée : soit le
parseur apprenne les lignes de continuation indentées, soit la consigne d'écriture
impose une seule ligne physique pour `validite:`/`statut:`. Tant que ce n'est pas
fait, chaque nouvelle fiche qui enrichit `validite:` sur plusieurs lignes reproduira
ce faux positif.

## Bilan des 7 contrôles sur les 13 fiches auditées

| Contrôle | Résultat |
|---|---|
| 1. Fraîcheur | FAIL sur 7 fiches (Creta-Samaria, CapFrehel, Cairngorms, GR21-Loges, GR34-Finistère, GR34-rade-de-Brest, Pierrefiques-76) — signalées, source nouvelle requise |
| 2. Concordance interne | 2 FAIL corrigés (HautesAlpes-BoisNoir, Alberes-66) ; PASS sur les 11 autres |
| 3. Honnêteté sur l'incertain | PASS sur les 13 — aucune restriction présentée comme probable sans le dire |
| 4. Pertinence | PASS sur les 13 |
| 5. Sévérité juste | PASS sur les 13 |
| 6. Ton | PASS sur les 13 (aucun jargon de veille détecté en section publique) |
| 7. Source vivante | 2 FAIL d'audit vérifiés en direct → PASS (Ariège, Drôme) ; sources encore fraîches sur les 2 autres HAUTE du lot |
| 3 bis (validité) | 2 faux positifs d'outillage corrigés (Savoie-Planay-Pralognan, Aude-11) → PASS |

13 fiches contrôlées, 4 corrections appliquées, 9 constats FRAÎCHEUR/SOURCE VIVANTE
laissés au prochain passage de veille (2 vérifiés PASS en direct malgré le signal
d'audit, 7 nécessitent une source nouvelle). Build : **OK (QA passée)**.
