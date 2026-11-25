import os, html, importlib, sys
sys.path.insert(0, os.path.dirname(__file__))
from content_meta import *
OUT = os.path.join(os.path.dirname(__file__), "..", "public")
LANGS = ["ar", "en", "es", "fr"]
PATH = {"ar": "/", "en": "/en/", "es": "/es/", "fr": "/fr/"}
LNAME = {"ar": "العربية", "en": "English", "es": "Español", "fr": "Français"}
SHOTLANG = {"ar": "ar", "en": "en", "es": "es", "fr": "en"}

CREDITS = [
 ("EasyList, EasyPrivacy, Adblock Warning Removal List, Liste AR, EasyList Spanish, Fanboy's lists","https://easylist.to/","GPLv3 / CC BY-SA 3.0"),
 ("AdGuard Base, Annoyances, Spanish/Portuguese, Tracking, Mobile, Social","https://github.com/AdguardTeam/AdguardFilters","GPLv3"),
 ("uBlock filters, uBlock Quick fixes","https://github.com/uBlockOrigin/uAssets","GPLv3"),
 ("Phishing URL Blocklist","https://gitlab.com/malware-filter/phishing-filter","CC BY-SA 4.0"),
 ("Malicious URL Blocklist (URLhaus, abuse.ch)","https://gitlab.com/malware-filter/urlhaus-filter","CC0 / CC BY-SA 4.0"),
 ("Peter Lowe's list","https://pgl.yoyo.org/adservers/","free to use, non-commercial"),
 ("AdAway hosts","https://adaway.org/","CC BY 3.0"),
 ("Steven Black hosts","https://github.com/StevenBlack/hosts","MIT"),
 ("HaGeZi DNS blocklists","https://github.com/hagezi/dns-blocklists","GPLv3"),
 ("Dan Pollock's hosts","https://someonewhocares.org/hosts/","free to use, not for sale"),
 ("NoCoin list","https://github.com/hoshsadiq/adblock-nocoin-list","MIT"),
 ("Hajb streams & downloads list","—","MIT"),
]
# benchmark rows: values none, hajb, ubol, adguard ; best index (lower better)
BENCH = [
 ("2865","50","84","543",1,None),
 ("86","1","23","4",1,None),
 ("8087","4299","4698","5222",1,None),
 ("1512","726","736","1231",1,"ms"),
 ("41","14","18","27",1,"mbu"),
 ("2803","2070","2012","2715",2,"mbu"),
 ("0","0","0","1",None,None),
 ("1/3","0/3","0/3","0/3",None,None),
]
LANG_SAFE_CODE = {"ar":"ar","en":"en","es":"es","fr":"fr"}

def e(s): return html.escape(s, quote=True)
def mb(n, t): return f"{n/1048576:.1f} {t['mb']}"

def img(src, alt, w, h, cls="", eager=False):
    return f'<img src="{src}" alt="{e(alt)}" width="{w}" height="{h}"{" class=%s" % chr(34)+cls+chr(34) if cls else ""} {"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} decoding="async">'

SIZES = {}
from PIL import Image
def isize(p):
    if p not in SIZES:
        SIZES[p] = Image.open(os.path.join(OUT, p.lstrip("/"))).size
    return SIZES[p]

def page(L):
    t = importlib.import_module("t_" + L).T
    pre = "/" if L == "ar" else PATH[L]
    sc = t["sc"]
    out = []
    w = out.append
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{PATH[l]}">' for l in LANGS) + f'<link rel="alternate" hreflang="x-default" href="{SITE}/">'
    w(f'''<!doctype html>
<html lang="{t["lang"]}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<link rel="canonical" href="{SITE}{PATH[L]}">{alts}
<meta property="og:type" content="website"><meta property="og:title" content="{e(t["title"])}"><meta property="og:description" content="{e(t["desc"])}"><meta property="og:url" content="{SITE}{PATH[L]}"><meta property="og:image" content="{SITE}/assets/og.png"><meta name="twitter:card" content="summary_large_image">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#0e1311" media="(prefers-color-scheme: dark)"><meta name="theme-color" content="#eef3ef" media="(prefers-color-scheme: light)">
<link rel="icon" href="/assets/favicon-32.png" type="image/png" sizes="32x32"><link rel="icon" href="/assets/favicon-16.png" type="image/png" sizes="16x16"><link rel="icon" href="/assets/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/plexarabic-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/reemkufi.woff2" as="font" type="font/woff2" crossorigin>
<script src="/assets/theme.js"></script>
<link rel="stylesheet" href="/assets/site.css?v=5">
</head>
<body>
<a class="skip" href="#main">{e(t["skip"])}</a>
<header class="top">
 <div class="wrap top-in">
  <a class="brand" href="{PATH[L]}" aria-label="{e(t["name"])} {VERSION}"><img src="/assets/mark.png" alt="" width="36" height="36"><span>{e(t["name"])}</span></a>
  <nav class="nav" aria-label="{e(t["name"])}"><ul>{"".join(f'<li><a href="#{a}">{e(b)}</a></li>' for a,b in t["nav"])}</ul></nav>
  <div class="tools">
   <div class="lang-picker" data-lang-picker>
    <button class="lang-btn" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="lang-menu" aria-label="{e(t["langs"])}: {e(LNAME[L])}"><span>{e(LNAME[L])}</span><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
    <ul id="lang-menu" class="lang-menu" role="menu" hidden>{"".join(f'<li role="none"><a role="menuitem" href="{PATH[l]}" hreflang="{l}" lang="{l}"' + (' aria-current="page"' if l==L else '') + f'>{LNAME[l]}</a></li>' for l in LANGS)}</ul>
   </div>
   <button class="theme" type="button" aria-label="{e(t["theme"])}" title="{e(t["theme"])}"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9z" fill="currentColor"/></svg></button>
  </div>
 </div>
</header>
<main id="main">
<section class="hero">
 <div class="wrap hero-in">
  <div class="hero-text">
   <p class="ver">{e(t["version"])} {VERSION}</p>
   <h1>{e(t["hero_h"])}</h1>
   <p class="lead">{e(t["hero_p"])}</p>
   <div class="dls">''')
    for key, f, sub, kind in (
        ("dl_chrome", CHROME_FILE, "dl_sub_chrome", "chrome"),
        ("dl_ff", FF_FILE, "dl_sub_ff", "firefox"),
        ("dl_kiwi", KIWI_FILE, "dl_sub_kiwi", "kiwi"),
    ):
        w(f'''
    <div class="dl">
     <a class="btn{' btn-main' if kind=='chrome' else ''}" href="/download/{kind}" download="{f}"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M12 3v11m0 0 4.5-4.5M12 14 7.5 9.5M4 19h16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>{e(t[key])}<small>{e(t[sub])} · {mb(SIZE[f], t)}</small></span></a>
     <div class="sha"><span class="sha-l">{e(t["sha"])}</span><code dir="ltr" translate="no">{SUMS[f]}</code><button type="button" class="copy" data-copy="{SUMS[f]}" data-done="{e(t["copied"])}">{e(t["copy"])}</button></div>
    </div>''')
    w(f'''
   </div>
   <p class="note">{e(t["hero_note"])} <a href="#install">{e(t["how_install"])}</a> · <a href="https://github.com/{REPO}/releases/tag/v{VERSION}">{e(t["all_files"])}</a></p>
  </div>
  <figure class="arch">
   {img(f"/assets/img/ui/ui-popup-main-{sc}.webp", t["hero_alt"], *isize(f"/assets/img/ui/ui-popup-main-{sc}.webp"), eager=True)}
  </figure>
 </div>
</section>

<section id="features" class="sec">
 <div class="wrap">
  <h2>{e(t["f_h"])}</h2>
  <p class="sec-lead">{e(t["f_p"])}</p>''')
    for gname, items in t["groups"]:
        w(f'<h3 class="grp">{e(gname)}</h3><ul class="feats">')
        for a, b in items:
            w(f'<li><h4>{e(a)}</h4><p>{e(b)}</p></li>')
        w('</ul>')
    w(f'''
  <h3 class="grp">{e(t["shots_h"])}</h3>
  <div class="gallery">''')
    for name, cap in t["shots"]:
        p = f"/assets/img/ui/{name}-{sc}.webp"
        W,H = isize(p)
        w(f'<figure class="shot{" tall" if H > W else ""}"><a href="{p}">{img(p, cap, W, H)}</a><figcaption>{e(cap)}</figcaption></figure>')
    w(f'''</div>
  <h3 class="grp">{e(t["demo_h"])}</h3>
  <div class="demo">
   <figure><a href="/assets/img/ui/demo-before-no-blocker.webp">{img("/assets/img/ui/demo-before-no-blocker.webp", t["demo_alt_b"], 1200, 800)}</a><figcaption>{e(t["demo_before"])}</figcaption></figure>
   <figure><a href="/assets/img/ui/demo-after-hajb.webp">{img("/assets/img/ui/demo-after-hajb.webp", t["demo_alt_a"], 1200, 800)}</a><figcaption>{e(t["demo_after"])}</figcaption></figure>
  </div>
 </div>
</section>

<section id="benchmark" class="sec alt">
 <div class="wrap">
  <h2>{e(t["b_h"])}</h2>
  <p class="sec-lead">{e(t["b_p"])}</p>
  <figure class="bars" aria-labelledby="bars-cap">
   <figcaption id="bars-cap">{e(t["b_bars"])}</figcaption>
   <ul>''')
    for (lab, val, cls) in ((t["b_cols"][2], 50, "me"), (t["b_cols"][3], 84, ""), (t["b_cols"][4], 543, ""), (t["b_cols"][1], 2865, "none")):
        w(f'<li class="{cls}"><span class="bl">{e(lab)}</span><span class="bt"><span class="bf" style="--v:{max(val/2865*100,0.9):.2f}%"></span></span><span class="bv">{val}</span></li>')
    w(f'''</ul>
  </figure>
  <div class="tbl"><table>
   <caption>{e(t["b_cap"])}</caption>
   <thead><tr>{"".join(f'<th scope="col"{" class=me" if i==2 else ""}>{e(c)}</th>' for i,c in enumerate(t["b_cols"]))}</tr></thead>
   <tbody>''')
    for row, (n, h, u, a, best, unit) in zip(t["b_rows"], BENCH):
        vals = [n, h, u, a]
        cells = ""
        for i, v in enumerate(vals):
            txt = v + (f" {t[unit]}" if unit else "")
            b = (best is not None and i == best) or (best is None and i == 1)
            cells += f'<td{" class=me" if i==1 else ""}>{"<strong>"+e(txt)+"</strong>" if b else e(txt)}</td>'
        w(f'<tr><th scope="row">{e(row)}</th>{cells}</tr>')
    w(f'''</tbody></table></div>
  <details class="method"><summary>{e(t["b_method_h"])}</summary><ul>{"".join(f"<li>{e(x)}</li>" for x in t["b_method"])}</ul></details>
 </div>
</section>

<section id="privacy" class="sec">
 <div class="wrap">
  <h2>{e(t["p_h"])}</h2>
  <p class="sec-lead">{e(t["p_lead"])}</p>
  <ul class="checks">{"".join(f"<li>{e(x)}</li>" for x in t["p_points"])}</ul>
  <div class="tbl"><table class="perms">
   <caption>{e(t["perm_cap"])}</caption>
   <thead><tr>{"".join(f'<th scope="col">{e(c)}</th>' for c in t["perm_cols"])}</tr></thead>
   <tbody>''')
    for name, kind, why in t["perms"]:
        lab = {"req": t["req"], "opt": t["opt"], "reqff": t["req"]+" "+t["ffonly"], "optff": t["opt"]+" "+t["ffonly"]}[kind]
        w(f'<tr><th scope="row"><code dir="ltr" translate="no">{e(name)}</code></th><td><span class="tag {kind[:3]}">{e(lab)}</span></td><td>{e(why)}</td></tr>')
    w(f'''</tbody></table></div>
 </div>
</section>

<section id="install" class="sec alt">
 <div class="wrap">
  <h2>{e(t["i_h"])}</h2>
  <p class="sec-lead">{e(t["i_lead"])}</p>
  <div class="before"><h3>{e(t["i_before_h"])}</h3><ol>{"".join(f"<li>{x}</li>" for x in t["i_before"])}</ol></div>
  <div class="tabs" data-tabs>
   <div class="tablist" role="tablist" aria-label="{e(t["i_h"])}">{"".join(f'<a role="tab" id="tab-{k}" href="#i-{k}" aria-controls="i-{k}">{e(v)}</a>' for k,v in t["tabs"])}</div>''')
    tabname = dict(t["tabs"])
    def steps(lst, shotlang):
        s = '<ol class="steps">'
        for (h, p, shot) in lst:
            s += f'<li><h4>{e(h)}</h4><p>{p}</p>'
            if shot:
                src = f"/assets/img/install/{shot}{'-'+shotlang if shotlang else ''}.webp"
                W, H = isize(src)
                s += f'<figure class="ishot"><a href="{src}">{img(src, h, W, H)}</a></figure>'
            s += '</li>'
        return s + '</ol>'
    w(f'<section class="panel" id="i-chrome" role="tabpanel" aria-labelledby="tab-chrome"><h3>{e(tabname["chrome"])}</h3>{steps(t["chrome_steps"], SHOTLANG[L])}<p class="fine">{e(t["shot_note_cr"])}</p></section>')
    for k in ("edge", "brave", "opera", "vivaldi"):
        w(f'<section class="panel" id="i-{k}" role="tabpanel" aria-labelledby="tab-{k}"><h3>{e(tabname[k])}</h3><ol class="plain">{"".join(f"<li>{x}</li>" for x in t[k])}</ol><p class="fine">{e(t["similar"])} <a href="#i-chrome">{e(tabname["chrome"])}</a></p></section>')
    w(f'''<section class="panel" id="i-firefox" role="tabpanel" aria-labelledby="tab-firefox"><h3>{e(tabname["firefox"])}</h3>
     <p class="note" role="note">{e(t["ff_note"])}</p>{steps(t["ff_steps"], None)}</section>
    <section class="panel" id="i-android" role="tabpanel" aria-labelledby="tab-android"><h3>{e(tabname["android"])}</h3>
     <p>{e(t["and_lead"])}</p>
     <h4>{e(t["and_kiwi_h"])}</h4>
     <p><a href="/download/kiwi" download="{KIWI_FILE}"><code>{KIWI_FILE}</code></a></p>
     <ol class="plain">{"".join(f"<li>{x}</li>" for x in t["and_kiwi_steps"])}</ol>
     <p class="fine">{e(t["and_kiwi_note"])}</p>
     <h4>{e(t["and_other_h"])}</h4>
     <p>{e(t["and_other"])}</p>
     <h4>{e(t["and_ff_h"])}</h4>
     <p>{e(t["and_ff"])}</p>
     <ol class="plain">{"".join(f"<li>{x}</li>" for x in t["and_ff_steps"])}</ol></section>
    <section class="panel" id="i-update" role="tabpanel" aria-labelledby="tab-update"><h3>{e(tabname["update"])}</h3>
     <h4>{e(t["up_h"])}</h4><ol class="plain">{"".join(f"<li>{x}</li>" for x in t["up"])}</ol>
     <figure class="ishot narrow"><a href="/assets/img/install/chrome-reload-{SHOTLANG[L]}.webp">{img(f"/assets/img/install/chrome-reload-{SHOTLANG[L]}.webp", t["up"][2], *isize(f"/assets/img/install/chrome-reload-{SHOTLANG[L]}.webp"))}</a></figure>
     <h4>{e(t["un_h"])}</h4><ol class="plain">{"".join(f"<li>{x}</li>" for x in t["un"])}</ol>
     <h4>{e(t["verify_h"])}</h4><p>{e(t["verify_p"])}</p>
     <pre dir="ltr" translate="no"><code>Windows:  certutil -hashfile {CHROME_FILE} SHA256
macOS:    shasum -a 256 {CHROME_FILE}
Linux:    sha256sum {CHROME_FILE}</code></pre>
     <p><a href="/download/sha256sums">SHA256SUMS</a></p></section>
  </div>
 </div>
</section>

<section id="faq" class="sec">
 <div class="wrap narrow-w">
  <h2>{e(t["faq_h"])}</h2>
  {"".join(f'<details class="qa"><summary>{e(q)}</summary><p>{a}</p></details>' for q,a in t["faq"])}
 </div>
</section>

<section id="credits" class="sec alt">
 <div class="wrap">
  <h2>{e(t["cr_h"])}</h2>
  <p class="sec-lead">{e(t["cr_p"])}</p>
  <ul class="credits" dir="ltr">{"".join(f'<li><span>{e(n)}</span> <span class="lic">{e(lic)}</span>' + (f' <a href="{u}" rel="noopener">{e(u.split("//")[1].rstrip("/"))}</a>' if u.startswith("http") else "") + '</li>' for n,u,lic in CREDITS)}</ul>
  <p class="fine">{e(t["cr_note"])}</p>
 </div>
</section>
</main>
<footer class="foot">
 <div class="wrap foot-in">
  <p>{e(t["foot"])}</p>
  <p>Hajb {VERSION} · <a href="https://github.com/{REPO}">{e(t["foot_src"])}</a></p>
 </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
''')
    return "".join(out)

for L in LANGS:
    d = os.path.join(OUT, PATH[L].strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(page(L))
print("built")
