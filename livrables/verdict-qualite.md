# Verdict qualité — 2026-08-20

Agent Vérificateur qualité, distinct de l'agent de veille du jour. Fiches contrôlées
exclusivement à partir des constats de `livrables/audit-qualite.md` (généré par
`python3 site/audit_qualite.py --ecrire`, régénéré en fin de contrôle). Aucune recherche
web menée : les points qui en auraient nécessité une sont signalés, pas corrigés.

**13 fiches contrôlées** (celles citées par l'audit) : GR-E4-Creta-Samaria,
Réunion-974/AP-2026-693, CH-EST-Trubbach, CH-Europaweg-Randa-Zermatt,
Drome-Bellegarde-en-Diois, Drome-Justin-Die, ES-AND-Niebla, ES-ARA-Huesca-Riglos,
Matosinhos-PT, GR221-222-Mallorca, Alberes-66, FR-06-AlpesMaritimes,
PO-66-Thues-entre-Valls.

## PASS / FAIL par contrôle

1. **FRAÎCHEUR** — FAIL sur 5 fiches : GR-E4-Creta-Samaria (BLOQUANT, 6 j pour un seuil de
   2 j « décidée au jour le jour »), Réunion-974 (14 j / seuil 12 j), CH-EST-Trubbach et
   CH-Europaweg-Randa-Zermatt (jamais revérifiées depuis détection, 9 j), GR221-222-Mallorca
   (13 j / seuil 12 j). Tous hors périmètre (revérification = recherche web) → signalés,
   non corrigés.
2. **CONCORDANCE INTERNE** — FAIL détecté et corrigé sur Drome-Justin-Die (« Portion
   concernée » ignorait un arrêté préfectoral déjà identifié dans `statut:`). FAIL
   technique détecté et corrigé sur 4 fiches (Niebla, Huesca-Riglos, Matosinhos-PT,
   Mallorca) : voir découverte transverse ci-dessous. PASS ailleurs, en particulier
   FR-06-AlpesMaritimes (Portion concernée / statut / Zone détails cohérents entre eux,
   vérifié sans y toucher, conformément à la consigne).
3. **HONNÊTETÉ SUR CE QU'ON NE SAIT PAS** — était en défaut de facto sur Matosinhos-PT et
   Mallorca : la clause déjà écrite (« cette échéance est désormais dépassée… ») n'atteignait
   jamais le lecteur, tronquée par le même défaut technique. Corrigé par le repli de la
   ligne. Ailleurs PASS.
4. **PERTINENCE** — RAS : aucune des alertes signalées par l'audit ne justifie une clôture
   au vu de son propre texte (feux non déclarés éteints/fixés, structures non rouvertes
   confirmées).
5. **SÉVÉRITÉ JUSTE** — Alberes-66 examinée en détail : la sévérité rouge s'appuie sur deux
   arrêtés municipaux datés et non expirés (Sorède jusqu'au 13/09/2026, Argelès-sur-Mer
   « jusqu'à nouvel ordre »), retrouvés et revérifiés les 10/08 et 18/08. Ce n'est PAS un
   « à confirmer »/« probable » au sens de la règle des 14 jours (l'acte existe, il a été
   trouvé) : condition d'application non remplie, pas de dégradation d'autorité.
   FR-06-AlpesMaritimes : dégradation déjà pilotée en interne par la veille (échéance fixée
   au 23/08/2026), pas d'action de ma part, cohérence interne vérifiée PASS.
6. **TON** — FAIL corrigé sur PO-66-Thues-entre-Valls (« malgré une nouvelle recherche
   ciblée » dans Zone (détails), jargon banni, reformulé pour le lecteur).
7. **SOURCE VIVANTE** — non testé : nécessite un accès web, hors périmètre de ce rôle sur
   ce run. À confier au prochain passage de veille, en particulier sur les 2 alertes
   ROUGES du lot (Alberes-66, FR-06-AlpesMaritimes).

## Découverte transverse (au-delà d'une fiche isolée)

`site/build_site.py::parse_alerte` ne lit que la **première ligne physique** de chaque
champ d'en-tête (`cle: valeur`) ; toute continuation indentée sur les lignes suivantes est
silencieusement ignorée, aussi bien pour l'affichage public (`validite` est publié tel quel
sur la carte d'alerte, `build_site.py:440`) que pour les contrôles déterministes d'audit.
Quatre fiches en étaient victimes ce run — leur `validite:` publiée s'arrêtait au milieu
d'une phrase, parfois juste avant la clause d'honnêteté sur une échéance dépassée
(Matosinhos-PT, Mallorca). Corrigé pour les 4 en repliant le champ sur une seule ligne
physique, sans perte de texte (`site/verif_faits.py` : 0 perte/invention sur les 7 fiches
touchées). Ce n'est pas anecdotique : toute prochaine fiche écrite avec une valeur de
frontmatter repliée sur plusieurs lignes sera tronquée de la même façon, sans erreur de
build. À signaler pour correction de fond (proscrire le retour à la ligne dans les valeurs
de frontmatter, ou faire évoluer le parseur) — hors périmètre de ce rôle, je ne touche pas
au code.

## Corrections appliquées (dans le périmètre)

- `incendie|Drome-Bellegarde-en-Diois|feu-massif-Claps-400ha|2026-08-03` — `validite:`
  reformulée : retrait de la mention datée « à la vérification du 17/08/2026 » lue à tort
  comme une échéance expirée par l'audit, remplacée par une clause explicite « jusqu'à
  nouvel ordre (déclaration officielle de fixation du feu) ».
- `incendie|Drome-Justin-Die|foret-fermee|2026-07-02` — `validite:` reformulée ; « Portion
  concernée » mise à jour avec l'arrêté préfectoral n°26-2026-6 du 03/07/2026 (déjà connu
  de `statut:` depuis le 18/08, absent du texte public) ; « Zone (détails) » complétée d'un
  paragraphe MAJ 18/08 reprenant cette même information pour le lecteur.
- `incendie|ES-AND-Niebla|feu-hors-capacite-extincion-20000ha|2026-08-06` — `validite:`
  repliée sur une seule ligne physique (troncature à la publication) + clause « jusqu'à
  nouvel ordre » ajoutée.
- `incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`
  — `validite:` repliée sur une seule ligne physique (même défaut) + clause « jusqu'à
  nouvel ordre » ajoutée.
- `infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15` — `validite:` repliée sur
  une seule ligne physique : la clause d'honnêteté déjà écrite était absente du site publié.
- `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` — `validite:` repliée sur
  une seule ligne physique, même défaut, même effet.
- `incendie|PO-66-Thues-entre-Valls|feu-Caranca-acces-interdit|2026-07-24` — « Zone
  (détails) » : « malgré une nouvelle recherche ciblée » remplacé par « aucun communiqué
  préfectoral plus récent que le CP n°9 (postérieur au 30/07) n'a été retrouvé pour
  confirmer cette information ».

Vérifications après correction : `python3 site/verif_faits.py` → 0 perte/invention sur les
7 fiches touchées. `python3 site/build_site.py` → `OK (QA passée)`. `python3
site/audit_qualite.py` → 0 BLOQUANT sur les fiches touchées (le seul BLOQUANT restant,
GR-E4-Creta-Samaria, n'a pas été touché par moi et reste à traiter par l'agent de veille).

## Actions laissées à l'agent de veille (recherche web requise)

- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — **BLOQUANT** :
  vérifiée il y a 6 j pour un seuil de 2 j. Revérifier le statut du jour sur samaria.gr.
- `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — vérifiée il y a 14 j (seuil
  12 j). Consulter la carte ONF interactive.
- `fermeture|CH-EST-Trubbach|fermeture-deviation-seg-1.1|2026-05-26` — jamais revérifiée
  depuis 9 j : tenter une couverture presse.
- `fermeture|CH-Europaweg-Randa-Zermatt|fermeture-deviation-seg-27.3|2024-07-03` — jamais
  revérifiée depuis 9 j : tenter une couverture presse.
- `infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15` — validité expirée le
  14/08, non prolongée : chercher une confirmation de réouverture (clôturer si confirmée).
- `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` — vérifiée il y a 13 j ET
  validité expirée le 15/08 : chercher une confirmation de réouverture des refuges.
- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — pas de dégradation d'autorité
  (base légale non expirée, voir contrôle 5) ; une publication de presse postérieure au
  29/07 reste utile à trouver pour la fraîcheur narrative, sans urgence.
- Contrôle **SOURCE VIVANTE** non testé sur aucune fiche (hors périmètre) : à faire au
  prochain passage, en priorité sur Alberes-66 et FR-06-AlpesMaritimes (rouges).
- Correction de fond suggérée : le défaut de troncature du frontmatter multi-lignes
  (voir « Découverte transverse ») mérite d'être traité dans `site/build_site.py` ou
  documenté comme interdit dans `agent-prompt.md`, pour éviter sa réapparition.
