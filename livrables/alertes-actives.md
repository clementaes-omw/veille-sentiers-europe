# Alertes actives — Veille Sentiers Europe (pilote)

REGISTRE PERSISTANT. État courant des restrictions/changements sur les sentiers du périmètre
pilote (France + Caminos ES). Mémoire de l'agent veille-europe : sert à ne remonter dans le
digest QUE le NOUVEAU ou le CHANGÉ. Les items inchangés voient seulement leur « Dernière
vérif » mise à jour. Les items expirés/levés passent en [CLÔTURÉ] (date), pas supprimés.
*Amorcé le 2026-07-17 par import du registre de la veille OMW (mêmes alertes France).*

**Clé** = `type|zone|objet|date-d'effet` (stable d'un run à l'autre).

| Clé | Type | Portion concernée | Alternative | Zone (détails) | Itinéraires | Sévérité | Validité | 1ère détection | Dernière vérif | Source | Statut |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| réglementation\|Écrins\|bivouac\|2026-06-19 | réglementation | Cœur du PN des Écrins — bivouac réglementé partout ; **interdit à moins de 500 m des lacs Lauvitel et Muzelle**. | Bivouac autorisé 19h→9h, 1 nuit/site. | Écrins (cœur) | GR54 / Tour Oisans-Écrins | MOYENNE | arrêté directeur 16/06/2026 | 2026-06-19 | 2026-07-23 | [ecrins-parcnational.fr](https://www.ecrins-parcnational.fr/actualite/reglementation-bivouac-evolue) | ACTIF — règle à documenter (non revérifiée le 25/07) |
| risque-feu\|Corse\|interdiction-feu\|2026-06-15 | risque feu / accès | Tout le GR20 : **feux/réchauds interdits du 15/06 au 30/09**. | Sentier ouvert hors Albertacce et Bavella. | Arrêté-cadre « fermeture massifs 2026 » | GR20 | MOYENNE | interdiction feu 15/06→30/09/2026 | 2026-06-29 | 2026-07-25 | haute-corse.gouv.fr | ACTIF — INCHANGÉ 25/07 |
| refuge\|Canigou-Cortalets\|fermeture-travaux\|2026-05 | refuge / reroutage | Refuge des Cortalets (GR10) fermé ~3 ans travaux. | Aucune solution officielle. | Canigou (Mariailles↔Batère) | GR10 | MOYENNE | ~3 ans | 2026-05-20 | 2026-07-17 | gr10.org | ACTIF |
| reroutage\|Pierrefiques-76\|déviation\|2025-05-18 | reroutage | GR21 Beaurepaire-Pierrefiques, jusqu'au 18/09/2026. | Déviation officielle. | 76 | GR21 | MOYENNE | jusqu'au 18/09/2026 | 2025-05-18 | 2026-07-22 | FFRando | ACTIF |
| reroutage\|GR21-Loges-Bénouville\|glissement-fermeture\|2026-02-17 | reroutage / fermeture locale | GR21 Loges-Bénouville fermé. | Déviation FFRando. | 76 glissement | GR21 | MOYENNE | provisoire | 2026-07-12 | 2026-07-22 | [FFRandonnée](https://www.ffrandonnee.fr/s-informer/actualites/le-sentier-gr-2-1-provisoirement-ferme-pres-d-etretat) | ACTIF [HYPOTHÈSE] |
| réouverture\|Boréon-Mercantour\|post-Alex\|2026 | réouverture | GR52 Boréon b377→380 fermé. | Déviations balisées. | Boréon (06) | GR52 / GTM | INFO | rouvert via déviations | 2026-06-29 | 2026-07-25 | mercantour-parcnational.fr | ACTIF — INCHANGÉ 25/07 |
| accès\|Calanques-13\|risque-feu-4couleurs\|2026-06-01 | accès / risque feu | **Désescalade 2 jours consécutifs (24-25/07) : 0 massif fermé.** | GR98/GR51 praticables. | Confirmé 25/07 (cg13.eway.fr) | GR51 & GR98 [HYPOTHÈSE] | MOYENNE (depuis HAUTE) | quotidienne | 2026-06-01 | 2026-07-25 | [cg13.eway.fr](https://cg13.eway.fr/conditions.php) | ACTIF — **CHANGÉ 25/07 : sévérité → MOYENNE** |
| risque-feu\|Var-83\|fermetures-massifs-rouges\|2026-07-01 | fermeture massif / risque feu | Épisode 01-02/07 terminé. | Sans objet. | Var | GR51 & GR98 | HAUTE | terminé | 2026-07-03 | 2026-07-04 | var.gouv.fr | [CLÔTURÉ] (2026-07-04) |
| reroutage\|GR34-Finistère\|fermetures-érosion-2026\|2026-S1 | reroutage / fermetures locales | GR34 : 15+ fermetures/déviations (29). | Déviations locales. | Finistère | GR34 | MOYENNE | variable | 2026-07-03 | 2026-07-22 | [FFRando 29](https://finistere.ffrandonnee.fr/html/6831/actualites) | ACTIF |
| reroutage\|GR34-rade-de-Brest\|nouveau-tracé-officiel\|2026-05-28 | reroutage pérenne | GR34 nouveau tracé côtier 29km. | Ancien coexiste. | Rade de Brest | GR34 | MOYENNE (haute trace) | pérenne | 2026-07-03 | 2026-07-22 | [FFRando 29](https://finistere.ffrandonnee.fr/html/6831/actualites) | ACTIF |
| réglementation\|PN-Pyrénées\|baignade-lacs-interdite\|2026-06-15 | réglementation | Baignade interdite lacs cœur PN Pyrénées. | Sans objet. | Cœur PN Pyrénées | GR10 / HRP / HRMP | MOYENNE | permanente | 2026-07-02 | 2026-07-05 | pyrenees-parcnational.fr | ACTIF |
| conditions\|Écrins-GR54\|enneigement-conditions\|2026-06-24 | info sentier / conditions | Aup Martin déconseillé → GR54A. | Variante GR54A. | GR54 | GR54 | MOYENNE | temporaire | 2026-07-02 | 2026-07-25 | ecrins-parcnational.fr | ACTIF — **⚠ GR54A recommandé est fermé pour incendie** |
| sentiers\|Mercantour\|etat-sentiers-2026\|2026-05-15 | reroutage / info sentier | GR56A dévié ; GR52 gués ; GR5 hiver fermé. | Déviation Cimet. | Mercantour | GR56 / GR52-GTM / GR5 | MOYENNE | pérenne/saisonnier | 2026-07-02 | 2026-07-25 | mercantour-parcnational.fr | ACTIF |
| risque-feu\|Morbihan-56\|fermeture-massifs\|2026-06-23 | fermeture massif / risque feu | Épisode 23-29/06 terminé. | Levé 29/06. | Est/Nord 56 | GR34 | MOYENNE | LEVÉ | 2026-07-02 | 2026-07-04 | morbihan.gouv.fr | [CLÔTURÉ] (2026-07-04) |
| risque-feu\|Gard-30\|fermetures-5-secteurs-rouges\|2026-07-01 | risque feu / fermeture massifs | Gard Rhodanien ACTIVE EN CONTINU. | GR70 libre ; GR653 à risque. | Gard | GR70 ; GR653 | HAUTE | journalière | 2026-07-04 | 2026-07-25 | gard.gouv.fr 23/07 | ACTIF — INCHANGÉ 25/07 [données incomplètes] |
| fermetures-sentiers\|Réunion-974\|AP-2026-693\|2026-05-21 | fermetures sentiers | Sentiers fermés AP 2026-693. | Carte ONF. | La Réunion | GR R2 | MOYENNE | jusqu'au prochain AP | 2026-07-04 | 2026-07-04 | ONF Réunion | ACTIF [HYPOTHÈSE] |
| risque-feu\|Aude-11\|fermeture-5-massifs-saison\|2026-07-03 | risque feu / fermeture massifs saisonnière | 5 massifs fermés 03/07→31/08. | Zones vertes matin. | Aude | GR36 & GR78 [HYPOTHÈSE] | MOYENNE | 03/07→31/08/2026 | 2026-07-06 | 2026-07-25 | aude.gouv.fr | ACTIF — INCHANGÉ 25/07 |
| risque-feu\|Hérault-34\|fermetures-massifs-quotidiennes\|2026-07-02 | risque feu / fermeture massifs (journalier) | Carlencas fixé depuis 08/07. | Aucune fermeture GR653. | GR653 distinct de Carlencas | GR653 (34) | MOYENNE | journalière | 2026-07-06 | 2026-07-25 | France 3 08/07 | ACTIF — nouveau feu Poussan en ligne dédiée |
| incendie\|GR20-Albertacce-Niolu\|feu-GR20-fermé\|2026-07-12 | incendie / fermeture sentier | **GR20 Asco↔Ciottulu ROUVERT** ; Tighjettu↔Ballone fermé. **Restonica 860 ha.** | Navette Ascu↔Verghju. | Albertacce fixé 21/07 | GR20 | HAUTE | Albertacce fixé ; Restonica active | 2026-07-15 | 2026-07-25 | corsenetinfos.corsica ; France3 Corse | ACTIF — **CHANGÉ 25/07** |
| risque-feu\|Var-83\|fermetures-massifs-quotidiennes\|2026-07-08 | risque feu / fermeture massifs (journalier) | **TOUS massifs Var fermés depuis 25/07.** | Aucune alternative. | Bulletin préfecture 24/07 ; Gros Bessillon | GR51, GR98, GR90, GR9 | HAUTE confirmée | fermeture totale 25/07 | 2026-07-09 | 2026-07-25 | Préfet du Var 25/07 | ACTIF — **CHANGÉ 25/07 : désescalade 24/07 INFIRMÉE** |
| incendie\|PO-66-Trévillach\|feu-4900ha-zone-interdite\|2026-07-04 | incendie / fermetures post-incendie | Zone brûlée ~5000 ha. **GR10 non concerné.** | Aucune déviation. | Feu du 04/07 fixé | GR36 [HYPOTHÈSE] | HAUTE | durable | 2026-07-14 | 2026-07-25 | Préf. 66 n°18 | ACTIF — INCHANGÉ 25/07 |
| risque-feu\|Morbihan-56\|restrictions-80-communes\|2026-07-07 | risque feu / restrictions accès massifs + canicule | 80 communes, échu 15/07. | Expirées. | GR34 littoral | GR34 (56) [HYPOTHÈSE] | MOYENNE | ÉCHUES | 2026-07-11 | 2026-07-17 | morbihan.gouv.fr | [CLÔTURÉ] (2026-07-17) |
| reroutage\|GR10-Luchon-Superbagnères\|nouveau-tracé-pérenne\|2024-05-30 | reroutage pérenne | Nouveau tracé rouvert 30/05/2024. | Suivre balisage. | 31 | GR10 | INFO | pérenne | 2026-07-07 | 2026-07-07 | FFRandonnée | ACTIF |
| incendie\|ES-AND-Archez-Competa\|feu-actif-confinement-Competa\|2026-07-17 | incendie / évacuations | Feu Árchez sans activité depuis 18/07. | Aucune alternative. | A-7206 non reconfirmée | GR249, GR242 [HYPOTHÈSE] | MOYENNE | sans activité | 2026-07-17 | 2026-07-25 | Andalucía Información | ACTIF — INCHANGÉ 25/07 : 7e run sans nouvelle |
| incendie\|IT-ValGrande\|interdiction-acces-sentiers-parc\|2026-07-10 | incendie / interdiction d'accès | Val Grande révoqué 17/07 sauf Premosello. | Reste rouvert. | Colloro→Alpe Lut/i Curt | Sentiero Italia CAI [HYPOTHÈSE] | MOYENNE | levée partielle | 2026-07-17 | 2026-07-25 | parcovalgrande.it | ACTIF — INCHANGÉ 25/07 |
| fermeture\|TMB-CH-Orsieres\|fermeture-deviation-seg-6.35\|2026-07-11 | fermeture / déviation | TMB Prayon↔Branche dévié. | Nouveau tracé. | Orsières | TMB | MOYENNE | 11/07/2026→07/07/2027 | 2026-07-17 | 2026-07-21 | FFRandonnée | ACTIF |
| refuge\|GR221-222-Mallorca\|refuges-Consell-fermes\|2026-08-01 | refuge | Refuges Consell fermés 01→15/08. | Aucune alternative. | GR221/222 | GR221, GR222 | MOYENNE | 01→15/08/2026 | 2026-07-17 | 2026-07-17 | caminsdepedra | ACTIF |
| reroutage\|VF-Lazio-Prato-La-Corte\|frana-deviation\|2026-01-30 | reroutage / fermeture locale | Prato La Corte fermé (glissement). | Via dell'Ara. | Parco di Veio | Via Francigena (P1) | MOYENNE | temporaire | 2026-07-17 | 2026-07-25 | parcodiveio.it | ACTIF — INCHANGÉ 25/07 |
| infrastructure\|Matosinhos-PT\|pont-levadizo-fermé\|2026-06-15 | infrastructure / traversée coupée | Pont mobile fermé piétons. | Bus gratuit 15min. | Camino Portugués da Costa | Camino Portugués da Costa | INFO | 15/06→fin 09/2026 | 2026-07-17 | 2026-07-17 | Gronze | ACTIF |
| risque-feu\|Corse-Bavella-Illarata\|fermeture-preventive\|2026-07-18 | risque feu / fermeture massif (préventive) | **Bavella rouvert. Illarata : 4 secteurs fermés** (interdiction générale levée). | Aucune pour 4 secteurs. | Arrêté 20/07 | GR20 (Bavella rouvert) | MOYENNE (depuis HAUTE) | 4 secteurs fermés | 2026-07-18 | 2026-07-25 | gr20-infos.com ; corse-du-sud.gouv.fr | ACTIF (Illarata) — **CHANGÉ 25/07** |
| incendie\|Drome-Justin-Die\|foret-fermee\|2026-07-02 | incendie / fermeture massif | Justin : **4400 ha, fixé 16/07.** | Aucune alternative. | Reprise 21/07 maitrisée | GR9/GR93 [HYPOTHÈSE] | HAUTE | fixé, accès interdit | 2026-07-18 | 2026-07-25 | info.fr 18/07 | ACTIF — **CHANGÉ 25/07** |
| fermeture\|FR-Baronnies-GR9\|arretes-municipaux\|2026-07-07 | fermeture / risque feu | Communes fermées ; **échéance Saillans demain.** | Aucune alternative. | Plan de Baix LEVÉ | GR9 (Baronnies) | HAUTE | variable | 2026-07-18 | 2026-07-25 | drome-cestmanature.com | ACTIF — **CHANGÉ 25/07 (léger)** |
| risque-feu\|Vaucluse-84\|fermeture-8-massifs\|2026-07-01 | risque feu / fermeture massif | **15/15 massifs fermés au 23/07.** Statut 25/07 non confirmé. | Aucune ; Ventoux non recoupé. | Escalade confirmée | GR4, GR9, GR6/GR91 | HAUTE | maximale probable | 2026-07-18 | 2026-07-25 | info.fr 23/07 | ACTIF — **CHANGÉ 25/07** |
| incendie\|Ariege-Bordes-Uchentein\|GR10-ferme-Esbintz-Valier\|2026-07-10 | incendie / fermeture sentier | GR10 Esbintz↔Valier fermé. **Bilan 240 ha.** | **Esbintz↔Col de la Core praticable.** | Feu fixé 18/07 | GR10 (Couserans) | HAUTE | jusqu'à nouvel ordre | 2026-07-20 | 2026-07-25 | info.fr | ACTIF — **CHANGÉ 25/07** |
| risque-feu\|Alberes-66\|fermeture-massif-GR10\|2026-07-10 | risque feu / fermeture massif | Albères fermé depuis 10/07. | Aucune alternative. | Argelès, Sorède, Cerbère | GR10 | HAUTE | jusqu'à nouvel ordre | 2026-07-20 | 2026-07-25 | arrêté 26.238 | ACTIF |
| reroutage\|Aspe-64-Chemin-Mature\|eboulement-devie-col-Arras\|2026-01-05 | reroutage / fermeture locale | Chemin Mâture fermé 05/01/2026. | Déviation col d'Arras. | Aspe (64) | GR10 | MOYENNE | jusqu'à nouvel ordre | 2026-07-20 | 2026-07-22 | FFRandonnée | ACTIF |
| incendie\|Corse-Mare-a-Mare-Nord\|fermeture-Vergio-Albertacce\|2026-07-19 | incendie / fermeture sentier | Vergio↔Albertacce fermé ; étendu Corte↔Calacuccia. | Navette Asco↔Vergio. | Lié à la Restonica | Mare a Mare Nord | MOYENNE | jusqu'à nouvel ordre | 2026-07-20 | 2026-07-25 | haute-corse.gouv.fr | ACTIF — INCHANGÉ 25/07 |
| fermeture\|PN-Pyrenees-Moundelhs\|travaux-forestiers-cirque\|2026-07-15 | fermeture / travaux | Cirque du Moundelhs fermé 15/07. | Aucune. | Bielle/Billières | Aucun P1 | INFO | jusqu'à nouvel ordre | 2026-07-20 | 2026-07-23 | pyrenees-parcnational.fr | ACTIF |
| incendie\|HautesPyrenees-Bareges\|Pic-Lurtet-Glere-piste-fermee\|2026-07-08 | incendie / fermeture piste | Piste de la Glère fermée. Feu **fixé depuis le 22/07 (14e jour).** | Aucune alternative. | Foudre 08/07, Barèges | GR10 (Barèges) ; HRP [HYPOTHÈSE] | HAUTE | fixé, pas éteint | 2026-07-21 | 2026-07-25 | toulouse7.com ; lasemainedespyrenees.fr | ACTIF — INCHANGÉ 25/07 : statut reconfirmé par défaut |
| incendie\|Savoie-Planay-Pralognan\|RD915-refuges-Vanoise\|2026-07-07 | incendie / accès refuges | Feu en **stabilisation (~75 ha). RD915 rouverte depuis le 15/07 sous alternat** (piétons/cyclistes exclus). | RD915 praticable en voiture sous alternat. | Refuges Vanoise statut non documenté | GR55 ; TGV [HYPOTHÈSE] | MOYENNE | RD915 alternat depuis 15/07 | 2026-07-21 | 2026-07-25 | savoie.gouv.fr MAJ 23/07 | ACTIF — **CHANGÉ 25/07 : 1re MAJ après 4j de silence** |
| incendie\|HautesAlpes-BoisNoir\|GR54A-ferme-Argentiere-Freissinieres\|2026-07-19 | incendie / fermeture massif | Bois Noir : **~400 ha au 24/07** (vs 240-255 au 23/07), toujours actif. GR54A fermé. | **GR54 classique** (repli confirmé). | Massif entier interdit, RD138A coupée | GR54A (fermé), GR54 (repli) | HAUTE | en progression, pas de levee | 2026-07-22 | 2026-07-25 | ecrins-parcnational.fr | ACTIF — **CHANGÉ 25/07 : nouvelle aggravation à 400ha** |
| incendie\|FR-IDF-Fontainebleau\|foret-fermee-arrete-jusqua-26-07\|2026-07-12 | incendie / fermeture massif | Foret Fontainebleau/Trois-Pignons/Commanderie : **arrêtés PROLONGÉS jusqu'au 31/07/2026** (vs 26/07 initial). | Aucune déviation officielle. | S.-et-M., risque persistant | GR1, GR2, GR3, GR11, GR13, GR655 | HAUTE | jusqu'au 31/07/2026 inclus | 2026-07-22 | 2026-07-25 | seine-et-marne.gouv.fr MAJ 24/07 | ACTIF — **CHANGÉ 25/07 : PROLONGATION CONFIRMÉE** |
| incendie\|UK-Cairngorms-Glenmore\|wildfire-Strathnethy-C7-fermee\|2026-07-16 | incendie / fermeture accès | Cairngorms : **nouvelle reprise de feu nuit du 24-25/07** près de Coire na Ciste. C7 toujours fermée. | Aucune alternative. | Opérations jusqu'à semaine du 27-31/07 | Secteur Cairngorms, hors GR référencé | HAUTE | reprise 24-25/07 | 2026-07-22 | 2026-07-25 | Highland Council 24/07 ; Strathspey Herald 24/07 | ACTIF — **CHANGÉ 25/07 : AGGRAVATION, nouvelle reprise** |
| incendie\|AT-Vorarlberg-Silvretta\|coulee-boue-sentiers-fermes\|2026-07-12 | terrain / fermeture | Coulée de boue Silvretta (Partenen) : sentier lac Silvrettasee fermé. | Aucune alternative. | Vorarlberg 12-13/07 | Aucun P1 | MOYENNE | réouverture non confirmée | 2026-07-23 | 2026-07-23 | vorarlberg.orf.at | ACTIF — NOUVEAU 23/07 |
| reroutage\|SI-Julijske-Alpe\|deviation-Trnovo-Srpenica\|2025-10 | reroutage pérenne | Juliana Trail Trnovo-Srpenica impossible depuis oct 2025. | Déviation via Žaga. | Vallée de la Soča | Juliana Trail, Alpe-Adria Trail | MOYENNE | pérenne | 2026-07-23 | 2026-07-23 | soca-valley.com | ACTIF — NOUVEAU 23/07 |
| reroutage\|SK-Tatras-Krivan\|fermeture-Tri-studnicky\|2026 | reroutage / fermeture | Accès Kriváň fermé (travaux, réouverture sept-oct 2026). | Autre itinéraire d'ascension. | Tatras slovaques | Kriváň, hors P1 | MOYENNE | travaux en cours | 2026-07-23 | 2026-07-23 | presse slovaque | ACTIF — NOUVEAU 23/07 |
| risque-feu\|FR-Landes-Gironde\|vigilance-rouge-bivouac-interdit\|2026-07-21 | risque feu / réglementation accès | Landes/Gironde vigilance rouge (niveau 4/5) depuis 21/07 : bivouac isolé interdit. | Sans objet pour circulation à pied. | Massifs landais/girondins | GR65, GR8, GR654 | MOYENNE | depuis 21/07 | 2026-07-24 | 2026-07-24 | landes.gouv.fr ; gironde.gouv.fr | ACTIF — NOUVEAU 24/07 |
| incendie\|ES-CENTRO-Guadalajara-LaMierla\|feu-record-32000ha\|2026-07-16 | incendie | La Mierla (Guadalajara) : **~32000 ha, stabilisation au 23/07 sans maîtrise totale.** | Aucune ; secteur à éviter. | Pire juillet depuis 1994 | Aucun GR confirmé [HYPOTHÈSE] | MOYENNE (HAUTE régional) | combustion continue | 2026-07-24 | 2026-07-25 | Infobae ; telemadrid.es 23/07 | ACTIF — INCHANGÉ 25/07 : dernier point 23/07 |
| fermeture\|GR-E4-Creta-Samaria\|fermetures-meteo-repetees\|2026-07-16 | fermeture / conditions météo | Gorges de Samaria fermetures répétées (vent, canicule). | Se renseigner sur samaria.gr. | Xyloskalo | E4 Crète | MOYENNE | pattern selon météo | 2026-07-24 | 2026-07-24 | Tα Nέα 21/07 ; ekriti.gr | ACTIF — NOUVEAU 24/07 |
| incendie\|Var-Gros-Bessillon\|feu-actif-Ponteves-Cotignac-Correns\|2026-07-22 | incendie | **Gros Bessillon (Pontevès/Cotignac/Correns) : ~2500-2850 ha, non maîtrisé.** ~400 évacués, ~25 maisons détruites. | Aucune — secteur à éviter. | Déclenché 22/07, plusieurs reprises ; ferme tous massifs Var | GR9/GR51 (Haut-Var/Centre-Var) [HYPOTHÈSE] | HAUTE | non maîtrisé au 25/07 | 2026-07-25 | 2026-07-25 | frequence-sud.fr ; info.fr | ACTIF — NOUVEAU 25/07 |
| incendie\|Herault-34-Poussan\|feu-garrigue-Gardiole\|2026-07-24 | incendie | Massif de la Gardiole (Poussan/Gigean/Frontignan) : **~100-150 ha**, parti 24/07, pas d'évacuation. | Aucune fermeture officielle trouvée. | Second départ Pomérols même jour | GR51 [HYPOTHÈSE] | MOYENNE | statut 25/07 non confirmé | 2026-07-25 | 2026-07-25 | feuxdeforet.fr ; France 3 Occitanie | ACTIF — NOUVEAU 25/07 |
| incendie\|ES-CYL-Murias-de-Ponjos\|feu-IGR2-proximite-Torre-del-Bierzo\|2026-07-22 | incendie | Murias de Ponjos (León) : IGR-2, **~2700-3000 ha, 6 villages évacués**, proche Torre del Bierzo. | Aucune alternative. | Camino de Invierno à proximité, pas Camino Francés | Camino de Invierno [HYPOTHÈSE] | MOYENNE | en cours au 24/07 | 2026-07-22 | 2026-07-25 | ileon.eldiario.es 24/07 | ACTIF — NOUVEAU 25/07 |
| fermeture\|IT-DOLOMITES-Brenta\|Cima-Falkner-Bocchette-sentieri-chiusi\|2025-07 | fermeture / risque géologique | Bocchette del Brenta (Cima Falkner) : la plupart des sentiers fermés depuis l'éboulement de juillet 2025. | Sentiero SAT O136 (Grostè-Tuckett) ouvert. | Toujours actif au 09/07/2026 | Réseau Bocchette (hors P1) | MOYENNE | depuis juillet 2025 | 2025-07 | 2026-07-25 | il Dolomiti 09/07/2026 | ACTIF — NOUVEAU 25/07 |
| incendie\|PT-CENTRO-SUL-Monchique-Marmelete\|feu-actif-ViaAlgarviana-Setor11\|2026-07-25 | incendie | Vale de Água, Monchique/Marmelete : feu **Em Curso, signalé 25/07 04h58** (API fogos.pt), sur Setor 11 Via Algarviana. | Aucune — événement très récent. | 65 hommes, 19 engins, vent fort | Via Algarviana (GR13) Setor 11 [HYPOTHÈSE] | MOYENNE | données parcellaires | 2026-07-25 | 2026-07-25 | api.fogos.pt/new/fires | ACTIF — NOUVEAU 25/07 |

## Items mineurs / hébergement
- Écrins / haut Vénéon : refuges du haut Vénéon ouverts pour l'été (ecrins-parcnational.fr, 12/06/2026) — INFO, variante hors boucle principale GR54.
- GR10 Ariège : ouverture gîte « Le Relais Clément » à Faup (gr10.org, 19/06/2026).
- GR5 Levens (06) : balise 261 fermée travaux depuis 16/02/2026 (FFRando 06) — impact faible.
- Vanoise : refuge de Turia rouvre été 2026 après réhabilitation.
- GR5 Roure (06) : déviation b238→M130 depuis 2019.
- Corse-du-Sud (2A) : arrêté 03/07/2026 alerte sécheresse — contexte GR20, pas de restriction nouvelle.
- ES-GAL / Camino de Invierno : feu de Ribas de Sil (190 ha) ÉTEINT le 15/07.
- ES-CYL / Camino Francés : feux ferroviaires du 15/07 (Sahágun) éteints.
- ES-NORTE / Camino Primitivo : feu Pico del Hospital, extinction héliportée 12/07.
- ES-AND / Almería : incendio de Los Gallardos (7000 ha, 13 morts) — hors GR du référentiel.
- ES-AND / Cazorla : Sendero del Río Borosa rouvert 08/07.
- ES-AND / Doñana : Sendero Dunar fermé (Matalascañas/Almonte) — hors GR suivi.
- PT-CENTRO-SUL : aucun feu majeur actif au 17/07 (hormis contexte).
- CH flux fédéral : sentier refuge Monte Rosa fermé/dévié → 06/2027 ; Saas-Almagell fermé → 05/2027.
- AT / Tirol : feu Wildermieming maîtrisé 17/07.
- IS : safetravel.is — Solheimajokull conditions dangereuses, hors trails suivis.
- UK / West Highland Way : travaux Ewich Forest, réouverture Ptarmigan-Rowchoish.
- ES-GAL : feux Boborás/Crecente éteints 18/07 — RAS Camino.
- ES-CYL : alerte incendie régionale Junta CyL 19-22/07, sans fermeture Camino.
- IT-Dolomites : sentiero 666 rouvert ; Via Ferrata O304 fermée 22-29/07.
- IT-Centre : Latium bollino rosso 15-16/07 + alerte élevé 18-20/07.
- ES-AND : 3e vague chaleur 19-22/07, GR référencés non touchés.
- FR : vigilance orange canicule 7 départements sud (contexte général).
- ES-AND / Grazalema : feu El Alamillo éteint 14/07.
- ES-AND / Almería : feu La Capacidad contrôlé rapidement 18/07.
- ES-AND / Málaga : Istán RÉSOLU — confusion avec un feu de février 2026, artefact d'indexation écarté.
- PT-CENTRO-SUL / Algarve : Faro « perigo máximo », chaleur en hausse 21/07.
- CH-VALAIS-VAUD : déviation courte Crans-Montana, fermetures Saas-Fee (hors itinéraires suivis).
- FR-ALPES-N / Isère : 4 sites péri-urbains fermés Grenoble-Alpes Métropole — hors GR référencés.
- ES-AND / Huelva : feu Almonaster la Real résolu <24h.
- ES-CYL / Segovia : feu de Brieva, hors tracé Camino Francia/Plata.
- Morbihan/GR34 : épisodes canicule clos, sécheresse à surveiller.
- UK-IE : notices mineures stables (Pennine Way, Coast to Coast, Wicklow Way).
- SCAND-NO / Lofoten : chantier Torsfjorden-Ryten-Kvalvika, sentier ouvert normalement.
- ES-CYL : alerte régionale rehaussée « situación operativa 2 » 22-23/07 (Castropodame, La Baña).
- ES-AND : décrue chaleur attendue à partir du 24/07 [HYPOTHÈSE] ; feux Granada/Málaga/Huelva sans lien GR confirmé.
- PT-CENTRO-SUL / Algarve : signal Odeceixe NON CORROBORÉ, retiré du suivi.
- FR-EST / Vosges : incendie Kemberg maîtrisé le jour même, aucune fermeture GR trouvée.
- AT : Wildermieming éteint (inchangé) ; Stuibenfall rouvert depuis 26/06.
- ES-CYL / Léon-Bierzo : Castropodame + La Baña + Murias de Ponjos, proximité Bierzo sans impact confirmé sur le tracé.
- ES-GAL : Camino Francés confirmé hors zone affectée par le feu (Diario de Santiago).
- ES-CANARIAS : sémaphore volcanique INVOLCAN vert/jaune, aucune fermeture GR131/GR130.
- Agrégateurs (gronze.com) : items sans date exploitable, à revoir méthode de capture.

## À vérifier manuellement
- Pages FB éditoriales (parcs/OT/orgas) : non vérifiées en run autonome.
- Vanoise : rien de spécifique dans infos pratiques été 2026 (vérifié 02/07).
- Arrêtés feu Pyrénées (64/65/09/66) + côté ES : non détaillés.
- ~~GR10 Luchon-Superbagnères~~ : RÉSOLU, passé en ligne registre.
- **Canicule / risque feu haute saison** : vigilance quotidienne maintenue Corse, 83, 13, 30, 26.
- ~~Hérault/Aude~~ : RÉSOLU, passés en lignes registre.
- **Corse — GR20-Albertacce, page « Incendie du refuge d'Ortu » non datée [ajouté 25/07]** : page gr20-infos.com sans date vérifiable, possible piège d'indexation — aucune alerte créée tant que non confirmée, à vérifier au prochain passage FR-CORSE.
- **Corse — statut d'accueil du refuge de Paliri** : accès sentier rouvert, accueil du bâtiment non confirmé.
- **Barèges/Pic de Lurtet et Planay/Pralognan** : suivis en lignes registre dédiées.
- **Ariège/GR10 — écart de bilan** : RÉSOLU 25/07, fixé à 240 ha.
- **UK — Cairngorms/Glenmore [MAJ 25/07]** : nouvelle reprise de feu, statut alerte régionale et route C7 à reconfirmer au prochain passage UK-IE.
- **Réunion — AP 2026-693** : PDF/carte ONF non lus, à recouper avec GR R2.
- ~~Lozère — Causse Méjean~~ : RÉSOLU 25/07 — incendie du 06/07/2026 à Hures-la-Parade (~200-216 ha), éteint sans fermeture GR confirmée, retiré du suivi actif.
- ~~Pyrénées-Orientales — GR10 Albères~~ : RÉSOLU, passé en ligne registre dédiée.
- Mercantour — sentiers fermés Mollières/Valabres/Pelousette : hors tracé principal (voir ligne registre).
- **Sources officielles ES illisibles en autonome** : contournements presse validés (Galiciapress, leonoticias, RTPA, etc).
- **ES-AND — feu d'Árchez/Cómpeta** : toujours aucune source postérieure au 18/07.
- **ES-AND — Los Gallardos post-incendie** : phase de liquidation, aucun AP formel trouvé.
- **IT-NO — Val Grande** : 2 itinéraires encore fermés à Premosello Chiovenda.
- **CH — TMB Orsières** : re-balayage du flux CSV fédéral chaque mardi.
- **IT-CENTRE — VF Prato La Corte** : toujours en vigueur au 25/07.
- **ES-BALEARES — refuges Consell 01-15/08** : motif non publié.
- **ES-CANARIAS — senderosdelapalma.es** : tableau illisible en autonome.
- **DE — DWD Waldbrandindex** : URL CSV à retrouver.
- **BENELUX — grsentiers.be** : newsletters Mailchimp, dernier n°129.
- **Camino de Invierno — Ribas de Sil** : zone brûlée sans dégradation du chemin documentée.
- **Camino Primitivo — Pico del Hospital** : traité comme RAS, confiance modérée.
- **Ourense/Sanabrés — focos train** : éteints par défaut, à re-balayer.
- ~~ES-CYL — feu de Castropodame/Villaverde de los Cestos~~ : RÉSOLU/amélioré 25/07 — IGR 2→1, évacués rentrés ; La Baña/Encinedo toujours sans mise à jour fiable, à vérifier au prochain passage ES-CYL ; aucun impact confirmé sur le Camino Francés.
- ~~13 (Calanques) — divergence communiqué vs carte technique~~ : RÉSOLU 24/07.
- ~~83 (Var) — confirmation de la désescalade du 24/07~~ : RÉSOLU 25/07 — la désescalade était infondée, retournement vers fermeture totale confirmé officiellement (voir ligne registre).
- **Vaucluse-84 — page officielle du jour introuvable [MAJ 25/07]** : toujours 404 le 3e run consécutif, à re-tenter.
- **Gard-30 — page officielle du jour introuvable [MAJ 25/07]** : toujours 404, à re-tenter.
- **Corse — Fango/Bonifato/Agriate, reconduction non retrouvée [MAJ 25/07]** : aucune page datée 24-25/07, traité par défaut comme reconduit.
- ~~Corse — Albertacce/GR20, contradiction Tighjettu↔Ciottulu~~ : RÉSOLU 25/07, passé en ligne registre.
- **Agrégateurs — méthode de capture des dates à revoir** : gronze.com items sans date exploitable.

## Pistes abandonnées
(vide)

## Notes
- TYPE : réglementation / fermeture massif / reroutage / refuge / risque feu / accès.
- SÉVÉRITÉ : haute (bloque une étape ou interdiction) / moyenne / info.
- Le digest ne reprend QUE le nouveau/changé ; ce registre garde l'état complet.
