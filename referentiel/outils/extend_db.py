#!/usr/bin/env python3
"""Extension Europe de sentiers-db.csv : GR espagnols (es.wikipedia), GR belges,
E-paths, + couche curée CH/IT/AT/DE/BENELUX/UK-IE/SCAND/IS/PT/ES."""
import csv
import re

DB = "/Users/clement/Library/CloudStorage/Dropbox/OMW/OMW - Agents/veille-europe/referentiel/sentiers-db.csv"

# mots-clés (villes/provinces) → zone ES
ES_KEYS = {
    "ES-CAT": ["Barcelona", "Barcelone", "Gerona", "Girona", "Lérida", "Lleida", "Tarragona",
               "Junquera", "Ripoll", "Berga", "Puigcerdá", "Montserrat", "Manresa", "Solsona",
               "Ampurdán", "Rupit", "Besós", "Tremp", "Urgel", "Abadesas", "Mequinenza",
               "Ulldecona", "Tortosa", "Cadaqués", "Portbou", "Tarrasa", "Igualada", "Olot"],
    "ES-NAV-RIO-ARA": ["Zaragoza", "Huesca", "Teruel", "Navarra", "Rioja", "Logroño",
                       "Pamplona", "Olite", "Jaca", "Graus", "Riglos", "Sos del Rey",
                       "Tierrantona", "Biel", "Ezcaray", "Canfranc", "Ordesa", "Benasque",
                       "Ansó", "Roncal", "Roncesvalles", "Sangüesa", "Tarazona", "Borja",
                       "Daroca", "Albarracín", "Alcañiz", "Andorra"],
    "ES-NORTE": ["Vizcaya", "Guipúzcoa", "Álava", "Bilbao", "San Sebastián", "Donostia",
                 "Santander", "Cantabria", "Asturias", "Oviedo", "Gijón", "Reinosa",
                 "Irún", "Getxo", "Laredo", "Llanes", "Covadonga", "Picos de Europa",
                 "Potes", "Karrantza", "Fuenterrabía", "Hondarribia"],
    "ES-GAL": ["Coruña", "Lugo", "Orense", "Ourense", "Pontevedra", "Finisterre",
               "Fisterra", "Sarria", "Santiago", "Vigo", "Tui", "Ribadeo", "Fonteo",
               "Monforte", "Verín"],
    "ES-CYL": ["Burgos", "León", "Palencia", "Zamora", "Salamanca", "Soria", "Valladolid",
               "Segovia", "Ávila", "Cervera de Pisuerga", "Maraña", "Ponferrada",
               "Astorga", "Béjar", "Ciudad Rodrigo", "Aranda", "Sanabria", "Gredos"],
    "ES-AND": ["Sevilla", "Granada", "Málaga", "Cádiz", "Córdoba", "Jaén", "Almería",
               "Huelva", "Tarifa", "Ronda", "Antequera", "Cazorla", "Nerja", "Algeciras",
               "Despeñaperros", "Aracena", "Sierra Nevada"],
    "ES-CENTRO": ["Madrid", "Toledo", "Cuenca", "Guadalajara", "Ciudad Real", "Albacete",
                  "Cáceres", "Badajoz", "Mérida", "Plasencia", "Manzanares", "Cercedilla",
                  "Sigüenza", "Talavera"],
    "ES-LEVANTE": ["Valencia", "Alicante", "Castellón", "Murcia", "Elche", "Orihuela",
                   "Morella", "Denia", "Cartagena", "Caravaca", "Sagunto", "Requena"],
    "ES-BALEARES": ["Mallorca", "Menorca", "Ibiza", "Palma", "Pollensa", "Andratx",
                    "Tramuntana", "Mahón", "Ciudadela"],
    "ES-CANARIAS": ["Tenerife", "La Palma", "Gran Canaria", "Lanzarote", "Fuerteventura",
                    "La Gomera", "El Hierro", "Teide"],
}

def es_zones(text):
    zones = []
    for z, keys in ES_KEYS.items():
        if any(k in text for k in keys) and z not in zones:
            zones.append(z)
    return zones

def clean(t):
    t = re.sub(r"\[\[([^|\]]*\|)?([^\]]+)\]\]", r"\2", t)
    t = t.replace("'''", "").replace("''", "")
    t = re.sub(r"<br\s*/?>", " ", t)
    t = re.sub(r"\{\{[^}]*\}\}", "", t)
    return re.sub(r"\s+", " ", t).strip()

SCRATCH = "/private/tmp/claude-501/-Users-clement/95437a69-196e-4202-9334-415e7bb14af9/scratchpad/"
rows = []

# ------------------------------------------------ GR espagnols (tableau es.wiki)
w = open(SCRATCH + "es_gr.wiki", encoding="utf-8").read()
tbl = w[w.index("{| class"):]
tbl = tbl[:tbl.index("|}")]
for chunk in tbl.split("|-"):
    lines = [l for l in chunk.splitlines() if l.startswith("|") and not l.startswith("|}")]
    if not lines:
        continue
    cells = []
    for l in lines:
        cells.extend(c.strip() for c in re.split(r"\|\|", l.lstrip("|")))
    if len(cells) < 3:
        continue
    ident = clean(cells[0])
    m = re.match(r"^GR[- ]?([\d.]+)", ident)
    if not m:
        continue
    num = m.group(1)
    nom = clean(cells[1])
    itin = clean(cells[2])
    zones = es_zones(nom + " " + itin)
    notes = "" if zones else "zones à préciser"
    rows.append([f"GR{num}-ES", nom or f"GR-{num} (España)", "GR", "ES",
                 "|".join(zones), "P3", "wikipedia-es:GR", notes + (f" ; via {itin[:120]}" if itin else "")])

# ------------------------------------------------ GR belges (liste fr.wiki)
w = open(SCRATCH + "be_gr.wiki", encoding="utf-8").read()
for m in re.finditer(r"^\*+\s*(.+)$", w, re.M):
    t = clean(m.group(1))
    gm = re.match(r"^(GR\s?\d+[A-Z]?)\s*[:,–-]?\s*(.*)$", t)
    if not gm:
        continue
    code = gm.group(1).replace(" ", "")
    nom = gm.group(2)[:120] or code
    rows.append([f"{code}-BE", nom, "GR", "BE", "BENELUX", "P3", "wikipedia:GR-Belgique", ""])

# ------------------------------------------------ E-paths (E1..E12)
w = open(SCRATCH + "epaths.wiki", encoding="utf-8").read()
for m in re.finditer(r"^\*+\s*.*?\b(E\d{1,2})\b\s*[:,]?\s*(.+)$", w, re.M):
    code, desc = m.group(1), clean(m.group(2))[:160]
    if any(r[0] == code for r in rows):
        continue
    rows.append([code, f"Sentier européen {code} — {desc}", "E-PATH", "EU", "EU-MULTI", "P3",
                 "wikipedia:E-paths", "suit des tronçons nationaux (GR/national trails)"])

# ------------------------------------------------ couche curée Europe
CURATED = [
    # Suisse
    ["VIA-ALPINA-CH", "Via Alpina Suisse (Vaduz → Montreux)", "NATIONAL", "CH", "CH-EST|CH-VALAIS-VAUD", "P1", "curated", "route nationale 1 SuisseMobile"],
    ["TOUR-COMBINS", "Tour des Combins", "TOUR", "CH/IT", "CH-VALAIS-VAUD|IT-NO", "P2", "curated", ""],
    ["TOUR-CERVIN", "Tour du Cervin / Matterhorn", "TOUR", "CH/IT", "CH-VALAIS-VAUD|IT-NO", "P2", "curated", ""],
    ["TOUR-MONTE-ROSA", "Tour du Mont Rose", "TOUR", "CH/IT", "CH-VALAIS-VAUD|IT-NO", "P2", "curated", ""],
    ["VIA-FRANCIGENA-CH", "Via Francigena — tronçon suisse (Ste-Croix → Gd-St-Bernard)", "CAMINO", "CH", "CH-VALAIS-VAUD", "P2", "curated", "prolonge le GR145"],
    # Italie
    ["ALTA-VIA-1-VDA", "Alta Via 1 de la Vallée d'Aoste (Giants' Trail)", "ALTA-VIA", "IT", "IT-NO", "P1", "curated", ""],
    ["ALTA-VIA-2-VDA", "Alta Via 2 de la Vallée d'Aoste", "ALTA-VIA", "IT", "IT-NO", "P2", "curated", ""],
    ["GTA-IT", "Grande Traversata delle Alpi (Piémont)", "GR-INT", "IT", "IT-NO", "P2", "curated", ""],
    ["AV-MONTI-LIGURI", "Alta Via dei Monti Liguri", "ALTA-VIA", "IT", "IT-NO", "P2", "curated", ""],
    ["ALTA-VIA-1-DOLOMITI", "Alta Via 1 des Dolomites (Braies → Belluno)", "ALTA-VIA", "IT", "IT-DOLOMITES", "P1", "curated", ""],
    ["ALTA-VIA-2-DOLOMITI", "Alta Via 2 des Dolomites (Bressanone → Feltre)", "ALTA-VIA", "IT", "IT-DOLOMITES", "P2", "curated", ""],
    ["VIA-FRANCIGENA-IT", "Via Francigena — tronçon italien (Gd-St-Bernard → Rome)", "CAMINO", "IT", "IT-NO|IT-CENTRE", "P1", "curated", ""],
    ["SENTIERO-ITALIA", "Sentiero Italia CAI", "NATIONAL", "IT", "IT-NO|IT-DOLOMITES|IT-CENTRE", "P3", "curated", "~7 000 km — zones pilote uniquement"],
    ["ALPE-ADRIA", "Alpe-Adria-Trail (Grossglockner → Muggia)", "GR-INT", "AT/SI/IT", "AT|IT-DOLOMITES", "P2", "curated", "tronçon slovène hors zones"],
    # Autriche / Allemagne
    ["E5-ALPES", "E5 alpin — Oberstdorf → Meran", "E-PATH", "DE/AT/IT", "DE|AT|IT-DOLOMITES", "P1", "curated", "tronçon le plus fréquenté de l'E5"],
    ["ADLERWEG", "Adlerweg (Tyrol)", "NATIONAL", "AT", "AT", "P2", "curated", ""],
    ["WESTWEG", "Westweg (Forêt-Noire, Pforzheim → Bâle)", "NATIONAL", "DE", "DE", "P2", "curated", ""],
    ["RHEINSTEIG", "Rheinsteig (Wiesbaden → Bonn)", "NATIONAL", "DE", "DE", "P3", "curated", ""],
    ["MOSELSTEIG", "Moselsteig", "NATIONAL", "DE", "DE", "P3", "curated", ""],
    ["MALERWEG", "Malerweg (Suisse saxonne)", "NATIONAL", "DE", "DE", "P3", "curated", ""],
    ["RENNSTEIG", "Rennsteig (forêt de Thuringe)", "NATIONAL", "DE", "DE", "P3", "curated", ""],
    # Benelux
    ["MULLERTHAL", "Mullerthal Trail (Luxembourg)", "NATIONAL", "LU", "BENELUX", "P2", "curated", ""],
    ["PIETERPAD", "Pieterpad (Pieterburen → Maastricht)", "NATIONAL", "NL", "BENELUX", "P3", "curated", ""],
    # UK / Irlande
    ["WHW", "West Highland Way (Écosse)", "NATIONAL", "UK", "UK-IE", "P1", "curated", ""],
    ["PENNINE-WAY", "Pennine Way", "NATIONAL", "UK", "UK-IE", "P2", "curated", ""],
    ["C2C", "Coast to Coast Walk (Wainwright)", "NATIONAL", "UK", "UK-IE", "P2", "curated", ""],
    ["SWCP", "South West Coast Path", "NATIONAL", "UK", "UK-IE", "P2", "curated", ""],
    ["HADRIANS-WALL", "Hadrian's Wall Path", "NATIONAL", "UK", "UK-IE", "P3", "curated", ""],
    ["WICKLOW-WAY", "Wicklow Way (Irlande)", "NATIONAL", "IE", "UK-IE", "P2", "curated", ""],
    ["KERRY-WAY", "Kerry Way (Irlande)", "NATIONAL", "IE", "UK-IE", "P3", "curated", ""],
    # Scandinavie / Islande
    ["KUNGSLEDEN", "Kungsleden (Abisko → Hemavan, Laponie suédoise)", "NATIONAL", "SE", "SCAND", "P1", "curated", ""],
    ["PADJELANTALEDEN", "Padjelantaleden (Laponie)", "NATIONAL", "SE", "SCAND", "P3", "curated", ""],
    ["JOTUNHEIMEN", "Traversées du Jotunheimen (routes DNT, Besseggen)", "NATIONAL", "NO", "SCAND", "P2", "curated", ""],
    ["LAUGAVEGUR", "Laugavegur (Landmannalaugar → Þórsmörk)", "NATIONAL", "IS", "IS", "P1", "curated", ""],
    ["FIMMVORDUHALS", "Fimmvörðuháls (Þórsmörk → Skógar)", "NATIONAL", "IS", "IS", "P2", "curated", ""],
    # Ibérie hors caminos (curée, zones sûres)
    ["GR221-ES", "GR221 — Ruta de Pedra en Sec (Serra de Tramuntana, Mallorca)", "GR", "ES", "ES-BALEARES", "P1", "curated", ""],
    ["GR223-ES", "GR223 — Camí de Cavalls (Menorca)", "GR", "ES", "ES-BALEARES", "P2", "curated", ""],
    ["GR131-ES", "GR131 — Canaries (El Hierro → Lanzarote)", "GR", "ES", "ES-CANARIAS", "P2", "curated", ""],
    ["GR240-ES", "GR240 — Sendero Sulayr (Sierra Nevada)", "GR", "ES", "ES-AND", "P3", "curated", ""],
    ["GR247-ES", "GR247 — Bosques del Sur (Cazorla)", "GR", "ES", "ES-AND", "P3", "curated", ""],
    ["GR92-ES", "GR92 — Sender del Mediterrani (Catalogne)", "GR", "ES", "ES-CAT", "P2", "curated", ""],
    ["GR7-ES", "GR7 espagnol / E4 (Tarifa → Andorre)", "GR", "ES/AD", "ES-AND|ES-LEVANTE|ES-CAT", "P2", "curated", ""],
    ["CAMINITO-DEL-REY", "Caminito del Rey (El Chorro, Málaga)", "NATIONAL", "ES", "ES-AND", "P3", "curated", "accès sur réservation"],
    ["ROTA-VICENTINA", "Rota Vicentina — Fishermen's Trail + Historical Way", "NATIONAL", "PT", "PT-CENTRO-SUL", "P1", "curated", ""],
    ["CAMINO-FAROS", "Camiño dos Faros (Costa da Morte)", "NATIONAL", "ES", "ES-GAL", "P3", "curated", ""],
]
rows.extend(CURATED)

# ------------------------------------------------ fusion dans la base
with open(DB, encoding="utf-8") as f:
    existing = list(csv.reader(f, delimiter=";"))
header, body = existing[0], existing[1:]
known = {r[0] for r in body}
added = 0
for r in rows:
    if r[0] in known:
        continue
    body.append(r)
    known.add(r[0])
    added += 1

with open(DB, "w", newline="", encoding="utf-8") as f:
    wcsv = csv.writer(f, delimiter=";")
    wcsv.writerow(header)
    wcsv.writerows(body)

from collections import Counter
print(f"ajoutés : {added} → total {len(body)}")
print(dict(Counter(r[2] for r in body)))
es = [r for r in body if r[0].endswith("-ES") and r[6].startswith("wikipedia-es")]
print("GR ES wikipédia :", len(es), "— sans zone :", sum(1 for r in es if not r[4]))
