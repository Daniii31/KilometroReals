import re
# -*- coding: utf-8 -*-
"""Genera Kilómetro Real en ./dist  ·  python3 build.py"""
import os, shutil, json, html
from fuel import FUELP
from content import KINDS, ARTICLES, GUIDES, BRANDS, TOP10
from models import cars, cost, BODY, TYPE, FUEL, DEFAULTS
from extras import analyses, car_analysis, car_faq
from models import slugify
from vs_pairs import VS_PAIRS as _VSP
from brands_meta import ORIGIN, badge as bbadge
ARTICLES = ARTICLES + analyses()

# ===== CONFIGURACIÓN =====
DOMAIN = "https://kilometroreal.com"
LOGO_SVG = '<svg class="mark" aria-hidden="true" viewBox="0 0 60 90"><defs><clipPath id="kb-{u}"><path d="M0 44V30h60v54a6 6 0 0 1-6 6H6a6 6 0 0 1-6-6z"/></clipPath></defs><path d="M0 30C0 13.4 13.4 0 30 0s30 13.4 30 30z" fill="#F2C314"/><path class="lb" d="M0 30h60v54a6 6 0 0 1-6 6H6a6 6 0 0 1-6-6z" fill="#101D33"/><g fill="#fff" clip-path="url(#kb-{u})"><path d="M22.9 31.5h2.4L7.3 85H3.1z"/><path d="M34.8 31.5h2.4L57 85h-4.3z"/><path d="M28.7 35.4h2.5l1.4 7.1h-5z"/><path d="M28 48.7h4.4l1.7 10.6h-8z"/><path d="M26.5 67.6h7.2l2.5 15.3H23.9z"/></g></svg>'
LOGO_H = LOGO_SVG.replace("{u}", "h")
LOGO_F = LOGO_SVG.replace("{u}", "f")
LOGO_PH = LOGO_SVG.replace("{u}", "p").replace('class="mark"', 'class="phmark"').replace('fill="#101D33"', 'fill="#FFFFFF"').replace('<g fill="#fff"', '<g fill="#101D33"')
OG_DIM = '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
SITE = "Kilómetro Real"
ADSENSE_CLIENT = "ca-pub-8706325038832951"    # "ca-pub-..." cuando Google apruebe
GA_ID = ""
UPDATED = "octubre de 2026"
import hashlib as _h
VERSION = _h.md5((open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.css"), "rb").read() + open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.js"), "rb").read() + open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fuel.py"), "rb").read())).hexdigest()[:8]

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "dist")
IMG_DIR = os.path.join(HERE, "img")
NEWS = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
CARS = cars()
BY = {c["id"]: c for c in CARS}
K = {c["id"]: cost(c) for c in CARS}

def esc(s): return html.escape(str(s), quote=True)
def num(v): return f"{round(v):,}".replace(",", ".")
def eur(v): return num(v) + " €"
def pk(v): return f"{v:.3f}".replace(".", ",")
def dec(v): return str(v).replace(".", ",")
LAB = {"cero": "0", "eco": "ECO", "c": "C"}
def tag(c): return f'<span class="tag {c["lab"]}" title="Etiqueta DGT">{LAB[c["lab"]]}</span>'
def typ(c): return f'<span class="type t-{c["t"]}">{TYPE[c["t"]]}</span>'
def curl(c): return f"/coches/{c['id']}/"
def aurl(a): return f"/noticias/{a['slug']}/"
def gurl(g): return f"/guias/{g['slug']}/"
def kmain(a): return a["k"].split()[0]
def has_img(name): return any(os.path.exists(os.path.join(IMG_DIR, f"{name}.{e}")) for e in ("jpg", "webp"))
def img_tag(name, alt, eager=False):
    for e in ("webp", "jpg"):
        if os.path.exists(os.path.join(IMG_DIR, f"{name}.{e}")):
            load = 'fetchpriority="high"' if eager else 'loading="lazy"'
            cap = "Imagen: prensa de la marca." if name.startswith("prensa-") else ("Imagen: Kilómetro Real." if name.startswith("portada-") else "Imagen ilustrativa generada con IA.")
            srcset = f' srcset="/assets/img/{name}-800.webp 800w, /assets/img/{name}.{e} 1600w" sizes="(max-width: 820px) 94vw, 760px"' if os.path.exists(os.path.join(IMG_DIR, f"{name}-800.webp")) else ""
            return f'<figure style="margin:0"><img src="/assets/img/{name}.{e}"{srcset} alt="{esc(alt)}" {load} decoding="async" width="1600" height="900" style="width:100%;height:auto;border-radius:14px;aspect-ratio:16/9;object-fit:cover"><figcaption class="note" style="margin-top:6px">{cap}</figcaption></figure>'
    return ""
def ad(slot): return f'<div class="ad" data-slot="{slot}"></div>'

# Siluetas simples por carrocería
SIL = {
 "hatch": "M6 58c0-9 6-13 16-15l28-4c12-12 26-19 46-19h34c14 0 24 7 34 19l14 3c9 2 12 8 12 16z",
 "sedan": "M4 58c0-8 5-12 14-13l34-6c14-11 30-17 52-17h28c16 0 30 7 42 17l24 4c9 2 12 7 12 15z",
 "suv": "M6 58c0-12 4-17 14-19l24-4c10-13 24-21 46-21h46c14 0 24 8 32 20l12 3c8 2 10 8 10 21z",
  "coupe": "M4 58c0-7 4-10 12-11l40-7c16-9 32-14 52-14h22c18 0 32 6 46 14l26 5c8 1 10 6 10 13z",
 "van": "M6 58c0-14 4-19 13-21l16-3c8-15 22-24 46-24h64c12 0 18 9 22 22l10 3c7 2 9 8 9 23z",
}
BODY_SIL = {"urbano": "hatch", "compacto": "hatch", "berlina": "sedan", "familiar": "sedan", "suv-p": "suv", "suv-m": "suv", "suv-g": "van", "monovolumen": "van", "deportivo": "coupe"}
def sil(c):
    return (f'<div class="sil"><svg viewBox="0 0 220 72" aria-hidden="true"><path fill="currentColor" d="{SIL[BODY_SIL[c["body"]]]}"/>'
            '<circle cx="56" cy="58" r="13" style="fill:var(--surface)"/><circle cx="56" cy="58" r="9" fill="currentColor"/><circle cx="166" cy="58" r="13" style="fill:var(--surface)"/><circle cx="166" cy="58" r="9" fill="currentColor"/></svg></div>')

NAV = [("/coches/", "Coches", "coches"), ("/mejores/", "Rankings", "mejores"), ("/calculadoras/", "Calculadoras", "calc"),
       ("/cual-me-conviene/", "¿Cuál me conviene?", "finder"), ("/noticias/", "Noticias", "noticias")]

NAV_EN = [("/en/cars/", "Cars", "coches"), ("/en/rankings/", "Rankings", "mejores"), ("/en/calculators/", "Calculators", "calc"),
          ("/en/which-car/", "Which car?", "finder")]
SOCIAL = {}   # p. ej. {"Instagram": "https://instagram.com/kilometroreal"}
ICON = {
 "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
 "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
}
ALT = {}  # ruta ES -> ruta EN (se rellena al construir la versión inglesa)
def en_of(path): return ALT.get(path)
def es_of(path):
    for k, v in ALT.items():
        if v == path: return k
    return None

REVEAL = ['class="sec-head', 'class="cards', 'class="rankgrid', 'class="newslist', 'class="cta', 'class="faq', 'class="guides', 'class="quote', 'class="cgrid', 'class="rank"']
def add_reveal(body):
    for r in REVEAL: body = body.replace(r, r.replace('class="', 'class="reveal '))
    return body

def page(path, title, desc, body, active="", schema=None, noindex=False, full_title=None, lang="es", endcta=True, reading=False, og=None):
    en = lang == "en"
    if len(desc) > 160: desc = desc[:157].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
    ft = full_title or (title if title == SITE or len(title) > 48 else f"{title} | {SITE}")
    alt_en = path if en else en_of(path)
    alt_es = es_of(path) if en else path
    hl = ""
    if alt_en and alt_es:
        hl = f'<link rel="alternate" hreflang="es" href="{DOMAIN}{alt_es}"><link rel="alternate" hreflang="en" href="{DOMAIN}{alt_en}"><link rel="alternate" hreflang="x-default" href="{DOMAIN}{alt_es}">'
    canon = f'<link rel="canonical" href="{DOMAIN}{path}"><meta property="og:url" content="{DOMAIN}{path}">'
    consent = ('<script>window.adsbygoogle=window.adsbygoogle||[];(function(){var c=null;try{c=localStorage.getItem("kr_consent")}catch(e){}'
               'adsbygoogle.pauseAdRequests=c?0:1;adsbygoogle.requestNonPersonalizedAds=c==="all"?0:1;'
               'window.dataLayer=window.dataLayer||[];function g(){dataLayer.push(arguments)}window.gtag=window.gtag||g;'
               'var ok=c==="all"?"granted":"denied";gtag("consent","default",{ad_storage:ok,ad_user_data:ok,ad_personalization:ok,analytics_storage:ok});})()</script>')
    ads = consent + f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>' if ADSENSE_CLIENT else ""
    ga = (f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{GA_ID}");</script><script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>') if GA_ID else ""
    ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ""
    cur = ' aria-current="page"'
    navl = NAV_EN if en else NAV
    home = "/en/" if en else "/"
    sp = "Search a car" if en else "Buscar un coche"
    nav = f'<form class="hsearch" role="search">{ICON["search"]}<input class="carsearch" type="search" list="cars" placeholder="{sp}" aria-label="{sp}"></form>'
    nav += "".join(f'<a href="{h}"{cur if k == active else ""}>{l}</a>' for h, l, k in navl)
    if not en: pass
    cmpurl = "/en/compare/" if en else "/comparador/"
    nav += f'<a class="cta" href="{cmpurl}"{cur if active == "comparador" else ""}>{"Compare cars" if en else "Comparar coches"}</a>'
    other = (alt_es or "/") if en else (alt_en or "/en/")
    langbtn = f'<a class="iconbtn lang" href="{other}" hreflang="{"es" if en else "en"}" lang="{"es" if en else "en"}" title="{"Ver en español" if en else "View in English"}">{"ES" if en else "EN"}</a>'
    actions = (f'<div class="hdr-actions">{langbtn}<button type="button" class="iconbtn theme-btn" aria-label="{"Dark mode" if en else "Modo oscuro"}" title="{"Dark mode" if en else "Modo oscuro"}">{ICON["moon"]}</button>'
               f'<button type="button" class="iconbtn menu-btn" aria-controls="mainnav" aria-expanded="false" aria-label="{"Menu" if en else "Menú"}">{ICON["menu"]}</button></div>')
    social = "".join(f'<a href="{u}" target="_blank" rel="noopener me">{n}</a>' for n, u in SOCIAL.items())
    if en:
        foot = f"""<div><a class="logo" href="/en/">{LOGO_F}{SITE}</a><p class="muted" style="margin-top:10px;max-width:34ch">What every car really costs you, kilometre by kilometre. For buyers in Spain.</p></div>
<div><h4>Tools</h4><a href="/en/compare/">Compare</a><a href="/en/cars/">All cars</a><a href="/en/rankings/">Rankings</a><a href="/en/which-car/">Which car?</a><a href="/en/calculators/">Calculators</a></div>
<div><h4>In Spanish</h4><a href="/noticias/" hreflang="es">Noticias</a><a href="/guias/" hreflang="es">Guías</a><a href="/ayudas/" hreflang="es">Ayudas Plan Auto+</a>{('<h4 style="margin-top:14px">Follow us</h4>' + social) if social else ''}</div>
<div><h4>{SITE}</h4><a href="/en/about/">About us</a><a href="/en/methodology/">How we calculate</a><a href="/en/contact/">Contact</a><a href="/en/terms/">Terms of use</a><a href="/en/privacy/">Privacy</a><a href="/en/cookies/">Cookies</a><a href="/en/cookies/#manage" class="cookie-prefs">Manage cookies</a><a href="/aviso-legal/" hreflang="es">Legal notice (ES)</a></div>
<div class="legal">© 2026 {SITE}. Indicative list prices and consumption figures, updated in October 2026. Always check the current offer with the dealer.</div>"""
    else:
        foot = f"""<div><a class="logo" href="/">{LOGO_F}{SITE}</a><p class="muted" style="margin-top:10px;max-width:34ch">Lo que te cuesta de verdad cada coche, kilómetro a kilómetro. Sin letra pequeña.</p></div>
<div><h4>Herramientas</h4><a href="/comparador/">Comparador</a><a href="/coches/">Todos los coches</a><a href="/marcas/">Marcas</a><a href="/mejores/">Rankings</a><a href="/cual-me-conviene/">¿Cuál me conviene?</a><a href="/calculadoras/">Calculadoras</a><a href="/mi-coche/">¿Cuánto me cuesta mi coche?</a><a href="/comparar/">Comparativas</a><a href="/precio-gasolina-hoy/">Precio gasolina hoy</a></div>
<div><h4>Actualidad</h4><a href="/noticias/">Noticias y análisis</a><a href="/electricos-chinos/">Eléctricos chinos</a><a href="/coches-chinos-comprar-sin-miedo/">¿Coche chino? Guía</a><a href="/ayudas/">Ayudas Plan Auto+</a><a href="/guias/">Guías</a>{('<h4 style="margin-top:14px">Síguenos</h4>' + social) if social else ''}</div>
<div><h4>{SITE}</h4><a href="/quienes-somos/">Quiénes somos</a><a href="/metodologia/">Cómo calculamos</a><a href="/contacto/">Contacto</a><a href="/aviso-legal/">Aviso legal</a><a href="/condiciones-de-uso/">Condiciones de uso</a><a href="/privacidad/">Privacidad</a><a href="/cookies/">Cookies</a><a href="/cookies/#gestionar" class="cookie-prefs">Gestionar cookies</a></div>
<div class="legal">© 2026 {SITE}. Precios de tarifa y consumos orientativos, actualizados en {UPDATED}. Confirma siempre la oferta vigente en el concesionario.</div>"""
    end = ""
    if endcta:
        end = (f'<section class="endcta"><div class="wrap"><div class="cta reveal"><div><h2>{"Torn between two cars?" if en else "¿Dudas entre dos coches?"}</h2>'
               f'<p>{"Compare them in euros per kilometre in 10 seconds." if en else "Compáralos en euros por kilómetro en 10 segundos."}</p></div>'
               f'<a class="btn" href="{cmpurl}">{"Compare now" if en else "Comparar ahora"}</a></div></div></section>')
    doc = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(ft)}</title>
<meta name="description" content="{esc(desc)}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta name="theme-color" content="#ffffff">
<script>document.documentElement.classList.add("js");try{{if(localStorage.getItem("kr_theme")==="dark")document.documentElement.dataset.theme="dark"}}catch(e){{}}</script>
<meta property="og:site_name" content="{SITE}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website">{canon}{hl}
<meta property="og:image" content="{og or DOMAIN + "/assets/img/og.png?v=2"}">{"" if og else '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'}<meta property="og:locale" content="{"en_GB" if en else "es_ES"}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico?v=2" sizes="any"><link rel="icon" href="/favicon.svg?v=2" type="image/svg+xml"><link rel="icon" href="/favicon-32.png?v=2" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2"><link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/data/coches.json" as="fetch" crossorigin><link rel="alternate" type="application/rss+xml" title="{SITE}" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Figtree:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v={VERSION}">
{ads}{ga}{ld}
</head>
<body>
{'<div class="readbar" aria-hidden="true"></div>' if reading else ''}
<a class="skip" href="#contenido">{"Skip to content" if en else "Saltar al contenido"}</a>
<header class="top"><div class="wrap in">
<a class="logo" href="{home}">{LOGO_H}{SITE}</a>
<nav class="main" id="mainnav" aria-label="{"Sections" if en else "Secciones"}">{nav}</nav>
{actions}
</div></header>
<main id="contenido">
{add_reveal(body)}
{end}
</main>
<footer><div class="wrap in">
{foot}
</div></footer>
<button type="button" class="totop" aria-label="{"Back to top" if en else "Volver arriba"}">{ICON["up"]}</button>
<script src="/assets/js/app.js?v={VERSION}" defer></script>
</body>
</html>"""
    if path.endswith(".html"): fn = os.path.join(OUT, path.strip("/"))
    else:
        d = os.path.join(OUT, path.strip("/")); os.makedirs(d, exist_ok=True); fn = os.path.join(d, "index.html")
    with open(fn, "w", encoding="utf-8") as f: f.write(doc)

from urllib.parse import quote
def sharebuttons(path, text, en=False):
    u = DOMAIN + path; t = quote(text); uu = quote(u)
    I = {"wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.8-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.4-.3z"/></svg>',
         "tg": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.9 4.3 18.6 20c-.2 1.1-.9 1.4-1.8.9l-5-3.7-2.4 2.3c-.3.3-.5.5-1 .5l.4-5.1 9.2-8.3c.4-.4-.1-.6-.6-.2L6 13.6 1.1 12c-1.1-.3-1.1-1.1.2-1.6L20.4 3c.9-.3 1.7.2 1.5 1.3z"/></svg>',
         "x": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.8 3h3.1l-6.8 7.8L22 21h-6.2l-4.9-6.4L5.3 21H2.2l7.3-8.3L2 3h6.4l4.4 5.8zm-1.1 16.2h1.7L7.4 4.7H5.6z"/></svg>',
         "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8.5c0-.3.2-.5.5-.5z"/></svg>',
         "ln": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg>'}
    lab = "Share:" if en else "Compartir:"
    return (f'<div class="share-row"><span class="lbl">{lab}</span>'
            f'<a class="sbtn wa" href="https://wa.me/?text={t}%20{uu}" target="_blank" rel="noopener">{I["wa"]}WhatsApp</a>'
            f'<a class="sbtn" href="https://t.me/share/url?url={uu}&text={t}" target="_blank" rel="noopener">{I["tg"]}Telegram</a>'
            f'<a class="sbtn" href="https://twitter.com/intent/tweet?url={uu}&text={t}" target="_blank" rel="noopener">{I["x"]}X</a>'
            f'<a class="sbtn" href="https://www.facebook.com/sharer/sharer.php?u={uu}" target="_blank" rel="noopener">{I["fb"]}Facebook</a>'
            f'<button type="button" class="sbtn copylink" data-url="{u}">{I["ln"]}{"Copy link" if en else "Copiar enlace"}</button></div>')

TESTIMONIALS = []  # solo opiniones reales: [("Texto", "Nombre, ciudad")]
def testimonials_block(en=False):
    if TESTIMONIALS:
        q = "".join(f'<figure class="quote"><p>“{t}”</p><footer>{w}</footer></figure>' for t, w in TESTIMONIALS)
        return f'<section class="tight"><div class="wrap"><div class="sec-head"><div><h2>{"What users say" if en else "Lo que dicen los usuarios"}</h2></div></div><div class="cards">{q}</div></div></section>'
    if en: return ""
    return ('<section class="tight"><div class="wrap"><div class="panel reveal" style="display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap">'
            '<div><h3>¿Te ha servido Kilómetro Real?</h3><p class="muted" style="margin-top:4px">Cuéntanos tu experiencia. Las opiniones reales aparecerán aquí.</p></div>'
            '<a class="btn ghost" href="/contacto/?motivo=opinion">Dejar mi opinión</a></div></div></section>')

ALIASES = {"Tesla Model 3": "tesla-model-3-rwd", "Tesla Model Y": "tesla-model-y-rwd", "BYD Dolphin Surf": "byd-dolphin-surf", "BYD Atto 2": "byd-atto-2",
 "BYD Atto 3": "byd-atto-3", "Seal U DM-i": "byd-seal-u-dm-i", "Leapmotor B10": "leapmotor-b10", "Leapmotor T03": "leapmotor-t03", "Leapmotor C10": "leapmotor-c10",
 "Leapmotor B05": "leapmotor-b05", "Kia EV3": "kia-ev3", "Geely E2": "geely-e2", "Dacia Spring": "dacia-spring", "Renault 5": "renault-5-e-tech",
 "Toyota C-HR+": "toyota-c-hr", "Dacia Sandero": "dacia-sandero-tce", "Fiat 600": "fiat-600-hybrid"}
def autolink(html_body):
    """Enlaza la primera mención de cada modelo a su ficha (fuera de enlaces y etiquetas)."""
    import re as _re
    used = set(); parts = _re.split(r'(<a\b.*?</a>|<[^>]+>)', html_body, flags=_re.S)
    for i, ptxt in enumerate(parts):
        if not ptxt or ptxt.startswith("<"): continue
        for name, cid in sorted(ALIASES.items(), key=lambda x: -len(x[0])):
            if cid in used or cid not in BY: continue
            m = _re.search(r'(?<![\w-])' + _re.escape(name) + r'(?![\w+-])', ptxt)
            if m:
                ptxt = ptxt[:m.start()] + f'<a href="{curl(BY[cid])}">{name}</a>' + ptxt[m.end():]; used.add(cid)
        parts[i] = ptxt
    return "".join(parts)

BRANDS_ALL = sorted({c["b"] for c in CARS})
def build_brands():
    rows = []
    for b in BRANDS_ALL:
        lst = by_pk([c for c in CARS if c["b"] == b]); cheapest = lst[0]
        rows.append(f'<a class="card bcard" href="/marcas/{slugify(b)}/"><div class="bhead">{bbadge(b)}<div><h3>{esc(b)}</h3><span class="muted borig">{ORIGIN.get(b, "")}</span></div></div><p>{len(lst)} modelo{"s" if len(lst) > 1 else ""} · desde {eur(min(c["p"] for c in lst))}</p><div class="foot"><span class="muted" style="font-size:.85rem">Más barato de tener: {esc(cheapest["m"])}</span></div></a>')
    page("/marcas/", "Todas las marcas de coches en España", f"Las {len(BRANDS_ALL)} marcas de coches del comparador: modelos, precios y coste real de cada una.",
         f'{crumbs((None, "Marcas"))}<section class="tight"><div class="wrap"><h1>Marcas</h1><p class="muted" style="margin:10px 0 24px;max-width:62ch">Elige una marca y verás todos sus modelos ordenados por lo que cuestan de verdad.</p><div class="cards">{"".join(rows)}</div></div></section>', "coches")
    for b in BRANDS_ALL:
        lst = by_pk([c for c in CARS if c["b"] == b]); sb = slugify(b)
        news = [a for a in NEWS if b.lower() in (a["t"] + a["body"]).lower()][:6]
        types = sorted({TYPE[c["t"]].lower() for c in lst})
        intro = (f'{b} vende en España {len(lst)} modelo{"s" if len(lst) > 1 else ""} en nuestro comparador, con precios de tarifa desde {eur(min(c["p"] for c in lst))} hasta {eur(max(c["p"] for c in lst))}. '
                 f'Su gama incluye versiones de tipo {", ".join(types)}. El que menos cuesta de tener es el <a href="{curl(lst[0])}">{esc(lst[0]["n"])}</a>, con {pk(K[lst[0]["id"]]["perKm"])} € por kilómetro.')
        body = f"""{crumbs(("/marcas/", "Marcas"), (None, b))}
<section class="tight"><div class="wrap">
 <div class="bhero">{bbadge(b, "lg")}<div><h1>Coches {esc(b)}: precios y coste real</h1><span class="muted">Marca de {ORIGIN.get(b, "")} · {len(lst)} modelo{"s" if len(lst) > 1 else ""}</span></div></div>
 <p style="margin:12px 0 24px;max-width:70ch;color:var(--ink2);font-size:1.05rem">{intro}</p>
 <div class="cards">{"".join(car_card(c) for c in lst)}</div>
 {ad("marca")}
 {('<div class="sec-head" style="margin-top:36px"><div><h2>Noticias de ' + esc(b) + '</h2></div></div><div class="newslist">' + "".join(news_card(a) for a in news) + '</div>') if news else ''}
 <p style="margin-top:28px"><a class="btn" href="/comparador/#{lst[0]["id"]}-vs-{(lst[1] if len(lst) > 1 else by_pk(CARS)[0])["id"]}">Comparar {esc(lst[0]["m"])}</a></p>
</div></section>"""
        ld = {"@context": "https://schema.org", "@type": "ItemList", "name": f"Coches {b}", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": DOMAIN + curl(c), "name": c["n"]} for i, c in enumerate(lst)]}
        page(f"/marcas/{sb}/", f"Coches {b}: precios, modelos y coste real (2026)", f"Todos los coches {b} en venta en España: precio, consumo y lo que cuestan de verdad al mes. Desde {eur(min(c['p'] for c in lst))}.", body, "coches", ld)

def build_feeds():
    from email.utils import format_datetime
    from datetime import datetime, timezone, timedelta
    items = ""
    for a in NEWS[:30]:
        d = datetime.fromisoformat(a["date"]).replace(hour=8, tzinfo=timezone(timedelta(hours=2)))
        items += (f"<item><title>{esc(a['t'])}</title><link>{DOMAIN}{aurl(a)}</link><guid>{DOMAIN}{aurl(a)}</guid>"
                  f"<pubDate>{format_datetime(d)}</pubDate><description>{esc(a['st'])}</description></item>\n")
    rss = (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>{SITE}</title><link>{DOMAIN}/</link>'
           f'<description>Noticias y análisis sobre el coste real de los coches en España</description><language>es-es</language>\n{items}</channel></rss>\n')
    open(os.path.join(OUT, "feed.xml"), "w", encoding="utf-8").write(rss)
    import datetime as _dt
    newest = max(_dt.date.fromisoformat(a["date"]) for a in NEWS)
    recent = [a for a in NEWS if _dt.date.fromisoformat(a["date"]) >= newest - _dt.timedelta(days=2)]
    nm = "".join(f'<url><loc>{DOMAIN}{aurl(a)}</loc><news:news><news:publication><news:name>{SITE}</news:name><news:language>es</news:language></news:publication>'
                 f'<news:publication_date>{a["date"]}</news:publication_date><news:title>{esc(a["t"])}</news:title></news:news></url>\n' for a in recent)
    open(os.path.join(OUT, "news-sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n' + nm + "</urlset>\n")

def crumbs(*items):
    parts = ['<a href="/">Inicio</a>'] + [f'<a href="{h}">{l}</a>' if h else f'<span>{l}</span>' for h, l in items]
    return '<div class="wrap"><nav class="crumbs" aria-label="Ruta">' + " / ".join(parts) + "</nav></div>"

def org(): return {"@type": "Organization", "name": SITE, "url": DOMAIN, "logo": f"{DOMAIN}/assets/img/logo-horizontal.png"}

# ===== piezas =====
def car_card(c, extra=""):
    k = K[c["id"]]
    return (f'<a class="card" href="{curl(c)}">{sil(c)}<div class="meta">{tag(c)}{typ(c)}</div><h3>{esc(c["n"])}</h3>{extra}'
            f'<div class="foot"><span class="price">{eur(c["p"])}</span><span class="perkm"><b>{pk(k["perKm"])} €</b>/km</span></div></a>')

def tl(c):
    return f'{c["trunk"]} L' if c["trunk"] else "Caja de carga"


def thumb(name, alt):
    for e in ("webp", "jpg"):
        if os.path.exists(os.path.join(IMG_DIR, f"{name}.{e}")):
            small = os.path.exists(os.path.join(IMG_DIR, f"{name}-800.webp"))
            src = f"/assets/img/{name}-800.webp" if small else f"/assets/img/{name}.{e}"
            srcset = f' srcset="/assets/img/{name}-800.webp 800w, /assets/img/{name}.{e} 1600w" sizes="(max-width: 700px) 92vw, 400px"' if small else ""
            return f'<img class="thumb" src="{src}"{srcset} alt="{esc(alt)}" width="1600" height="900" loading="lazy" decoding="async">'
    return ""
# ===== portadas automáticas para noticias sin foto =====
def ensure_covers():
    try:
        from figs import FIGS
    except Exception:
        FIGS = {}
    todo = []
    for a in ARTICLES:
        if has_img(a["img"]): continue
        name = "portada-" + a["slug"][:60]
        a["img"] = name
        if has_img(name): continue
        fig = a.get("fig") or FIGS.get(a["slug"], (None, None))[0]
        figl = a.get("figl") or FIGS.get(a["slug"], (None, None))[1]
        if a.get("fig") and not a.get("figl") and FIGS.get(a["slug"], (None,))[0] != a.get("fig"): figl = figl if a["slug"] in FIGS else ""
        todo.append({"name": name, "kicker": KINDS[kmain(a)], "kind": kmain(a), "title": a["t"], "fig": fig, "figl": figl})
    if not todo: return
    import subprocess, tempfile
    from PIL import Image
    tf = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False); json.dump(todo, tf, ensure_ascii=False); tf.close()
    subprocess.run(["node", os.path.join(HERE, "covers.mjs"), tf.name], check=True)
    for c in todo:
        png = os.path.join(IMG_DIR, c["name"] + ".png"); im = Image.open(png).convert("RGB")
        im.save(os.path.join(IMG_DIR, c["name"] + ".webp"), "WEBP", quality=80, method=6)
        im.resize((800, 450), Image.LANCZOS).save(os.path.join(IMG_DIR, c["name"] + "-800.webp"), "WEBP", quality=78, method=6)
        os.remove(png)

def news_card(a):
    k = kmain(a)
    th = thumb(a["img"], a["t"]) or f'<div class="thumb ph ph-{k}" aria-hidden="true">{LOGO_PH}</div>'
    return (f'<a class="card" href="{aurl(a)}">{th}<span class="kicker">{KINDS[k]}</span><h3>{a["t"]}</h3><p>{a["st"]}</p>'
            f'<div class="foot"><span class="muted" style="font-size:.85rem">{a["dtxt"]} · {a["min"]} min</span></div></a>')

def guide_card(g):
    return f'<a class="card" href="{gurl(g)}">{thumb(g["img"], g["t"])}<span class="kicker">Guía</span><h3>{g["t"]}</h3><p>{g["st"]}</p></a>'

def rank_li(c, right=None, sub=None):
    k = K[c["id"]]
    right = right or f'<span class="num">{pk(k["perKm"])} €/km</span>'
    sub = sub or f'{TYPE[c["t"]]} · {eur(c["p"])} · {eur(k["month"])}/mes'
    return f'<li><span><a href="{curl(c)}">{esc(c["n"])}</a><span class="sub">{sub}</span></span>{right}</li>'

def by_pk(lst): return sorted(lst, key=lambda c: K[c["id"]]["perKm"])

RANKINGS = [
 ("mas-baratos-por-km", "Los coches más baratos de tener", "Ordenados por coste real por kilómetro: compra, pérdida de valor, energía, seguro, taller e impuestos.", lambda: by_pk(CARS)[:25], None),
 ("electricos-mas-baratos", "Los eléctricos más baratos de tener", "Los coches eléctricos con menor coste real por kilómetro, cargando sobre todo en casa.", lambda: by_pk([c for c in CARS if c["t"] == "ev"])[:25], None),
 ("suv-mas-baratos", "Los SUV más baratos de tener", "SUV pequeños, medianos y grandes ordenados por lo que cuestan de verdad cada kilómetro.", lambda: by_pk([c for c in CARS if c["body"].startswith("suv")])[:25], None),
 ("hibridos-mas-economicos", "Los híbridos más económicos", "Híbridos e híbridos enchufables con menor coste real: la opción para quien no quiere depender del enchufe.", lambda: by_pk([c for c in CARS if c["t"] in ("hev", "phev")])[:25], None),
 ("electricos-mas-autonomia", "Los eléctricos con más autonomía", "Ordenados por autonomía homologada WLTP. En autopista y con frío, cuenta con bastante menos.", lambda: sorted([c for c in CARS if c["t"] == "ev"], key=lambda c: -c["rng"])[:25], lambda c: f'<span class="num">{c["rng"]} km</span>'),
 ("etiqueta-cero-menos-30000", "Coches con etiqueta CERO por menos de 30.000 €", "Eléctricos e híbridos enchufables con precio de tarifa por debajo de 30.000 €, antes de ayudas.", lambda: by_pk([c for c in CARS if c["lab"] == "cero" and c["p"] <= 30000]), None),
 ("coches-chinos-mas-baratos", "Los coches chinos más baratos de tener", "MG, BYD, Omoda, Jaecoo, Leapmotor, Geely y el resto de marcas chinas, ordenadas por coste real por kilómetro.", lambda: by_pk([c for c in CARS if c["cn"]])[:25], None),
 ("familiares-y-7-plazas", "Familiares, monovolúmenes y SUV de 7 plazas", "Los coches con más espacio ordenados por coste real. Junto a cada uno, su maletero.", lambda: by_pk([c for c in CARS if c["body"] in ("familiar", "suv-g", "monovolumen") or c["trunk"] >= 580]), lambda c: f'<span class="num">{pk(K[c["id"]]["perKm"])} €/km · {tl(c)}</span>'),
 ("coches-menos-de-15000-euros", "Los mejores coches por menos de 15.000 €", "Coches nuevos con precio de tarifa de hasta 15.000 €, ordenados por lo que cuestan de verdad cada kilómetro: compra, pérdida de valor, energía, seguro, taller e impuesto.", lambda n=15000: by_pk([c for c in CARS if c["p"] <= n])[:30], lambda c: f'<span class="num">{pk(K[c["id"]]["perKm"])} €/km · {eur(c["p"])}</span>'),
 ("coches-menos-de-20000-euros", "Los mejores coches por menos de 20.000 €", "Coches nuevos con precio de tarifa de hasta 20.000 €, ordenados por lo que cuestan de verdad cada kilómetro: compra, pérdida de valor, energía, seguro, taller e impuesto.", lambda n=20000: by_pk([c for c in CARS if c["p"] <= n])[:30], lambda c: f'<span class="num">{pk(K[c["id"]]["perKm"])} €/km · {eur(c["p"])}</span>'),
 ("coches-menos-de-25000-euros", "Los mejores coches por menos de 25.000 €", "Coches nuevos con precio de tarifa de hasta 25.000 €, ordenados por lo que cuestan de verdad cada kilómetro: compra, pérdida de valor, energía, seguro, taller e impuesto.", lambda n=25000: by_pk([c for c in CARS if c["p"] <= n])[:30], lambda c: f'<span class="num">{pk(K[c["id"]]["perKm"])} €/km · {eur(c["p"])}</span>'),
 ("coches-menos-de-30000-euros", "Los mejores coches por menos de 30.000 €", "Coches nuevos con precio de tarifa de hasta 30.000 €, ordenados por lo que cuestan de verdad cada kilómetro: compra, pérdida de valor, energía, seguro, taller e impuesto.", lambda n=30000: by_pk([c for c in CARS if c["p"] <= n])[:30], lambda c: f'<span class="num">{pk(K[c["id"]]["perKm"])} €/km · {eur(c["p"])}</span>'),
 ("deportivos-mas-baratos", "Los deportivos más baratos de mantener", "GTI, RS, M, AMG y GR: los coches más prestacionales ordenados por lo que cuestan de verdad cada kilómetro, con su potencia.", lambda: by_pk([c for c in CARS if (c["cv"] >= 250 and c["t"] in ("ice", "mhev")) or c["body"] == "deportivo" or (c["cv"] >= 450 and not c["body"].startswith("suv"))])[:30], lambda c: f'<span class="num">{pk(K[c["id"]]["perKm"])} €/km · {c["cv"]} CV</span>'),
]

POP_PAIRS = [("dacia-spring", "hyundai-i10"), ("tesla-model-3-rwd", "toyota-corolla-hybrid"), ("byd-dolphin-surf", "seat-ibiza-1-0-tsi"),
             ("geely-e2", "renault-clio-e-tech"), ("tesla-model-y-rwd", "toyota-rav4-hybrid"), ("leapmotor-b10", "dacia-duster-hybrid"),
             ("kia-ev3", "volkswagen-t-roc-1-5-tsi"), ("byd-seal-u-dm-i", "hyundai-tucson-hibrido"), ("renault-5-e-tech", "peugeot-208-hybrid-110"),
             ("mg-4-electric", "seat-leon-1-5-tsi"), ("skoda-elroq", "skoda-karoq-1-5-tsi"), ("dacia-sandero-eco-g-glp", "dacia-sandero-tce"),
             ("volkswagen-golf-gti", "cupra-leon-vz-2-0-tsi"), ("bmw-m3-competition", "mercedes-amg-c-63-s-e-performance"), ("audi-rs-3-sportback", "mercedes-amg-a-45-s-4matic")]

def match_card(a, b):
    A, B = BY[a], BY[b]
    ka, kb = K[a], K[b]
    w, l = (A, B) if ka["total"] <= kb["total"] else (B, A)
    d = abs(ka["total"] - kb["total"])
    return (f'<a class="card" href="/comparador/#{a}-vs-{b}"><div class="match"><span class="who">{esc(A["n"])}</span><span class="num">{pk(ka["perKm"])} €/km</span>'
            f'<span class="who">{esc(B["n"])}</span><span class="num">{pk(kb["perKm"])} €/km</span>'
            f'<span class="save">El {esc(w["n"])} ahorra {eur(d)} en 5 años</span></div></a>')

# ===== páginas =====
def build_home():
    quick = "".join(f'<button type="button" class="chip" data-pair="{a}|{b}">{esc(BY[a]["n"])} vs {esc(BY[b]["n"])}</button>' for a, b in POP_PAIRS[:4])
    cheapest = by_pk(CARS)[:6]; evs = by_pk([c for c in CARS if c["t"] == "ev"])[:6]; suvs = by_pk([c for c in CARS if c["body"].startswith("suv")])[:6]
    panel = lambda t, slug, lst: f'<div class="panel"><h3>{t}</h3><ol class="rank">{"".join(rank_li(c) for c in lst)}</ol><p style="margin-top:12px"><a href="/mejores/{slug}/" style="font-weight:700;text-decoration:none">Ver los 25 →</a></p></div>'
    body = f"""
<section class="hero"><div class="wrap grid">
 <div>
  <h1>¿Cuánto te cuesta <em>de verdad</em> tu próximo coche?</h1>
  <p class="lead">El precio es solo el principio. Sumamos lo que pierde de valor, la gasolina o la luz, el seguro, el taller y el impuesto. Y te lo damos en euros por kilómetro.</p>
  <div class="proof"><span><b>{len(CARS)}</b>modelos en venta</span><span><b>5</b>gastos sumados</span><span><b>10 s</b>para comparar</span></div>
  <div class="road" aria-hidden="true"><svg class="carmini" viewBox="0 0 220 72"><path fill="currentColor" d="M6 58c0-9 6-13 16-15l28-4c12-12 26-19 46-19h34c14 0 24 7 34 19l14 3c9 2 12 8 12 16z"/><circle cx="56" cy="58" r="11" fill="#0d1726"/><circle cx="166" cy="58" r="11" fill="#0d1726"/></svg></div>
 </div>
 <form class="tool needs-js" id="duel" autocomplete="off">
  <div class="pair">
   <div><label class="lbl" for="qa">Coche A</label><input type="text" id="qa" list="cars" value="{esc(BY['dacia-spring']['n'])}" placeholder="Escribe un modelo"></div>
   <div class="vs">VS</div>
   <div><label class="lbl" for="qb">Coche B</label><input type="text" id="qb" list="cars" value="{esc(BY['hyundai-i10']['n'])}" placeholder="Escribe otro"></div>
  </div>
  <div id="duelres" aria-live="polite"><div class="skel" aria-hidden="true"><i></i><i class="s"></i></div></div>
  <div class="quick"><p class="muted">Prueba con:</p><div class="chips">{quick}</div></div>
 </form>
</div></section>
{ad("portada-1")}
<section><div class="wrap">
 <div class="sec-head"><div><h2>Duelos que sorprenden</h2><p>Con 15.000 km al año durante 5 años. Pulsa cualquiera para cambiar los números a tu medida.</p></div><a href="/comparador/">Abrir comparador →</a></div>
 <div class="cards c3">{"".join(match_card(a, b) for a, b in POP_PAIRS[4:10])}</div>
</div></section>
<section class="tight"><div class="wrap"><div class="cta mc-cta"><div><h2>¿Cuánto te cuesta tu coche al mes?</h2><p>Elige el tuyo y te decimos lo que pagas de verdad, y con qué coche parecido ahorrarías.</p></div><a class="btn" href="/mi-coche/">Calcular el mío</a></div></div></section>
<section class="tight"><div class="wrap">
 <div class="sec-head"><div><h2>Calculadoras</h2><p>Las cuentas que todo conductor se hace alguna vez, resueltas en segundos.</p></div><a href="/calculadoras/">Todas →</a></div>
 <div class="cards c5">{"".join(f'<a class="card calc-card" href="/calculadoras/{x[0]}/"><span class="badge">{x[2]}</span><h3>{x[1]}</h3></a>' for x in CALCS)}</div>
</div></section>
<section class="band"><div class="wrap">
 <div class="sec-head"><div><h2>Rankings</h2><p>Los coches que menos te cuestan cada kilómetro, por categoría.</p></div><a href="/mejores/">Todos los rankings →</a></div>
 <div class="rankgrid">{panel("Más baratos de tener", "mas-baratos-por-km", cheapest)}{panel("Eléctricos", "electricos-mas-baratos", evs)}{panel("SUV", "suv-mas-baratos", suvs)}</div>
</div></section>
<section class="tight"><div class="wrap"><div class="panel promo">
 <div><h2>¿Te da miedo comprar un coche chino?</h2><p class="muted" style="margin-top:8px;max-width:62ch">MG, Omoda, Jaecoo o BYD son más baratos, pero ¿son fiables? Seguridad, garantía, talleres y reventa explicados con datos, y cuáles salen más baratos que su rival de siempre.</p></div>
 <a class="btn" href="/coches-chinos-comprar-sin-miedo/">Leer la guía</a></div></div></section>
<section><div class="wrap"><div class="cta"><div><h2>¿No sabes cuál elegir?</h2><p>Responde 4 preguntas y te decimos los 3 coches que menos te van a costar a ti.</p></div><a class="btn" href="/cual-me-conviene/">Empezar el test</a></div></div></section>
{ad("portada-2")}
<section class="tight"><div class="wrap">
 <div class="sec-head"><div><h2>Análisis y noticias</h2></div><a href="/noticias/">Todas →</a></div>
 <div class="newslist">{"".join(news_card(a) for a in NEWS[:6])}</div>
</div></section>
{testimonials_block()}
<section class="tight"><div class="wrap">
 <div class="sec-head"><div><h2>Guías para decidir</h2></div><a href="/guias/">Todas →</a></div>
 <div class="newslist">{"".join(guide_card(g) for g in GUIDES[:3])}</div>
</div></section>"""
    page("/", SITE, f"Compara el coste real de {len(CARS)} coches en venta en España: eléctricos, híbridos y gasolina. Euros por kilómetro, al mes y en 5 años.", body, "",
         {"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": DOMAIN, "inLanguage": "es-ES"},
         full_title=f"{SITE}: lo que te cuesta de verdad cada coche", endcta=False)

def build_comparador():
    pop = "".join(f'<li><span><a href="#{a}-vs-{b}">{esc(BY[a]["n"])} vs {esc(BY[b]["n"])}</a></span></li>' for a, b in POP_PAIRS)
    body = f"""{crumbs((None, "Comparador"))}
<section class="tight" id="comparador"><div class="wrap">
 <h1>Comparador de coste real</h1>
 <p class="muted" style="margin:10px 0 24px;max-width:62ch">Elige dos coches y ajusta tus kilómetros. Te decimos cuál te sale más barato y por qué.</p>
 <div class="cmp">
  <div style="min-width:0">
   <div class="tool needs-js">
    <div class="pair">
     <div><label class="lbl" for="ca">Coche A</label><input type="text" id="ca" list="cars" autocomplete="off"></div>
     <button type="button" class="btn ghost" id="swap" aria-label="Intercambiar coches" style="padding:12px 14px">⇄</button>
     <div><label class="lbl" for="cb">Coche B</label><input type="text" id="cb" list="cars" autocomplete="off"></div>
    </div>
    <div id="cres" aria-live="polite"><div class="skel" aria-hidden="true"><i></i><i class="s"></i></div></div>
    <p style="margin-top:12px;display:flex;gap:10px;align-items:center;flex-wrap:wrap"><button type="button" class="btn ghost" id="share">Copiar enlace de esta comparativa</button><span class="muted" id="sharemsg" style="font-size:.9rem"></span></p>
   </div>
   {ad("comparador-1")}
   <div class="panel" style="margin-top:22px"><h3>En qué se va el dinero</h3><div class="breakdown" id="cbars" style="margin-top:12px"></div>
    <div class="legend"><span><i class="c-dep"></i>Pérdida de valor</span><span><i class="c-energy"></i>Energía</span><span><i class="c-ins"></i>Seguro</span><span><i class="c-mnt"></i>Mantenimiento</span><span><i class="c-tax"></i>Impuesto</span></div></div>
   <div class="panel" style="margin-top:22px;overflow-x:auto"><h3>Cara a cara</h3><table class="specs" id="cspecs" style="margin-top:8px"></table><p class="note" style="margin-top:8px">En verde, el mejor de los dos en cada dato.</p></div>
  </div>
  <aside class="settings">
   <div class="panel">
    <h3 style="margin-bottom:14px">Tu uso</h3>
    <div class="settings">
     <div><label class="lbl" for="s-km">Km al año <span class="pval" id="v-km"></span></label><input type="range" id="s-km" min="5000" max="40000" step="1000"></div>
     <div><label class="lbl" for="s-y">Años que lo tendrás <span class="pval" id="v-y"></span></label><input type="range" id="s-y" min="2" max="10" step="1"></div>
     <div><label class="lbl" for="s-home">Carga en casa <span class="pval" id="v-home"></span></label><input type="range" id="s-home" min="0" max="100" step="5"></div>
     <div class="row"><div><label class="lbl" for="s-gas">Gasolina €/L</label><input type="number" id="s-gas" step="0.01" inputmode="decimal"></div><div><label class="lbl" for="s-die">Diésel €/L</label><input type="number" id="s-die" step="0.01" inputmode="decimal"></div></div>
     <div class="row"><div><label class="lbl" for="s-ph">Luz casa €/kWh</label><input type="number" id="s-ph" step="0.01" inputmode="decimal"></div><div><label class="lbl" for="s-pp">Carga pública €/kWh</label><input type="number" id="s-pp" step="0.01" inputmode="decimal"></div></div>
     <div class="row"><div><label class="lbl" for="s-glp">GLP €/L</label><input type="number" id="s-glp" step="0.01" inputmode="decimal"></div></div>
    </div>
   </div>
   <div class="panel hide"><h3>Tus últimas comparativas</h3><p class="note">Se guardan solo en tu navegador.</p><div class="recent" id="crecent" style="margin-top:8px"></div></div>
   <div class="panel"><h3>Rivales del coche A</h3><p class="note">Misma carrocería, ordenados por coste real. Pulsa para compararlo.</p><ol class="rank" id="crivals" style="margin-top:6px"></ol></div>
   {ad("comparador-lateral")}
  </aside>
 </div>
</div></section>
<section class="band tight"><div class="wrap two">
 <div class="panel"><h3>Comparativas populares</h3><ol class="rank">{pop}</ol></div>
 <div class="panel"><h3>Cómo calculamos</h3><div class="body" style="font-size:.98rem">
  <ul><li><strong>Pérdida de valor:</strong> precio menos lo que vale al venderlo, según la depreciación media de la marca y la tecnología.</li>
  <li><strong>Energía:</strong> consumo real medio por tus kilómetros. Los enchufables cargados en casa hacen parte de sus kilómetros en eléctrico.</li>
  <li><strong>Seguro:</strong> terceros ampliado, conductor de 35 años.</li>
  <li><strong>Mantenimiento e impuesto:</strong> revisiones, neumáticos y el impuesto de circulación medio. Muchos ayuntamientos bonifican el 75 % a los eléctricos.</li></ul>
  <p class="note">Precios de tarifa de acceso sin descuentos ni ayudas, actualizados en {UPDATED}. Orientativos.</p></div></div>
</div></section>"""
    page("/comparador/", "Comparador de coste real de coches", f"Compara dos coches y descubre cuál te sale más barato de verdad. {len(CARS)} modelos: eléctricos, híbridos, gasolina y diésel.", body, "comparador",
         {"@context": "https://schema.org", "@type": "WebApplication", "name": "Comparador de coste real", "applicationCategory": "FinanceApplication", "operatingSystem": "Web", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}, endcta=False)

def build_catalog():
    rows = []
    for c in by_pk(CARS):
        k = K[c["id"]]
        rng = f'{c["rng"]} km' if c["t"] in ("ev", "phev") else "—"
        rows.append(f'<tr data-n="{esc(c["n"].lower())}" data-t="{c["t"]}" data-body="{c["body"]}" data-p="{c["p"]}" data-pk="{k["perKm"]:.4f}" data-mo="{k["month"]:.0f}" data-name="{esc(c["n"])}" data-rng="{c["rng"]}" data-cv="{c["cv"]}" data-trunk="{c["trunk"]}">'
                    f'<td><a href="{curl(c)}">{esc(c["n"])}</a></td><td>{tag(c)}</td><td>{typ(c)}</td><td>{BODY[c["body"]]}</td>'
                    f'<td class="n">{eur(c["p"])}</td><td class="n"><b>{pk(k["perKm"])}</b></td><td class="n">{eur(k["month"])}</td><td class="n">{rng}</td><td class="n">{c["cv"]}</td><td class="n">{tl(c)}</td></tr>')
    topt = "".join(f'<option value="{k}">{v}</option>' for k, v in TYPE.items())
    bopt = "".join(f'<option value="{k}">{v}</option>' for k, v in BODY.items())
    th = lambda k, l, n="": f'<th class="{n}"><button type="button" data-k="{k}">{l} ↕</button></th>'
    body = f"""{crumbs((None, "Coches"))}
<section class="tight"><div class="wrap">
 <h1>Todos los coches</h1>
 <p class="muted" style="margin:10px 0 22px;max-width:64ch">{len(CARS)} modelos en venta en España, ordenados por lo que cuestan de verdad cada kilómetro. Filtra, ordena y entra en la ficha de cada uno. También puedes verlos <a href="/marcas/">por marca</a>.</p>
 <div class="filters">
  <div class="q"><label class="lbl" for="f-q">Buscar</label><input type="search" id="f-q" placeholder="Marca o modelo"></div>
  <div><label class="lbl" for="f-t">Tecnología</label><select id="f-t"><option value="">Todas</option>{topt}</select></div>
  <div><label class="lbl" for="f-b">Carrocería</label><select id="f-b"><option value="">Todas</option>{bopt}</select></div>
  <div><label class="lbl" for="f-p">Precio máximo</label><select id="f-p"><option value="">Sin límite</option><option value="20000">20.000 €</option><option value="25000">25.000 €</option><option value="30000">30.000 €</option><option value="40000">40.000 €</option><option value="50000">50.000 €</option></select></div>
 </div>
 <div id="f-brand"></div>
 <p class="count" id="f-count">{len(CARS)} modelos</p>
 <div class="tablewrap" id="catalogo"><table class="list"><thead><tr>{th("name","Modelo")}<th>Etiqueta</th><th>Tecnología</th><th>Carrocería</th>{th("p","Precio","n")}{th("pk","€/km","n")}{th("mo","Al mes","n")}{th("rng","Autonomía","n")}{th("cv","CV","n")}{th("trunk","Maletero","n")}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>
 <p class="note" style="margin-top:10px">Coste con 15.000 km al año durante 5 años. Precios de tarifa orientativos sin descuentos.</p>
</div></section>
<template id="kr-brands">{"".join(f'<a class="bbanner" data-b="{esc(b.lower())}" href="/marcas/{slugify(b)}/">{bbadge(b, "lg")}<span><b>{esc(b)}</b><span class="muted">Marca de {ORIGIN.get(b, "")} · {sum(1 for c in CARS if c["b"] == b)} modelos</span></span><span class="bgo">Ver la marca →</span></a>' for b in BRANDS_ALL)}</template>"""
    page("/coches/", "Todos los coches en venta y su coste real", f"Catálogo de {len(CARS)} coches nuevos en España con precio, coste por kilómetro, coste al mes, autonomía, potencia y maletero.", body, "coches")

def build_car(c):
    k = K[c["id"]]
    faq = car_faq(c)
    rivals = sorted([x for x in CARS if x["body"] == c["body"] and x["id"] != c["id"]], key=lambda x: abs(x["p"] - c["p"]))[:6]
    cheaper_rivals = by_pk(rivals)
    mx = k["total"]
    segs = "".join(f'<span class="{cl}" style="width:{k[x]/mx*100:.1f}%"></span>' for x, cl in [("dep", "c-dep"), ("energy", "c-energy"), ("ins", "c-ins"), ("mnt", "c-mnt"), ("tax", "c-tax")])
    plugin = c["t"] in ("ev", "phev")
    consumo = f'{dec(c["c"])} {"kWh" if c["t"] == "ev" else "L"}/100 km' + (" en modo híbrido" if c["t"] == "phev" else "")
    specs = [("Precio de tarifa", eur(c["p"])), ("Tecnología", TYPE[c["t"]]), ("Combustible", FUEL[c["f"]] + (" y electricidad" if c["t"] == "phev" else "")),
             ("Carrocería", BODY[c["body"]]), ("Potencia", f'{c["cv"]} CV'), ("Consumo real estimado", consumo), ("Maletero", tl(c)),
             ("Etiqueta DGT", {"cero": "CERO", "eco": "ECO", "c": "C"}[c["lab"]])]
    if c["t"] == "ev": specs[5:5] = [("Batería", f'{c["bat"]} kWh'), ("Autonomía WLTP", f'{c["rng"]} km')]
    if c["t"] == "phev": specs[5:5] = [("Batería", f'{c["bat"]} kWh'), ("Autonomía eléctrica WLTP", f'{c["rng"]} km')]
    _pr = {"g": FUELP["g95"], "d": FUELP["die"], "glp": FUELP["glp"]}
    if c["t"] == "ev": _c100 = c["c"] * DEFAULTS["ph"]
    else: _c100 = c["c"] * _pr.get(c["f"], FUELP["g95"])
    specs.append(("Energía cada 100 km", f'{_c100:.2f} €'.replace(".", ",") + (" (cargando en casa)" if c["t"] == "ev" else " (precio de hoy)")))
    specs.append(("Seguro estimado al año", f'{eur(round(c["ins"]*1.55, -1))} a los 25 años · {eur(round(c["ins"], -1))} a los 35 · {eur(round(c["ins"]*0.88, -1))} a los 50'))
    plan = ""
    if c["lab"] == "cero":
        plan = (f'<div class="panel"><h3>Ayudas Plan Auto+</h3><p style="margin-top:6px">{"Con un precio por debajo de 45.000 € sin IVA, " if c["p"] <= 54450 else ""}'
                + ("puede optar al Plan Auto+, con hasta 4.500 € de ayuda estatal más el descuento del concesionario. " if c["p"] <= 54450 else "su precio supera el límite de 45.000 € sin IVA del Plan Auto+. ")
                + ("Al fabricarse fuera de Europa, la ayuda puede ser menor. " if c["cn"] else "")
                + '</p><p style="margin-top:8px"><a href="/ayudas/">Cómo funcionan las ayudas →</a></p></div>')
    best_rival = cheaper_rivals[0] if cheaper_rivals else None
    _byid = {x["id"]: x for x in CARS}
    _vs = [(a, b) for a, b in _VSP if c["id"] in (a, b) and a in _byid and b in _byid][:6]
    vs_html = ('<div class="vschips"><b>Comparativas cara a cara:</b> ' + " ".join(f'<a class="chip" href="/comparar/{a}-vs-{b}/">{esc(_byid[b if a == c["id"] else a]["n"])}</a>' for a, b in _vs) + '</div>') if _vs else ""
    lead = f'Tenerlo 5 años y hacer 15.000 km al año te cuesta unos <strong>{eur(k["month"])} al mes</strong>, sumando todo.'
    calc_home = '<div><label class="lbl" for="cc-in-home">Carga en casa <span class="pval" id="cc-home"></span></label><input type="range" id="cc-in-home" min="0" max="100" step="5" value="80"></div>' if plugin else ""
    rv = "".join(car_card(x, f'<p>{"Te ahorra" if K[x["id"]]["total"] < k["total"] else "Cuesta"} {eur(abs(K[x["id"]]["total"]-k["total"]))} {"" if K[x["id"]]["total"] < k["total"] else "más "}en 5 años</p>') for x in cheaper_rivals)
    body = f"""{crumbs(("/coches/", "Coches"), (None, c["n"]))}
<div class="wrap carhead">
 <div>
  <span class="eyebrow">{BODY[c["body"]]} · {TYPE[c["t"]]}</span>
  <h1 style="margin-top:10px">{esc(c["n"])}</h1>
  <div style="display:flex;gap:8px;align-items:center;margin-top:12px;flex-wrap:wrap">{tag(c)}<span class="muted">Etiqueta {({"cero": "CERO", "eco": "ECO", "c": "C"})[c["lab"]]}</span><span class="muted">·</span><a class="blink" href="/marcas/{slugify(c["b"])}/">{bbadge(c["b"], "sm")}Todos los {esc(c["b"])}</a></div>
  <p style="font-size:1.12rem;margin-top:14px;color:var(--ink2)">{lead}</p>
  <div class="bigfig">
   <div><b>{pk(k["perKm"])} €</b><span>por kilómetro</span></div>
   <div><b>{eur(k["month"])}</b><span>al mes</span></div>
   <div><b>{eur(k["total"])}</b><span>en 5 años</span></div>
  </div>
  <div class="sharebar"><a class="btn" href="/comparador/#{c["id"]}-vs-{(cheaper_rivals[0] if cheaper_rivals else c)["id"]}">Comparar con otro coche</a></div>
  <div style="margin-top:14px">{sharebuttons(curl(c), f"El {c['n']} cuesta de verdad {eur(k['month'])} al mes. Míralo:")}</div>
 </div>
 <div class="panel" id="carcalc" data-id="{c["id"]}">
  {sil(c).replace('class="sil"', 'class="sil" style="height:90px;justify-content:center"')}
  <h3 style="margin-top:10px">Calcúlalo con tu uso</h3>
  <div class="settings" style="margin-top:12px">
   <div><label class="lbl" for="cc-in-km">Km al año <span class="pval" id="cc-km">15.000</span></label><input type="range" id="cc-in-km" min="5000" max="40000" step="1000" value="15000"></div>
   {calc_home}
  </div>
  <div class="bigfig" style="grid-template-columns:repeat(3,minmax(0,1fr))"><div><b id="cc-pk">{pk(k["perKm"])} €</b><span>por km</span></div><div><b id="cc-mo">{eur(k["month"])}</b><span>al mes</span></div><div><b id="cc-tot">{eur(k["total"])}</b><span>5 años</span></div></div>
 </div>
</div>
{ad("ficha-1")}
<section class="tight"><div class="wrap two">
 <div class="panel"><h3>En qué se va el dinero en 5 años</h3><div class="bar" style="margin-top:14px;height:18px">{segs}</div>
  <table class="specs" style="margin-top:12px"><tbody>
   <tr><th><i class="c-dep" style="display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px"></i>Pérdida de valor</th><td>{eur(k["dep"])}</td></tr>
   <tr><th><i class="c-energy" style="display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px"></i>{"Electricidad" if c["t"] == "ev" else "Energía"}</th><td>{eur(k["energy"])}</td></tr>
   <tr><th><i class="c-ins" style="display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px"></i>Seguro</th><td>{eur(k["ins"])}</td></tr>
   <tr><th><i class="c-mnt" style="display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px"></i>Mantenimiento</th><td>{eur(k["mnt"])}</td></tr>
   <tr><th><i class="c-tax" style="display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px"></i>Impuesto de circulación</th><td>{eur(k["tax"])}</td></tr>
  </tbody></table>
  <p class="note" style="margin-top:10px">Lo vendes por unos {eur(k["resid"])} a los 5 años.</p></div>
 <div style="display:grid;gap:24px;align-content:start">
  <div class="panel"><h3>Ficha técnica</h3><table class="specs" style="margin-top:6px"><tbody>{"".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in specs)}</tbody></table></div>
  {plan}
 </div>
</div></section>
<section class="tight"><div class="wrap two">
 <div class="article"><h2 style="margin-bottom:12px">Nuestro análisis</h2><div class="body" style="font-size:1.04rem">{car_analysis(c)}</div></div>
 <div><h2 style="margin-bottom:12px">Preguntas frecuentes</h2><div class="faq">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)}</div></div>
</div></section>
<section class="band tight"><div class="wrap">
 <div class="sec-head"><div><h2>Rivales del {esc(c["n"])}</h2><p>{BODY[c["body"]]} de precio parecido, ordenados por coste real.{(" El que menos cuesta: " + esc(best_rival["n"]) + ".") if best_rival else ""}</p></div><a href="/comparador/#{c["id"]}-vs-{(best_rival or c)["id"]}">Comparar →</a></div>
 <div class="cards">{rv}</div>
 {vs_html}
</div></section>
<section class="tight"><div class="wrap"><div class="cta mc-cta"><div><h2>¿Ya tienes un {esc(c["n"])}?</h2><p>Pon tus kilómetros y te decimos cuánto te cuesta al mes de verdad y qué coches te saldrían más baratos.</p></div><a class="btn primary" href="/mi-coche/?coche={c["id"]}">Calcular mi coste</a></div></div></section>
<section class="tight"><div class="wrap"><p class="note">Datos orientativos actualizados en {UPDATED}: precio de tarifa de acceso sin descuentos ni ayudas, consumo real estimado y depreciación media. Confirma la oferta en el concesionario.</p></div></section>"""
    schema = {"@context": "https://schema.org", "@type": "Car", "name": c["n"], "brand": {"@type": "Brand", "name": c["b"]}, "bodyType": BODY[c["body"]],
              "fuelType": FUEL[c["f"]], "vehicleEngine": {"@type": "EngineSpecification", "enginePower": {"@type": "QuantitativeValue", "value": c["cv"], "unitText": "CV"}}}
    faqld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    crumbld = {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": DOMAIN + "/"}, {"@type": "ListItem", "position": 2, "name": "Coches", "item": DOMAIN + "/coches/"}, {"@type": "ListItem", "position": 3, "name": c["n"], "item": DOMAIN + curl(c)}]}
    schema.pop("@context"); schema = {"@context": "https://schema.org", "@graph": [schema, faqld, crumbld]}
    page(curl(c), f'{c["n"]}: coste real al mes y por km', f'¿Cuánto cuesta tener un {c["n"]}? {eur(k["month"])} al mes y {pk(k["perKm"])} €/km sumando compra, energía, seguro, taller e impuestos. Ficha y rivales.', body, "coches", schema)

def build_rankings():
    cards = "".join(f'<a class="card" href="/mejores/{s}/"><span class="kicker">Ranking</span><h3>{t}</h3><p>{d}</p></a>' for s, t, d, _, _ in RANKINGS)
    page("/mejores/", "Rankings de coches por coste real", "Los coches más baratos de tener en España: eléctricos, SUV, híbridos, autonomía, etiqueta CERO y familiares.",
         f'{crumbs((None, "Rankings"))}<section class="tight"><div class="wrap"><h1>Rankings</h1><p class="muted" style="margin:10px 0 24px;max-width:62ch">Ordenamos todos los coches por lo que de verdad importa: lo que te cuestan cada kilómetro.</p><div class="cards">{cards}</div></div></section>', "mejores")
    for s, t, d, fn, right in RANKINGS:
        lst = fn()
        items = "".join(rank_li(c, right(c) if right else None) for c in lst)
        others = "".join(f'<a class="chip" href="/mejores/{s2}/">{t2}</a>' for s2, t2, _, _, _ in RANKINGS if s2 != s)
        body = f"""{crumbs(("/mejores/", "Rankings"), (None, t))}
<section class="tight"><div class="wrap narrow">
 <h1>{t}</h1><p class="muted" style="margin:10px 0 22px">{d} Calculado con 15.000 km al año durante 5 años.</p>
 <div class="panel"><ol class="rank">{items}</ol></div>
 {ad("ranking")}
 <p style="margin-top:20px"><a class="btn" href="/comparador/#{lst[0]["id"]}-vs-{lst[1]["id"] if len(lst) > 1 else lst[0]["id"]}">Comparar el 1.º y el 2.º</a></p>
 <div style="margin-top:18px">{sharebuttons(f"/mejores/{s}/", t)}</div>
 <h2 style="margin:36px 0 14px;font-size:1.3rem">Otros rankings</h2><div class="chips">{others}</div>
</div></section>"""
        page(f"/mejores/{s}/", t, f"{d} Lista actualizada en {UPDATED}.", body, "mejores",
             {"@context": "https://schema.org", "@type": "ItemList", "name": t, "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": DOMAIN + curl(c), "name": c["n"]} for i, c in enumerate(lst)]})

def build_finder():
    def q(key, title, opts, default):
        b = "".join(f'<button type="button" class="opt" data-q="{key}" data-v="{v}" aria-pressed="{str(v == default).lower()}">{l}<small>{s}</small></button>' for v, l, s in opts)
        return f'<div class="q"><h3>{title}</h3><div class="opts">{b}</div></div>'
    body = f"""{crumbs((None, "¿Cuál me conviene?"))}
<section class="tight"><div class="wrap quiz" id="finder">
 <h1>¿Qué coche me conviene?</h1>
 <p class="muted" style="margin:10px 0 28px">Cuatro respuestas y te decimos los tres coches que menos te van a costar a ti. Cambia cualquier respuesta y el resultado se actualiza al momento.</p>
 {q("budget", "1. ¿Cuánto quieres gastar como máximo?", [(20000, "Hasta 20.000 €", "Urbanos y básicos"), (30000, "Hasta 30.000 €", "La mayoría del mercado"), (40000, "Hasta 40.000 €", "Más espacio y equipo"), (999999, "Sin límite", "Todo el mercado")], 30000)}
 {q("km", "2. ¿Cuántos kilómetros haces al año?", [(8000, "Pocos", "Unos 8.000 km"), (15000, "Normal", "Unos 15.000 km"), (25000, "Bastantes", "Unos 25.000 km"), (35000, "Muchísimos", "Más de 30.000 km")], 15000)}
 {q("home", "3. ¿Puedes cargar en casa o en el trabajo?", [("si", "Sí", "Garaje o plaza con enchufe"), ("no", "No", "Dependería de cargadores públicos")], "si")}
 {q("body", "4. ¿Qué tipo de coche buscas?", [("any", "Me da igual", "Lo más barato"), ("urbano", "Pequeño", "Para ciudad"), ("compacto,berlina", "Compacto o berlina", "Para todo"), ("suv-p,suv-m,suv-g", "SUV", "Más alto"), ("familiar,suv-g,monovolumen", "Familiar o 7 plazas", "Mucho maletero"), ("deportivo", "Deportivo", "Para disfrutar")], "any")}
 <div id="fres" class="needs-js" aria-live="polite" style="margin-top:10px"><div class="skel" aria-hidden="true"><i></i><i class="s"></i></div></div>
 {ad("test")}
</div></section>"""
    page("/cual-me-conviene/", "¿Qué coche me conviene? Test de 4 preguntas", "Responde 4 preguntas y descubre los 3 coches que menos te van a costar según tu presupuesto, tus kilómetros y dónde cargas.", body, "finder")

def build_news():
    page("/noticias/", "Noticias de coches eléctricos e híbridos", "Últimas noticias del mercado del coche en España: ventas, lanzamientos, marcas chinas y ayudas.",
         f'{crumbs((None, "Noticias"))}<section class="tight"><div class="wrap"><h1>Noticias</h1><p class="muted" style="margin:10px 0 24px">Lo que mueve el mercado del coche en España, con sus fuentes.</p><div class="newslist">{"".join(news_card(a) for a in NEWS)}</div>{ad("noticias")}<p style="margin-top:28px"><a href="/electricos-chinos/">Todas las marcas chinas →</a> · <a href="/ayudas/">Ayudas Plan Auto+ →</a></p></div></section>', "noticias")
    for a in NEWS:
        k = kmain(a)
        rel = [x for x in NEWS if x is not a][:3]
        src = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in a["src"])
        body = f"""{crumbs(("/noticias/", "Noticias"), (None, KINDS[k]))}
<section class="tight"><div class="wrap narrow article">
 <span class="kicker">{KINDS[k]}</span><h1>{a["t"]}</h1><p class="standfirst">{a["st"]}</p>
 <div class="byline"><strong>Redacción {SITE}</strong><time datetime="{a["date"]}">{a["dtxt"]}</time><span>{a["min"]} min de lectura</span></div>
 {img_tag(a["img"], a["t"], True)}
 <div class="body" style="margin-top:20px">{autolink(a["body"])}</div>
 {ad("articulo")}
 <div class="sources">Fuentes: {src}</div>
 <div style="margin-top:18px">{sharebuttons(aurl(a), a["t"])}</div>
 <div class="cta" style="margin-top:32px"><div><h2>¿Cuánto te costaría a ti?</h2><p>Compara cualquier coche con el tuyo en euros por kilómetro.</p></div><a class="btn" href="/comparador/">Abrir comparador</a></div>
 <h2 style="margin:36px 0 16px;font-size:1.3rem">Sigue leyendo</h2><div class="newslist">{"".join(news_card(x) for x in rel)}</div>
</div></section>"""
        imgu = next((f"{DOMAIN}/assets/img/{a['img']}.{e}" for e in ("webp", "jpg") if os.path.exists(os.path.join(IMG_DIR, f"{a['img']}.{e}"))), f"{DOMAIN}/assets/img/og.png")
        schema = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": a["t"], "description": a["st"], "datePublished": a["date"] + "T08:00:00+02:00", "dateModified": a["date"] + "T08:00:00+02:00",
                  "image": [imgu], "inLanguage": "es-ES", "author": org(), "publisher": {**org(), "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/assets/img/logo-horizontal.png"}}, "mainEntityOfPage": DOMAIN + aurl(a)}
        page(aurl(a), a["t"], a["st"], body, "noticias", schema, reading=True, og=imgu if not imgu.endswith("og.png") else None)

def build_guides():
    page("/guias/", "Guías para comprar coche", "Etiquetas DGT, cargar en casa, autonomía real, híbrido o eléctrico, segunda mano y renting.",
         f'{crumbs((None, "Guías"))}<section class="tight"><div class="wrap"><h1>Guías</h1><p class="muted" style="margin:10px 0 24px">Respuestas claras antes de cambiar de coche.</p><div class="newslist">{"".join(guide_card(g) for g in GUIDES)}</div>{ad("guias")}</div></section>', "guias")
    for g in GUIDES:
        others = [x for x in GUIDES if x is not g][:3]
        body = f"""{crumbs(("/guias/", "Guías"), (None, g["t"]))}
<section class="tight"><div class="wrap narrow article">
 <span class="kicker">Guía</span><h1>{g["t"]}</h1><p class="standfirst">{g["st"]}</p>
 <div class="byline"><strong>Redacción {SITE}</strong><span>Actualizada en {UPDATED}</span></div>
 {img_tag(g["img"], g["t"], True)}
 <div class="body" style="margin-top:20px">{autolink(g["body"])}</div>{ad("guia")}
 <div style="margin-top:18px">{sharebuttons(gurl(g), g["t"])}</div>
 <h2 style="margin:36px 0 16px;font-size:1.3rem">Más guías</h2><div class="newslist">{"".join(guide_card(x) for x in others)}</div>
</div></section>"""
        page(gurl(g), g["t"], g["st"], body, "guias", {"@context": "https://schema.org", "@type": "Article", "headline": g["t"], "description": g["st"], "dateModified": "2026-10-09", "inLanguage": "es-ES", "author": org(), "publisher": org()}, reading=True)

def build_chinos():
    def brand(b):
        n, on, g, models, p = b
        cars_b = [c for c in CARS if c["b"] == n or (n == "Omoda / Jaecoo" and c["b"] in ("Omoda", "Jaecoo"))]
        links = " · ".join(f'<a href="{curl(c)}">{esc(c["m"])}</a>' for c in cars_b) or " · ".join(models)
        return (f'<div class="card"><div class="meta" style="justify-content:space-between"><h3>{n}</h3><span class="pill {"on" if on else "soon"}">{"A la venta" if on else "Llega en 2026"}</span></div>'
                f'<p>Grupo: {g}</p><p style="color:var(--ink2)">{p}</p><p style="font-size:.9rem">{links}</p></div>')
    share = [("Tesla", 21.2, 0), ("BYD", 13.0, 1), ("Leapmotor", 8.0, 1), ("Geely", 4.3, 1), ("Deepal", 2.2, 1), ("XPENG", 1.9, 1)]
    bars = "".join(f'<li><span>{n}<span class="sub">{"Marca china" if cn else "Resto"}</span></span><span class="num">{dec(v)} %</span></li>' for n, v, cn in share)
    chinese = by_pk([c for c in CARS if c["cn"]])
    body = f"""{crumbs((None, "Eléctricos chinos"))}
<section class="tight"><div class="wrap">
 <h1>Coches chinos en España</h1><p class="muted" style="margin:10px 0 24px;max-width:64ch">Ya venden uno de cada tres eléctricos en España. Todas las marcas, de quién son, qué modelos puedes comprar y cuánto cuestan de verdad. ¿Dudas de su fiabilidad? Lee nuestra <a href="/coches-chinos-comprar-sin-miedo/">guía para comprar un coche chino sin miedo</a>.</p>
 <div class="two"><div class="panel"><h3>Cuota en eléctricos · septiembre 2026</h3><ol class="rank">{bars}</ol><p class="note" style="margin-top:8px">Fuente: <a href="https://autonomiacocheselectricos.es/articulos/coches-electricos-mas-vendidos-espana-septiembre-2026/" target="_blank" rel="noopener">Autonomía Coches Eléctricos</a></p></div>
 <div class="panel"><h3>Los chinos más baratos de tener</h3><ol class="rank">{"".join(rank_li(c) for c in chinese[:6])}</ol></div></div>
 <h2 style="margin:40px 0 16px">Todas las marcas</h2><div class="cards">{"".join(brand(b) for b in BRANDS)}</div>
 {ad("chinos")}
 <h2 style="margin:40px 0 16px">Noticias</h2><div class="newslist">{"".join(news_card(a) for a in NEWS if "china" in a["k"])}</div>
</div></section>"""
    page("/electricos-chinos/", "Coches chinos en España: marcas, modelos y coste real", "BYD, Leapmotor, Geely, MG, XPENG y las marcas chinas que llegan a España: modelos, cuota y cuánto cuestan de verdad.", body, "noticias")

def build_ayudas():
    a = next(x for x in ARTICLES if x["k"] == "ayuda")
    eligible = by_pk([c for c in CARS if c["lab"] == "cero" and c["p"] <= 54450])[:10]
    src = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in a["src"])
    body = f"""{crumbs((None, "Ayudas"))}
<section class="tight"><div class="wrap narrow article">
 <span class="kicker">Ayudas 2026</span><h1>Plan Auto+: las ayudas para comprar coche eléctrico</h1><p class="standfirst">Cuánto te dan, qué coches entran y cómo se cobra.</p>
 <div class="bigfig" style="margin-bottom:26px"><div><b>4.500 €</b><span>ayuda estatal máxima</span></div><div><b>+1.000 €</b><span>descuento mínimo del concesionario</span></div><div><b>45.000 €</b><span>precio máximo sin IVA</span></div></div>
 <div class="body">{a["body"]}</div>
 <div class="panel" style="margin-top:20px"><h3>Los 10 coches que pueden optar con menor coste real</h3><ol class="rank">{"".join(rank_li(c) for c in eligible)}</ol></div>
 {ad("ayudas")}<div class="sources">Fuentes: {src}</div>
</div></section>"""
    page("/ayudas/", "Ayudas Plan Auto+ 2026 para coche eléctrico", "Cuánto da el Plan Auto+, qué coches entran, el criterio europeo y qué cambia respecto al MOVES III.", body, "noticias")

F = lambda s: f'<span class="fill">{s}</span>'
def legal_page(path, title, desc, inner, noindex=True):
    page(path, title, desc, f'{crumbs((None, title))}<section class="tight"><div class="wrap narrow article"><h1>{title}</h1><div class="body" style="margin-top:20px">{inner}</div></div></section>', "", noindex=noindex)

OWNER = {"name": "Daniel Vorobkanych", "nif": "60388141P", "addr": "Carrer Riera, 3", "city": "43480 Vila-seca (Tarragona)", "email": "danielvorobkanych2@gmail.com"}
def owner_addr():
    return OWNER["addr"] + (", " + OWNER["city"] if OWNER["city"] else ", " + F("[código postal y localidad]"))

def method_example():
    c = BY["toyota-corolla-hybrid"]; k = K[c["id"]]; S = DEFAULTS
    resid = k["resid"]
    rows = [("Precio de tarifa", eur(c["p"])), ("Valor estimado a los 5 años", eur(resid)), ("Pérdida de valor", eur(k["dep"])),
            ("Energía: " + str(c["c"]).replace(".", ",") + " L/100 km × 75.000 km × " + pk(S["gas"]) + " €/L", eur(k["energy"])),
            ("Seguro (5 años)", eur(k["ins"])), ("Mantenimiento (5 años)", eur(k["mnt"])), ("Impuesto de circulación (5 años)", eur(k["tax"])),
            ("<b>Total en 5 años</b>", "<b>" + eur(k["total"]) + "</b>")]
    tbl = "".join(f'<tr><th>{a}</th><td class="n">{b}</td></tr>' for a, b in rows)
    return (f'<h2>Un ejemplo con números reales</h2><p>Así sale el coste del <a href="{curl(c)}">{c["n"]}</a> con los valores por defecto:</p>'
            f'<div class="tablewrap"><table class="specs vs"><tbody>{tbl}</tbody></table></div>'
            f'<p>Dividido entre 75.000 km da <b>{pk(k["perKm"])} € por kilómetro</b>, y entre 60 meses, <b>{eur(k["month"])} al mes</b>. Todas las fichas se calculan igual.</p>')

def build_legal():
    legal_page("/quienes-somos/", "Quiénes somos", f"Qué es {SITE}, quién está detrás y cómo calculamos el coste real de cada coche de forma independiente y transparente.", f"""<p>{SITE} nace de una idea sencilla: el precio de un coche no es lo que pagas el día que lo compras, sino lo que te cuesta cada kilómetro durante los años que lo tienes.</p>
<h2>Cómo trabajamos</h2><p>Cada noticia cita sus fuentes con enlace. Los datos del comparador son estimaciones con un método público, que explicamos en el propio comparador. Corregimos los errores en cuanto los detectamos.</p>
<h2>Quién está detrás</h2><p>Kilómetro Real es un proyecto independiente creado y mantenido por {OWNER["name"]}. No trabaja para ninguna marca, concesionario ni financiera.</p>
<h2>Publicidad</h2><p>Nos financiamos con publicidad. Los anunciantes no deciden qué publicamos ni cómo lo contamos.</p><p>¿Has visto un error? Escríbenos desde <a href="/contacto/">contacto</a>.</p>""", noindex=False)
    legal_page("/metodologia/", "Cómo calculamos el coste real", "El método de Kilómetro Real para calcular lo que cuesta tener un coche.", f"""<p>Todos los números de Kilómetro Real salen del mismo método público, para que puedas comparar cualquier coche con cualquier otro en igualdad de condiciones.</p>
<h2>Qué sumamos</h2><ul><li><strong>Pérdida de valor:</strong> el precio de tarifa menos el valor estimado del coche al venderlo, según la depreciación media de cada marca. A eléctricos e híbridos enchufables les aplicamos una depreciación algo mayor.</li>
<li><strong>Energía:</strong> consumo real medio estimado por los kilómetros que hagas. En eléctricos mezclamos carga en casa y carga pública; en enchufables, la parte de kilómetros que puedes hacer en eléctrico si cargas a diario.</li>
<li><strong>Seguro:</strong> estimación de un seguro a terceros ampliado para un conductor de 35 años, según el valor del coche.</li>
<li><strong>Mantenimiento:</strong> revisiones, neumáticos y desgaste típico de cada tecnología.</li>
<li><strong>Impuesto de circulación:</strong> media municipal según la potencia, con la bonificación habitual a los eléctricos.</li></ul>
<h2>Valores por defecto</h2><p>15.000 km al año durante 5 años, gasolina a {pk(FUELP["g95"])} €/L, diésel a {pk(FUELP["die"])} €/L, GLP a {pk(FUELP["glp"])} €/L (precios medios del {FUELP["dtxt"]}, con la rebaja fiscal vigente), luz en casa a 0,15 €/kWh y carga pública a 0,49 €/kWh, con un 80 % de carga en casa. Todo se puede cambiar en el <a href="/comparador/">comparador</a>.</p>
{method_example()}<h2>Límites</h2><p>Los precios son de tarifa de acceso, sin descuentos ni ayudas, y se actualizaron en {UPDATED}. Son orientativos y sirven para comparar. Antes de comprar, confirma la oferta en el concesionario. Si ves un dato mal, <a href="/contacto/">avísanos</a> y lo corregimos.</p>""", noindex=False)
    build_contact()
    legal_page("/aviso-legal/", "Aviso legal", "Aviso legal del sitio web.", f"""<p>En cumplimiento de la Ley 34/2002 (LSSI-CE), estos son los datos del titular:</p>
<ul><li>Titular: {OWNER["name"]}</li><li>NIF: {OWNER["nif"]}</li><li>Domicilio: {owner_addr()}</li><li>Correo: <a href="mailto:{OWNER["email"]}">{OWNER["email"]}</a></li></ul>
<h2>Propiedad intelectual</h2><p>Los textos y el diseño pertenecen a su titular. Las marcas citadas pertenecen a sus propietarios.</p>
<h2>Responsabilidad</h2><p>La información es orientativa. Precios, ayudas y datos técnicos pueden cambiar: confírmalos con el fabricante o el concesionario antes de decidir.</p>""")
    legal_page("/privacidad/", "Privacidad", "Política de privacidad.", f"""<p>Responsable: {OWNER["name"]}, NIF {OWNER["nif"]}, domicilio {owner_addr()}, correo <a href="mailto:{OWNER["email"]}">{OWNER["email"]}</a>.</p>
<h2>Qué datos tratamos</h2><p>Si nos escribes, usamos tu correo y tu mensaje solo para responderte. No vendemos ni cedemos tus datos.</p>
<h2>Publicidad</h2><p>Este sitio muestra anuncios de Google AdSense. Google y sus socios pueden usar cookies para mostrar anuncios según tus visitas, siempre que lo aceptes en el aviso de consentimiento. Puedes gestionarlo en la <a href="https://adssettings.google.com" target="_blank" rel="noopener">configuración de anuncios de Google</a>.</p>
<h2>Fuentes tipográficas</h2><p>Las fuentes se cargan desde Google Fonts, por lo que tu navegador se conecta a servidores de Google.</p>
<h2>Tus derechos</h2><p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo al correo de contacto, y reclamar ante la AEPD (aepd.es).</p>""")
    legal_page("/cookies/", "Cookies", "Qué cookies usa Kilómetro Real, para qué sirven y cómo cambiar tu elección en cualquier momento.", """<p>Una cookie es un pequeño archivo que una web guarda en tu navegador. Aquí te contamos cuáles usamos y cómo cambiar de opinión.</p>
<h2>Cookies y datos que usamos</h2><ul>
<li><strong>Publicidad (Google AdSense):</strong> Google y sus socios pueden usar cookies para mostrar y medir anuncios. Solo se usan para anuncios personalizados si lo aceptas en el aviso de consentimiento.</li>
<li><strong>Medición (Google Analytics, si está activo):</strong> estadísticas anónimas de visitas. Solo con tu permiso.</li>
<li><strong>Consentimiento:</strong> guardan la elección que hiciste en el aviso para no volver a preguntarte.</li>
<li><strong>Preferencias de la web (almacenamiento local, no cookies):</strong> el modo claro u oscuro y tus últimas comparaciones. No salen de tu navegador.</li></ul>
<h2 id="gestionar">Cómo cambiar tu elección</h2><p>La primera vez que entras te preguntamos si aceptas las cookies de publicidad personalizada. Si las rechazas, verás anuncios igualmente, pero no basados en tu actividad. Pulsa el botón para volver a abrir el aviso y cambiar lo que elegiste. También puedes borrar las cookies desde la configuración de tu navegador.</p>
<p><button type="button" class="btn ghost cookie-prefs">Gestionar cookies</button></p>
<p>Más información sobre cómo usa Google los datos: <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">policies.google.com/technologies/partner-sites</a>.</p>""")
    legal_page("/condiciones-de-uso/", "Condiciones de uso", "Condiciones de uso de Kilómetro Real: qué ofrecemos, cómo se calculan los datos y responsabilidades al usar la web.", """<p>Al usar Kilómetro Real aceptas estas condiciones. Son sencillas: queremos que la información te sea útil y que sepas sus límites.</p>
<h2>Qué es Kilómetro Real</h2><p>Una web gratuita e informativa que estima lo que cuesta tener un coche en España: pérdida de valor, energía, seguro, mantenimiento e impuesto. No vendemos coches, no somos concesionario ni intermediario y no cobramos a las marcas por aparecer.</p>
<h2>Los datos son orientativos</h2><p>Los precios son de tarifa, sin descuentos ni ayudas, y los consumos y la depreciación son estimaciones medias. Tu caso puede ser distinto. Antes de comprar, confirma precio, ayudas y condiciones con el concesionario o el fabricante. Explicamos cómo calculamos en <a href="/metodologia/">nuestra metodología</a>.</p>
<h2>No es asesoramiento</h2><p>Nada de lo publicado es asesoramiento financiero, fiscal ni legal. Las calculadoras de financiación y ayudas son simulaciones.</p>
<h2>Uso permitido</h2><p>Puedes consultar, compartir y enlazar cualquier página. No está permitido copiar de forma masiva los contenidos o los datos, ni usar sistemas automáticos que sobrecarguen la web.</p>
<h2>Publicidad y enlaces</h2><p>La web se financia con publicidad de Google AdSense. Los anuncios los elige Google y no suponen una recomendación nuestra. No respondemos del contenido de webs externas enlazadas.</p>
<h2>Errores y cambios</h2><p>Si ves un dato mal, <a href="/contacto/">avísanos</a> y lo corregimos. Podemos actualizar estas condiciones; la versión vigente es siempre la publicada aquí.</p>""", noindex=False)
    build_404()

CONTACT_EMAIL = "danielvorobkanych2@gmail.com"   # buzón que recibe los mensajes del formulario
def contact_form(en=False):
    T = (lambda es, e: e) if en else (lambda es, e: es)
    topics = [("dato", T("Hay un dato mal", "Wrong data")), ("noticia", T("Tengo una noticia", "News tip")), ("opinion", T("Mi opinión sobre la web", "Feedback")),
              ("publicidad", T("Publicidad", "Advertising")), ("otro", T("Otra cosa", "Something else"))]
    opts = "".join(f'<option value="{v}">{l}</option>' for v, l in topics)
    priv = "/en/privacy/" if en else "/privacidad/"
    return f"""<form class="form panel" id="contactform" action="/contacto.php" method="post" novalidate>
 <input type="hidden" name="lang" value="{"en" if en else "es"}">
 <div class="hp" aria-hidden="true"><label for="website">Web</label><input type="text" id="website" name="website" tabindex="-1" autocomplete="off"></div><input type="hidden" name="t" value="">
 <div class="cgrid">
  <div><label class="lbl" for="cf-name">{T("Nombre", "Name")}</label><input type="text" id="cf-name" name="name" autocomplete="name" required maxlength="80"></div>
  <div><label class="lbl" for="cf-email">{T("Correo electrónico", "Email")}</label><input type="email" id="cf-email" name="email" autocomplete="email" required maxlength="120"></div>
 </div>
 <div><label class="lbl" for="cf-topic">{T("Motivo", "Topic")}</label><select id="cf-topic" name="topic">{opts}</select></div>
 <div><label class="lbl" for="cf-msg">{T("Mensaje", "Message")}</label><textarea id="cf-msg" name="message" required minlength="20" maxlength="4000"></textarea></div>
 <label class="check"><input type="checkbox" name="consent" value="1" required><span>{T(f'He leído y acepto la <a href="{priv}">política de privacidad</a>. Usaremos tus datos solo para responderte.', f'I have read and accept the <a href="{priv}">privacy policy</a>. We will only use your details to reply.')}</span></label>
 <div><button type="submit" class="btn">{T("Enviar mensaje", "Send message")}</button></div>
 <div id="formstatus" role="status" aria-live="polite"></div>
</form>"""

def build_contact():
    body = f"""{crumbs((None, "Contacto"))}<section class="tight"><div class="wrap narrow">
 <h1>Contacto</h1><p class="muted" style="margin:10px 0 24px">¿Has visto un dato mal, tienes una noticia o quieres contarnos qué te parece la web? Escríbenos. Respondemos en 48 horas laborables.</p>
 {contact_form()}
 <p class="note" style="margin-top:16px">También puedes escribirnos directamente a <span class="num">{CONTACT_EMAIL}</span>.</p>
</div></section>"""
    page("/contacto/", "Contacto", f"Escribe a {SITE}: errores en los datos, noticias, opiniones o publicidad.", body, "", endcta=False)

def build_404():
    pop = "".join(f'<a class="chip" href="{curl(BY[x])}">{esc(BY[x]["n"])}</a>' for x in ["dacia-spring", "tesla-model-3-rwd", "toyota-corolla-hybrid", "byd-dolphin-surf", "kia-ev3", "renault-5-e-tech"])
    body = f"""<section><div class="wrap narrow" style="text-align:center">
 <div class="road" aria-hidden="true" style="margin:0 auto 26px"><svg class="carmini" viewBox="0 0 220 72"><path fill="currentColor" d="M6 58c0-9 6-13 16-15l28-4c12-12 26-19 46-19h34c14 0 24 7 34 19l14 3c9 2 12 8 12 16z"/><circle cx="56" cy="58" r="11" fill="#0d1726"/><circle cx="166" cy="58" r="11" fill="#0d1726"/></svg></div>
 <p class="badge">Error 404</p>
 <h1 style="margin-top:14px">Te has salido de la carretera</h1>
 <p class="muted" style="margin:12px auto 24px;max-width:46ch">Esta página no existe o ha cambiado de dirección. Busca un coche o vuelve a la ruta.</p>
 <form class="searchbox" role="search" style="margin:0 auto 20px"><input class="carsearch" type="search" list="cars" placeholder="Busca un coche, por ejemplo Kia EV3" aria-label="Buscar un coche"></form>
 <p style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap"><a class="btn" href="/">Volver al inicio</a><a class="btn ghost" href="/comparador/">Abrir comparador</a></p>
 <h2 style="margin:36px 0 14px;font-size:1.2rem">Los más buscados</h2><div class="chips" style="justify-content:center">{pop}</div>
</div></section>"""
    page("/404.html", "Página no encontrada", "Esta página no existe.", body, "", noindex=True, endcta=False)

CN_DUELS = [("mg-zs-1-5", "seat-arona-1-0-tsi"), ("mg-zs-hybrid", "toyota-yaris-cross-hybrid"), ("omoda-5-1-6-tgdi", "nissan-juke-dig-t"),
            ("jaecoo-7-1-6-tgdi", "hyundai-tucson-1-6-48v"), ("mg-hs-1-5t", "volkswagen-tiguan-1-5-etsi"), ("mg-3-hybrid", "toyota-yaris-hybrid"),
            ("byd-dolphin-surf", "dacia-spring"), ("byd-seal-u-dm-i", "toyota-rav4-hybrid"), ("mg-4-electric", "volkswagen-id-3"), ("byd-atto-2", "kia-ev3")]
def build_cn_guide():
    duels = ""
    for a, b in CN_DUELS:
        A, B = BY[a], BY[b]; ka, kb = K[a], K[b]
        cheaper = A if ka["total"] <= kb["total"] else B
        duels += (f'<tr><td><a href="{curl(A)}">{esc(A["n"])}</a><span class="sub">{eur(A["p"])} · {pk(ka["perKm"])} €/km</span></td>'
                  f'<td><a href="{curl(B)}">{esc(B["n"])}</a><span class="sub">{eur(B["p"])} · {pk(kb["perKm"])} €/km</span></td>'
                  f'<td><strong>{esc(cheaper["n"])}</strong><span class="sub">ahorra {eur(abs(ka["total"]-kb["total"]))} en 5 años</span></td>'
                  f'<td><a class="chip" href="/comparador/#{a}-vs-{b}">Comparar</a></td></tr>')
    cheap = by_pk([c for c in CARS if c["cn"] and c["p"] <= 30000])[:10]
    cn_res = sum(c["res"] for c in CARS if c["cn"]) / len([c for c in CARS if c["cn"]])
    tr_res = sum(c["res"] for c in CARS if not c["cn"]) / len([c for c in CARS if not c["cn"]])
    faq = [("¿Son seguros los coches chinos?", "Muchos tienen la máxima nota en Euro NCAP: el Omoda 5, el MG4, el BYD Atto 3 y el BYD Dolphin Surf lograron 5 estrellas. No todos: el MG ZS se quedó en 4. Mira siempre el resultado del modelo concreto."),
           ("¿Qué garantía tienen?", "Suelen ser de las más largas del mercado: 7 años o 150.000 km en MG, Omoda y Jaecoo, y 6 años o 150.000 km en BYD. La garantía legal mínima en España es de 3 años."),
           ("¿Dónde los reparo?", "La red oficial es todavía pequeña. Los recambios básicos suelen llegar en unas 72 horas, pero las reparaciones de chapa pueden alargarse. Pregunta por el taller oficial más cercano antes de comprar."),
           ("¿Pierden más valor?", "Es la gran incógnita. Al ser marcas nuevas, no hay historial de reventa. En nuestros cálculos les aplicamos una depreciación mayor que a las marcas tradicionales para no inflar su ventaja."),
           ("¿Tienen ayudas del Plan Auto+?", "Los eléctricos y enchufables pueden optar, pero si se fabrican fuera de Europa la ayuda puede ser menor que la de un coche europeo.")]
    faqh = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = f"""{crumbs((None, "Coches chinos sin miedo"))}
<section class="tight"><div class="wrap narrow article">
 <span class="kicker">Guía para comprar</span>
 <h1>¿Coche chino? Lo que tienes que saber antes de comprar un MG, Omoda, Jaecoo o BYD</h1>
 <p class="standfirst">Son más baratos y vienen muy equipados, pero muchos compradores tienen dudas. Las resolvemos con datos, sin miedo y sin publicidad.</p>
 <div class="byline"><strong>Redacción {SITE}</strong><span>Actualizada en {UPDATED}</span></div>
 <div class="bigfig" style="margin-bottom:24px"><div><b>43 %</b><span>los ve ya como alternativa real</span></div><div><b>37 %</b><span>duda de los recambios</span></div><div><b>54 %</b><span>cree que su calidad es buena</span></div></div>
 <div class="body">
 <p>Las marcas chinas ya venden uno de cada tres eléctricos en España, y MG, Omoda o Jaecoo están entre las opciones más baratas para quien busca un SUV nuevo. Aun así, según el Observatorio Cetelem, las dudas siguen ahí: recambios (37 %), durabilidad (35 %), seguridad (31 %) y posventa (28 %). Vamos una por una.</p>
 <h2>1. Seguridad: mejor de lo que mucha gente cree</h2>
 <p>El Omoda 5, el MG4, el BYD Atto 3 y el BYD Dolphin Surf obtuvieron la máxima nota de 5 estrellas en Euro NCAP, el organismo europeo que hace las pruebas de choque. No es una regla para todos: el MG ZS se quedó en 4 estrellas. La recomendación es la misma que para cualquier marca: mira la nota del modelo exacto.</p>
 <h2>2. Garantía: de las más largas del mercado</h2>
 <table><thead><tr><th>Marca</th><th>Garantía</th><th>Batería</th></tr></thead><tbody>
 <tr><td>MG</td><td>7 años o 150.000 km</td><td>Consulta en el concesionario</td></tr>
 <tr><td>Omoda</td><td>7 años o 150.000 km</td><td>8 años o 160.000 km</td></tr>
 <tr><td>Jaecoo</td><td>7 años o 150.000 km</td><td>8 años o 160.000 km</td></tr>
 <tr><td>BYD</td><td>6 años o 150.000 km</td><td>Consulta en el concesionario</td></tr>
 <tr><td>Kia (como referencia)</td><td>7 años o 150.000 km</td><td>7 años o 150.000 km</td></tr>
 <tr><td>Hyundai (como referencia)</td><td>5 años sin límite</td><td>8 años o 160.000 km</td></tr>
 <tr><td>Seat (como referencia)</td><td>3 años sin límite</td><td>8 años o 160.000 km</td></tr>
 </tbody></table>
 <p class="note">Condiciones publicadas por Motor16. Pueden cambiar y suelen exigir hacer las revisiones en la red oficial: confírmalas siempre por escrito antes de firmar.</p>
 <h2>3. Talleres y recambios: el punto débil</h2>
 <p>Aquí está la duda más razonable. Su red oficial todavía es pequeña: mientras una marca como Renault tiene más de 250 talleres autorizados en España, algunas marcas chinas tienen unas pocas decenas. BYD tenía 28 puntos de venta a mediados de 2026 y quiere llegar a 36 concesionarios y 65 talleres antes de fin de año.</p>
 <p>Los recambios básicos suelen llegar en unas 72 horas, pero las reparaciones de chapa pueden tardar más porque los coches no se fabrican en Europa. Según Ganvam, el 54 % de los compradores duda de la posventa de estas marcas.</p>
 <h2>4. Valor de reventa: la gran incógnita</h2>
 <p>Como son marcas recién llegadas, nadie sabe todavía cuánto valdrán dentro de cinco años. Por prudencia, en nuestros cálculos les aplicamos una depreciación mayor: de media estimamos que conservan un {round(cn_res * 100)} % de su valor a los 5 años, frente al {round(tr_res * 100)} % de las marcas tradicionales.</p>
 <div class="fact"><strong>La clave está aquí.</strong> Con esta estimación prudente, solo 2 de los 10 coches chinos de la tabla de abajo salen más baratos que su rival tradicional. Pero si conservaran su valor igual que una marca de siempre, ganarían 8 de los 10. Es decir: <strong>son más baratos de comprar, y que lo sean también de tener depende de cuánto valgan al venderlos.</strong></div>
 <p>Por eso, si vas a quedarte el coche muchos años (cuando la reventa importa menos), un chino puede ser una compra muy sensata. Si lo cambias cada pocos años, la marca tradicional suele ser la apuesta más segura.</p>
 <h2>Chino o de toda la vida: cara a cara</h2>
 </div>
 <div class="tablewrap" style="margin-bottom:10px"><table class="list" style="min-width:680px"><thead><tr><th>Chino</th><th>Rival tradicional</th><th>Sale más barato</th><th></th></tr></thead><tbody>{duels}</tbody></table></div>
 <p class="note">Con 15.000 km al año durante 5 años, sumando pérdida de valor, energía, seguro, mantenimiento e impuesto.</p>
 <div class="body">
 <h2>5 preguntas antes de firmar</h2>
 <ol><li>¿Dónde está el taller oficial más cercano a mi casa?</li>
 <li>¿Qué cubre exactamente la garantía y qué revisiones exige?</li>
 <li>¿Cuánto tarda en llegar una pieza de carrocería?</li>
 <li>¿El precio anunciado es al contado o solo financiando?</li>
 <li>¿Qué nota tiene este modelo en Euro NCAP?</li></ol>
 <h2>Los coches chinos más baratos de tener</h2>
 </div>
 <div class="panel"><ol class="rank">{"".join(rank_li(c) for c in cheap)}</ol></div>
 {ad("chinos-guia")}
 <h2 style="margin:32px 0 12px;font-size:1.3rem">Preguntas frecuentes</h2><div class="faq">{faqh}</div>
 <div class="sources">Fuentes: <a href="https://www.hibridosyelectricos.com/coches/coches-chinos-dejan-ser-rareza-en-espana-43-ya-ve-como-alternativa-marcas-siempre_87239_102.html" target="_blank" rel="noopener">Observatorio Cetelem (Híbridos y Eléctricos)</a> · <a href="https://www.motor16.com/noticias/garantia-oficial-coches-espana/" target="_blank" rel="noopener">Motor16, garantías</a> · <a href="https://www.motor16.com/noticias/seguridad-coches-chinos-byd-mg-omoda/" target="_blank" rel="noopener">Motor16, Euro NCAP</a> · <a href="https://es.motor1.com/news/743167/mg-zs-renault5-test-euroncap/" target="_blank" rel="noopener">Motor1, MG ZS</a> · <a href="https://www.byd.com/es-es/news-list/byd-dolphin-surf-maxima-calificacion-seguridad-cinco-estrllas-euro-ncap" target="_blank" rel="noopener">BYD, Dolphin Surf</a> · <a href="https://www.motor.es/noticias/coches-chinos-postventa-reparaciones-2026115824.html" target="_blank" rel="noopener">Motor.es, posventa</a></div>
 <div style="margin-top:18px">{sharebuttons("/coches-chinos-comprar-sin-miedo/", "¿Coche chino? Lo que tienes que saber antes de comprar")}</div>
</div></section>"""
    ld = {"@context": "https://schema.org", "@graph": [{"@type": "Article", "headline": "¿Coche chino? Lo que tienes que saber antes de comprar un MG, Omoda, Jaecoo o BYD", "dateModified": "2026-10-09", "inLanguage": "es-ES", "author": org(), "publisher": org()},
          {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
    page("/coches-chinos-comprar-sin-miedo/", "¿Es fiable comprar un coche chino? MG, Omoda, Jaecoo y BYD con datos", "Seguridad, garantía, talleres y reventa de los coches chinos en España, con datos. Y cuáles salen más baratos que su rival de siempre.", body, "coches", ld, reading=True)

def build_static():
    for d in ("assets/css", "assets/js", "assets/img", "assets/data"): os.makedirs(os.path.join(OUT, d), exist_ok=True)
    import subprocess
    ESB = "/opt/npm-tools/node_modules/esbuild/bin/esbuild"
    for src, dst in (("site.css", "assets/css/site.css"), ("app.js", "assets/js/app.js")):
        code = open(os.path.join(HERE, src), encoding="utf-8").read()
        if src == "app.js":
            code = re.sub(r"gas:[0-9.]+,die:[0-9.]+,glp:[0-9.]+", f"gas:{FUELP['g95']},die:{FUELP['die']},glp:{FUELP['glp']}", code)
        tmp = os.path.join(OUT, dst.replace(".", ".src.", 1) if False else os.path.splitext(dst)[0] + ".src" + os.path.splitext(dst)[1]); open(tmp, "w", encoding="utf-8").write(code)
        try: subprocess.run([ESB, tmp, "--minify", "--outfile=" + os.path.join(OUT, dst), "--log-level=error"], check=True, timeout=60)
        except Exception: shutil.copy(tmp, os.path.join(OUT, dst))
        os.remove(tmp)
    for f in os.listdir(os.path.join(HERE, "icons")): shutil.copy(os.path.join(HERE, "icons", f), os.path.join(OUT, f))
    with open(os.path.join(OUT, "site.webmanifest"), "w") as f:
        json.dump({"name": SITE, "short_name": "Kilómetro Real", "start_url": "/", "display": "standalone", "background_color": "#ffffff", "theme_color": "#101D33",
                   "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, f)
    with open(os.path.join(HERE, "contacto.php"), encoding="utf-8") as f: php = f.read().replace("__CONTACT_EMAIL__", CONTACT_EMAIL)
    with open(os.path.join(OUT, "contacto.php"), "w", encoding="utf-8") as f: f.write(php)
    if os.path.isdir(IMG_DIR):
        for f in os.listdir(IMG_DIR): shutil.copy(os.path.join(IMG_DIR, f), os.path.join(OUT, "assets/img", f))
    keys = ["id", "b", "m", "n", "t", "f", "body", "p", "c", "bat", "rng", "cv", "trunk", "res", "ins", "mnt", "tax", "lab", "cn"]
    with open(os.path.join(OUT, "assets/data/coches.json"), "w", encoding="utf-8") as f:
        json.dump([{k: c[k] for k in keys} for c in CARS], f, ensure_ascii=False, separators=(",", ":"))
    shutil.copy(os.path.join(HERE, "brand", "icon-app.svg"), os.path.join(OUT, "favicon.svg"))
    shutil.copy(os.path.join(HERE, "brand", "logo.svg"), os.path.join(OUT, "assets", "img", "logo.svg"))
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /contacto.php\n\nSitemap: {DOMAIN}/sitemap.xml\nSitemap: {DOMAIN}/news-sitemap.xml\n")
    shutil.copy(os.path.join(HERE, "htaccess.txt"), os.path.join(OUT, ".htaccess"))
    urls = ["/", "/comparador/", "/coches/", "/marcas/"] + [f"/marcas/{slugify(b)}/" for b in sorted({c["b"] for c in CARS})] + ["/mejores/", "/cual-me-conviene/", "/calculadoras/"] + [f"/calculadoras/{x[0]}/" for x in CALCS] + [ "/noticias/", "/electricos-chinos/", "/ayudas/", "/coches-chinos-comprar-sin-miedo/", "/guias/", "/quienes-somos/", "/metodologia/", "/contacto/", "/condiciones-de-uso/", "/precio-gasolina-hoy/", "/comparar/", "/mi-coche/"]
    urls += [curl(c) for c in CARS] + [f"/comparar/{a}-vs-{b}/" for a, b in __import__("vs_pairs").VS_PAIRS] + [f"/mejores/{r[0]}/" for r in RANKINGS] + [aurl(a) for a in NEWS] + [gurl(g) for g in GUIDES]
    urls += sorted({v for v in ALT.values() if v.startswith("/en/") and v not in ("/en/privacy/", "/en/cookies/")})
    urls = list(dict.fromkeys(urls))
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{DOMAIN}{u}</loc><lastmod>{__import__("datetime").date.today().isoformat()}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    if ADSENSE_CLIENT:
        open(os.path.join(OUT, "ads.txt"), "w").write(f"google.com, {ADSENSE_CLIENT.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")

# ===== calculadoras =====
def fld(id_, label, inp): return f'<div><label class="lbl" for="{id_}">{label}</label>{inp}</div>'
def ninput(id_, v, step="any", extra=""): return f'<input type="number" id="{id_}" value="{v}" step="{step}" inputmode="decimal" {extra}>'
CALCS = [
 ("coste-viaje-gasolina", "Calculadora de gasolina para un viaje", "€/viaje", "Cuánto cuesta un viaje en coche en gasolina, diésel o electricidad, y cuánto toca pagar a cada uno.",
  f"""<div class="calc" id="calc-viaje"><div class="cgrid">
  {fld("v-car", "Tu coche (opcional)", '<input type="text" id="v-car" list="cars" placeholder="Escribe un modelo" autocomplete="off">')}
  {fld("v-km", "Distancia (km)", ninput("v-km", 600, "1"))}
  {fld("v-c", "Consumo cada 100 km", ninput("v-c", 6.0, "0.1"))}
  {fld("v-u", "Unidad", '<select id="v-u"><option value="L">Litros</option><option value="kWh">kWh</option></select>')}
  {fld("v-p", "Precio por litro o kWh (€)", ninput("v-p", FUELP["g95"], "0.01"))}
  {fld("v-n", "Personas en el coche", ninput("v-n", 2, "1", 'min="1"'))}
  {fld("v-t", "Peajes y parking (€)", ninput("v-t", 0, "1"))}
  <div><label class="lbl" for="v-ret">Ida y vuelta</label><label class="switch"><input type="checkbox" id="v-ret" checked> Sí, contar la vuelta</label></div>
  </div><div class="cres" id="v-res" aria-live="polite"></div></div>""",
  """<h2>Cómo se calcula</h2><p>Multiplicamos los kilómetros por el consumo cada 100 km y por el precio del combustible, sumamos peajes y parking, y lo dividimos entre las personas que viajan. Si eliges tu coche, rellenamos su consumo real estimado.</p>
<h2>Trucos para gastar menos</h2><ul><li>Bajar de 120 a 110 km/h en autopista reduce el consumo de forma notable.</li><li>Llevar las ruedas a la presión correcta y quitar el portaequipajes vacío ayuda más de lo que parece.</li><li>Repostar en gasolineras de autoservicio fuera de la autopista suele ser más barato.</li></ul>""",
  [("¿Cuánto gasta un coche en 100 km?", "Un coche de gasolina moderno gasta entre 5 y 7 litros cada 100 km en uso real; un híbrido, entre 4 y 5,5; un eléctrico, entre 14 y 19 kWh."),
   ("¿Cómo se reparte la gasolina de un viaje?", "Lo más justo es dividir el combustible, los peajes y el parking entre todos los que viajan. La calculadora lo hace por ti.")]),
 ("coste-carga-electrico", "Calculadora de carga de coche eléctrico", "kWh", "Cuánto cuesta cargar tu coche eléctrico en casa, con tarifa nocturna o en un cargador rápido.",
  f"""<div class="calc" id="calc-carga"><div class="cgrid">
  {fld("c-car", "Tu coche (opcional)", '<input type="text" id="c-car" list="cars" placeholder="Escribe un eléctrico" autocomplete="off">')}
  {fld("c-bat", "Batería útil (kWh)", ninput("c-bat", 60, "0.1"))}
  {fld("c-from", "Cargar desde (%)", ninput("c-from", 20, "1", 'min="0" max="100"'))}
  {fld("c-to", "Hasta (%)", ninput("c-to", 80, "1", 'min="0" max="100"'))}
  {fld("c-where", "Dónde cargas", '<select id="c-where"><option value="0.15">En casa, tarifa normal (0,15 €/kWh)</option><option value="0.10">En casa, tarifa nocturna (0,10 €/kWh)</option><option value="0.35">Cargador público lento (0,35 €/kWh)</option><option value="0.49" >Cargador rápido (0,49 €/kWh)</option><option value="0.59">Ultrarrápido (0,59 €/kWh)</option></select>')}
  {fld("c-p", "Precio exacto (€/kWh)", ninput("c-p", 0.15, "0.01"))}
  {fld("c-cons", "Consumo (kWh/100 km)", ninput("c-cons", 16, "0.1"))}
  </div><div class="cres" id="c-res" aria-live="polite"></div></div>""",
  """<h2>Cómo se calcula</h2><p>Calculamos la energía que entra en la batería, le sumamos alrededor de un 10 % de pérdidas en la carga y la multiplicamos por el precio del kWh. Con el consumo de tu coche estimamos los kilómetros que ganas.</p>
<h2>Por qué no cargar siempre al 100 %</h2><p>Muchos fabricantes recomiendan cargar al 80 % en el día a día para cuidar la batería, salvo en las baterías LFP, que toleran bien el 100 %. En cargadores rápidos, la potencia cae mucho por encima del 80 %, así que suele compensar parar antes.</p>""",
  [("¿Cuánto cuesta cargar un coche eléctrico en casa?", "Con una tarifa de 0,15 €/kWh, llenar una batería de 60 kWh cuesta unos 10 €. Con tarifa nocturna, bastante menos."),
   ("¿Es más barato cargar de noche?", "Sí. Con la tarifa 2.0TD el periodo valle (de 0 a 8 h y fines de semana) es el más barato.")]),
 ("cuota-financiacion-coche", "Calculadora de cuota para financiar un coche", "TIN", "Cuánto pagarás al mes, cuánto pagas de intereses y cuál es la TAE aproximada de un préstamo para coche.",
  f"""<div class="calc" id="calc-fin"><div class="cgrid">
  {fld("f-p", "Precio del coche (€)", ninput("f-p", 25000, "100"))}
  {fld("f-e", "Entrada (€)", ninput("f-e", 5000, "100"))}
  {fld("f-tin", "Interés TIN (%)", ninput("f-tin", 7.99, "0.01"))}
  {fld("f-m", "Plazo", '<select id="f-m"><option value="24">24 meses</option><option value="36">36 meses</option><option value="48">48 meses</option><option value="60" selected>60 meses</option><option value="72">72 meses</option><option value="84">84 meses</option><option value="96">96 meses</option></select>')}
  {fld("f-com", "Comisión de apertura (%)", ninput("f-com", 2, "0.1"))}
  </div><div class="cres" id="f-res" aria-live="polite"></div></div>""",
  """<h2>Fíjate en la TAE, no solo en la cuota</h2><p>La TAE incluye el interés y las comisiones, así que es el número que sirve para comparar préstamos. Una cuota baja a muchos meses puede salir mucho más cara en total. Calculamos la TAE aproximada a partir del interés y la comisión de apertura; la oficial puede variar ligeramente por seguros o gastos incluidos.</p>
<h2>Cuidado con la financiación de concesionario</h2><p>Muchas ofertas anunciadas solo valen financiando y exigen permanencia. Compara siempre el total que pagarás con lo que costaría al contado. Te lo explicamos en la guía de <a href="/guias/renting-financiacion-o-contado/">renting, financiación o contado</a>.</p>""",
  [("¿Qué es mejor, más entrada o más plazo?", "Más entrada y menos plazo casi siempre significa pagar menos intereses en total, aunque la cuota mensual sea más alta."),
   ("¿Qué diferencia hay entre TIN y TAE?", "El TIN es el interés puro. La TAE suma las comisiones y refleja el coste real del préstamo en un año.")]),
 ("etiqueta-dgt", "¿Qué etiqueta DGT tiene mi coche?", "DGT", "Averigua la etiqueta ambiental de tu coche según el combustible y el año de matriculación.",
  f"""<div class="calc" id="calc-eti"><div class="cgrid">
  {fld("e-t", "Tipo de coche", '<select id="e-t"><option value="g">Gasolina</option><option value="d">Diésel</option><option value="hev">Híbrido no enchufable</option><option value="glp">GLP o gas natural</option><option value="phev-">Híbrido enchufable de menos de 40 km eléctricos</option><option value="phev">Híbrido enchufable de 40 km eléctricos o más</option><option value="ev">Eléctrico</option></select>')}
  {fld("e-y", "Año de matriculación", ninput("e-y", 2012, "1", 'min="1970" max="2026"'))}
  </div><div class="cres" id="e-res" aria-live="polite"></div></div>""",
  """<h2>Cómo se decide la etiqueta</h2><p>La DGT asigna la etiqueta según la norma de emisiones (Euro) del coche, que en la práctica depende sobre todo del combustible y de la fecha de matriculación. En los casos frontera, como los diésel de 2015, la fecha exacta importa.</p>
<p>Este cálculo es orientativo. Para saber la etiqueta exacta de tu coche, consulta tu matrícula en la sede electrónica de la DGT. Te lo explicamos todo en la <a href="/guias/etiquetas-dgt/">guía de etiquetas</a>.</p>""",
  [("¿Qué etiqueta tiene un diésel de 2014?", "Normalmente la B. Los diésel solo tienen la C si cumplen la norma Euro 6, habitual a partir de septiembre de 2015."),
   ("¿Los híbridos tienen etiqueta ECO?", "Sí, los híbridos no enchufables y los enchufables de menos de 40 km eléctricos llevan la ECO.")]),
 ("amortizacion-electrico", "¿Me compensa un coche eléctrico?", "km", "A partir de cuántos kilómetros al año un eléctrico te sale más barato que un gasolina o un híbrido.",
  f"""<div class="calc" id="calc-amo"><div class="cgrid">
  {fld("a-ev", "Coche eléctrico", '<input type="text" id="a-ev" list="cars" value="Renault 5 E-Tech" autocomplete="off">')}
  {fld("a-ice", "Frente a", '<input type="text" id="a-ice" list="cars" value="Renault Clio TCe" autocomplete="off">')}
  {fld("a-y", "Años que lo tendrás", ninput("a-y", 5, "1", 'min="2" max="10"'))}
  {fld("a-h", "Porcentaje de carga en casa", ninput("a-h", 80, "5", 'min="0" max="100"'))}
  </div><div class="cres" id="a-res" aria-live="polite"></div></div>""",
  """<h2>Cómo se calcula</h2><p>Comparamos el coste total de los dos coches (pérdida de valor, energía, seguro, mantenimiento e impuesto) para cada nivel de kilómetros al año y buscamos el punto en el que el eléctrico pasa a ser más barato. No incluye ayudas como el Plan Auto+, que adelantarían ese punto.</p>
<p>Si cargas casi siempre en la calle, el eléctrico necesita muchos más kilómetros para compensar. Prueba a cambiar el porcentaje de carga en casa y verás la diferencia.</p>""",
  [("¿Compensa un eléctrico si hago pocos kilómetros?", "Depende de la diferencia de precio. Con modelos de precio parecido, puede compensar desde el primer kilómetro; con diferencias grandes, necesitas muchos kilómetros."),
   ("¿Y si no puedo cargar en casa?", "Entonces dependerás de cargadores públicos, bastante más caros, y el eléctrico tardará mucho más en compensar.")]),
]

def build_calcs():
    cards = "".join(f'<a class="card calc-card" href="/calculadoras/{s}/"><span class="badge">{b}</span><h3>{t}</h3><p>{d}</p></a>' for s, t, b, d, _, _, _ in CALCS)
    page("/calculadoras/", "Calculadoras para conductores", "Calculadoras gratis: gasolina de un viaje, carga de coche eléctrico, cuota de financiación, etiqueta DGT y si te compensa un eléctrico.",
         f'{crumbs((None, "Calculadoras"))}<section class="tight"><div class="wrap"><h1>Calculadoras</h1><p class="muted" style="margin:10px 0 24px;max-width:62ch">Respuestas rápidas a las cuentas que todo conductor se hace alguna vez.</p><div class="cards">{cards}</div>{ad("calculadoras")}</div></section>', "calc")
    for s, t, b, d, form, text, faq in CALCS:
        others = "".join(f'<a class="chip" href="/calculadoras/{s2}/">{t2}</a>' for s2, t2, *_ in CALCS if s2 != s)
        faqh = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
        body = f"""{crumbs(("/calculadoras/", "Calculadoras"), (None, t))}
<section class="tight"><div class="wrap narrow">
 <span class="badge">{b}</span><h1 style="margin-top:12px">{t}</h1><p class="muted" style="margin:10px 0 24px">{d}</p>
 <div class="tool needs-js">{form}</div>
 {ad("calc")}
 <div class="body" style="margin-top:30px">{text}</div>
 <div style="margin-top:18px">{sharebuttons(f"/calculadoras/{s}/", t)}</div>
 <h2 style="margin:30px 0 12px;font-size:1.3rem">Preguntas frecuentes</h2><div class="faq">{faqh}</div>
 <h2 style="margin:30px 0 12px;font-size:1.3rem">Otras calculadoras</h2><div class="chips">{others}</div>
</div></section>"""
        ld = {"@context": "https://schema.org", "@graph": [{"@type": "WebApplication", "name": t, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Web", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}},
              {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
        page(f"/calculadoras/{s}/", t, d, body, "calc", ld)

if __name__ == "__main__":
    exec(open(os.path.join(HERE, "en.py"), encoding="utf-8").read())
    fill_alt()
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    ensure_covers()
    build_static(); build_home(); build_comparador(); build_catalog()
    for c in CARS: build_car(c)
    exec(open(os.path.join(HERE, "pages_extra.py"), encoding="utf-8").read(), globals()); build_fuel(); build_vs(); build_micoche()
    build_rankings(); build_finder(); build_calcs(); build_brands(); build_cn_guide(); build_news(); build_guides(); build_chinos(); build_ayudas(); build_legal()
    # redirección de la antigua sección
    page("/novedades-precios/", "Novedades y precios", "Precios de los coches en venta.", '<section><div class="wrap narrow"><h1>Novedades y precios</h1><p style="margin-top:12px">Esta sección ahora está en <a href="/coches/">Todos los coches</a>.</p></div></section>', "", noindex=True)
    build_en_all(); build_feeds()
    with open(os.path.join(OUT, "sitemap.xml"), encoding="utf-8") as f: sm = f.read()
    extra = "".join(f"<url><loc>{DOMAIN}{u}</loc><lastmod>{__import__("datetime").date.today().isoformat()}</lastmod></url>\n" for u in sorted(set(ALT.values())))
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f: f.write(sm.replace("</urlset>", extra + "</urlset>"))
    n = sum(len([f for f in fs if f.endswith(".html")]) for _, _, fs in os.walk(OUT))
    print("OK", n, "páginas")
