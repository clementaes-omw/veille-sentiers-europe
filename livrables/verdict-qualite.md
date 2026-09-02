# Verdict qualité du registre — 2026-09-02

Agent Vérificateur Qualité, distinct de l'agent de veille dont le run du jour a produit
et revuérifié les fiches ci-dessous (dont 3 nouvelles fiches Bretagne, déjà résolues côté
carte avant mon passage via `ALIAS_ZONE`). Aucune des 5 fiches contrôlées ci-dessous n'a
été écrite par moi : je les contrôle, je ne relis pas mon propre travail.

Périmètre : les 6 constats confiés par la mission — les 4 lignes « À traiter » de
`livrables/audit-qualite.md` régénéré en début de passage (0 bloquant, 4 alertes) plus
les 2 lignes « Dette de forme » (jargon de veille en « Zone (détails) ») — portant sur
5 fiches distinctes (la fiche Ariège cumule un constat de fraîcheur de source et un
constat de jargon). Aucune autre fiche du registre (105 fichiers, 76 actives) n'a été
ouverte ni touchée.

## Corrections appliquées (périmètre : réécriture à information constante)

1. **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — TON
   (contrôle 6) : le paragraphe « Zone (détails) » MAJ 02/09 contenait « nouvelle
   recherche ciblée sur l'acte manquant » et « non retenu ici », du jargon de veille
   dans un champ public. Reformulé pour décrire l'état constaté : page des actualités
   de la préfecture inaccessible, aucun article récent sur pyreneesfm.com, aucune 5e
   reconduction ni levée publiée, feu distinct d'Ax-les-Thermes/Bonascre sans lien
   avec cette fermeture. Aucun fait, date, chiffre ou source modifié ou supprimé.
   Contrôle 6 → PASS.
2. **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — même défaut,
   paragraphe MAJ 02/09 : « Une recherche ciblée sur ces quatre communes… » reformulé
   en « Aucun arrêté de levée nommant ces quatre communes n'a été retrouvé (mairies,
   drome.gouv.fr, diois-tourisme.com) ». Même méthode déjà documentée dans le reste du
   paragraphe conservée telle quelle. Contrôle 6 → PASS.

Après ces 2 corrections : `python3 site/audit_qualite.py --ecrire` ne signale plus de
dette de forme sur ces deux fiches (2 → 0) et ne signale toujours aucun bloquant ;
`python3 site/build_site.py` rend **OK (QA passée)** (76 actives, 29 clôturées,
105 fichiers, registre 636 867 car.). Seul avertissement de ton restant : une fiche
hors périmètre (`fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei`, 1 tiret
cadratin), non touchée conformément à la consigne de ne pas sortir du périmètre confié.

## Vérification demandée par la mission sur la fiche Ariège

`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10` : le champ
`verif:` porte bien `2026-09-02`, daté du jour, et `statut:` documente la recherche
ciblée déjà menée aujourd'hui par l'agent de veille (page préfecture inaccessible,
pyreneesfm.com revu sans nouvel article) sans résultat nouveau. Contrôle FRAÎCHEUR (1) :
PASS sur la date de vérification. Contrôle SOURCE VIVANTE (7) reste en FAIL non
bloquant côté audit sur la source la plus récente citée dans le champ `Source`
(Pyrénées FM 18/08, 15 j) : c'est la source de l'**arrêté anti-feu**, distincte de celle
qui établit la **fermeture du GR®10** elle-même, laquelle s'appuie sur 3 sources
indépendantes déjà anciennes mais jamais démenties (France 3 Occitanie 04/08,
ruralites2024.fr 03/08, radiocouserans.fr 02/08). Cette fermeture n'est pas présentée
au fil de la fiche comme « à confirmer » ou « probable » : c'est un fait établi et
recoupé, décrit comme tel dans « Portion concernée ». La règle des 14 jours
(`agent-prompt.md` § DURÉE DE VIE D'UNE HYPOTHÈSE) porte explicitement sur les
hypothèses non confirmées au-delà de 14 jours, pas sur un fait déjà établi dont seule
la source la plus récente vieillit faute d'actualité nouvelle sur l'arrêté qui lui est
associé : elle ne s'applique donc pas ici, conformément à la nuance déjà actée dans
`statut:` par l'agent de veille du jour. Aucune dégradation de sévérité appliquée ; je
n'ai pas refait de vérification web des sources moi-même (hors périmètre), je m'appuie
sur la recherche ciblée déjà documentée aujourd'hui dans le fichier.

## Signalé, non corrigé — nécessite une source nouvelle (prochain passage de veille)

1. **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** —
   FRAÎCHEUR (contrôle 1) FAIL : vérifiée il y a 5 j, seuil 2 j pour une restriction
   « décidée au jour le jour ». Concordance interne bonne (Portion concernée, `statut:`
   et Zone détails datent tous du 28/08). Zone E4 Crète hors périmètre du jour
   (couverte le vendredi) : pas de recherche de source de ma part. **Action attendue
   au prochain passage sur l'E4 Crète** : revuérifier samaria.gr et crete.gov.gr avant
   la prochaine étape.
2. **`incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`** — voir
   section dédiée ci-dessus. **Action attendue au prochain passage sur l'Ariège** :
   rechercher spécifiquement une 5e reconduction ou une levée de l'arrêté anti-feu
   (ariege.gouv.fr une fois accessible, recueil des actes administratifs) ; le fait de
   fermeture du GR®10 lui-même n'est pas remis en cause et ne demande pas de nouvelle
   recherche tant qu'aucun signal contraire n'apparaît.
3. **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — SOURCE VIVANTE
   (contrôle 7) : source la plus récente citée datée du 21/08 (12 j), revuérifiée
   aujourd'hui par l'agent de veille sans résultat nouveau (`statut:` du jour).
   « Portion concernée » ne repose pas sur du « à confirmer »/« probable » : l'arrêté
   du 21/08 est un texte réglementaire déjà confirmé par 2 sources indépendantes
   (mairie-die.fr, ici.fr) et abroge explicitement celui du 24/07 ; ce n'est donc pas
   une hypothèse au sens de la règle des 14 jours, et aucune dégradation n'est
   appliquée. **Action attendue au prochain passage sur Vaucluse-Drôme-Ardèche** :
   rechercher une publication postérieure au 21/08 confirmant que l'interdiction (ou
   l'étude de risque en cours) reste en vigueur ; la fraîcheur de la source reste un
   point à retraiter tant qu'aucune nouvelle publication n'est trouvée.
4. **`incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`** — FRAÎCHEUR
   FAIL : vérifiée il y a 14 j, seuil 12 j (sévérité MOYENNE). Concordance interne
   bonne, validité « jusqu'à nouvel ordre ». Cap Fréhel était dans le périmètre
   Bretagne du run du jour mais a été omis de la liste de fichiers traités par l'agent
   de veille. Pas de recherche de source de ma part (hors périmètre du vérificateur).
   **Action attendue au prochain passage sur FR-BRE** : recontrôler l'arrêté municipal
   de Plévenon (levée éventuelle, un mois et demi après l'incendie et la publication
   de la déviation officielle).

## Bilan des 7 contrôles sur les 5 fiches auditées

| Contrôle | Résultat |
|---|---|
| 1. Fraîcheur | PASS sur Ariège et Baronnies-GR9 (`verif:` du jour) ; FAIL signalé sur Creta-Samaria (5 j / seuil 2 j, zone hors périmètre du jour) et CapFrehel (14 j / seuil 12 j, zone oubliée du run) |
| 2. Concordance interne | PASS sur les 5 — Portion concernée, `statut:` et Zone (détails) racontent le même état sur chacune |
| 3. Honnêteté sur l'incertain | PASS sur les 5 — aucune restriction non confirmée présentée comme certaine sans le dire |
| 4. Pertinence | PASS sur les 5, aucune clôture à recommander |
| 5. Sévérité juste | PASS sur les 5 ; pas de dégradation appliquée sur Ariège ni Drôme, la règle des 14 jours ne s'appliquant pas à un fait déjà établi (voir sections dédiées) |
| 6. Ton | 2 FAIL non bloquants corrigés (Ariège, Baronnies-GR9) → PASS ; PASS d'emblée sur Creta-Samaria, Drôme, CapFrehel |
| 7. Source vivante | FAIL non bloquant persistant, signalé sans correction, sur Ariège (18/08, 15 j) et Drôme (21/08, 12 j) : recherche ciblée déjà menée aujourd'hui par l'agent de veille sans résultat nouveau, fait de fermeture établi indépendamment de la source la plus récente |

5 fiches contrôlées, 2 corrections de ton appliquées (Ariège, Baronnies-GR9), 4 constats
laissés au prochain passage de veille par zone (E4 Crète, Ariège, Vaucluse-Drôme-Ardèche,
FR-BRE). `python3 site/audit_qualite.py --ecrire` : 0 bloquant avant et après (4 alertes
non bloquantes restantes, exactement celles listées ci-dessus). `python3
site/build_site.py` : **OK (QA passée)**.
