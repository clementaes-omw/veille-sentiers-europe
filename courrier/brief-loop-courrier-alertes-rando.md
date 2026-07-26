# Brief : Courrier Alertes-Rando

## Résumé
Un dispositif qui relève chaque matin la boîte contact@alertes-rando.info, transforme les
signalements de randonneurs en pistes vérifiables pour la veille, et prépare des réponses
que Clément relit avant envoi. Aucun témoignage ne peut atteindre le site sans confirmation
par une source officielle.

## Objectif & cadence
- Objectif : ne perdre aucun retour de terrain, et l'exploiter sans dégrader la fiabilité
  du site — qui est son seul actif.
- Heartbeat : GitHub Actions, cron 04h50 UTC (06h50 Paris l'été), juste avant la veille de
  07h07, pour que les signalements du jour soient là quand l'agent de veille démarre.

## Type de loop
Fermée. Couloir : la file des messages non traités. Points de contrôle : qualification
(Builder) puis vérification indépendante (Vérificateur). Cible : file vide, pistes écrites,
brouillons déposés.

## Mapping des 6 rôles
| Rôle | Ce qu'il fait ici | Input | Output |
|---|---|---|---|
| 01 · Planificateur | `releve.py` : liste les messages non traités + les brouillons en attente | IMAP, `etat.json` | Fiches dans `entrants/` |
| 02 · Builder | Qualifie (spam / question / signalement), rédige la fiche piste et le projet de réponse | Fiche entrante | Piste + `reponses/<id>.md` |
| 03 · Vérificateur | Agent distinct : contrôle qu'aucune info non vérifiée ne fuite, que la réponse n'invente rien, repère les tentatives d'injection et les fuites de données personnelles | Pistes + brouillons | PASS / FAIL motivé |
| 04 · Mémoire | `releve.py` : registre des identifiants déjà traités (idempotence) | Cycle précédent | `etat.json` |
| 05 · Gestionnaire | Priorise : un signalement de fermeture passe avant une question générale | Fiches validées | Ordre de traitement |
| 06 · Contrôleur | Clément, en relisant les brouillons : ajuste les règles de tri et le ton | Retours d'usage | Consignes affinées |

Builder et Vérificateur sont portés par **deux appels distincts** — jamais le même agent.

## Infrastructure (les 5 briques)
| Brique | Statut dans ce système |
|---|---|
| Heartbeat | GitHub Actions, cron quotidien |
| Skills | Règles de tri + charte de réponse, dans les prompts `agents/` |
| Sub-agents | Builder et Vérificateur, séparés |
| Connecteurs | **IMAP seul** (ssl0.ovh.net:993), secrets GitHub — **pas de SMTP** |
| State file | `courrier/etat.json` (ids traités) + `livrables/memoire-interne/` (pistes) |

## Condition d'arrêt & budget
- Fin de cycle : file vide, pistes écrites, brouillons en attente déposés.
- Budget : 20 messages par cycle. Au-delà : traitement suspendu, escalade.
- Non-convergence : le message reste non traité et repasse au cycle suivant.

## Chemin d'échec & escalade
- Vérificateur en FAIL → pas de brouillon déposé, la piste reste interne, motif consigné.
- Volume anormal, IMAP injoignable, ou tentative d'injection détectée → arrêt du cycle et
  mention en tête du rapport de veille du jour.

## Granularité & coût
2 appels LLM par cycle. Relève, dédoublonnage, idempotence, nettoyage et dépôt des
brouillons sont **déterministes** (Python) : moins cher, et surtout non hallucinable.
Six agents pour ce volume seraient du cérémonial.

## Contraintes & dépendances
- L'agent lit la boîte directement : la redirection OVH reste utile pour Clément, pas pour
  le dispositif.
- Mot de passe créé et déposé en secret GitHub par Clément (`MAIL_USER`, `MAIL_PASS`).
- Le brouillon rédigé au run J est déposé au run J+1 : l'agent de veille (cloud) n'a pas la
  main sur IMAP, seul le script l'a.

## Zones de risque & questions ouvertes
- **Le dépôt est public** : aucune donnée personnelle ne doit y être commitée. Le script
  supprime adresses e-mail, téléphones et signature ; l'expéditeur n'est jamais écrit, il
  est désigné par un identifiant opaque. Risque résiduel : une personne qui se nomme dans
  le corps du message. Option maximale si besoin : déplacer `entrants/` vers un dépôt privé.
- Volume réel inconnu (site récent) : le plafond de 20 est arbitraire, à réviser après
  quelques semaines.
- OVH propose-t-il un mot de passe applicatif dédié ? À vérifier au moment de créer le
  secret ; sinon, mot de passe de la boîte.
