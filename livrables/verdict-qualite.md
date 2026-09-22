# Verdict qualité du registre — 2026-09-22

Agent Vérificateur Qualité, distinct de l'agent de veille du jour. Aucune des 27 fiches
listées par `livrables/audit-qualite.md` (généré le 2026-09-22, après le run du jour) n'a
été écrite par cet agent : audit mené en toute indépendance, conformément à
`agents/verificateur-alertes.md`.

**27 fiches contrôlées** (liste de travail = intégralité des constats de l'audit déterministe,
aucune autre fiche du dossier n'a été ouverte). **2 corrections appliquées**, **9 PASS motivés
sans correction**, **16 actions laissées à l'agent de veille** (nécessitent une source
nouvelle, hors périmètre de ce rôle).

## PASS / FAIL par contrôle (sur les 27 fiches examinées)

1. **FRAÎCHEUR** — 16 FAIL (revérification hors délai ou jamais revérifiée depuis
   détection) → tous signalés « à traiter au prochain run », aucun ne peut être corrigé sans
   recherche d'une source nouvelle. 11 PASS (délai respecté ou fiche revérifiée le jour même
   par l'agent de veille).
2. **CONCORDANCE INTERNE** — 2 FAIL trouvés et corrigés (Covatannaz, Savoie Planay-Pralognan :
   la « Portion concernée » citait une échéance de validité désormais dépassée sans le dire).
   25 PASS.
3. **HONNÊTETÉ SUR CE QU'ON NE SAIT PAS** — 27 PASS après corrections. Quatre fiches
   (ES-ARA-Huesca-Riglos, ES-GAL-Quiroga, Pierrefiques-76, FR-Landes-Gironde) déclarées « à
   traiter » par l'audit déterministe se sont révélées, à la lecture, déjà parfaitement
   honnêtes sur ce point : voir « Faux positifs de l'audit » ci-dessous.
4. **PERTINENCE** — 27 PASS. Aucune fiche ne présente de preuve de résolution complète qui
   justifierait une clôture (feux « contrôlés » mais pas « éteints », déviations et chantiers
   sans confirmation de fin) : aucune clôture appliquée, aucune recommandée.
5. **SÉVÉRITÉ JUSTE** — 5 alertes ROUGE/HAUTE contrôlées une à une contre la règle des 14
   jours (agent-prompt.md) : 5 PASS motivés, sévérité maintenue à raison (voir détail).
6. **TON** — 27 PASS. Aucun jargon de veille repéré dans les champs publics des fiches lues ;
   les deux fiches corrigées respectent la même exigence (zéro tiret cadratin dans les
   sections publiques, formulé pour le lecteur).
7. **SOURCE VIVANTE** — contrôlée sur les 5 alertes ROUGE (minimum exigé par le rôle) : 5
   PASS, les 5 URLs sources rouvertes et confirmées conformes au contenu de la fiche (voir
   détail).

## Corrections appliquées (périmètre : forme, à information constante)

- **`fermeture\|CH-Vaud-Sainte-Croix-Baulmes\|Gorges-Covatannaz-travaux\|2026-08-17`** — la
  validité annonçait une déviation « jusqu'au 18/09/2026 » sans qu'aucun passage postérieur
  n'ait constaté la fin des travaux ; le site affichait donc une échéance passée comme si elle
  restait à venir. Réécrit `validite:`, « Portion concernée » et `statut:` pour dire
  explicitement que l'échéance est dépassée et que la fin des travaux n'est pas confirmée,
  sans inventer ni la réouverture ni la prolongation.
- **`incendie\|Savoie-Planay-Pralognan\|RD915-refuges-Vanoise\|2026-07-07`** — même défaut :
  le chantier de créneaux horaires sur la RD915 était donné « jusqu'au 18/09/2026 » sans
  qu'un passage postérieur au 08/09 n'ait confirmé sa fin. Réécrit `validite:`, « Portion
  concernée » et `statut:` en conséquence ; noté au passage que les trois saisons de
  gardiennage de refuge citées (Grand Bec, Péclet-Polset, Col de la Vanoise) sont closes
  depuis, par calendrier normal, sans rapport avec l'incendie.

Après ces deux corrections : `python3 site/build_site.py` → **OK (QA passée)** (96 actives,
32 clôturées, 128 fichiers, aucune fiche sous le seuil d'intégrité de 45 %).
`python3 site/audit_qualite.py --ecrire` → **0 bloquant** sur l'ensemble du registre, comme
avant ce passage. Les deux fiches corrigées réapparaissent dans le rapport déterministe
(l'algorithme retient la date la plus tardive *citée* dans `validite:`, y compris quand cette
date sert désormais à dire explicitement qu'elle est dépassée et non confirmée : un faux
positif mécanique, pas une alerte de fond — voir ci-dessous). Le point réel que ce contrôle
visait (une échéance passée sous silence) est résolu sur les deux fiches.

## PASS motivés sans correction

### Alertes ROUGE fondées sur un arrêté daté (règle des 14 jours non applicable)

L'audit signale ces 5 alertes HAUTE pour une source « vieillie » (12 à 32 jours). Dans les
5 cas, la « Portion concernée » ne repose pas sur un « à confirmer »/« probable »/« non
localisé »/« recoupement en cours » (le déclencheur de la règle des 14 jours), mais sur un
acte officiel daté, republié et reconfirmé par une recherche ciblée directe le jour même
(22/09) par l'agent de veille, exactement comme le prescrit agent-prompt.md pour ce cas de
figure. Source vivante vérifiée pour chacune (voir tableau) :

- `incendie\|Ariege-Bordes-Uchentein\|GR10-ferme-Esbintz-Valier\|2026-07-10` — arrêté
  préfectoral du 31/08/2026 (Bordes-Uchentein), source PDF confirmée en ligne et conforme.
- `incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02` — arrêté préfectoral du 21/08/2026
  (relayé par mairie-die.fr), page confirmée en ligne, interdiction toujours présentée comme
  en vigueur.
- `incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19` — arrêté
  municipal du 15/08/2026 (ville-argentiere.fr), page confirmée en ligne, mesure toujours
  présentée comme active.
- `incendie\|Pyrenees-Atlantiques-Etsaut\|feu-pas-ourtasse-gr10-evacuation\|2026-09-02` —
  source à 12 jours seulement (sous le seuil de 14 j de toute façon), article du 10/09
  confirmé en ligne, accès au sol toujours donné strictement interdit.
- `fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07` — liste de référence du PNR
  Baronnies Provençales (MAJ 01/09), page confirmée en ligne, 12 communes toujours nommées
  avec arrêté daté individuel.

### Faux positifs de l'audit déterministe (contrôle 3, validité)

Ces 4 fiches sont signalées pour une « validité qui s'arrête au 18/09/2026, désormais
passé », mais l'examen montre qu'il s'agit d'un artefact du script : il retient la date la
plus tardive *citée* dans le champ `validite:`, qu'elle décrive une échéance réelle ou
simplement la date de la dernière vérification. Dans les 4 cas, le texte est déjà honnête et
à jour, sans échéance réellement dépassée passée sous silence : aucune correction nécessaire.

- `incendie\|ES-ARA-Huesca-Riglos\|...` — le 18/09 cité est la date de la dernière
  vérification, pas une échéance ; la fiche dit déjà explicitement que l'échéance réelle
  (15/09, réouverture de la route A-1603) est dépassée sans confirmation.
- `incendie\|ES-GAL-Quiroga\|...` — le 18/09 cité est la date à laquelle le feu a été
  déclaré « contrôlé », pas une échéance de fermeture.
- `reroutage\|Pierrefiques-76\|déviation\|2025-05-18` — `validite:` dit déjà noir sur blanc
  « échéance atteinte sans confirmation de réouverture ».
- `risque-feu\|FR-Landes-Gironde\|...` — le 18/09 cité est la date de la dernière
  vérification de la fiche, pas une échéance ; le niveau de vigilance en vigueur (JAUNE
  Gironde, ORANGE Landes) est suivi et daté correctement.

## Actions laissées à l'agent de veille (nécessitent une source nouvelle, hors périmètre)

Toutes en FRAÎCHEUR FAIL (contrôle 1) : la seule correction possible exige une vérification
de source que ce rôle n'est pas autorisé à faire. Zones CH-EST hors périmètre du run du jour
(rotation T2/T3, signalées explicitement par l'agent de veille) ; les autres nécessitent
simplement une lecture ciblée de la source déjà citée au prochain passage sur leur zone.

| Clé | Constat | Action attendue |
|---|---|---|
| `fermeture\|CH-EST-Frutigen\|Kander-Uferweg-impraticable\|2026-08-17` | vérifiée il y a 14 j | rechecker le CSV officiel (id 2600749) |
| `fermeture\|CH-EST-Kandersteg\|Spitze-Stei-deviation-seg-1.13\|2023-05-08` | jamais revérifiée depuis 14 j | rechecker le CSV officiel (id 2596765) |
| `fermeture\|CH-EST-Trubbach\|fermeture-deviation-seg-1.1\|2026-05-26` | vérifiée il y a 14 j | rechecker le CSV officiel (id 2596318) |
| `conditions\|IS-Hautes-Terres\|traversee-deconseillee-fimmvorduhals-glacier\|2026-08-25` | jamais revérifiée depuis 10 j | rechecker safetravel.is |
| `terrain\|IS-HautesTerres\|Fimmvorduhals-recul-glaciaire-crevasses\|2026-08` | vérifiée il y a 17 j | rechecker safetravel.is / Iceland Review. **Point de vigilance : cette fiche et la précédente (`conditions\|IS-Hautes-Terres\|...`) documentent la même situation (recul glaciaire, secteur Fimmvörðuháls) sous deux clés distinctes** ; à recouper et, le cas échéant, à fusionner au prochain passage sur la zone plutôt qu'à maintenir séparées — hors périmètre de correction de ce rôle. |
| `eboulement\|IT-Dolomites-BorcaDiCadore\|frana-passo-staulanza-route-rifugio-citta-di-fiume\|2026-09-10` | jamais revérifiée depuis 10 j | rechecker l'état de la route/du parking |
| `fermeture\|GR-E4-Creta-Samaria\|fermetures-meteo-repetees\|2026-07-16` | vérifiée il y a 4 j (seuil 2 j, décision au jour le jour) | rechecker samaria.gr |
| `fermeture\|IT-Centre-Carrara\|via-francigena-nazzano-bonascola-frana\|2024` | vérifiée il y a 17 j | rechecker la presse locale (La Voce Apuana) |
| `fermeture\|IT-DOLOMITES-Brenta\|Cima-Falkner-Bocchette-sentieri-chiusi\|2025-07` | vérifiée il y a 17 j | rechecker la page SAT |
| `fermeture\|IT-Dolomites-Pelmo\|frana-versante-nordovest-borca-di-cadore\|2026-08-10` | vérifiée il y a 17 j | rechecker la presse (il Dolomiti, La Adige) |
| `fermeture\|IT-Liguria-CinqueTerre\|SentieroVerdeAzzurro-Corniglia-Vernazza-Monterosso\|2026-09-10` | jamais revérifiée depuis 10 j | rechecker parks.it |
| `incendie\|IT-NO-Biellese-Valsessera\|Monte-Barone-...\|2026-08-03` | vérifiée il y a 17 j | rechecker l'ordonnance du comune di Coggiola |
| `incendie\|IT-ValGrande\|interdiction-acces-sentiers-parc\|2026-07-10` | vérifiée il y a 17 j | rechecker parcovalgrande.it (4 fermetures distinctes) |
| `refuge\|IT-Dolomites-Friuli-Cimoliana\|bivacco-gervasutti-amianto-inagibile\|2026-09-09` | jamais revérifiée depuis 8 j | rechecker CAI Cervignano |
| `reroutage\|Lot-Cieurac-Flaujac-Poujols\|GR65-devie-incendie\|2026-07-25` | vérifiée il y a 17 j | rechecker FFRandonnée / mairies de Limogne-en-Quercy |
| `reroutage\|VF-Lazio-Prato-La-Corte\|frana-deviation\|2026-01-30` | vérifiée il y a 17 j | rechecker parcodiveio.it |

## Statut final

`python3 site/build_site.py` → OK (QA passée). `python3 site/audit_qualite.py` → 0 bloquant
sur l'ensemble du registre (inchangé par rapport à avant ce passage). Aucune fiche supprimée,
aucune sévérité dégradée ou remontée d'autorité, aucune fiche hors de la liste de travail de
l'audit n'a été touchée.