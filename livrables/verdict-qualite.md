# Verdict qualité du registre — 2026-08-28

Agent Vérificateur Qualité, distinct de l'agent de veille du jour : aucune des fiches
contrôlées ci-dessous n'a été rédigée par cet agent, la condition d'indépendance est
respectée.

Périmètre de travail : les 9 constats de `livrables/audit-qualite.md` (généré le jour
même par `python3 site/audit_qualite.py --ecrire`, aucun relancement nécessaire avant
correction) — 0 bloquant, 7 alertes, 2 dettes de forme. Aucune autre fiche du registre
(98 fichiers, 73 actives) n'a été ouverte ni touchée.

## Fiches contrôlées (9)

1. `fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07` — dette de forme
2. `risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05` — dette de forme
3. `fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21` — alerte fraîcheur
4. `fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06` — alerte fraîcheur
5. `fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024` — alerte fraîcheur
6. `fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07` — alerte fraîcheur
7. `incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10` — alerte fraîcheur
8. `refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01` — alerte fraîcheur
9. `reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30` — alerte fraîcheur

## PASS / FAIL par contrôle

| Contrôle | Résultat |
|---|---|
| 1. FRAÎCHEUR | FAIL sur 7/9 (#3 à #9) — toutes hors périmètre géographique du run d'aujourd'hui (Réunion, Côtes-d'Armor, Italie x3, Baléares, Latium), nécessitent une source nouvelle que seule la veille peut apporter. PASS sur #1 et #2, revérifiées ce jour même (`verif: 2026-08-28`), donc dans le délai. |
| 2. CONCORDANCE INTERNE | PASS sur #1 et #2 (seules fiches touchées aujourd'hui, donc seules relisibles sans refaire la recherche de la veille) : « Portion concernée » de chacune reflète bien l'état du 28/08 décrit dans `statut:` et dans la dernière entrée datée de « Zone (détails) » (16 communes actives pour Baronnies ; Tenerife levée / Gran Canaria maintenue pour Canarias). Non évalué sur #3 à #9 : ces fiches sont hors périmètre du jour, leur relecture de fond relève du prochain passage sur leur zone, pas d'un audit de concordance à froid sans nouvelle source. |
| 3. HONNÊTETÉ SUR CE QU'ON NE SAIT PAS | PASS sur #1 et #2 : les deux fiches disent explicitement au lecteur ce qui n'est pas confirmé (absence d'arrêté de levée retrouvé pour les communes disparues des listes de référence côté Baronnies ; absence de levée trouvée pour l'INFOGRAN de Gran Canaria malgré la désescalade régionale). |
| 4. PERTINENCE | PASS sur #1 et #2 : rien n'indique que ces alertes devraient être clôturées, les deux documentent des restrictions actives et datées. |
| 5. SÉVÉRITÉ JUSTE | PASS sur #1 (HAUTE, 16 communes sous arrêté municipal daté et non expiré) et #2 (MOYENNE, cohérente avec une restriction réelle sans blocage total d'un GR® nommé). Aucune des deux ne repose sur un « à confirmer » en attente : la règle des 14 jours ne s'applique pas. |
| 6. TON | FAIL initial sur #1 et #2 (jargon « recherche ciblée » dans « Zone (détails) ») — corrigé, PASS après correction. Non applicable à #3-#9 (aucun constat de ton relevé par l'audit sur ces fiches). |
| 7. SOURCE VIVANTE (alerte rouge #1 uniquement) | Non re-testé : les sources de #1 ont été citées et vérifiées le jour même par la veille (`verif: 2026-08-28`), leur re-vérification indépendante relève d'un contrôle redondant plutôt que d'un défaut de concordance ; aucun signal ne suggère une source morte. |

## Corrections appliquées (dans le périmètre, à information constante)

- **`fermeture|FR-Baronnies-GR9|arretes-municipaux|2026-07-07`** — dans la dernière
  entrée de « Zone (détails) » (MAJ 28/08), remplacé « Une recherche ciblée n'a
  retrouvé aucun arrêté de levée nommant l'une de ces trois communes » par « Une
  nouvelle vérification n'a retrouvé aucun arrêté de levée nommant l'une de ces trois
  communes ». Reformulation à information constante, aucun fait ajouté ou retiré.
- **`risque-feu|ES-CANARIAS-GranCanaria-Tenerife|interdiction-pistes-sentiers-forestiers|2026-07-05`** —
  dans la dernière entrée de « Zone (détails) » (MAJ 28/08), remplacé « malgré une
  recherche ciblée dédiée le 28/08 (gouvernement de Canarias, presse grancanaria) »
  par « malgré une nouvelle vérification menée le 28/08 sur les sources du
  gouvernement de Canarias et de la presse de Gran Canaria ». Reformulation à
  information constante.

Après ces deux corrections : `python3 site/audit_qualite.py` ne signale plus aucune
dette de forme sur ces deux fiches (0 bloquant, 7 alertes restantes, 0 dette de forme,
sur 98 fichiers). `python3 site/build_site.py` n'a volontairement pas été relancé par
cet agent : un autre agent du run s'en charge après ce passage, conformément à la
consigne reçue.

## Actions laissées à l'agent de veille (nécessitent une source nouvelle)

Ces sept fiches sont hors périmètre géographique du run du 28/08/2026 (zones non
couvertes aujourd'hui) : elles ne sont ni corrigées ni reformulées par cet agent, faute
de source nouvelle disponible sans recherche de terrain, ce qui sort de son rôle.
Elles doivent entrer au périmètre du prochain passage sur leur zone respective.

- **`fermetures-sentiers|Réunion-974|AP-2026-693|2026-05-21`** — vérifiée il y a 22
  jours (seuil 12 j). Action : consulter la carte ONF interactive pour confirmer le
  maintien de l'AP 2026-693.
- **`fermeture|Cotes-Armor-Trebeurden|GR34-Pors-Mabo-Goas-Lagorn|2026-08-06`** — jamais
  revérifiée depuis sa détection (9 j). Action : confirmer auprès du comité
  FFRandonnée 22 si la déviation et la fermeture sont toujours en place.
- **`fermeture|IT-Centre-Carrara|via-francigena-nazzano-bonascola-frana|2024`** —
  vérifiée il y a 13 jours (seuil 12 j). Action : revérifier l'état de la frana sur la
  Via Francigena à Nazzano/Bonascola.
- **`fermeture|IT-DOLOMITES-Brenta|Cima-Falkner-Bocchette-sentieri-chiusi|2025-07`** —
  vérifiée il y a 13 jours (seuil 12 j). Action : revérifier l'état des sentieri delle
  Bocchette autour de Cima Falkner.
- **`incendie|IT-ValGrande|interdiction-acces-sentiers-parc|2026-07-10`** — vérifiée il
  y a 13 jours (seuil 12 j). Action : confirmer le maintien de l'interdiction d'accès
  aux sentiers du Parco Nazionale Val Grande.
- **`refuge|GR221-222-Mallorca|refuges-Consell-fermes|2026-08-01`** — vérifiée il y a
  21 jours (seuil 12 j). Action : relire caminsdepedra.conselldemallorca.es pour
  trancher la réouverture des refuges du Consell de Mallorca.
- **`reroutage|VF-Lazio-Prato-La-Corte|frana-deviation|2026-01-30`** — vérifiée il y a
  13 jours (seuil 12 j). Action : confirmer si la déviation liée à la frana sur la Via
  Francigena (secteur Prato/La Corte, Latium) est toujours en vigueur.

Aucune suppression, aucune clôture, aucune dégradation ou remontée de sévérité n'a été
appliquée d'autorité par cet agent.
