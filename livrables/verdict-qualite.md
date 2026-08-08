# Verdict qualité — 2026-08-08

Vérificateur distinct de l'agent de veille du jour ; aucune des fiches auditées n'a été
écrite par ce vérificateur. Périmètre : la fiche citée par `livrables/audit-qualite.md`
du 2026-08-08 (0 bloquant, 1 alerte, 0 info), et elle seule.

## Fiche contrôlée : 1

**`risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26`**
(`livrables/alertes/risque-feu--po-66--vigilance-rouge-fermeture-tous-massifs--2026-07-26.md`)

| Contrôle | Verdict | Détail |
|---|---|---|
| 1. Fraîcheur | PASS | `verif: 2026-08-08` (aujourd'hui) ; seuil HAUTE = 4 j, `validite:` en "nouvel ordre" → validité ouverte, non expirée. |
| 2. Concordance interne | FAIL → **corrigé** | « Portion concernée » affichait encore « Vérifié au 03/08 » alors que `statut:` portait une recherche du 07/08 (page des communiqués d'août accessible, aucun communiqué sur le risque incendie). Réécrit à information constante : la portion reflète maintenant l'état constaté le 07/08, sans levée trouvée au-delà du 27/07. |
| 3. Honnêteté sur l'inconnu | PASS (après correction) | Le texte dit explicitement qu'aucune levée/reconduction n'a été retrouvée et que la fermeture est maintenue par défaut faute de signal contraire. |
| 4. Pertinence | RAS, à surveiller | Fermeture généralisée « tous massifs » sans confirmation explicite depuis le 27/07 (12 j). Pas de marqueur « à confirmer/probable » dans la portion → la règle des 14 jours ne s'applique pas encore (elle jouerait à partir du 2026-08-10). Recommandation, non appliquée : prioriser une recherche ciblée d'un communiqué post-27/07 dès le prochain passage sur PO-66. |
| 5. Sévérité juste | PASS | HAUTE justifiée par 3 sources de presse indépendantes et datées citant explicitement la préfecture (France3, Seven Radio, info.fr). |
| 6. Ton | PASS | Aucun jargon de veille détecté dans « Portion concernée »/« Alternative » (confirmé par l'audit, 0 info) ; « ce run », « lot T2 » etc. absents. |
| 7. Source vivante | PASS | Les 3 URLs de la section Source ont été rouvertes (WebFetch) : toutes répondent et portent bien le contenu annoncé (vigilance rouge, fermeture des 9 massifs, reconduction du 27/07). L'alerte de l'audit (« source datée du 28/07, 11 j ») porte sur l'ANCIENNETÉ de l'information, pas sur une source morte — voir action laissée ci-dessous. |

## Correction appliquée hors périmètre strict, requise pour publier

**`incendie|HautesAlpes-BoisNoir|GR54A-ferme-Argentiere-Freissinieres|2026-07-19`**
(`livrables/alertes/incendie--hautesalpes-boisnoir--gr54a-ferme-argentiere-freissinieres--2026-07-19.md`)
— non citée par l'audit qualité, mais `python3 site/build_site.py` échouait en bloquant
(`[page] markdown gras non rendu (** résiduel)`) : un `**` ouvrant du 26/07 dans
« Zone (détails) » n'était jamais refermé (terminé par un guillemet `»` orphelin au lieu
de `**`). Correction mécanique d'un seul caractère, aucune information ajoutée ni retirée,
nécessaire pour que le site reste publiable.

## Action laissée à l'agent de veille (prochain passage sur PO-66)

- `risque-feu|PO-66|vigilance-rouge-fermeture-tous-massifs|2026-07-26` : rechercher une
  publication plus récente que le 27/07 (arrêté, communiqué préfecture, presse) confirmant
  le maintien ou la levée de la vigilance rouge « tous massifs ». Zone en surveillance
  rapprochée : si aucune confirmation n'est trouvée d'ici le 2026-08-10 (14 j après
  détection), appliquer la règle de dégradation du prompt si la portion venait à retomber
  sur un marqueur « à confirmer »/« probable ».

## Non touché (hors liste de travail de l'audit)

6 fiches restent signalées par le build (WARN non bloquant, jargon dans « Zone (détails) » :
« ce run », « recherche ciblée », « run europe », « indexation », « prochain passage »).
Non citées par `audit-qualite.md` de ce jour → non touchées par ce vérificateur, à nettoyer
au prochain passage de la veille sur ces fiches (GR20-Albertacce-Niolu, ES-AND-Archez-Competa,
Herault-34-Poussan, ES-CYL-Murias-de-Ponjos, ES-CYL-Castropodame-La-Bana, ES-AND-Los-Gallardos).

## Build

`python3 site/build_site.py` → **OK (QA passée)** (60 actives, 11 clôturées, 22 digests ;
registre 320998 car. / 71 fichiers).
