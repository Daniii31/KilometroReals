# -*- coding: utf-8 -*-
"""Contenido generado con los datos: análisis, textos de ficha y preguntas frecuentes."""
from statistics import median
from models import cars, cost, BODY, TYPE, DEFAULTS

CARS = cars()
BY = {c["id"]: c for c in CARS}
K = {c["id"]: cost(c) for c in CARS}
def num(v): return f"{round(v):,}".replace(",", ".")
def eur(v): return num(v) + " €"
def pk(v): return f"{v:.3f}".replace(".", ",")
def pct(v): return f"{round(v * 100)} %"
def link(c): return f'<a href="/coches/{c["id"]}/">{c["n"]}</a>'
def by_pk(lst): return sorted(lst, key=lambda c: K[c["id"]]["perKm"])

def breakeven(a, b, y=5):
    """Km/año a partir de los que A (eléctrico) sale más barato que B. None si nunca (hasta 60.000)."""
    def tot(c, km): return cost(c, {**DEFAULTS, "km": km, "y": y})["total"]
    for km in range(1000, 60001, 500):
        if tot(a, km) <= tot(b, km): return km
    return None

PLURAL = {"urbano": "urbanos", "compacto": "compactos", "berlina": "berlinas", "familiar": "familiares", "suv-p": "SUV pequeños", "suv-m": "SUV medianos", "suv-g": "SUV grandes", "monovolumen": "monovolúmenes", "deportivo": "deportivos"}
def charge_home(c): return c["bat"] * DEFAULTS["ph"] * 1.1
def charge_pub(c): return c["bat"] * DEFAULTS["pp"]

# ================= ANÁLISIS (artículos propios) =================
def analyses():
    out = []
    types = ["ev", "phev", "hev", "mhev", "ice"]
    rows = ""
    for t in types:
        lst = [c for c in CARS if c["t"] == t]
        rows += (f'<tr><td>{TYPE[t]}</td><td class="num">{len(lst)}</td><td class="num">{eur(median(K[c["id"]]["month"] for c in lst))}</td>'
                 f'<td class="num">{pk(median(K[c["id"]]["perKm"] for c in lst))}</td><td class="num">{pct(median(K[c["id"]]["dep"] / K[c["id"]]["total"] for c in lst))}</td></tr>')
    cheap = by_pk(CARS)[:5]; dear = by_pk(CARS)[-5:][::-1]
    med_month = median(K[c["id"]]["month"] for c in CARS)
    out.append(dict(slug="cuanto-cuesta-tener-un-coche-en-espana", k="analisis", fig="", date="2026-10-09", dtxt="9 oct 2026", min=5, img="analisis-coste-real",
     t=f"Cuánto cuesta de verdad tener un coche en España: lo hemos calculado para {len(CARS)} modelos",
     st=f"El coche nuevo mediano cuesta {eur(med_month)} al mes cuando sumas todo. La compra es solo una parte.",
     body=f"""<p>Cuando alguien pregunta cuánto cuesta un coche, casi siempre responde con el precio de tarifa. Pero ese número no dice lo que sale de tu cuenta cada mes. Por eso hemos calculado el coste real de los {len(CARS)} modelos de nuestro comparador: lo que pierde de valor, la energía, el seguro, el mantenimiento y el impuesto de circulación, con 15.000 km al año durante 5 años.</p>
<div class="fact">El coche nuevo mediano en España cuesta unos <b>{eur(med_month)} al mes</b> de verdad, y el más barato de tener se queda en <b>{eur(K[cheap[0]["id"]]["month"])}</b>.</div>
<h2>Por tecnología</h2>
<table><thead><tr><th>Tecnología</th><th class="num">Modelos</th><th class="num">Coste al mes (mediana)</th><th class="num">€/km</th><th class="num">Peso de la pérdida de valor</th></tr></thead><tbody>{rows}</tbody></table>
<p>La pérdida de valor es, de lejos, el gasto más grande en casi todos los coches nuevos. Pesa más que la gasolina o la luz, y por eso un coche caro que gasta poco rara vez es el más barato de tener.</p>
<h2>Los cinco más baratos de tener</h2><ol>{"".join(f"<li>{link(c)}: {eur(K[c['id']]['month'])} al mes ({pk(K[c['id']]['perKm'])} €/km)</li>" for c in cheap)}</ol>
<h2>Los cinco más caros de tener</h2><ol>{"".join(f"<li>{link(c)}: {eur(K[c['id']]['month'])} al mes ({pk(K[c['id']]['perKm'])} €/km)</li>" for c in dear)}</ol>
<h2>Cómo lo calculamos</h2><p>Usamos el precio de tarifa de acceso sin descuentos ni ayudas, el consumo real medio estimado, un seguro a terceros ampliado para un conductor de 35 años, el mantenimiento típico de cada tecnología y la depreciación media de cada marca. Son cifras orientativas, pensadas para comparar coches entre sí. Puedes cambiar los kilómetros y los precios de la energía en el <a href="/comparador/">comparador</a>.</p>""",
     src=[("Cálculos propios de Kilómetro Real", "/comparador/")]))

    pairs = [("dacia-spring", "hyundai-i10"), ("byd-dolphin-surf", "seat-ibiza-1-0-tsi"), ("renault-5-e-tech", "renault-clio-tce"), ("leapmotor-b10", "seat-arona-1-0-tsi"),
             ("kia-ev3", "kia-stonic-48v"), ("skoda-elroq", "skoda-kamiq-1-0-tsi"), ("volkswagen-id-3", "volkswagen-golf-1-5-etsi"), ("tesla-model-3-rwd", "seat-leon-1-5-tsi"),
             ("tesla-model-y-rwd", "volkswagen-tiguan-1-5-etsi"), ("mg-4-electric", "mg-zs-1-5")]
    trs = ""
    for a, b in pairs:
        be = breakeven(BY[a], BY[b])
        txt = "desde el primer kilómetro" if be == 1000 else (f"a partir de {num(be)} km/año" if be else "no compensa ni con 60.000 km/año")
        trs += f'<tr><td>{link(BY[a])}</td><td>{link(BY[b])}</td><td>{txt}</td></tr>'
    out.append(dict(slug="electrico-o-gasolina-a-partir-de-cuantos-km-compensa", k="analisis", fig="", date="2026-10-09", dtxt="9 oct 2026", min=4, img="analisis-amortizacion",
     t="Eléctrico o gasolina: a partir de cuántos kilómetros al año compensa",
     st="Hemos enfrentado 10 eléctricos con su rival de gasolina más parecido. En algunos casos el eléctrico gana desde el primer kilómetro.",
     body=f"""<p>Un eléctrico suele costar más al comprarlo y menos cada kilómetro. La pregunta es cuántos kilómetros necesitas para que lo segundo compense lo primero. Lo hemos calculado para diez parejas de coches parecidos, cargando el eléctrico en casa el 80 % de las veces y teniendo los dos coches 5 años.</p>
<table><thead><tr><th>Eléctrico</th><th>Rival</th><th>El eléctrico sale más barato</th></tr></thead><tbody>{trs}</tbody></table>
<h2>Qué decide el resultado</h2>
<ul><li><strong>La diferencia de precio.</strong> Cuanto más cara es la versión eléctrica, más kilómetros necesitas para recuperarla.</li>
<li><strong>Dónde cargas.</strong> Con luz de casa a 0,15 €/kWh el eléctrico gasta muy poco. Si dependes de cargadores públicos, la cuenta empeora mucho.</li>
<li><strong>La pérdida de valor.</strong> Los eléctricos se deprecian algo más rápido, y eso juega en su contra.</li>
<li><strong>Las ayudas.</strong> No están incluidas. Con el <a href="/ayudas/">Plan Auto+</a> el eléctrico puede ganar antes.</li></ul>
<p>Haz la cuenta con tus números en la <a href="/calculadoras/amortizacion-electrico/">calculadora de amortización</a>.</p>""",
     src=[("Cálculos propios de Kilómetro Real", "/calculadoras/amortizacion-electrico/")]))

    under = by_pk([c for c in CARS if c["p"] <= 20000])
    trs = "".join(f'<tr><td>{link(c)}</td><td>{TYPE[c["t"]]}</td><td class="num">{eur(c["p"])}</td><td class="num">{eur(K[c["id"]]["month"])}</td></tr>' for c in under)
    out.append(dict(slug="que-coche-comprar-con-20000-euros", k="analisis", fig="", date="2026-10-09", dtxt="9 oct 2026", min=3, img="analisis-20000",
     t="Qué coche nuevo comprar con 20.000 euros: los que menos cuestan de verdad",
     st=f"Hay {len(under)} coches nuevos por debajo de 20.000 € de tarifa. Estos son, ordenados por lo que cuestan al mes de verdad.",
     body=f"""<p>Con 20.000 euros todavía se puede comprar un coche nuevo en España, y no solo urbanos de gasolina: también algún eléctrico y coches de GLP con etiqueta ECO. Los hemos ordenado por coste real, no por precio.</p>
<table><thead><tr><th>Modelo</th><th>Tecnología</th><th class="num">Precio</th><th class="num">Coste al mes</th></tr></thead><tbody>{trs}</tbody></table>
<h2>Lo que nos llama la atención</h2>
<p>El {link(under[0])} es el que menos cuesta de tener. Los coches de GLP, como el Sandero ECO-G, combinan precio bajo, combustible barato y etiqueta ECO, una mezcla muy difícil de batir si haces muchos kilómetros y no puedes cargar en casa.</p>
<p>Si puedes estirar el presupuesto, mira nuestro ranking de <a href="/mejores/etiqueta-cero-menos-30000/">coches con etiqueta CERO por menos de 30.000 €</a>, o haz el <a href="/cual-me-conviene/">test</a> para ver cuál te conviene a ti.</p>""",
     src=[("Cálculos propios de Kilómetro Real", "/coches/")]))

    dep_rows = ""
    for t in types:
        lst = [c for c in CARS if c["t"] == t]
        dep_rows += f'<tr><td>{TYPE[t]}</td><td class="num">{pct(median(1 - c["res"] for c in lst))}</td><td class="num">{eur(median(K[c["id"]]["dep"] for c in lst))}</td></tr>'
    keep = sorted(CARS, key=lambda c: -c["res"])[:6]
    out.append(dict(slug="perdida-de-valor-el-gasto-que-nadie-mira", k="analisis", fig="", date="2026-10-09", dtxt="9 oct 2026", min=3, img="analisis-depreciacion",
     t="La pérdida de valor: el gasto más grande de tu coche y el que nadie mira",
     st="En la mayoría de coches nuevos, lo que pierde de valor en 5 años supera a todo lo que gastas en gasolina o luz.",
     body=f"""<p>Nadie paga la depreciación con una factura, por eso pasa desapercibida. Pero cuando vendes el coche, la diferencia entre lo que pagaste y lo que te dan es dinero que has gastado, igual que la gasolina.</p>
<table><thead><tr><th>Tecnología</th><th class="num">Valor perdido en 5 años (mediana)</th><th class="num">En euros (mediana)</th></tr></thead><tbody>{dep_rows}</tbody></table>
<h2>Los que mejor aguantan su valor</h2><ul>{"".join(f"<li>{link(c)}: conserva en torno al {pct(c['res'])} de su precio a los 5 años</li>" for c in keep)}</ul>
<h2>Cómo pagar menos depreciación</h2>
<ul><li>Elige marcas y versiones con buena reventa. Los híbridos de Toyota y los modelos de Dacia son ejemplos claros.</li>
<li>Tenlo más años: la pérdida de valor es más fuerte al principio.</li>
<li>Valora un seminuevo o un kilómetro cero: el primer dueño ya ha pagado la caída más grande.</li></ul>
<p>Son estimaciones medias por marca y tecnología. El valor real dependerá del estado del coche y del mercado de ocasión.</p>""",
     src=[("Cálculos propios de Kilómetro Real", "/coches/")]))

    evs = sorted([c for c in CARS if c["t"] == "ev"], key=lambda c: c["p"])[:15]
    trs = "".join(f'<tr><td>{link(c)}</td><td class="num">{c["bat"]} kWh</td><td class="num">{eur(charge_home(c))}</td><td class="num">{eur(charge_pub(c))}</td><td class="num">{f"{c["c"] * DEFAULTS["ph"] * 1.1:.2f}".replace(".", ",")} €</td></tr>' for c in evs)
    out.append(dict(slug="cuanto-cuesta-cargar-un-coche-electrico-modelo-a-modelo", k="analisis", fig="", date="2026-10-09", dtxt="9 oct 2026", min=3, img="analisis-carga",
     t="Cuánto cuesta cargar un coche eléctrico, modelo a modelo",
     st="Llenar la batería en casa cuesta entre 4 y 13 euros en los eléctricos más vendidos. En un cargador rápido, el triple.",
     body=f"""<p>Cargar un eléctrico es barato en casa y bastante más caro en la calle. Para que lo veas con números, hemos calculado lo que cuesta llenar la batería de los 15 eléctricos más asequibles del mercado, de vacío a lleno, con dos precios de referencia: 0,15 €/kWh en casa (sumando un 10 % de pérdidas) y 0,49 €/kWh en un cargador público.</p>
<table><thead><tr><th>Modelo</th><th class="num">Batería</th><th class="num">Llenar en casa</th><th class="num">Llenar en la calle</th><th class="num">100 km en casa</th></tr></thead><tbody>{trs}</tbody></table>
<p>En la práctica casi nunca se carga de 0 a 100 %, pero estos números sirven para comparar. Calcula tu caso exacto en la <a href="/calculadoras/coste-carga-electrico/">calculadora de carga</a> y lee nuestra guía sobre <a href="/guias/cuanto-cuesta-cargar-coche-electrico-casa/">cargar en casa</a>.</p>""",
     src=[("Cálculos propios de Kilómetro Real", "/calculadoras/coste-carga-electrico/")]))
    return out

# ================= FICHA: análisis y preguntas =================
def car_analysis(c):
    k = K[c["id"]]
    same = by_pk([x for x in CARS if x["body"] == c["body"]])
    pos = same.index(c) + 1
    avg = median(K[x["id"]]["perKm"] for x in same)
    diff = (k["perKm"] - avg) / avg
    parts = {"pérdida de valor": k["dep"], "energía": k["energy"], "seguro": k["ins"], "mantenimiento": k["mnt"]}
    big = max(parts, key=parts.get)
    pool = [x for x in same[:pos - 1] if 0.7 * c["p"] <= x["p"] <= 1.3 * c["p"] and (c["cv"] < 250 or x["cv"] >= 0.85 * c["cv"])]
    cheaper = pool[:1] or [x for x in same[:pos - 1] if c["cv"] < 250 or x["cv"] >= 0.85 * c["cv"]][:1]
    rank_txt = f"{pos}.º más barato de tener" if pos <= (len(same) + 1) // 2 else f"{len(same) - pos + 1}.º más caro de tener"
    p = [f'De {"las" if c["body"] == "berlina" else "los"} {len(same)} {PLURAL[c["body"]]} de nuestro comparador, el {c["n"]} es el <strong>{rank_txt}</strong>. '
         + (f'Su coste por kilómetro está un {round(abs(diff) * 100)} % {"por debajo" if diff < 0 else "por encima"} de la media de su categoría.' if abs(diff) >= 0.02 else "Su coste por kilómetro está en la media de su categoría.")]
    p.append(f'Su gasto más grande es la <strong>{big}</strong>: {eur(parts[big])} en 5 años, el {pct(parts[big] / k["total"])} de todo lo que cuesta.')
    if c["t"] == "ev":
        p.append(f'Llenar su batería de {c["bat"]} kWh en casa cuesta unos {eur(charge_home(c))}, y recorrer 100 km, unos {f"{c["c"] * DEFAULTS["ph"] * 1.1:.2f}".replace(".", ",")} €.')
    elif c["t"] == "phev":
        p.append(f'Si lo cargas a diario, puede hacer buena parte de los trayectos cortos en eléctrico: homologa {c["rng"]} km sin gasolina. Si no lo enchufas, gasta como un híbrido pesado.')
    else:
        fuelp = {"g": DEFAULTS["gas"], "d": DEFAULTS["die"], "glp": DEFAULTS["glp"]}[c["f"]]
        p.append(f'Con un consumo real de {str(c["c"]).replace(".", ",")} L/100 km, cada 100 km te cuestan unos {f"{c["c"] * fuelp:.2f}".replace(".", ",")} € de combustible.')
    if cheaper:
        x = cheaper[0]
        p.append(f'Si buscas algo parecido que cueste menos de tener, mira el {link(x)}: {pk(K[x["id"]]["perKm"])} €/km.')
    return "".join(f"<p>{s}</p>" for s in p)

def car_faq(c):
    k = K[c["id"]]
    lab = {"cero": "CERO", "eco": "ECO", "c": "C"}[c["lab"]]
    qa = [(f'¿Cuánto cuesta tener un {c["n"]} al mes?', f'Unos {eur(k["month"])} al mes con 15.000 km al año durante 5 años, sumando pérdida de valor, energía, seguro, mantenimiento e impuesto. Son {pk(k["perKm"])} € por kilómetro.')]
    if c["t"] == "ev":
        qa.append((f'¿Cuánto cuesta cargar el {c["n"]}?', f'Llenar su batería de {c["bat"]} kWh cuesta unos {eur(charge_home(c))} en casa a 0,15 €/kWh y unos {eur(charge_pub(c))} en un cargador público a 0,49 €/kWh.'))
        qa.append((f'¿Qué autonomía tiene el {c["n"]}?', f'Homologa {c["rng"]} km en ciclo WLTP. En autopista y con frío, cuenta con bastante menos.'))
    else:
        qa.append((f'¿Cuánto gasta el {c["n"]}?', f'Estimamos un consumo real de {str(c["c"]).replace(".", ",")} litros cada 100 km' + (" en modo híbrido, y bastante menos si lo cargas a diario." if c["t"] == "phev" else ".")))
    qa.append((f'¿Qué etiqueta DGT tiene el {c["n"]}?', f'Etiqueta {lab}.' + (" Puede circular por las zonas de bajas emisiones de la mayoría de ciudades." if lab in ("CERO", "ECO") else " Consulta la ordenanza de tu ciudad para las zonas de bajas emisiones.")))
    if c["lab"] == "cero":
        qa.append((f'¿Tiene ayudas el {c["n"]}?', ("Su precio está por debajo del límite del Plan Auto+, así que puede optar a la ayuda, que llega a 4.500 € más el descuento del concesionario." if c["p"] <= 54450 else "Su precio supera el límite de 45.000 € sin IVA del Plan Auto+.") + (" Al fabricarse fuera de Europa, la cuantía puede ser menor." if c["cn"] else "")))
    return qa
