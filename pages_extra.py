# Páginas extra: precio de los carburantes hoy y comparativas A vs B. Se ejecuta dentro de build.py.
from vs_pairs import VS_PAIRS

def ldj(*items): return {"@context": "https://schema.org", "@graph": list(items)}
def faq_ld(faq): return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faq]}
def faq_box(faq): return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq) + "</div>"
def fprice(v): return f"{v:.3f}".replace(".", ",") + " €"

# ---------------- HISTÓRICO DE CARBURANTES ----------------
# fuel_history.json guarda un registro por día. El build añade (o corrige) solo el día de fuel.py,
# así la serie crece cada mañana sin pasos extra.
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
FUEL_MONTH_URLS = []
def load_fuel_hist():
    fp = os.path.join(HERE, "fuel_history.json")
    try: H = json.load(open(fp, encoding="utf-8"))
    except Exception: H = []
    d = {h["date"]: h for h in H}
    d[FUELP["date"]] = {"date": FUELP["date"], **{k: FUELP[k] for k in ("g95", "g98", "die", "die_plus", "glp")}}
    H = [d[k] for k in sorted(d)]
    with open(fp, "w", encoding="utf-8") as f: json.dump(H, f, indent=1)
    return H

def mslug(ym): return f"{MESES[int(ym[5:7]) - 1]}-{ym[:4]}"
def mname(ym): return f"{MESES[int(ym[5:7]) - 1]} de {ym[:4]}"
def ddmm(d): return f"{int(d[8:10])}/{int(d[5:7])}"

def fuel_chart(H, title):
    """Gráfico SVG de gasolina 95 y diésel. Sin JS: tooltip nativo por punto y tabla aparte."""
    H = [h for h in H if "g95" in h and "die" in h][-90:]
    if len(H) < 2: return ""
    W, Ht, L, R, T, B = 480, 230, 44, 104, 14, 30
    vals = [h[k] for h in H for k in ("g95", "die")]
    lo, hi = min(vals), max(vals)
    pad = max(0.01, (hi - lo) * 0.15); lo -= pad; hi += pad
    import datetime as _dt
    _d = [_dt.date.fromisoformat(h["date"]) for h in H]; span = max(1, (_d[-1] - _d[0]).days)
    x = lambda i: L + (W - L - R) * (_d[i] - _d[0]).days / span
    y = lambda v: T + (Ht - T - B) * (hi - v) / (hi - lo)
    grid = ""
    for j in range(4):
        v = lo + (hi - lo) * j / 3
        vt = f"{v:.2f}".replace(".", ",")
        grid += f'<line x1="{L}" x2="{W-R}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="fc-grid"/><text x="{L-6}" y="{y(v)+4:.1f}" class="fc-ax" text-anchor="end">{vt}</text>'
    step = max(1, -(-len(H) // 5))
    ticks, lastx = [], -999
    for i in list(range(0, len(H) - 1, step)) + [len(H) - 1]:
        if x(i) - lastx >= 52 or i == len(H) - 1:
            if ticks and x(i) - lastx < 52: ticks.pop()
            ticks.append(i); lastx = x(i)
    xt = "".join(f'<text x="{x(i):.1f}" y="{Ht-8}" class="fc-ax" text-anchor="middle">{ddmm(H[i]["date"])}</text>' for i in ticks)
    series = ""
    for k, cls, name, short in (("g95", "fc-a", "Gasolina 95", "G95"), ("die", "fc-b", "Diésel", "Diésel")):
        pts = " ".join(f"{x(i):.1f},{y(h[k]):.1f}" for i, h in enumerate(H))
        last = H[-1][k]
        series += f'<polyline points="{pts}" class="fc-line {cls}"/>'
        series += "".join(f'<g class="fc-pt"><circle cx="{x(i):.1f}" cy="{y(h[k]):.1f}" r="9" class="fc-hit"/><circle cx="{x(i):.1f}" cy="{y(h[k]):.1f}" r="4" class="fc-dot {cls}"/><title>{name}, {ddmm(h["date"])}: {fprice(h[k])}</title></g>' for i, h in enumerate(H))
        series += f'<text x="{W-R+8}" y="{y(last)+4:.1f}" class="fc-lbl">{short} {fprice(last).replace(" €", "")}</text>'
    legend = '<div class="fc-leg"><span><i class="fc-a"></i>Gasolina 95</span><span><i class="fc-b"></i>Diésel</span><span class="muted">€ por litro, media en España</span></div>'
    return (f'<figure class="fchart">{legend}<svg viewBox="0 0 {W} {Ht}" role="img" aria-label="{esc(title)}">{grid}{xt}{series}</svg>'
            f'<figcaption class="note">Pasa el dedo o el ratón por los puntos para ver el precio de cada día. Debajo tienes la tabla con todos los datos.</figcaption></figure>')

def fuel_table(H):
    rows = "".join(f'<tr><td>{ddmm(h["date"])}/{h["date"][:4]}</td>' + "".join(f'<td class="n">{fprice(h[k]) if k in h else "–"}</td>' for k in ("g95", "g98", "die", "die_plus", "glp")) + "</tr>" for h in reversed(H))
    return f'<div class="tablewrap"><table class="list fit"><thead><tr><th>Día</th><th class="n">Gasolina 95</th><th class="n">Gasolina 98</th><th class="n">Diésel</th><th class="n">Diésel premium</th><th class="n">GLP</th></tr></thead><tbody>{rows}</tbody></table></div>'

FCSS = ('<style>.fchart{margin:8px 0 0}.fchart svg{width:100%;max-width:560px;height:auto;display:block;overflow:visible}'
        '.fc-grid{stroke:var(--line);stroke-width:1}.fc-ax{font:13px var(--f-data);fill:var(--muted)}.fc-lbl{font:600 14px var(--f-data);fill:var(--ink2)}'
        '.fc-line{fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}.fc-a{stroke:#1846c7;background:#1846c7}.fc-b{stroke:#c2570c;background:#c2570c}'
        '.fc-dot{fill:var(--surface);stroke-width:2}.fc-hit{fill:transparent}.fc-pt:hover .fc-dot{r:6}'
        '.fc-leg{display:flex;gap:16px;flex-wrap:wrap;font-size:.9rem;margin-bottom:6px;color:var(--ink2)}.fc-leg i{display:inline-block;width:14px;height:3px;border-radius:2px;margin-right:6px;vertical-align:middle}'
        ':root[data-theme="dark"] .fc-a{stroke:#5f8cf5;background:#5f8cf5}:root[data-theme="dark"] .fc-b{stroke:#d26f22;background:#d26f22}'
        '@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .fc-a{stroke:#5f8cf5;background:#5f8cf5}:root:not([data-theme="light"]) .fc-b{stroke:#d26f22;background:#d26f22}}</style>')

def build_fuel_months(H):
    months = sorted({h["date"][:7] for h in H})
    for ym in months:
        M = [h for h in H if h["date"].startswith(ym)]
        g = [h["g95"] for h in M]; d = [h["die"] for h in M if "die" in h]
        avg = lambda xs: sum(xs) / len(xs)
        lo_g = min(M, key=lambda h: h["g95"]); hi_g = max(M, key=lambda h: h["g95"])
        path = f"/precio-gasolina-hoy/{mslug(ym)}/"
        FUEL_MONTH_URLS.append(path)
        i = months.index(ym)
        nav = " · ".join(([f'<a href="/precio-gasolina-hoy/{mslug(months[i-1])}/">← {mname(months[i-1])}</a>'] if i else []) + ([f'<a href="/precio-gasolina-hoy/{mslug(months[i+1])}/">{mname(months[i+1])} →</a>'] if i + 1 < len(months) else []))
        faq = [(f"¿Cuánto costó de media la gasolina en {mname(ym)}?", f"La gasolina 95 costó de media {fprice(avg(g))} el litro en los {len(M)} días con datos, y el diésel {fprice(avg(d))}."),
               (f"¿Qué día fue más barata la gasolina en {mname(ym)}?", f'El {ddmm(lo_g["date"])}, con {fprice(lo_g["g95"])} el litro de gasolina 95. El día más caro fue el {ddmm(hi_g["date"])}, con {fprice(hi_g["g95"])}.')]
        body = f"""{crumbs(("/precio-gasolina-hoy/", "Precio de la gasolina hoy"), (None, mname(ym).capitalize()))}{FCSS}
<section class="tight"><div class="wrap narrow">
 <h1>Precio de la gasolina en {mname(ym)}</h1>
 <p class="lead" style="margin-top:12px">En {mname(ym)}, la gasolina 95 costó de media <b>{fprice(avg(g))}</b> el litro y el diésel <b>{fprice(avg(d))}</b>. El día más barato para la gasolina fue el {ddmm(lo_g["date"])} ({fprice(lo_g["g95"])}) y el más caro, el {ddmm(hi_g["date"])} ({fprice(hi_g["g95"])}).</p>
 {fuel_chart(M, f"Precio de la gasolina 95 y el diésel en {mname(ym)}")}
</div></section>
<section class="tight"><div class="wrap narrow">
 <div class="sec-head"><div><h2>Precio día a día</h2><p>Media de España en euros por litro. {len(M)} días con datos.</p></div><a href="/precio-gasolina-hoy/">Precio de hoy →</a></div>
 {fuel_table(M)}
 <p class="muted" style="margin-top:12px">{nav}</p>
 <h2 style="margin:28px 0 12px;font-size:1.3rem">Preguntas frecuentes</h2>{faq_box(faq)}
 <p class="note" style="margin-top:16px">Datos del Ministerio para la Transición Ecológica, recogidos cada mañana por Kilómetro Real. Cuánto gasta tu coche con estos precios: <a href="/calculadoras/coste-viaje-gasolina/">calculadora de coste de un viaje</a> y <a href="/mejores/coches-que-menos-gastan/">coches que menos gastan</a>.</p>
</div></section>"""
        page(path, f"Precio de la gasolina en {mname(ym)}", f"Precio medio de la gasolina 95 ({fprice(avg(g))}) y el diésel ({fprice(avg(d))}) en {mname(ym)}, día a día, con el día más barato y el más caro.", body, "", ldj(faq_ld(faq)))
    return months


# ---------------- PRECIO DE LA GASOLINA POR PROVINCIA ----------------
# provincias.json lo genera cada mañana la GitHub Action precios-provincias.yml (tools/provincias.py) con la API del Ministerio.
def load_prov():
    f = os.path.join(HERE, "provincias.json")
    if not os.path.exists(f): return None
    try: return json.load(open(f, encoding="utf-8"))
    except Exception: return None
PROVD = load_prov()
def pdate(d): return f"{int(d[8:10])} de {MESES[int(d[5:7]) - 1]} de {d[:4]}" if d else ""
def pcts(a, b):
    d = (a - b) * 100
    if abs(d) < 0.05: return "igual que la media de España"
    return f'{abs(d):.1f} céntimos {"más cara" if d > 0 else "más barata"} que la media de España'.replace(".", ",")

def prov_section():
    if not PROVD: return ""
    rows = "".join(f'<tr><td><a href="/precio-gasolina-hoy/{P["slug"]}/">{P["name"]}</a></td><td class="n">{fprice(P["avg"]["g95"]) if P["avg"].get("g95") else "-"}</td><td class="n">{fprice(P["avg"]["die"]) if P["avg"].get("die") else "-"}</td><td class="n hm">{fprice(P["cheap"]["g95"][0]["g95"]) if P["cheap"].get("g95") else "-"}</td></tr>' for P in sorted(PROVD["prov"], key=lambda P: P["name"]))
    return f"""<section class="tight"><div class="wrap narrow">
 <div class="sec-head"><div><h2>Precio de la gasolina por provincia</h2><p>Media de {PROVD["n"]:,} gasolineras, {pdate(PROVD["date"])}. Toca tu provincia para ver las gasolineras más baratas.</p></div></div>
 <div class="tablewrap"><table class="list fit"><thead><tr><th>Provincia</th><th class="n">Gasolina 95</th><th class="n">Diésel</th><th class="n hm">La más barata</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>""".replace(f'{PROVD["n"]:,}', f'{PROVD["n"]:,}'.replace(",", "."))

def st_table(L, k):
    def maps(s):
        if s.get("lat") and s.get("lon"): return f'<a href="https://www.google.com/maps/search/?api=1&query={s["lat"]},{s["lon"]}" rel="nofollow noopener" target="_blank">Cómo llegar</a>'
        return ""
    rows = "".join(f'<tr><td class="n">{i}</td><td><b>{esc(s["r"])}</b><br><small class="muted">{esc(s["d"])}, {esc(s["l"])}</small></td><td class="n"><b>{fprice(s[k])}</b><br><small>{maps(s)}</small></td></tr>' for i, s in enumerate(L, 1))
    return f'<div class="tablewrap"><table class="list fit"><thead><tr><th class="n">#</th><th>Gasolinera</th><th class="n">Litro</th></tr></thead><tbody>{rows}</tbody></table></div>'

def build_fuel_prov():
    if not PROVD: return
    N = PROVD["nac"]; dt = pdate(PROVD["date"]); allp = sorted(PROVD["prov"], key=lambda P: P["name"])
    rank = {P["slug"]: i for i, P in enumerate(sorted([P for P in PROVD["prov"] if P["avg"].get("g95")], key=lambda P: P["avg"]["g95"]), 1)}
    nprov = len(rank)
    picks = [BY[i] for i in ("seat-ibiza-1-0-tsi", "toyota-corolla-hybrid", "volkswagen-golf-2-0-tdi") if i in BY]
    for P in PROVD["prov"]:
        A = P["avg"]; name = P["name"]; path = f"/precio-gasolina-hoy/{P['slug']}/"
        if not A.get("g95") or not P["cheap"].get("g95"): continue
        FUEL_MONTH_URLS.append(path)
        cg = P["cheap"]["g95"][0]; cd = P["cheap"].get("die", [None])[0]
        save = (A["g95"] - cg["g95"]) * 50
        tiles = "".join(f'<div><span>{n}</span><b>{fprice(A[k])}</b><small>media de {P["n"]} gasolineras</small></div>' for n, k in (("Gasolina 95", "g95"), ("Diésel", "die"), ("Gasolina 98", "g98"), ("GLP (autogás)", "glp")) if A.get(k))
        def p100(c): return f'{c["c"] * (A["die"] if c["f"] == "d" else A["g95"]):.2f}'.replace(".", ",")
        cars = "".join(f'<li><a href="{curl(c)}">{esc(c["n"])}</a>: {p100(c)} € cada 100 km</li>' for c in picks if c["t"] not in ("ev", "phev"))
        muni = "".join(f'<tr><td>{esc(m["l"])}</td><td class="n">{fprice(m["g95"])}</td><td class="n">{fprice(m["die"])}</td><td class="n hm">{m["n"]}</td></tr>' for m in P["muni"][:8])
        big = ", ".join(f'{esc(m["l"])} ({fprice(m["g95"])})' for m in P.get("big", [])[:4])
        others = " · ".join(f'<a href="/precio-gasolina-hoy/{Q["slug"]}/">{Q["name"]}</a>' for Q in allp if Q["slug"] != P["slug"])
        faq = [(f"¿Cuánto cuesta hoy la gasolina en {name}?", f"De media, {fprice(A['g95'])} el litro de gasolina 95 y {fprice(A['die']) if A.get('die') else '-'} el de diésel, según los precios de {P['n']} gasolineras publicados por el Ministerio el {dt}."),
               (f"¿Cuál es la gasolinera más barata de {name} hoy?", f"Para gasolina 95, {cg['r']} en {cg['d']} ({cg['l']}), a {fprice(cg['g95'])} el litro." + (f" Para diésel, {cd['r']} en {cd['d']} ({cd['l']}), a {fprice(cd['die'])}." if cd else "")),
               (f"¿Cuánto me ahorro repostando en la más barata?", f"Llenar 50 litros de gasolina 95 en la gasolinera más barata de {name} cuesta unos {eur(round(cg['g95'] * 50))}, unos {f'{save:.2f}'.replace('.', ',')} € menos que pagando el precio medio.")]
        body = f"""{crumbs(("/precio-gasolina-hoy/", "Precio de la gasolina hoy"), (None, name))}{FCSS}
<section class="tight"><div class="wrap narrow">
 <h1>Precio de la gasolina hoy en {name}</h1>
 <p class="lead" style="margin-top:12px">A {dt}, la gasolina 95 cuesta de media <b>{fprice(A["g95"])}</b> el litro en {name}{(f' y el diésel <b>{fprice(A["die"])}</b>') if A.get("die") else ""}. Es {pcts(A["g95"], N["g95"])}: {name} es la provincia número {rank[P["slug"]]} de {nprov} de la más barata a la más cara.</p>
 <div class="fuelgrid">{tiles}</div>
 <p class="note" style="margin-top:10px">Precios de {P["n"]} gasolineras de venta al público en {name}. Fuente: Ministerio para la Transición Ecológica (Geoportal de gasolineras). Actualizado cada mañana.</p>
</div></section>
<section class="tight"><div class="wrap narrow">
 <div class="sec-head"><div><h2>Gasolineras más baratas de {name}: gasolina 95</h2><p>Las 10 más baratas hoy. Repostar en la primera te ahorra unos {f"{save:.2f}".replace(".", ",")} € por depósito de 50 litros frente a la media.</p></div></div>
 {st_table(P["cheap"]["g95"], "g95")}
</div></section>
{('<section class="tight"><div class="wrap narrow"><div class="sec-head"><div><h2>Gasolineras más baratas de ' + name + ': diésel</h2><p>Las 10 más baratas hoy para gasóleo A.</p></div></div>' + st_table(P["cheap"]["die"], "die") + '</div></section>') if P["cheap"].get("die") else ""}
{ad("prov")}
<section class="tight"><div class="wrap narrow">
 {('<div class="sec-head"><div><h2>Municipios con la gasolina más barata</h2><p>Media de los municipios de ' + name + ' con 3 o más gasolineras.' + (' En las localidades con más gasolineras: ' + big + '.' if big else '') + '</p></div></div><div class="tablewrap"><table class="list fit"><thead><tr><th>Municipio</th><th class="n">Gasolina 95</th><th class="n">Diésel</th><th class="n hm">Gasolineras</th></tr></thead><tbody>' + muni + '</tbody></table></div>') if muni else ""}
 <h2 style="margin:28px 0 12px;font-size:1.3rem">Lo que cuestan 100 km en {name}</h2>
 <ul>{cars}</ul>
 <p class="muted">Calcula tu trayecto con la <a href="/calculadoras/coste-viaje-gasolina/">calculadora de coste de un viaje</a>, mira los <a href="/mejores/coches-que-menos-gastan/">coches que menos gastan</a> o la <a href="/precio-gasolina-hoy/">media de España hoy</a>.</p>
 <h2 style="margin:28px 0 12px;font-size:1.3rem">Preguntas frecuentes</h2>{faq_box(faq)}
 <h2 style="margin:28px 0 12px;font-size:1.1rem">Precio de la gasolina en otras provincias</h2>
 <p class="muted" style="line-height:1.9">{others}</p>
</div></section>"""
        _pc = [f"Precio gasolina hoy en {name}: desde {fprice(cg['g95'])} en la más barata", f"Precio gasolina hoy en {name}: desde {fprice(cg['g95'])}", f"Gasolina hoy en {name}: desde {fprice(cg['g95'])}"]
        _pt = next((x for x in _pc if len(x) <= 62), _pc[-1])
        _dd = dt.rsplit(" de ", 1)[0]
        page(path, f"Precio de la gasolina hoy en {name}: {fprice(A['g95'])} y las más baratas",
             f"Hoy, {_dd}: gasolina 95 a {fprice(A['g95'])} de media en {name}. La más barata, {cg['r']} en {cg['l']}, a {fprice(cg['g95'])}. Ranking de las 10 más baratas.",
             body, "", ldj(faq_ld(faq)), full_title=_pt)

# ---------------- PRECIO DE LA GASOLINA HOY ----------------
def build_fuel():
    F = FUELP
    H = load_fuel_hist()
    months = build_fuel_months(H)
    build_fuel_prov()
    def delta(now, before):
        d = now - before
        if abs(d) < 0.0005: return '<span class="muted">igual que hace unos días</span>'
        return f'<span class="{"bad" if d > 0 else "good"}-t">{"+" if d > 0 else "−"}{abs(d)*100:.1f} cts frente al {F["prev"]["date"][8:10]}/{F["prev"]["date"][5:7]}</span>'
    tiles = [("Gasolina 95", F["g95"], delta(F["g95"], F["prev"]["g95"])), ("Diésel", F["die"], delta(F["die"], F["prev"]["die"])),
             ("Gasolina 98", F["g98"], ""), ("Diésel premium", F["die_plus"], ""), ("GLP (autogás)", F["glp"], "")]
    tiles_h = "".join(f'<div><span>{n}</span><b>{fprice(v)}</b><small>por litro</small>{("<em>" + d + "</em>") if d else ""}</div>' for n, v, d in tiles)
    tank = "".join(f'<tr><td>{n}</td><td class="n">{eur(round(v*l))}</td><td class="n">{eur(round(v*l2))}</td></tr>' for n, v, l, l2 in
                   [("Gasolina 95", F["g95"], 45, 60), ("Diésel", F["die"], 45, 60), ("GLP", F["glp"], 45, 60)])
    picks = ["dacia-sandero-tce", "seat-ibiza-1-0-tsi", "toyota-yaris-hybrid", "renault-clio-e-tech", "toyota-corolla-hybrid", "seat-leon-1-5-tsi",
             "volkswagen-t-roc-1-5-tsi", "nissan-qashqai-mild-hybrid", "hyundai-tucson-hibrido", "kia-sportage-1-6-crdi", "dacia-duster-eco-g-glp", "mg-zs-hybrid"]
    price = {"g": F["g95"], "d": F["die"], "glp": F["glp"]}
    rows = []
    for i in picks:
        c = BY.get(i)
        if not c or c["t"] in ("ev", "phev"): continue
        p100 = c["c"] * price[c["f"]]
        rows.append((p100, f'<tr><td><a href="{curl(c)}">{esc(c["n"])}</a></td><td class="hm">{FUEL[c["f"]]}</td><td class="n">{str(c["c"]).replace(".", ",")} L</td><td class="n"><b>{eur(round(p100, 2)).replace(" €", "") if False else f"{p100:.2f}".replace(".", ",") + " €"}</b></td><td class="n">{eur(round(p100*150/12))}</td></tr>'))
    rows = "".join(r for _, r in sorted(rows))
    evs = [BY[i] for i in ("dacia-spring", "mg-4-electric", "tesla-model-3-rwd") if i in BY]
    ev_txt = ", ".join(f'{esc(c["n"])} {c["c"]*DEFAULTS["ph"]:.2f} €'.replace(".", ",") for c in evs)
    reb = next((a for a in ARTICLES if "rebaja" in a["slug"]), None)
    src = " · ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{n}</a>' for n, u in F["src"])
    faq = [("¿Cuánto cuesta hoy el litro de gasolina en España?", f'De media, {fprice(F["g95"])} la gasolina 95 y {fprice(F["g98"])} la 98, a {F["dtxt"]}.'),
           ("¿Y el diésel?", f'El gasóleo A cuesta de media {fprice(F["die"])} por litro, y el premium {fprice(F["die_plus"])}.'),
           ("¿Cuánto cuesta llenar el depósito?", f'Un depósito de 50 litros de gasolina 95 sale por unos {eur(round(F["g95"]*50))}, y de diésel por unos {eur(round(F["die"]*50))}.'),
           ("¿Es más barato el GLP?", f'Sí: el litro de GLP cuesta {fprice(F["glp"])}, aunque los coches de GLP gastan algo más de litros que uno de gasolina. Mira el <a href="/coches/dacia-sandero-eco-g-glp/">Sandero GLP</a>.')]
    body = f"""{crumbs((None, "Precio de la gasolina hoy"))}
<section class="tight"><div class="wrap narrow">
 <h1>Precio de la gasolina y el diésel hoy</h1>
 <p class="lead" style="margin-top:12px">A {F["dtxt"]}, la gasolina 95 cuesta de media <b>{fprice(F["g95"])}</b> el litro y el diésel <b>{fprice(F["die"])}</b> en España.</p>
 <div class="fuelgrid">{tiles_h}</div>
 <p class="note" style="margin-top:10px">Precios medios de venta al público en la Península y Baleares. Fuente: {src}.</p>
</div></section>
<section class="tight"><div class="wrap narrow">{FCSS}
 <div class="sec-head"><div><h2>Evolución del precio</h2><p>Gasolina 95 y diésel, día a día. Lo actualizamos cada mañana.</p></div></div>
 {fuel_chart(H, "Evolución del precio de la gasolina 95 y el diésel")}
 <p class="muted" style="margin-top:10px">Histórico por meses: {" · ".join(f'<a href="/precio-gasolina-hoy/{mslug(m)}/">{mname(m)}</a>' for m in reversed(months))}</p>
</div></section>
{prov_section()}
<section class="tight"><div class="wrap narrow">
 <div class="sec-head"><div><h2>Cuánto cuesta llenar el depósito</h2><p>Con los precios medios de hoy.</p></div></div>
 <div class="tablewrap"><table class="list fit"><thead><tr><th>Combustible</th><th class="n">Depósito de 45 L</th><th class="n">Depósito de 60 L</th></tr></thead><tbody>{tank}</tbody></table></div>
</div></section>
<section class="tight"><div class="wrap narrow">
 <div class="sec-head"><div><h2>Lo que cuestan 100 km en los coches más vendidos</h2><p>Con su consumo real estimado y el precio de hoy. Al mes, haciendo 15.000 km al año.</p></div><a href="/calculadoras/coste-viaje-gasolina/">Calcular un viaje →</a></div>
 <div class="tablewrap"><table class="list fit"><thead><tr><th>Coche</th><th class="hm">Combustible</th><th class="n">Consumo</th><th class="n">Cada 100 km</th><th class="n">Al mes</th></tr></thead><tbody>{rows}</tbody></table></div>
 <p class="muted" style="margin-top:12px">Con un eléctrico cargando en casa a 0,15 €/kWh, 100 km cuestan bastante menos: {ev_txt}. {('Más en <a href="/mejores/electricos-mas-baratos/">eléctricos más baratos de tener</a>.')}</p>
</div></section>
<section class="tight"><div class="wrap narrow">
 {('<div class="panel promo"><div><h2>La rebaja del impuesto se reduce cada mes</h2><p>Hasta fin de año el descuento fiscal baja de forma escalonada. Te contamos cuánto puede subir el litro.</p></div><a class="btn" href="' + aurl(reb) + '">Leer la noticia</a></div>') if reb else ''}
 <h2 style="margin:28px 0 12px;font-size:1.3rem">Preguntas frecuentes</h2>{faq_box(faq)}
 <p class="note" style="margin-top:16px">Actualizado el {F["dtxt"]}. Los precios cambian cada día y en cada gasolinera; compara antes de repostar.</p>
</div></section>"""
    _dd = pdate(F["date"]).rsplit(" de ", 1)[0]
    _chg = F["g95"] - F["prev"]["g95"]
    _chg_t = "igual que ayer" if abs(_chg) < 0.0005 else (f'{"sube" if _chg > 0 else "baja"} {abs(_chg)*100:.1f} cts'.replace(".", ","))
    _cheap = min((P for P in (PROVD or {}).get("prov", []) if P["avg"].get("g95")), key=lambda P: P["avg"]["g95"], default=None)
    _ft = f"Precio gasolina hoy {_dd}: {fprice(F['g95'])} y diésel {fprice(F['die'])}"
    page("/precio-gasolina-hoy/", f"Precio de la gasolina hoy: {fprice(F['g95'])} el litro",
         f'Hoy, {_dd}: gasolina 95 a {fprice(F["g95"])} ({_chg_t}) y diésel a {fprice(F["die"])} de media.' + (f' La provincia más barata, {_cheap["name"]} ({fprice(_cheap["avg"]["g95"])}).' if _cheap else ""),
         body, "", ldj(faq_ld(faq)), full_title=_ft if len(_ft) <= 64 else None)

# ---------------- COMPARATIVAS A vs B ----------------
def vs_slug(a, b): return f"/comparar/{a}-vs-{b}/"

def build_vs():
    cards = []
    for a_id, b_id in VS_PAIRS:
        A, B = BY[a_id], BY[b_id]; ka, kb = K[a_id], K[b_id]
        W, L = (A, B) if ka["perKm"] <= kb["perKm"] else (B, A)
        kw, kl = K[W["id"]], K[L["id"]]
        save = kl["total"] - kw["total"]
        same = abs(save) < 300
        biggest = max(("dep", "pérdida de valor"), ("energy", "energía"), ("ins", "seguro"), ("mnt", "mantenimiento"), key=lambda x: abs(kl[x[0]] - kw[x[0]]))
        rows = [("Precio de tarifa", eur(A["p"]), eur(B["p"])), ("Coste por km", pk(ka["perKm"]) + " €", pk(kb["perKm"]) + " €"),
                ("Al mes", eur(ka["month"]), eur(kb["month"])), ("En 5 años", eur(ka["total"]), eur(kb["total"])),
                ("Pérdida de valor", eur(ka["dep"]), eur(kb["dep"])), ("Energía", eur(ka["energy"]), eur(kb["energy"])),
                ("Seguro", eur(ka["ins"]), eur(kb["ins"])), ("Mantenimiento", eur(ka["mnt"]), eur(kb["mnt"])),
                ("Tecnología", TYPE[A["t"]], TYPE[B["t"]]), ("Etiqueta DGT", {"cero": "CERO", "eco": "ECO", "c": "C"}[A["lab"]], {"cero": "CERO", "eco": "ECO", "c": "C"}[B["lab"]]),
                ("Potencia", f'{A["cv"]} CV', f'{B["cv"]} CV'), ("Maletero", tl(A), tl(B))]
        tbl = "".join(f'<tr><th>{n}</th><td class="n">{x}</td><td class="n">{y}</td></tr>' for n, x, y in rows)
        verdict = (f'Salen prácticamente igual: la diferencia es de apenas {eur(abs(save))} en 5 años. Decide por gusto, espacio o etiqueta.' if same else
                   f'El <b>{esc(W["n"])}</b> te ahorra <b>{eur(save)}</b> en 5 años, unos <b>{eur(save/60)} al mes</b>. Donde más se nota es en la {biggest[1]}.')
        cheaper_buy = A if A["p"] < B["p"] else B
        kc = K[cheaper_buy["id"]]; ko = K[(B if cheaper_buy is A else A)["id"]]
        why = [w for key, w in (("dep", "pierde más valor"), ("energy", "gasta más en energía"), ("ins", "paga más de seguro"), ("mnt", "cuesta más de mantener")) if kc[key] > ko[key]]
        why_t = (", ".join(why[:-1]) + " y " + why[-1]) if len(why) > 1 else (why[0] if why else "")
        twist = "" if cheaper_buy["id"] == W["id"] or same or not why_t else f' Ojo: el {esc(cheaper_buy["n"])} es más barato de comprar, pero acaba costando más porque {why_t}.'
        faq = [(f'¿Qué es más barato, el {A["n"]} o el {B["n"]}?', f'Con 15.000 km al año durante 5 años, el {W["n"]} cuesta {pk(kw["perKm"])} €/km y el {L["n"]} {pk(kl["perKm"])} €/km.'),
               (f'¿Cuánto cuesta al mes el {A["n"]}?', f'Unos {eur(ka["month"])} al mes sumando pérdida de valor, energía, seguro, mantenimiento e impuesto.'),
               (f'¿Cuánto cuesta al mes el {B["n"]}?', f'Unos {eur(kb["month"])} al mes con el mismo cálculo.')]
        rel = [p for p in VS_PAIRS if (p != (a_id, b_id)) and (a_id in p or b_id in p)][:4]
        rel_h = "".join(f'<a class="chip" href="{vs_slug(x, y)}">{esc(BY[x]["n"])} vs {esc(BY[y]["n"])}</a>' for x, y in rel)
        body = f"""{crumbs(("/comparar/", "Comparativas"), (None, f'{A["n"]} vs {B["n"]}'))}
<section class="tight"><div class="wrap narrow">
 <h1>{esc(A["n"])} vs {esc(B["n"])}: ¿cuál sale más barato?</h1>
 <p class="lead" style="margin-top:12px">{verdict}{twist}</p>
 <div class="vsduo">
  <a class="vside{' win' if W['id']==A['id'] and not same else ''}" href="{curl(A)}">{('<span class="crownb">Más barato</span>') if W['id']==A['id'] and not same else ''}<span class="nm">{esc(A["n"])}</span><b>{pk(ka["perKm"])} €<small>/km</small></b><span class="muted">{eur(ka["month"])} al mes</span></a>
  <span class="vsx">VS</span>
  <a class="vside{' win' if W['id']==B['id'] and not same else ''}" href="{curl(B)}">{('<span class="crownb">Más barato</span>') if W['id']==B['id'] and not same else ''}<span class="nm">{esc(B["n"])}</span><b>{pk(kb["perKm"])} €<small>/km</small></b><span class="muted">{eur(kb["month"])} al mes</span></a>
 </div>
 <p style="margin-top:18px"><a class="btn" href="/comparador/#{a_id}-vs-{b_id}">Cambiar kilómetros y años</a></p>
</div></section>
<section class="tight"><div class="wrap narrow">
 <h2 style="margin-bottom:12px">Cara a cara</h2>
 <div class="tablewrap"><table class="specs vs"><thead><tr><th></th><th class="n">{esc(A["n"])}</th><th class="n">{esc(B["n"])}</th></tr></thead><tbody>{tbl}</tbody></table></div>
 <p class="note" style="margin-top:10px">15.000 km al año durante 5 años. Precio de tarifa sin descuentos ni ayudas; consumo real estimado; carburantes a precio medio del {FUELP["dtxt"]}. <a href="/metodologia/">Cómo calculamos</a>.</p>
 <h2 style="margin:28px 0 12px;font-size:1.3rem">Preguntas frecuentes</h2>{faq_box(faq)}
 {('<h2 style="margin:28px 0 12px;font-size:1.3rem">Otras comparativas</h2><div class="chips">' + rel_h + '</div>') if rel_h else ''}
</div></section>"""
        _vc = [f'{A["n"]} vs {B["n"]}: cuál es más barato de tener', f'{A["n"]} vs {B["n"]}: ¿cuál es más barato?', f'{A["n"]} vs {B["n"]}: ¿cuál conviene?', f'{A["n"]} vs {B["n"]}']
        page(vs_slug(a_id, b_id), next((x for x in _vc if len(x) <= 60), _vc[-1]), (f'{A["n"]} o {B["n"]}: salen casi igual, apenas {eur(abs(save))} de diferencia en 5 años. Precio, consumo real, seguro, taller y pérdida de valor, cara a cara.' if same else f'El {W["n"]} te ahorra {eur(save)} en 5 años frente al {L["n"]}, unos {eur(save/60)} al mes. Precio, consumo, seguro, taller y pérdida de valor, cara a cara.'),
             body, "coches", ldj(faq_ld(faq)))
        cards.append(f'<a class="card" href="{vs_slug(a_id, b_id)}"><h3>{esc(A["n"])} <span class="muted">vs</span> {esc(B["n"])}</h3><p>{"Casi empate" if same else esc(W["n"]) + " ahorra " + eur(save) + " en 5 años"}</p></a>')
    page("/comparar/", "Comparativas de coches por coste real", "Los duelos más buscados de coches en España, comparados en euros por kilómetro: cuál sale más barato de tener y cuánto ahorras.",
         f'{crumbs((None, "Comparativas"))}<section class="tight"><div class="wrap"><h1>Comparativas</h1><p class="muted" style="margin:10px 0 24px;max-width:62ch">Los cruces que más se buscan, resueltos con el coste real: compra, pérdida de valor, energía, seguro, taller e impuesto.</p><div class="vsfind needs-js"><label class="lbl" for="vsq">Busca un coche o una marca</label><input type="search" id="vsq" placeholder="Ej.: Sandero, Tesla, MG…"><span class="muted" id="vsn">{len(cards)} comparativas</span></div><div class="cards c3" id="vsl">{"".join(cards)}</div><p class="muted" id="vs0" hidden>No hay comparativas con ese coche. Prueba en el <a href="/comparador/">comparador</a>, que cruza cualquier pareja.</p></div></section><script>(function(){{var q=document.getElementById("vsq"),l=document.getElementById("vsl"),n=document.getElementById("vsn"),z=document.getElementById("vs0");if(!q)return;var c=[].slice.call(l.children),f=function(s){{return s.normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase()}};q.addEventListener("input",function(){{var v=f(q.value.trim()),k=0;c.forEach(function(e){{var m=!v||f(e.textContent).indexOf(v)>-1;e.hidden=!m;if(m)k++}});n.textContent=k+(k==1?" comparativa":" comparativas");z.hidden=k>0}})}})();</script>', "coches")

# ---------------- ¿CUÁNTO ME CUESTA MI COCHE? ----------------
def build_micoche():
    body = f"""{crumbs((None, "¿Cuánto me cuesta mi coche?"))}
<section class="tight"><div class="wrap narrow">
 <h1>¿Cuánto te cuesta tu coche de verdad?</h1>
 <p class="lead" style="margin-top:12px">Elige tu coche y cuántos kilómetros haces. Te decimos lo que te cuesta al mes sumándolo todo, y cuánto ahorrarías con otro.</p>
 <form class="tool micoche needs-js" id="micoche" autocomplete="off">
  <div class="mc-grid">
   <div class="mc-car"><label class="lbl" for="mc-car">Tu coche (o el que quieres)</label><input type="text" id="mc-car" list="cars" placeholder="Escribe la marca o el modelo, por ejemplo Seat Ibiza" required></div>
   <div><label class="lbl" for="mc-km">Km al año</label><select id="mc-km"><option value="8000">8.000 km</option><option value="10000">10.000 km</option><option value="15000" selected>15.000 km</option><option value="20000">20.000 km</option><option value="30000">30.000 km</option></select></div>
   <div><label class="lbl" for="mc-y">Años que lo tendrás</label><select id="mc-y"><option value="3">3 años</option><option value="5" selected>5 años</option><option value="8">8 años</option></select></div>
  </div>
  <div id="mc-res" aria-live="polite"><p class="muted mc-empty">Escribe tu coche para ver el resultado.</p></div>
 </form>
 <script>window.KR_VS={json.dumps([f"{a}-vs-{b}" for a, b in VS_PAIRS])};</script>
 <p class="note" style="margin-top:12px">Estimación con precio de tarifa, consumo real medio, depreciación media, seguro a terceros ampliado (35 años), taller e impuesto. Carburantes a precio medio del {FUELP["dtxt"]}. <a href="/metodologia/">Cómo calculamos</a>.</p>
</div></section>"""
    faq = [("¿Cuánto cuesta mantener un coche al mes?", "Depende mucho del modelo: entre unos 250 € al mes los urbanos más baratos y más de 1.000 € los deportivos, sumando pérdida de valor, combustible, seguro, taller e impuesto."),
           ("¿Qué gasto pesa más?", "Casi siempre la pérdida de valor: lo que el coche vale menos cada año. Después suele ir el combustible o la electricidad.")]
    body += f'<section class="tight"><div class="wrap narrow"><h2 style="margin-bottom:12px;font-size:1.3rem">Preguntas frecuentes</h2>{faq_box(faq)}</div></section>'
    page("/mi-coche/", "¿Cuánto me cuesta mi coche al mes? Calculadora", "Calcula lo que te cuesta tu coche al mes sumando pérdida de valor, gasolina o luz, seguro, taller e impuesto, y cuánto ahorrarías con otro.",
         body, "calc", ldj({"@type": "WebApplication", "name": "¿Cuánto me cuesta mi coche?", "applicationCategory": "FinanceApplication", "operatingSystem": "Web", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}, faq_ld(faq)))

# ---------------- INFORMES MENSUALES ----------------
def build_informes():
    import glob
    reps = []
    for f in sorted(glob.glob(os.path.join(HERE, "informes", "*.json")), reverse=True):
        with open(f, encoding="utf-8") as fh: reps.append(json.load(fh))
    for i, R in enumerate(reps): build_informe(R, reps[i + 1] if i + 1 < len(reps) else None)
    cards = "".join(f'<a class="card" href="/informes/{R["slug"]}/"><span class="kicker">Informe · {R["mes"]}</span><h3>Lo que cuestan de verdad los 10 coches más vendidos de {R["mes"]}</h3><p>Ventas oficiales cruzadas con nuestro cálculo de coste real.</p></a>' for R in reps)
    page("/informes/", "Informes: el coste real de los coches más vendidos", "Cada mes cruzamos las matriculaciones oficiales con nuestro cálculo de coste real: lo que de verdad cuestan los coches que más compran los españoles.",
         f'{crumbs((None, "Informes"))}<section class="tight"><div class="wrap"><h1>Informes mensuales</h1><p class="muted" style="margin:10px 0 24px;max-width:64ch">Cada mes tomamos los 10 coches más vendidos en España y calculamos lo que cuestan de verdad. Puedes citar cualquier dato enlazando a la página del informe.</p><div class="cards">{cards}</div></div></section>', "noticias")
    return reps

def build_informe(R, prev):
    S = DEFAULTS
    rows = []
    for pos, t in enumerate(R["top"], 1):
        vs = [BY[x] for x in t["ids"] if x in BY]
        acc = min(vs, key=lambda c: c["p"])
        ka = K[acc["id"]]
        mos = [K[c["id"]]["month"] for c in vs]
        rows.append(dict(pos=pos, m=t["m"], u=t["u"], c=acc, k=ka, lo=min(mos), hi=max(mos), vs=vs))
    by_cost = sorted(rows, key=lambda r: r["k"]["month"])
    for i, r in enumerate(by_cost, 1): r["cpos"] = i
    by_price = sorted(rows, key=lambda r: r["c"]["p"])
    for i, r in enumerate(by_price, 1): r["ppos"] = i
    cheap, dear = by_cost[0], by_cost[-1]
    tot_u = sum(r["u"] for r in rows)
    avg = sum(r["k"]["month"] * r["u"] for r in rows) / tot_u
    jump = max(rows, key=lambda r: r["ppos"] - r["cpos"])
    fall = max(rows, key=lambda r: r["cpos"] - r["ppos"])
    share = tot_u / R["total"] * 100
    n = lambda r: esc(r["m"])
    # gráfico de barras (coste al mes, versión de acceso)
    mx = max(r["k"]["month"] for r in rows) * 1.08
    bars = "".join(f'<div class="ibar" tabindex="0" title="{esc(r["c"]["n"])}: {eur(r["k"]["month"])} al mes · {pk(r["k"]["perKm"])} €/km · {r["u"]:,} ventas".replace(",", ".")><span class="ibl"><b>{r["cpos"]}.</b> {n(r)}</span><span class="ibt"><i style="width:{r["k"]["month"]/mx*100:.1f}%"></i></span><span class="ibv">{eur(r["k"]["month"])}</span></div>' for r in by_cost)
    tb = "".join(f'<tr><td class="n">{r["pos"]}</td><td><a href="{curl(r["c"])}">{n(r)}</a><span class="sub">{esc(r["c"]["n"])} · {TYPE[r["c"]["t"]]}</span></td><td class="n hm">{r["u"]:,}</td><td class="n">{eur(r["c"]["p"])}</td><td class="n"><b>{eur(r["k"]["month"])}</b></td><td class="n hm">{pk(r["k"]["perKm"])}</td><td class="n hm">{eur(r["lo"])} a {eur(r["hi"])}</td></tr>'.replace(f'{r["u"]:,}', f'{r["u"]:,}'.replace(",", ".")) for r in rows)
    _dm = round(dear["k"]["month"]) - round(cheap["k"]["month"])
    _cn = {"dep": "pierde menos valor", "energy": "gasta menos en " + "energía", "ins": "tiene un seguro más barato", "mnt": "cuesta menos de taller"}
    _cp = {"dep": "pierde más valor", "energy": "gasta más en " + "energía", "ins": "tiene un seguro más caro", "mnt": "cuesta más de taller"}
    _av = {x: sum(r["k"][x] for r in rows) / len(rows) for x in _cn}
    def _why(r, better):
        ks = sorted(_cn, key=lambda x: (r["k"][x] - _av[x]) * (1 if better else -1))
        ks = [x for x in ks if (r["k"][x] < _av[x]) == better][:2]
        w = [(_cn if better else _cp)[x] for x in ks]
        return " y ".join(w) if w else ""
    concl = [
        f'<b>El más barato de tener es el {n(cheap)}</b>: {eur(cheap["k"]["month"])} al mes en su versión de acceso ({esc(cheap["c"]["n"])}), {pk(cheap["k"]["perKm"])} € por kilómetro.',
        f'<b>El más caro es el {n(dear)}</b>: {eur(dear["k"]["month"])} al mes. Son {eur(_dm)} más cada mes que el {n(cheap)}, unos {eur(_dm * 12 * S["y"])} en {S["y"]} años.',
        f'<b>Quien compró uno de estos 10 coches paga de media {eur(avg)} al mes</b> sumándolo todo, ponderando por las unidades vendidas de cada modelo.',
    ]
    if jump["ppos"] - jump["cpos"] >= 2:
        concl.append(f'<b>La sorpresa es el {n(jump)}</b>: es el {jump["ppos"]}º más barato de comprar, pero el {jump["cpos"]}º más barato de tener. Frente a la media de los diez, {_why(jump, True)}.')
    if fall["cpos"] - fall["ppos"] >= 2:
        concl.append(f'<b>El caso contrario es el {n(fall)}</b>: el {fall["ppos"]}º más barato de comprar, pero baja al {fall["cpos"]}º puesto cuando lo sumas todo: frente a la media de los diez, {_why(fall, False)}.')
    concl.append(f'Entre los 10 suman {num(tot_u)} matriculaciones, el {f"{share:.1f}".replace(".", ",")} % de los {num(R["total"])} turismos vendidos en {R["mes"]}.')
    src = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{esc(t)}</a>' for t, u in R["fuentes"])
    url = f"/informes/{R['slug']}/"
    cite = f'Según el informe de Kilómetro Real ({DOMAIN}{url}), el {cheap["m"]} es el más barato de tener entre los 10 coches más vendidos de {R["mes"]}, con {eur(cheap["k"]["month"])} al mes.'
    faq = [
        (f"¿Cuál es el coche más vendido en España en {R['mes']}?", f"El {rows[0]['m']}, con {rows[0]['u']:,} matriculaciones según los datos de ANFAC.".replace(",", ".")),
        (f"¿Cuál de los coches más vendidos es más barato de tener?", f"El {cheap['m']}: {eur(cheap['k']['month'])} al mes en su versión de acceso, sumando compra, pérdida de valor, energía, seguro, taller e impuesto."),
        ("¿Cómo calculáis el coste real?", f"Con {num(S['km'])} km al año durante {S['y']} años: lo que pierde de valor el coche, el carburante o la electricidad a precio de hoy, un seguro estimado, el mantenimiento y el impuesto de circulación. Todo está explicado en la <a href=\"/metodologia/\">metodología</a>."),
        ("¿Puedo usar estos datos?", "Sí. Puedes citar cualquier cifra de este informe siempre que enlaces a esta página como fuente."),
    ]
    body = f"""{crumbs(("/informes/", "Informes"), (None, R["mes"].capitalize()))}
<section class="tight"><div class="wrap narrow article">
 <span class="kicker">Informe mensual · {R["mes"]}</span>
 <h1>Lo que cuestan de verdad los 10 coches más vendidos de {R["mes"]}</h1>
 <p class="standfirst">Tomamos las matriculaciones oficiales del mes y calculamos lo que cuesta cada coche al mes cuando sumas todo: compra, pérdida de valor, {("carburante o luz")}, seguro, taller e impuesto.</p>
 <div class="bigfig" style="margin:22px 0 8px"><div><b>{eur(cheap["k"]["month"])}</b><span>{n(cheap)}, el más barato de tener</span></div><div><b>{eur(dear["k"]["month"])}</b><span>{n(dear)}, el más caro</span></div><div><b>{eur(avg)}</b><span>media ponderada por ventas</span></div></div>
 <h2 style="margin:30px 0 6px">Coste real al mes, de menos a más</h2>
 <p class="note" style="margin-bottom:14px">Versión de acceso de cada modelo · {num(S["km"])} km al año durante {S["y"]} años · carburantes a precio del {FUELP["dtxt"]}.</p>
 <div class="ichart" role="img" aria-label="Coste real al mes de los 10 coches más vendidos de {R["mes"]}, de menos a más. Los datos completos están en la tabla siguiente.">{bars}</div>
 <h2 style="margin:34px 0 12px">Conclusiones</h2>
 <ul class="iconcl">{"".join(f"<li>{x}</li>" for x in concl)}</ul>
 {ad("informe")}
 <h2 style="margin:34px 0 12px">Los datos completos</h2>
 <div class="tablewrap"><table class="list fit itable"><thead><tr><th class="n">Ventas</th><th>Modelo</th><th class="n hm">Unidades</th><th class="n">Precio</th><th class="n">Al mes</th><th class="n hm">€/km</th><th class="n hm">Todas sus versiones</th></tr></thead><tbody>{tb}</tbody></table></div>
 <p class="note" style="margin-top:10px">Puesto y unidades: matriculaciones de turismos en España en {R["mes"]}. Precio de tarifa de la versión de acceso, sin descuentos ni ayudas. "Todas sus versiones" es el rango de coste al mes del modelo en nuestro comparador.</p>
 <div class="panel icite" style="margin-top:28px"><h3>¿Quieres citar este informe?</h3><p>Puedes usar cualquier dato, gráfico o conclusión enlazando a esta página. Por ejemplo:</p><blockquote id="citetxt">{esc(cite)}</blockquote><button type="button" class="btn" data-copy="#citetxt">Copiar texto</button></div>
 <h2 style="margin:30px 0 12px;font-size:1.3rem">Preguntas frecuentes</h2>{faq_box(faq)}
 <div class="sources">Fuentes de las ventas: {src}. Coste real: cálculo propio de Kilómetro Real (<a href="/metodologia/">metodología</a>).</div>
 <p style="margin-top:22px"><a class="btn primary" href="/mi-coche/">¿Y el tuyo? Calcúlalo</a></p>
</div></section>"""
    art = {"@type": "Article", "headline": f"Lo que cuestan de verdad los 10 coches más vendidos de {R['mes']}", "datePublished": R["fecha"], "dateModified": R["fecha"],
           "author": {"@type": "Organization", "name": SITE, "url": DOMAIN + "/"}, "publisher": {"@type": "Organization", "name": SITE, "logo": {"@type": "ImageObject", "url": DOMAIN + "/icon-512.png"}},
           "mainEntityOfPage": DOMAIN + url, "image": DOMAIN + "/assets/img/og.png?v=2"}
    page(url, f"Coste real de los coches más vendidos de {R['mes_corto']} {R['fecha'][:4]}", f"Los 10 coches más vendidos de {R['mes']} y lo que cuestan de verdad al mes: el {cheap['m']} sale a {eur(cheap['k']['month'])} y el {dear['m']} a {eur(dear['k']['month'])}. Datos de ANFAC y cálculo propio.",
         body, "noticias", ldj(art, faq_ld(faq)))
