# Référentiel zones-sources — Veille Sentiers Europe (v2 Europe, 2026-07-17)

**Rôle** : source de vérité du périmètre de veille. L'unité de veille n'est PAS le sentier
mais la **zone-source** : un ensemble d'autorités (préfecture / communauté autonome / canton /
région) dont les publications couvrent d'un coup tous les sentiers qui la traversent.
Périmètre v2 : **Europe de l'Ouest** — France + Réunion, péninsule Ibérique complète,
arc alpin (CH/IT/AT), Allemagne, Benelux, îles Britanniques, Scandinavie, Islande.

**Cadences (le cœur du contrôle de coût)** :
- **T1 — quotidien en saison** : zones à risque saisonnier actif. Saison feux FR/ES :
  15/06 → 30/09. Réunion (cyclones/éboulements) : 15/11 → 30/04.
- **T2 — hebdomadaire en rotation** : le reste, découpé en 6 lots (lundi→samedi, voir §3).
  Dimanche : pas de lot — revue du registre (échéances, validités expirées).
- **T3 — mensuel / événementiel** : zones à très faible signal (bassin parisien, Centre).
- **Escalade** : toute zone portant une alerte ACTIVE de sévérité HAUTE passe en quotidien
  jusqu'à clôture, quelle que soit sa cadence nominale (comportement hérité de la veille OMW).

**Règle de coût par run** : commencer par les agrégateurs transversaux (§4) qui couvrent
beaucoup de zones en 1-2 lectures ; ne descendre au niveau préfecture/presse QUE pour les
zones T1 du jour, le lot T2 du jour, et les zones en escalade. Ne jamais balayer tout le
référentiel en un run.

---

## 1. Zones-sources FRANCE

Préfecture = `https://www.<slug>.gouv.fr`. ⚠ = carte/page JS illisible en autonome →
utiliser le contournement listé (colonnes héritées de la veille OMW, éprouvées été 2026).

### T1 — quotidien en saison feux (15/06 → 30/09)

| Code | Périmètre | Sources socle | Contournements éprouvés | Sentiers majeurs couverts |
|------|-----------|---------------|-------------------------|---------------------------|
| FR-CORSE | 2A + 2B | préfectures ⚠ (carte risque quotidienne JS) ; PNR Corse | corsenetinfos.corsica, alta-frequenza.corsica, France 3 Corse | GR20, Mare a Mare N/C/S, Mare e Monti |
| FR-13 | Bouches-du-Rhône | bouches-du-rhone.gouv.fr ⚠ ; PN Calanques | frequence-sud.fr (articles quotidiens) | GR98, GR51, GR9, GR2013, GR653 (départ Arles) |
| FR-83 | Var | var.gouv.fr ⚠ (carte 19h) ; PN Port-Cros | varactu.fr ; relais mairies (ville-draguignan.fr) | GR51, GR98, GR9, GR49, GR90 |
| FR-06 | Alpes-Maritimes | alpes-maritimes.gouv.fr ; PN Mercantour ; FFRando 06 (fermetures GR, lisible) | presse locale (Nice-Matin ⚠ paywall) | GR5, GR52, GR51, GTM, GR56 (bordure) |
| FR-04-05 | Alpes-de-Hte-Provence + Hautes-Alpes | préfectures ; PN Écrins (actus lisibles) ; PNR Queyras | — | GR5, GR6, GR54, GR56, GR58, GR69 La Routo |
| FR-30-48 | Gard + Lozère | **gard.gouv.fr page actu quotidienne** (lisible, pas de page = pas de « très sévère ») ; lozere.gouv.fr ; PN Cévennes | ⚠ pièges d'indexation pages 2025 homonymes | GR70, GR7, GR44, GR6, GR653, GR65 (bordure 48) |
| FR-34-11 | Hérault + Aude | **aude.gouv.fr « FERMETURE DES MASSIFS » (AP en PDF, lisible)** ; herault.gouv.fr ⚠ | France 3 Occitanie, Hérault Tribune, ICI | GR653, GR7, GR36, GR77, GR78 |
| FR-66 | Pyrénées-Orientales | pyrenees-orientales.gouv.fr ⚠ (tout en JS) | **presse quotidienne OBLIGATOIRE** : L'Indépendant, madeinperpignan, ICI Roussillon (leçon Trévillach : feu de 5 000 ha manqué 8 jours faute de presse) | GR10, GR36, HRP, GR653 (bordure) |
| FR-84-26-07 | Vaucluse + Drôme + Ardèche (Ventoux, Baronnies, Cévennes ardéchoises) | préfectures ; ONF | France 3 / ICI par département | GR4, GR9, GR91, GR42, GR420, GR7 |
| FR-974 | La Réunion (T1 = saison cyclonique 15/11→30/04 ; sinon T2) | PN Réunion ; **ONF « sentiers fermés »** (AP, lisible) | Imaz Press, Clicanoo | GR R1, GR R2, GR R3 |

### T2 — hebdomadaire en rotation (escalade → T1 si alerte HAUTE)

| Code | Périmètre | Sources socle | Sentiers majeurs couverts |
|------|-----------|---------------|---------------------------|
| FR-PYR-O | 64, 65, 31, 09 | préfectures ; PN Pyrénées (actus lisibles) ; gr10.org ; PNR Ariégeoises/Catalanes | GR10, HRP, HRMP, GR78, GR101, GR653, GR65 (fin) |
| FR-ALPES-N | 38, 73, 74 | préfectures ; PN Vanoise ; FFRando comités | GR5, GR55, GR96, TMB, GR738, GTJ (sud), GR9 (nord) |
| FR-MC | 15, 43, 63, 12, 46, 19, 23, 87 | préfectures ; PNR Aubrac/Volcans ; FFRando | GR65, GR400, GR441, GR30, GR4, GR6, GR7, GR652 |
| FR-BRE | 29, 22, 56, 35, 44 | **FFRando comités (source n°1 : érosion/fermetures littoral, lisible)** ; préfectures ; PNR Armorique/Golfe | GR34, GR37, GR38, GR39, GR341 |
| FR-NOR | 76, 14, 50, 61, 27 | FFRando 76 (leçon GR21 : fermetures publiées là, pas en préfecture) ; Conservatoire du littoral | GR21, GR223, GR2, GR36 (ouest), GR22 |
| FR-EST | 59, 62, 80, 02, 60, 08, 51, 10, 52, 54, 57, 55, 67, 68, 88, 70, 25, 39, 90 | préfectures ; PNR Ballons des Vosges ; Club Vosgien (balisage Alsace) ; FFRando | GR5, GR14, GR53, GR531/532, GR59, GR120, GR121, GR145, GTJ |
| FR-SO | 24, 33, 40, 47, 32, 82, 81, 16, 17, 79, 86, 36, 18 | préfectures (40 : feux Landes) ; FFRando | GR65, GR654, GR655, GR36, GR653, GR8, GR4 (ouest) |

### T3 — mensuel / événementiel

| Code | Périmètre | Sentiers majeurs couverts |
|------|-----------|---------------------------|
| FR-IDF-CVL | Île-de-France + Centre-Val de Loire | GR1, GR2, GR3, GR13, GR655 (nord), GR11 (fr) |

## 2. Zones-sources ESPAGNE (Caminos du nord) & PORTUGAL NORD

| Code | Cadence | Périmètre | Sources socle | Sentiers couverts |
|------|---------|-----------|---------------|-------------------|
| ES-GAL | **T1 été** | Galicia | mediorural.xunta.gal ⚠ SSL illisible en autonome (testé 17/07) → **presse socle : Galiciapress, El Progreso, Quincemil (elespanol)** ; X @incendios085 ; incendiosgalicia.net | Francés (fin), Portugués, Inglés, Finisterre-Muxía, Invierno (fin), Sanabrés (fin), Norte (fin), Primitivo (fin) |
| ES-CYL | **T1 été** | Castilla y León (Burgos, Palencia, León, Zamora, Salamanca) | INFORCYL ⚠ JS + medioambiente.jcyl.es ⚠ SSL (testés 17/07) → **presse socle : leonoticias, Diario de León, ileon** ; X @INFOCYL | Francés (Burgos→Ponferrada — fermé ~1 sem. en 08/2025 : Cruz de Ferro), Vía de la Plata, Sanabrés, Invierno (début) |
| ES-NAV-RIO-ARA | T2 | Navarra + La Rioja + Aragón (Huesca) | **navarra.es LISIBLE (validé 17/07)** ; aragon.es lisible mais statique (pas de temps réel) ; larioja.org ⚠ 403 → presse ; Diario de Navarra, Heraldo de Aragón ; PN Ordesa | Francés (début), Aragonés, Baztán, GR11 (centre), HRMP (versant ES) |
| ES-NORTE | T2 | País Vasco + Cantabria + Asturias | euskadi.eus ⚠ SSL (testé 17/07) → presse ; X @112Asturias ; **RTPA + El Fielato validés 17/07 (Asturies)** ; El Diario Montañés, El Comercio | Norte, Primitivo (début), Baztán (fin) |
| ES-CAT | T3 (bonus) | Cataluña (Pyrénées) | interior.gencat.cat (Infocat) [à confirmer] ; PN Aigüestortes | GR11 (est) |
| PT-NORTE | T3 (bonus) | Portugal Norte (Porto→Valença) | **fogos.pt** (agrégateur feux, lisible) ; IPMA ; prociv.gov.pt | Portugués Central + da Costa (tramo PT) |

## 2b. Zones ESPAGNE (extension) / PORTUGAL SUD / ATLANTIQUE & NORD
*(verdicts de lisibilité testés le 17/07/2026 — recherche agent Ibérie/Atlantique)*

| Code | Cadence | Périmètre | Sources socle (avec verdicts lisibilité) | Sentiers majeurs couverts |
|---|---|---|---|---|
| ES-AND | T1 quotidien saisonnier (juin–oct, feux INFOCA + fermetures chaleur) ; T2 hebdo hors saison | Andalousie (8 provinces) | (a) Ventana del Visitante Junta [LISIBLE partiel — avis de fermeture/réouverture sentiers visibles en HTML, carto en JS] ; (b) INFOCA : ⚠ infoca.es = domaine parqué [ERREUR], page Junta incendios-activos [LISIBLE mais coquille vide : données dans visor ArcGIS = JS] ; (c) presse : Diario Sur, Canal Sur, Europa Sur | GR7/E4, Caminito del Rey, Camino Mozárabe, GR247 Bosques del Sur, GR240 Sulayr |
| ES-CENTRO | T2 hebdo, bascule T1 sur épisode feux/canicule été | Madrid, Castilla-La Mancha, Extremadura | (a) pas de portail sentiers unifié → presse + comptes 112 CLM/Extremadura ; (b) Plan INFOEX infoex.info [LISIBLE mais institutionnel — temps réel sur app.infoex.info, probablement JS] ; Plan INFOCAM/GEACAM [non testé] ; (c) presse : Hoy.es, elDiario.es CLM/Extremadura | Vía de la Plata (Mérida–Salamanca), Camino de Madrid, Camino de Levante, GR10-ES |
| ES-LEVANTE | T3 mensuel-événementiel (bascule T2 en épisode feux/DANA) | C. Valencienne + Murcie | presse (Levante-EMV, La Verdad) ; 112 GVA [à confirmer au 1er run] | GR7/E4 (tronçon), GR330, Camino de Levante |
| ES-BALEARES | T3 mensuel-événementiel (torrentades hiver, fermetures refuges, feux ponctuels) | Mallorca, Menorca | (a) caminsdepedra.conselldemallorca.es [LISIBLE — avis fermeture refuges en HTML ; ⚠ redirection 301 depuis .cat] ; Camí de Cavalls/Consell Menorca [non testé] ; (b) IBANAT/112 Illes Balears via presse ; (c) Diario de Mallorca, Menorca.info | GR221 Tramuntana, GR222, Camí de Cavalls (GR223) |
| ES-CANARIAS | T2 hebdo permanent, bascule T1 sur épisode éruptif ou feux | Tenerife, La Palma, La Gomera, El Hierro, Gran Canaria | (a) senderosdelapalma.es [⚠ rétrogradé PARTIEL le 17/07 run 2 : pages lisibles mais TABLEAU d'état non extrait en autonome → presse canarienne] ; ⚠ tenerifeon.es incidences [403 anti-bot] → Teide/Cabildo via presse ; (b) semáforo volcanique IGN/INVOLCAN (relais presse) ; (c) Canarias7, eldia.es | GR131 (toutes îles), GR130 La Palma, sentiers Teide/Anaga, Ruta de los Volcanes |
| PT-CENTRO-SUL | **T1 quotidien saisonnier (mai–oct : régime de feux le plus meurtrier d'Europe, fermetures ICNF récurrentes)** ; T2 hors saison | Portugal centre + Alentejo/Algarve | (a) rotavicentina.com [LISIBLE — bannière risque incendie + carte d'avisos blog.rotavicentina.com/mapa-de-avisos, avis lisibles mais sans géoloc fine] ; (b) fogos.pt [⚠ front JS ILLISIBLE (retesté 17/07 run 2) → **API JSON `api.fogos.pt/new/fires` LISIBLE** : statuts, moyens, surfaces ICNF, KML] + risque ICNF ; (c) Sul Informação, Público | Rota Vicentina (Trilho dos Pescadores + Caminho Histórico), GR15 Guadiana, GR22 aldeias históricas |
| UK-IE | T2 hebdo (pas de régime de feux ; tempêtes/érosion événementiel, wildfire warnings Écosse au printemps) | Angleterre, Écosse, Irlande | (a) nationaltrail.co.uk [LISIBLE mais ⚠ URLs profondes instables → entrer par la home] ; westhighlandway.org [LISIBLE — section « Notices »] ; (b) Scottish Fire and Rescue / Mountaineering Scotland [non testé] ; (c) BBC News régional | Pennine Way, West Highland Way, Coast to Coast, Wicklow Way, Kerry Way |
| SCAND | T2 hebdo en saison (mi-juin–sept : crues de fonte, ponts, météo) ; T3 hors saison | Suède (Laponie), Norvège | (a) ut.no/DNT [LISIBLE partiel — carte en JS] ; STF + Länsstyrelsen Norrbotten [fjallsakerhetsradet.se → 404, à retrouver] ; (b) **varsom.no [LISIBLE — avalanches/crues/glissements en HTML pur]** + yr.no/SMHI ; (c) NRK, SVT Norrbotten | Kungsleden, Padjelantaleden, sentiers DNT (Jotunheimen, Hardangervidda), Besseggen |
| IS | T2 hebdo en saison (juil–sept) + bascule T1 événementielle (éruption, jökulhlaup) | Islande (Hautes Terres) | (a) **safetravel.is [LISIBLE — alertes en HTML ; ⚠ /alerts → 404, entrer par la home]** ; (b) en.vedur.is (Met Office volcanique/hydro) [non testé] + road.is (ouverture pistes F) ; (c) RÚV English, Iceland Monitor | Laugavegur, Fimmvörðuháls, Hornstrandir, Askja |

## 2c. Zones ALPES & EUROPE DU NORD-OUEST
*(verdicts testés le 17/07/2026 — recherche agent Alpes/Nord)*

| Code | Cadence | Périmètre | Sources socle (avec verdicts lisibilité) | Sentiers majeurs couverts |
|---|---|---|---|---|
| CH-VALAIS-VAUD | T2 hebdo | Valais, Vaud | **Officiel : fermetures/déviations Suisse Rando via data.geo.admin.ch layer `ch.astra.wanderland-sperrungen_umleitungen` [LISIBLE/EXPLOITABLE, validé 17/07 run 2 — ⚠ le data.zip ne contient que des métadonnées : utiliser le CSV direct `…/csv/2056/ch.astra.wanderland-sperrungen_umleitungen_line.csv` (879 annonces FR/DE/IT/EN, abstracts parfois vides)]** ; schweizmobil.ch [JS] ; opendata.swiss [403]. Météo : MétéoSuisse [non testé]. Secours : Le Nouvelliste [paywall probable] | TMB (CH), Chamonix-Zermatt, Via Francigena CH, Tour des Combins, GR5/Léman |
| CH-EST | T3 mensuel-événementiel (même flux national que CH-VALAIS-VAUD) | Oberland bernois, Grisons, Tessin | même flux data.geo.admin.ch [LISIBLE] ; Suisse Rando [non testé] ; offices ticino.ch/graubuenden.ch [non testé] | Via Alpina suisse, trekkings Grisons/Tessin |
| IT-NO | T2 hebdo (forte saison estivale TMB/Alte Vie) | Vallée d'Aoste, Piémont, Ligurie | Catasto Sentieri VdA [JS — homepage avec avis lisibles] ; ordonnances regione.vda.it [non testé] ; CAI Piemonte/Liguria [non testé]. Feux/météo : Centro Funzionale VdA, ARPA Piemonte [non testé]. Secours : AostaSera / La Stampa Aosta | TMB (IT), Alta Via 1-2 VdA, GTA, Sentiero Liguria |
| IT-DOLOMITES | T2 hebdo (fréquentation massive, orages/éboulements été) | Trentino-Alto Adige, Veneto, Friuli | SAT sentieri chiusi sat.tn.it [⚠ rétrogradé 17/07 run 2 : page lisible mais elenco/carte des fermetures NON extraits en autonome (JS) → presse l'Adige] ; Provincia Bolzano/CAI Alto Adige [pas de liste centralisée trouvée]. Météo : MeteoTrentino, ARPAV [non testé]. Secours : l'Adige / Alto Adige | Alta Via 1, Alta Via 2, Alpe-Adria (départ) |
| IT-CENTRE | T2 hebdo, **bascule T1 en épisode canicule/feux (Toscane/Latium juil.-août)** | Toscane, Latium, Émilie-Romagne | viefrancigene.org [JS — maillon faible, compenser par presse] ; bollettini antincendio Regione Toscana / Protezione Civile Lazio [non testé]. Secours : La Nazione, Il Tirreno [paywall partiel] | Via Francigena italienne (Cisa→Rome) |
| AT | T2 hebdo | Tyrol, Vorarlberg, Carinthie | alpenvereinaktiv.com [JS] ; alpine-auskunft.at ÖAV [non testé]. Météo : Geosphere Austria [non testé]. **Secours : ORF Tirol tirol.orf.at [LISIBLE — incidents montagne + feux]** | E5 (AT), Adlerweg, Alpe-Adria |
| DE | T3 mensuel-événementiel, bascule T2 en été sec (précédent : feux Sächsische Schweiz 2022) | Forêt-Noire, Rhin/Moselle, Saxe, Thuringe | Schwarzwaldverein, NP Sächsische Schweiz, rheinsteig.de [non testés]. **Feux : DWD Waldbrandgefahrenindex [⚠ retesté 17/07 run 2 : page cadre lisible mais niveaux non extraits (carte/table dynamiques) ; URL CSV opendata.dwd.de à retrouver]**. Secours : presse régionale [paywall partiel] | Westweg, Rheinsteig, Moselsteig, Malerweg, Rennsteig, E5 sud |
| BENELUX | T3 mensuel-événementiel (tempêtes/chablis, sécheresse ; réseau très entretenu) | Belgique, Luxembourg, Pays-Bas | SGR asbl grsentiers.be [⚠ rétrogradé 17/07 run 2 : rubrique GR'Info = archive de newsletters Mailchimp, contenu non lisible en direct → ouvrir la dernière newsletter] ; mullerthal-trail.lu [non testé]. **Feux : brandweer.nl/natuurbrandrisico [LISIBLE — phases par région de sécurité NL]**. Secours : RTBF régions / L'Avenir | GR5 nord, GR57, GR12, Mullerthal, Pieterpad |

## 2d. Zones EXTENSION v3 (19/07/2026 — Scandinavie détaillée, Balkans, Grèce, Tatras)
*(verdicts de lisibilité testés le 19/07 ; SCAND se subdivise en SCAND-NO / SCAND-SE)*

| Code | Cadence | Périmètre | Sources socle (avec verdicts lisibilité) | Sentiers majeurs couverts |
|---|---|---|---|---|
| SCAND-NO | T2 (juin–sept), T3 hors saison | Norvège : Jotunheimen, Hardangervidda, Lofoten | **varsom.no [LISIBLE]** ; ut.no [LISIBLE, carte JS] ; statsforvalteren.no [à valider] | Besseggen, Trolltunga, Hardangervidda, Lofoten, cabanes DNT |
| SCAND-SE | T3 (T2 juil–sept) | Suède : Laponie/Norrbotten | **lansstyrelsen.se/norrbotten « Leder och stugor » [LISIBLE — ponts saisonniers]** ; STF [non testé] ; naturkartan [probable JS] | Kungsleden, Padjelantaleden, Abisko–Nikkaluokta |
| SI-HR | T2 | Slovénie / Croatie | **pzs.si/novice [LISIBLE, alertes datées]** ; **stanje-poti.pzs.si [LISIBLE — fermetures par massif, SANS dates]** ; tnp.si « Current conditions » [LISIBLE] ; gss.hr [SSL expiré → écarter] | Triglav, Juliana Trail, Alpe-Adria, Via Dinarica, Premužićeva staza |
| GR-E4 | T2 (avr–oct), T3 hors saison | Grèce : Crète, Péloponnèse | samaria.gr [LISIBLE, statut réel sur samaria-tickets.necca.gov.gr → fetcher direct] ; civilprotection.gov.gr carte incendie [non testé] ; neakriti.gr [non testé] | E4 Crète (Samaria, Lefka Ori), E4 Péloponnèse, Menalon Trail |
| PL-SK-TATRAS | T2 (T1 possible haute saison — fermetures très fréquentes) | Tatras PL + SK | **tpn.gov.pl/komunikat-turystyczny [LISIBLE]** (⚠ tpn.pl → 301) ; spravatanap.sk [injoignable → fallback presse SK] | Orla Perć, Rysy, Morskie Oko, Tatranská magistrála |

### Densification des sources (19/07) — ajouts par zone existante
- **IT-DOLOMITES** : **ildolomiti.it/montagna [LISIBLE, sans paywall, quotidien]** ; bellunopress [non testé] ; éviter corrieredellealpi (paywall).
- **IT-NO** : genova24.it (Ligurie), torinotoday.it (Piémont) [non testés] ; éviter lastampa (paywall).
- **AT** : salzburg.orf.at, kaernten.orf.at [présumés LISIBLES — même plateforme que tirol.orf.at validé].
- **ES-AND** : europapress.es/andalucia, diariodecadiz.es [non testés] ; ideal.es paywall métré.
- **ES-CANARIAS** : eldia.es et laprovincia.es [BLOQUÉS — Prensa Ibérica] → **eldiario.es/canariasahora** en alternative.
- **UK-IE** : ⚠ walkhighlands et outdooraccess-scotland [403 anti-bot] → fallback BBC Scotland + mountaineering.scot [non testé].
- **FR-PYR-O / FR-ALPES-N** : ⚠ ladepeche.fr, actu.fr, france3-regions [BLOQUÉS en fetch direct] → tester les flux RSS, ici.fr, actumontagne.com ; ledauphine = paywall.
- ⚠ Leçon générale : les grands groupes de presse FR/ES bloquent le fetch direct — privilégier RSS et sources institutionnelles (toutes lisibles : TPN, TNP, PZS, Länsstyrelsen, samaria).

## 3. Cadences consolidées & rotation T2 (calage v2 Europe)

**T1 quotidien en saison feux (15/06→30/09)** : FR-CORSE, FR-13, FR-83, FR-06, FR-04-05,
FR-30-48, FR-34-11, FR-66, FR-84-26-07, ES-GAL, ES-CYL, **ES-AND, PT-CENTRO-SUL** (mai→oct).
Saison cyclonique (15/11→30/04) : FR-974. Bascules T1 événementielles : IT-CENTRE (canicule),
ES-CANARIAS/IS (éruption), toute zone avec alerte HAUTE active.

**Rotation T2 (lun→sam)** :
- lun : FR-PYR-O · ES-NAV-RIO-ARA · ES-NORTE
- mar : FR-ALPES-N · FR-MC · CH-VALAIS-VAUD (+ CH-EST 1 sem./4)
- mer : FR-BRE · FR-NOR · UK-IE · SCAND-NO + SCAND-SE (en saison)
- jeu : FR-EST · AT · SI-HR · PL-SK-TATRAS (+ DE et BENELUX 1 sem./4)
- ven : FR-SO · ES-CENTRO · ES-CANARIAS · GR-E4 (+ FR-IDF-CVL, ES-LEVANTE, ES-BALEARES 1 sem./4)
- sam : IT-NO · IT-DOLOMITES · IT-CENTRE · IS (en saison)
- dim : revue registre (validités expirées, clôtures, échéances).

## 4. Agrégateurs transversaux (chaque run, coût ~2-3 lectures)

- **gronze.com/actualidad** — actu de TOUS les caminos (fermetures, incendies, étapes) ; le
  meilleur ratio signal/coût du périmètre ES. Vérifié 07/2026 (+ forums par camino).
- **caminosantiago.org** (Federación) — communiqués officiels pèlerins.
- **ffrandonnee.fr** actus nationales — modifications officielles de tracés GR®.
- **Météo-France vigilance** (vigilance.meteofrance.fr) [lisibilité autonome à confirmer ;
  sinon relais presse] — uniquement orange/rouge impactant l'accès (critère PRD).
- **AEMET avisos** (aemet.es) — partiellement lisible (liste OK, détail JS ; testé 17/07).
- Leçon 1er run (17/07) : les sites officiels ES tombent massivement en autonome (certificats
  SSL FNMT non vérifiables + JS) → la presse régionale est le SOCLE côté ES, comme pour le 66.
  À tester : agrégateur **incendiohoy.es**.

## 5b. Affectation complète départements → zones (utilisée par sentiers-db.csv)

Chaque département métropolitain est rattaché à UNE zone (les zones T1 gardent leur
découpage fin ; le reste est regroupé dans les lots T2/T3) :

- **FR-CORSE** : 2A, 2B · **FR-13** : 13 · **FR-83** : 83 · **FR-06** : 06 ·
  **FR-04-05** : 04, 05 · **FR-30-48** : 30, 48 · **FR-34-11** : 34, 11, 81 ·
  **FR-66** : 66 · **FR-84-26-07** : 84, 26, 07 · **FR-974** : 974
- **FR-PYR-O** : 64, 65, 31, 09 · **FR-ALPES-N** : 38, 73, 74, 01
- **FR-MC** : 03, 12, 15, 19, 23, 42, 43, 46, 63, 69, 87
- **FR-BRE** : 22, 29, 35, 44, 56 · **FR-NOR** : 14, 27, 50, 53, 61, 72, 76
- **FR-EST** : 02, 08, 10, 21, 25, 39, 51, 52, 54, 55, 57, 58, 59, 60, 62, 67, 68, 70, 71, 80, 88, 89, 90
- **FR-SO** : 16, 17, 18, 24, 32, 33, 36, 40, 47, 79, 82, 85, 86
- **FR-IDF-CVL** : 75, 77, 78, 91, 92, 93, 94, 95, 28, 37, 41, 45, 49
- Hors périmètre : 971, 972, 973, 976, Nouvelle-Calédonie (GR G1/M1/NC1 marqués HP en base).

## 5. Hors périmètre v2 (pour mémoire — extension v3 éventuelle)

Europe de l'Est et Balkans (E3, E8, Via Dinarica), Grèce (E4 sud), Slovénie (tronçon
Alpe-Adria), Finlande (Karhunkierros), Antilles/Guyane/Nouvelle-Calédonie (GR G1/M1/NC1,
marqués HP en base). Les E-paths sont en base (E1-E12) mais ne sont veillés qu'à travers
les tronçons nationaux couverts par les zones ci-dessus.

---
*v1 pilote — 2026-07-17. Sources FR héritées du référentiel OMW v2 (2026-07-01, calé GPX) et
des contournements éprouvés dans le registre été 2026. Sources ES vérifiées par recherche web
le 17/07/2026 sauf mention [à confirmer au 1er run].*
