# Verdict qualité du registre — 2026-08-27

Agent Vérificateur Qualité, distinct de l'agent de veille du jour : aucune des fiches
contrôlées ci-dessous n'a été rédigée par cet agent, la condition d'indépendance est
respectée.

Périmètre de travail : les 10 constats de `livrables/audit-qualite.md` (généré le jour
même par `python3 site/audit_qualite.py --ecrire`, aucun relancement nécessaire) — 1
bloquant, 8 alertes, 1 dette de forme. Aucune autre fiche du registre (98 fichiers) n'a
été ouverte ni touchée.

## Fiches contrôlées (10)

1. `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — BLOQUANT
2. `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`
3. `fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06`
4. `incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16`
5. `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`
6. `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`
7. `risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`
8. `risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`
9. `risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01`
10. `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`

## PASS / FAIL par contrôle

| Contrôle | Résultat |
|---|---|
| 1. FRAÎCHEUR | FAIL sur 7/10 (#1 à #5, #7, #8) — toutes hors périmètre géographique du run d'aujourd'hui, nécessitent une source nouvelle. PASS sur #6, #9, #10 (revérifiées ce jour). |
| 2. CONCORDANCE INTERNE | FAIL initial sur #9 (Gard-30) et #4 (ES-CENTRO) — corrigés ci-dessous, PASS après correction. PASS sur les 8 autres. |
| 3. HONNÊTETÉ SUR CE QU'ON NE SAIT PAS | PASS sur les 10 : aucune fiche ne présente une hypothèse comme un fait acquis (Albères et Esterel-Tanneron documentent explicitement l'absence de communiqué récent ; Mallorca et Réunion documentent explicitement ce qui reste à confirmer). |
| 4. PERTINENCE | PASS sur les 10 : rien, dans les éléments déjà écrits, ne justifie une clôture. |
| 5. SÉVÉRITÉ JUSTE | PASS sur les 2 alertes rouges (#6, #9) : leur HAUTE repose sur des textes datés et non expirés (arrêtés municipaux pour Albères, classement préfectoral officiel pour le Gard), pas sur un « à confirmer ». La règle des 14 jours ne s'applique à aucune des deux, faute d'hypothèse en attente. #10 a déjà été correctement dégradée HAUTE→MOYENNE par la veille le 22/08 en application de cette règle. Pas de recommandation de mouvement de sévérité sur les 7 autres (MOYENNE déjà). |
| 6. TON | FAIL initial sur #10 (jargon « recherche ciblée » dans Zone (détails)) — corrigé, PASS après correction. PASS sur les 9 autres. |
| 7. SOURCE VIVANTE (rouges #6, #9) | PASS. Gard-30 : 3 URL gard.gouv.fr testées, 200 OK. Albères-66 : arrêté PDF, rnnmassane.fr, mapetiterando.fr vivants (200) ; ouillade.eu répond 403 (probable protection anti-bot du site, testé avec deux user-agents) mais n'est pas la source qui fonde la sévérité — celle-ci repose sur les deux arrêtés municipaux, vérifiés vivants. |

## Corrections appliquées (dans le périmètre, à information constante)

- **`risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01`** — « Portion concernée »
  complétée d'une phrase indiquant qu'aucun classement plus récent que celui du 18/08
  n'a été publié (neuf jours de silence au 27/08), information déjà présente dans
  « Zone (détails) » et le champ `statut:` mais absente du texte affiché. Aucun fait
  ajouté ou retiré.
- **`risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`** —
  reformulation d'une phrase de « Zone (détails) » contenant le jargon de veille
  « recherche ciblée » (remplacée par « une source jusqu'ici non consultée »), sans
  changer le fait rapporté.
- **`incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16`** —
  « Portion concernée » ne décrivait que l'épisode initial (34 localités évacuées, 14
  confinées, ~32 000 ha au 23/07) sans mentionner la stabilisation de l'incendie
  (maîtrisé au 04/08, ~33 000 ha au bilan final, évacuations progressivement levées),
  pourtant déjà connue via `statut:` et `validite:`. Réécrite en conséquence ; une
  entrée datée « MAJ 04/08 » a été ajoutée à la chronologie de « Zone (détails) » pour
  que l'information ne reste plus seulement dans un champ invisible du site.

Après ces trois corrections : `python3 site/build_site.py` rend « OK (QA passée) »
(73 actives, 25 clôturées, 98 fichiers) et `python3 site/audit_qualite.py` ne signale
plus aucun de ces trois constats (ni le bloquant ni la dette de forme touchés par cette
session) ; aucune boucle supplémentaire n'a été nécessaire.

## Actions laissées à l'agent de veille (nécessitent une source nouvelle)

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** (BLOQUANT) —
  vérifiée il y a 13 jours pour une restriction décidée au jour le jour (seuil 2 jours).
  Zone hors périmètre géographique du run d'aujourd'hui (Grèce, lot T2 du vendredi) :
  non touchée. Le digest du jour (`livrables/digest_2026-08-27.md`) mentionne déjà ce
  constat en tête, conformément à la consigne de mention obligatoire d'un bloquant non
  traité. Action attendue au prochain passage sur la zone : revérifier samaria.gr /
  samaria-tickets.necca.gov.gr.
- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — vérifiée il y a 21
  jours (seuil 12 j). Action : consulter directement la carte ONF interactive plutôt
  qu'une recherche texte, comme déjà noté en `statut:`.
- **`fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06`** — jamais
  revérifiée depuis sa détection (8 j). Action : confirmer auprès du comité
  FFRandonnée 22 si la déviation et la fermeture sont toujours en place.
- **`incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16`** —
  vérifiée il y a 13 jours (seuil 12 j). Action : chercher une source postérieure au
  04/08 confirmant le maintien de la maîtrise du feu, et trancher enfin le recoupement
  avec un itinéraire GR® référencé (toujours en [HYPOTHÈSE]).
- **`refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`** — vérifiée il y a
  20 jours (seuil 12 j), échéance annoncée du 15/08 dépassée sans confirmation de
  réouverture. Action : relire caminsdepedra.conselldemallorca.es pour trancher.
- **`risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`**
  — vérifiée il y a 13 jours (seuil 12 j). Action : mise à jour sur les 5 îles
  (INFOGRAN Gran Canaria, sentiers de pèlerinage Candelaria à Tenerife, La Palma/La
  Gomera/El Hierro).
- **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** —
  vérifiée il y a 13 jours (seuil 12 j). Action : statut de vigilance Gironde/Landes à
  date, et confirmation (toujours en attente depuis le 24/07) du statut du tronçon
  GR®8 à Biscarrosse/Gastes/Sainte-Eulalie-en-Born.
- **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** — non bloquant : la
  sévérité HAUTE repose sur deux arrêtés municipaux datés et non expirés (Sorède
  jusqu'au 13/09, Argelès jusqu'à nouvel ordre), tous deux vérifiés vivants aujourd'hui ;
  la règle des 14 jours sur les hypothèses non tranchées ne s'applique pas ici, faute
  d'« à confirmer » en attente. Recommandation non impérative : continuer à chercher une
  publication de presse plus récente que le 29/07 pour documenter l'état du terrain
  au-delà des seuls textes réglementaires.

Aucune suppression, aucune clôture, aucune dégradation ou remontée de sévérité n'a été
appliquée d'autorité par cet agent.
