# Verdict qualité du registre — 2026-08-26

Vérificateur qualité, agent distinct de la veille du jour. 7 fiches contrôlées, toutes
issues de `livrables/audit-qualite.md` (généré par `python3 site/audit_qualite.py --ecrire`
avant cette passe). Aucune fiche non citée par l'audit n'a été ouverte ni modifiée.

Après corrections : `python3 site/build_site.py` → **OK (QA passée)** (77 actives,
24 clôturées, 101 fichiers). `python3 site/audit_qualite.py --ecrire` relancé : les 3
constats portant sur des fiches corrigées ont disparu ; il reste 4 constats (1 bloquant),
tous hors périmètre de correction directe (détail plus bas).

## Verdicts par fiche

### `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`
1. FRAÎCHEUR — PASS (`verif` du jour même).
2. CONCORDANCE INTERNE — PASS (Portion / Zone / `statut` cohérents : seuls l'Amselsee et le
   bas de l'Amselgrund restent fermés, hélicoptère en cours depuis le 25/08).
3. HONNÊTETÉ — PASS (« aucune prolongation officielle n'est publiée à ce jour » dit en clair).
4. PERTINENCE — PASS (chantier réel en cours, pas une fermeture caduque).
5. SÉVÉRITÉ — PASS (HAUTE justifiée : arrêté du Landratsamt de Pirna, non expiré).
6. TON — PASS.
7. SOURCE VIVANTE — PASS (nationalpark-saechsische-schweiz.de/warnungen/eilmeldung-waldsperrung
   vérifiée ce jour : en ligne, contenu conforme au texte publié).
**Correction appliquée** : le champ `validite:` était écrit sur 6 lignes physiques. Le
parseur de front-matter (`build_site.parse_alerte`, utilisé aussi par `audit_qualite.py`)
ne recolle QUE les sections `##`, jamais les champs `champ: valeur` : il ne lisait donc que
la première ligne du champ (« …le 14/08 ne fixe » — coupée en plein mot), ce qui faisait
croire à l'audit que la validité s'arrêtait au 14/08, alors que la suite du texte (déjà
écrite, jamais lue par le script) dit l'inverse : plus d'échéance depuis le 14/08. Réécrit
en une seule ligne physique, mot pour mot identique, aucune information ajoutée ni retirée.
Vérifié : l'audit ne signale plus cette clé.
**Note technique (hors périmètre, pour le pilote)** : ce même défaut de parseur peut
affecter silencieusement toute autre fiche dont `validite:` ou `statut:` est mis en forme
sur plusieurs lignes physiques (plusieurs le sont dans le registre) — seule celle-ci a été
prise en défaut aujourd'hui, les autres n'ont pas été auditées sur ce point précis. À
envisager : faire recoller les continuations indentées des champs d'en-tête dans
`parse_alerte()`, comme c'est déjà fait pour les listes en section.

### `risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01`
1. FRAÎCHEUR — PASS (`verif` du jour, validité journalière).
2. CONCORDANCE INTERNE — **FAIL avant correction** : « Portion concernée » présentait le
   classement du 18/08 sans dire qu'aucune page plus récente n'existait, alors que `statut:`
   savait déjà (recherche du jour) qu'aucun classement n'avait été publié depuis huit jours.
   Défaut n°1 du registre, exactement le cas visé par ce contrôle.
3. HONNÊTETÉ — FAIL avant correction (même cause), PASS après.
4. PERTINENCE — PASS (classement préfectoral toujours en vigueur, silence ≠ levée).
5. SÉVÉRITÉ — PASS (rouge appuyée sur un classement officiel daté, pas une hypothèse).
6. TON — PASS.
7. SOURCE VIVANTE — PASS (gard.gouv.fr, page du 18/08, vérifiée ce jour : en ligne,
   confirme les 3 secteurs et les 94 communes).
**Correction appliquée** : réécrit « Portion concernée » pour dire explicitement que le
classement du 18/08 est le dernier publié et qu'aucune page plus récente n'est parue depuis
huit jours (information déjà connue via `statut:`, aucune source nouvelle nécessaire) ;
ajouté une entrée datée du 26/08 à la chronologie de « Zone (détails) », dans le style déjà
utilisé pour les silences précédents de la préfecture. Vérifié : l'audit ne signale plus
l'écart de 8 jours sur cette clé.

### `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`
1. FRAÎCHEUR — PASS (`verif` du jour).
2. CONCORDANCE INTERNE — PASS après un ajustement mineur (voir correction).
3. HONNÊTETÉ — PASS (« aucune de ces deux mesures n'a de clause de republication »).
4. PERTINENCE — PASS (deux arrêtés municipaux non expirés : Sorède jusqu'au 13/09/2026,
   Argelès « jusqu'à nouvel ordre »).
5. SÉVÉRITÉ — PASS (rouge fondée sur les arrêtés eux-mêmes, pas sur l'ancienneté de la
   presse — la fiche l'argumente déjà explicitement en MAJ 12/08, avis partagé).
6. TON — PASS.
7. SOURCE VIVANTE — mitigé : `mapetiterando.fr` (18/07/2026) répond et confirme la fermeture
   des 4 communes ; `ouillade.eu` a renvoyé 403 et `rnnmassane.fr` 503 à la vérification de
   ce jour, l'arrêté PDF n'a pas pu être relu (extraction illisible). Rien ne prouve que ces
   pages soient réellement mortes (403/503 ponctuels compatibles avec un blocage anti-robot),
   mais je n'ai pas pu les confirmer vivantes non plus. **Signalé, non corrigé** : à revérifier
   au prochain passage avec un accès direct ; si `ouillade.eu` est bien mort, le retirer des
   sources ou le remplacer.
**Correction appliquée** : la fin de « Portion concernée » ne citait qu'une vérification du
24/08, alors que `statut:` atteste d'une relecture du texte intégral de l'arrêté ARR2026-024PM
faite le jour même (26/08). Complété avec cette date et ce détail, déjà connus, sans nouvelle
source.
**Signalé, non corrigé** (constat ALERTE de l'audit, nécessite une source nouvelle) : la
seule presse datée sous cette alerte rouge reste `ouillade.eu` du 29/07 (28 jours). La fiche
documente déjà de nombreuses tentatives infructueuses (10, 12, 13, 14, 18, 26/08) pour en
retrouver une plus récente. Je ne dégrade pas la sévérité : la base légale de l'interdiction
(les deux arrêtés, non expirés) reste indépendante de l'âge de cet article de presse, et le
prompt n'impose la dégradation automatique que pour une alerte encore adossée à « à
confirmer »/« probable », ce qui n'est pas le cas ici. **Action laissée à la veille** :
retrouver une publication postérieure au 29/07 sur l'accès au massif, ou consulter
directement les arrêtés/pages municipales si le réseau le permet.

### `infrastructure|SCAND-SE-Norrbotten|kungsleden-barque-sitojaure-fermee|2026-07-29`
1. FRAÎCHEUR — PASS (fiche créée et vérifiée aujourd'hui).
2. CONCORDANCE INTERNE — PASS.
3. HONNÊTETÉ — PASS (absence de date de reprise dite explicitement).
4. PERTINENCE — PASS.
5. SÉVÉRITÉ — PASS (MOYENNE : un service de franchissement fermé, pas le sentier).
6. TON — **FAIL avant correction** : « Zone (détails) » contenait « lisible en autonome »,
   du jargon de veille (mécanique de lecture de page) dans un champ public.
7. SOURCE VIVANTE — non contrôlée (sévérité MOYENNE, hors obligation du contrôle 7).
**Correction appliquée** : supprimé « lisible en autonome » de la phrase, aucune information
retirée (la source et son absence de date restent dites). Vérifié : l'audit ne signale plus
de jargon sur cette clé.

### `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`
1. FRAÎCHEUR — **FAIL bloquant** : vérifiée il y a 12 j, seuil 2 j (fermetures décidées au
   jour le jour). 2–6. PASS par ailleurs (portion honnête sur l'absence de source récente,
   sévérité MOYENNE cohérente, pas de jargon public). 7. non contrôlée (MOYENNE).
**Non corrigé — hors périmètre du run d'aujourd'hui** (zone Crète, lot du vendredi, pas
couverte aujourd'hui) : lever ce FAIL demande une source nouvelle (samaria.gr ou presse
datée d'août), donc le travail de la veille. **Signalé en tête de liste, priorité haute** :
c'est le seul constat encore BLOQUANT du registre.

### `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`
1. FRAÎCHEUR — FAIL (20 j, seuil 12 j, sévérité moyenne). 2–6 PASS (fiche déjà honnête :
   `[HYPOTHÈSE]`, recoupement GR®R2 à faire annoncé comme tel). 7 non contrôlée.
**Non corrigé — hors périmètre** (pas de nouvelle source disponible aujourd'hui pour ce
recoupement AP/carte ONF). **Action laissée à la veille** : consulter directement la carte
ONF interactive au prochain passage sur la zone, comme déjà noté en `statut:`.

### `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`
1. FRAÎCHEUR — FAIL (19 j, seuil 12 j, sévérité moyenne). 2–6 PASS (le texte dit déjà
   explicitement que l'échéance du 15/08 est dépassée sans confirmation de réouverture —
   c'est exactement la formulation honnête attendue). 7 non contrôlée.
**Non corrigé — hors périmètre** (pas de nouvelle source aujourd'hui). **Action laissée à
la veille** : revérifier caminsdepedra.conselldemallorca.es au prochain passage sur la zone.

## Corrections appliquées (résumé, avec clés)

1. `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`
   — `validite:` remis sur une seule ligne physique (faux positif de parseur), aucune
   information changée.
2. `risque-feu|Gard-30|fermetures-5-secteurs-rouges|2026-07-01` — « Portion concernée »
   réécrite pour dire que le classement du 18/08 est le dernier connu et que 8 jours se sont
   écoulés sans nouvelle publication ; entrée datée du 26/08 ajoutée à « Zone (détails) ».
3. `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — date de dernière vérification
   complétée (24/08 → 26/08) dans « Portion concernée », à partir de `statut:`.
4. `infrastructure|SCAND-SE-Norrbotten|kungsleden-barque-sitojaure-fermee|2026-07-29` —
   jargon de veille (« lisible en autonome ») retiré de « Zone (détails) ».

## Actions laissées à l'agent de veille (à traiter au prochain run, par ordre de priorité)

1. **Bloquant** — `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` :
   revérifier samaria.gr / presse crétoise, la fiche n'a pas été revue depuis 12 jours sur
   une restriction annoncée « au jour le jour ».
2. `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` : retrouver une source postérieure
   au 29/07/2026 sur l'accès au massif des Albères, ou confirmer que `ouillade.eu` et
   `rnnmassane.fr` répondent bien depuis un accès direct (403/503 obtenus aujourd'hui depuis
   cet environnement).
3. `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` : recouper l'AP 2026-693 avec la
   carte ONF interactive au prochain passage sur la zone 974.
4. `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` : revérifier
   caminsdepedra.conselldemallorca.es, l'échéance du 15/08 est dépassée depuis 11 jours.

Aucune fiche n'a été clôturée, supprimée ni dégradée en sévérité par ce contrôle.
