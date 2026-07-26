# Courrier Alertes-Rando

Traitement autonome de la boîte `contact@alertes-rando.info`. Architecture et décisions :
[brief-loop-courrier-alertes-rando.md](brief-loop-courrier-alertes-rando.md).

## Ce que fait le dispositif

1. **06h50** — `releve.py` (GitHub Actions) dépose les brouillons validés la veille, relève
   les nouveaux messages, écrit une fiche anonymisée par message dans `entrants/`.
2. **07h07** — l'agent de veille lit ces fiches : il qualifie (Builder), fait auditer le
   résultat par un agent distinct (Vérificateur), et transforme les signalements en
   **pistes à confirmer**, jamais en alertes publiées.
3. **Le lendemain 06h50** — les brouillons validés sont déposés dans le dossier Brouillons
   de la boîte. Clément relit et envoie — ou pas.

## Trois garanties de conception

- **Aucun envoi possible.** Le dispositif n'ouvre que de l'IMAP, jamais de SMTP. « Réponses
  en brouillon uniquement » n'est pas une consigne qu'un modèle pourrait contourner : c'est
  une impossibilité technique.
- **Aucune donnée personnelle dans le dépôt** (qui est public). L'expéditeur n'est jamais
  écrit : il est désigné par un identifiant opaque. Adresses, téléphones et signature sont
  retirés du corps avant écriture. L'adresse de réponse n'existe qu'en mémoire, le temps de
  fabriquer le brouillon.
- **Aucune publication sur simple témoignage.** Un signalement devient une piste datée que
  la veille doit confirmer par une source officielle. C'est ce qui protège la fiabilité du
  site, son seul actif.

## Mise en service — à faire une fois

Créer les deux secrets dans GitHub (Settings → Secrets and variables → Actions → *New
repository secret*) :

| Secret | Valeur |
|---|---|
| `MAIL_USER` | `contact@alertes-rando.info` |
| `MAIL_PASS` | le mot de passe de la boîte |

Puis déclencher une première fois à la main : onglet **Actions** → *Relève du courrier* →
**Run workflow**. Le job doit finir en vert avec « OK — N entrant(s) ».

> Le mot de passe n'est connu que de GitHub (chiffré, jamais affiché dans les logs) et
> d'OVH. Il n'apparaît nulle part dans le dépôt. Si tu le changes chez OVH, mets à jour le
> secret, sinon la relève échouera — visiblement, l'onglet Actions passera au rouge.

## Vérifier sans risque

```bash
python3 courrier/releve.py --autotest   # contrôle l'anonymisation, sans réseau ni secret
```

## Fichiers

| Chemin | Rôle |
|---|---|
| `releve.py` | Relève IMAP, anonymisation, dépôt des brouillons (déterministe, sans LLM) |
| `entrants/` | Une fiche par message reçu, anonymisée, à qualifier |
| `reponses/` | Brouillons rédigés, en attente de dépôt |
| `reponses/deposees/` | Brouillons déjà déposés dans la boîte |
| `etat.json` | Identifiants déjà traités (idempotence) |
| `verdict.md` | Dernier rapport du Vérificateur |
| `agents/` | Les deux prompts : Builder et Vérificateur |
