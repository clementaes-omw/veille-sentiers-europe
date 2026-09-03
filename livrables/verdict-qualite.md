# Verdict qualité du registre — 2026-09-03

Agent Vérificateur Qualité, distinct de l'agent de veille du jour. Aucune des 8 fiches
listées ci-dessous n'a été écrite par moi aujourd'hui : je les contrôle, je ne relis pas
mon propre travail.

Périmètre : les 8 constats de `livrables/audit-qualite.md` régénéré en tête de passage
(1 bloquant, 5 alertes, 2 dette de forme), sur 8 fiches distinctes. Aucune autre fiche du
registre (105 fichiers, 76 actives) n'a été ouverte ni touchée.

## À traiter au prochain run (nécessite une source nouvelle, hors de mon périmètre)

1. **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — BLOQUANT.
   FRAÎCHEUR (contrôle 1) FAIL : vérifiée il y a 6 j, seuil 2 j pour une restriction
   « décidée au jour le jour ». Concordance interne bonne (Portion concernée, `statut:`
   et Zone détails datent tous du 28/08, sans contradiction). Zone E4 Crète hors
   périmètre des agents de veille d'aujourd'hui (Sud-Est/Pyrénées, Provence-Corse,
   Est/Alpin/Nord, Iberia) : pas de recherche de source de ma part, je ne peux pas
   revérifier ce que la veille du jour n'a pas couvert. **Action attendue au prochain
   passage sur la zone Grèce/E4 Crète** : revérifier le statut du jour sur samaria.gr et
   crete.gov.gr (Région de Crète) avant de republier « ACTIF » sans changement de date.
2. **`incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`** — ALERTE.
   FRAÎCHEUR (contrôle 1) FAIL : vérifiée il y a 15 j, seuil 12 j (sévérité MOYENNE).
   Concordance interne bonne, validité « jusqu'à nouvel ordre » (non expirée). Zone
   Bretagne non couverte par le run du jour. **Action attendue au prochain passage
   FR-BRE** : recontrôler auprès de la mairie de Plévenon ou de la FFRandonnée
   Côtes-d'Armor si l'arrêté municipal du 15/07 a été levé, un mois et demi après
   l'incendie et la publication de la déviation officielle.

## Vérifié sans dégradation — règle des 14 jours correctement appliquée

3. **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — ALERTE
   audit (contrôle 7, source vieillie) : la source la plus récente citée date du 18/08
   (16 j). L'agent de veille du jour a déjà mené une recherche ciblée (`statut:` du
   03/09 : ariège.gouv.fr et pyreneesfm.com relus, aucune 5e reconduction ni levée de
   l'arrêté anti-feu trouvée). Vérification du raisonnement : la sévérité HAUTE de
   cette fiche repose sur la **fermeture du GR®10** elle-même (chutes de pierres,
   secteur Ayès↔Cap des Lauses), un fait établi et recoupé par 3 sources indépendantes
   (France 3 Occitanie 04/08, ruralites2024.fr 03/08, radiocouserans.fr 02/08), décrit
   comme tel dans « Portion concernée » sans aucun marqueur d'hypothèse (« à confirmer »,
   « probable »…). L'échéance non reconduite de l'arrêté préfectoral anti-feu est un
   sujet distinct, correctement isolé dans le texte (« ce point, distinct de la
   fermeture du tronçon pour chutes de pierres, n'est pas encore tranché »). La règle
   des 14 jours (`agent-prompt.md` § DURÉE DE VIE D'UNE HYPOTHÈSE) porte sur une
   alerte dont la sévérité repose sur une hypothèse non confirmée : ce n'est pas le cas
   ici, elle ne s'applique donc pas au fait de fermeture. Raisonnement bien documenté
   dans `statut:`. Contrôles 3 et 5 → PASS. Aucune dégradation appliquée, aucune
   correction nécessaire.
4. **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — même situation : source la
   plus récente datée du 21/08 (13 j), déjà revérifiée aujourd'hui par l'agent de veille
   (`statut:` du 03/09 : mairie-die.fr, drome.gouv.fr et presse relus, l'arrêté du 21/08
   reste la donnée la plus récente). « Portion concernée » décrit un arrêté préfectoral
   déjà publié et confirmé par 2 sources indépendantes (mairie-die.fr, ici.fr), qui
   abroge explicitement celui du 24/07 ; l'absence de date de levée tient au fait que
   la sortie dépend d'une étude de risque en cours, pas d'une hypothèse non tranchée.
   Aucun marqueur d'hypothèse dans « Portion concernée ». Contrôles 3 et 5 → PASS.
   Aucune dégradation appliquée, aucune correction nécessaire.

## Corrections appliquées (périmètre : réécriture à information constante)

5. **`fermeture|Drome-Omblese|sentiers-pas-du-gouillat-pas-de-comberoufle|2026-07-07`**
   — l'audit signalait une `validite:` expirée au 31/08/2026. Vérification : la fiche
   contient déjà, depuis le run précédent (MAJ 01/09 en « Zone (détails) »), le second
   régime préfectoral (arrêté DDT-SEF-2026-0176, valable jusqu'au 15/09/2026) qui prend
   le relais de l'arrêté municipal échu — et « Portion concernée » le disait déjà
   correctement. La cause du faux signal est mécanique : le parseur de front-matter de
   `site/build_site.py` (`parse_alerte`) ne recolle pas les lignes de continuation d'un
   champ replié sur plusieurs lignes ; seule la première ligne du `validite:` était
   effectivement lue par l'audit, qui n'y voyait que la date expirée du 31/08 sans la
   suite mentionnant le 15/09. Correction : `validite:` reformaté sur une seule ligne
   physique, aucun fait ajouté ni retiré. Contrôle 2 (concordance interne) → PASS déjà
   avant correction sur le texte affiché ; correction de forme pour que l'audit lise le
   même état que le lecteur.
6. **`risque-feu|HauteGaronne-31|vigilance-rouge-camping-sauvage-interdit|2026-07-09`**
   — l'audit signalait une `validite:` expirée au 09/07/2026. Vérification : cette
   fiche vient justement d'être corrigée aujourd'hui par l'agent de veille — la source
   officielle (haute-garonne.gouv.fr, MAJ 30/07) ne fixe aucune date de fin, la mesure
   s'appliquant tant que dure la vigilance rouge, et « Portion concernée » a bien été
   réécrite en conséquence (aucune échéance n'y est affichée). Même cause mécanique que
   ci-dessus : le `validite:` replié sur plusieurs lignes n'était lu par l'audit que
   jusqu'à sa première ligne, qui contient la seule date du 09/07/2026 (date de
   signature de l'arrêté, pas d'échéance) sans la suite qui écarte explicitement la
   fausse échéance de presse du 01/09. Correction : `validite:` reformaté sur une seule
   ligne, avec la formule « en vigueur jusqu'à nouvel ordre » ajoutée en paraphrase
   fidèle de ce que dit déjà la source citée (« restera en vigueur durant toute la
   durée de vigilance très élevée », « sans date de fin ») — aucun fait nouveau, mais
   une formulation qui met l'information décisive dans la partie du champ que le
   contrôle automatique retient, pour que ce faux positif ne se reproduise pas les
   prochains jours. Contrôle 2 → PASS, déjà correct côté « Portion concernée » avant
   ma correction.
7. **`risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18`** — TON
   (contrôle 6) : le paragraphe « Zone (détails) » MAJ 03/09 contenait « nouvelle
   recherche ciblée sur l'arrêté n°2A-2026-07-20-00007 par son numéro », jargon de
   veille banni des champs publics. Reformulé en décrivant l'état du terrain (« toujours
   aucune publication postérieure au 23/07/2026 trouvée, ni sur l'arrêté … ni sur
   l'actualité récente de Corse-du-Sud ») : mêmes faits, même source, aucune date ni
   numéro d'arrêté modifié. Contrôle 6 → PASS.
8. **`risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`** — même
   défaut, paragraphe « Vérifié le 03/09/2026 » : « recherche ciblée sur l'acte manquant »
   reformulé en « toujours aucune publication postérieure au 31/08 trouvée pour ce
   massif (recueil des actes administratifs …, presseagence.fr, nicepremium.fr) ».
   Contrôle 6 → PASS.

Après les 4 corrections (items 5 à 8) : `python3 site/build_site.py` rend
**OK (QA passée)** (76 actives, 29 clôturées, 105 fichiers, registre 641 747 car.).
`python3 site/audit_qualite.py --ecrire` : les 4 fiches corrigées ne remontent plus
aucun constat (registre passé de 8 à 4 constats ; le compteur de dette de forme
« Zone (détails) » passe de 2 à 0). Restent, sans que je les aie touchées, le 1 bloquant
et les 3 alertes hors de mon périmètre (items 1 à 4 ci-dessus), conformes à la règle de
sortie : je ne corrige pas ce qui exige une source nouvelle, je le signale.

## Bilan des 7 contrôles sur les 8 fiches auditées

| Contrôle | Résultat |
|---|---|
| 1. Fraîcheur | PASS sur Omblèze, HauteGaronne, Bavella-Illarata, AlpesMaritimes, Ariège, Justin-Die (verif du jour ou validité cohérente) ; FAIL signalé (non corrigé) sur Creta-Samaria (6 j / seuil 2 j, zone hors périmètre du jour) et CapFrehel (15 j / seuil 12 j, zone Bretagne non couverte) |
| 2. Concordance interne | PASS sur les 8 fiches — Portion concernée, `statut:` et Zone (détails) racontent le même état ; sur Omblèze et HauteGaronne, seul le `validite:` du front-matter (non affiché au lecteur) a dû être reformaté pour que l'audit automatique le lise correctement |
| 3. Honnêteté sur l'incertain | PASS sur les 8 — aucune restriction non confirmée présentée comme certaine sans le dire ; Ariège et Justin-Die distinguent clairement le fait établi (fermeture) de l'incertitude résiduelle (reconduction de l'arrêté anti-feu, échéance de l'étude de risque) |
| 4. Pertinence | PASS sur les 8, aucune clôture à recommander |
| 5. Sévérité juste | PASS sur les 8 ; pas de dégradation appliquée sur Ariège ni Justin-Die, la règle des 14 jours ne s'appliquant pas à une sévérité HAUTE qui repose sur un fait déjà établi et non sur une hypothèse non tranchée (voir sections dédiées) |
| 6. Ton | 2 FAIL non bloquants corrigés (Bavella-Illarata, AlpesMaritimes) → PASS ; PASS d'emblée sur les 6 autres |
| 7. Source vivante | FAIL non bloquant persistant, signalé sans correction, sur Ariège (18/08, 16 j) et Justin-Die (21/08, 13 j) : recherche ciblée déjà menée aujourd'hui par l'agent de veille sans résultat nouveau, fait de fermeture établi indépendamment de l'âge de la source la plus récente |

8 fiches contrôlées, 4 corrections appliquées (Omblèze, HauteGaronne, Bavella-Illarata,
AlpesMaritimes — 2 réécritures de `validite:` à information constante, 2 nettoyages de
jargon de veille), 4 constats laissés au prochain passage de veille par zone (E4 Crète,
FR-BRE, et 2 rappels de recherche ciblée sur Ariège/Vaucluse-Drôme-Ardèche déjà en cours
de suivi, sans dégradation de sévérité requise). `python3 site/audit_qualite.py --ecrire` :
1 bloquant avant et après (Creta-Samaria, hors périmètre), 8 → 4 constats au total.
`python3 site/build_site.py` : **OK (QA passée)**.
