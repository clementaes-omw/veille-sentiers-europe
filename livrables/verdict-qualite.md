# Verdict qualité — 2026-09-04

Agent Vérificateur Qualité, distinct de l'agent de veille qui a produit le run du jour.
Périmètre : les 5 constats de `livrables/audit-qualite.md` (généré par
`python3 site/audit_qualite.py --ecrire`, 0 bloquant / 5 alerte / 0 info sur 105 fiches).
Aucune fiche hors de cette liste n'a été touchée.

**5 fiches contrôlées.** 3 corrections appliquées (reformulations à information constante).
0 dégradation de sévérité appliquée. 2 actions laissées à l'agent de veille.

---

## 1. `incendie|Ariege-Bordes-Uchentein|GR10-ferme-Esbintz-Valier|2026-07-10`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | PASS — vérifiée le jour même (04/09) |
| Concordance interne | FAIL → **corrigé** |
| Honnêteté sur ce qu'on ne sait pas | PASS |
| Pertinence | PASS |
| Sévérité | PASS |
| Ton | PASS |
| Source vivante | PASS |

- **Concordance** : « Portion concernée » se terminait sur « vérification du 28/08/2026 »
  alors que `statut:` (vérif 04/09) et la chronologie de « Zone (détails) » (MAJ 02/09)
  attestaient déjà un état plus récent, inchangé. Corrigé à information constante : la date
  est recalée sur 04/09, le fait rapporté (aucune réouverture annoncée) ne change pas.
- **Sévérité** : l'audit signale une alerte rouge appuyée sur une source du 18/08 (17 j).
  Vérifié : `statut:` justifie explicitement le maintien HAUTE sur un fait de terrain
  (chutes de pierres sur sol déstabilisé par l'incendie, tronçon Ayès↔Cap des Lauses),
  distinct et indépendant de l'arrêté préfectoral d'interdiction du feu qui, lui, est
  échu. Ce n'est pas une hypothèse « à confirmer »/« probable » au sens de la règle des
  14 jours, mais un constat matériel étayé par 3 sources de presse indépendantes et
  datées (France 3 Occitanie 04/08, ruralites2024.fr 03/08, radiocouserans.fr 02/08),
  ce qui satisfait par ailleurs l'exigence de 2 sources indépendantes pour une alerte
  rouge. **Aucune dégradation recommandée.**
- **Source vivante** : France 3 Occitanie (04/08) revérifiée en direct — en ligne, contenu
  conforme (fermeture GR®10 Ayès↔Cap des Lauses, chutes de pierres).

## 2. `incendie|Drome-Justin-Die|foret-fermee|2026-07-02`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | PASS |
| Concordance interne | FAIL → **corrigé** |
| Honnêteté | PASS |
| Pertinence | PASS |
| Sévérité | PASS |
| Ton | PASS |
| Source vivante | PASS |

- **Concordance** : même défaut que la fiche précédente, « Portion concernée » figée sur
  « vérification du 29/08/2026 » pendant que `statut:` (04/09) confirmait déjà l'absence de
  changement. Date recalée sur 04/09, aucun fait ajouté ni retiré.
- **Sévérité** : l'audit signale une source du 21/08 (14 j). `statut:` justifie
  explicitement le maintien HAUTE : l'arrêté préfectoral du 21/08/2026 est un acte
  officiel en vigueur, pas une hypothèse non confirmée, et il n'a volontairement aucune
  échéance calendaire (fermeture liée à une étude de risque en cours) — l'écoulement des
  jours ne l'invalide donc pas comme le ferait un arrêté à durée fixe non reconduit. La
  règle des 14 jours, qui vise les hypothèses « à confirmer »/« probable », ne s'applique
  pas à un acte confirmé. **Aucune dégradation recommandée.**
- **Source vivante** : mairie-die.fr revérifiée en direct — en ligne, arrêté du 21/08/2026
  confirmé (interdiction d'accès aux forêts de Justin, Laup et Solaure-en-Diois).

## 3. `incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | **FAIL** (vérifiée il y a 13 j, seuil MOYENNE 12 j) |
| Concordance interne | PASS |
| Honnêteté | PASS |
| Pertinence | PASS |
| Sévérité | PASS (MOYENNE cohérente : 80 % du massif rouvert, fermeture résiduelle localisée) |
| Ton | PASS |
| Source vivante | non contrôlée (hors périmètre obligatoire : alerte MOYENNE, hors zone du run du jour) |

Fiche hors périmètre du run d'aujourd'hui, non revue par la veille depuis le 22/08. Le FAIL
fraîcheur demande une source nouvelle (le détail cartographique des parcelles encore
fermées et son recoupement avec les GR® n'est toujours pas publié par la préfecture) : ce
n'est pas mon rôle d'aller la chercher. **Recommandation : à inscrire au périmètre du
prochain passage**, avec pour objectif précis de vérifier si la fermeture résiduelle
(parcelles brûlées + zone tampon) est toujours en vigueur et si le détail par tracé GR® a
été publié depuis.

## 4. `incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | **FAIL** (vérifiée il y a 16 j, seuil MOYENNE 12 j) |
| Concordance interne | PASS |
| Honnêteté | PASS |
| Pertinence | à surveiller (voir ci-dessous) |
| Sévérité | PASS (MOYENNE cohérente : arrêté municipal, déviation balisée existante, pas de blocage total) |
| Ton | PASS |
| Source vivante | non contrôlée (hors périmètre obligatoire, hors zone du run du jour) |

Fiche hors périmètre du run d'aujourd'hui. Elle n'a été vérifiée qu'une seule fois (19/08)
depuis sa détection tardive (12/08, soit un mois après l'incendie du 12-13/07). L'arrêté
municipal du 15/07 ferme la portion « le temps que la végétation se régénère », sans
échéance annoncée — ce type de fermeture temporaire est justement celui qui risque le plus
d'être levé sans que le site s'en aperçoive. **Recommandation : à inscrire en priorité au
périmètre du prochain passage**, pour vérifier si la portion Cap Fréhel ↔ Fort La Latte a
rouvert (arrêté municipal levé) depuis le 19/08.

## 5. `incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`

| Contrôle | Verdict |
|---|---|
| Fraîcheur | PASS |
| Concordance interne | FAIL (mineur) → **corrigé** |
| Honnêteté | PASS |
| Pertinence | PASS |
| Sévérité | PASS |
| Ton | PASS |
| Source vivante | PASS |

- **Concordance** : « Portion concernée » indiquait « Vérifié à nouveau le 02/09/2026 »
  alors que `statut:` (vérif 04/09) précise qu'une nouvelle recherche ciblée a bien été
  menée le 04/09, sans rien trouver au-delà du constat du 02/09. Corrigé à information
  constante : la phrase distingue maintenant la date de la dernière vérification (04/09)
  de la date du dernier fait constaté (02/09), sans ajouter ni retirer d'information.
- **Sévérité** : l'audit signale une source du 24/08 (11 j). `statut:` justifie
  explicitement le maintien HAUTE : l'arrêté municipal du 15/08/2026 est un acte officiel
  en vigueur, présenté par la mairie elle-même comme valable « en attendant l'ensemble
  des avis des autorités compétentes », sans échéance — la règle des 14 jours (hypothèses
  non confirmées) ne s'applique pas à un acte confirmé. **Aucune dégradation
  recommandée.**
- **Source vivante** : ville-argentiere.fr revérifiée en direct — en ligne, arrêté du
  15/08/2026 confirmé (interdiction d'accès et de circulation dans le secteur du Bois
  Noir).

---

## Corrections appliquées

Les 3 corrections suivantes sont des reformulations à information constante (recalage
d'une date de vérification citée en « Portion concernée » sur l'état déjà présent dans
`statut:`/« Zone (détails) »), conformes au périmètre autorisé. Aucun fait ajouté, retiré
ni modifié.

- `livrables/alertes/incendie--ariege-bordes-uchentein--gr10-ferme-esbintz-valier--2026-07-10.md`
- `livrables/alertes/incendie--drome-justin-die--foret-fermee--2026-07-02.md`
- `livrables/alertes/incendie--hautesalpes-boisnoir--gr54a-ferme-argentiere-freissinieres--2026-07-19.md`

Vérification post-correction : `python3 site/build_site.py` → **OK (QA passée)** (76
actives, 29 clôturées, 47 digests, registre 105 fichiers). `python3 site/audit_qualite.py
--ecrire` relancé → toujours **0 bloquant**, mêmes 5 alertes (attendu : elles portent sur
la fraîcheur des sources/vérifications dans le frontmatter, pas sur le texte public
retouché).

## Actions laissées à l'agent de veille (prochain run)

1. **Fontainebleau** (`incendie|FR-IDF-Fontainebleau|foret-fermee-arrete-jusqua-26-07|2026-07-12`)
   — revérifier la fermeture résiduelle (parcelles brûlées + zone tampon) et chercher le
   détail cartographique par tracé GR®, non publié à ce jour.
2. **GR34 Cap Fréhel** (`incendie|GR34-CapFrehel|fermeture-lande-fort-la-latte|2026-07-15`)
   — priorité : vérifier si l'arrêté municipal du 15/07 (fermeture pour régénération de la
   végétation, sans échéance) a été levé ; une seule vérification en un mois et demi
   d'existence de la fiche.

Aucune autre action : sur les 3 alertes rouges (Ariège, Drôme, Hautes-Alpes), le motif de
sévérité HAUTE est déjà justifié en clair dans `statut:` par un fait de terrain ou un acte
officiel sans échéance, distinct d'une hypothèse non confirmée — pas de recherche de
source supplémentaire à mener sur ce point précis.

VERIFICATEUR QUALITE COMPLETE
