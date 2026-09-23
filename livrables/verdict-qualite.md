# Verdict qualité du registre — 2026-09-23

Agent Vérificateur Qualité, distinct des 4 agents de veille parallèles du run du jour.
Aucune des fiches contrôlées ci-dessous n'a été écrite par cet agent : audit mené en toute
indépendance, conformément à `agents/verificateur-alertes.md`.

**Périmètre de ce passage** (fixé par la consigne de lancement, pas par moi) : les fiches de
`livrables/audit-qualite.md` (généré le 2026-09-23, après le run du jour) qui relèvent des
zones touchées aujourd'hui, plus 6 fiches signalées « validité expirée » quelle que soit leur
zone. Les 23 autres constats de l'audit (CH-EST, IT-Dolomites/IT-NO/IT-Centre/IT-ValGrande,
GR-E4, IS-Hautes-Terres, DE-Schwarzwald, FR-IDF-Fontainebleau, VF-Lazio, Lot-Cieurac, et les 4
alertes rouges à source vieillie hors HautesAlpes-BoisNoir) concernent des zones à cadence T2
différente, non revuérifiées aujourd'hui par la veille : je ne les ai pas rouvertes, elles
restent gouvernées par l'audit déterministe tel quel.

**11 fiches contrôlées en détail. 5 corrections appliquées, 6 PASS motivés sans correction
(dont 3 faux positifs de l'audit déterministe), 3 actions laissées à l'agent de veille.**

## PASS / FAIL par contrôle (sur les 11 fiches examinées)

1. **FRAÎCHEUR** — 5 PASS : les 5 fiches touchées aujourd'hui par la veille (Réunion-974,
   ES-CENTRO-Guadalajara-LaMierla, HautesAlpes-BoisNoir, FR-06-AlpesMaritimes, PO-66) sont
   revuérifiées le jour même (`verif: 2026-09-23`). Les 6 fiches « validité expirée » ont une
   fraîcheur correcte par ailleurs (0 à 5 jours), le défaut qu'elles portent est spécifique à
   la validité, pas à la revérification.
2. **CONCORDANCE INTERNE** — 2 FAIL trouvés et corrigés : `risque-feu|FR-06-AlpesMaritimes|…`
   et `risque-feu|PO-66|…`, où « Portion concernée » citait un état du 14/09 alors que le
   suivi (`statut:` et « Zone (détails) ») connaissait déjà le 23/09 — exactement le défaut
   structurel qui justifie ce rôle. 9 PASS après correction sur le reste des 11 fiches.
3. **HONNÊTETÉ SUR CE QU'ON NE SAIT PAS** — 6 PASS sur les fiches à validité expirée : dans
   les 3 cas où l'échéance dépassée est réelle (CH-Vaud-Sainte-Croix-Baulmes,
   ES-ARA-Huesca-Riglos, Pierrefiques-76), le texte dit déjà noir sur blanc que la fin n'est
   pas confirmée — rien à corriger, la règle « absence de signal ≠ levée » déjà en usage dans
   le registre est respectée. Dans les 3 autres (ES-GAL-Quiroga, UK-Cornwall-Tintagel,
   FR-Landes-Gironde), l'audit se trompe de date (voir « Faux positifs » ci-dessous) : le
   texte est déjà honnête, PASS sans y toucher.
4. **PERTINENCE** — 11 PASS. Aucune des fiches examinées ne présente de preuve d'une
   résolution complète qui justifierait une clôture (déviations et chantiers sans
   confirmation de fin, incendie éteint mais accès routier encore réglementé sans date
   confirmée, arrêtés toujours en vigueur à la dernière lecture directe) : aucune clôture
   appliquée, aucune recommandée.
5. **SÉVÉRITÉ JUSTE** — 2 alertes ROUGE examinées. Réunion-974 : HAUTE justifiée par un
   arrêté préfectoral lu intégralement et reconfirmé le jour même (23/09) — PASS.
   HautesAlpes-BoisNoir : HAUTE maintenue malgré un arrêté municipal du 15/08 (39 jours) ;
   la règle des 14 jours ne s'applique pas au sens strict ici, l'alerte n'étant pas adossée à
   un « à confirmer »/« probable » mais à un acte officiel confirmé et reconfirmé
   directement à la source à chaque passage (dont aujourd'hui) — PASS, mais reste signalée
   « à traiter » par l'audit pour une confirmation plus fraîche de l'absence de levée (voir
   actions laissées à la veille).
6. **TON** — 3 corrections appliquées : jargon « recherche ciblée » remplacé par
   « vérification »/reformulé dans `fermetures-sentiers|Réunion-974|…`,
   `incendie|ES-CENTRO-Guadalajara-LaMierla|…` et `incendie|HautesAlpes-BoisNoir|…`. PASS
   après correction ; plus aucune occurrence de jargon dans ces 3 fiches (confirmé par
   relance de l'audit).
7. **SOURCE VIVANTE** — contrôlée sur les 2 alertes ROUGE du lot (minimum exigé par le
   rôle). `ville-argentiere.fr/feu-bois-noir-informations` (HautesAlpes-BoisNoir) : URL
   vivante, confirme l'arrêté municipal du 15/08/2026 pour le secteur du Bois Noir — PASS.
   `ouest-lareunion.com/les-sentiers-ouverts-et-fermes-dans-l-ouest` (Réunion-974) : URL
   vivante, confirme le Bras des Merles toujours listé fermé — PASS, avec une réserve
   mineure : cette page secondaire nomme un arrêté du 29/04/2026 quelque part sur la page,
   différent du n°2026-1617 du 16/09/2026 dont le PDF a déjà été lu intégralement par
   l'agent de veille le 20/09 ; le fait principal (fermeture toujours listée) n'en est pas
   affecté, non retenu comme un défaut de fond. `onf.fr` (source primaire ONF) a renvoyé une
   erreur 503 au moment du contrôle, sans que cela remette en cause la fiche puisqu'une
   autre source officielle du même jour la corrobore.

## Corrections appliquées (périmètre : forme, à information constante)

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — jargon de veille
  « recherche ciblée » dans « Zone (détails) » (MAJ 23/09) reformulé pour le lecteur.
- **`incendie|ES-CENTRO-Guadalajara-LaMierla|feu-record-32000ha|2026-07-16`** — même défaut,
  même correction (MAJ 23/09).
- **`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`** — même
  défaut, même correction (MAJ 23/09).
- **`risque-feu|FR-06-AlpesMaritimes|fermeture-esterel-tanneron|2026-07-17`** —
  « Portion concernée » citait « vérifié le 14/09/2026, soit 14 jours sans nouvelle
  confirmation » alors que le suivi (Zone détails, statut) était déjà au 23/09 (23 jours).
  Date et écart corrigés dans « Portion concernée », à information constante (le fait —
  aucune publication postérieure au 31/08 — ne change pas, seul le compteur était figé).
- **`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`** — défaut
  structurel visé par ce rôle : le `statut:` (invisible) savait déjà, depuis ce matin, que
  les Pyrénées-Orientales étaient repassées en vigilance rouge « très élevé » le 21/09 puis
  en orange le 22/09, et qu'un feu distinct (35 ha, Villeneuve-de-la-Raho, D19 coupée) avait
  eu lieu le 21/09 — mais « Portion concernée » et « Zone (détails) » s'arrêtaient au 17/09.
  Versé dans « Zone (détails) » (nouvelle entrée MAJ 23/09) et répercuté dans « Portion
  concernée », rien n'est perdu ni inventé : tous les faits ajoutés (dates, D19, 35 ha,
  Villeneuve-de-la-Raho) figuraient déjà dans le `statut:` de cette même fiche avant mon
  passage (vérifié dans `git show HEAD` : le run du jour avait déjà écrit ces faits, ils
  n'atteignaient simplement pas le texte public). **Note technique** : `verif_faits.py`
  signale ce déplacement comme une « invention » (19, 21, 22) parce qu'il ne compare que les
  sections publiques à `git HEAD`, sans regarder `statut:`, qui est hors de son périmètre de
  contrôle et hors du périmètre visible du site. Les trois nombres existent déjà dans le
  `statut:` de la version commitée (HEAD) de ce même fichier — ce n'est pas une fabrication,
  c'est exactement le déplacement statut → chronologie que ce rôle est chargé de faire.

Après ces 5 corrections : `python3 site/audit_qualite.py --ecrire` → 34 → **29 constats**
(les 5 constats visés par ces corrections ont disparu, aucun nouveau n'apparaît).
`python3 site/build_site.py` → **OK (QA passée)** (100 actives, 34 clôturées, 134 fichiers,
aucune fiche sous le seuil d'intégrité de 45 %).

## PASS motivés sans correction

### Fiches à validité expirée revues (6, toutes zones confondues, comme demandé)

- **`fermeture|CH-Vaud-Sainte-Croix-Baulmes|Gorges-Covatannaz-travaux|2026-08-17`** —
  échéance réelle (déviation « jusqu'au 18/09/2026 ») dépassée. Le texte le dit déjà
  explicitement (`validite:`, « Portion concernée ») et n'affirme ni réouverture ni
  prolongation faute de vérification du flux data.geo.admin.ch postérieure au 15/09 : PASS,
  rien à corriger. Reste « à traiter au prochain run » (relecture directe du flux, entrée id
  2600748) — nécessite une source nouvelle, hors périmètre.
- **`incendie|ES-ARA-Huesca-Riglos|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee|2026-08-10`**
  — échéance réelle (route A-1603 réglementée « jusqu'au 15/09/2026 au moins ») dépassée. Le
  texte le dit déjà explicitement, sans documenter de levée : PASS. Reste « à traiter au
  prochain run » : réouverture de la route A-1603, statut du monastère au public, état du
  Camino Aragónés lui-même — trois points nécessitant une source nouvelle.
- **`reroutage|Pierrefiques-76|déviation|2025-05-18`** — échéance réelle (travaux « jusqu'au
  18 septembre 2026 ») dépassée. `validite:` dit déjà « échéance atteinte sans confirmation
  de réouverture », MAJ 20/09 documente la recherche infructueuse : PASS. Reste « à traiter
  au prochain run » (FFRando Seine-Maritime, mairie de Pierrefiques) — source nouvelle, hors
  périmètre.

### Faux positifs de l'audit déterministe (contrôle « validité expirée »)

Le script retient mécaniquement la date la plus tardive *citée* dans `validite:`, qu'elle
décrive une échéance réelle ou tout autre événement daté. Dans ces 3 cas, la date retenue
n'est pas une échéance de restriction : le texte est déjà honnête et à jour, aucune
correction nécessaire.

- **`incendie|ES-GAL-Quiroga|feu-pacios-da-serra-420ha|2026-09-15`** — le 18/09 cité est la
  date à laquelle le feu a été déclaré « contrôlé » (controlado), pas une échéance de
  fermeture ; aucune fermeture du Camino de Invierno n'est même documentée.
- **`fermeture|UK-Cornwall-Tintagel|SWCP-effondrement-inondation|2025-12-18`** — le 18/12/2025
  cité est la date de départ de la fermeture, pas une échéance ; `validite:` dit déjà
  explicitement « aucune date de réouverture annoncée ». Fiche créée aujourd'hui (détection
  23/09), source officielle unique (South West Coast Path), sévérité MOYENNE cohérente.
- **`risque-feu|FR-Landes-Gironde|vigilance-rouge-bivouac-interdit|2026-07-21`** — le 18/09
  cité est la date de la dernière vérification de la fiche, pas une échéance ; le niveau de
  vigilance en vigueur (Gironde JAUNE depuis le 08/09, Landes ORANGE depuis le 14/09) est
  suivi et daté correctement, et la fraîcheur (5 j) est sous le seuil de 12 j pour une
  sévérité MOYENNE.

## Actions laissées à l'agent de veille (nécessitent une source nouvelle, hors périmètre)

| Clé | Constat | Action attendue |
|---|---|---|
| `fermeture\|CH-Vaud-Sainte-Croix-Baulmes\|Gorges-Covatannaz-travaux\|2026-08-17` | échéance du 18/09 dépassée, non confirmée | relire directement le flux data.geo.admin.ch (entrée id 2600748) pour savoir si la déviation Gorges de Covatannaz a été levée |
| `incendie\|ES-ARA-Huesca-Riglos\|feu-camino-aragones-monastere-san-juan-de-la-pena-fermee\|2026-08-10` | échéance du 15/09 dépassée, non confirmée | vérifier la réouverture de la route A-1603 (Santa Cruz de la Serós ↔ Botaya), l'accès au monastère de San Juan de la Peña, et l'état du Camino Aragónés lui-même |
| `reroutage\|Pierrefiques-76\|déviation\|2025-05-18` | échéance du 18/09 dépassée, non confirmée | revuérifier auprès de FFRando Seine-Maritime / mairie de Pierrefiques si le chantier de la station d'épuration de Beaurepaire est achevé et le chemin de la Dragonnerie rouvert |

Par ailleurs, toujours ouvert et hors périmètre de correction pour ce rôle (signalé par
l'audit, contrôle « source vieillie sous une alerte ROUGE ») :
`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19` — la source
la plus récente listée dans « Source » date du 24/08 (30 j) ; le fond de la fermeture est
confirmé aujourd'hui directement à la source (ville-argentiere.fr, vérifié par ce rôle,
vivante et conforme), mais une confirmation officielle plus fraîche (recueil des actes
administratifs, presse) reste à trouver pour clore ce point de l'audit.

Les 23 autres constats de `livrables/audit-qualite.md` (zones CH-EST, IT-Dolomites/IT-NO/
IT-Centre/IT-ValGrande, GR-E4, IS-Hautes-Terres, DE-Schwarzwald, FR-IDF-Fontainebleau,
VF-Lazio, Lot-Cieurac, et les 4 alertes rouges à source vieillie hors HautesAlpes-BoisNoir)
sont hors périmètre de ce passage : cadence T2 différente, non couvertes par le run du jour,
non rouvertes par ce rôle. Ils restent gouvernés par l'audit déterministe tel quel.

## Statut final

`python3 site/audit_qualite.py --ecrire` → 29 constats (0 bloquant), en baisse depuis les 34
du début de ce passage. `python3 site/build_site.py` → **OK (QA passée)** (100 actives, 34
clôturées, 134 fichiers). Aucune fiche supprimée, aucune sévérité dégradée ou remontée
d'autorité, aucune fiche hors de la liste de travail (audit + les 6 fiches « validité
expirée » nommément désignées) n'a été touchée. Aucune publication git effectuée par ce
rôle, conformément à la consigne.
