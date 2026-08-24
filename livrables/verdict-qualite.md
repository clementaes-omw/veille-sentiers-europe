# Verdict qualité — 2026-08-24

Vérificateur qualité, exécution distincte de la veille du jour (aucune fiche listée
ci-dessous n'a été rédigée par cet agent). Point de départ : `livrables/audit-qualite.md`
généré aujourd'hui, 15 fiches avec au moins un constat sur 74 alertes actives.

## Action prioritaire laissée à la veille

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** (BLOQUANT) —
  vérifiée il y a 10 j contre un seuil de 2 j (restriction décidée au jour le jour, Crète,
  hors périmètre du jour). Corriger cette fiche demande une recherche de source nouvelle
  (l'accès à la gorge de Samaria a-t-il été rouvert/refermé depuis ?), ce qui sort du rôle
  du vérificateur qualité (audit de forme, pas de recherche de nouveaux constats). À traiter
  au prochain passage de veille sur la zone Crète/GR-E4.

## PASS / FAIL par contrôle (sur les 15 fiches citées par l'audit)

1. **FRAÎCHEUR** — FAIL sur 5 fiches, toutes hors périmètre du jour et nécessitant une
   source nouvelle (Samaria, Réunion-974, CH-EST-Trubbach, CH-Europaweg-Randa-Zermatt,
   TMB-CH-Orsieres, GR221-222-Mallorca) → signalées ci-dessous, non corrigées (hors
   périmètre du vérificateur).
2. **CONCORDANCE INTERNE** — FAIL initial sur 1 fiche (Malerweg-Bastei, écart de 8 j entre
   « Portion concernée » et le suivi) → **corrigé**.
3. **HONNÊTETÉ SUR CE QU'ON NE SAIT PAS** — PASS sur les 15 fiches : chaque incertitude
   (Baronnies-GR9, Alberes-66, ponts/refuges à échéance dépassée) est déjà formulée en clair
   pour le lecteur.
4. **PERTINENCE** — PASS global ; recommandation de clôture à évaluer par la veille pour les
   4 feux fixés/éteints sans arrêté ni fermeture de sentier (Aude-Montseret, Drôme-Bellegarde,
   Lozère-La Bastide-Puylaurent, Var-Ginasservis) si aucune reprise n'est constatée au
   prochain passage — non appliquée d'autorité, seulement recommandée.
5. **SÉVÉRITÉ JUSTE** — PASS. Vérifié spécifiquement pour Baronnies-GR9 et Alberes-66 (les
   deux alertes rouges signalées par l'audit avec une source de presse vieille de 12 et 26
   jours) : dans les deux cas l'alerte n'est **pas** adossée à un marqueur d'hypothèse
   (« à confirmer », « probable », « non localisé »...) mais à des arrêtés municipaux datés et
   non expirés (PNR Baronnies Provencçales, MAJ 12/08, arrêtés individuels jusqu'au 10/08 pour
   le plus récent ; Sorède n°26.216 jusqu'au 13/09/2026, Argelès « jusqu'à nouvel ordre »). La
   règle des 14 jours (agent-prompt.md, § DURÉE DE VIE D'UNE HYPOTHÈSE) ne s'applique donc pas :
   elle vise une alerte rouge fondée sur une hypothèse non tranchée, pas une alerte fondée sur
   un acte publié dont seule la reprise de presse est ancienne. Aucune dégradation appliquée.
6. **TON** — PASS. 0 occurrence de jargon de veille dans « Zone (détails) » sur l'ensemble du
   registre (0 info à l'audit).
7. **SOURCE VIVANTE** — PASS. Sources vérifiées en direct pour les 3 alertes rouges citées par
   l'audit : saechsische-schweiz.de/gut-zu-wissen/aktuelles (Malerweg, à jour, mentionne bien
   les fermetures Amselsee/Amselgrund/Kohlichtgraben), baronnies-provencales.fr (Baronnies-GR9,
   à jour du 12/08, liste bien les communes sous arrêté), ouillade.eu (Alberes-66, article du
   29/07 toujours en ligne, contenu conforme).

## Corrections appliquées (à information constante, sans recherche de source nouvelle)

- `fermeture|DE-Sachsen-SaechsischeSchweiz|Malerweg-Bastei-Rathen-Hohnstein-Polenztal-Sturmschaeden|2026-08-01`
  — « Portion concernée » datait du 16/08 alors que `statut:` et « Zone (détails) »
  connaissaient déjà l'état vérifié au 24/08 (aucun changement de périmètre depuis le 18/08) :
  réécrite pour afficher l'état à la date de vérif.
- `incendie|Aude-Montseret-Corbieres|feu-fixe-100ha|2026-08-06` — `validite:` reformulée en
  clair (« aucune restriction en vigueur ») : le champ citait une date de vérification passée
  comme si c'était une échéance, alors qu'aucun arrêté ni fermeture n'existe.
- `incendie|Drome-Bellegarde-en-Diois|feu-massif-Claps-400ha|2026-08-03` — même correction :
  la date de fixation du feu (17/08) n'est pas une échéance, `validite:` reformulée.
- `incendie|Lozere-La-Bastide-Puylaurent|feu-252ha|2026-08-19` — même correction.
- `incendie|Var-Ginasservis|feu-30ha-RD30-coupee|2026-08-14` — même correction.
- `infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15` — `validite:` déjà honnête sur
  le dépassement de l'échéance annoncée (14/08) ; reformulée pour dire explicitement que la
  fermeture est présumée se poursuivre jusqu'à nouvel ordre faute de confirmation, au lieu de
  se lire comme une échéance calendaire dépassée sans suite.
- `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` — même correction sur
  `validite:` (l'échéance du 15/08 est dépassée sans confirmation de réouverture).
- `risque-feu|HautesPyrenees-65|interdiction-feu-massifs-forestiers|2026-07-27` — `validite:`
  précisée « jusqu'à nouvel ordre » : l'arrêté n'a pas d'échéance calendaire annoncée (cf.
  « Zone (détails) » et statut, déjà explicites sur ce point), seul le champ `validite:` ne le
  disait pas assez clairement.

Aucune suppression, aucune fiche réécrite en bloc : uniquement les champs cités ci-dessus,
sur les 15 fiches indiquées par l'audit. `python3 site/build_site.py` → `OK (QA passée)`
après corrections. `python3 site/audit_qualite.py` : 15 → 8 fiches avec constat, 17 → 9
alertes, 1 bloquant inchangé (Samaria, hors périmètre de correction du vérificateur).

## Actions laissées à l'agent de veille (nécessitent une source nouvelle)

- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — BLOQUANT, revérifier
  en priorité (seuil 2 j très dépassé, 10 j).
- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — revérifier (18 j, seuil 12 j).
- `fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26` — revérifier (13 j, seuil
  12 j) ; jamais revérifiée depuis sa détection.
- `fermeture|CH-Europaweg-Randa-Zermatt|fermeture-deviation-seg-27.3|2024-07-03` — revérifier
  (13 j, seuil 12 j) ; jamais revérifiée depuis sa détection.
- `fermeture|TMB-CH-Orsieres|fermeture-deviation-seg-6.35|2026-07-11` — revérifier (13 j,
  seuil 12 j).
- `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` — revérifier (17 j, seuil 12
  j) ; confirmer si les refuges ont rouvert après l'échéance annoncée du 15/08.
- Recommandation de clôture à évaluer (non appliquée d'autorité, contrôle PERTINENCE) : les 4
  feux fixés/éteints sans arrêté ni fermeture de sentier documentés (Aude-Montseret,
  Drôme-Bellegarde-en-Diois, Lozère-La Bastide-Puylaurent, Var-Ginasservis) — clôturer si le
  prochain passage confirme l'absence de toute reprise ou de tout arrêté.
- `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` et
  `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — pas d'action requise sur la
  sévérité (voir contrôle 5 ci-dessus) ; à défaut d'y voir une urgence, une recherche
  ciblée d'une source de presse plus récente resterait utile pour rafraîchir la couverture.