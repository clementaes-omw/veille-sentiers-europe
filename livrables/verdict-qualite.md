# Verdict qualité — 2026-08-11

Vérificateur qualité, agent distinct de la veille du jour (5 agents parallèles, digest
`livrables/digest_2026-08-11.md`). Aucune recherche web menée : audit de ce qui est déjà
publié, à partir de `livrables/audit-qualite.md` (régénéré avant contrôle, 8 constats sur
78 fiches, 0 bloquant) et des fiches qu'il cite.

**9 fiches contrôlées** : les 8 citées par l'audit-qualite.md du jour, plus 1 fiche non
citée par l'audit mais dont l'échec d'intégrité du build (`site/build_site.py`) a été
tracé jusqu'à sa cause (voir en bas de ce document).

## Résumé PASS/FAIL par contrôle

| Contrôle | Résultat |
|---|---|
| 1. FRAÎCHEUR | FAIL sur 4 fiches (Samaria, Foradada del Toscar, Cairngorms, Gros Bessillon) — hors périmètre du vérificateur, cf. « à traiter au prochain run » |
| 2. CONCORDANCE INTERNE | FAIL trouvé et corrigé sur 1 fiche hors liste (Écrins-GR54 : Alternative recommandait un itinéraire fermé pour incendie) ; PASS sur les 8 fiches de la liste |
| 3. HONNÊTETÉ | PASS sur les 9 fiches : chaque incertitude est déclarée en clair au lecteur |
| 4. PERTINENCE | PASS — aucune fiche à clôturer identifiable sans nouvelle source |
| 5. SÉVÉRITÉ JUSTE | PASS — aucune dégradation à recommander d'autorité ; voir note Albères-66 ci-dessous (règle des 14 jours vérifiée et jugée non applicable) |
| 6. TON | FAIL corrigé sur 4 fiches (jargon de veille dans un champ public) ; voir détail |
| 7. SOURCE VIVANTE | Non vérifiable sans accès web dans ce passage ; aucune URL manifestement morte relevée à la lecture |

## Corrections appliquées (dans mon périmètre, à information constante)

- `incendie|ES-AND-Niebla|feu-hors-capacite-extincion-20000ha|2026-08-06` — jargon
  « indexation »/« piège d'indexation » dans « Zone (détails) » reformulé pour le lecteur
  (le fait — un article sur un feu en Galice était un recyclage de bilans 2025, sans lien
  avec Niebla — est conservé intégralement).
- `risque-feu|Corse-Bavella-Illarata|fermeture-preventive|2026-07-18` — jargon
  « recherche ciblée » dans « Zone (détails) » (MAJ 11/08) reformulé en « nouvelle
  vérification des arrêtés n°2A-2026-07-20-00006 et -00007, cherchés par leur numéro ».
- `risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17` — jargon
  « en autonome » dans « Zone (détails) » reformulé (la carte Entente Valabre existe mais
  son contenu JavaScript n'a pas pu être consulté).
- `incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16` — un tiret
  cadratin dans un titre de source cité en plein texte de « Zone (détails) » remplacé par
  une virgule (même titre, même page, aucune perte d'information).

## Correction appliquée hors liste de l'audit (intégrité du build)

`site/build_site.py` a bloqué la publication (« QA ÉCHEC », site NON écrit) sur
`conditions|Écrins-GR54|enneigement-conditions|2026-06-24` : le run du jour avait
condensé un `statut:` empilé sur plusieurs semaines (07/08 → 03/08 → 31/07 → 29/07 →
27/07) en un seul paragraphe du 11/08, faisant perdre 63 % du texte du fichier — le
garde-fou anti-corruption exact que ce rôle existe pour attraper. Cette fiche n'est pas
citée par `audit-qualite.md` (qui ne contrôle pas l'accumulation de `statut:`), mais son
échec bloquait la publication de tout le site : je l'ai donc traitée, strictement dans
mon périmètre (« un statut devenu un journal empilé → ramené à l'état courant, historique
versé dans la chronologie de Zone (détails). Rien ne se perd, tout se déplace »).

- **Restauration** : l'historique complet (MAJ 27/07, 29/07, 31/07, 03/08, 07/08) a été
  reformulé pour le lecteur (sans jargon : « fetch direct », « un run antérieur », « au
  prochain passage » supprimés à information constante) et versé dans « Zone (détails) »,
  qui n'a donc pas rétréci. Le `statut:` garde le résumé courant du 11/08 écrit par la
  veille du jour.
- **Défaut plus grave trouvé en le lisant** : le champ « Alternative » de cette fiche
  recommande toujours « la variante GR54A » pour contourner le col de l'Aup Martin. Or le
  GR54A est fermé depuis le 19/07/2026 pour incendie sur le massif du Bois Noir (fiche
  `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres`, sévérité HAUTE,
  toujours active). C'est exactement le défaut structurel décrit dans « Pourquoi tu
  existes » de mon prompt de rôle : un texte public qui recommande une variante fermée
  pendant que d'autres fiches du même site savent qu'elle est fermée depuis trois
  semaines. Corrigé : « Alternative » avertit maintenant explicitement que le GR54A est
  fermé, renvoie vers la fiche Bois Noir, et cite le repli officiellement confirmé (GR54
  classique par le col de l'Aup Martin) — sans trancher la question, non résolue par une
  source postérieure au 02/07, de savoir si les conditions de neige début de saison qui
  déconseillaient ce même passage sont encore d'actualité mi-août : je ne l'ai pas
  inventée, je la signale ci-dessous à la veille.

## À traiter au prochain run (hors périmètre du vérificateur — nécessite une source neuve)

- `fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16` — dernière
  vérification datée du 07/08 (4 jours), alors que la fiche affirme elle-même des
  fermetures « décidées au jour le jour » (seuil de fraîcheur : 2 jours). Consulter
  samaria.gr pour le statut du jour et re-vérifier au minimum tous les 2 jours tant que le
  régime de fermetures répétées est en vigueur.
- `incendie|ES-ARA-Huesca-Viu-Foradada-del-Toscar|feu-foudre-GR11-haute-montagne|2026-08-04`
  — la seule échéance connue (dernier point 06/08) est dépassée de 5 jours. Chercher une
  source postérieure (Aragón/Huesca, GR11) pour confirmer si le feu à Foradada del Toscar
  est éteint, en décrue, ou toujours actif ; réécrire la validité en conséquence ou
  clôturer si éteint.
- `incendie|UK-Cairngorms-Glenmore|wildfire-Strathnethy-C7-fermee|2026-07-16` — la
  fermeture générale a déjà été levée le 07/08 (sévérité dégradée HAUTE→MOYENNE ce
  jour-là), mais l'échéance citée dans `validite:` est elle aussi dépassée. Chercher une
  mise à jour firescotland.gov.uk/cairngorms.co.uk postérieure au 07/08 pour confirmer
  l'état des fermetures résiduelles (Ryvoan Trail, Lodge Trail, secteur Abernethy) et, si
  elles sont levées, clôturer ou dégrader encore.
- `incendie|Var-Gros-Bessillon|feu-actif-Ponteves-Cotignac-Correns|2026-07-22` — feu
  déclaré FIXÉ le 07/08 mais non éteint (surveillance ~450 pompiers). Chercher une mise à
  jour var.gouv.fr postérieure au 08/08 : si aucune reprise n'est confirmée après
  plusieurs jours de surveillance, la fiche est mûre pour une clôture ou une nouvelle
  dégradation de sévérité ; sinon documenter la reprise.

## Note motivée — Albères-66, règle des 14 jours vérifiée et jugée non applicable

`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` est une alerte rouge détectée le
20/07/2026 (22 jours). L'audit du jour la signale pour une source de presse vieillie (29/07,
13 jours). Avant d'agir, j'ai vérifié précisément le critère de la règle des 14 jours
(`agent-prompt.md` § DURÉE DE VIE D'UNE HYPOTHÈSE) : elle s'applique à une alerte rouge
dont la « Portion concernée » repose sur « à confirmer », « probable », « non localisé »
ou « recoupement en cours ». Ce n'est pas le cas ici — la « Portion concernée » ne
contient aucun de ces marqueurs, elle affirme des faits déjà noyautés dans deux arrêtés
municipaux nommés et datés (Sorède n°26.216, Argelès-sur-Mer / ARR2026-024PM). La mise à
jour du 10/08, faite par la veille du jour avant mon passage, a déjà répondu au fond au
signalement de l'audit : les deux arrêtés ont une validité qui ne périme pas comme une
page d'actualité (Sorède court par construction jusqu'au 13/09 ; Argelès est « jusqu'à
nouvel ordre », sans clause de reconduction à surveiller). Je n'ai donc appliqué aucune
dégradation : ni le fait matériel (source de presse vieillie) ni le critère textuel de la
règle des 14 jours ne la justifient ici. Pas de jargon trouvé dans les champs publics de
cette fiche.

Point à recouper (observation, pas une action) : le lien PDF cité dans « Source » porte le
numéro « arrêté 26.238 », alors que le texte de la fiche cite « arrêté n°26.216 » pour
Sorède. Les deux nombres ne se recoupent pas explicitement dans le texte actuel — à
clarifier au prochain passage sur la zone (peut-être deux arrêtés distincts, à confirmer).

## Vérifications techniques après corrections

- `python3 site/audit_qualite.py --ecrire` : 5 constats restants (les 4 « validité
  expirée, source neuve requise » + Albères-66 source vieillie), **0 bloquant**, contre 8
  constats avant ce passage.
- `python3 site/build_site.py` : **OK (QA passée)** → `site/index.html` (65 actives, 13
  clôturées, 78 fichiers). Le « ⚠ ton » résiduel (9 fiches) ne concerne que des fiches non
  citées par l'audit du jour, donc hors périmètre de ce passage (règle : une fiche non
  citée par l'audit ne se touche pas).
