# -*- coding: utf-8 -*-
"""Layout-QA: startet einen lokalen Server auf docs/ und prüft jede Seite bei 390, 820 und 1280 px.

    python3 src/qa.py                 # alle Seiten
    python3 src/qa.py --shot out.png  # zusätzlich Screenshot der Startseite bei 390 px

Prüft: horizontales Scrollen, herausragende Eingabefelder, abgeschnittene Auswahltexte,
Eingabe-Paare nicht auf einer Linie, fehlende Bilder, JavaScript-Fehler, tote interne Links.
Braucht Playwright mit Chromium. Exit-Code 1 bei Problemen.
"""
import glob, os, re, socket, subprocess, sys, time

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")

CHK = """(()=>{const out=[];
document.querySelectorAll('.row2').forEach((r,k)=>{const ins=[...r.querySelectorAll('input,select')].map(e=>Math.round(e.getBoundingClientRect().top));if(ins.length==2&&Math.abs(ins[0]-ins[1])>2&&r.getBoundingClientRect().width>500)out.push('Eingabefelder nicht auf einer Linie #'+k)});
document.querySelectorAll('input,select,textarea').forEach(e=>{const b=e.getBoundingClientRect(),f=e.closest('form,main');if(f&&b.right>f.getBoundingClientRect().right+1)out.push('Feld ragt heraus '+(e.id||e.name))});
document.querySelectorAll('select').forEach(e=>{if(e.scrollWidth>e.clientWidth+2)out.push('Auswahltext abgeschnitten '+e.id)});
if(document.documentElement.scrollWidth>innerWidth)out.push('horizontales Scrollen ('+document.documentElement.scrollWidth+'px)');
document.querySelectorAll('img').forEach(i=>{if(i.complete&&i.naturalWidth==0)out.push('Bild fehlt '+i.getAttribute('src'))});
return out})()"""


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def dead_links():
    """Interne Links auf nicht vorhandene Dateien/Anker (statisch geprüft)."""
    out = []
    files = {os.path.basename(f): open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(ROOT, "*.html"))}
    for name, h in files.items():
        for href in re.findall(r'href="([^"]+)"', h):
            if href.startswith(("http", "mailto:", "tel:", "#", "data:")) or href.endswith((".css", ".svg", ".png", ".xml")):
                if href.startswith("#") and len(href) > 1 and f'id="{href[1:]}"' not in h:
                    out.append(f"{name}: Anker {href} fehlt")
                continue
            target, _, anchor = href.partition("#")
            if not os.path.exists(os.path.join(ROOT, target)):
                out.append(f"{name}: Link auf fehlende Datei {target}")
            elif anchor and target in files and f'id="{anchor}"' not in files[target]:
                out.append(f"{name}: Anker {href} fehlt")
    return out


# Seiten, die schon vor der Meta-Prüfung zu lange Title/Description hatten (nur Warnung; beim nächsten Überarbeiten kürzen)
META_ALT = {"abrechnungsfrist-nebenkosten.html", "abrechnungsfrist-rechner.html", "anlage-v.html", "heizkosten-rechner.html",
            "index.html", "rechner.html", "umlagefaehige-nebenkosten.html"}


def meta_lengths(max_title=60, max_desc=155):
    """Title > 60 bzw. Description > 155 Zeichen (Google kürzt sonst). Seiten mit noindex werden übersprungen."""
    import html as _h
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        h = open(f, encoding="utf-8").read()
        t = re.search(r"<title>(.*?)</title>", h, re.S)
        if not t or 'name="robots" content="noindex' in h:
            continue
        d = re.search(r'<meta name="description" content="([^"]*)"', h)
        tl, dl = len(_h.unescape(t.group(1))), len(_h.unescape(d.group(1))) if d else 0
        if tl > max_title or dl > max_desc:
            out.append(f"{os.path.basename(f)}: Title {tl}/{max_title}, Description {dl}/{max_desc}")
    return out


def bundle_pages():
    """Pakete (config "includes"): Paketseite ohne Summen-/Vergleichsbeträge, wenn no_compare (DS24-Ablehnung
    09.11.: „einzeln zusammen …“ galt als Streichpreis) – erlaubt sind nur Paketpreis und Einzelpreise der Karten.
    Auf jeder enthaltenen Produktseite mit Checkout muss der Paket-Hinweis Anzahl und Preis richtig nennen."""
    import json
    cfg = json.load(open(os.path.join(ROOT, "..", "config.json"), encoding="utf-8"))
    by = {p["slug"]: p for p in cfg.get("products", [])}
    eur = lambda v: f"{float(v):.2f}".replace(".", ",")
    out = []
    for b in cfg.get("products", []):
        inc = [by[s] for s in dict.fromkeys(b.get("includes", [])) if s in by and s != b["slug"]]
        if not inc:
            continue
        f = os.path.join(ROOT, b["slug"] + ".html")
        if not os.path.exists(f):
            out.append(f"{b['slug']}.html fehlt")
            continue
        h = re.sub(r"<script.*?</script>", " ", open(f, encoding="utf-8").read(), flags=re.S).replace("&nbsp;", " ")
        if b.get("no_compare"):
            ok = {eur(b["price"])} | {eur(q["price"]) for q in inc}
            amts = set(re.findall(r"(\d+,\d{2}) ?€", h)) - ok
            if amts:
                out.append(f"{b['slug']}.html: Beträge außer Paket-/Einzelpreisen trotz no_compare: {sorted(amts)}")
            if re.search(r"einzeln zusammen|Ersparnis|sparen Sie", h, re.I):
                out.append(f"{b['slug']}.html: Vergleichs-/Ersparnisformulierung trotz no_compare")
        want = f"{len(inc)} Vorlagen für {eur(b['price'])} €"
        for q in inc:
            if not q.get("checkout_url"):
                continue
            hq = open(os.path.join(ROOT, q["slug"] + ".html"), encoding="utf-8").read().replace("&nbsp;", " ")
            hint = re.search(r'class="bundlehint">.*?href="' + re.escape(b["slug"]) + r'\.html".*?</p>', hq, re.S)
            if not hint or want not in hint.group(0):
                out.append(f"{q['slug']}.html: Paket-Hinweis fehlt oder nennt nicht „{want}“")
    return out


def main(argv):
    from playwright.sync_api import sync_playwright
    shot = argv[argv.index("--shot") + 1] if "--shot" in argv else None
    bad = 0
    for d in dead_links():
        bad += 1
        print("LINK", d)
    for d in bundle_pages():
        bad += 1
        print("PAKET", d)
    # Zu lange Metadaten: bei den Altseiten in META_ALT nur Warnung, sonst ein Problem.
    for m in meta_lengths():
        if m.split(":")[0] in META_ALT:
            print("META-WARNUNG", m)
        else:
            bad += 1
            print("META", m)
    port = free_port()
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1"], cwd=ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for w, h in [(390, 844), (820, 1180), (1280, 900)]:
                pg = b.new_page(viewport={"width": w, "height": h})
                errs = []
                pg.on("pageerror", lambda e: errs.append("JS-Fehler: " + str(e)))
                pages = sorted(glob.glob(os.path.join(ROOT, "*.html")))
                for f in pages:
                    u = os.path.basename(f)
                    pg.goto(f"http://127.0.0.1:{port}/{u}")
                    pg.wait_for_timeout(100)
                    r = pg.evaluate(CHK) + errs
                    if r:
                        bad += 1
                        print(w, u, r)
                    errs.clear()
                if shot and w == 390:
                    pg.goto(f"http://127.0.0.1:{port}/index.html")
                    pg.wait_for_timeout(200)
                    pg.screenshot(path=shot, full_page=True)
                    print("Screenshot:", shot)
                pg.close()
            b.close()
            print(f"{len(pages)} Seiten × 3 Breiten geprüft")
    finally:
        srv.terminate()
    print("QA ok" if not bad else f"QA: {bad} Probleme")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
