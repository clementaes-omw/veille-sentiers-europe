#!/usr/bin/env python3
"""
Générateur du site « Veille Sentiers Europe » (pilote France + Caminos ES).

Lit les livrables de l'agent veille-europe (livrables/) :
  - digest_YYYY-MM-DD.md   (un par jour)
  - alertes-actives.md     (registre persistant, tableau markdown)
et produit site/index.html : une page autonome (HTML + CSS + JS inline)
avec le registre d'alertes rendu en cartes et les digests archivés par date.

Sans dépendance. Usage : python3 build_site.py
"""
import csv
import html
import json
import re
import subprocess
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIVRABLES = HERE.parent / "livrables"
OUT = HERE / "index.html"
# Analytics (Umami Cloud, sans cookies — pas de bannière RGPD nécessaire).
# Renseigner le website ID fourni par cloud.umami.is pour activer ; vide = pas de script.
UMAMI_WEBSITE_ID = "135c550a-aa46-47be-9e60-f5b5c936eb52"
# Formulaire de contact — le site est statique (Pages), il faut un relais pour recevoir.
# On utilise l'IDENTIFIANT FormSubmit et non l'adresse e-mail : celle-ci n'apparaît donc
# nulle part dans le HTML public, hors de portée des robots à spam (c'est tout l'intérêt
# du formulaire face à un lien mailto). Le jeton est public par conception — il ne permet
# que d'envoyer un message vers la boîte, jamais de la lire ni de découvrir l'adresse.
# Formulaire activé le 2026-07-26 (destination : contact@alertes-rando.info).
FORM_ENDPOINT = "https://formsubmit.co/75c4f4f7d26954df26f9d870cfeb0c82"

# --- COULEURS ---------------------------------------------------------------
# Deux palettes, écrites UNE fois ici puis interpolées dans le CSS (le thème manuel
# et le thème système ont besoin du même jeu à deux endroits : les dupliquer à la
# main, c'était quatre copies à garder d'accord).
#
# Distinction qui manquait : --ink est la couleur du TEXTE. Le bandeau de navigation
# s'en servait comme fond ; en thème sombre --ink passe au crème et la barre virait
# au blanc en haut d'une page noire. --surface-invert est un fond, il reste sombre
# dans les deux thèmes. Même logique pour --on-accent, le texte posé sur un aplat
# --pine : blanc sur le vert foncé du thème clair, encre sur le vert clair du sombre
# (c'est le blanc en dur qui tombait à 2.34:1).
PALETTE_CLAIR = """
  --paper: #ffffff; --panel: #f1efe8; --ink: #20261f; --ink-2: #545a4f;
  --line: #ddd9cc; --pine: #2f5d45; --pine-soft: #e4ece6;
  --haute: #a83227; --haute-bg: #f6e7e4; --moy: #8a5715; --moy-bg: #f4ecdd;
  --info: #45607a; --info-bg: #e7edf1; --clos: #5e635b; --clos-bg: #e8e7e0;
  --surface-invert: #20261f; --on-invert: #f1efe8; --on-accent: #ffffff;"""
PALETTE_SOMBRE = """
  --paper: #1a1e1a; --panel: #22271f; --ink: #e6e4da; --ink-2: #a7ab9e;
  --line: #3a4036; --pine: #7fb598; --pine-soft: #26332b;
  --haute: #e07a6e; --haute-bg: #392420; --moy: #d8a35c; --moy-bg: #362c1c;
  --info: #93b0c4; --info-bg: #232d34; --clos: #9ba196; --clos-bg: #262a24;
  --surface-invert: #10130f; --on-invert: #e6e4da; --on-accent: #14211a;"""
CATEGORIES = json.loads(
    (HERE.parent / "referentiel" / "categories.json").read_text(encoding="utf-8"))["categories"]


def fold_txt(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s if not unicodedata.combining(ch)).lower()


def categorize(c):
    """Catégorie d'une alerte = 1re catégorie dont un mot-clé matche le champ Type
    (ordre du json = priorité). None si type orphelin → violation QA."""
    t = fold_txt(c["type"])
    for cat in CATEGORIES:
        if any(k in t for k in cat["keywords"]):
            return cat
    return None

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
MOIS_COURT = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.",
              "août", "sept.", "oct.", "nov.", "déc."]

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)([^*]+?)(?<!\*)\*(?!\*)")
CODE_RE = re.compile(r"`([^`]+)`")
STRIKE_RE = re.compile(r"~~(.+?)~~")


def fr_date(iso: str, court: bool = False) -> str:
    d = date.fromisoformat(iso)
    mois = MOIS_COURT[d.month - 1] if court else MOIS[d.month - 1]
    jour = "1er" if d.day == 1 else str(d.day)
    return f"{jour} {mois} {d.year}" if not court else f"{jour} {mois}"


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = LINK_RE.sub(
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}" target="_blank" '
                  f'rel="noopener">{m.group(1)}</a>', text)
    text = STRIKE_RE.sub(r"<del>\1</del>", text)
    text = BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = ITALIC_RE.sub(r"<em>\1</em>", text)
    text = CODE_RE.sub(r"<code>\1</code>", text)
    # marqueurs de fiabilité de l'agent → pastilles
    text = text.replace("[FAIT]", '<span class="tag fait">FAIT</span>')
    text = re.sub(r"\[HYPOTHÈSE( faible)?\]",
                  lambda m: f'<span class="tag hypo">HYPOTHÈSE{m.group(1) or ""}</span>', text)
    text = text.replace("[à vérifier manuellement]", '<span class="tag verif">à vérifier</span>')
    text = text.replace("[CLÔTURÉ]", '<span class="tag clos">CLÔTURÉ</span>')
    return text


def sev_class(text: str) -> str:
    """Classe de sévérité = premier mot-clé rencontré (« MOYENNE (haute pour
    la trace) » doit rester moyenne)."""
    up = text.upper()
    if "CLÔTURÉ" in up:
        return "clos"
    m = re.search(r"HAUTE|MOYENNE|INFO", up)
    if not m:
        return "info"
    return {"HAUTE": "haute", "MOYENNE": "moyenne", "INFO": "info"}[m.group(0)]


def md_to_html(md: str, skip_h1: bool = True) -> str:
    """Markdown → HTML (titres, listes imbriquées, blockquote, hr, tableaux, paragraphes)."""
    lines = md.splitlines()
    parts, para = [], []
    list_stack = []  # niveaux d'indentation ouverts

    def close_lists(to_level=-1):
        while list_stack and list_stack[-1] > to_level:
            parts.append("</ul>")
            list_stack.pop()

    def flush_para():
        if para:
            parts.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    i = 0
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if not s:
            flush_para()
            close_lists()
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,})$", s):
            flush_para(); close_lists()
            parts.append("<hr>")
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            flush_para(); close_lists()
            level = len(m.group(1))
            if not (level == 1 and skip_h1):
                txt = m.group(2)
                cls = ""
                if level == 3:
                    cls = f' class="sev-{sev_class(txt)}"'
                parts.append(f"<h{level}{cls}>{inline(txt)}</h{level}>")
            i += 1
            continue
        if s.startswith(">"):
            flush_para(); close_lists()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip("> ").strip())
                i += 1
            parts.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
            continue
        if s.startswith("|"):
            flush_para(); close_lists()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            parts.append(render_table(rows))
            continue
        m = re.match(r"^(\s*)[-*]\s+(.*)$", raw)
        if m:
            flush_para()
            indent = len(m.group(1)) // 2
            if not list_stack or indent > list_stack[-1]:
                parts.append("<ul>")
                list_stack.append(indent)
            else:
                close_lists(indent)
                if not list_stack:
                    parts.append("<ul>")
                    list_stack.append(indent)
            # recolle les continuations indentées non-liste
            item = m.group(2)
            while (i + 1 < len(lines)
                   and re.match(r"^\s{2,}\S", lines[i + 1])
                   and not re.match(r"^\s*[-*]\s", lines[i + 1])
                   and not lines[i + 1].strip().startswith(("#", "|", ">"))):
                item += " " + lines[i + 1].strip()
                i += 1
            parts.append(f"<li>{inline(item)}</li>")
            i += 1
            continue
        close_lists()
        para.append(s)
        i += 1
    flush_para()
    close_lists()
    return "\n".join(parts)


def split_row(row: str):
    row = row.strip().strip("|")
    row = row.replace("\\|", "\x00")
    return [c.strip().replace("\x00", "|") for c in row.split("|")]


def render_table(rows):
    body = []
    header = None
    for r in rows:
        cells = split_row(r)
        if all(re.match(r"^:?-{2,}:?$", c) for c in cells if c):
            continue
        if header is None:
            header = cells
            continue
        body.append(cells)
    if header is None:
        return ""
    th = "".join(f"<th>{inline(c)}</th>" for c in header)
    trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>"
                  for cells in body)
    return f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


# ---------------------------------------------------------------- registre

# Depuis 2026-07-25, le registre n'est plus un fichier monolithique mais un dossier :
# une alerte = un fichier livrables/alertes/<clé slugifiée>.md. Motif : l'agent réécrit
# chaque fichier en entier (les outils GitHub ne savent pas patcher une ligne) ; sur
# 122 Ko il condensait le texte au lieu de le reproduire — 1,5 Ko se réécrit sans perte.
ALERTES_DIR = LIVRABLES / "alertes"
CHAMPS_ENTETE = ["cle", "type", "itin", "sev", "validite", "detection", "verif", "statut"]
CHAMPS_SECTION = {"portion concernée": "portion", "alternative": "alternative",
                  "zone (détails)": "zone", "source": "source"}
TOUS_CHAMPS = ["cle", "type", "portion", "alternative", "zone", "itin", "sev",
               "validite", "detection", "verif", "source", "statut"]


def parse_alerte(md: str) -> dict:
    """Un fichier d'alerte → dict de 12 champs (même forme que l'ancien tableau).
    Front-matter `champ: valeur` entre --- , puis sections `## Titre` pour le texte long."""
    champs = {k: "" for k in TOUS_CHAMPS}
    champs["ordre"] = 10**6                      # sans `ordre` → en fin de groupe
    lignes = md.splitlines()
    i = 0
    if lignes and lignes[0].strip() == "---":    # front-matter
        i = 1
        while i < len(lignes) and lignes[i].strip() != "---":
            cle, sep, val = lignes[i].partition(":")
            cle = cle.strip()
            if sep and cle in CHAMPS_ENTETE:
                champs[cle] = val.strip()
            elif sep and cle == "ordre":
                champs["ordre"] = int(val.strip() or 10**6)
            i += 1
        i += 1
    courant, tampon = None, []                   # sections
    def vider():
        if courant:
            champs[courant] = "\n".join(tampon).strip()
    for ligne in lignes[i:]:
        if ligne.startswith("## "):
            vider()
            courant = CHAMPS_SECTION.get(ligne[3:].strip().lower())
            tampon = []
        elif courant:
            tampon.append(ligne)
    vider()
    return champs


def load_alertes():
    """Charge toutes les alertes du dossier, ordonnées comme dans l'ancien tableau."""
    if not ALERTES_DIR.is_dir():
        return []
    cards = []
    for p in sorted(ALERTES_DIR.glob("*.md")):
        if p.name.lower() == "readme.md":
            continue
        c = parse_alerte(p.read_text(encoding="utf-8"))
        c["_fichier"] = p.name
        cards.append(c)
    cards.sort(key=lambda c: (c["ordre"], c["_fichier"]))
    return cards


def parse_registre(md: str):
    """[LEGACY] Ancien registre monolithique — conservé pour rejouer un état d'archive."""
    lines = md.splitlines()
    cards, rest = [], []
    header_seen = False
    for line in lines:
        s = line.strip()
        if s.startswith("|"):
            cells = split_row(s)
            if all(re.match(r"^:?-{2,}:?$", c) for c in cells if c):
                continue
            if not header_seen:
                header_seen = True  # ligne d'en-tête, ignorée
                continue
            if len(cells) >= 12:
                cards.append(dict(zip(
                    ["cle", "type", "portion", "alternative", "zone", "itin", "sev",
                     "validite", "detection", "verif", "source", "statut"], cells)))
            elif len(cells) >= 10:  # ancien schéma (10 col.) toléré
                c = dict(zip(["cle", "type", "zone", "itin", "sev", "validite",
                              "detection", "verif", "source", "statut"], cells))
                c["portion"], c["alternative"] = "", ""
                cards.append(c)
            continue
        rest.append(line)
    return cards, "\n".join(rest)


TRAIL_RE = re.compile(
    r"(GR\s?®?\s?R?\d+[A-Za-z]?(?:[-–]ES|[-–]BE)?"
    r"|HRP|HRMP|TMB|GTJ|GTM|GTA|Kungsleden|Laugavegur|Adlerweg|Westweg"
    r"|Rota Vicentina|Pieterpad|Mullerthal"
    r"|Camino [A-ZÀ-ÿ][\wÀ-ÿ]*(?: d[aeo][ls]? [A-ZÀ-ÿ][\wÀ-ÿ]*| [A-ZÀ-ÿ][\wÀ-ÿ]*)?"
    r"|Vía de la Plata|Via [A-Z][\wÀ-ÿ]+|Sentiero [A-Z][\wÀ-ÿ]+"
    r"|Alta Via [\w À-ÿ]+?(?=\s*[—(;,.]|$)"
    r"|West Highland Way|Pennine Way|Wicklow Way|Kerry Way"
    r"|Tour [\wÀ-ÿ' -]+?(?=\s*[—(;,.]|$))")


def clamp_word(s: str, n: int = 22) -> str:
    s = s.strip(" -–—")
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0].strip(" -–—")
    return (cut or s[:n]) + "…"


def itin_badges(c) -> list:
    """Badges sentiers : TOUS les sentiers reconnus dans Itinéraires (puis Portion en
    repli), dédoublonnés, hors mentions « non concerné » ; repli = zone de la clé."""
    seen = []
    for text in (c["itin"], c["portion"]):
        for m in TRAIL_RE.finditer(text):
            suite = text[m.end():m.end() + 40]
            if re.match(r"\s*(\([^)]*\))?\s*(NON|non) concern", suite):
                continue
            b = clamp_word(m.group(0).replace("GR ", "GR"))
            if b not in seen:
                seen.append(b)
        if seen:
            break
    if not seen:
        parts = c["cle"].split("|")
        seen = [clamp_word(parts[1] if len(parts) > 1 else c["itin"], 20) or "—"]
    if len(seen) > 5:
        seen = seen[:5] + [f"+{len(seen) - 5}"]
    return seen


def itin_badge(c) -> str:
    return itin_badges(c)[0]


_CLES_DU_JOUR = None


def cles_du_jour() -> set:
    """Clés citées par le digest le plus récent = les alertes réellement bougées au
    dernier passage. C'est la seule définition qui s'EFFACE toute seule : tirée du champ
    `statut:`, la pastille « changé » restait collée à la fiche des semaines après le
    changement (25 cartes sur 60 la portaient le 02/08/2026, dont des reroutages de 2025).
    Le digest, lui, ne liste que le NOUVEAU/CHANGÉ du jour."""
    global _CLES_DU_JOUR
    if _CLES_DU_JOUR is None:
        digests = sorted(LIVRABLES.glob("digest_*.md"))
        txt = digests[-1].read_text(encoding="utf-8") if digests else ""
        _CLES_DU_JOUR = set(re.findall(r"`([^`]+\|[^`]+)`", txt))
    return _CLES_DU_JOUR


def render_card(c) -> str:
    statut_txt = c["statut"]
    closed = "CLÔTURÉ" in statut_txt.upper()
    sev = "clos" if closed else sev_class(c["sev"])
    sev_label = {"haute": "Alerte rouge", "moyenne": "Alerte orange",
                 "info": "Info", "clos": "Clôturée"}[sev]
    changed = c["cle"] in cles_du_jour()
    chips = ""
    if changed and not closed:
        chips += ('<span class="chip changed" title="Alerte déjà connue dont la situation a '
                  'évolué au dernier passage de veille (surface, dates, périmètre…)">changé</span>')
    iso_re = re.compile(r"^\d{4}-\d{2}-\d{2}")
    det_txt = (fr_date(c["detection"][:10], True) if iso_re.match(c["detection"])
               else html.escape(c["detection"][:16]))
    ver_txt = (fr_date(c["verif"][:10], True) if iso_re.match(c["verif"])
               else html.escape(c["verif"][:16]))
    dates = (f'<span title="Première détection">détectée {det_txt}</span>'
             f'<span class="sep">·</span>'
             f'<span title="Dernière vérification">vérifiée {ver_txt}</span>')
    searchable = re.sub(r"[*`~\[\]\\]|\([^)]*\)$", "",
                        " ".join([c["itin"], c["portion"], c["zone"]]))
    searchable = unicodedata.normalize("NFD", searchable)
    searchable = "".join(ch for ch in searchable if not unicodedata.combining(ch)).lower()
    lead = c["portion"] or c["zone"]  # repli si ancien schéma 10 colonnes
    alt = c["alternative"] or "Aucune alternative connue à ce jour."
    cat = categorize(c)
    cat_slug = cat["slug"] if cat else "inconnue"
    badges_html = "\n    ".join(f'<span class="badge itin">{html.escape(b)}</span>'
                                for b in itin_badges(c))
    # La ligne de tête (sentiers, gravité, type) sert de TITRE de la fiche : sans elle,
    # 167 articles se suivaient sans un seul point de saut pour un lecteur d'écran.
    # L'infobulle qui portait la légende de gravité est retirée : répétée 71 fois,
    # inatteignable au doigt et au clavier, elle est maintenant affichée en clair
    # une seule fois sous les filtres.
    return f"""<article class="card {sev}" data-itin="{html.escape(searchable, quote=True)}" data-cat="{cat_slug}">
  <h3 class="card-top">
    {badges_html}
    <span class="badge sev-{sev}">{sev_label}</span>
    {chips}
    <span class="type">{inline(c["type"])}</span>
  </h3>
  <p class="portion">{inline(lead)}</p>
  <p class="alt"><span class="alt-label">Alternative</span> {inline(alt)}</p>
  <details>
    <summary>Détails</summary>
    <p>{inline(c["zone"])}</p>
  </details>
  <p class="meta dates"><span title="Validité">{inline(c["validite"])}</span><span class="sep">·</span>{dates}</p>
  <p class="meta sources">Sources : {inline(c["source"])}</p>
</article>"""



# ---------------------------------------------------------------- bivouac

BIV_COLS = ["pays", "zone", "nom", "type", "regle", "conditions", "feu", "sentiers",
            "source_url", "date_source", "date_verif", "statut", "notes"]
# Pas d'emoji dans ces pastilles : les cartes d'alerte n'en portent pas, la règle est
# déjà écrite en toutes lettres et la couleur fait le reste. Un emoji décoratif à côté
# d'un mot qui dit la même chose est l'un des marqueurs d'écriture générée.
REGLE_META = {
    "interdit": ("Interdit", "haute"),
    "tolere": ("Toléré (conditions)", "moyenne"),
    "autorise": ("Autorisé", "ok"),
    "variable": ("Variable / droit commun", "info"),
}


def load_bivouac():
    p = HERE.parent / "referentiel" / "bivouac.csv"
    if not p.exists():
        return []
    rows = list(csv.reader(p.open(encoding="utf-8"), delimiter=";"))
    out = []
    for r in rows[1:]:
        if len(r) >= 13 and r[0].strip():
            out.append(dict(zip(BIV_COLS, [c.strip() for c in r])))
    order = {"FR": 0, "CH": 1, "IT": 2, "AT": 3, "DE": 4, "ES": 5, "PT": 6}
    out.sort(key=lambda b: (order.get(b["pays"], 9), b["nom"]))
    return out


def render_bivouac_card(b) -> str:
    label, cls = REGLE_META.get(b["regle"], (b["regle"], "info"))
    searchable = fold_txt(" ".join([b["nom"], b["sentiers"], b["zone"], b["pays"], b["conditions"]]))
    searchable = re.sub(r"[*`~\[\]\\]", "", searchable)
    hyp = ('<span class="tag hypo">HYPOTHÈSE</span> ' if b["statut"].upper().startswith("HYPO") else "")
    src = b["source_url"]
    src_html = (f'<a href="{html.escape(src, quote=True)}" target="_blank" rel="noopener">'
                f'{html.escape(src.split("/")[2] if "://" in src else src)}</a>') if src else "—"
    notes = f'<p class="meta">{inline(b["notes"])}</p>' if b["notes"] else ""
    return f"""<article class="card bcard {cls}" data-bsearch="{html.escape(searchable, quote=True)}" data-regle="{b["regle"]}">
  <div class="card-top">
    <span class="badge itin">{html.escape(b["pays"])}</span>
    <span class="badge sev-{'haute' if cls=='haute' else 'moyenne' if cls=='moyenne' else 'info' if cls=='info' else 'ok'}">{label}</span>
    <span class="type">{html.escape(b["type"])}</span>
  </div>
  <h3 class="bname">{inline(b["nom"])}</h3>
  <p class="portion">{hyp}{inline(b["conditions"])}</p>
  <p class="alt"><span class="alt-label">Feux</span> {inline(b["feu"] or "non précisé")}</p>
  {notes}
  <p class="meta dates"><span>{inline(b["sentiers"])}</span><span class="sep">·</span>source du {html.escape(b["date_source"])}<span class="sep">·</span>vérifié le {html.escape(b["date_verif"])}</p>
  <p class="meta sources">Source : {src_html}</p>
</article>"""

# ---------------------------------------------------------------- carte

# Leaflet (carte interactive) — CDN unpkg, version épinglée + SRI officiels 1.9.4.
# La bibliothèque n'est chargée qu'à la première ouverture de l'onglet Carte (injection
# à la demande côté JS) : les autres vues ne paient pas ce téléchargement.
LEAFLET_VER = "1.9.4"
LEAFLET_CSS_URL = f"https://unpkg.com/leaflet@{LEAFLET_VER}/dist/leaflet.css"
LEAFLET_JS_URL = f"https://unpkg.com/leaflet@{LEAFLET_VER}/dist/leaflet.js"
LEAFLET_CSS_SRI = "sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
LEAFLET_JS_SRI = "sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="

ZONES_COORDS_CSV = HERE.parent / "referentiel" / "zones-coords.csv"

# Zones d'alerte (2e champ de la clé) hétérogènes → code zone-source de zones-coords.csv.
# Le préfixe suffit pour les clés déjà codées (FR-06-AlpesMaritimes → FR-06, ES-CYL-Bierzo
# → ES-CYL…) ; cette table ne couvre QUE les zones locales/nommées sans préfixe reconnu.
# Toute zone active qui n'est ni préfixée ni aliasée est listée au build (voir zones_carte).
ALIAS_ZONE = {
    # Sud-Est / Méditerranée
    "Calanques-13": "FR-13",
    "Var-83": "FR-83", "Var-Gros-Bessillon": "FR-83",
    "Gard-30": "FR-30-48",
    "Hérault-34": "FR-34-11", "Aude-11": "FR-34-11",
    "Vaucluse-84": "FR-84-26-07", "FR-Baronnies-GR9": "FR-84-26-07",
    "Drome-Justin-Die": "FR-84-26-07",
    "Corse": "FR-CORSE", "Corse-Bavella-Illarata": "FR-CORSE",
    # Alpes du Sud / Écrins
    "Écrins": "FR-04-05", "Écrins-GR54": "FR-04-05", "HautesAlpes-BoisNoir": "FR-04-05",
    # Alpes du Nord
    "Savoie-Planay-Pralognan": "FR-ALPES-N",
    # Alpes-Maritimes / Mercantour
    "Mercantour": "FR-06", "Boréon-Mercantour": "FR-06",
    # Pyrénées
    "Alberes-66": "FR-66", "PO-66": "FR-66", "PO-66-Argeles-Cerbere": "FR-66",
    "PO-66-Thues-entre-Valls": "FR-66", "PO-66-Trévillach": "FR-66",
    "Canigou-Cortalets": "FR-66",
    "PN-Pyrénées": "FR-PYR-O", "PN-Pyrenees-Moundelhs": "FR-PYR-O",
    "Ariege-Bordes-Uchentein": "FR-PYR-O", "HautesPyrenees-Bareges": "FR-PYR-O",
    "Aspe-64-Chemin-Mature": "FR-PYR-O", "GR10-Luchon-Superbagnères": "FR-PYR-O",
    # Ouest / Nord
    "GR34-CapFrehel": "FR-BRE", "GR34-Finistère": "FR-BRE", "GR34-rade-de-Brest": "FR-BRE",
    "GR21-Loges-Bénouville": "FR-NOR", "Pierrefiques-76": "FR-NOR",
    "Lot-Cieurac-Flaujac-Poujols": "FR-SO", "FR-Landes-Gironde": "FR-SO",
    "FR-IDF-Fontainebleau": "FR-IDF-CVL",
    # Réunion
    "Réunion-974": "FR-974",
    # Suisse
    "CH-Europaweg-Randa-Zermatt": "CH-VALAIS-VAUD", "TMB-CH-Orsieres": "CH-VALAIS-VAUD",
    # Italie
    "IT-ValGrande": "IT-NO", "VF-Lazio-Prato-La-Corte": "IT-CENTRE",
    # Royaume-Uni / Portugal
    "UK-Cairngorms-Glenmore": "UK-IE", "Matosinhos-PT": "PT-NORTE",
    # Baléares
    "GR221-222-Mallorca": "ES-BALEARES",
    # Balkans / Tatras
    "SI-Julijske-Alpe": "SI-HR",
    "PL-Tatras-Pusta-Dolinka": "PL-SK-TATRAS", "PL-Tatras-Rysy": "PL-SK-TATRAS",
    "SK-Tatras-Krivan": "PL-SK-TATRAS",
}


def load_zones_coords() -> dict:
    """Lit referentiel/zones-coords.csv → {code: {code, nom, lat, lon}}."""
    coords = {}
    if not ZONES_COORDS_CSV.exists():
        return coords
    for row in csv.reader(ZONES_COORDS_CSV.open(encoding="utf-8"), delimiter=";"):
        if not row or not row[0].strip() or row[0].strip().startswith("#"):
            continue
        if row[0].strip().lower() == "code":
            continue
        if len(row) < 4:
            continue
        try:
            lat, lon = float(row[2]), float(row[3])
        except ValueError:
            continue
        code = row[0].strip()
        coords[code] = {"code": code, "nom": row[1].strip(), "lat": lat, "lon": lon}
    return coords


def resolve_zone(zone_str: str, coords: dict):
    """Zone (2e champ de clé) → code zone-source. 1) alias manuel exact (insensible
    casse/accents) ; 2) préfixe : un code qui préfixe la zone à une frontière (fin de
    chaîne ou tiret), le plus long l'emporte. None si non mappable."""
    zf = fold_txt(zone_str.strip())
    for k, v in ALIAS_ZONE.items():
        if fold_txt(k) == zf:
            return v
    best = None
    for code in coords:
        cf = fold_txt(code)
        if zf == cf or zf.startswith(cf + "-"):
            if best is None or len(cf) > len(fold_txt(best)):
                best = code
    return best


def _q_token(badge: str) -> str:
    """Terme de recherche propre tiré d'un badge sentier (sans « … » ni parenthèse)."""
    return badge.split("…")[0].split("(")[0].strip()


def zones_carte(actives, coords):
    """Regroupe les alertes ACTIVES par zone-source résolue → une entrée (un marqueur)
    par zone. Retourne (liste_zones, zones_non_mappées). Les rouges sont mises en tête
    de chaque popup, et les zones sont triées par sévérité max (rouge d'abord)."""
    order = {"haute": 0, "moyenne": 1, "info": 2, "clos": 3}
    groupes, non_mappees = {}, []
    for c in actives:
        parts = c["cle"].split("|")
        zone_str = parts[1] if len(parts) > 1 else ""
        code = resolve_zone(zone_str, coords)
        if not code or code not in coords:
            non_mappees.append((zone_str, c["cle"]))
            continue
        g = groupes.get(code)
        if g is None:
            base = coords[code]
            g = {"code": code, "nom": base["nom"], "lat": base["lat"],
                 "lon": base["lon"], "alertes": []}
            groupes[code] = g
        g["alertes"].append({
            "sev": sev_class(c["sev"]),
            "type": c["type"],
            "itin": itin_badges(c),
            "cle": c["cle"],
        })
    liste = []
    for g in groupes.values():
        g["alertes"].sort(key=lambda a: order.get(a["sev"], 4))
        g["sevMax"] = g["alertes"][0]["sev"]
        g["q"] = _q_token(g["alertes"][0]["itin"][0]) if g["alertes"][0]["itin"] else ""
        liste.append(g)
    liste.sort(key=lambda g: (order.get(g["sevMax"], 4), g["nom"]))
    return liste, non_mappees


# ---------------------------------------------------------------- contrôle qualité

BADGE_INTERDITS = ["[", "]", "HYPOTH", "Aucun", "P1 ;", "à préciser", "recouper"]

# --- TON PUBLIC ------------------------------------------------------------
# « Portion concernée » et « Alternative » s'adressent à un randonneur qui prépare
# son étape, pas au journal de bord de la veille. Ces fragments trahissent le
# narratif interne du run (couverture, indexation, tentatives) : ils n'ont rien à
# faire sur le site. Comparés sur le texte replié (fold_txt) → sans accents.
JARGON_INTERNE = [
    "ce run", "au dernier run", "run europe", "runs ", "des runs", "prochain run",
    "reindexation", "indexation", "pages indexees", "non indexe", "trou de couverture",
    "lot t2", "lot bivouac", "cadence", "perimetre du jour", "hors cadence",
    "en autonome", "recherche ciblee", "prochain passage", "au registre",
    "hypothese de decrue", "tentative n",
]

# --- MARQUEURS D'ÉCRITURE IA -----------------------------------------------
# Passage de la skill `humanizer` sur le registre le 08/08/2026 (guide « Signs of AI
# writing » de Wikipédia). Deux tells sont mécaniques, donc contrôlables ici : le tiret
# cadratin, marqueur le plus fiable, et l'emoji décoratif. Un site de sécurité qui sent
# le texte généré perd la confiance qu'il demande au lecteur.
# Le tiret reste légitime dans le frontmatter (séparateur de champ) et dans les intitulés
# de source (on cite une page officielle, on ne la reformule pas) : ces deux zones ne
# passent pas par ce contrôle.
# Ce qui trahit la machine, c'est le tiret PONCTUANT, entouré d'espaces. Le tiret collé
# entre deux mots relève de la typographie normale et appartient souvent à un nom propre
# sourcé (« PR-A 370 Turre–El Jalí ») : le remplacer déformerait un fait. D'où l'espace
# exigée d'un côté au moins.
TIRETS_LONGS = re.compile(r"\s[—–]|[—–]\s")


def emojis(txt: str) -> list:
    return [c for c in txt
            if ord(c) > 0x2100 and unicodedata.category(c) in ("So", "Sk")]


# Une alerte ROUGE ne peut pas rester adossée à une hypothèse non tranchée
# indéfiniment : passé ce délai, soit on dégrade en MOYENNE, soit on écrit
# explicitement au lecteur que le texte n'est pas publié (et on cesse de le
# présenter comme « probable »).
HYPO_MARQUEURS = ["a confirmer", "probable", "non localise", "non trouve",
                  "en cours de recoupement", "reste a faire", "a recouper"]
HYPO_DELAI_JOURS = 14   # deux semaines de recherches infructueuses = un fait à publier

# Garde-fou anti-corruption du registre (incident 2026-07-25 : un run a réécrit
# alertes-actives.md en version condensée, 125 Ko → 27 Ko, perdant tout le détail).
# Depuis l'éclatement en un fichier par alerte, le contrôle se fait fichier par fichier :
# il attrape aussi la corruption d'UNE seule alerte, invisible dans l'ancienne masse.
ALERTES_REL = "livrables/alertes"          # chemin relatif au dépôt (pour git)
MONOLITHE_REL = "livrables/alertes-actives.md"   # ancien registre, ne doit plus renaître
MAX_TOTAL_SHRINK = 0.25    # perte de texte tolérée sur l'ensemble du registre
MAX_FILE_SHRINK = 0.45     # perte tolérée sur une alerte prise isolément
MIN_ALERTE_CHARS = 250     # plancher absolu par alerte si git est indisponible


def _repo():
    return str(HERE.parent)


def _git(*args):
    """Exécute une commande git ; None si git indisponible ou en échec."""
    try:
        r = subprocess.run(["git", "-C", _repo(), *args],
                           capture_output=True, text=True, timeout=30)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def _tailles_courantes():
    return {p.name: len(p.read_text(encoding="utf-8"))
            for p in ALERTES_DIR.glob("*.md") if p.name.lower() != "readme.md"}


def _tailles_precedentes(courantes):
    """Tailles des fichiers d'alerte au dernier commit où le dossier DIFFÈRE de l'état
    courant. None si git est indisponible (build hors dépôt, 1er run)."""
    log = _git("log", "--format=%H", "--", ALERTES_REL)
    if log is None:
        return None
    for sha in log.split():
        arbre = _git("ls-tree", "-r", "-l", sha, "--", ALERTES_REL)
        if arbre is None:
            continue
        tailles = {}
        for ligne in arbre.splitlines():
            meta, _, chemin = ligne.partition("\t")
            nom = chemin.rsplit("/", 1)[-1]
            if nom.lower() == "readme.md" or not nom.endswith(".md"):
                continue
            champs = meta.split()
            if len(champs) >= 4 and champs[3].isdigit():
                tailles[nom] = int(champs[3])       # taille en octets (≈ caractères)
        if tailles and tailles != courantes:
            return tailles
    return None


def registry_integrity_errors():
    """Bloque le build si le registre s'effondre : dossier absent, alerte disparue,
    texte global ou texte d'une alerte qui fond anormalement en un seul run."""
    errs = []
    if (LIVRABLES / "alertes-actives.md").exists():
        errs.append(
            f"[intégrité] l'ancien registre monolithique {MONOLITHE_REL} est réapparu — "
            f"le registre vit désormais dans {ALERTES_REL}/ (un fichier par alerte). "
            f"Reporter son contenu dans les fichiers concernés puis le supprimer.")
    if not ALERTES_DIR.is_dir():
        errs.append(f"[intégrité] dossier {ALERTES_REL}/ introuvable — registre perdu.")
        return errs

    cur = _tailles_courantes()
    if not cur:
        errs.append(f"[intégrité] aucune alerte dans {ALERTES_REL}/ — registre vidé.")
        return errs
    for nom, taille in sorted(cur.items()):
        if taille < MIN_ALERTE_CHARS:
            errs.append(f"[intégrité] alerte quasi vide ({taille} car.) : {nom} — "
                        f"fichier tronqué ou écrasé.")

    prev = _tailles_precedentes(cur)
    if prev is None:
        return errs                      # pas d'historique : contrôles absolus seulement

    disparus = sorted(set(prev) - set(cur))
    if disparus:
        errs.append(
            f"[intégrité] {len(disparus)} alerte(s) SUPPRIMÉE(S) du registre : "
            f"{', '.join(disparus[:5])}{'…' if len(disparus) > 5 else ''} — une alerte ne "
            f"se supprime jamais, elle se clôture (Statut « [CLÔTURÉ] (date) »). "
            f"Restaurer depuis git : git checkout <sha> -- {ALERTES_REL}/<fichier>")

    for nom in sorted(set(prev) & set(cur)):
        if prev[nom] and cur[nom] < prev[nom] * (1 - MAX_FILE_SHRINK):
            pct = round((1 - cur[nom] / prev[nom]) * 100)
            errs.append(
                f"[intégrité] l'alerte {nom} a perdu {pct}% de son texte "
                f"({prev[nom]}→{cur[nom]} car.) — réécriture condensée probable. "
                f"Restaurer ce fichier depuis git puis n'y appliquer que la mise à jour "
                f"réelle du jour.")

    tot_prev, tot_cur = sum(prev.values()), sum(cur.values())
    if tot_prev and tot_cur < tot_prev * (1 - MAX_TOTAL_SHRINK):
        pct = round((1 - tot_cur / tot_prev) * 100)
        errs.append(
            f"[intégrité] le registre a perdu {pct}% de son texte en un run "
            f"({tot_prev}→{tot_cur} caractères) — corruption probable. Restaurer le "
            f"dossier depuis git puis ne réappliquer que les nouveautés du jour. "
            f"NE PAS PUBLIER en l'état.")
    return errs


def _age_jours(champ_date: str):
    """Âge en jours d'un champ `detection:`/`verif:` (None si non datable)."""
    m = re.match(r"(\d{4}-\d{2}-\d{2})", (champ_date or "").strip())
    if not m:
        return None
    return (date.today() - date.fromisoformat(m.group(1))).days


def ton_warnings(cards) -> list:
    """Même contrôle de ton, appliqué à « Zone (détails) » — AVERTISSEMENT seulement.
    Ce champ porte le narratif historique de 30+ fiches héritées : on ne le réécrit pas
    en masse (c'est exactement le geste qui a corrompu le registre le 25/07), on le
    nettoie fiche par fiche au fil des mises à jour. Le compteur doit décroître."""
    out = []
    for c in cards:
        plie = fold_txt(c["zone"])
        hits = sorted({f.strip() for f in JARGON_INTERNE if f in plie})
        n_tirets = len(TIRETS_LONGS.findall(c["zone"]))
        if n_tirets:
            hits.append(f"{n_tirets} tiret(s) cadratin(s)")
        if emojis(c["zone"]):
            hits.append("emoji")
        if hits:
            out.append(f"{c['cle'][:55]} → {', '.join(hits)}")
    return out


def qa_check(cards, page: str, bivouac=None):
    """Valide le rendu AVANT publication. Toute violation = build en échec (exit 2).
    C'est la boucle demandée : build → QA → correction → rebuild jusqu'à 0 violation."""
    errs = []
    for c in cards:
        ref = c["cle"][:60]
        for b in itin_badges(c):
            if not b or b == "—":
                errs.append(f"[badge] vide pour {ref}")
            if any(f in b for f in BADGE_INTERDITS):
                errs.append(f"[badge] fragment interdit « {b} » pour {ref}")
            if len(b) > 24:
                errs.append(f"[badge] trop long ({len(b)}) « {b} » pour {ref}")
        if not c["portion"].strip():
            errs.append(f"[portion] vide pour {ref}")
        if not c["alternative"].strip():
            errs.append(f"[alternative] vide pour {ref}")
        for champ in ("portion", "alternative"):
            if "OMW" in c[champ] or "OnMyWay" in c[champ]:
                errs.append(f"[{champ}] mention OMW pour {ref}")
            plie = fold_txt(c[champ])
            for frag in JARGON_INTERNE:
                if frag in plie:
                    errs.append(
                        f"[ton] jargon de veille « {frag.strip()} » dans {champ} pour {ref} : "
                        f"ce champ s'adresse au randonneur, décrire l'état ACTUEL du terrain "
                        f"et pas le déroulé de la veille (l'historique va en « Zone (détails) »)")
            if TIRETS_LONGS.search(c[champ]):
                errs.append(
                    f"[ton] tiret cadratin dans {champ} pour {ref} : c'est le marqueur "
                    f"d'écriture IA le plus reconnaissable. Un point, une virgule, "
                    f"deux-points ou des parenthèses font le travail.")
            if emojis(c[champ]):
                errs.append(
                    f"[ton] emoji « {''.join(emojis(c[champ])[:3])} » dans {champ} pour "
                    f"{ref} : la gravité est déjà portée par le champ `sev:` et par la "
                    f"couleur de la carte.")
        closed_c = "CLÔTURÉ" in c["statut"].upper()
        if sev_class(c["sev"]) == "haute" and not closed_c:
            plie = fold_txt(c["portion"])
            marq = next((m for m in HYPO_MARQUEURS if m in plie), None)
            age = _age_jours(c["detection"])
            if marq and age is not None and age > HYPO_DELAI_JOURS:
                errs.append(
                    f"[hypothèse] alerte rouge encore adossée à « {marq} » {age} jours après "
                    f"détection pour {ref} — soit la source est trouvée et l'alerte est "
                    f"confirmée, soit on dégrade en MOYENNE et on écrit noir sur blanc au "
                    f"lecteur ce qui n'est PAS publié (ex. « aucun arrêté publié à ce jour "
                    f"sur le site de la préfecture »)")
        if categorize(c) is None:
            errs.append(f"[catégorie] type orphelin « {c['type']} » pour {ref} — "
                        "ajouter la catégorie ou le mot-clé dans referentiel/categories.json")
    if "OMW" in page or "OnMyWay" in page:
        errs.append("[page] mention OMW/OnMyWay dans le HTML")
    if "**" in page:
        errs.append("[page] markdown gras non rendu (** résiduel)")
    if "\\|" in page:
        errs.append("[page] pipe échappé résiduel (\\|)")
    if "[[" in page or "]]" in page:
        errs.append("[page] wikilien résiduel ([[…]])")
    n_details = page.count("<details>")
    if n_details != len(cards):
        errs.append(f"[structure] {n_details} volets <details> pour {len(cards)} cartes "
                    f"(attendu {len(cards)})")
    n_biv = len(bivouac or [])
    if page.count('class="meta sources"') != len(cards) + n_biv:
        errs.append("[structure] ligne Sources manquante sur au moins une carte/fiche")
    if page.count('class="meta dates"') != len(cards) + n_biv:
        errs.append("[structure] ligne validité/dates manquante sur au moins une carte/fiche")
    if 'id="q"' not in page or 'id="noresult"' not in page:
        errs.append("[structure] recherche sentier absente")
    if UMAMI_WEBSITE_ID and UMAMI_WEBSITE_ID not in page:
        errs.append("[analytics] website ID configuré mais script absent de la page")
    if page.count("<title>") != 1:
        errs.append("[structure] balise <title> manquante ou dupliquée")
    for b in (bivouac or []):
        ref = f"bivouac:{b['nom'][:40]}"
        if b["regle"] not in REGLE_META:
            errs.append(f"[bivouac] règle inconnue « {b['regle']} » pour {ref}")
        if not b["source_url"].strip():
            errs.append(f"[bivouac] source manquante pour {ref}")
        if not b["conditions"].strip():
            errs.append(f"[bivouac] conditions vides pour {ref}")
        if b["statut"].upper() not in ("FAIT", "HYPOTHESE", "HYPOTHÈSE"):
            errs.append(f"[bivouac] statut invalide « {b['statut']} » pour {ref}")
    return errs


def build():
    if not LIVRABLES.is_dir():
        print(f"introuvable : {LIVRABLES}", file=sys.stderr)
        return 1

    digests = sorted(LIVRABLES.glob("digest_*.md"), reverse=True)

    bivouac = load_bivouac()
    cards = load_alertes()
    actives = [c for c in cards if "CLÔTURÉ" not in c["statut"].upper()]
    closes = [c for c in cards if "CLÔTURÉ" in c["statut"].upper()]
    hautes = [c for c in actives if sev_class(c["sev"]) == "haute"]

    # --- vue Carte : zones-sources touchées par une alerte active -----------
    zones_coords = load_zones_coords()
    zones_liste, zones_non_mappees = zones_carte(actives, zones_coords)
    if zones_non_mappees:
        print(f"⚠ carte : {len(zones_non_mappees)} alerte(s) active(s) dont la zone n'est "
              f"pas mappable vers referentiel/zones-coords.csv (aucun marqueur — enrichir "
              f"le CSV ou la table ALIAS_ZONE) :", file=sys.stderr)
        for zone_str, cle in zones_non_mappees[:20]:
            print(f"  ~ zone « {zone_str} » (clé {cle[:60]})", file=sys.stderr)
    zones_json = (json.dumps(zones_liste, ensure_ascii=False)
                  .replace("<", "\\u003c").replace("]]", "] ]"))
    n_marqueurs = len(zones_liste)

    order = {"haute": 0, "moyenne": 1, "info": 2}
    actives.sort(key=lambda c: order.get(sev_class(c["sev"]), 3))

    cards_html = "\n".join(render_card(c) for c in actives)
    closed_html = "\n".join(render_card(c) for c in closes)

    # filtres catégories (générés depuis la donnée : seules les catégories peuplées)
    counts = {}
    for c in actives + closes:
        cat = categorize(c)
        if cat:
            counts[cat["slug"]] = counts.get(cat["slug"], 0) + 1
    # aria-pressed plutôt qu'une classe : l'état d'un filtre n'était porté que par la
    # couleur, invisible pour un lecteur d'écran comme pour un daltonien.
    cats_html = (f'<button type="button" class="cat" data-cat="" aria-pressed="true">Toutes '
                 f'<span>{len(actives) + len(closes)}</span></button>')
    for cat in CATEGORIES:
        n = counts.get(cat["slug"], 0)
        if n:
            cats_html += (f'<button type="button" class="cat" data-cat="{cat["slug"]}" '
                          f'aria-pressed="false">'
                          f'{html.escape(cat["label"])} <span>{n}</span></button>')
    # Les sections annexes du registre (Items mineurs, À vérifier manuellement, Pistes
    # abandonnées, Notes) sont la MÉMOIRE INTERNE de l'agent : jamais rendues sur le site.

    if digests:
        latest_iso = digests[0].stem.replace("digest_", "")
    else:
        verifs = [c["verif"][:10] for c in cards
                  if re.match(r"^\d{4}-\d{2}-\d{2}", c["verif"])]
        latest_iso = max(verifs) if verifs else date.today().isoformat()
    nav_items, sections = [], []
    for p in digests:
        iso = p.stem.replace("digest_", "")
        label = fr_date(iso, court=True)
        nav_items.append(f'<button class="navlink" data-view="d-{iso}">{label}<span class="yr">{iso[:4]}</span></button>')
        body = md_to_html(p.read_text(encoding="utf-8"))
        sections.append(f"""<section id="d-{iso}" class="view digest" hidden>
<p class="eyebrow">Rapport quotidien</p>
<h2 class="digest-title">{fr_date(iso)}</h2>
{body}
</section>""")

    bivouac_section = ""
    if bivouac:
        bcards = "\n".join(render_bivouac_card(b) for b in bivouac)
        bcounts = {}
        for b in bivouac:
            bcounts[b["regle"]] = bcounts.get(b["regle"], 0) + 1
        bchips = (f'<button type="button" class="cat bcat" data-regle="" aria-pressed="true">'
                  f'Toutes <span>{len(bivouac)}</span></button>')
        for slug, (label, _c) in REGLE_META.items():
            n = bcounts.get(slug, 0)
            if n:
                bchips += (f'<button type="button" class="cat bcat" data-regle="{slug}" '
                           f'aria-pressed="false">{html.escape(label)} '
                           f'<span>{n}</span></button>')
        bivouac_section = f"""<section id="bivouac" class="view" hidden>
  <p class="eyebrow">Base de référence · {len(bivouac)} espaces &amp; règles</p>
  <h2 class="reg-title">Bivouac &amp; réglementation</h2>
  <p class="disclaimer">Les règles évoluent par arrêté : vérifiez toujours la source officielle avant de partir.
  Une alerte active peut temporairement durcir une règle (voir l'onglet Alertes).</p>
  <div class="cats" role="group" aria-label="Filtrer par règle">{bchips}</div>
  <div class="cards">
  {bcards}
  </div>
  <p id="bnoresult" class="noresult" hidden>Aucune fiche pour cette recherche.</p>
</section>"""

    built = datetime.now().strftime("%d/%m/%Y %H:%M")
    n_dig = len(digests)

    analytics = (f'<script defer src="https://cloud.umami.is/script.js" '
                 f'data-website-id="{UMAMI_WEBSITE_ID}"></script>' if UMAMI_WEBSITE_ID else "")

    # Description et Open Graph : c'est par là qu'arrive un randonneur qui cherche
    # « GR20 fermé » sur un moteur, et c'est ce que voit un forum où l'on colle le lien.
    # Les compteurs sont dans le texte : ils datent la page dans les résultats.
    meta_desc = (f"{len(actives)} alertes actives dont {len(hautes)} rouges sur les GR®, "
                 f"les chemins de Compostelle et les grands itinéraires d'Europe. "
                 f"Fermetures, déviations et réglementations, datées et sourcées, "
                 f"mises à jour le {fr_date(latest_iso)}.")
    meta_desc = html.escape(meta_desc, quote=True)
    og_title = "Alertes-Rando.info, l'état des sentiers d'Europe au jour le jour"

    # --- Carte : bouton de nav, section, CSS et JS (Leaflet à la demande) ----
    # Ces morceaux sont construits hors de la grande f-string de page pour éviter le
    # doublement des accolades CSS/JS : ils y sont interpolés tels quels.
    carte_nav = '<button class="navlink" data-view="carte">Carte</button>'
    marqueurs_txt = ("Aucune zone en alerte active sur la carte." if n_marqueurs == 0
                     else (f"{n_marqueurs} zone en alerte active." if n_marqueurs == 1
                           else f"{n_marqueurs} zones en alerte active."))
    carte_section = f"""<section id="carte" class="view" hidden aria-labelledby="t-carte">
  <p class="eyebrow">Vue géographique</p>
  <h2 class="reg-title" id="t-carte">Carte des alertes</h2>
  <p class="disclaimer">Un repère par zone touchée par au moins une alerte active. La position
  marque le centre indicatif de la zone-source (département, massif ou région), pas le point
  exact de l'incident. Cliquez un repère pour voir les sentiers concernés.</p>
  <div id="carte-map" class="carte-map" role="application"
       aria-label="Carte des zones de sentiers en alerte active"></div>
  <p class="carte-compte" id="carte-compte">{marqueurs_txt}</p>
  <p class="legende">
    <span class="l-haute"><b>Alerte rouge</b> étape bloquée ou interdiction</span>
    <span class="l-moyenne"><b>Orange</b> impact réel, sans blocage</span>
    <span class="l-info"><b>Info</b> bon à savoir avant de partir</span>
  </p>
  <p class="disclaimer">Fond cartographique &copy; les contributeurs
  <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a>.</p>
</section>"""

    carte_css = """
/* --- vue Carte (Leaflet) --- */
.carte-map { height: 55vh; min-height: 320px; width: 100%; z-index: 0;
  border: 1px solid var(--line); border-radius: 8px; margin: var(--s-4) 0 var(--s-3);
  background: var(--panel); }
.leaflet-container { background: var(--panel); font: inherit; }
.carte-compte { font-family: var(--mono); font-size: var(--t-sm); color: var(--ink-2);
  margin: 0 0 var(--s-3); }
.marqueur-zone { display: block; width: 18px; height: 18px; border-radius: 50%;
  border: 2px solid var(--paper); box-shadow: 0 0 0 1px rgba(0, 0, 0, .3); }
.marqueur-zone.m-haute { background: var(--haute); }
.marqueur-zone.m-moyenne { background: var(--moy); }
.marqueur-zone.m-info { background: var(--info); }
.leaflet-popup-content-wrapper, .leaflet-popup-tip { background: var(--paper);
  color: var(--ink); box-shadow: 0 2px 10px rgba(0, 0, 0, .25); }
.leaflet-popup-content { font: var(--t-sm)/1.5 var(--sans); margin: 12px 14px; color: var(--ink); }
.leaflet-popup-content a { color: var(--pine); }
.carte-pop h4 { margin: 0 0 6px; font-size: var(--t-md); font-weight: 700; }
.carte-pop ul { list-style: none; margin: 0 0 8px; padding: 0; }
.carte-pop li { margin: 5px 0; line-height: 1.4; }
.carte-pop .pt-type { font-family: var(--mono); font-size: var(--t-xs); color: var(--ink-2); }
.carte-pop .voir { font-family: var(--mono); font-size: var(--t-xs); text-transform: uppercase;
  letter-spacing: .04em; color: var(--pine); background: none; border: 0; padding: 4px 0;
  cursor: pointer; }
.carte-pop .voir:hover { color: var(--ink); text-decoration: underline; }
.leaflet-bar a { background: var(--paper); color: var(--ink); border-bottom-color: var(--line); }
.leaflet-bar a:hover { background: var(--panel); }
.leaflet-control-attribution { background: var(--paper); color: var(--ink-2); }
.leaflet-control-attribution a { color: var(--pine); }
/* En thème sombre, les tuiles OSM (raster, claires) sont assombries pour rester lisibles. */
:root[data-theme="dark"] .leaflet-tile {
  filter: brightness(.6) invert(1) contrast(.95) hue-rotate(180deg) saturate(.5) brightness(.9); }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .leaflet-tile {
    filter: brightness(.6) invert(1) contrast(.95) hue-rotate(180deg) saturate(.5) brightness(.9); } }
"""

    carte_js = """
  // --- Carte Leaflet : bibliothèque chargée à la 1re ouverture de l'onglet ----------
  var carteFaite = false;
  function chargerLeaflet(cb) {
    if (window.L) { cb(); return; }
    var css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
    css.integrity = 'sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=';
    css.crossOrigin = '';
    document.head.appendChild(css);
    var s = document.createElement('script');
    s.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
    s.integrity = 'sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=';
    s.crossOrigin = '';
    s.onload = cb;
    s.onerror = function () {
      var el = document.getElementById('carte-compte');
      if (el) el.textContent = 'Carte indisponible : la bibliothèque cartographique n\\'a pas pu être chargée.';
    };
    document.head.appendChild(s);
  }
  function pastilleCarte(sev) {
    var lib = { haute: 'Rouge', moyenne: 'Orange', info: 'Info', clos: 'Clôturée' };
    return '<span class="badge sev-' + sev + '">' + (lib[sev] || sev) + '</span>';
  }
  function escapeHtml(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
                    .replace(/"/g, '&quot;');
  }
  function construireCarte() {
    var zones = window.__ZONES || [];
    var map = L.map('carte-map', { scrollWheelZoom: false });
    window.__carteMap = map;
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    var zdec = { haute: 1000, moyenne: 500, info: 0, clos: 0 };
    var pts = [];
    zones.forEach(function (z) {
      var icon = L.divIcon({
        className: '',
        html: '<span class="marqueur-zone m-' + (z.sevMax || 'info') + '"></span>',
        iconSize: [18, 18], iconAnchor: [9, 9], popupAnchor: [0, -9]
      });
      var m = L.marker([z.lat, z.lon], {
        icon: icon, zIndexOffset: zdec[z.sevMax] || 0, title: z.nom, alt: z.nom
      }).addTo(map);
      var h = '<div class="carte-pop"><h4>' + escapeHtml(z.nom) + '</h4><ul>';
      z.alertes.forEach(function (a) {
        h += '<li>' + pastilleCarte(a.sev) + ' <strong>' + escapeHtml(a.itin.join(', '))
           + '</strong> <span class="pt-type">' + escapeHtml(a.type) + '</span></li>';
      });
      h += '</ul><button type="button" class="voir" data-q="' + escapeHtml(z.q || '')
         + '">Voir dans les alertes &rarr;</button></div>';
      m.bindPopup(h);
      pts.push([z.lat, z.lon]);
    });
    if (pts.length) { map.fitBounds(pts, { padding: [30, 30], maxZoom: 6 }); }
    else { map.setView([46, 6], 4); }
    // clic « Voir dans les alertes » dans une popup → bascule vers le registre + recherche
    document.getElementById('carte-map').addEventListener('click', function (e) {
      var b = e.target.closest && e.target.closest('.voir');
      if (!b) return;
      var q = document.getElementById('q');
      if (q) q.value = b.getAttribute('data-q') || '';
      if (window.__show) window.__show('registre', true);
      if (q) q.dispatchEvent(new Event('input'));
      window.scrollTo({ top: 0 });
    });
  }
  window.__initCarte = function () {
    if (carteFaite) { if (window.__carteMap) window.__carteMap.invalidateSize(); return; }
    carteFaite = true;
    chargerLeaflet(function () {
      construireCarte();
      setTimeout(function () { if (window.__carteMap) window.__carteMap.invalidateSize(); }, 60);
    });
  };
"""

    page = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="https://www.alertes-rando.info/">
<title>Alertes Rando</title>
<meta name="description" content="{meta_desc}">
<meta name="theme-color" content="#20261f" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1a1e1a" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Alertes-Rando.info">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://www.alertes-rando.info/">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary">
<link rel="preload" href="fonts/Roboto-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/RobotoMono-var.woff2" as="font" type="font/woff2" crossorigin>
{analytics}
<style>
@font-face {{ font-family: "Roboto"; src: url(fonts/Roboto-var.woff2) format("woff2");
  font-weight: 100 900; font-display: swap; }}
@font-face {{ font-family: "Roboto Mono"; src: url(fonts/RobotoMono-var.woff2) format("woff2");
  font-weight: 100 700; font-display: swap; }}
:root, :root[data-theme="light"] {{
  color-scheme: light;{PALETTE_CLAIR}
  --sans: "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  --mono: "Roboto Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  /* échelle typo : 7 crans au lieu de 26 tailles voisines */
  --t-xs: .6875rem; --t-sm: .8125rem; --t-md: .9375rem; --t-base: 1rem;
  --t-lg: 1.125rem; --t-xl: 1.5rem; --t-2xl: 2.25rem;
  /* espacement : grille de 4 */
  --s-1: 4px; --s-2: 8px; --s-3: 12px; --s-4: 16px; --s-5: 24px;
  --s-6: 32px; --s-7: 48px; --s-8: 64px;
  --rythme: 160ms cubic-bezier(.2, 0, .2, 1);
  /* posé sur --surface-invert, qui est sombre dans les deux thèmes */
  --on-invert-2: #a9ada1;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{ color-scheme: dark;{PALETTE_SOMBRE} }}
}}
:root[data-theme="dark"] {{ color-scheme: dark;{PALETTE_SOMBRE} }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--paper); color: var(--ink);
  font: 16px/1.55 var(--sans); }}
a {{ color: var(--pine); }}
code {{ font-family: var(--mono); font-size: .85em; background: var(--panel);
  padding: 1px 5px; border-radius: 4px; }}
del {{ color: var(--ink-2); }}
/* 1080 et non 1180 : c'est ici que se règle la longueur de ligne. À 1180, la
   colonne principale faisait 860px et une ligne d'alerte dépassait 90 caractères,
   au-delà du confortable. Resserrer le conteneur tient la mesure autour de 82
   caractères sans avoir à brider le texte à l'intérieur des cartes. */
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 0 20px 60px; }}

.skip {{ position: absolute; left: -9999px; top: 0; z-index: 10; background: var(--pine);
  color: var(--on-accent); font-family: var(--mono); font-size: var(--t-sm);
  padding: var(--s-3) var(--s-4); border-radius: 0 0 8px 0; }}
.skip:focus {{ left: 0; }}
main:focus {{ outline: none; }}
.sr-only {{ position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }}

.topnav {{ background: var(--surface-invert); }}
.topnav .nav-in {{ max-width: 1080px; margin: 0 auto; padding: 0 20px; display: flex;
  justify-content: space-between; align-items: stretch; gap: var(--s-5); overflow-x: auto; }}
.topnav .navlink {{ display: inline-flex; align-items: center; padding: var(--s-3) 0;
  min-height: 44px; border-left: 0; border-radius: 0;
  border-bottom: 2px solid transparent; white-space: nowrap; color: var(--on-invert-2); }}
.topnav .navlink:hover {{ background: none; color: var(--on-invert); }}
.topnav .navlink.active {{ color: var(--on-invert); border-bottom-color: var(--haute); background: none; }}
.topnav .navlink:focus-visible {{ outline: 2px solid var(--on-invert); outline-offset: -2px; }}
.theme-btn {{ margin-left: auto; align-self: center; display: inline-flex; align-items: center;
  justify-content: center; min-width: 44px; min-height: 44px; padding: 0 var(--s-2);
  background: none; border: 0; cursor: pointer; color: var(--on-invert-2);
  font-family: var(--mono); font-size: var(--t-xs); text-transform: uppercase;
  letter-spacing: .06em; transition: color var(--rythme); }}
.theme-btn:hover {{ color: var(--on-invert); }}
.theme-btn:focus-visible {{ outline: 2px solid var(--on-invert); outline-offset: -2px; }}
.theme-btn svg {{ width: 17px; height: 17px; fill: none; stroke: currentColor;
  stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }}

nav.rail {{ position: sticky; top: 16px; align-self: start; display: flex;
  flex-direction: column; gap: 3px; max-height: calc(100vh - 40px); overflow: auto; }}
.rail-label {{ font-family: var(--mono); font-weight: 700; font-size: .64rem;
  text-transform: uppercase; letter-spacing: .06em; color: var(--ink-2);
  margin: 16px 0 5px; padding-left: 13px; }}
.navlink {{ display: flex; justify-content: space-between; align-items: center;
  gap: var(--s-2); text-align: left; border: 0; background: none; cursor: pointer;
  font-family: var(--mono); font-size: var(--t-sm); letter-spacing: .02em;
  text-transform: uppercase; color: var(--ink-2); padding: var(--s-3);
  min-height: 44px; border-left: 3px solid transparent; border-radius: 0 6px 6px 0;
  transition: color var(--rythme), background-color var(--rythme),
              border-color var(--rythme); }}
.navlink:hover {{ color: var(--ink); background: var(--panel); }}
.navlink.active {{ color: var(--ink); font-weight: 500; border-left-color: var(--haute); }}
.navlink .yr {{ font-size: var(--t-xs); color: var(--ink-2); }}
.navlink:focus-visible {{ outline: 2px solid var(--pine); outline-offset: 1px; }}

header.mast {{ display: flex; align-items: flex-end; gap: 24px; flex-wrap: wrap;
  padding: 20px 0; }}
h1 {{ font-family: var(--sans); font-weight: 700; font-size: clamp(2.3rem, 6.5vw, 4rem);
  letter-spacing: -.055em; margin: 0; line-height: 1.02; text-wrap: balance; }}
/* Le mono va bien aux dates, aux compteurs et aux étiquettes. Sur six lignes de
   prose, il ralentit la lecture : l'accroche repasse en sans. */
.tagline {{ margin: var(--s-3) 0 0; color: var(--ink); font-family: var(--sans);
  font-weight: 400; font-size: var(--t-lg); line-height: 1.5; max-width: 62ch; }}
.mast-stats {{ margin-left: auto; display: flex; gap: var(--s-5); }}
.stat {{ text-align: right; }}
.stat b {{ display: block; font-family: var(--mono); font-weight: 700; font-size: var(--t-2xl);
  letter-spacing: -.03em; font-variant-numeric: tabular-nums; line-height: 1.05; }}
.stat.warn b {{ color: var(--haute); }}
.stat span {{ font-family: var(--mono); font-size: var(--t-xs); text-transform: uppercase;
  color: var(--ink-2); }}

/* 248px et non 220 : la recherche est passée à 16px (zoom iOS) et son texte
   d'invite ne tenait plus dans la colonne. */
.layout {{ display: grid; grid-template-columns: 248px 1fr; gap: var(--s-6); padding-top: var(--s-5); }}
main {{ min-width: 0; }}
.view > :first-child {{ margin-top: 0; }}
.eyebrow {{ font-family: var(--mono); font-size: .66rem; text-transform: uppercase;
  letter-spacing: .06em; color: var(--pine); margin: 0 0 4px; font-weight: 700; }}
h2.digest-title, h2.reg-title {{ font-family: var(--sans); font-weight: 800;
  letter-spacing: -.03em; font-size: 1.7rem; margin: 0 0 14px; text-wrap: balance; }}
.digest h2, .view h2 {{ font-family: var(--sans); font-weight: 800; letter-spacing: -.02em; }}
.digest > p, .digest li, .annexes p, .annexes li {{ max-width: 74ch; }}
.digest h3 {{ font-size: 1.06rem; margin: 26px 0 8px; padding-left: 10px;
  border-left: 4px solid var(--line); line-height: 1.35; }}
.digest h3.sev-haute {{ border-left-color: var(--haute); }}
.digest h3.sev-moyenne {{ border-left-color: var(--moy); }}
blockquote {{ margin: 12px 0; padding: 8px 14px; background: var(--panel);
  border-radius: 6px; color: var(--ink-2); font-size: .92rem; }}
blockquote p {{ margin: 0; }}
hr {{ border: none; border-top: 1px solid var(--line); margin: 22px 0; }}
.table-wrap {{ overflow-x: auto; margin: 14px 0; border: 1px solid var(--line); border-radius: 8px; }}
table {{ border-collapse: collapse; font-size: .85rem; min-width: 700px; }}
th, td {{ padding: 7px 10px; border-bottom: 1px solid var(--line);
  text-align: left; vertical-align: top; }}
th {{ background: var(--panel); font-size: .74rem; text-transform: uppercase; letter-spacing: .05em; }}

.tag {{ display: inline-block; font-size: .66rem; font-weight: 700; letter-spacing: .05em;
  padding: 1px 6px; border-radius: 4px; vertical-align: 1px; }}
.tag.fait {{ background: var(--pine-soft); color: var(--pine); }}
.tag.hypo {{ background: var(--moy-bg); color: var(--moy); }}
.tag.verif {{ background: var(--info-bg); color: var(--info); }}
.tag.clos {{ background: var(--clos-bg); color: var(--clos); }}

.rail .search {{ margin: 0 0 var(--s-3); }}
/* 16px obligatoire : en dessous, Safari iOS zoome à la prise de focus et ne
   revient pas. C'est le geste principal du site, sur son appareil principal. */
.search input {{ width: 100%; font-family: var(--mono); font-size: 16px; color: var(--ink);
  background: none; border: 1.5px solid var(--ink); border-radius: 8px;
  min-height: 44px; padding: var(--s-2) var(--s-3);
  transition: border-color var(--rythme), box-shadow var(--rythme); }}
.search input:focus {{ outline: none; border-color: var(--pine);
  box-shadow: 0 0 0 3px var(--pine-soft); }}
.search input::placeholder {{ color: var(--ink-2); }}
.noresult {{ color: var(--ink-2); font-style: italic; }}
.cats {{ display: flex; flex-wrap: wrap; gap: var(--s-2); margin: var(--s-3) 0 var(--s-1); }}
.cat {{ display: inline-flex; align-items: center; gap: var(--s-1);
  font-family: var(--mono); font-size: var(--t-sm); color: var(--ink); background: var(--paper);
  border: 1px solid var(--ink); border-radius: 999px; padding: var(--s-2) var(--s-4);
  min-height: 44px; cursor: pointer;
  transition: color var(--rythme), background-color var(--rythme), border-color var(--rythme); }}
.cat span {{ color: inherit; opacity: .7; font-size: var(--t-xs); font-variant-numeric: tabular-nums; }}
.cat:hover {{ border-color: var(--pine); color: var(--pine); }}
.cat[aria-pressed="true"] {{ background: var(--pine); border-color: var(--pine); color: var(--on-accent); }}
.cat[aria-pressed="true"] span {{ color: var(--on-accent); opacity: .85; }}
.cat:focus-visible {{ outline: 2px solid var(--pine); outline-offset: 1px; }}

/* Légende de gravité : elle n'existait que dans l'attribut title des 71 pastilles,
   donc invisible au tactile et au clavier. C'était la clé de lecture du site. */
.legende {{ display: flex; flex-wrap: wrap; gap: var(--s-2) var(--s-4);
  margin: var(--s-3) 0 var(--s-5); padding: var(--s-3) var(--s-4);
  background: var(--panel); border-radius: 8px;
  font-size: var(--t-sm); color: var(--ink-2); }}
.legende b {{ font-family: var(--mono); font-size: var(--t-xs); font-weight: 700;
  text-transform: uppercase; letter-spacing: .05em; padding: 2px 7px;
  border-radius: 5px; margin-right: var(--s-1); }}
.legende .l-haute b {{ background: var(--haute-bg); color: var(--haute); }}
.legende .l-moyenne b {{ background: var(--moy-bg); color: var(--moy); }}
.legende .l-info b {{ background: var(--info-bg); color: var(--info); }}
.legende > span {{ display: inline-flex; align-items: baseline; }}
.about p {{ max-width: none; font-size: .97rem; line-height: 1.6; }}
.about p.disclaimer {{ margin-top: 22px; }}

.contact {{ margin-top: 36px; padding-top: 22px; border-top: 1.5px solid var(--ink); }}
.contact form {{ display: grid; gap: 14px; max-width: 640px; margin-top: 14px; }}
.contact label {{ display: block; margin-bottom: 5px; font-family: var(--mono);
  font-size: .68rem; text-transform: uppercase; letter-spacing: .06em; color: var(--ink-2); }}
.contact input, .contact textarea {{ width: 100%; font: inherit; font-size: .92rem;
  color: var(--ink); background: var(--paper); border: 1.5px solid var(--ink);
  border-radius: 8px; padding: 9px 12px; }}
.contact textarea {{ min-height: 150px; resize: vertical; }}
.contact input:focus, .contact textarea:focus {{ outline: none; border-color: var(--pine);
  box-shadow: 0 0 0 3px var(--pine-soft); }}
.contact button {{ justify-self: start; font-family: var(--mono); font-size: .76rem;
  text-transform: uppercase; letter-spacing: .06em; color: var(--paper);
  background: var(--pine); border: 0; border-radius: 8px; padding: 11px 24px; cursor: pointer; }}
.contact button:hover {{ background: var(--ink); }}
.contact button:focus-visible {{ outline: 2px solid var(--pine); outline-offset: 2px; }}
.contact .hp {{ position: absolute; left: -9999px; width: 1px; height: 1px; }}
.contact .note {{ font-size: .84rem; color: var(--ink-2); max-width: 70ch; }}
.contact .statut {{ font-family: var(--mono); font-size: .8rem; line-height: 1.5;
  padding: 10px 14px; border-radius: 8px; margin: 0; }}
.contact .statut.ok {{ background: var(--pine-soft); color: var(--pine); }}
.contact .statut.ko {{ background: var(--haute-bg); color: var(--haute); }}
.footlink {{ font: inherit; color: var(--pine); background: none; border: 0;
  display: inline-flex; align-items: center; min-height: 44px; padding: 0 var(--s-2);
  text-decoration: underline; cursor: pointer; transition: color var(--rythme); }}
.footlink:hover {{ color: var(--ink); }}
.footlink:focus-visible {{ outline: 2px solid var(--pine); outline-offset: 2px; }}
.cards {{ display: flex; flex-direction: column; gap: var(--s-4); margin: var(--s-5) 0 var(--s-6); }}
.card {{ border: 1px solid var(--clos); border-left-width: 5px;
  border-radius: 8px; padding: var(--s-4); background: var(--paper); }}
.card.haute {{ border-color: var(--haute); }}
.card.moyenne {{ border-color: var(--moy); }}
.card.info {{ border-color: var(--info); }}
/* Pas d'opacity sur une carte clôturée : elle rabotait le contraste de tout ce
   qu'elle contenait, pastille comprise (2.1:1 mesuré). L'atténuation passe par la
   bordure et le fond, qui ne touchent pas au texte. */
.card.clos {{ border-color: var(--line); background: var(--clos-bg); }}
.card.ok {{ border-color: var(--pine); }}
h3.card-top {{ font-size: inherit; font-weight: inherit; line-height: inherit; }}
h3.bname {{ font-size: var(--t-lg); font-weight: 700; margin: 0 0 var(--s-2); }}
.badge.sev-ok {{ background: var(--pine-soft); color: var(--pine); }}
.bname {{ margin: 0 0 6px; font-size: 1.02rem; }}
.disclaimer {{ color: var(--ink-2); font-size: .85rem; font-style: italic; max-width: 80ch; }}
.card-top {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 8px; }}
.badge {{ font-family: var(--mono); font-size: .69rem; font-weight: 700;
  padding: 3px 8px; border-radius: 5px; }}
.badge.itin {{ background: var(--ink); color: var(--paper); }}
.badge.sev-haute {{ background: var(--haute-bg); color: var(--haute); }}
.badge.sev-moyenne {{ background: var(--moy-bg); color: var(--moy); }}
.badge.sev-info {{ background: var(--info-bg); color: var(--info); }}
.badge.sev-clos {{ background: var(--clos-bg); color: var(--clos); }}
.chip.changed {{ font-family: var(--mono); font-size: .69rem; font-weight: 600;
  color: var(--pine); background: var(--pine-soft); padding: 3px 8px; border-radius: 5px; }}
.card .type {{ font-family: var(--mono); color: var(--ink-2); font-size: var(--t-sm); }}
/* Pas de max-width sur le contenu d'une carte : la carte est un cadre fermé, du
   texte qui s'arrête 160px avant sa bordure se lit comme un défaut de rendu — et
   le bloc Alternative, qui a un fond, laissait carrément une boîte inachevée.
   La longueur de ligne est tenue par la largeur de la colonne (voir .wrap), pas
   en rognant le texte à l'intérieur du cadre. */
.card .portion {{ margin: 0 0 var(--s-3); font-size: var(--t-base); letter-spacing: .01em;
  line-height: 1.55; }}
.card .alt {{ margin: 0 0 var(--s-3); font-size: var(--t-md);
  padding: var(--s-2) var(--s-3); background: var(--pine-soft); color: var(--ink); border-radius: 6px; }}
.card .alt a {{ color: var(--pine); }}
.card .alt-label {{ display: inline-block; font-family: var(--mono); font-size: .64rem;
  font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: var(--pine);
  margin-right: 8px; vertical-align: 1px; }}
.card.clos .alt {{ background: var(--clos-bg); color: var(--ink); }}
.card.clos .alt a {{ color: var(--pine); }}
.card.clos .alt-label {{ color: var(--clos); }}
.card .meta {{ margin: 0; color: var(--ink-2); font-size: var(--t-sm); }}
.card .meta.dates {{ margin-top: var(--s-3); padding-top: var(--s-2); border-top: 1px solid var(--line); }}
.card .meta.sources {{ margin-top: var(--s-1); }}
.card .meta .sep {{ margin: 0 6px; }}
.card details {{ margin-top: var(--s-3); font-size: var(--t-md); }}
.card summary {{ display: inline-flex; align-items: center; min-height: 44px;
  cursor: pointer; color: var(--pine); font-family: var(--mono);
  font-weight: 600; font-size: var(--t-sm); list-style: none;
  transition: color var(--rythme); }}
.card summary:hover {{ color: var(--ink); }}
.card summary::-webkit-details-marker {{ display: none; }}
.card summary::before {{ content: "> "; }}
.card details p {{ margin: var(--s-2) 0 0; }}
.card .key {{ margin: 6px 0 0; }}
.card .key code {{ font-size: .72rem; color: var(--ink-2); background: none; padding: 0; }}
h2.bloc, h3.bloc {{ font-family: var(--sans); font-weight: 800; letter-spacing: -.02em;
  font-size: var(--t-lg); margin: var(--s-6) 0 var(--s-1); }}
.annexes h2 {{ font-size: 1.2rem; margin-top: 34px; }}

footer {{ margin-top: var(--s-7); padding-top: var(--s-4); border-top: 1.5px solid var(--ink);
  color: var(--ink-2); font-family: var(--mono); font-size: var(--t-xs);
  text-transform: uppercase; display: flex; gap: var(--s-2); flex-wrap: wrap;
  justify-content: center; text-align: center; }}

@media (max-width: 760px) {{
  .topnav .nav-in {{ justify-content: flex-start; gap: var(--s-4); padding: 0 var(--s-4); }}
  /* la barre défile horizontalement : sans ça le bouton de thème se retrouve
     hors écran, au bout du défilement */
  .theme-btn {{ position: sticky; right: 0; background: var(--surface-invert);
    box-shadow: -10px 0 10px -6px var(--surface-invert); }}
  .layout {{ display: block; }}
  header.mast {{ padding: var(--s-4) 0 var(--s-2); gap: var(--s-3); }}
  .tagline {{ font-size: var(--t-base); }}
  .mast-stats {{ width: 100%; margin-left: 0; justify-content: flex-start; gap: var(--s-6); }}
  .stat {{ text-align: left; }}
  .stat b {{ font-size: var(--t-xl); }}
  nav.rail {{ position: static; flex-direction: row; align-items: center;
    max-height: none; overflow-x: auto; padding-bottom: var(--s-2); margin-bottom: var(--s-3);
    border-bottom: 1.5px solid var(--ink); }}
  .rail-label {{ display: none; }}
  .rail .search {{ flex: none; width: 210px; margin: 0 var(--s-2) 0 0; }}
  .navlink {{ flex: none; border-left: 0; border-bottom: 2px solid transparent;
    border-radius: 0; white-space: nowrap; }}
  .navlink.active {{ border-bottom-color: var(--haute); }}
  /* Les filtres tenaient sur 7 rangées, soit 244px : la première alerte partait
     à 674px, hors écran sur un petit téléphone. Une rangée qui défile les ramène
     à 44px sans rien retirer. */
  .cats {{ flex-wrap: nowrap; overflow-x: auto; scroll-snap-type: x proximity;
    padding-bottom: var(--s-1); margin-bottom: var(--s-2);
    -webkit-overflow-scrolling: touch; }}
  .cat {{ flex: none; scroll-snap-align: start; }}
  .legende {{ flex-direction: column; gap: var(--s-2); }}
}}
/* Les cibles tactiles passent à 44px partout : sur un écran, l'espace récupéré
   par la rangée de filtres finance largement les 12px ajoutés ici. */
@media (prefers-reduced-motion: no-preference) {{
  .view {{ animation: fade .18s ease; }}
  @keyframes fade {{ from {{ opacity: 0; transform: translateY(3px); }} }}
}}
@media (prefers-reduced-motion: reduce) {{
  * {{ transition-duration: .01ms !important; animation-duration: .01ms !important; }}
}}

/* On prépare son étape chez soi et on marche sans réseau : la page doit sortir
   correctement sur papier, volets ouverts et URL des sources visibles. */
@media print {{
  :root {{ color-scheme: light; }}
  .topnav, nav.rail, .cats, .theme-btn, .skip, .contact, .search {{ display: none !important; }}
  .layout {{ display: block; }}
  body {{ background: #fff; color: #000; font-size: 11pt; }}
  .wrap {{ max-width: none; padding: 0; }}
  .view[hidden] {{ display: none !important; }}
  .card {{ break-inside: avoid; border: 1px solid #999; border-left-width: 4px;
    background: #fff; margin-bottom: 8pt; }}
  .card summary {{ min-height: 0; }}   /* les volets sont ouverts par beforeprint */
  .card .alt {{ background: #f2f2f2; }}
  a {{ color: #000; text-decoration: underline; }}
  .card .meta.sources a::after {{ content: " (" attr(href) ")"; font-size: 8pt;
    word-break: break-all; }}
  footer {{ border-top: 1px solid #000; }}
}}
{carte_css}
</style>
<script>
/* Avant le premier pixel : sinon le thème choisi s'applique après coup et la page
   clignote en clair chez quelqu'un qui a demandé sombre. */
(function () {{
  try {{
    var t = localStorage.getItem('theme');
    window.__theme = t || 'auto';
    if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
  }} catch (e) {{}}
}})();
</script>
</head>
<body>
<a class="skip" href="#main">Aller aux alertes</a>

<nav class="topnav" aria-label="Navigation">
  <div class="nav-in">
    <button class="navlink active" data-view="registre">Alertes actives</button>
    {'<button class="navlink" data-view="bivouac">Bivouac &amp; réglementation</button>' if bivouac else ''}
    {carte_nav}
    <button class="navlink" data-view="apropos">À propos</button>
    <button class="theme-btn" id="theme-btn" type="button" aria-label="Changer de thème">
      <span class="sr-only">Thème&nbsp;: </span><span id="theme-txt" aria-live="polite">auto</span>
    </button>
  </div>
</nav>

<div class="wrap">
<header class="mast">
  <div>
    <h1>Alertes-Rando.info</h1>
    <p class="tagline">Fermetures, déviations et réglementations sur les GR®, les chemins de Compostelle et les grands itinéraires d'Europe. Veille quotidienne : chaque alerte est datée, localisée et sourcée.</p>
  </div>
  <div class="mast-stats">
    <div class="stat warn"><b>{len(hautes)}</b><span>alertes rouges</span></div>
    <div class="stat"><b>{len(actives)}</b><span>alertes actives</span></div>
  </div>
</header>

<div class="layout">
<nav class="rail" aria-label="Recherche et rapports quotidiens">
  <div class="search">
    <input type="search" id="q" placeholder="Rechercher un sentier…"
           aria-label="Rechercher les alertes par sentier">
  </div>
  {'<p class="rail-label">Rapports quotidiens</p>' if nav_items else ''}
  {"".join(nav_items)}
</nav>

<main id="main" tabindex="-1">
<section id="registre" class="view" aria-labelledby="t-registre">
  <h2 id="t-registre" class="sr-only">Alertes actives</h2>
  <div class="cats" role="group" aria-label="Filtrer par catégorie">
  {cats_html}
  </div>
  <p class="legende">
    <span class="l-haute"><b>Alerte rouge</b> étape bloquée ou interdiction</span>
    <span class="l-moyenne"><b>Orange</b> impact réel, sans blocage</span>
    <span class="l-info"><b>Info</b> bon à savoir avant de partir</span>
  </p>
  <p id="live" class="sr-only" role="status" aria-live="polite"></p>
  <div class="cards">
  {cards_html}
  </div>
  <p id="noresult" class="noresult" hidden>Aucune alerte ne correspond à cette recherche.</p>
  <h2 class="bloc">Alertes clôturées</h2>
  <div class="cards">
  {closed_html}
  </div>
</section>

<section id="apropos" class="view about" hidden>
  <p class="eyebrow">Le projet</p>
  <h2 class="reg-title">À propos</h2>
  <p>Alertes-Rando.info part d'une difficulté que connaissent les marcheurs au long
  cours : l'information est éparpillée. Un massif fermé par arrêté préfectoral en plein
  été, un tronçon de GR® dévié après un éboulement, un refuge qui n'accueille plus, un
  bivouac soudain réglementé… Ces décisions sont bel et bien publiées, mais elles dorment
  dans des PDF de préfectures, des communiqués de parcs nationaux, des pages de
  fédérations et des articles de presse locale. Personne ne les rassemblait, et la
  fermeture se découvrait au pied du panneau, sac sur le dos.</p>
  <p>Alertes-Rando fait cette collecte à votre place. Chaque matin, une veille
  automatisée parcourt les sources officielles et la presse locale sur les grands
  itinéraires (GR® français, chemins de Compostelle, grandes traversées européennes),
  puis recoupe et date ce qu'elle trouve avant de le hiérarchiser. Le résultat tient en
  une page : des alertes classées par gravité, <strong>rouge</strong> pour une étape
  bloquée ou une interdiction, <strong>orange</strong> pour un impact réel sans blocage,
  <strong>info</strong> pour ce qui est bon à savoir. Chacune indique la portion
  concernée, une alternative quand elle existe, et les
  sources pour vérifier par vous-même.</p>
  <p>Les rapports quotidiens archivent en plus l'état des sentiers jour après jour. Une
  base bivouac &amp; réglementation rassemble les règles de près d'une centaine d'espaces
  protégés en Europe (parcs nationaux, réserves, massifs), pour savoir où poser la tente
  sans mauvaise surprise.</p>
  <p class="disclaimer">Ce site aide à préparer, il ne remplace jamais la source
  officielle. Avant de partir, vérifiez l'arrêté, la carte préfectorale ou la page du
  parc : elles seules font foi.</p>

  <div id="contact" class="contact">
    <h3 class="bloc">Nous écrire</h3>
    <p class="note">Vous avez croisé une déviation sur le terrain, ou repéré une fermeture
    que nous avons manquée ? Vous avez vu une erreur à signaler ? Les retours de marcheurs
    corrigent cette veille, et c'est ce qui la rend fiable.</p>
    <form id="form-contact" action="{FORM_ENDPOINT}" method="POST">
      <div>
        <label for="c-nom">Nom (facultatif)</label>
        <input id="c-nom" type="text" name="Nom" autocomplete="name">
      </div>
      <div>
        <label for="c-mail">Votre e-mail</label>
        <input id="c-mail" type="email" name="email" autocomplete="email" required>
      </div>
      <div>
        <label for="c-msg">Message</label>
        <textarea id="c-msg" name="Message" required
                  placeholder="Sentier concerné, secteur, ce que vous avez constaté…"></textarea>
      </div>
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <input type="hidden" name="_subject" value="Message depuis alertes-rando.info">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_template" value="table">
      <button type="submit">Envoyer</button>
      <p class="statut" id="c-statut" role="status" hidden></p>
    </form>
    <p class="note">Votre adresse ne sert qu'à vous répondre. Le message transite par le
    service FormSubmit, qui nous le fait parvenir par e-mail. Ce site ne le stocke pas, ne
    le transmet à personne et ne l'utilise à aucune autre fin.</p>
  </div>
</section>

{bivouac_section}
{carte_section}
{"".join(sections)}
</main>
</div>

<footer>
  <span>Généré le {built}</span><span>·</span>
  <span>alertes-rando.info, veille quotidienne automatisée</span><span>·</span>
  <span>État au {fr_date(latest_iso)}</span><span>·</span>
  <button class="footlink" data-view="apropos" data-anchor="contact">Contact</button>
</footer>
</div>

<script>window.__ZONES = {zones_json};</script>
<script>
(function () {{
  var links = document.querySelectorAll('.navlink');
  var views = document.querySelectorAll('.view');

  // Une vue = une URL. Sans ça, on ne pouvait ni envoyer le rapport du 6 août à
  // quelqu'un, ni mettre la page bivouac en favori, et le bouton Retour du
  // navigateur faisait sortir du site au lieu de revenir à la vue précédente.
  function vueVersHash(id) {{
    if (id === 'registre') return '';
    if (id.indexOf('d-') === 0) return '#rapport-' + id.slice(2);
    return '#' + id;
  }}
  function hashVersVue(h) {{
    h = (h || '').replace(/^#/, '');
    if (!h) return 'registre';
    if (h === 'contact') return 'apropos';
    if (h.indexOf('rapport-') === 0) h = 'd-' + h.slice(8);
    var el = document.getElementById(h);
    return (el && el.classList.contains('view')) ? h : 'registre';
  }}
  function show(id, pousser) {{
    var el = document.getElementById(id);
    if (!el || !el.classList.contains('view')) id = 'registre';
    links.forEach(function (x) {{ x.classList.toggle('active', x.dataset.view === id); }});
    views.forEach(function (v) {{ v.hidden = (v.id !== id); }});
    if (id === 'carte' && window.__initCarte) window.__initCarte();
    if (pousser) {{
      var h = vueVersHash(id);
      history.pushState({{ vue: id }}, '', h || location.pathname + location.search);
    }}
  }}
  window.__show = show;
{carte_js}
  links.forEach(function (b) {{
    b.addEventListener('click', function () {{
      show(b.dataset.view, true);
      window.scrollTo({{ top: 0 }});
    }});
  }});
  window.addEventListener('popstate', function () {{
    show(hashVersVue(location.hash), false);
  }});
  // route d'entrée : un lien partagé ouvre directement la bonne vue
  if (location.hash) {{
    var vue0 = hashVersVue(location.hash);
    if (vue0 !== 'registre') show(vue0, false);
    if (location.hash === '#contact') {{
      var c0 = document.getElementById('contact');
      if (c0) c0.scrollIntoView({{ block: 'start' }});
    }}
  }}

  // pied de page → ouvre « À propos » et amène directement au formulaire
  document.querySelectorAll('.footlink[data-view]').forEach(function (b) {{
    b.addEventListener('click', function () {{
      show(b.dataset.view, false);
      var cible = b.dataset.anchor && document.getElementById(b.dataset.anchor);
      history.pushState({{ vue: b.dataset.view }}, '',
                        b.dataset.anchor ? '#' + b.dataset.anchor : vueVersHash(b.dataset.view));
      if (cible) {{ cible.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }}
      else {{ window.scrollTo({{ top: 0 }}); }}
    }});
  }});

  // thème : auto (système) → clair → sombre. L'état est relu au chargement par le
  // script du <head>, celui-ci ne gère que la bascule et l'étiquette.
  var THEMES = ['auto', 'light', 'dark'];
  var LIB = {{ auto: 'auto', light: 'clair', dark: 'sombre' }};
  var tbtn = document.getElementById('theme-btn');
  var ttxt = document.getElementById('theme-txt');
  var theme = (window.__theme && THEMES.indexOf(window.__theme) !== -1) ? window.__theme : 'auto';
  if (ttxt) ttxt.textContent = LIB[theme];
  if (tbtn) tbtn.addEventListener('click', function () {{
    theme = THEMES[(THEMES.indexOf(theme) + 1) % THEMES.length];
    if (theme === 'auto') document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', theme);
    if (ttxt) ttxt.textContent = LIB[theme];
    try {{ localStorage.setItem('theme', theme); }} catch (e) {{}}
  }});

  // impression : on ouvre les volets « Détails » le temps du tirage, sinon la
  // feuille sort amputée de la moitié de ce qu'on venait chercher.
  window.addEventListener('beforeprint', function () {{
    document.querySelectorAll('.card details:not([open])').forEach(function (d) {{
      d.open = true; d.setAttribute('data-print-open', '');
    }});
  }});
  window.addEventListener('afterprint', function () {{
    document.querySelectorAll('.card details[data-print-open]').forEach(function (d) {{
      d.open = false; d.removeAttribute('data-print-open');
    }});
  }});

  // envoi du formulaire sans quitter la page (le POST classique reste le repli sans JS)
  var fc = document.getElementById('form-contact');
  if (fc) {{
    fc.addEventListener('submit', function (e) {{
      e.preventDefault();
      var st = document.getElementById('c-statut');
      var bouton = fc.querySelector('button[type=submit]');
      st.hidden = false; st.className = 'statut'; st.textContent = 'Envoi en cours…';
      bouton.disabled = true;
      fetch(fc.action.replace('formsubmit.co/', 'formsubmit.co/ajax/'), {{
        method: 'POST', headers: {{ 'Accept': 'application/json' }}, body: new FormData(fc)
      }})
        .then(function (r) {{
          return r.json().catch(function () {{ return {{}}; }})
                  .then(function (d) {{ return {{ http: r.status, d: d || {{}} }}; }});
        }})
        .then(function (res) {{
          if (String(res.d.success) === 'true') {{
            st.className = 'statut ok';
            st.textContent = 'Message envoyé, merci ! Nous vous répondrons à l\\'adresse indiquée.';
            fc.reset();
            return;
          }}
          // on affiche le motif réel renvoyé par le service : sans lui, impossible de
          // distinguer « formulaire pas encore activé » d'une vraie panne
          st.className = 'statut ko';
          st.textContent = res.d.message
            ? 'Envoi refusé (' + res.http + ') : ' + res.d.message
            : 'Envoi refusé (HTTP ' + res.http + '). Réessayez dans un moment.';
        }})
        .catch(function () {{
          st.className = 'statut ko';
          st.textContent = 'Envoi impossible : le service de messagerie est injoignable '
            + '(connexion coupée ou bloquée par une extension du navigateur).';
        }})
        .then(function () {{ bouton.disabled = false; }});
    }});
  }}

  var q = document.getElementById('q');
  var cards = document.querySelectorAll('.card:not(.bcard)');
  var noresult = document.getElementById('noresult');
  var live = document.getElementById('live');
  // `.cat` attrapait aussi les chips bivouac, qui portent les deux classes : cliquer
  // un filtre bivouac déclenchait en plus le gestionnaire des alertes et basculait
  // la vue. Les deux jeux de boutons sont maintenant disjoints.
  var catBtns = document.querySelectorAll('.cat:not(.bcat)');
  var curCat = '';
  function fold(s) {{
    return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase().trim();
  }}
  // Le compteur est annoncé aux lecteurs d'écran : filtrer ne produisait aucun retour
  // audible, on ne savait pas si la recherche avait pris.
  var direFiltre = null;
  function annoncer(n, filtre) {{
    if (!live) return;
    clearTimeout(direFiltre);
    direFiltre = setTimeout(function () {{
      live.textContent = filtre
        ? (n === 0 ? 'Aucune alerte ne correspond.'
                   : n + (n > 1 ? ' alertes affichées.' : ' alerte affichée.'))
        : '';
    }}, 400);
  }}
  function applyFilters() {{
    var v = fold(q.value);
    var hits = 0;
    cards.forEach(function (c) {{
      var ok = (!v || (c.dataset.itin || '').indexOf(v) !== -1)
            && (!curCat || c.dataset.cat === curCat);
      c.style.display = ok ? '' : 'none';
      if (ok) hits++;
    }});
    noresult.hidden = !((v || curCat) && hits === 0);
    annoncer(hits, !!(v || curCat));
  }}
  // 263 cartes repeintes à chaque frappe : on attend que la saisie se pose.
  var minuteur = null;
  q.addEventListener('input', function () {{
    clearTimeout(minuteur);
    minuteur = setTimeout(function () {{
      var biv = document.getElementById('bivouac');
      var onBivouac = biv && !biv.hidden;
      if (fold(q.value) && document.getElementById('registre').hidden && !onBivouac) {{
        show('registre', true);
      }}
      applyFilters();
      applyBivouacFilters();
    }}, 120);
  }});
  var bcards = document.querySelectorAll('.bcard');
  var bnoresult = document.getElementById('bnoresult');
  var bcatBtns = document.querySelectorAll('.bcat');
  var curRegle = '';
  function applyBivouacFilters() {{
    if (!bcards.length) return;
    var v = fold(q.value);
    var hits = 0;
    bcards.forEach(function (c) {{
      var ok = (!v || (c.dataset.bsearch || '').indexOf(v) !== -1)
            && (!curRegle || c.dataset.regle === curRegle);
      c.style.display = ok ? '' : 'none';
      if (ok) hits++;
    }});
    if (bnoresult) bnoresult.hidden = !((v || curRegle) && hits === 0);
  }}
  function marquer(boutons, cle, valeur) {{
    boutons.forEach(function (x) {{
      var sien = x.dataset[cle] || '';
      x.setAttribute('aria-pressed', (sien === valeur || (!valeur && !sien)) ? 'true' : 'false');
    }});
  }}
  bcatBtns.forEach(function (b) {{
    b.addEventListener('click', function () {{
      curRegle = (curRegle === b.dataset.regle) ? '' : b.dataset.regle;
      marquer(bcatBtns, 'regle', curRegle);
      applyBivouacFilters();
    }});
  }});
  catBtns.forEach(function (b) {{
    b.addEventListener('click', function () {{
      curCat = (curCat === b.dataset.cat) ? '' : b.dataset.cat;
      marquer(catBtns, 'cat', curCat);
      if (document.getElementById('registre').hidden) show('registre', true);
      applyFilters();
    }});
  }});
}})();
</script>
</body>
</html>
"""
    errs = qa_check(cards, page, bivouac) + registry_integrity_errors()
    warns = ton_warnings(cards)
    if warns:
        print(f"⚠ ton : {len(warns)} fiche(s) dont « Zone (détails) » raconte encore le "
              f"déroulé de la veille au lieu de l'état du terrain (non bloquant — "
              f"à nettoyer au prochain passage sur la fiche) :", file=sys.stderr)
        for w in warns[:12]:
            print("  ~ " + w, file=sys.stderr)
        if len(warns) > 12:
            print(f"  … et {len(warns) - 12} autre(s)", file=sys.stderr)
    if errs:
        print(f"QA ÉCHEC — {len(errs)} violation(s), site NON écrit :", file=sys.stderr)
        for e in errs:
            print("  ✗ " + e, file=sys.stderr)
        print("→ corriger le registre (ou signaler un bug générateur) puis relancer ; "
              "boucler jusqu'à exit 0. NE PAS PUBLIER.", file=sys.stderr)
        return 2
    OUT.write_text(page, encoding="utf-8")

    # robots.txt + sitemap.xml : le site n'en avait aucun. Le sitemap ne déclare que
    # l'URL canonique — les vues internes vivent derrière un fragment (#rapport-…),
    # que les moteurs ne comptent pas comme des pages distinctes. Les rendre
    # indexables une par une demanderait un vrai build multi-pages.
    (HERE / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: https://www.alertes-rando.info/sitemap.xml\n",
        encoding="utf-8")
    (HERE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <url>\n'
        '    <loc>https://www.alertes-rando.info/</loc>\n'
        f'    <lastmod>{latest_iso}</lastmod>\n'
        '    <changefreq>daily</changefreq>\n'
        '  </url>\n'
        '</urlset>\n',
        encoding="utf-8")

    masse = sum(_tailles_courantes().values())
    print(f"OK (QA passée) → {OUT}  ({len(actives)} actives, {len(closes)} clôturées, "
          f"{n_dig} digests ; registre {masse} car. / {len(cards)} fichiers)")
    if bivouac:   # suivi de la veille bivouac hebdomadaire (non bloquant)
        hypo = sum(1 for b in bivouac if b["statut"].upper().startswith("HYPO"))
        print(f"   bivouac : {len(bivouac)} fiches, {hypo} HYPOTHESE, "
              f"plus ancienne vérif {min(b['date_verif'] for b in bivouac)}")
    return 0


if __name__ == "__main__":
    sys.exit(build())
