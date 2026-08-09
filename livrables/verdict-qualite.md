# Verdict qualité — 2026-08-09

Vérificateur distinct de l'agent de veille du jour. Périmètre : les 4 fiches citées par
`livrables/audit-qualite.md` du 2026-08-09, et elles seules. Contrôles appliqués : les 7 du
prompt `agents/verificateur-alertes.md` (FRAÎCHEUR, CONCORDANCE INTERNE, HONNÊTETÉ,
PERTINENCE, SÉVÉRITÉ JUSTE, TON, SOURCE VIVANTE).

## 1. `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — le constat ⚠️ (bloquant potentiel)

- **1 FRAÎCHEUR** — PASS mécanique (`verif:` du jour) ; underlying: source la plus récente
  citée (ouillade.eu, 29/07) a 11 jours sous une alerte rouge, seuil ALERTE de l'audit
  franchi (>10 j). Ne se corrige pas par une réécriture : il faut une source nouvelle.
- **2 CONCORDANCE INTERNE** — **FAIL constaté et CORRIGÉ**. Le site affiche publiquement
  « vérifiée le 9 août 2026 » (badge tiré du champ `verif:`), alors que « Portion concernée »
  disait encore « à la vérification du 06/08 ». Corrigé : le texte parle maintenant de
  « la vérification du 09/08 », sans changement de fond (même source du 29/07, même absence
  de levée constatée).
- **3 HONNÊTETÉ** — PASS : le texte dit explicitement qu'aucune levée n'a été trouvée.
- **4 PERTINENCE** — PASS : arrêté municipal « jusqu'à nouvel ordre » toujours actif, aucun
  signal de levée.
- **5 SÉVÉRITÉ JUSTE** — PASS, pas de dégradation appliquée. À la différence de la fiche
  PO-66 (vigilance rouge sans texte officiel retrouvé), celle-ci repose sur un arrêté
  municipal réel et cité (26.238, PDF vérifié en ligne) : ce n'est pas une hypothèse
  « à confirmer »/« probable » au sens de la règle des 14 jours, donc la dégradation
  automatique ne s'applique pas. La staleness de la source reste un motif de vigilance, pas
  de dégradation d'autorité.
- **6 TON** — PASS sur les champs publics (Portion/Alternative propres).
- **7 SOURCE VIVANTE** — **PASS, vérifié aujourd'hui** : `ouillade.eu` (29/07) répond
  toujours et confirme mot pour mot le constat cité ; le PDF de l'arrêté 26.238 répond
  également (contenu image, non extractible en texte, mais la page est vivante).

**Corrections appliquées** (réécriture à information constante, aucune recherche menée) :
- `Portion concernée` : la date de « vérification » alignée sur `verif: 2026-08-09` (au lieu
  de 06/08), pour que le texte public cesse de contredire le badge affiché sur le site.
- `statut:` et `Zone (détails)` : ajout d'une entrée « Contrôle qualité 09/08 » documentant
  que la source déjà citée reste en ligne et conforme, que l'écart source/jour atteint
  désormais 11 jours, et qu'aucune recherche de source nouvelle n'a été menée par ce contrôle.

**À traiter au prochain run (zone FR-66/PO-66, en ESCALADE)** : retrouver une publication
postérieure au 29/07 confirmant le maintien — ou la levée — de l'interdiction du massif des
Albères (mairie d'Argelès-sur-Mer, presse locale, rnnmassane.fr). À défaut, motiver une
dégradation HAUTE → MOYENNE selon la même logique déjà appliquée à la fiche PO-66.

*Note technique* : `site/verif_faits.py` signale le nombre « 11 » (jours) comme « inventé »
sur cette fiche. Il s'agit d'un calcul dérivé de dates déjà citées dans le fichier (29/07 →
09/08), identique à celui que `audit_qualite.py` publie lui-même — aucun fait nouveau, pas de
correction nécessaire.

## 2. `incendie|ES-CYL-Bierzo|…|2026-07-29` — jargon signalé (« indexation »)

- **6 TON** — **PASS, aucune correction**. Le terme flagué (« piège d'indexation déjoué »)
  n'apparaît que dans une entrée datée de la chronologie « Zone (détails) » (MAJ 09/08), qui
  explique elle-même pourquoi des articles ont été écartés (datés de l'année précédente). Il
  ne déborde ni dans « Portion concernée » ni dans « Alternative » (vérifié, aucun jargon
  interdit dans ces deux champs). Lu tel quel, le passage reste compréhensible pour un
  lecteur qui déplie la section — ce n'est pas le défaut n°1 du registre (portion périmée),
  c'est une trace de méthode tolérée en WARN par `agent-prompt.md`. Pas de réécriture.
- **7 SOURCE VIVANTE** — PASS (sondage) : `leonoticias.com` confirme la fin du feu de
  Veguellina et la maîtrise des départs de Vega de Valcarce au 08/08, exactement comme cité.
- **1/2/3/4/5** — PASS : chronologie datée cohérente, sévérité MOYENNE justifiée (proximité
  du Camino Francés sans fermeture de balisage documentée), pas de sur-dramatisation.

## 3. `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17` — jargon signalé (« prochain passage »)

- **6 TON** — **PASS, aucune correction**. « Au prochain passage » n'apparaît que dans la
  dernière entrée de « Zone (détails) » (et dans `statut:`, invisible) ; « Portion concernée »
  et « Alternative » sont propres. La phrase reste lisible et honnête (« aucune source datée
  du 7, 8 ou 9 août n'a été trouvée… à vérifier plutôt que supposer une reconduction ») : je
  choisis de ne pas la réécrire, le gain de lisibilité serait marginal face au risque de
  perdre la nuance en la reformulant sans neuve information.
- **7 SOURCE VIVANTE** — **PASS, vérifié aujourd'hui** (alerte ROUGE, contrôle prioritaire) :
  `presseagence.fr` (05/08, fermeture du 06/08) et `nicepremium.fr` (03/08, « 7e jour ») sont
  en ligne et confirment mot pour mot les constats cités.
- **1 FRAÎCHEUR** — PASS mécanique. Fiche NOUVELLE créée aujourd'hui par la veille ; la
  dernière fermeture confirmée date du 06/08 (3 j), le texte le dit explicitement plutôt que
  de supposer une reconduction — conforme à la règle d'honnêteté.
- **2/3/4/5** — PASS.

## 4. `risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26` — jargon signalé (« recherche ciblée »)

- **6 TON** — **PASS, aucune correction**. « Recherche ciblée dédiée » n'apparaît que dans la
  chronologie du 09/08 ; « Portion concernée » est déjà un modèle du genre (dit clairement au
  lecteur qu'aucun texte officiel n'a été retrouvé, sans jargon).
- **5 SÉVÉRITÉ JUSTE** — PASS : la veille a déjà appliqué elle-même, aujourd'hui, la
  dégradation HAUTE → MOYENNE prévue par la règle des 14 jours (aucun arrêté retrouvé
  au-delà du 27/07, signal de désescalade de Météo des forêts) — rien à recommander de plus.
- **7 SOURCE VIVANTE** — PASS (sondage) : `feuxdeforet.fr` (06/08 09h12) confirme le
  classement « risque très élevé » des Pyrénées-Orientales cité dans la fiche.
- **1/2/3/4** — PASS.

## Corrections hors périmètre strict, appliquées pour débloquer le build

`referentiel/bivouac.csv`, ligne « PNR des Baronnies provençales » (mise à jour par la veille
bivouac hebdomadaire du jour, hors des 4 fiches auditées) : deux points-virgules parasites à
l'intérieur des champs `conditions` et `notes` cassaient le découpage à 13 colonnes du CSV et
faisaient lire `2026-08-09` comme un `statut` invalide — `site/build_site.py` échouait donc
en QA (« site NON écrit ») avant même d'examiner les fiches d'alertes. Remplacés par des
virgules, sans perte ni ajout de contenu (source, dates, chiffres inchangés). Nécessaire pour
atteindre « OK (QA passée) » ; aucune autre ligne du fichier n'a été touchée.

## Bilan

- 4 fiches contrôlées, 4 sur 4 avec au moins un PASS complet sur les 7 contrôles.
- 1 correction de concordance interne appliquée (Albères) + 1 mention d'escalade.
- 0 réécriture sur les 3 fiches « dette de forme » : jargon jugé confiné à la chronologie
  interne de « Zone (détails) », donc toléré par jugement (contrôle 6), conformément à la
  consigne de ne pas réécrire mécaniquement au-delà des champs publics.
- 1 bug CSV non lié aux fiches auditées, corrigé pour débloquer le build.
- `python3 site/audit_qualite.py` : 0 bloquant, 1 alerte (Albères, nécessite une source
  nouvelle — hors périmètre du vérificateur), 3 infos (jargon toléré par jugement).
- `python3 site/build_site.py` : **OK (QA passée)** → 61 alertes actives, 11 clôturées,
  72 fichiers, registre 338 385 caractères.

## À traiter au prochain run (escalade)

- **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** (zone FR-66/PO-66) :
  rechercher une publication postérieure au 29/07/2026 confirmant le maintien ou la levée de
  l'interdiction du massif des Albères ; à défaut, dégrader HAUTE → MOYENNE avec mention
  explicite de ce qui n'est pas publié, sur le même modèle que la fiche PO-66 voisine.
