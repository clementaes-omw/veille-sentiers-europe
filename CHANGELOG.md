# Journal des changements

Ce journal démarre le 2026-08-08. Il ne recense pas les runs de veille (chaque run laisse
déjà son digest daté dans `livrables/`) mais les **changements de fabrique** : générateur,
contrôles qualité, CI, présentation. Le `git log` seul ne suffisait plus : le travail de
design du 08/08 s'est retrouvé embarqué dans des commits dont le message parle d'autre
chose, et rien n'expliquait plus pourquoi le générateur définit `--surface-invert` ou
pourquoi le champ de recherche est figé à 16 px.

## 2026-08-16 — Le header regroupe les trois vues du corpus

Quatre onglets de même rang, dont « Carte » séparé d'« Alertes actives » par « Bivouac » :
rien ne disait lesquels montrent la même matière. Le header tient maintenant en deux blocs,
**Alertes actives : Carte • Liste • Réglementation bivouac** à gauche, **À propos** à
droite. Les deux s'alignent au pixel sur le `h1` et sur les compteurs du bandeau (120 px et
1160 px à 1280 px de large), pas sur le bord de la fenêtre.

Choix d'accessibilité qui mérite d'être écrit, parce qu'il est contre-intuitif. Une première
version posait un `role="group"` nommé « Alertes actives » sur l'ensemble. Une fois la base
bivouac entrée dans le groupe, ce nom devenait faux : la réglementation n'est pas une alerte,
et un lecteur d'écran l'aurait rangée sous cette étiquette. Le groupe n'a donc plus de nom
propre, et l'étiquette visible n'est plus `aria-hidden` : elle est lue comme du texte, si
bien que l'annonce reprend mot pour mot ce qui est à l'écran. Seules les puces restent
masquées, elles seraient annoncées « puce » entre chaque entrée.

Le sélecteur de thème est retiré : bouton, CSS, script anti-scintillement du `<head>` et
bascule JS. Le thème suit désormais le réglage du système, comme avant son ajout le 08/08 —
`prefers-color-scheme` n'a pas bougé. Les sélecteurs `[data-theme]` de la palette et des
tuiles Leaflet restent en place, inertes : plus rien ne pose l'attribut, mais les retirer
demandait de toucher au rendu sombre de la carte pour un gain nul.

Mesuré : étiquette à 4.98:1 en clair et 6.03:1 en sombre, cibles à 44 px, les trois vues et
leurs fragments (`#carte`, `#bivouac`, racine) inchangés. Sous 760 px la barre défile de
194 px, contre 263 px avant le retrait du bouton de thème.

## 2026-08-16 — Le ton des digests passe du prompt au build

Sept jours après le passage de la skill `humanizer`, les règles d'écriture tenaient : les
digests du 09 au 15/08 ne portaient aucun tiret cadratin ni emoji, et le compteur de jargon
de veille sur les fiches était tombé de 30 à 0, nettoyé au fil des passages par
`agents/verificateur-alertes.md`.

Le run du 16/08 en a réintroduit sept, tous au même endroit : le tiret comme séparateur
d'usage, dans la ligne « Itinéraires » et dans les items de « Levées ou expirées ». Le
prompt l'interdisait depuis le 08/08 ; rien ne le vérifiait. Une règle qu'aucun test ne
défend finit toujours par céder, et elle cède exactement là où le tiret ne ressemble pas à
un tic de style mais à de la mise en forme.

`digest_ton_errors()` contrôle donc les digests comme les fiches : tiret cadratin ponctuant
et emoji sont bloquants, et le message nomme l'occurrence avec son contexte. Le seuil est
posé au 2026-08-09, premier digest écrit sous les nouvelles règles : les précédents sont
l'archive et gardent la prose qu'ils avaient le jour de leur publication. Le prompt liste
maintenant les quatre formes exactes à écrire plutôt que la seule interdiction, puisque
c'est la mise en forme, pas le style, qui a rechuté.

## 2026-08-12 — Les codes de zone nationaux ne portent plus de marqueur

Un code qui couvre un pays entier ne peut pas produire un repère juste. `DE` affichait
l'alerte **rouge** du Malerweg (Suisse saxonne) à 349 km de son massif, en Basse-Franconie,
et le Westweg à 177 km — deux terrains distants de 600 km sous un seul point. `UK-IE`
affichait les Cairngorms dans le Lake District, 289 km au sud.

Trois codes régionaux : `DE-SACHSEN` (Malerweg, repère Bastei), `DE-SW` (Forêt-Noire, sur le
tracé du Westweg), `UK-SCOTLAND` (Highlands, à mi-chemin du Ben Nevis et des Cairngorms), plus
les alias correspondants dans `ALIAS_ZONE`. `FR-NOR` remonte sur la côte d'Albâtre : la zone
s'intitulait « GR21, côte d'Albâtre » mais son point était au sud de l'estuaire de la Seine.
Écarts ramenés à 4, 19, 23 et 11 km. Le compte public passe de 34 à 35 marqueurs.

`DE` et `UK-IE` restent comme replis, sans alerte. Choix de prudence assumé : les retirer
ferait tomber la prochaine alerte non aliasée en constat BLOQUANT — visible tout de suite —
là où les garder la posera en silence sur un centroïde national faux.

## 2026-08-12 — La vue Carte passe l'audit design

L'onglet Carte est arrivé sans repasser par les règles fixées le 08/08. Mesures reprises au
même protocole, sur le rendu réel, en thème clair **et** sombre, à 375 px et 1280 px :
**8 échecs de contraste et 5 cibles tactiles sous 44 px** au départ, 0 et 0 à l'arrivée.

**Contraste : la feuille de Leaflet gagnait la cascade.** Elle est injectée à l'ouverture de
l'onglet, donc en fin de `<head>`, donc *après* le `<style>` de la page : à spécificité égale
c'est l'ordre qui tranche, et nos règles de thème à une seule classe perdaient toutes. Le
fond des popups redevenait blanc en sombre pendant que le texte, lui, suivait le thème et
passait au clair. Nom de sentier mesuré à **1,27:1**. Le lien Leaflet est maintenant inséré
*avant* le premier `<style>` de la page. Deux règles ne suffisaient toujours pas : Leaflet
vise ses contrôles avec deux classes (`.leaflet-touch .leaflet-bar a`,
`.leaflet-container .leaflet-control-attribution`), elles sont donc préfixées par
`.carte-map`.

**Cibles tactiles.** Le marqueur faisait 18 px, les boutons de zoom 30 px, les liens de popup
36 px, le bouton « voir » 23 px, l'onglet Carte 40 px de large. La pastille reste visuellement
à 18 px mais sa cible passe à 44 px (boîte transparente centrée) ; le reste est monté à 44 px.
On vise au pouce, en marchant, parfois avec des gants.

**Titres.** La popup ouvrait un `<h4>` sous le `<h2>` de la vue : saut de niveau, corrigé en
`<h3>`.

**Grille et rythme.** Espacements de la popup remis sur la grille de 4 (`--s-*`), transitions
`--rythme` sur les deux éléments interactifs qui n'en avaient pas. La carte est masquée à
l'impression : sur papier, un fond de tuiles ne rend qu'un rectangle vide.

**Un correctif fonctionnel au passage.** Le `maxBounds` s'arrêtait à 40° E alors que le
marqueur de La Réunion est à 55,52° E : demander à le centrer recalait la vue à 37,92° et le
marqueur restait hors écran au-dessus du zoom 3. L'alerte GRR2 était publiée sur une carte qui
interdisait d'y aller. Limite est portée à 60° E. Les constantes `LEAFLET_*` étaient mortes
(URL et SRI écrits en dur dans le JS, `LEAFLET_VER` sans effet) : elles sont désormais
substituées dans le script.

**Deux pièges rencontrés, notés pour la prochaine fois.** Mesurer un contraste juste après
avoir basculé le thème rend la couleur de *départ* de la transition, pas celle d'arrivée :
il faut laisser passer les 160 ms, faute de quoi on croit à un échec. Et passer un lien en
`display: flex` supprime les espaces HTML entre ses enfants — « GR48-ES » et le type d'alerte
se sont retrouvés collés jusqu'à l'ajout d'un `gap`.

## 2026-08-09 — Les cartes d'alerte se remplissent jusqu'à leur bordure

Correction d'une régression de l'audit de la veille. Le cap de longueur de ligne avait été
posé sur le texte (`max-width: 78ch` sur `.portion` et `.alt`, `90ch` sur `.meta`), à
l'intérieur d'un cadre bordé : à 1280 px, la zone utile d'une carte faisait 822 px et le
bloc « Alternative » s'arrêtait à 658 px. Soit 164 px de vide à droite, et comme ce bloc
porte un fond, une boîte visiblement inachevée.

Une carte est un cadre fermé : la mesure se tient par la largeur de la colonne, pas en
rognant le texte dedans. Les `max-width` internes sont retirés, et `.wrap` passe de 1180 à
1080 px (le bandeau de navigation suit). La colonne principale tombe à 760 px, la carte se
remplit de bord à bord, et la ligne se stabilise à 82 caractères — contre 80 avant, et 93
qu'aurait donnés le plein cadre à l'ancienne largeur.

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
