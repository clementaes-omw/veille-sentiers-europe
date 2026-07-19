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
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIVRABLES = HERE.parent / "livrables"
OUT = HERE / "index.html"
# Analytics (Umami Cloud, sans cookies — pas de bannière RGPD nécessaire).
# Renseigner le website ID fourni par cloud.umami.is pour activer ; vide = pas de script.
UMAMI_WEBSITE_ID = ""
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

def parse_registre(md: str):
    """Extrait les lignes du tableau d'alertes (10 colonnes) + le reste du document."""
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


def render_card(c) -> str:
    statut_txt = c["statut"]
    closed = "CLÔTURÉ" in statut_txt.upper()
    sev = "clos" if closed else sev_class(c["sev"])
    sev_label = {"haute": "Alerte rouge", "moyenne": "Alerte orange",
                 "info": "Info", "clos": "Clôturée"}[sev]
    changed = "CHANGÉ" in statut_txt
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
    return f"""<article class="card {sev}" data-itin="{html.escape(searchable, quote=True)}" data-cat="{cat_slug}">
  <div class="card-top">
    {badges_html}
    <span class="badge sev-{sev}" title="Alerte rouge = étape bloquée ou interdiction · orange = impact réel sans blocage · info = à savoir">{sev_label}</span>
    {chips}
    <span class="type">{inline(c["type"])}</span>
  </div>
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
REGLE_META = {
    "interdit": ("🚫", "Interdit", "haute"),
    "tolere": ("🌙", "Toléré (conditions)", "moyenne"),
    "autorise": ("✅", "Autorisé", "ok"),
    "variable": ("⚖️", "Variable / droit commun", "info"),
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
    emoji, label, cls = REGLE_META.get(b["regle"], ("⚖️", b["regle"], "info"))
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
    <span class="badge sev-{'haute' if cls=='haute' else 'moyenne' if cls=='moyenne' else 'info' if cls=='info' else 'ok'}">{emoji} {label}</span>
    <span class="type">{html.escape(b["type"])}</span>
  </div>
  <p class="bname"><strong>{inline(b["nom"])}</strong></p>
  <p class="portion">{hyp}{inline(b["conditions"])}</p>
  <p class="alt"><span class="alt-label">Feux</span> {inline(b["feu"] or "non précisé")}</p>
  {notes}
  <p class="meta dates"><span>{inline(b["sentiers"])}</span><span class="sep">·</span>source du {html.escape(b["date_source"])}<span class="sep">·</span>vérifié le {html.escape(b["date_verif"])}</p>
  <p class="meta sources">Source : {src_html}</p>
</article>"""

# ---------------------------------------------------------------- contrôle qualité

BADGE_INTERDITS = ["[", "]", "HYPOTH", "Aucun", "P1 ;", "à préciser", "recouper"]


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
    reg_md = (LIVRABLES / "alertes-actives.md").read_text(encoding="utf-8")
    cards, reg_rest = parse_registre(reg_md)
    actives = [c for c in cards if "CLÔTURÉ" not in c["statut"].upper()]
    closes = [c for c in cards if "CLÔTURÉ" in c["statut"].upper()]
    hautes = [c for c in actives if sev_class(c["sev"]) == "haute"]

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
    cats_html = (f'<button class="cat active" data-cat="">Toutes '
                 f'<span>{len(actives) + len(closes)}</span></button>')
    for cat in CATEGORIES:
        n = counts.get(cat["slug"], 0)
        if n:
            cats_html += (f'<button class="cat" data-cat="{cat["slug"]}">'
                          f'{cat["emoji"]} {html.escape(cat["label"])} <span>{n}</span></button>')
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
<p class="eyebrow">Digest quotidien</p>
<h2 class="digest-title">{fr_date(iso)}</h2>
{body}
</section>""")

    bivouac_section = ""
    if bivouac:
        bcards = "\n".join(render_bivouac_card(b) for b in bivouac)
        bcounts = {}
        for b in bivouac:
            bcounts[b["regle"]] = bcounts.get(b["regle"], 0) + 1
        bchips = f'<button class="cat bcat active" data-regle="">Toutes <span>{len(bivouac)}</span></button>'
        for slug, (emoji, label, _c) in REGLE_META.items():
            n = bcounts.get(slug, 0)
            if n:
                bchips += (f'<button class="cat bcat" data-regle="{slug}">{emoji} {html.escape(label)} '
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
    page = f"""<title>Alertes Rando</title>
{analytics}
<style>
:root {{
  --paper: #faf9f5; --panel: #f1efe8; --ink: #20261f; --ink-2: #5a6055;
  --line: #ddd9cc; --pine: #2f5d45; --pine-soft: #e4ece6;
  --haute: #b3362b; --haute-bg: #f6e7e4; --moy: #a86a1f; --moy-bg: #f4ecdd;
  --info: #4a6478; --info-bg: #e7edf1; --clos: #8a8f86; --clos-bg: #ecebe5;
  --serif: "Iowan Old Style", "Palatino Nova", Palatino, "Palatino Linotype", Georgia, serif;
  --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --paper: #1a1e1a; --panel: #22271f; --ink: #e6e4da; --ink-2: #a7ab9e;
    --line: #3a4036; --pine: #7fb598; --pine-soft: #26332b;
    --haute: #e07a6e; --haute-bg: #392420; --moy: #d8a35c; --moy-bg: #362c1c;
    --info: #93b0c4; --info-bg: #232d34; --clos: #8a8f86; --clos-bg: #262a24;
  }}
}}
:root[data-theme="light"] {{
  --paper: #faf9f5; --panel: #f1efe8; --ink: #20261f; --ink-2: #5a6055;
  --line: #ddd9cc; --pine: #2f5d45; --pine-soft: #e4ece6;
  --haute: #b3362b; --haute-bg: #f6e7e4; --moy: #a86a1f; --moy-bg: #f4ecdd;
  --info: #4a6478; --info-bg: #e7edf1; --clos: #8a8f86; --clos-bg: #ecebe5;
}}
:root[data-theme="dark"] {{
  --paper: #1a1e1a; --panel: #22271f; --ink: #e6e4da; --ink-2: #a7ab9e;
  --line: #3a4036; --pine: #7fb598; --pine-soft: #26332b;
  --haute: #e07a6e; --haute-bg: #392420; --moy: #d8a35c; --moy-bg: #362c1c;
  --info: #93b0c4; --info-bg: #232d34; --clos: #8a8f86; --clos-bg: #262a24;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--paper); color: var(--ink);
  font: 16px/1.55 var(--sans); }}
a {{ color: var(--pine); }}
code {{ font-family: var(--mono); font-size: .85em; background: var(--panel);
  padding: 1px 5px; border-radius: 4px; }}
del {{ color: var(--ink-2); }}
.wrap {{ max-width: 1200px; margin: 0 auto; padding: 0 20px 60px; }}

header.mast {{ display: flex; align-items: center; gap: 18px; flex-wrap: wrap;
  padding: 26px 0 18px; border-bottom: 2px solid var(--ink); }}
.waymark {{ width: 34px; height: 26px; border-radius: 3px; overflow: hidden;
  box-shadow: 0 0 0 1px var(--line); flex: none; display: flex; flex-direction: column; }}
.waymark .w {{ flex: 1; background: #fff; }}
.waymark .r {{ flex: 1; background: #c0392b; }}
h1 {{ font-family: var(--serif); font-size: clamp(1.5rem, 3.5vw, 2.1rem);
  margin: 0; line-height: 1.15; text-wrap: balance; }}
h1 .amp {{ color: var(--pine); font-style: italic; }}
.tagline {{ margin: 2px 0 0; color: var(--ink-2); font-size: .92rem; }}
.mast-stats {{ margin-left: auto; display: flex; gap: 22px; }}
.stat {{ text-align: right; }}
.stat b {{ display: block; font-family: var(--serif); font-size: 1.5rem;
  font-variant-numeric: tabular-nums; line-height: 1.1; }}
.stat.warn b {{ color: var(--haute); }}
.stat span {{ font-size: .72rem; text-transform: uppercase; letter-spacing: .07em;
  color: var(--ink-2); }}

.layout {{ display: grid; grid-template-columns: 210px 1fr; gap: 36px; padding-top: 26px; }}
nav.rail {{ position: sticky; top: 16px; align-self: start; display: flex;
  flex-direction: column; gap: 3px; max-height: calc(100vh - 40px); overflow: auto; }}
.rail-label {{ font-size: .72rem; text-transform: uppercase; letter-spacing: .08em;
  color: var(--ink-2); margin: 14px 0 5px; }}
.navlink {{ display: flex; justify-content: space-between; align-items: baseline;
  gap: 8px; text-align: left; border: 0; background: none; color: var(--ink);
  font: inherit; font-size: .93rem; padding: 6px 10px; border-radius: 6px;
  cursor: pointer; border-left: 3px solid transparent; }}
.navlink .yr {{ color: var(--ink-2); font-size: .72rem; font-family: var(--mono); }}
.navlink:hover {{ background: var(--panel); }}
.navlink.active {{ background: var(--pine-soft); border-left-color: var(--pine); font-weight: 600; }}
.navlink.registre {{ font-weight: 600; }}
.navlink:focus-visible {{ outline: 2px solid var(--pine); outline-offset: 1px; }}

main {{ min-width: 0; }}
.view > :first-child {{ margin-top: 0; }}
.eyebrow {{ font-size: .74rem; text-transform: uppercase; letter-spacing: .09em;
  color: var(--pine); margin: 0 0 4px; font-weight: 600; }}
h2.digest-title, h2.reg-title {{ font-family: var(--serif); font-size: 1.7rem;
  margin: 0 0 14px; text-wrap: balance; }}
.digest h2, .view h2 {{ font-family: var(--serif); }}
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

.rail .search {{ margin: 0 0 10px; }}
.search input {{ width: 100%; font: inherit; font-size: .9rem; color: var(--ink);
  background: var(--paper); border: 1.5px solid var(--line); border-radius: 8px;
  padding: 8px 12px; }}
.search input:focus {{ outline: none; border-color: var(--pine);
  box-shadow: 0 0 0 3px var(--pine-soft); }}
.search input::placeholder {{ color: var(--ink-2); }}
.noresult {{ color: var(--ink-2); font-style: italic; }}
.cats {{ display: flex; flex-wrap: wrap; gap: 7px; margin: 12px 0 4px; }}
.cat {{ font: inherit; font-size: .82rem; color: var(--ink); background: var(--panel);
  border: 1px solid var(--line); border-radius: 999px; padding: 4px 12px; cursor: pointer; }}
.cat span {{ color: var(--ink-2); font-size: .74rem; font-variant-numeric: tabular-nums; }}
.cat:hover {{ border-color: var(--pine); }}
.cat.active {{ background: var(--pine); border-color: var(--pine); color: #fff; }}
.cat.active span {{ color: rgba(255,255,255,.75); }}
.cat:focus-visible {{ outline: 2px solid var(--pine); outline-offset: 1px; }}
.cards {{ display: flex; flex-direction: column; gap: 14px; margin: 18px 0 30px; }}
.card {{ border: 1px solid var(--line); border-left: 5px solid var(--clos);
  border-radius: 8px; padding: 14px 16px; background: var(--paper); }}
.card.haute {{ border-left-color: var(--haute); }}
.card.moyenne {{ border-left-color: var(--moy); }}
.card.info {{ border-left-color: var(--info); }}
.card.clos {{ opacity: .75; }}
.card.ok {{ border-left-color: var(--pine); }}
.badge.sev-ok {{ background: var(--pine-soft); color: var(--pine); }}
.bname {{ margin: 0 0 6px; font-size: 1.02rem; }}
.disclaimer {{ color: var(--ink-2); font-size: .85rem; font-style: italic; max-width: 80ch; }}
.card-top {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 8px; }}
.badge {{ font-size: .7rem; font-weight: 700; letter-spacing: .04em;
  padding: 2px 8px; border-radius: 5px; }}
.badge.itin {{ background: var(--ink); color: var(--paper); font-family: var(--mono); }}
.badge.sev-haute {{ background: var(--haute-bg); color: var(--haute); }}
.badge.sev-moyenne {{ background: var(--moy-bg); color: var(--moy); }}
.badge.sev-info {{ background: var(--info-bg); color: var(--info); }}
.badge.sev-clos {{ background: var(--clos-bg); color: var(--clos); }}
.chip.changed {{ font-size: .7rem; font-weight: 700; color: var(--pine);
  background: var(--pine-soft); padding: 2px 8px; border-radius: 5px; }}
.card .type {{ color: var(--ink-2); font-size: .8rem; }}
.card .portion {{ margin: 0 0 10px; font-size: .97rem; line-height: 1.5; max-width: 90ch; }}
.card .alt {{ margin: 0 0 10px; font-size: .92rem; max-width: 90ch;
  padding: 8px 12px; background: var(--pine-soft); border-radius: 6px; }}
.card .alt-label {{ display: inline-block; font-size: .68rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: .06em; color: var(--pine);
  margin-right: 8px; vertical-align: 1px; }}
.card.clos .alt {{ background: var(--clos-bg); }}
.card.clos .alt-label {{ color: var(--clos); }}
.card .meta {{ margin: 0; color: var(--ink-2); font-size: .82rem; max-width: 90ch; }}
.card .meta.dates {{ margin-top: 10px; padding-top: 8px; border-top: 1px solid var(--line); }}
.card .meta.sources {{ margin-top: 3px; }}
.card .meta .sep {{ margin: 0 6px; }}
.card details {{ margin-top: 10px; font-size: .88rem; }}
.card summary {{ cursor: pointer; color: var(--pine); font-weight: 600; font-size: .82rem; }}
.card details p {{ margin: 8px 0 0; max-width: 90ch; }}
.card .key {{ margin: 6px 0 0; }}
.card .key code {{ font-size: .72rem; color: var(--ink-2); background: none; padding: 0; }}
h3.bloc {{ font-family: var(--serif); font-size: 1.15rem; margin: 34px 0 4px; }}
.annexes h2 {{ font-size: 1.2rem; margin-top: 34px; }}

footer {{ margin-top: 50px; padding-top: 14px; border-top: 1px solid var(--line);
  color: var(--ink-2); font-size: .8rem; display: flex; gap: 8px; flex-wrap: wrap; }}

@media (max-width: 760px) {{
  .layout {{ display: block; }}
  nav.rail {{ position: static; flex-direction: row; align-items: center;
    max-height: none; overflow-x: auto; padding-bottom: 10px; margin-bottom: 14px;
    border-bottom: 1px solid var(--line); }}
  .rail-label {{ display: none; }}
  .rail .search {{ flex: none; width: 200px; margin: 0 6px 0 0; }}
  .navlink {{ flex: none; border-left: 0; border-bottom: 3px solid transparent; border-radius: 6px 6px 0 0; }}
  .navlink.active {{ border-bottom-color: var(--pine); }}
  .mast-stats {{ width: 100%; margin-left: 0; justify-content: flex-start; }}
  .stat {{ text-align: left; }}
}}
@media (prefers-reduced-motion: no-preference) {{
  .view {{ animation: fade .18s ease; }}
  @keyframes fade {{ from {{ opacity: 0; transform: translateY(3px); }} }}
}}
</style>

<div class="wrap">
<header class="mast">
  <div class="waymark" aria-hidden="true"><span class="w"></span><span class="r"></span></div>
  <div>
    <h1>Alertes <span class="amp">Rando</span></h1>
    <p class="tagline">Alertes fermetures, sécurité et règlementation sur les GR®, chemins de Compostelle, grands itinéraires d'Europe</p>
  </div>
  <div class="mast-stats">
    <div class="stat warn"><b>{len(hautes)}</b><span>alertes rouges</span></div>
    <div class="stat"><b>{len(actives)}</b><span>alertes actives</span></div>
  </div>
</header>

<div class="layout">
<nav class="rail" aria-label="Navigation">
  <div class="search">
    <input type="search" id="q" placeholder="Rechercher un sentier…"
           aria-label="Rechercher les alertes par sentier">
  </div>
  <button class="navlink registre active" data-view="registre">Alertes actives</button>
  {'<button class="navlink registre" data-view="bivouac">Bivouac &amp; réglementation</button>' if bivouac else ''}
  {'<p class="rail-label">Digests quotidiens</p>' if nav_items else ''}
  {"".join(nav_items)}
</nav>

<main>
<section id="registre" class="view">
  <p class="eyebrow">Dernière mise à jour : {fr_date(latest_iso)}</p>
  <h2 class="reg-title">Alertes actives sur les sentiers</h2>
  <div class="cats" role="group" aria-label="Filtrer par catégorie">
  {cats_html}
  </div>
  <div class="cards">
  {cards_html}
  </div>
  <p id="noresult" class="noresult" hidden>Aucune alerte pour cette recherche — bon signe pour ce sentier.</p>
  <h3 class="bloc">Alertes clôturées</h3>
  <div class="cards">
  {closed_html}
  </div>
</section>

{bivouac_section}
{"".join(sections)}
</main>
</div>

<footer>
  <span>Généré le {built}</span><span>·</span>
  <span>alertes-rando.info — veille quotidienne automatisée</span><span>·</span>
  <span>État au {fr_date(latest_iso)}</span>
</footer>
</div>

<script>
(function () {{
  var links = document.querySelectorAll('.navlink');
  var views = document.querySelectorAll('.view');
  function show(id) {{
    links.forEach(function (x) {{ x.classList.toggle('active', x.dataset.view === id); }});
    views.forEach(function (v) {{ v.hidden = (v.id !== id); }});
  }}
  links.forEach(function (b) {{
    b.addEventListener('click', function () {{
      show(b.dataset.view);
      window.scrollTo({{ top: 0 }});
    }});
  }});

  var q = document.getElementById('q');
  var cards = document.querySelectorAll('.card:not(.bcard)');
  var noresult = document.getElementById('noresult');
  var catBtns = document.querySelectorAll('.cat');
  var curCat = '';
  function fold(s) {{
    return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase().trim();
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
  }}
  q.addEventListener('input', function () {{
    var biv = document.getElementById('bivouac');
    var onBivouac = biv && !biv.hidden;
    if (fold(q.value) && document.getElementById('registre').hidden && !onBivouac) show('registre');
    applyFilters();
    applyBivouacFilters();
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
  bcatBtns.forEach(function (b) {{
    b.addEventListener('click', function () {{
      curRegle = (curRegle === b.dataset.regle) ? '' : b.dataset.regle;
      bcatBtns.forEach(function (x) {{
        x.classList.toggle('active', x.dataset.regle === curRegle || (!curRegle && !x.dataset.regle));
      }});
      applyBivouacFilters();
    }});
  }});
  catBtns.forEach(function (b) {{
    b.addEventListener('click', function () {{
      curCat = (curCat === b.dataset.cat) ? '' : b.dataset.cat;
      catBtns.forEach(function (x) {{
        x.classList.toggle('active', x.dataset.cat === curCat || (!curCat && !x.dataset.cat));
      }});
      if (document.getElementById('registre').hidden) show('registre');
      applyFilters();
    }});
  }});
}})();
</script>
"""
    errs = qa_check(cards, page, bivouac)
    if errs:
        print(f"QA ÉCHEC — {len(errs)} violation(s), site NON écrit :", file=sys.stderr)
        for e in errs:
            print("  ✗ " + e, file=sys.stderr)
        print("→ corriger le registre (ou signaler un bug générateur) puis relancer ; "
              "boucler jusqu'à exit 0. NE PAS PUBLIER.", file=sys.stderr)
        return 2
    OUT.write_text(page, encoding="utf-8")
    print(f"OK (QA passée) → {OUT}  ({len(actives)} actives, {len(closes)} clôturées, {n_dig} digests)")
    return 0


if __name__ == "__main__":
    sys.exit(build())
