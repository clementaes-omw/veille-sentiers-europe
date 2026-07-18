#!/usr/bin/env python3
"""Construit referentiel/sentiers-db.csv à partir des listes Wikipédia (GR + GRP)
+ couches curées (Hautes Routes, Caminos). Mapping département → zone-source."""
import csv
import re
import sys

OUT = "/Users/clement/Library/CloudStorage/Dropbox/OMW/OMW - Agents/veille-europe/referentiel/sentiers-db.csv"

# ---------------------------------------------------------------- dept → zone
DEPT_ZONE = {
    "01": "FR-ALPES-N", "02": "FR-EST", "03": "FR-MC", "04": "FR-04-05", "05": "FR-04-05",
    "06": "FR-06", "07": "FR-84-26-07", "08": "FR-EST", "09": "FR-PYR-O", "10": "FR-EST",
    "11": "FR-34-11", "12": "FR-MC", "13": "FR-13", "14": "FR-NOR", "15": "FR-MC",
    "16": "FR-SO", "17": "FR-SO", "18": "FR-SO", "19": "FR-MC", "21": "FR-EST",
    "22": "FR-BRE", "23": "FR-MC", "24": "FR-SO", "25": "FR-EST", "26": "FR-84-26-07",
    "27": "FR-NOR", "28": "FR-IDF-CVL", "29": "FR-BRE", "2A": "FR-CORSE", "2B": "FR-CORSE",
    "30": "FR-30-48", "31": "FR-PYR-O", "32": "FR-SO", "33": "FR-SO", "34": "FR-34-11",
    "35": "FR-BRE", "36": "FR-SO", "37": "FR-IDF-CVL", "38": "FR-ALPES-N", "39": "FR-EST",
    "40": "FR-SO", "41": "FR-IDF-CVL", "42": "FR-MC", "43": "FR-MC", "44": "FR-BRE",
    "45": "FR-IDF-CVL", "46": "FR-MC", "47": "FR-SO", "48": "FR-30-48", "49": "FR-IDF-CVL",
    "50": "FR-NOR", "51": "FR-EST", "52": "FR-EST", "53": "FR-NOR", "54": "FR-EST",
    "55": "FR-EST", "56": "FR-BRE", "57": "FR-EST", "58": "FR-EST", "59": "FR-EST",
    "60": "FR-EST", "61": "FR-NOR", "62": "FR-EST", "63": "FR-MC", "64": "FR-PYR-O",
    "65": "FR-PYR-O", "66": "FR-66", "67": "FR-EST", "68": "FR-EST", "69": "FR-MC",
    "70": "FR-EST", "71": "FR-EST", "72": "FR-NOR", "73": "FR-ALPES-N", "74": "FR-ALPES-N",
    "75": "FR-IDF-CVL", "76": "FR-NOR", "77": "FR-IDF-CVL", "78": "FR-IDF-CVL",
    "79": "FR-SO", "80": "FR-EST", "81": "FR-34-11", "82": "FR-SO", "83": "FR-83",
    "84": "FR-84-26-07", "85": "FR-SO", "86": "FR-SO", "87": "FR-MC", "88": "FR-EST",
    "89": "FR-EST", "90": "FR-EST", "91": "FR-IDF-CVL", "92": "FR-IDF-CVL",
    "93": "FR-IDF-CVL", "94": "FR-IDF-CVL", "95": "FR-IDF-CVL", "974": "FR-974",
}
DEPT_NAME = {
    "Ain": "01", "Aisne": "02", "Allier": "03", "Alpes-de-Haute-Provence": "04",
    "Hautes-Alpes": "05", "Alpes-Maritimes": "06", "Ardèche": "07", "Ardennes": "08",
    "Ariège": "09", "Aube": "10", "Aude": "11", "Aveyron": "12", "Bouches-du-Rhône": "13",
    "Calvados": "14", "Cantal": "15", "Charente": "16", "Charente-Maritime": "17",
    "Cher": "18", "Corrèze": "19", "Côte-d'Or": "21", "Côtes-d'Armor": "22", "Creuse": "23",
    "Dordogne": "24", "Doubs": "25", "Drôme": "26", "Eure": "27", "Eure-et-Loir": "28",
    "Finistère": "29", "Corse-du-Sud": "2A", "Haute-Corse": "2B", "Gard": "30",
    "Haute-Garonne": "31", "Gers": "32", "Gironde": "33", "Hérault": "34",
    "Ille-et-Vilaine": "35", "Indre": "36", "Indre-et-Loire": "37", "Isère": "38",
    "Jura": "39", "Landes": "40", "Loir-et-Cher": "41", "Loire": "42", "Haute-Loire": "43",
    "Loire-Atlantique": "44", "Loiret": "45", "Lot": "46", "Lot-et-Garonne": "47",
    "Lozère": "48", "Maine-et-Loire": "49", "Manche": "50", "Marne": "51",
    "Haute-Marne": "52", "Mayenne": "53", "Meurthe-et-Moselle": "54", "Meuse": "55",
    "Morbihan": "56", "Moselle": "57", "Nièvre": "58", "Nord": "59", "Oise": "60",
    "Orne": "61", "Pas-de-Calais": "62", "Puy-de-Dôme": "63", "Pyrénées-Atlantiques": "64",
    "Hautes-Pyrénées": "65", "Pyrénées-Orientales": "66", "Bas-Rhin": "67",
    "Haut-Rhin": "68", "Rhône": "69", "Haute-Saône": "70", "Saône-et-Loire": "71",
    "Sarthe": "72", "Savoie": "73", "Haute-Savoie": "74", "Paris": "75",
    "Seine-Maritime": "76", "Seine-et-Marne": "77", "Yvelines": "78", "Deux-Sèvres": "79",
    "Somme": "80", "Tarn": "81", "Tarn-et-Garonne": "82", "Var": "83", "Vaucluse": "84",
    "Vendée": "85", "Vienne": "86", "Haute-Vienne": "87", "Vosges": "88", "Yonne": "89",
    "Territoire de Belfort": "90", "Essonne": "91", "Hauts-de-Seine": "92",
    "Seine-Saint-Denis": "93", "Val-de-Marne": "94", "Val-d'Oise": "95",
    "La Réunion": "974", "Réunion": "974",
}
REGION_NOTE = {"Corse": "FR-CORSE"}  # mention région sans département

# zones curées (priorité sur l'extraction auto) — héritées de sentiers.md / GPX OMW
OVERRIDES = {
    "GR5": "FR-EST|FR-ALPES-N|FR-04-05|FR-06",
    "GR10": "FR-PYR-O|FR-66",
    "GR20": "FR-CORSE",
    "GR21": "FR-NOR",
    "GR34": "FR-BRE",
    "GR36": "FR-NOR|FR-SO|FR-MC|FR-34-11|FR-66",
    "GR51": "FR-06|FR-83|FR-13",
    "GR52": "FR-06",
    "GR54": "FR-04-05|FR-ALPES-N",
    "GR55": "FR-ALPES-N",
    "GR56": "FR-04-05",
    "GR58": "FR-04-05",
    "GR65": "FR-MC|FR-SO|FR-PYR-O",
    "GR70": "FR-30-48|FR-MC",
    "GR78": "FR-PYR-O|FR-34-11|FR-66",
    "GR98": "FR-13|FR-83",
    "GR101": "FR-PYR-O",
    "GR145": "FR-EST",
    "GR653": "FR-13|FR-34-11|FR-30-48|FR-SO|FR-PYR-O",
    "GR654": "FR-SO|FR-MC|FR-EST",
    "GR655": "FR-EST|FR-IDF-CVL|FR-SO|FR-PYR-O",
    "GR738": "FR-ALPES-N",
    "GTM": "FR-06",
    "GTJ": "FR-EST|FR-ALPES-N",
}
P1 = set(OVERRIDES) | {"GRR1", "GRR2", "GRR3", "TMB", "HRP", "HRMP"}

COMPOSTELLE_GR = {"GR65", "GR653", "GR654", "GR655", "GR78", "GR101", "GR652"}


def clean(t):
    t = re.sub(r"<ref[^>]*>.*?</ref>", "", t, flags=re.S)
    t = re.sub(r"<ref[^>]*/>", "", t)
    t = re.sub(r"\[\[([^|\]]*\|)?([^\]]+)\]\]", r"\2", t)
    t = re.sub(r"\{\{,\}\}", "", t)
    t = re.sub(r"\{\{[^{}]*\}\}", "", t)
    t = t.replace("'''", "").replace("''", "")
    t = re.sub(r"<br\s*/?>", " — ", t)
    return re.sub(r"\s+", " ", t).strip(" —:•")


def zones_from_text(text):
    """Départements cherchés UNIQUEMENT dans les parenthèses (le format Wikipédia
    y met les départements) — évite les faux positifs type « Auvers-sur-Oise »."""
    zones = []
    scope = " ; ".join(re.findall(r"\(([^)]+)\)", text))
    for name, code in DEPT_NAME.items():
        if re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", scope):
            z = DEPT_ZONE[code]
            if z not in zones:
                zones.append(z)
    for name, z in REGION_NOTE.items():
        if name in text and z not in zones:
            zones.append(z)
    return zones


rows = []  # code, nom, type, pays, zones, priorite, source, notes

# ---------------------------------------------------------------- GR France
w = open("gr_list.wiki", encoding="utf-8").read()
sections = re.split(r"^=== (.+?) ===$", w, flags=re.M)
for i in range(1, len(sections), 2):
    sec, body = sections[i], sections[i + 1]
    for m in re.finditer(r"\{\{SGR\|\s*([A-Za-z0-9]*)\s*\|(.*?)\}\}\n", body, re.S):
        num, content = m.group(1).strip(), m.group(2)
        parts = content.split(":", 1)
        nom = clean(parts[0])
        via = clean(parts[1]) if len(parts) > 1 else ""
        if "transfrontaliers" in sec:
            code, typ, pays = f"GRT{num[1:]}", "GRT", "FR/ES"
            zdef = "FR-PYR-O|FR-66"
            zones = zones_from_text(nom + " " + via) or zdef.split("|")
        elif "outre-mer" in sec:
            code, typ, pays = f"GR{num}", "GR", "FR (outre-mer)"
            zones = ["FR-974"] if num.startswith("R") else []
        elif "non numérotés" in sec:
            code = num if num else re.sub(r"[^A-Za-zÀ-ÿ]", "", nom.split(" — ")[0])[:24]
            typ, pays = "GR", "FR"
            zones = zones_from_text(nom + " " + via)
        else:
            code, typ, pays = f"GR{num}", "GR", "FR"
            zones = zones_from_text(nom + " " + via)
        if code in OVERRIDES:
            zones = OVERRIDES[code].split("|")
        notes = ""
        if code in COMPOSTELLE_GR:
            notes = "voie de Compostelle (France)"
        if code == "GR5":
            pays = "NL/BE/LU/FR"
        prio = "P1" if code in P1 else ("P3" if typ == "GRT" else "P2")
        if not zones:
            if "outre-mer" in sec:
                zones, notes = [], (notes + " ; " if notes else "") + "hors périmètre pilote (Antilles/NC/Guyane)"
                prio = "HP"
            else:
                notes = (notes + " ; " if notes else "") + "zones à préciser"
        rows.append([code, nom, typ, pays, "|".join(zones), prio, "wikipedia:GR-France", notes])

# ---------------------------------------------------------------- GRP
w = open("grp_list.wiki", encoding="utf-8").read()
region, dept = "", ""
for line in w.splitlines():
    m = re.match(r"^== (.+?) ==$", line)
    if m:
        region, dept = clean(m.group(1)), ""
        continue
    m = re.match(r"^=== (.+?) ===$", line)
    if m:
        dept = clean(m.group(1))
        continue
    m = re.match(r"^\*\s*\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", line)
    if m and region and "Notes" not in region:
        nom = clean(m.group(1))
        code_dept = DEPT_NAME.get(dept)
        zones = [DEPT_ZONE[code_dept]] if code_dept else zones_from_text(dept + " " + region)
        rows.append(["", nom, "GRP", "FR", "|".join(zones), "P3",
                     "wikipedia:GRP", f"{dept or region}"])

# ---------------------------------------------------------------- couches curées
CURATED = [
    ["HRP", "Haute Route Pyrénéenne", "HR", "FR/ES/AD", "FR-PYR-O|FR-66|ES-NAV-RIO-ARA|ES-CAT", "P1", "curated", "haute route, hors GR"],
    ["HRMP", "Haute Route des Monts Perdus", "HR", "FR/ES", "FR-PYR-O|ES-NAV-RIO-ARA", "P1", "curated", "Gavarnie/Ordesa"],
    ["HR-CHX-ZERMATT", "Haute Route Chamonix – Zermatt", "HR", "FR/CH", "FR-ALPES-N", "P2", "curated", "partie CH hors périmètre pilote"],
    ["TMB", "Tour du Mont-Blanc", "GR-INT", "FR/IT/CH", "FR-ALPES-N", "P1", "curated", "parties IT/CH hors périmètre pilote"],
    ["CAM-FRANCES", "Camino Francés (SJPP → Santiago)", "CAMINO", "FR/ES", "FR-PYR-O|ES-NAV-RIO-ARA|ES-CYL|ES-GAL", "P1", "curated", ""],
    ["CAM-ARAGONES", "Camino Aragonés (Somport → Puente la Reina)", "CAMINO", "ES", "ES-NAV-RIO-ARA", "P2", "curated", ""],
    ["CAM-NORTE", "Camino del Norte (Irún → Santiago)", "CAMINO", "ES", "ES-NORTE|ES-GAL", "P1", "curated", ""],
    ["CAM-PRIMITIVO", "Camino Primitivo (Oviedo → Santiago)", "CAMINO", "ES", "ES-NORTE|ES-GAL", "P1", "curated", ""],
    ["CAM-INGLES", "Camino Inglés (Ferrol/A Coruña → Santiago)", "CAMINO", "ES", "ES-GAL", "P2", "curated", ""],
    ["CAM-PORT-CENTRAL", "Camino Portugués Central (Porto → Santiago)", "CAMINO", "PT/ES", "PT-NORTE|ES-GAL", "P1", "curated", ""],
    ["CAM-PORT-COSTA", "Camino Portugués da Costa", "CAMINO", "PT/ES", "PT-NORTE|ES-GAL", "P2", "curated", ""],
    ["CAM-PLATA", "Vía de la Plata (Sevilla → Astorga)", "CAMINO", "ES", "ES-CYL", "P2", "curated", "tronçon sud (Extremadura/Andalucía) hors périmètre pilote"],
    ["CAM-SANABRES", "Camino Sanabrés (Granja de Moreruela → Santiago)", "CAMINO", "ES", "ES-CYL|ES-GAL", "P2", "curated", ""],
    ["CAM-INVIERNO", "Camino de Invierno (Ponferrada → Santiago)", "CAMINO", "ES", "ES-CYL|ES-GAL", "P2", "curated", ""],
    ["CAM-BAZTAN", "Camino del Baztán (Bayonne → Pamplona)", "CAMINO", "FR/ES", "FR-PYR-O|ES-NAV-RIO-ARA", "P2", "curated", ""],
    ["CAM-VASCO", "Camino Vasco del Interior (Irún → Sto Domingo/Burgos)", "CAMINO", "ES", "ES-NORTE|ES-CYL", "P3", "curated", "túnel de San Adrián"],
    ["CAM-LEBANIEGO", "Camino Lebaniego (San Vicente → Sto Toribio)", "CAMINO", "ES", "ES-NORTE", "P3", "curated", ""],
    ["CAM-SALVADOR", "Camino del Salvador (León → Oviedo)", "CAMINO", "ES", "ES-CYL|ES-NORTE", "P3", "curated", ""],
    ["CAM-OLVIDADO", "Camino Olvidado (Bilbao → Ponferrada)", "CAMINO", "ES", "ES-NORTE|ES-CYL", "P3", "curated", ""],
    ["CAM-MADRID", "Camino de Madrid (Madrid → Sahagún)", "CAMINO", "ES", "ES-CYL", "P3", "curated", "départ Madrid hors zones pilote"],
    ["CAM-CATALAN", "Camí de Sant Jaume / Camino Catalán", "CAMINO", "ES", "ES-CAT|ES-NAV-RIO-ARA", "P3", "curated", ""],
    ["CAM-FINISTERRE", "Epílogo Finisterre – Muxía", "CAMINO", "ES", "ES-GAL", "P1", "curated", ""],
    ["GR11-ES", "GR11 — Senda Transpirenaica (ES)", "GR", "ES/AD", "ES-NORTE|ES-NAV-RIO-ARA|ES-CAT", "P2", "curated", "versant sud des Pyrénées"],
]
rows.extend(CURATED)

# GRP corses (Mare a Mare / Mare e Monti) si absents du parsing GRP
noms = " ; ".join(r[1] for r in rows)
for nom in ["Mare a Mare Nord", "Mare a Mare Centre", "Mare a Mare Sud",
            "Mare e Monti Nord", "Mare e Monti Sud"]:
    if nom not in noms:
        rows.append(["", nom, "GRP", "FR", "FR-CORSE", "P2", "curated", "Corse"])

# ---------------------------------------------------------------- patchs manuels
# zones connues (mapping massif/région de connaissance générale, note "estimé")
PATCH_ZONES = {
    "GR16": "FR-EST", "GR23": "FR-NOR", "GR25": "FR-NOR", "GR52A": "FR-06",
    "GR62": "FR-30-48|FR-MC", "GR62A": "FR-30-48|FR-MC", "GR63": "FR-84-26-07",
    "GR66": "FR-30-48", "GR67": "FR-30-48", "GR69": "FR-13|FR-04-05",
    "GR80": "FR-SO", "GR91B": "FR-84-26-07", "GR94": "FR-04-05|FR-84-26-07",
    "GR97": "FR-84-26-07", "GR108": "FR-PYR-O", "GR108A": "FR-PYR-O",
    "GR121B": "FR-EST", "GR121C": "FR-EST", "GR127": "FR-EST", "GR128A": "FR-EST",
    "GR137": "FR-EST", "GR169": "FR-MC", "GR222": "FR-NOR", "GR223": "FR-NOR",
    "GR224": "FR-NOR", "GR226": "FR-NOR", "GR235": "FR-NOR", "GR303": "FR-MC",
    "GR340": "FR-BRE", "GR342": "FR-BRE", "GR349": "FR-BRE", "GR351": "FR-EST",
    "GR360": "FR-SO", "GR364": "FR-SO", "GR365": "FR-SO", "GR367": "FR-34-11",
    "GR406": "FR-06|FR-04-05", "GR429": "FR-84-26-07", "GR440": "FR-MC",
    "GR441": "FR-MC", "GR461": "FR-SO", "GR463": "FR-SO", "GR465": "FR-MC",
    "GR534": "FR-EST", "GR549": "FR-ALPES-N", "GR559": "FR-EST", "GR590": "FR-EST",
    "GR595": "FR-EST", "GR620": "FR-MC", "GR636": "FR-SO",
    "GR653A": "FR-06|FR-83|FR-13", "GR653D": "FR-04-05|FR-84-26-07|FR-13",
    "GR765": "FR-EST|FR-MC", "GR787": "FR-34-11", "GR861": "FR-PYR-O",
    "TourduCézallier": "FR-MC", "TGV": "FR-ALPES-N",
    "GR1": "FR-IDF-CVL", "GR11": "FR-IDF-CVL", "GR15": "FR-IDF-CVL|FR-EST",
    "GR59": "FR-EST", "GR61": "FR-30-48", "GR62B": "FR-MC", "GR68": "FR-30-48",
    "GR96": "FR-ALPES-N", "GR125": "FR-EST", "GR225": "FR-NOR|FR-IDF-CVL",
    "GR353": "FR-IDF-CVL", "GR400": "FR-MC", "GR412": "FR-MC", "GR470": "FR-MC",
    "GRP-METROPOLE-DE-LYON-PAR-LES-FORTS": "FR-MC",
    "GRP-MONTS-ET-COTEAUX-DU-LYONNAIS": "FR-MC",
    "GRP-TOUR-DES-MONTS-DU-LYONNAIS": "FR-MC",
    "GRP-TOUR-DU-BEAUJOLAIS-DES-PIERRES-DOREES": "FR-MC",
}
PATCH_NOTES = {
    "GR367": "sentier Cathare", "GR653A": "Via Aurelia (Compostelle)",
    "GR653D": "Via Domitia (Compostelle)", "GR765": "voie de Cluny/Lyon (Compostelle)",
    "GR861": "Via Garona", "GR127": "De Dennebrœucq à Arras",
}
DROP_NOMS = {"Liste des sentiers de grande randonnée de France",
             "Sentiers de grande randonnée de pays"}
CURATED_CODES = {c[0] for c in CURATED}
seen_curated = set()
cleaned = []
for r in rows:
    # scories de parsing : paramètre GR_lien= et fragments de template
    r[1] = re.sub(r"^GR_lien=[^|]*\|\s*", "", r[1])
    if "}}" in r[1]:
        r[1] = r[1].split("}}")[0].strip()
        if r[0] == "GR412":
            r[7] = (r[7] + " ; " if r[7] else "") + "supprimé de la numérotation"
    if r[0] in ("HRP", "TMB", "HRMP") and r[6] != "curated":
        continue  # doublon wiki des versions curées
    if r[0] in PATCH_ZONES and not r[4]:
        r[4] = PATCH_ZONES[r[0]]
        r[7] = (r[7].replace("zones à préciser", "").strip(" ;") or "")
        r[7] = (r[7] + " ; " if r[7] else "") + "zones estimées (massif)"
    if r[0] in PATCH_NOTES:
        extra = PATCH_NOTES[r[0]]
        if r[0] == "GR127":
            r[1] = extra
        elif extra not in r[7]:
            r[7] = (r[7] + " ; " if r[7] else "") + extra
    cleaned.append(r)
rows = cleaned
# GR128 perdu par le glitch de parsing (imbriqué dans GR127)
if not any(r[0] == "GR128" for r in rows):
    rows.append(["GR128", "De Wissant à Aix-la-Chapelle", "GR", "FR/BE/DE",
                 "FR-EST", "P2", "wikipedia:GR-France", "réparé (glitch parsing)"])
# tri : GR num, GR autres, GRT, HR, CAMINO, GRP
def sort_key(r):
    order = {"GR": 0, "GR-INT": 1, "HR": 2, "CAMINO": 3, "GRT": 4, "GRP": 5}
    m = re.match(r"^GR(\d+)([A-Z]*)$", r[0])
    return (order.get(r[2], 9), int(m.group(1)) if m else 9999, r[0])
rows = [r for r in rows if r[1] not in DROP_NOMS]
rows.sort(key=sort_key)

# codes GRP auto (slug) quand vides
for r in rows:
    if not r[0]:
        r[0] = "GRP-" + re.sub(r"[^A-Z0-9]+", "-",
               r[1].upper().replace("GRP", "").replace("É", "E").replace("È", "E")
               .replace("Ê", "E").replace("À", "A").replace("Ô", "O").replace("Î", "I")
               .replace("Û", "U").replace("Ç", "C")).strip("-")[:38]

# seconde passe de patch (les codes GRP-slug n'existaient pas à la 1re passe)
for r in rows:
    if r[0] in PATCH_ZONES and not r[4]:
        r[4] = PATCH_ZONES[r[0]]
        r[7] = (r[7] + " ; " if r[7] else "") + "zones estimées (massif)"

# fusion des GRP listés sous plusieurs départements (union des zones)
merged, by_code = [], {}
for r in rows:
    if r[2] == "GRP" and r[0] in by_code:
        prev = by_code[r[0]]
        prev[4] = "|".join(dict.fromkeys((prev[4] + "|" + r[4]).strip("|").split("|")))
        if r[7] and r[7] not in prev[7]:
            prev[7] = (prev[7] + " + " if prev[7] else "") + r[7]
        continue
    by_code[r[0]] = r
    merged.append(r)
rows = merged

with open(OUT, "w", newline="", encoding="utf-8") as f:
    wcsv = csv.writer(f, delimiter=";")
    wcsv.writerow(["code", "nom", "type", "pays", "zones_sources", "priorite", "source", "notes"])
    wcsv.writerows(rows)

from collections import Counter
print("total:", len(rows), dict(Counter(r[2] for r in rows)))
print("prio :", dict(Counter(r[5] for r in rows)))
manquants = [r[0] for r in rows if not r[4]]
print("sans zone:", len(manquants), manquants[:25])
EOF_MARKER = None
