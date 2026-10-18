def tle(c):
    return f'{c["trunk"]} L' if c["trunk"] else "Cargo bed"

# -*- coding: utf-8 -*-
# English version. Executed inside build.py (shares its globals): exec(open("en.py").read())
TYPE_EN = {"ev": "Electric", "phev": "Plug-in hybrid", "hev": "Hybrid", "mhev": "Mild hybrid", "ice": "Combustion"}
BODY_EN = {"urbano": "City car", "compacto": "Hatchback", "berlina": "Saloon", "familiar": "Estate", "suv-p": "Small SUV", "suv-m": "Medium SUV", "suv-g": "Large SUV", "monovolumen": "MPV", "deportivo": "Sports car"}
BODY_EN_PL = {"urbano": "city cars", "compacto": "hatchbacks", "berlina": "saloons", "familiar": "estates", "suv-p": "small SUVs", "suv-m": "medium SUVs", "suv-g": "large SUVs", "monovolumen": "MPVs", "deportivo": "sports cars"}
FUEL_EN = {"e": "Electricity", "g": "Petrol", "d": "Diesel", "glp": "LPG"}
LAB_EN = {"cero": "ZERO", "eco": "ECO", "c": "C"}
def n_en(v): return f"{round(v):,}"
def e_en(v): return "€" + n_en(v)
def pk_en(v): return f"€{v:.3f}"
def curl_en(c): return f"/en/cars/{c['id']}/"
def typ_en(c): return f'<span class="type t-{c["t"]}">{TYPE_EN[c["t"]]}</span>'
RANK_EN = {"coches-etiqueta-eco-mas-baratos": ("cheapest-eco-label-cars", "The cheapest ECO label cars to own", "Hybrids, mild hybrids and LPG cars with the DGT ECO label, ranked by real cost per kilometre."),
 "coches-que-menos-gastan": ("most-fuel-efficient-cars", "The most fuel-efficient petrol, diesel and hybrid cars", "Ranked by what you spend on fuel every 100 km, with real-world consumption and today's prices."),
 "coches-con-mas-maletero": ("cars-with-biggest-boot", "Cars with the biggest boot", "Models with the most boot space according to the manufacturer, largest first."),
 "coches-seguro-mas-barato": ("cheapest-cars-to-insure", "The cheapest cars to insure", "Ranked by our estimated comprehensive insurance with excess for a 35-year-old driver. Always get several quotes."),
 "coches-glp-mas-baratos": ("cheapest-lpg-cars", "The cheapest LPG cars to own", "Petrol and LPG bi-fuel cars: ECO label and a fuel that costs about half as much as petrol."),
 "coches-diesel-mas-baratos": ("cheapest-diesel-cars", "The cheapest diesel cars to own", "The new diesel cars still on sale, ranked by real cost per kilometre."),
 "coches-gasolina-mas-baratos": ("cheapest-petrol-cars", "The cheapest petrol cars to own", "Non-electrified petrol cars ranked by what they really cost per kilometre."),
 "urbanos-mas-baratos": ("cheapest-city-cars", "The cheapest city cars to own", "Small city cars, petrol, hybrid and electric, ranked by real cost per kilometre."),
 "compactos-mas-baratos": ("cheapest-hatchbacks", "The cheapest hatchbacks to own", "Compact hatchbacks ranked by what they really cost per kilometre."),
 "berlinas-mas-baratas": ("cheapest-saloons", "The cheapest saloons to own", "Saloons of every size ranked by real cost per kilometre."),
 "mas-baratos-por-km": ("cheapest-cars-to-own", "The cheapest cars to own", "Ranked by real cost per kilometre: depreciation, energy, insurance, servicing and tax."),
 "electricos-mas-baratos": ("cheapest-electric-cars", "The cheapest electric cars to own", "Electric cars with the lowest real cost per kilometre, charging mostly at home."),
 "suv-mas-baratos": ("cheapest-suvs", "The cheapest SUVs to own", "Small, medium and large SUVs ranked by what they really cost per kilometre."),
 "hibridos-mas-economicos": ("cheapest-hybrids", "The most economical hybrids", "Hybrids and plug-in hybrids with the lowest real cost: for drivers who don't want to rely on a plug."),
 "electricos-mas-autonomia": ("longest-range-electric-cars", "Electric cars with the longest range", "Ranked by official WLTP range. On the motorway and in the cold, expect quite a bit less."),
 "etiqueta-cero-menos-30000": ("zero-label-cars-under-30000", "ZERO-label cars under €30,000", "Electric and plug-in hybrid cars with a list price under €30,000, before incentives."),
 "coches-chinos-mas-baratos": ("cheapest-chinese-cars", "The cheapest Chinese cars to own", "MG, BYD, Omoda, Jaecoo, Leapmotor, Geely and other Chinese brands ranked by real cost per kilometre."),
 "familiares-y-7-plazas": ("family-and-7-seat-cars", "Estates, MPVs and 7-seat SUVs", "The roomiest cars ranked by real cost, with their boot size."),
 "coches-menos-de-15000-euros": ("best-cars-under-15000-euros", "The best cars under €15,000", "New cars with a list price up to €15,000, ranked by what they really cost per kilometre."),
 "coches-menos-de-20000-euros": ("best-cars-under-20000-euros", "The best cars under €20,000", "New cars with a list price up to €20,000, ranked by what they really cost per kilometre."),
 "coches-menos-de-25000-euros": ("best-cars-under-25000-euros", "The best cars under €25,000", "New cars with a list price up to €25,000, ranked by what they really cost per kilometre."),
 "coches-menos-de-30000-euros": ("best-cars-under-30000-euros", "The best cars under €30,000", "New cars with a list price up to €30,000, ranked by what they really cost per kilometre."),
 "deportivos-mas-baratos": ("cheapest-performance-cars", "The cheapest performance cars to run", "GTI, RS, M, AMG, GR and friends: the most performance-focused cars ranked by real cost per kilometre, with their power.")}
CALC_EN = {"coste-viaje-gasolina": "trip-fuel-cost", "coste-carga-electrico": "ev-charging-cost", "cuota-financiacion-coche": "car-finance-calculator",
           "etiqueta-dgt": "dgt-environmental-label", "amortizacion-electrico": "is-an-electric-car-worth-it"}

def fill_alt():
    ALT.update({"/": "/en/", "/comparador/": "/en/compare/", "/coches/": "/en/cars/", "/mejores/": "/en/rankings/", "/calculadoras/": "/en/calculators/",
                "/cual-me-conviene/": "/en/which-car/", "/quienes-somos/": "/en/about/", "/metodologia/": "/en/methodology/", "/contacto/": "/en/contact/",
                "/privacidad/": "/en/privacy/", "/cookies/": "/en/cookies/", "/condiciones-de-uso/": "/en/terms/"})
    for c in CARS: ALT[curl(c)] = curl_en(c)
    for es, (en_, _, _) in RANK_EN.items(): ALT[f"/mejores/{es}/"] = f"/en/rankings/{en_}/"
    for es, en_ in CALC_EN.items(): ALT[f"/calculadoras/{es}/"] = f"/en/calculators/{en_}/"

def crumbs_en(*items):
    parts = ['<a href="/en/">Home</a>'] + [f'<a href="{h}">{l}</a>' if h else f'<span>{l}</span>' for h, l in items]
    return '<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav></div>"

def car_card_en(c, extra=""):
    k = K[c["id"]]
    return (f'<a class="card" href="{curl_en(c)}">{sil(c)}<div class="meta">{tag(c)}{typ_en(c)}</div><h3>{esc(c["n"])}</h3>{extra}'
            f'<div class="foot"><span class="price">{e_en(c["p"])}</span><span class="perkm"><b>{pk_en(k["perKm"])}</b>/km</span></div></a>')
def rank_li_en(c, right=None):
    k = K[c["id"]]
    right = right or f'<span class="num">{pk_en(k["perKm"])}/km</span>'
    return f'<li><span><a href="{curl_en(c)}">{esc(c["n"])}</a><span class="sub">{TYPE_EN[c["t"]]} · {e_en(c["p"])} · {e_en(k["month"])}/month</span></span>{right}</li>'
SKEL = '<div class="skel" aria-hidden="true"><i></i><i class="s"></i></div>'

def en_home():
    quick = "".join(f'<button type="button" class="chip" data-pair="{a}|{b}">{esc(BY[a]["n"])} vs {esc(BY[b]["n"])}</button>' for a, b in POP_PAIRS[:4])
    def mc(a, b):
        A, B = BY[a], BY[b]; ka, kb = K[a], K[b]; w = A if ka["total"] <= kb["total"] else B
        return (f'<a class="card" href="/en/compare/#{a}-vs-{b}"><div class="match"><span class="who">{esc(A["n"])}</span><span class="num">{pk_en(ka["perKm"])}/km</span>'
                f'<span class="who">{esc(B["n"])}</span><span class="num">{pk_en(kb["perKm"])}/km</span><span class="save">The {esc(w["n"])} saves {e_en(abs(ka["total"]-kb["total"]))} over 5 years</span></div></a>')
    panel = lambda t, s, lst: f'<div class="panel"><h3>{t}</h3><ol class="rank">{"".join(rank_li_en(c) for c in lst)}</ol><p style="margin-top:12px"><a href="/en/rankings/{s}/" style="font-weight:700;text-decoration:none">See all 25 →</a></p></div>'
    calcs = "".join(f'<a class="card calc-card" href="/en/calculators/{CALC_EN[x[0]]}/"><span class="badge">{x[2]}</span><h3>{CALCS_EN[x[0]][0]}</h3></a>' for x in CALCS)
    body = f"""
<section class="hero"><div class="wrap grid">
 <div>
  <h1>What will your next car <em>really</em> cost you?</h1>
  <p class="lead">The price tag is just the start. We add depreciation, fuel or electricity, insurance, servicing and road tax, and give you the answer in euros per kilometre.</p>
  <div class="proof"><span><b>{len(CARS)}</b>models on sale</span><span><b>5</b>costs added up</span><span><b>10 s</b>to compare</span></div>
  <div class="road" aria-hidden="true"><svg class="carmini" viewBox="0 0 220 72"><path fill="currentColor" d="M6 58c0-9 6-13 16-15l28-4c12-12 26-19 46-19h34c14 0 24 7 34 19l14 3c9 2 12 8 12 16z"/><circle cx="56" cy="58" r="11" fill="#0d1726"/><circle cx="166" cy="58" r="11" fill="#0d1726"/></svg></div>
 </div>
 <form class="tool needs-js" id="duel" autocomplete="off">
  <div class="pair">
   <div><label class="lbl" for="qa">Car A</label><input type="text" id="qa" list="cars" value="{esc(BY['dacia-spring']['n'])}" placeholder="Type a model"></div>
   <div class="vs">VS</div>
   <div><label class="lbl" for="qb">Car B</label><input type="text" id="qb" list="cars" value="{esc(BY['hyundai-i10']['n'])}" placeholder="Type another"></div>
  </div>
  <div id="duelres" aria-live="polite">{SKEL}</div>
  <div class="quick"><p class="muted">Try:</p><div class="chips">{quick}</div></div>
 </form>
</div></section>
{ad("portada-1")}
<section><div class="wrap">
 <div class="sec-head"><div><h2>Surprising match-ups</h2><p>At 15,000 km a year over 5 years. Tap any of them to adjust the numbers to you.</p></div><a href="/en/compare/">Open the comparison →</a></div>
 <div class="cards c3">{"".join(mc(a, b) for a, b in POP_PAIRS[4:10])}</div>
</div></section>
<section class="tight"><div class="wrap">
 <div class="sec-head"><div><h2>Calculators</h2><p>The sums every driver does at some point, solved in seconds.</p></div><a href="/en/calculators/">All →</a></div>
 <div class="cards c5">{calcs}</div>
</div></section>
<section class="band"><div class="wrap">
 <div class="sec-head"><div><h2>Rankings</h2><p>The cars that cost you least per kilometre, by category.</p></div><a href="/en/rankings/">All rankings →</a></div>
 <div class="rankgrid">{panel("Cheapest to own", "cheapest-cars-to-own", by_pk(CARS)[:6])}{panel("Electric", "cheapest-electric-cars", by_pk([c for c in CARS if c["t"] == "ev"])[:6])}{panel("SUVs", "cheapest-suvs", by_pk([c for c in CARS if c["body"].startswith("suv")])[:6])}</div>
</div></section>
<section><div class="wrap"><div class="cta"><div><h2>Not sure which one to pick?</h2><p>Answer 4 questions and we'll show you the 3 cars that will cost you least.</p></div><a class="btn" href="/en/which-car/">Take the test</a></div></div></section>
<section class="tight"><div class="wrap"><div class="panel"><h3>News and buying guides</h3><p class="muted" style="margin-top:6px">Our news, market analysis and guides are written in Spanish. <a href="/noticias/" hreflang="es">Read them here</a>.</p></div></div></section>"""
    page("/en/", SITE, f"Compare the real cost of {len(CARS)} new cars on sale in Spain: electric, hybrid and petrol. Euros per kilometre, per month and over 5 years.", body, "",
         {"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": DOMAIN + "/en/", "inLanguage": "en"}, full_title=f"{SITE}: what every car really costs you", lang="en", endcta=False)

def en_compare():
    pop = "".join(f'<li><span><a href="#{a}-vs-{b}">{esc(BY[a]["n"])} vs {esc(BY[b]["n"])}</a></span></li>' for a, b in POP_PAIRS)
    body = f"""{crumbs_en((None, "Compare"))}
<section class="tight" id="comparador"><div class="wrap">
 <h1>Real-cost car comparison</h1>
 <p class="muted" style="margin:10px 0 24px;max-width:62ch">Pick two cars and set your mileage. We'll tell you which one is cheaper and why.</p>
 <div class="cmp">
  <div style="min-width:0">
   <div class="tool needs-js">
    <div class="pair">
     <div><label class="lbl" for="ca">Car A</label><input type="text" id="ca" list="cars" autocomplete="off"></div>
     <button type="button" class="btn ghost" id="swap" aria-label="Swap cars" style="padding:12px 14px">⇄</button>
     <div><label class="lbl" for="cb">Car B</label><input type="text" id="cb" list="cars" autocomplete="off"></div>
    </div>
    <div id="cres" aria-live="polite">{SKEL}</div>
    <p style="margin-top:12px;display:flex;gap:10px;align-items:center;flex-wrap:wrap"><button type="button" class="btn ghost" id="share">Copy link to this comparison</button><span class="muted" id="sharemsg" style="font-size:.9rem"></span></p>
   </div>
   {ad("comparador-1")}
   <div class="panel" style="margin-top:22px"><h3>Where the money goes</h3><div class="breakdown" id="cbars" style="margin-top:12px"></div>
    <div class="legend"><span><i class="c-dep"></i>Depreciation</span><span><i class="c-energy"></i>Energy</span><span><i class="c-ins"></i>Insurance</span><span><i class="c-mnt"></i>Servicing</span><span><i class="c-tax"></i>Road tax</span></div></div>
   <div class="panel" style="margin-top:22px;overflow-x:auto"><h3>Head to head</h3><table class="specs" id="cspecs" style="margin-top:8px"></table><p class="note" style="margin-top:8px">In green, the better of the two for each figure.</p></div>
  </div>
  <aside class="settings">
   <div class="panel">
    <h3 style="margin-bottom:14px">Your driving</h3>
    <div class="settings">
     <div><label class="lbl" for="s-km">Km per year <span class="pval" id="v-km"></span></label><input type="range" id="s-km" min="5000" max="40000" step="1000"></div>
     <div><label class="lbl" for="s-y">Years you'll keep it <span class="pval" id="v-y"></span></label><input type="range" id="s-y" min="2" max="10" step="1"></div>
     <div><label class="lbl" for="s-home">Charging at home <span class="pval" id="v-home"></span></label><input type="range" id="s-home" min="0" max="100" step="5"></div>
     <div class="row"><div><label class="lbl" for="s-gas">Petrol €/L</label><input type="number" id="s-gas" step="0.01" inputmode="decimal"></div><div><label class="lbl" for="s-die">Diesel €/L</label><input type="number" id="s-die" step="0.01" inputmode="decimal"></div></div>
     <div class="row"><div><label class="lbl" for="s-ph">Home power €/kWh</label><input type="number" id="s-ph" step="0.01" inputmode="decimal"></div><div><label class="lbl" for="s-pp">Public charging €/kWh</label><input type="number" id="s-pp" step="0.01" inputmode="decimal"></div></div>
     <div class="row"><div><label class="lbl" for="s-glp">LPG €/L</label><input type="number" id="s-glp" step="0.01" inputmode="decimal"></div></div>
    </div>
   </div>
   <div class="panel hide"><h3>Your recent comparisons</h3><p class="note">Saved only in your browser.</p><div class="recent" id="crecent" style="margin-top:8px"></div></div>
   <div class="panel"><h3>Rivals of car A</h3><p class="note">Same body type, ranked by real cost. Tap to compare.</p><ol class="rank" id="crivals" style="margin-top:6px"></ol></div>
  </aside>
 </div>
</div></section>
<section class="band tight"><div class="wrap two">
 <div class="panel"><h3>Popular comparisons</h3><ol class="rank">{pop}</ol></div>
 <div class="panel"><h3>How we calculate</h3><div class="body" style="font-size:.98rem"><p>We add depreciation, energy, insurance, servicing and road tax. List prices without discounts or incentives, updated in October 2026. Indicative figures. <a href="/en/methodology/">Full method</a>.</p></div></div>
</div></section>"""
    page("/en/compare/", "Real-cost car comparison", f"Compare two cars and find out which one is really cheaper to own. {len(CARS)} models: electric, hybrid, petrol and diesel.", body, "comparador",
         {"@context": "https://schema.org", "@type": "WebApplication", "name": "Real-cost car comparison", "applicationCategory": "FinanceApplication", "operatingSystem": "Web", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}, lang="en", endcta=False)

def en_catalog():
    rows = []
    for c in by_pk(CARS):
        k = K[c["id"]]; rng = f'{c["rng"]} km' if c["t"] in ("ev", "phev") else "—"
        rows.append(f'<tr data-n="{esc(c["n"].lower())}" data-t="{c["t"]}" data-body="{c["body"]}" data-p="{c["p"]}" data-pk="{k["perKm"]:.4f}" data-mo="{k["month"]:.0f}" data-name="{esc(c["n"])}" data-rng="{c["rng"]}" data-cv="{c["cv"]}" data-trunk="{c["trunk"]}">'
                    f'<td><a href="{curl_en(c)}">{esc(c["n"])}</a></td><td>{tag(c)}</td><td>{typ_en(c)}</td><td>{BODY_EN[c["body"]]}</td>'
                    f'<td class="n">{e_en(c["p"])}</td><td class="n"><b>{pk_en(k["perKm"])}</b></td><td class="n">{e_en(k["month"])}</td><td class="n">{rng}</td><td class="n">{c["cv"]}</td><td class="n">{tle(c)}</td></tr>')
    topt = "".join(f'<option value="{k}">{v}</option>' for k, v in TYPE_EN.items())
    bopt = "".join(f'<option value="{k}">{v}</option>' for k, v in BODY_EN.items())
    th = lambda k, l, n="": f'<th class="{n}"><button type="button" data-k="{k}">{l} ↕</button></th>'
    body = f"""{crumbs_en((None, "Cars"))}
<section class="tight"><div class="wrap">
 <h1>All cars</h1>
 <p class="muted" style="margin:10px 0 22px;max-width:64ch">{len(CARS)} new cars on sale in Spain, ranked by what they really cost per kilometre. Filter, sort and open each car's page.</p>
 <div class="filters">
  <div class="q"><label class="lbl" for="f-q">Search</label><input type="search" id="f-q" placeholder="Make or model"></div>
  <div><label class="lbl" for="f-t">Powertrain</label><select id="f-t"><option value="">All</option>{topt}</select></div>
  <div><label class="lbl" for="f-b">Body type</label><select id="f-b"><option value="">All</option>{bopt}</select></div>
  <div><label class="lbl" for="f-p">Max price</label><select id="f-p"><option value="">No limit</option><option value="20000">€20,000</option><option value="25000">€25,000</option><option value="30000">€30,000</option><option value="40000">€40,000</option><option value="50000">€50,000</option></select></div>
 </div>
 <p class="count" id="f-count">{len(CARS)} models</p>
 <div class="tablewrap" id="catalogo"><table class="list"><thead><tr>{th("name","Model")}<th>Label</th><th>Powertrain</th><th>Body</th>{th("p","Price","n")}{th("pk","€/km","n")}{th("mo","Per month","n")}{th("rng","Range","n")}{th("cv","hp","n")}{th("trunk","Boot","n")}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>
 <p class="note" style="margin-top:10px">Cost at 15,000 km a year over 5 years. Indicative list prices without discounts.</p>
</div></section>"""
    page("/en/cars/", "All new cars on sale in Spain and their real cost", f"Catalogue of {len(CARS)} new cars in Spain with price, cost per km, monthly cost, range, power and boot size.", body, "coches", lang="en")

def en_car(c):
    k = K[c["id"]]
    rivals = by_pk(sorted([x for x in CARS if x["body"] == c["body"] and x["id"] != c["id"]], key=lambda x: abs(x["p"] - c["p"]))[:6])
    same = by_pk([x for x in CARS if x["body"] == c["body"]]); pos = same.index(c) + 1
    rank = f"{pos}{'st' if pos % 10 == 1 and pos != 11 else 'nd' if pos % 10 == 2 and pos != 12 else 'rd' if pos % 10 == 3 and pos != 13 else 'th'} cheapest" if pos <= (len(same) + 1) // 2 else f"{len(same) - pos + 1}{'st' if (len(same) - pos + 1) % 10 == 1 and (len(same) - pos + 1) != 11 else 'nd' if (len(same) - pos + 1) % 10 == 2 and (len(same) - pos + 1) != 12 else 'rd' if (len(same) - pos + 1) % 10 == 3 and (len(same) - pos + 1) != 13 else 'th'} most expensive"
    parts = {"depreciation": k["dep"], "energy": k["energy"], "insurance": k["ins"], "servicing": k["mnt"]}; big = max(parts, key=parts.get)
    mx = k["total"]
    segs = "".join(f'<span class="{cl}" style="width:{k[x]/mx*100:.1f}%"></span>' for x, cl in [("dep", "c-dep"), ("energy", "c-energy"), ("ins", "c-ins"), ("mnt", "c-mnt"), ("tax", "c-tax")])
    plugin = c["t"] in ("ev", "phev")
    cons = f'{c["c"]} {"kWh" if c["t"] == "ev" else "L"}/100 km' + (" in hybrid mode" if c["t"] == "phev" else "")
    specs = [("List price", e_en(c["p"])), ("Powertrain", TYPE_EN[c["t"]]), ("Fuel", FUEL_EN[c["f"]] + (" and electricity" if c["t"] == "phev" else "")), ("Body type", BODY_EN[c["body"]]),
             ("Power", f'{c["cv"]} hp'), ("Estimated real consumption", cons), ("Boot", tle(c)), ("DGT label", LAB_EN[c["lab"]])]
    if c["t"] == "ev": specs[5:5] = [("Battery", f'{c["bat"]} kWh'), ("WLTP range", f'{c["rng"]} km')]
    if c["t"] == "phev": specs[5:5] = [("Battery", f'{c["bat"]} kWh'), ("WLTP electric range", f'{c["rng"]} km')]
    an = [f'Of the {len(same)} {BODY_EN_PL[c["body"]]} in our comparison, the {c["n"]} is the <strong>{rank} to own</strong>.',
          f'Its biggest cost is <strong>{big}</strong>: {e_en(parts[big])} over 5 years, {round(parts[big] / k["total"] * 100)}% of the total.']
    if c["t"] == "ev": an.append(f'A full charge of its {c["bat"]} kWh battery costs about {e_en(c["bat"] * 0.15 * 1.1)} at home, and 100 km about €{c["c"] * 0.15 * 1.1:.2f}.')
    elif c["t"] != "phev": an.append(f'At a real consumption of {c["c"]} L/100 km, every 100 km costs about €{c["c"] * {"g": FUELP["g95"], "d": FUELP["die"], "glp": FUELP["glp"]}[c["f"]]:.2f} in fuel.')
    faq = [(f"How much does a {c['n']} cost per month?", f"About {e_en(k['month'])} a month at 15,000 km a year over 5 years, including depreciation, energy, insurance, servicing and road tax. That's {pk_en(k['perKm'])} per km."),
           (f"Which DGT label does the {c['n']} have?", f"The {LAB_EN[c['lab']]} label.")]
    if c["t"] == "ev": faq.insert(1, (f"How much does it cost to charge the {c['n']}?", f"A full charge of its {c['bat']} kWh battery costs about {e_en(c['bat'] * 0.15 * 1.1)} at home at €0.15/kWh and {e_en(c['bat'] * 0.49)} at a public charger at €0.49/kWh."))
    faqh = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    calc_home = '<div><label class="lbl" for="cc-in-home">Charging at home <span class="pval" id="cc-home"></span></label><input type="range" id="cc-in-home" min="0" max="100" step="5" value="80"></div>' if plugin else ""
    rv = "".join(car_card_en(x, f'<p>{"Saves you" if K[x["id"]]["total"] < k["total"] else "Costs"} {e_en(abs(K[x["id"]]["total"] - k["total"]))} {"" if K[x["id"]]["total"] < k["total"] else "more "}over 5 years</p>') for x in rivals)
    body = f"""{crumbs_en(("/en/cars/", "Cars"), (None, c["n"]))}
<div class="wrap carhead">
 <div>
  <span class="eyebrow">{BODY_EN[c["body"]]} · {TYPE_EN[c["t"]]}</span>
  <h1 style="margin-top:10px">{esc(c["n"])}</h1>
  <div style="display:flex;gap:8px;align-items:center;margin-top:12px">{tag(c)}<span class="muted">{LAB_EN[c["lab"]]} label</span></div>
  <p style="font-size:1.12rem;margin-top:14px;color:var(--ink2)">Keeping it 5 years and driving 15,000 km a year costs you about <strong>{e_en(k["month"])} a month</strong>, all in.</p>
  <div class="bigfig"><div><b>{pk_en(k["perKm"])}</b><span>per kilometre</span></div><div><b>{e_en(k["month"])}</b><span>per month</span></div><div><b>{e_en(k["total"])}</b><span>over 5 years</span></div></div>
  <div class="sharebar"><a class="btn" href="/en/compare/#{c["id"]}-vs-{(rivals[0] if rivals else c)["id"]}">Compare with another car</a></div>
  <div style="margin-top:14px">{sharebuttons(curl_en(c), f"The {c['n']} really costs {e_en(k['month'])} a month:", True)}</div>
 </div>
 <div class="panel" id="carcalc" data-id="{c["id"]}">
  {photo_hero(c, True)}
  <h3 style="margin-top:10px">Work it out for your driving</h3>
  <div class="settings" style="margin-top:12px">
   <div><label class="lbl" for="cc-in-km">Km per year <span class="pval" id="cc-km">15,000</span></label><input type="range" id="cc-in-km" min="5000" max="40000" step="1000" value="15000"></div>
   {calc_home}
  </div>
  <div class="bigfig" style="grid-template-columns:repeat(3,minmax(0,1fr))"><div><b id="cc-pk">{pk_en(k["perKm"])}</b><span>per km</span></div><div><b id="cc-mo">{e_en(k["month"])}</b><span>per month</span></div><div><b id="cc-tot">{e_en(k["total"])}</b><span>5 years</span></div></div>
 </div>
</div>
{ad("ficha-1")}
<section class="tight"><div class="wrap two">
 <div class="panel"><h3>Where the money goes over 5 years</h3><div class="bar" style="margin-top:14px;height:18px">{segs}</div>
  <table class="specs" style="margin-top:12px"><tbody><tr><th>Depreciation</th><td>{e_en(k["dep"])}</td></tr><tr><th>{"Electricity" if c["t"] == "ev" else "Energy"}</th><td>{e_en(k["energy"])}</td></tr><tr><th>Insurance</th><td>{e_en(k["ins"])}</td></tr><tr><th>Servicing</th><td>{e_en(k["mnt"])}</td></tr><tr><th>Road tax</th><td>{e_en(k["tax"])}</td></tr></tbody></table>
  <p class="note" style="margin-top:10px">You'd sell it for about {e_en(k["resid"])} after 5 years.</p></div>
 <div class="panel"><h3>Specifications</h3><table class="specs" style="margin-top:6px"><tbody>{"".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in specs)}</tbody></table></div>
</div></section>
<section class="tight"><div class="wrap two">
 <div class="article"><h2 style="margin-bottom:12px">Our analysis</h2><div class="body" style="font-size:1.04rem">{"".join(f"<p>{x}</p>" for x in an)}</div></div>
 <div><h2 style="margin-bottom:12px">FAQ</h2><div class="faq">{faqh}</div></div>
</div></section>
<section class="band tight"><div class="wrap"><div class="sec-head"><div><h2>{esc(c["n"])} rivals</h2><p>{BODY_EN[c["body"]]} models at a similar price, ranked by real cost.</p></div></div><div class="cards">{rv}</div></div></section>
<section class="tight"><div class="wrap"><p class="note">Indicative data updated in October 2026: entry list price without discounts or incentives, estimated real consumption and average depreciation. Check the offer with the dealer.</p></div></section>"""
    schema = {"@context": "https://schema.org", "@graph": [{"@type": "Car", "name": c["n"], "brand": {"@type": "Brand", "name": c["b"]}, "bodyType": BODY_EN[c["body"]], "fuelType": FUEL_EN[c["f"]]},
              {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
    _w = "real-world range" if c["t"] == "ev" else "real fuel economy"
    _cands = [f'{c["n"]} price in Spain 2026: from {e_en(c["p"])} and running costs', f'{c["n"]} price in Spain: from {e_en(c["p"])} and running costs', f'{c["n"]} price in Spain 2026: from {e_en(c["p"])}', f'{c["n"]} price in Spain: from {e_en(c["p"])}', f'{c["n"]}: price and real cost']
    _t = next((x for x in _cands if len(x) <= 62), _cands[-1])
    _spec = f'{c["rng"]} km WLTP range' if c["t"] == "ev" else f'real-world {str(c["c"])} l/100 km'
    page(curl_en(c), _t, f'{c["n"]} from {e_en(c["p"])} in Spain, {_spec}. All in, it costs {e_en(k["month"])} a month ({pk_en(k["perKm"])} per km): depreciation, {"electricity" if c["t"] == "ev" else "fuel"}, insurance, servicing and tax.', body, "coches", schema, lang="en", full_title=_t if len(_t) > 48 else None)

def en_rankings():
    cards = "".join(f'<a class="card" href="/en/rankings/{v[0]}/"><span class="kicker">Ranking</span><h3>{v[1]}</h3><p>{v[2]}</p></a>' for v in RANK_EN.values())
    page("/en/rankings/", "Car rankings by real cost", "The cheapest cars to own in Spain: electric, SUVs, hybrids, range, ZERO label and family cars.",
         f'{crumbs_en((None, "Rankings"))}<section class="tight"><div class="wrap"><h1>Rankings</h1><p class="muted" style="margin:10px 0 24px;max-width:62ch">Every car ranked by what really matters: what it costs you per kilometre.</p><div class="cards">{cards}</div></div></section>', "mejores", lang="en")
    for s, t, d, fn, right in RANKINGS:
        es_slug = s; en_slug, te, de = RANK_EN[s]; lst = fn()
        rgt = None
        if s == "electricos-mas-autonomia": rgt = lambda c: f'<span class="num">{c["rng"]} km</span>'
        if s.startswith("coches-menos-de-"): rgt = lambda c: f'<span class="num">{pk_en(K[c["id"]]["perKm"])}/km · {e_en(c["p"])}</span>'
        if s == "coches-que-menos-gastan": rgt = lambda c: f'<span class="num">€{e100(c):.2f}<small>/100 km</small></span>'
        if s == "coches-con-mas-maletero": rgt = lambda c: f'<span class="num">{c["trunk"]} l</span>'
        if s == "coches-seguro-mas-barato": rgt = lambda c: f'<span class="num">≈ {e_en(c["ins"])}/yr</span>'
        if s in ("coches-etiqueta-eco-mas-baratos", "coches-glp-mas-baratos"): rgt = lambda c: f'<span class="num">{pk_en(K[c["id"]]["perKm"])}/km · {e_en(c["p"])}</span>'
        if s == "deportivos-mas-baratos": rgt = lambda c: f'<span class="num">{pk_en(K[c["id"]]["perKm"])}/km · {c["cv"]} hp</span>'
        if s == "familiares-y-7-plazas": rgt = lambda c: f'<span class="num">{pk_en(K[c["id"]]["perKm"])}/km · {tle(c)}</span>'
        items = "".join(rank_li_en(c, rgt(c) if rgt else None) for c in lst)
        others = "".join(f'<a class="chip" href="/en/rankings/{v[0]}/">{v[1]}</a>' for k2, v in RANK_EN.items() if k2 != s)
        body = f"""{crumbs_en(("/en/rankings/", "Rankings"), (None, te))}
<section class="tight"><div class="wrap narrow"><h1>{te}</h1><p class="muted" style="margin:10px 0 22px">{de} Calculated at 15,000 km a year over 5 years.</p>
 <div class="panel"><ol class="rank">{items}</ol></div>{ad("ranking")}
 <div style="margin-top:18px">{sharebuttons(f"/en/rankings/{en_slug}/", te, True)}</div>
 <h2 style="margin:36px 0 14px;font-size:1.3rem">Other rankings</h2><div class="chips">{others}</div></div></section>"""
        _mon = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][int(FUELP["date"][5:7]) - 1]
        _te = te.removeprefix("The "); _ts = f'{_te[:1].upper() + _te[1:]} in Spain ({_mon} {FUELP["date"][:4]})'
        _w0 = lst[0]
        _de = (f'The {len(lst)} electric cars that go furthest. No. 1: {_w0["n"]}, {_w0["rng"]} km WLTP from {e_en(_w0["p"])}. Updated {int(FUELP["date"][8:10])} {_mon}.' if s == "electricos-mas-autonomia" else
               f'{len(lst)} cars ranked by real cost of ownership in Spain. No. 1: {_w0["n"]}, {e_en(K[_w0["id"]]["month"])} a month all in, from {e_en(_w0["p"])}. Updated {int(FUELP["date"][8:10])} {_mon}.')
        page(f"/en/rankings/{en_slug}/", te, _de, body, "mejores",
             {"@context": "https://schema.org", "@type": "ItemList", "name": te, "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": DOMAIN + curl_en(c), "name": c["n"]} for i, c in enumerate(lst)]}, lang="en", full_title=_ts if len(_ts) <= 66 else None)

def en_finder():
    def q(key, title, opts, default):
        b = "".join(f'<button type="button" class="opt" data-q="{key}" data-v="{v}" aria-pressed="{str(v == default).lower()}">{l}<small>{s}</small></button>' for v, l, s in opts)
        return f'<div class="q"><h3>{title}</h3><div class="opts">{b}</div></div>'
    body = f"""{crumbs_en((None, "Which car?"))}
<section class="tight"><div class="wrap quiz" id="finder">
 <h1>Which car should I buy?</h1>
 <p class="muted" style="margin:10px 0 28px">Four answers and we'll show you the three cars that will cost you least. Change any answer and the result updates instantly.</p>
 {q("budget", "1. What's your maximum budget?", [(20000, "Up to €20,000", "City cars and basics"), (30000, "Up to €30,000", "Most of the market"), (40000, "Up to €40,000", "More space and kit"), (999999, "No limit", "The whole market")], 30000)}
 {q("km", "2. How many kilometres do you drive a year?", [(8000, "Few", "About 8,000 km"), (15000, "Average", "About 15,000 km"), (25000, "Quite a lot", "About 25,000 km"), (35000, "Loads", "Over 30,000 km")], 15000)}
 {q("home", "3. Can you charge at home or at work?", [("si", "Yes", "Garage or space with a socket"), ("no", "No", "I'd rely on public chargers")], "si")}
 {q("body", "4. What kind of car are you after?", [("any", "Don't mind", "The cheapest"), ("urbano", "Small", "For the city"), ("compacto,berlina", "Hatchback or saloon", "All-rounder"), ("suv-p,suv-m,suv-g", "SUV", "Higher up"), ("familiar,suv-g,monovolumen", "Estate or 7 seats", "Big boot"), ("deportivo", "Sports car", "For fun")], "any")}
 <div id="fres" class="needs-js" aria-live="polite" style="margin-top:10px">{SKEL}</div>
</div></section>"""
    page("/en/which-car/", "Which car should I buy? A 4-question test", "Answer 4 questions and find the 3 cars that will cost you least based on your budget, mileage and charging.", body, "finder", lang="en")

CALCS_EN = {
 "coste-viaje-gasolina": ("Trip fuel cost calculator", "How much a car trip costs in petrol, diesel or electricity, and how much each person pays.",
   [("v-car", "Your car (optional)"), ("v-km", "Distance (km)"), ("v-c", "Consumption per 100 km"), ("v-u", "Unit"), ("v-p", "Price per litre or kWh (€)"), ("v-n", "People in the car"), ("v-t", "Tolls and parking (€)"), ("v-ret", "Return trip")],
   "<h2>How it works</h2><p>We multiply the kilometres by the consumption per 100 km and the fuel price, add tolls and parking, and split it between everyone travelling. If you pick your car, we fill in its estimated real consumption.</p>"),
 "coste-carga-electrico": ("Electric car charging cost calculator", "How much it costs to charge your electric car at home, on a night tariff or at a rapid charger.",
   [("c-car", "Your car (optional)"), ("c-bat", "Usable battery (kWh)"), ("c-from", "Charge from (%)"), ("c-to", "To (%)"), ("c-where", "Where you charge"), ("c-p", "Exact price (€/kWh)"), ("c-cons", "Consumption (kWh/100 km)")],
   "<h2>How it works</h2><p>We work out the energy going into the battery, add around 10% charging losses and multiply by the price per kWh. With your car's consumption we estimate the range you gain.</p>"),
 "cuota-financiacion-coche": ("Car loan calculator: monthly payment, interest and APR", "Free car finance calculator: work out your monthly payment, total interest, APR and a year-by-year breakdown in euros, pounds or dollars.",
   [("f-p", "Car price"), ("f-e", "Deposit"), ("f-tin", "Interest rate (%)"), ("f-m", "Term"), ("f-com", "Arrangement fee (%)")],
   """<h2>How to use this car loan calculator</h2><p>Enter the price of the car, the deposit you'll put down, the interest rate the lender offers, the length of the loan and any arrangement fee. You'll instantly see your monthly payment, the total you'll pay, how much of it is interest and the approximate APR, plus how the balance goes down each year.</p>
<h2>A worked example</h2><p>Borrowing 20,000 at a 7.9% interest rate over 60 months gives a monthly payment of about 404.57. Over the five years you pay 24,274.28 in total, so the loan costs you 4,274.28 in interest. Stretch the same loan to 84 months and the payment drops, but the interest goes up a lot.</p>
<h2>The formula</h2><p>The monthly payment of a standard (amortising) car loan is <strong>P × r ÷ (1 − (1 + r)<sup>−n</sup>)</strong>, where P is the amount borrowed, r is the monthly interest rate (the annual rate divided by 12) and n is the number of monthly payments. Early payments are mostly interest; later ones are mostly capital.</p>
<h2>Look at the APR, not just the payment</h2><p>The APR includes interest and fees, so it's the figure to compare loans with. A low payment over many months can end up much more expensive overall. Dealer finance often looks cheap because of the advertised payment, so always compare the total amount payable.</p>
<h2>How to pay less interest</h2><ul><li>Put down a bigger deposit.</li><li>Choose the shortest term you can comfortably afford.</li><li>Compare the APR from your bank with the dealer's offer.</li><li>Check whether there's a fee for paying the loan off early.</li></ul>
<p>Want to know what the car itself will cost you, beyond the loan? See the <a href="/en/compare/">real cost comparison</a>.</p>"""),
 "etiqueta-dgt": ("Which DGT label does my car have?", "Find your car's environmental label from its fuel type and registration year.",
   [("e-t", "Type of car"), ("e-y", "Year of registration")],
   "<h2>How the label is decided</h2><p>The DGT assigns the label based on the car's emissions standard (Euro), which in practice depends on the fuel and the registration date. This is approximate: check your plate on the DGT website.</p>"),
 "amortizacion-electrico": ("Is an electric car worth it?", "How many kilometres a year you need for an electric car to be cheaper than a petrol or hybrid.",
   [("a-ev", "Electric car"), ("a-ice", "Compared with"), ("a-y", "Years you'll keep it"), ("a-h", "Share of home charging (%)")],
   "<h2>How it works</h2><p>We compare the total cost of both cars for each annual mileage and find the point where the electric one becomes cheaper. It doesn't include incentives such as Plan Auto+, which would bring that point forward.</p>"),
}
FAQ_EN_CALC = {"cuota-financiacion-coche": [
  ("How is a car loan monthly payment calculated?", "With the standard amortisation formula: amount borrowed × monthly rate ÷ (1 − (1 + monthly rate) to the power of minus the number of payments). The calculator does it for you and adds any arrangement fee."),
  ("What's the difference between the interest rate and the APR?", "The interest rate is the price of the money alone. The APR adds fees such as the arrangement fee and shows the real yearly cost of the loan, so it's the number to compare offers with."),
  ("Is a longer car loan better?", "A longer term lowers the monthly payment but increases the total interest you pay. If you can afford it, a shorter term is almost always cheaper overall."),
  ("Can I use it in pounds or dollars?", "Yes. Choose the currency at the top: the maths is the same for any currency.")]}
OPT_EN = {"v-u": [("Litres", "Litros"), ("kWh", "kWh")], "e-t": [("Petrol", "Gasolina"), ("Diesel", "Diésel"), ("Non plug-in hybrid", "Híbrido no enchufable"), ("LPG or natural gas", "GLP o gas natural"),
          ("Plug-in hybrid under 40 km electric", "Híbrido enchufable de menos de 40 km eléctricos"), ("Plug-in hybrid 40 km electric or more", "Híbrido enchufable de 40 km eléctricos o más"), ("Electric", "Eléctrico")]}

def en_calcs():
    import re as _re
    cards = "".join(f'<a class="card calc-card" href="/en/calculators/{CALC_EN[s]}/"><span class="badge">{ {"TIN": "APR"}.get(b, b)}</span><h3>{CALCS_EN[s][0]}</h3><p>{CALCS_EN[s][1]}</p></a>' for s, t, b, d, *_ in CALCS)
    page("/en/calculators/", "Calculators for drivers", "Free calculators: trip fuel cost, EV charging cost, car finance, DGT label and whether an electric car is worth it.",
         f'{crumbs_en((None, "Calculators"))}<section class="tight"><div class="wrap"><h1>Calculators</h1><p class="muted" style="margin:10px 0 24px;max-width:62ch">Quick answers to the sums every driver does at some point.</p><div class="cards">{cards}</div></div></section>', "calc", lang="en")
    for s, t, b, d, form, text, faq in CALCS:
        te, de, labels, txt = CALCS_EN[s]
        b = {"TIN": "APR"}.get(b, b)
        f = form
        for fid, lab in labels:
            f = _re.sub(rf'(<label class="lbl" for="{fid}">)[^<]*(</label>)', rf'\g<1>{lab}\g<2>', f)
        f = f.replace("Sí, contar la vuelta", "Yes, count the way back").replace('placeholder="Escribe un modelo"', 'placeholder="Type a model"').replace('placeholder="Escribe un eléctrico"', 'placeholder="Type an electric car"')
        for en_l, es_l in OPT_EN.get("v-u", []) + OPT_EN.get("e-t", []): f = f.replace(f">{es_l}<", f">{en_l}<")
        f = (f.replace("En casa, tarifa normal (0,15 €/kWh)", "Home, standard tariff (€0.15/kWh)").replace("En casa, tarifa nocturna (0,10 €/kWh)", "Home, night tariff (€0.10/kWh)")
              .replace("Cargador público lento (0,35 €/kWh)", "Public slow charger (€0.35/kWh)").replace("Cargador rápido (0,49 €/kWh)", "Rapid charger (€0.49/kWh)").replace("Ultrarrápido (0,59 €/kWh)", "Ultra-rapid (€0.59/kWh)"))
        f = _re.sub(r">(\d+) meses<", r">\1 months<", f)
        if s == "cuota-financiacion-coche":
            f = f.replace('<div class="cgrid">', '<div class="cgrid"><div><label class="lbl" for="f-cur">Currency</label><select id="f-cur"><option value="€">Euro (€)</option><option value="£">Pound (£)</option><option value="$">Dollar ($)</option></select></div>', 1)
        others = "".join(f'<a class="chip" href="/en/calculators/{CALC_EN[s2]}/">{CALCS_EN[s2][0]}</a>' for s2, *_ in CALCS if s2 != s)
        body = f"""{crumbs_en(("/en/calculators/", "Calculators"), (None, te))}
<section class="tight"><div class="wrap narrow">
 <span class="badge">{b}</span><h1 style="margin-top:12px">{te}</h1><p class="muted" style="margin:10px 0 24px">{de}</p>
 <div class="tool needs-js">{f}</div>
 <div class="body" style="margin-top:30px">{txt}</div>
 <div style="margin-top:18px">{sharebuttons(f"/en/calculators/{CALC_EN[s]}/", te, True)}</div>
 <h2 style="margin:30px 0 12px;font-size:1.3rem">Other calculators</h2><div class="chips">{others}</div>
</div></section>"""
        _app = {"@type": "WebApplication", "name": te, "applicationCategory": "FinanceApplication" if s == "cuota-financiacion-coche" else "UtilitiesApplication", "operatingSystem": "Web", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}
        _faq = FAQ_EN_CALC.get(s)
        if _faq:
            body = body.replace('<h2 style="margin:30px 0 12px;font-size:1.3rem">Other calculators</h2>', '<h2 style="margin:30px 0 12px;font-size:1.3rem">Frequently asked questions</h2>' + '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in _faq) + '</div><h2 style="margin:30px 0 12px;font-size:1.3rem">Other calculators</h2>', 1)
        sch = {"@context": "https://schema.org", "@graph": [_app] + ([{"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in _faq]}] if _faq else [])}
        page(f"/en/calculators/{CALC_EN[s]}/", te, de, body, "calc", sch, lang="en")

def en_static_pages():
    def simple(path, title, desc, inner, noindex=False, endcta=True):
        page(path, title, desc, f'{crumbs_en((None, title))}<section class="tight"><div class="wrap narrow article"><h1>{title}</h1><div class="body" style="margin-top:20px">{inner}</div></div></section>', "", noindex=noindex, lang="en", endcta=endcta)
    simple("/en/about/", "About us", f"What {SITE} is, who is behind it and how we independently calculate the real cost of owning every car in Spain.", f"""<p>{SITE} started from a simple idea: a car's price isn't what you pay on the day you buy it, but what it costs you every kilometre for as long as you own it.</p>
<h2>How we work</h2><p>Our figures come from a public method that we explain in full. Every news story cites its sources. We fix mistakes as soon as we spot them.</p>
<h2>Advertising</h2><p>We're funded by advertising. Advertisers don't decide what we publish or how we tell it.</p><p>Spotted a mistake? <a href="/en/contact/">Get in touch</a>.</p>""")
    simple("/en/methodology/", "How we calculate the real cost", f"{SITE}'s method for calculating what a car costs to own.", """<p>Every figure on Kilómetro Real comes from the same public method, so you can compare any car with any other on equal terms.</p>
<h2>What we add up</h2><ul><li><strong>Depreciation:</strong> list price minus the car's estimated value when you sell it, based on each brand's average depreciation. Electric and plug-in cars get slightly higher depreciation.</li>
<li><strong>Energy:</strong> estimated real-world consumption times your mileage. For electric cars we mix home and public charging; for plug-in hybrids, the share of kilometres you can drive on electricity if you charge daily.</li>
<li><strong>Insurance:</strong> an estimate for extended third-party cover for a 35-year-old driver, based on the car's value.</li>
<li><strong>Servicing:</strong> typical maintenance, tyres and wear for each powertrain.</li><li><strong>Road tax:</strong> average municipal tax by power, with the usual discount for electric cars.</li></ul>
<h2>Defaults</h2><p>15,000 km a year over 5 years, petrol €{FUELP["g95"]:.3f}/L, diesel €{FUELP["die"]:.3f}/L, LPG €{FUELP["glp"]:.3f}/L (averages on {FUELP["date"]}), home electricity €0.15/kWh and public charging €0.49/kWh, with 80% home charging. You can change all of it in the <a href="/en/compare/">comparison tool</a>.</p>
<h2>Limits</h2><p>Prices are entry list prices without discounts or incentives, updated in October 2026. They're indicative and meant for comparing. Before buying, check the offer with the dealer.</p>""")
    page("/en/contact/", "Contact", f"Write to {SITE}: data errors, news tips, feedback or advertising.",
         f'{crumbs_en((None, "Contact"))}<section class="tight"><div class="wrap narrow"><h1>Contact</h1><p class="muted" style="margin:10px 0 24px">Spotted wrong data, have a news tip or want to tell us what you think? Write to us. We reply within 2 working days.</p>{contact_form(True)}<p class="note" style="margin-top:16px">You can also email us at <span class="num">{CONTACT_EMAIL}</span>.</p></div></section>', "", lang="en", endcta=False)
    simple("/en/privacy/", "Privacy", "Privacy policy.", f"""<p>Data controller: see our <a href="/aviso-legal/" hreflang="es">legal notice</a> (in Spanish).</p>
<h2>What data we process</h2><p>If you write to us, we use your email address and message only to reply. We don't sell or share your data.</p>
<h2>Advertising</h2><p>This site shows Google AdSense ads. Google and its partners may use cookies to show ads based on your visits, provided you accept them in the consent notice. You can manage this in <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google's ad settings</a>.</p>
<h2>Fonts</h2><p>Fonts are loaded from Google Fonts, so your browser connects to Google's servers.</p>
<h2>Your rights</h2><p>You can exercise your rights of access, rectification, erasure, objection, restriction and portability by writing to us, and complain to the Spanish Data Protection Agency (aepd.es).</p>""", noindex=True)
    simple("/en/cookies/", "Cookies", "Which cookies Kilómetro Real uses, what they are for and how to change your choice at any time.", """<p>A cookie is a small file a website stores in your browser. Here is what we use and how to change your mind.</p>
<h2>Cookies and data we use</h2><ul>
<li><strong>Advertising (Google AdSense):</strong> Google and its partners may use cookies to show and measure ads. Personalised ads are only used if you accept them in the consent notice.</li>
<li><strong>Measurement (Google Analytics, if enabled):</strong> anonymous visit statistics, only with your permission.</li>
<li><strong>Consent:</strong> stores the choice you made so we don't ask again.</li>
<li><strong>Site preferences (local storage, not cookies):</strong> light or dark mode and your recent comparisons. They never leave your browser.</li></ul>
<h2 id="manage">How to change your choice</h2><p>The first time you visit we ask whether you accept personalised-advertising cookies. If you reject them you will still see ads, just not based on your activity. Press the button to reopen the notice and change your choice. You can also delete cookies in your browser settings.</p>
<p><button type="button" class="btn ghost cookie-prefs">Manage cookies</button></p>
<p>How Google uses data: <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">policies.google.com/technologies/partner-sites</a>.</p>""", noindex=True)
    simple("/en/terms/", "Terms of use", "Terms of use for Kilómetro Real: what we offer, how figures are calculated and your responsibilities when using the site.", """<p>By using Kilómetro Real you accept these terms. They are simple: we want the information to be useful and for you to know its limits.</p>
<h2>What Kilómetro Real is</h2><p>A free, informational website that estimates what owning a car in Spain costs: depreciation, energy, insurance, servicing and road tax. We don't sell cars, we're not a dealer or broker, and brands don't pay to appear.</p>
<h2>Figures are indicative</h2><p>Prices are list prices without discounts or incentives; consumption and depreciation are average estimates. Your case may differ. Before buying, confirm price, incentives and terms with the dealer or manufacturer. See <a href="/en/methodology/">how we calculate</a>.</p>
<h2>Not advice</h2><p>Nothing published here is financial, tax or legal advice. The finance and incentive calculators are simulations.</p>
<h2>Permitted use</h2><p>You may read, share and link to any page. Mass copying of content or data, or automated access that overloads the site, is not allowed.</p>
<h2>Advertising and links</h2><p>The site is funded by Google AdSense ads, chosen by Google; they are not our recommendation. We are not responsible for external websites we link to.</p>
<h2>Errors and changes</h2><p>If you spot wrong data, <a href="/en/contact/">let us know</a> and we'll fix it. We may update these terms; the version published here always applies.</p>""")

def build_en_all():
    en_home(); en_compare(); en_catalog()
    for c in CARS: en_car(c)
    en_rankings(); en_finder(); en_calcs(); en_static_pages()
