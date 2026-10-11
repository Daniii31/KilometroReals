# Páginas extra: precio de los carburantes hoy y comparativas A vs B. Se ejecuta dentro de build.py.
from vs_pairs import VS_PAIRS

def ldj(*items): return {"@context": "https://schema.org", "@graph": list(items)}
def faq_ld(faq): return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faq]}
def faq_box(faq): return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq) + "</div>"
def fprice(v): return f"{v:.3f}".replace(".", ",") + " €"

# ---------------- PRECIO DE LA GASOLINA HOY ----------------
def build_fuel():
    F = FUELP
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
    page("/precio-gasolina-hoy/", f"Precio de la gasolina hoy: {fprice(F['g95'])} el litro", f'Precio medio de la gasolina 95 ({fprice(F["g95"])}), diésel ({fprice(F["die"])}) y GLP hoy en España, cuánto cuesta llenar el depósito y cada 100 km.',
         body, "", ldj(faq_ld(faq)))

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
        page(vs_slug(a_id, b_id), next((x for x in _vc if len(x) <= 60), _vc[-1]), f'{A["n"]} o {B["n"]}: coste real por km, al mes y en 5 años, con pérdida de valor, consumo, seguro y mantenimiento. Te decimos cuál conviene.',
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
