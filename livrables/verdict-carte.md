# Verdict carte — 2026-09-14

Contrôle DÉCLENCHÉ (lundi, jour de cadence) + point prioritaire signalé : le run du jour a créé
3 nouvelles alertes (Benahavís HAUTE, Roncal-Urzainki, Bivacco Gervasutti — digest `77709a4`,
"veille: digest du 2026-09-14"), dont une, `incendie|ES-NAV-Roncal-Urzainki|feu-longue-duree-Pena-Gazpar|2026-08-14`,
dans une zone-source qui n'existait pas jusqu'ici en tant que telle. L'agent de recherche l'a
raccrochée par un **alias manuel dans `site/build_site.py`** (`ALIAS_ZONE`) plutôt que par une
ligne neuve de `referentiel/zones-coords.csv`. C'est le point que ce passage vérifie en priorité,
avant la revue de cadence habituelle.

Base : `python3 site/audit_qualite.py --ecrire` relancé ce jour (section carte : **0 alerte
perdue**, 0 bloquant) ; `livrables/audit-qualite.md` régénéré ; la fiche d'alerte concernée ;
`referentiel/zones-sources.md` (ligne `ES-NAV-RIO-ARA`, tableau T2) ; `site/build_site.py`
(source de l'alias) ; et un script de recoupement indépendant (ci-dessous) qui rejoue
`resolve_zone()` sur les 90 alertes actives du registre pour confirmer le compte de marqueurs.

Je n'ai rédigé aucune des 3 nouvelles fiches (agent de veille) ni posé l'alias (agent de
recherche) : rien à signaler sur la règle « pas de fond » — je contrôle une production qui n'est
pas la mienne.

**90 alertes actives, 38 zones-sources uniques portent au moins une alerte** (0 perdue, 0
bloquant carte, confirmé par script indépendant — voir mission 3). Vérification approfondie sur
les 3 zones touchées par les nouvelles alertes ; revue de cohérence rapide (code vs zone
déclarée) sur les 35 autres zones actives — aucune anomalie relevée.

## 1. `ES-NAV-Roncal-Urzainki` → alias `ALIAS_ZONE["ES-NAV-Roncal-Urzainki"] = "ES-NAV-RIO-ARA"` — CONFIRMÉ, alias en place et centroïde plausible

- **Alias vérifié en place** : `site/build_site.py` ligne 603, dans le bloc « Pyrénées » de
  `ALIAS_ZONE`, aux côtés de `"ES-ARA-Huesca-Riglos": "ES-NAV-RIO-ARA"` (même zone-source, déjà
  utilisée pour une autre alerte active). Le build (`python3 site/build_site.py`) rend
  « OK (QA passée) » sans aucun `⚠ carte`, et l'audit déterministe confirme **0 alerte perdue**.
- **Rattachement de zone** : `referentiel/zones-sources.md` définit `ES-NAV-RIO-ARA` comme
  « Navarra + La Rioja + Aragón (Huesca) », sentiers GR®11 (centre), Baztán, HRMP versant ES. La
  fiche d'alerte situe le feu à **Peña Gazpar, commune d'Urzainki, vallée du Roncal (Navarra)**,
  à quelques km au sud d'Isaba, et cite le GR®11 (étape Isaba↔Zuriza) comme sentier voisin
  [hypothèse non confirmée, signalée comme telle par l'agent de veille — fond hors de mon
  périmètre]. La vallée du Roncal est bien en Navarra, sur l'axe GR®11 couvert par ce code : le
  rattachement au code existant est correct, pas de zone-source neuve à créer.
- **Repère utilisé pour juger le centroïde** : Urzainki / vallée du Roncal se situe vers
  **42,86° N ; -0,94° E** (village d'Urzainki, à ~5 km au sud d'Isaba, Pyrénées navarraises).
  Le centroïde `ES-NAV-RIO-ARA` (42,55 ; -0,70) en est à environ **40 km** — cohérent avec un
  centroïde couvrant une zone qui va de La Rioja à Huesca/Ordesa (centaines de km d'étendue) ;
  le point tombe bien dans les Pyrénées navarraises/aragonaises, pas dans une autre région. Même
  ordre de grandeur que l'écart déjà toléré pour `ES-ARA-Huesca-Riglos` (Riglos, Huesca, à
  ~55 km du même centroïde) sur ce code. **Centroïde plausible, alias correctement ciblé.**
- **Verdict** : alias confirmé, aucune action à porter. Bonne pratique notée pour la suite : cet
  alias a été posé directement dans `build_site.py` par l'agent de recherche sans passer par ce
  contrôle avant sa première publication ; le protocole (mission 1, périmètre) veut que ce soit
  ce rôle qui recommande l'alias — ici le résultat est correct, mais je recommande qu'un alias
  neuf touchant `build_site.py` reste signalé à ce contrôle *avant* le prochain passage de
  cadence plutôt qu'après, pour que la vérification précède la publication plutôt que la suive.

## 2. `ES-AND` (nouvelle alerte `ES-AND-Benahavis`) — centroïde existant, plausible

- Résolution par préfixe (pas d'alias nécessaire) : `ES-AND-Benahavis` → `ES-AND`, code déjà
  présent dans `zones-coords.csv` (37,50 ; -4,60, Andalucía). Aucune ⚠ au build.
- **Repère** : Benahavís (province de Málaga, côte de la Costa del Sol) se situe vers
  **36,53° N ; -5,05° E**. Écart au centroïde régional : ≈ 115 km — important en valeur absolue,
  mais l'Andalousie est une communauté autonome qui s'étend sur ~550 km d'Huelva à Almería ; un
  centroïde unique pour toute la région ne peut pas être plus proche de chaque point sans en
  éloigner d'autres déjà couverts par ce même code. Cohérent avec la doctrine du référentiel
  (centre indicatif de région, pas point exact). **Pas de correction à proposer.**

## 3. `IT-DOLOMITES` (nouvelle alerte `IT-Dolomites-Friuli-Cimoliana`) — centroïde existant, plausible, une réserve mineure de libellé

- Résolution par préfixe : `IT-Dolomites-Friuli-Cimoliana` → `IT-DOLOMITES` (46,40 ; 11,80),
  déjà porteur d'autres alertes actives (`IT-DOLOMITES-Brenta`, `IT-Dolomites-BorcaDiCadore`).
  Aucune ⚠ au build.
- **Repère** : la vallée du Cimoliana / Dolomites frioulanes (secteur de Cimolais, refuges du
  massif du Duranno-Cima dei Preti) se situe vers **46,35° N ; 12,50° E**. Écart au centroïde :
  ≈ 50 km — plausible, le massif dolomitique est continu de ce secteur jusqu'au Trentin-Haut-
  Adige couvert par le même code.
- **Réserve mineure (non bloquante)** : l'intitulé du code en base, « Dolomites (Trentin-Haut-
  Adige, Vénétie) », ne mentionne pas le Frioul-Vénétie Julienne, alors que trois alertes sur les
  cinq portées par ce code touchent désormais des secteurs plus à l'est/sud-est (dont ce
  Cimoliana, en Frioul). Le centroïde reste géographiquement correct ; je recommande seulement,
  la prochaine fois que cette entrée est retouchée pour une autre raison, d'étendre le libellé à
  « … et Dolomites frioulanes » pour qu'il reflète l'usage réel — pas une correction que je fais
  moi-même (entrée existante, hors périmètre).

## 4. Revue de cohérence rapide — 35 autres zones actives

Passage code déclaré / région attendue sur les 35 zones restantes (voir sortie du script de
recoupement, non reproduite en détail ici) : aucun cas du type « GR®10 Ariège pointé sur
l'Espagne » ou « massif corse pointé sur le continent ». Les rattachements observés restent
conformes à `zones-sources.md` (ex. `FR-66` porte Alberes/Canigou/PO-66 ; `FR-PYR-O` porte les 9
zones Pyrénées-Atlantiques/Ariège/Hautes-Pyrénées/Haute-Garonne attendues ; `CH-EST` et
`CH-VALAIS-VAUD` restent bien séparés malgré le rappel historique sur l'ancien repli `DE`).
Aucun centroïde douteux à signaler ce jour en dehors de la réserve de libellé ci-dessus.

## Compte de marqueurs — vérifié

- **Affiché** (`site/index.html`, `#carte-compte`) : « 38 zones en alerte active. »
- **Attendu** (recoupement indépendant, `resolve_zone()` rejoué sur les 90 fiches au statut
  ACTIF du registre) : **38 codes uniques, 0 alerte perdue.**
- Concordance exacte. Confirme aussi le constat de `livrables/audit-qualite.md` (« 0 alerte
  perdue : chaque alerte active se résout vers un marqueur de la carte, le compte de marqueurs
  couvre toutes les actives »).

## Actions à porter (aucune bloquante)

- Aucune alerte perdue à raccrocher ce jour → **aucun ajout à `referentiel/zones-coords.csv`**
  (l'alias en place pour Roncal-Urzainki suffit et est confirmé correct).
- Aucun alias `build_site.py` supplémentaire à recommander.
- Aucun centroïde existant à corriger ; une seule réserve de libellé non bloquante sur
  `IT-DOLOMITES` (§3), à traiter à l'occasion d'une prochaine modification de cette ligne, pas en
  urgence.
- Rappel de process (§1) : faire remonter un besoin d'alias à ce contrôle avant sa pose dans
  `build_site.py`, pas seulement après.
