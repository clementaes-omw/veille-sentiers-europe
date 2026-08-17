# Verdict qualité — 2026-08-17

Vérificateur distinct de l'agent de veille du jour. 11 fiches contrôlées, celles listées par
`livrables/audit-qualite.md` (run du 2026-08-17, avant correction) — aucune autre fiche du
dossier n'a été ouverte ni modifiée. Deux fiches de ce lot (`Drome-Justin-Die`,
`Savoie-Planay-Pralognan`) avaient été touchées ce matin par l'agent de veille ; leur contenu
factuel a été confirmé correct, seul le format a été retouché, conformément au principe
« un agent qui valide sa propre production ne valide rien ».

## ⚠️ Chantier de fond à signaler (ne pas traiter au fil de l'eau)

**Bug confirmé dans `site/build_site.py::parse_alerte()`** (non corrigé, hors périmètre de cet
agent) : le parseur ne lit que la PREMIÈRE ligne de chaque champ de front-matter
(`champ: valeur`) ; toute ligne de continuation indentée sans « : » est silencieusement
ignorée — aussi bien par le site que par `audit_qualite.py`. Balayage du dossier complet
(lecture seule, aucune modification) :
- **70 des 89 fiches** ont au moins un champ de front-matter replié sur plusieurs lignes
  (`cle`, `type`, `itin`, `sev`, `validite`, `detection`, `verif`, `statut`, `ordre`).
  La plupart concernent `statut:`, qui est INVISIBLE sur le site et dont le marqueur utile
  (`ACTIF`/`[CLÔTURÉ]`) est toujours en tête de champ : impact pratique nul dans ce cas.
- **16 champs PUBLICS tronqués sur 11 fiches** (hors les 8 déjà corrigées ci-dessous) :
  `fermeture--drome-omblese--…` (sev, validite), `incendie--aude-conques-sur-orbiel--…` (itin),
  `incendie--es-and-niebla--…` (itin, validite),
  `incendie--es-ara-huesca-riglos--…` (itin, validite),
  `incendie--es-cyl-hermisende-sanabria--…` (itin, validite),
  `incendie--gr34-capfrehel--…` (validite), `incendie--herault-34-pegairolles-escalette--…`
  (itin, validite), `incendie--uk-cairngorms-glenmore--…` (validite),
  `risque-feu--gard-30--…` (itin). Ces fiches affichent une phrase coupée en milieu de mot sur
  le site (Itinéraires ou Validité) — c'est le même défaut que celui corrigé ce jour sur
  `Drome-Bellegarde-en-Diois`, `Lozere-Massegros`, `Drome-Justin-Die`, `Savoie-Planay-Pralognan`,
  `Aude-Montseret`. Aucune de ces 11 fiches n'était citée par l'audit du jour : je ne les ai
  donc pas touchées (hors périmètre), mais elles justifient une passe dédiée, pas un
  raccommodage fiche par fiche au fil des audits futurs.

## Corrections appliquées (dans mon périmètre — forme, information constante)

1. **`incendie|Aude-Montseret-Corbieres|feu-fixe-100ha|2026-08-06`** — `validite:` réécrite
   (retire l'auto-référence datée du 14/08 qui se lisait comme une échéance expirée ;
   `itin:` rejointe sur une ligne, elle était tronquée par le bug de parsing).
2. **`incendie|Lozere-Massegros-Causses-Gorges|feu-fixe-153ha|2026-08-09`** — même correction
   (`validite:` et `itin:`).
3. **`incendie|Drome-Bellegarde-en-Diois|feu-massif-Claps-400ha|2026-08-03`** — `validite:` et
   `itin:` rejointes (étaient tronquées : la validité s'arrêtait en plein milieu de phrase sur
   « (« ne » avec un guillemet français non fermé, publié tel quel sur le site).
4. **`incendie|Drome-Justin-Die|foret-fermee|2026-07-02`** — `validite:` rejointe sur une
   ligne (le site affichait « …arrêté du 17/07/2026 » sans fermer la parenthèse). Contenu
   factuel de la mise à jour du jour (dégradation HAUTE→MOYENNE, règle des 14 jours) laissé
   intact : seul le format était en cause, comme annoncé.
5. **`incendie|Savoie-Planay-Pralognan|RD915-refuges-Vanoise|2026-07-07`** — `validite:`
   rejointe sur une ligne (le site affichait « …travaux de » coupé net, sans même mentionner
   la date de fin des travaux). Contenu factuel du jour laissé intact.
6. **`incendie|Var-Ginasservis|feu-30ha-RD30-coupee|2026-08-14`** — `validite:` complétée
   (« sans nouvelle information à la vérification du 17/08/2026 ») pour ne plus se lire comme
   une échéance dépassée alors que la coupure RD30 est un état constaté, pas expiré.
7. **`incendie|Var-Gros-Bessillon|feu-actif-Ponteves-Cotignac-Correns|2026-07-22`** — même
   correction sur `validite:`.
8. **`infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15`** — « Portion concernée »
   et `validite:` réécrites : le texte affirmait au présent que la circulation « sera
   rétablie » le 14/08, date désormais passée sans confirmation. Reformulé pour dire au
   lecteur ce qui est confirmé (annonce APDL du 06/08) et ce qui ne l'est pas (reprise
   effective non reconfirmée) — cf. contrôle HONNÊTETÉ. **Reste listée « à traiter » :
   nécessite une source nouvelle, voir ci-dessous.**

Après ces 8 corrections : `python3 site/build_site.py` → **OK (QA passée)** ;
`python3 site/audit_qualite.py` → passé de 11 à **4 constats, 0 bloquant** (inchangé : le
score bloquant était déjà à 0 avant intervention).

## À traiter au prochain run (nécessite une source nouvelle — hors périmètre)

- **`fermeture|GR-E4-Creta-Samaria|fermetures-meteo-repetees|2026-07-16`** — FAIL contrôle 1
  (FRAÎCHEUR) : `verif: 2026-08-14`, soit 3 j, alors que la fiche annonce elle-même des
  fermetures « décidées au jour le jour » (seuil 2 j). Action : revérifier samaria.gr /
  sources grecques datées, mettre à jour `verif:` et la « Portion concernée » avec le statut
  du jour.
- **`infrastructure|Matosinhos-PT|pont-levadizo-fermé|2026-06-15`** — FAIL contrôle 4
  (PERTINENCE) : la réouverture était annoncée pour le 14/08/2026, désormais passé, sans
  confirmation. Action : chercher une source postérieure au 14/08 confirmant (ou infirmant)
  la reprise de la circulation ; si confirmée, clôturer la fiche.
- **`risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10`** — FAIL contrôle 7 (source
  vieillie, 19 j) sur une alerte ROUGE. J'ai vérifié la source citée (ouillade.eu) : elle est
  vivante et porte bien l'information annoncée (arrêté d'Argelès-sur-Mer du 10/07, dérogation
  VTT du 24/07). **Recommandation : la sévérité HAUTE reste justifiée** — contrairement au cas
  classique de l'« hypothèse non tranchée », cette alerte repose sur deux arrêtés municipaux
  datés et retrouvés (Sorède n°26.216, valide jusqu'au 13/09/2026 ; Argelès ARR2026-024PM,
  « jusqu'à nouvel ordre »), pas sur un « à confirmer ». Action : rechercher une publication
  de moins de 10 j confirmant le statut du jour, sans urgence de dégradation.
- **`risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`** — FAIL contrôle 7
  (source vieillie, 12 j) sur une alerte ROUGE. Source citée (presseagence.fr) vérifiée
  vivante et conforme. **Recommandation : HAUTE maintenue** pour l'instant (fermeture
  quasi quotidienne documentée sur 7 dates distinctes depuis le 17/07, pas de mention
  « à confirmer »/« probable » dans la Portion concernée — le déclencheur des 14 jours ne
  s'applique donc pas littéralement). À surveiller : si aucune publication postérieure au
  06/08 n'est trouvée d'ici le 23/08/2026 (14 j après détection du 09/08), réexaminer la
  sévérité conformément à la règle du prompt.

## Contrôles — bilan sur les 11 fiches

| Contrôle | Résultat |
|---|---|
| 1. FRAÎCHEUR | 10 PASS, 1 FAIL non corrigeable en périmètre (Creta-Samaria, ci-dessus) |
| 2. CONCORDANCE INTERNE | 8 FAIL corrigés (troncature multi-lignes ou auto-référence datée périmée) ; 3 PASS d'emblée (Ginasservis¹, Gros-Bessillon¹, Matosinhos corrigé en 3.) |
| 3. HONNÊTETÉ | 1 FAIL corrigé (Matosinhos) ; 10 PASS |
| 4. PERTINENCE | 11 PASS formel ; 1 recommandation de suivi (Matosinhos, clôture si non reconfirmé) ; note : Montseret et Massegros (feu fixé depuis 11 j / 7 j, aucune fermeture de sentier jamais documentée) sont à surveiller pour clôture si le silence des sources se prolonge encore 2-3 semaines — pas de FAIL aujourd'hui |
| 5. SÉVÉRITÉ JUSTE | 11 PASS — les deux alertes ROUGE (Albères, Esterel-Tanneron) reposent sur des textes datés et non expirés, pas sur une hypothèse ; sévérité maintenue |
| 6. TON | 11 PASS après correction (aucun jargon de veille détecté en public ; aucun tiret cadratin introduit) |
| 7. SOURCE VIVANTE | vérifiée sur les 2 alertes ROUGE du lot (Albères, Esterel-Tanneron) : les deux sources citées répondent et portent bien l'information annoncée |

¹ Ginasservis et Gros-Bessillon avaient un FAIL contrôle 2 au sens strict de l'audit
(validité lue comme expirée) mais la Portion concernée elle-même était déjà exacte — corrigé
par la même réécriture de `validite:`.

## Après correction

- `python3 site/build_site.py` → `OK (QA passée) → site/index.html (71 actives, 18 clôturées, …)`
- `python3 site/audit_qualite.py --ecrire` → **0 bloquant, 4 alerte(s), 0 info(s)** (contre 0
  bloquant, 11 alerte(s) avant intervention). Les 4 constats restants nécessitent tous une
  source nouvelle (voir section dédiée) : ce n'est pas du ressort du Vérificateur.
- Carte : 0 alerte perdue, cohérence inchangée.
