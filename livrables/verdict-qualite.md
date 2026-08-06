# Verdict qualité — 2026-08-06

Agent Vérificateur Qualité, distinct de l'agent de veille qui a produit le run du jour
(2026-08-06 : 3 alertes créées, 7 alertes modifiées dont 2 dégradations HAUTE→MOYENNE,
~20 fiches revérifiées stables). Base de travail : `livrables/audit-qualite.md`, régénéré
en tout début de passage par `python3 site/audit_qualite.py --ecrire` (état frais : 61
alertes actives, 71 fiches au total, **0 fiche avec constat, 0 bloquant, 0 alerte, 0 info**)
et `agent-prompt.md` (§ TON, § DURÉE DE VIE D'UNE HYPOTHÈSE). Aucune fiche non citée par
l'audit n'a été touchée — l'audit n'en citant aucune, aucune fiche n'a été modifiée par ce
passage.

L'audit déterministe étant vide, ce passage s'est concentré, comme demandé, sur ce qu'il ne
peut pas voir : le **contrôle 7 (source vivante)**, en interrogeant en direct les URLs citées
sous les alertes rouges, et une relecture manuelle des fiches touchées aujourd'hui (les 3
nouvelles + les 7 modifiées + les 2 dégradations) pour une deuxième paire d'yeux sur la
concordance interne, l'honnêteté et le ton, au-delà de ce que le script sait détecter.

Fiches dont l'audit dispose (univers de travail) : **71** (61 actives, 10 clôturées).
Fiches avec un constat de l'audit : **0**. Fiches contrôlées manuellement par ce passage :
**19** — les 12 alertes rouges actives (front-matter + Portion + Source relus pour
chacune), les 3 fiches nouvelles du jour, les 2 dégradations HAUTE→MOYENNE du jour, et 2
fiches issues des recommandations du verdict précédent (`ES-AND-Los-Gallardos` candidate à
la clôture, `Réunion-974` ex-bloquant fraîcheur) pour vérifier qu'elles ont bien été
reprises par la veille.
Corrections appliquées : **0** — rien dans mon périmètre n'appelait de correction.

## PASS / FAIL par contrôle

| # | Contrôle | Verdict | Détail |
|---|---|---|---|
| 1 | FRAÎCHEUR | **PASS** | Aucune fiche active en retard de revérification au-delà de son propre seuil (audit : 0 constat). `incendie\|IT-ValGrande\|…` (MOYENNE, `verif: 2026-08-05`, 1 j) est la plus proche du seuil (12 j) sans l'approcher. |
| 2 | CONCORDANCE INTERNE | **PASS** | Aucun décrochage Portion/statut détecté par l'audit ; relecture manuelle des 5 fiches nouvelles/dégradées confirme que « Portion concernée » décrit exactement l'état constaté à `verif:`, y compris pour les 2 dégradations (la Portion des fiches Drôme-Justin-Die et Corse-Bavella-Illarata affiche bien le même 06/08 que `statut:`). |
| 3 | HONNÊTETÉ SUR CE QU'ON NE SAIT PAS | **PASS** | Les 2 dégradations disent explicitement au lecteur ce qui n'est pas publié (« Aucune communication officielle n'a été publiée depuis le 16/07/2026 » ; « aucune source postérieure au 23/07 trouvée, ni levée ni reconduction ») plutôt que de présenter la fermeture comme confirmée. `fermetures-sentiers\|Réunion-974\|…` reste honnête sur le recoupement GR R2 non tranché. `incendie\|ES-AND-Los-Gallardos\|…` continue de dire clairement qu'aucun arrêté d'interdiction n'a été localisé. |
| 4 | PERTINENCE | **PASS avec 1 point de vigilance** | Aucune fiche manifestement obsolète au registre actif. `incendie\|ES-AND-Los-Gallardos\|feu-record-extinguido-5200ha-14morts\|2026-07-09` reste une candidate suivie : feu éteint depuis le 24/07 (13 j à ce jour), toujours aucun arrêté d'interdiction d'accès trouvé malgré plusieurs passages — pas encore au seuil des « trois semaines » du prompt, recommandation de clôture à réévaluer au prochain passage ES-AND si toujours rien. |
| 5 | SÉVÉRITÉ JUSTE | **PASS** | 12 alertes rouges actives, toutes adossées à une fermeture/interdiction sourcée. Les 2 dégradations HAUTE→MOYENNE du jour (Drôme-Justin-Die, Corse-Bavella-Illarata) sont motivées et documentées noir sur blanc pour le lecteur — exactement la recommandation laissée par le verdict du 05/08, correctement exécutée par la veille. `risque-feu\|Var-83\|…` (ré-escalade 4/9→8/9 massifs) et `incendie\|Var-Gros-Bessillon\|…` (feu toujours pas fixé) restent HAUTE à bon droit, sources du jour même. |
| 6 | TON | **PASS sur le périmètre actif** | 0 jargon de veille dans « Zone (détails) » des fiches actives (audit + build). Le build signale encore 5 fiches **CLÔTURÉES** avec du jargon résiduel (« ce run », « run Europe », « indexation », « prochain passage ») — hors périmètre de ce passage (l'audit exclut les clôturées, donc jamais citées), reporté ci-dessous pour la veille. |
| 7 | SOURCE VIVANTE | **PASS** | 11 URLs testées en direct (WebFetch) sous 11 alertes différentes : les 3 nouvelles fiches (nationalpark-saechsische-schweiz.de, oppenau.de, tpn.gov.pl) et 8 sources sous alertes rouges (var.gouv.fr — Gros Bessillon point n°52 ; vaucluse.gouv.fr ; gard.gouv.fr ; seine-et-marne.gouv.fr — Fontainebleau ; firescotland.gov.uk — Cairngorms ; ram05.fr — Hautes-Alpes Bois Noir ; france3-regions.fr — Ariège ; pyrenees-orientales.gouv.fr — PO-66). Toutes répondent et portent bien l'information citée par la fiche — aucune source morte, aucun contenu détourné. Non testées ce passage (budget) : Var-83, Baronnies-GR9, Albères-66 — sans signal d'alarme par ailleurs (audit muet, sources re-datées récemment par la veille). Seule nuance sans conséquence : gard.gouv.fr affiche un tampon « Mis à jour le 27/07 » sur un article resté figé au 23/07 (pas une nouvelle publication, l'agent de veille l'avait déjà correctement traité comme « aucune page postérieure trouvée »). PO-66 : `pyrenees-orientales.gouv.fr/Actualites` confirmé toujours cassé en direct (pagination bloquée sur 2023) — corrobore, sans le contredire, le constat déjà noté par la veille dans `statut:`. |

## Corrections appliquées

**Aucune.** L'audit ne citait aucune fiche, et la relecture manuelle + les contrôles de
source vivante n'ont rien trouvé qui relève de mon périmètre (Portion décrochée, jargon
en champ public, validité expirée non résolue, statut empilé). Le registre publié
aujourd'hui est conforme.

## À traiter au prochain run de veille

**Recommandation de clôture à surveiller (contrôle 4 PERTINENCE, non appliquée
d'autorité) :**
- `incendie|ES-AND-Los-Gallardos|feu-record-extinguido-5200ha-14morts|2026-07-09` — feu
  éteint depuis le 24/07 (13 j), aucun arrêté d'interdiction d'accès jamais confirmé
  malgré plusieurs recherches ciblées. Si le prochain passage ES-AND ne trouve toujours
  rien, l'alerte atteindra le seuil des trois semaines sans restriction officielle :
  passer en `[CLÔTURÉ]`.

**Fraîcheur de source à surveiller (contrôle 7, pas encore en défaut mais proche) :**
- `risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26` — dernier point de
  situation daté et fiable retrouvé : 27/07 (10 j à `verif: 06/08`, juste sous le seuil
  d'alerte de 10 j de l'audit). `pyrenees-orientales.gouv.fr/Actualites` reste bloqué sur
  une pagination cassée (confirmé en direct ce passage : les actualités les plus récentes
  visibles datent de 2023, pas d'entrée 2026 accessible). À re-sourcer en priorité au
  prochain passage PO-66 avant que la staleness ne devienne bloquante.
- `risque-feu|Alberes-66|fermeture-massif-GR10|2026-07-10` — re-sourcée hier à 8 j de
  staleness (ouillade.eu 29/07) ; sans nouvelle source d'ici quelques jours, retombera
  dans la même situation que Drôme/Illarata.

**Dette de forme hors périmètre (jargon de veille dans « Zone (détails) » de 5 fiches
CLÔTURÉES, jamais citées par l'audit qui exclut les fiches closes — signalé par le build,
non bloquant) :**
`incendie|GR20-Albertacce-Niolu|feu-GR20-fermé|2026-07-1…` ·
`incendie|ES-AND-Archez-Competa|feu-actif-confinement-Co…` ·
`incendie|Herault-34-Poussan|feu-garrigue-Gardiole|2026-…` ·
`incendie|ES-CYL-Murias-de-Ponjos|feu-IGR2-proximite-Tor…` ·
`incendie|ES-CYL-Castropodame-La-Bana|feux-IGR2-Castropo…`
(en baisse par rapport au 05/08, où 6 fiches clôturées portaient ce jargon — une a été
nettoyée depuis).

## Vérification finale

`python3 site/audit_qualite.py` → 0 constat sur 71 fiches, 0 bloquant.
`python3 site/build_site.py` → **OK (QA passée)** (61 actives, 10 clôturées, 71 fichiers,
registre 282 920 caractères) ; seul avertissement non bloquant : les 5 fiches closes citées
ci-dessus. Aucun fichier modifié par ce passage.
