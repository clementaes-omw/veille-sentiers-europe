# Journal des changements

Ce journal démarre le 2026-08-08. Il ne recense pas les runs de veille (chaque run laisse
déjà son digest daté dans `livrables/`) mais les **changements de fabrique** : générateur,
contrôles qualité, CI, présentation. Le `git log` seul ne suffisait plus : le travail de
design du 08/08 s'est retrouvé embarqué dans des commits dont le message parle d'autre
chose, et rien n'expliquait plus pourquoi le générateur définit `--surface-invert` ou
pourquoi le champ de recherche est figé à 16 px.

## 2026-08-08 — Audit design et accessibilité du site

Passage du site au crible des skills de design installées (`ui-ux-pro-max`, ses références
`quick-reference.md` et `pro-rules.md`, et `design-system` pour l'architecture de tokens).
Les mesures ci-dessous ont été prises sur le rendu réel, en thème clair **et** sombre, à
375 px et 1280 px. Elles sont dans `site/build_site.py` (commits `35d4ae7` et `ac0aff6`,
PR #30 et #31 — dont les messages, eux, parlent d'humanisation de la prose et de CI).

### Corrigé

**Contraste.** Deux échecs WCAG AA mesurés. Le chip de filtre actif tombait à 2.34:1 en
thème sombre : `color: #fff` était écrit en dur alors que `--pine` passe du vert foncé au
vert clair. La pastille « clôturé » tombait à 2.77:1 en clair, et pire encore dans une
carte à `opacity: .75`, l'opacité rabotant le contraste de tout son contenu. Résultat après
correction : 0 échec sur 26 paires testées dans les deux thèmes.

**Tokens.** `--ink` désignait la couleur du texte et servait aussi de fond au bandeau de
navigation : en thème sombre le token bascule au crème, et la barre virait au blanc en
haut d'une page noire. Ajout de `--surface-invert` (un fond, sombre dans les deux thèmes)
et de `--on-accent` (le texte posé sur un aplat `--pine`). La palette était recopiée quatre
fois dans le CSS ; elle est maintenant écrite une fois en Python (`PALETTE_CLAIR`,
`PALETTE_SOMBRE`) et interpolée. Les sélecteurs `[data-theme]` existaient sans qu'aucun
sélecteur de thème n'existe dans la page : le bouton a été ajouté (auto / clair / sombre,
mémorisé, appliqué avant le premier pixel pour éviter le clignotement).

**Accessibilité.** Pas de `<html lang="fr">` — le générateur émettait un fragment sans
balise `<html>`, et un lecteur d'écran prononçait « Bagnols-sur-Cèze » avec une voix
anglaise. Les 167 cartes n'avaient aucun titre : sur 30 000 px de page, zéro point de saut.
La ligne de tête (sentiers, gravité, type) devient le `<h3>` de la fiche. Hiérarchie remise
d'aplomb (h1 → h2 → h3, plus aucun saut de niveau), `aria-pressed` sur les filtres dont
l'état n'était porté que par la couleur, région `aria-live` annonçant le nombre de
résultats, lien d'évitement vers le contenu.

**La légende de gravité était une infobulle.** Répétée 71 fois dans l'attribut `title` des
pastilles, donc inatteignable au doigt et au clavier. La clé de lecture du site est
maintenant affichée une fois, en clair, sous les filtres.

**Mobile.** Le champ de recherche à 12.8 px déclenchait le zoom automatique de Safari iOS
au focus, sur le geste principal du site : passé à 16 px. 320 cibles tactiles sous 44 px,
ramenées à 0 (hors liens en ligne dans le texte, que la règle exclut). Les filtres
occupaient 244 px sur sept rangées et repoussaient la première alerte à 674 px, hors écran
sur un petit téléphone : une rangée qui défile les ramène à 48 px, et la première alerte à
551 px.

**URLs.** Les 25 vues étaient des `<button>` sans URL : impossible d'envoyer le rapport du
6 août à quelqu'un, de le mettre en favori, et le bouton Retour du navigateur faisait
sortir du site. Routage par fragment (`#bivouac`, `#rapport-2026-08-06`) avec `pushState`
et `popstate`.

**Référencement.** Ni description, ni Open Graph, ni `robots.txt`, ni `sitemap.xml`, sur un
site dont l'acquisition passe par la recherche et le partage sur forums. Description
générée avec les compteurs du jour, six balises `og:`, et les deux fichiers produits par le
build (donc déployés par `pages.yml`, qui publie tout `site/` — et ignorés par git au même
titre qu'`index.html`).

**Un bug fonctionnel trouvé au passage.** `document.querySelectorAll('.cat')` attrapait
aussi les chips bivouac, qui portent les deux classes : cliquer un filtre bivouac exécutait
en plus le gestionnaire des alertes et basculait l'utilisateur sur la vue Alertes. Corrigé
en `.cat:not(.bcat)`.

**Finitions.** Aucune `transition` n'existait dans la feuille de style, chaque changement
d'état claquait (160 ms, avec repli `prefers-reduced-motion`). Le filtrage repeignait 263
cartes à chaque frappe (debounce 120 ms). 26 tailles de police voisines et 23 valeurs
d'espacement hors grille, remplacées par une échelle de 7 crans et une grille de 4.
L'accroche était en chasse fixe sur six lignes, repassée en sans. Feuille `@media print`
ajoutée, volets « Détails » ouverts le temps du tirage et URL des sources imprimées : on
prépare son étape chez soi et on marche sans réseau.

### Écarté volontairement

**Les icônes.** La règle `no-emoji-icons` était violée par les 16 chips de catégorie. La PR
#29 (`humaniser`) les a supprimés le même jour avec sa propre justification — un emoji
décoratif à côté d'un mot qui dit la même chose est un marqueur d'écriture générée. Aucune
icône SVG n'a été réintroduite : ne rien mettre satisfait la règle et respecte cet
arbitrage éditorial.

**L'indexation par rapport.** Le routage par fragment règle le partage, le favori et le
bouton Retour, mais un fragment n'est pas une page pour un moteur de recherche : les 22
rapports quotidiens ne sont pas indexables séparément, et le sitemap ne déclare que l'URL
canonique. Y arriver demande un build multi-pages.

**Le poids.** ~1 Mo brut / 256 Ko gzip, dont 45 % de vues masquées présentes dans le DOM.
Même refonte multi-pages que ci-dessus.
