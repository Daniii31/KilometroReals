# -*- coding: utf-8 -*-
"""Contenido de Kilómetro Real. Para añadir una noticia: copia un bloque de ARTICLES y cambia los datos."""

KINDS = {"analisis": "Análisis", "dgt": "DGT y normas", "mercado": "Mercado", "china": "Eléctricos chinos", "lanz": "Lanzamientos", "ayuda": "Ayudas", "guia": "Guía"}

ARTICLES = [
dict(slug="diesel-se-hunde-hibridos-lideran-septiembre-2026", k="mercado", fig="", date="2026-10-09", dtxt="9 oct 2026", min=3, img="noticia-diesel-hunde",
 t="El diésel se hunde: ya solo es el 2,5 % de los coches nuevos que se venden en España",
 st="En septiembre, los híbridos siguen al frente con el 43,7 % del mercado y los electrificados ya son uno de cada tres turismos.",
 body="""<p>El reparto del mercado español ha cambiado de golpe. En septiembre se matricularon solo 2.363 turismos diésel, un 47,3 % menos que hace un año. Son apenas el 2,5 % de las ventas, cuando hace una década eran mayoría.</p>
<div class="fact">Híbridos no enchufables: <b>43,7 %</b> · Electrificados (eléctricos y enchufables): <b>34 %</b> · Gasolina: <b>16,2 %</b> · Diésel: <b>2,5 %</b></div>
<h2>Los híbridos mandan</h2><p>Los híbridos convencionales siguen siendo la opción favorita, con el 43,7 % de los turismos vendidos. La razón es sencilla: no hay que enchufarlos, gastan poco y llevan etiqueta ECO. Si estás pensando en uno, mira nuestro ranking de <a href="/mejores/hibridos-mas-economicos/">híbridos más económicos</a>.</p>
<h2>Los enchufables crecen más rápido que nadie</h2><p>Los electrificados sumaron 31.945 turismos, un 56 % más que hace un año. Dentro de ellos, los híbridos enchufables llegaron a 14.579 unidades, un 40,6 % más. Por regiones, Madrid (11.460), Cataluña (5.160) y Andalucía (3.705) encabezan las ventas de electrificados.</p>
<h2>Y la gasolina también cae</h2><p>Los turismos solo de gasolina bajaron un 24,4 %, hasta 15.184 unidades. Cada vez más compradores dan el salto a algún tipo de hibridación.</p>
<p>La patronal ANFAC ha pedido mantener las ayudas del Plan Auto+ hasta final de 2026 y aclarar qué pasará en 2027, porque, según sus datos, las ventas responden con fuerza cuando hay incentivos.</p>""",
 src=[("Infobae (datos de ANFAC)","https://www.infobae.com/espana/2026/10/06/los-electricos-ya-suponen-una-de-cada-tres-ventas-de-coches-en-espana-crecen-sus-matriculaciones-mas-de-un-50-en-un-ano/")]),

dict(slug="rebaja-impuesto-gasolina-diesel-octubre-noviembre-diciembre-2026", k="mercado", fig="", date="2026-10-09", dtxt="9 oct 2026", min=4, img="noticia-carburantes",
 t="Gasolina y diésel: cuánto bajan en octubre y cuánto pueden subir en noviembre",
 st="El Gobierno prorroga la rebaja del impuesto de los carburantes hasta fin de año, pero de forma decreciente: 20 céntimos en octubre, 13 en noviembre y 6 en diciembre.",
 body="""<p>Desde el 1 de octubre está en vigor el Real Decreto-ley 25/2026, aprobado el 29 de septiembre, que prorroga la rebaja del Impuesto sobre Hidrocarburos hasta final de año. Pero no se mantiene igual: va bajando mes a mes.</p>
<div class="fact">Rebaja por litro: <b>20 céntimos</b> en octubre · <b>13</b> en noviembre · <b>6</b> en diciembre. Como el IVA va encima, cada céntimo de rebaja supone unos <b>1,21 céntimos</b> en el surtidor.</div>
<h2>Qué ha pasado en octubre</h2><p>La gasolina 95 bajó nueve céntimos de golpe, hasta 1,788 euros por litro, porque su rebaja pasó de 5 a 20 céntimos. El gasóleo se quedó en 1,890 euros, porque ya tenía los 20 céntimos desde julio por la llamada cláusula de salvaguarda.</p>
<h2>Por qué está tan caro</h2><p>El petróleo Brent llegó a 109,8 dólares a mediados de septiembre por los ataques en el estrecho de Ormuz y el cierre preventivo de un oleoducto saudí. La gasolina tocó 1,94 euros el 28 de septiembre. Después, el crudo bajó hasta unos 101 dólares.</p>
<h2>Qué puede pasar el 1 de noviembre</h2><p>Si la rebaja baja a 13 céntimos, los dos carburantes subirían unos 8,5 céntimos por litro. Esa subida no se aplicaría si se activa la cláusula de salvaguarda, que mantiene los 20 céntimos si el IPC de los carburantes de septiembre supera en más de un 15 % al de 2025. El INE publicará ese dato a mediados de octubre.</p>
<h2>Qué significa para tu bolsillo</h2><p>Con un coche que gaste 6 litros cada 100 km, cada 10 céntimos de diferencia en el litro son unos 90 euros al año si haces 15.000 km. Calcula lo que te cuesta un viaje con nuestra <a href="/calculadoras/coste-viaje-gasolina/">calculadora de gasolina</a>, y mira cuánto ahorraría un eléctrico con tu uso en la <a href="/calculadoras/amortizacion-electrico/">calculadora de amortización</a>.</p>""",
 src=[("Carwow","https://www.carwow.es/editorial/consejos-conductores/coches-combustible/precio-gasolina-diesel-espana-impuestos")]),

dict(slug="cambios-dgt-octubre-2026-ambar-intermitente-carril-emergencia", k="dgt", fig="", date="2026-10-09", dtxt="9 oct 2026", min=3, img="noticia-dgt-octubre",
 t="Cambios de la DGT en octubre: adiós al ámbar intermitente en los pasos de peatones y llega el carril de emergencia",
 st="La reforma del Reglamento General de Circulación entró en vigor el 1 de octubre. Esto es lo que cambia para los conductores de coche.",
 body="""<p>El 1 de octubre entró en vigor la reforma del Reglamento General de Circulación. Muchos de los cambios afectan a patinetes, bicicletas y motos, pero hay dos novedades que todo conductor de coche debe conocer.</p>
<h2>1. El ámbar intermitente deja de ser la norma en los pasos de peatones</h2><p>El semáforo ámbar parpadeando deja de usarse como régimen general en los pasos de peatones. La DGT quiere acabar con la idea de que el parpadeo da vía libre al coche, cuando en realidad obliga a ceder el paso al peatón. El detalle de cada cruce dependerá de lo que publique el BOE.</p>
<h2>2. El carril de emergencia en los atascos</h2><p>En autopistas y autovías con tráfico denso, los coches del carril derecho deben apartarse hacia la derecha y los del izquierdo hacia la izquierda, dejando un pasillo libre en el centro para ambulancias, bomberos y policía.</p>
<div class="fact">Recuerda: desde el 1 de enero de 2026 la baliza luminosa <b>V-16</b> es obligatoria y los carriles <b>VAO</b> solo admiten coches con al menos dos ocupantes, motos y transporte público.</div>
<h2>¿Y las multas?</h2><p>La DGT todavía no ha publicado las cuantías de las nuevas sanciones; aparecerán en el BOE. Lo previsible es que se mantenga el descuento del 50 % por pronto pago, pero conviene confirmarlo cuando salga la norma.</p>
<h2>Para motos, bicis y patinetes</h2><p>La reforma endurece el equipamiento obligatorio de motoristas, ciclistas y usuarios de patinete, con elementos como guantes, casco o chaleco según el caso.</p>
<p>¿Dudas con la etiqueta de tu coche para las zonas de bajas emisiones? Compruébala con nuestra <a href="/calculadoras/etiqueta-dgt/">calculadora de etiqueta DGT</a>.</p>""",
 src=[("Motor16","https://www.motor16.com/las-ultimas-noticias/reforma-dgt-octubre-2026-novedades/")]),

dict(slug="plan-auto-plus-empresas-autonomos-hasta-7500-euros", k="ayuda", fig="", date="2026-10-09", dtxt="9 oct 2026", min=3, img="noticia-plan-auto-empresas",
 t="Plan Auto+ para autónomos y empresas: hasta 6.000 € por un coche y 7.500 € por una furgoneta eléctrica",
 st="La línea 2 del programa, publicada en el BOE, admite solicitudes hasta el 31 de diciembre y se reparte por orden de llegada.",
 body="""<p>Además de las ayudas para particulares, el Plan Auto+ tiene una línea específica para empresas y autónomos. Se publicó en el BOE el 24 de septiembre y admite solicitudes desde el 1 de octubre hasta las 13:00 del 31 de diciembre de 2026, por orden de presentación hasta agotar el dinero.</p>
<div class="fact">Presupuesto: <b>50 millones</b> (42 para empresas y 8 para autónomos) · Turismos: hasta <b>6.000 €</b> para autónomos y microempresas, <b>4.500 €</b> para el resto · Furgonetas: hasta <b>7.500 €</b> y <b>5.000 €</b></div>
<h2>Requisitos principales</h2><ul>
<li>Estar al corriente con Hacienda y la Seguridad Social.</li>
<li>Vehículos con etiqueta CERO. Quedan fuera autobuses, autocares y camiones.</li>
<li>Turismos de hasta siete plazas con un precio máximo de 45.000 € sin impuestos y tras descuentos.</li>
<li>Como máximo 10 vehículos por empresa y 3 por autónomo.</li>
<li>En renting o leasing, una duración mínima de tres años.</li>
<li>Vehículos nuevos matriculados desde el 1 de enero de 2026 (en algunos casos, desde el 1 de enero de 2025).</li></ul>
<h2>La cuantía no es fija</h2><p>Las cifras son topes. La ayuda final depende de lo electrificado que esté el vehículo, de su precio y de si el coche y su batería se fabrican en Europa, igual que en la línea para particulares.</p>
<p>¿Qué coches entran? Consulta los <a href="/mejores/etiqueta-cero-menos-30000/">coches con etiqueta CERO por menos de 30.000 €</a> y cómo funcionan las <a href="/ayudas/">ayudas para particulares</a>.</p>""",
 src=[("Diario de Avisos","https://diariodeavisos.elespanol.com/2026/09/ayudas-vehiculos-electricos/")]),

dict(slug="coches-nuevos-que-llegan-antes-de-fin-de-ano-2026", k="lanz", fig="", date="2026-10-08", dtxt="8 oct 2026", min=3, img="noticia-novedades-otono",
 t="Los coches nuevos que llegan a España antes de fin de año: del Dacia Striker al Audi Q9",
 st="Al menos 15 novedades importantes aterrizan antes de diciembre. Estas son las que ya tienen precio o fecha.",
 body="""<p>El otoño viene cargado de lanzamientos. Hay modelos para todos los bolsillos, desde un Dacia por menos de 25.000 euros hasta un SUV de lujo de más de 120.000.</p>
<table><thead><tr><th>Modelo</th><th>Llegada</th><th class="num">Desde</th></tr></thead><tbody>
<tr><td>Dacia Striker</td><td>Antes de fin de año</td><td class="num">menos de 25.000 €</td></tr>
<tr><td>Dongfeng Vigo (eléctrico)</td><td>Pedidos abiertos</td><td class="num">29.900 €</td></tr>
<tr><td>Dongfeng Mage (híbrido enchufable)</td><td>Pedidos abiertos</td><td class="num">31.990 €</td></tr>
<tr><td>Audi Q9</td><td>Noviembre</td><td class="num">126.090 €</td></tr>
<tr><td>BMW i7</td><td>Ya a la venta</td><td class="num">121.400 €</td></tr>
<tr><td>Audi A2 e-tron</td><td>Diciembre</td><td class="num">por confirmar</td></tr>
</tbody></table>
<h2>Otros que están al caer</h2><p>Sin precio cerrado todavía, también llegan el Volvo EX60, el Denza D9, la renovación del BMW iX3, el Mercedes GLA eléctrico, el Fiat 600 de gasolina, el Leapmotor B05, el DS Nº7, el Lancia Gamma, el Skoda Peaq, el Volkswagen ID.Polo, el Omoda 4 y el BYD Dolphin G.</p>
<h2>El que más interesa al bolsillo</h2><p>El Dacia Striker apunta a ser la opción familiar barata de la temporada. Hasta que tengamos sus datos completos, puedes comparar sus rivales directos en nuestro <a href="/coches/?carroceria=suv-m">catálogo de SUV medianos</a>, ordenados por lo que cuestan de verdad.</p>""",
 src=[("Motor16","https://www.motor16.com/las-ultimas-noticias/nuevos-modelos-espana-2026/")]),
dict(slug="record-electricos-septiembre-2026", k="mercado", fig="18,6%", date="2026-10-02", dtxt="2 oct 2026", min=4,
 img="noticia-record-septiembre",
 t="Récord histórico: casi uno de cada cinco coches nuevos vendidos en septiembre fue eléctrico",
 st="Los eléctricos puros marcan su mejor mes en España con 17.649 unidades, un 70,8 % más que hace un año.",
 body="""<p>Septiembre de 2026 pasará a la historia del mercado español. Los coches 100 % eléctricos sumaron 17.649 matriculaciones, la cifra más alta registrada nunca en un solo mes, y alcanzaron una cuota del 18,6 %. Hace solo un año esa cuota era del 12,1 %.</p>
<div class="fact k-mercado">El mercado total de turismos creció un <b>10,2 %</b> hasta <b>93.858</b> unidades, y los electrificados (eléctricos e híbridos enchufables) ya son el <b>34 %</b> de las ventas del mes.</div>
<h2>Los particulares tiran del mercado</h2>
<p>Tres de cada cuatro eléctricos vendidos en septiembre fueron a parar a particulares, no a flotas ni a empresas de alquiler. Es una señal de que el comprador de a pie ha perdido el miedo a la autonomía y al precio.</p>
<h2>Tesla manda, pero los chinos aprietan</h2>
<p>El Tesla Model 3 fue el eléctrico más vendido con 2.529 unidades, seguido del Model Y con 1.207. Detrás aparece un pelotón dominado por marcas chinas: el BYD Dolphin Surf, el BYD Atto 3 EVO, el Leapmotor B10, el BYD Atto 2 y los Geely E5 y E2 entran en el top 10.</p>
<table><thead><tr><th>#</th><th>Modelo</th><th class="num">Unidades</th></tr></thead><tbody>
<tr><td>1</td><td>Tesla Model 3</td><td class="num">2.529</td></tr><tr><td>2</td><td>Tesla Model Y</td><td class="num">1.207</td></tr><tr><td>3</td><td>BYD Dolphin Surf</td><td class="num">625</td></tr><tr><td>4</td><td>Kia EV3</td><td class="num">558</td></tr><tr><td>5</td><td>BYD Atto 3 EVO</td><td class="num">535</td></tr><tr><td>6</td><td>Leapmotor B10</td><td class="num">486</td></tr><tr><td>7</td><td>BYD Atto 2</td><td class="num">475</td></tr><tr><td>8</td><td>Toyota C-HR+</td><td class="num">438</td></tr><tr><td>9</td><td>Geely E5</td><td class="num">383</td></tr><tr><td>10</td><td>Geely E2</td><td class="num">371</td></tr>
</tbody></table>
<p>En lo que va de año, los eléctricos puros ya han superado las 100.000 unidades en España.</p>""",
 src=[("Autonomía Coches Eléctricos","https://autonomiacocheselectricos.es/articulos/coches-electricos-mas-vendidos-espana-septiembre-2026/"),("Motor16","https://www.motor16.com/las-ultimas-noticias/matriculaciones-turismos-septiembre-2026/")]),

dict(slug="marcas-chinas-tercio-electricos-espana", k="china", fig="33,6%", date="2026-10-02", dtxt="2 oct 2026", min=3,
 img="noticia-chinos-cuota",
 t="Las marcas chinas ya venden uno de cada tres eléctricos en España",
 st="BYD lidera, pero Leapmotor, Geely, Deepal y XPENG juntas ya venden más que el gigante chino.",
 body="""<p>El desembarco chino ya no es una promesa. En septiembre, las marcas de propiedad china matricularon 5.926 eléctricos en España, un 33,6 % de todo el segmento.</p>
<div class="fact k-china"><b>BYD</b> 2.290 · <b>Leapmotor</b> 1.412 · <b>Geely</b> 754 · <b>Deepal</b> 384 · <b>XPENG</b> 338</div>
<h2>BYD ya no está sola</h2>
<p>BYD es la segunda marca de eléctricos del mes, solo por detrás de Tesla. Pero lo llamativo es el empuje del resto: Leapmotor, apoyada en la red de Stellantis, se coloca con un 8 % de cuota, y Geely, recién llegada con el E2 y el E5, ya mete dos modelos en el top 10.</p>
<p>Sumadas, Leapmotor, Geely, Deepal y XPENG venden más que BYD sola. La competencia entre marcas chinas está empujando los precios a la baja, y eso se nota en las tarifas de las marcas europeas.</p>
<h2>Qué significa para el comprador</h2>
<p>Más oferta en el tramo de 15.000 a 30.000 euros, que es justo donde se mueve la mayoría de compradores particulares. Antes de decidir, compara el coste total: la depreciación de una marca nueva en el mercado puede comerse parte del ahorro inicial. Puedes calcularlo en nuestro <a href="/comparador/">comparador de coste real</a>.</p>""",
 src=[("Autonomía Coches Eléctricos","https://autonomiacocheselectricos.es/articulos/coches-electricos-mas-vendidos-espana-septiembre-2026/")]),

dict(slug="geely-e2-precio-espana", k="lanz china", fig="13.990€", date="2026-09-09", dtxt="9 sep 2026", min=3,
 img="prensa-geely-e2", press=True,
 t="Geely E2: el eléctrico más vendido de China llega a España por menos de 14.000 euros",
 st="Con descuentos y Plan Auto+ incluidos, se coloca en el terreno del Dacia Spring y el BYD Dolphin Surf.",
 body="""<p>Geely ha puesto a la venta en España el E2, un utilitario eléctrico de tracción trasera y 116 CV que llega con un precio muy agresivo. La versión de acceso arranca en 13.990 euros con reserva anticipada; sin promociones, la tarifa parte de 20.280 euros.</p>
<div class="fact k-lanz">Batería de <b>35 kWh</b>: hasta <b>252 km</b> WLTP · Batería de <b>47 kWh</b>: hasta <b>345 km</b> · Del 30 al 80 % en unos <b>25 min</b></div>
<h2>Química LFP y rivales claros</h2>
<p>Las dos baterías son LFP de CATL, una química más barata y duradera que tolera bien las cargas al 100 %. En el mercado se medirá con el Renault 5, el futuro Kia EV2 y el Skoda Epiq.</p>
<h2>¿Se fabricará en Valencia?</h2>
<p>Por ahora llega desde China. Se habla de producirlo en la planta de Ford en Almussafes, pero no hay confirmación oficial; el acuerdo apunta a primeros vehículos en 2028.</p>
<p>Ojo: el precio estrella incluye campañas, financiación y el adelanto de la ayuda del <a href="/ayudas/">Plan Auto+</a>. Calcula siempre el precio al contado y el coste total antes de firmar.</p>""",
 src=[("Carwow","https://www.carwow.es/noticias/7917/geely-e2-precio-espana-13990-euros")]),

dict(slug="byd-supera-ventas-2025-espana", k="china", fig="26.757", date="2026-08-04", dtxt="4 ago 2026", min=3,
 img="prensa-byd", press=True,
 t="BYD supera en siete meses todo lo que vendió en España en 2025",
 st="El Atto 2 es el modelo enchufable más vendido del país y el Seal U DM-i domina su segmento.",
 body="""<p>BYD matriculó 26.757 vehículos en España entre enero y julio, por encima de los 25.552 de todo 2025. Solo en julio colocó 3.898 unidades.</p>
<div class="fact k-china">Cuota en enchufables: <b>16,1 %</b> · Eléctricos: <b>10.586</b> (1.º del mercado) · Híbridos enchufables: <b>16.171</b></div>
<h2>Los modelos que tiran</h2>
<ul><li><strong>Atto 2:</strong> sumando sus versiones eléctrica e híbrida enchufable, 9.946 unidades.</li>
<li><strong>Seal U DM-i:</strong> 6.882 unidades y un 26,3 % del segmento de SUV medianos.</li>
<li><strong>Dolphin Surf:</strong> se queda con el 62,8 % del segmento de urbanos.</li></ul>
<p>La clave del éxito está en los híbridos enchufables, que crecen casi un 190 % y llevan la etiqueta CERO con precios de coche de combustión.</p>""",
 src=[("Movilidad Eléctrica","https://movilidadelectrica.com/ventas-byd-espana-2026-pulveriza-ventas-2025/")]),

dict(slug="plan-auto-plus-ayudas-coche-electrico-2026", k="ayuda", fig="4.500€", date="2026-09-20", dtxt="sep 2026", min=4,
 img="noticia-plan-auto",
 t="Plan Auto+: así funcionan las ayudas para comprar un eléctrico en 2026",
 st="Sustituye al MOVES III con un descuento directo en el concesionario, pero cambia las reglas.",
 body="""<p>El Plan Auto+ es el relevo del MOVES III, que terminó el 31 de diciembre de 2025. La gran diferencia es cómo se cobra: en lugar de una subvención que llegaba meses después, la ayuda se descuenta directamente en la factura de compra.</p>
<div class="fact k-ayuda">Hasta <b>4.500 €</b> de ayuda estatal + mínimo <b>1.000 €</b> del concesionario = hasta <b>5.500 €</b> · Solo etiqueta CERO · Precio máximo <b>45.000 €</b> sin IVA</div>
<h2>El criterio europeo</h2>
<p>La cuantía depende de que el coche sea eléctrico, económico y europeo. Un modelo fabricado fuera de Europa puede quedarse en torno al 75 % del máximo. Este punto afecta de lleno a muchos eléctricos chinos.</p>
<h2>Lo que se pierde respecto al MOVES</h2>
<ul><li>Ya no hay extra por achatarrar un coche viejo.</li><li>No subvenciona el punto de carga en casa; para eso hay que mirar ayudas autonómicas o municipales.</li><li>Los híbridos enchufables reciben menos que los eléctricos.</li></ul>
<p>El plan se anunció con carácter retroactivo desde el 1 de enero de 2026. Confirma siempre el estado oficial de la convocatoria antes de comprar.</p>""",
 src=[("Carwow","https://www.carwow.es/editorial/movilidad-electrica/ayudas-subvenciones-coches-electricos/plan-moves-vs-plan-auto-plus-diferencias-ayudas-coches-cargadores"),("RACE","https://www.race.es/ayudas-compra-vehiculos-electricos")]),

dict(slug="leapmotor-precios-espana-t03-b10", k="lanz china", fig="12.950€", date="2026-05-12", dtxt="may 2026", min=2,
 img="prensa-leapmotor", press=True,
 t="Leapmotor rompe precios: el T03 desde 12.950 euros y el B10 desde 22.500",
 st="La marca china asociada a Stellantis se pone agresiva en toda su gama con ayudas y financiación incluidas.",
 body="""<p>Leapmotor lanzó en primavera una campaña con precios muy bajos en toda su gama eléctrica. Los importes incluyen la ayuda del Plan Auto+ y 900 euros por certificados de ahorro energético al cambiar un coche térmico por uno eléctrico.</p>
<div class="fact k-lanz"><b>T03</b> 12.950 € · <b>B05</b> 19.500 € · <b>B10</b> 22.500 € · <b>C10</b> 28.000 € (financiando)</div>
<p>Al contado, cada modelo cuesta entre 750 y 1.500 euros más. La financiación exige un mínimo de 5.000 euros y 36 meses de permanencia, y los intereses no están incluidos.</p>
<p>El B10 se ha convertido en uno de los eléctricos más vendidos del país, y en septiembre fue el sexto del ranking.</p>""",
 src=[("Motor.es","https://www.motor.es/noticias/leapmotor-precios-espana-t03-b05-b10-c10-ofertas-mayo-2026-2026114256.html")]),

dict(slug="marcas-chinas-llegan-espana-2026", k="china", fig="+6", date="2026-06-15", dtxt="jun 2026", min=3,
 img="noticia-marcas-llegan",
 t="Seis marcas chinas que desembarcan en España este año",
 st="De Changan a Denza, la ofensiva china suma nombres nuevos en todos los segmentos.",
 body="""<p>A las marcas chinas que ya conocemos (BYD, MG, Omoda, Jaecoo, Lynk &amp; Co) se suman en 2026 nuevas firmas que buscan su hueco.</p>
<ul><li><strong>Geely:</strong> dueña de Volvo y Polestar, planea una red de unos 50 concesionarios.</li>
<li><strong>Changan:</strong> llega con varios SUV eléctricos.</li>
<li><strong>Chery:</strong> la matriz de Omoda y Jaecoo desembarca con su propia marca y empezará a fabricar en Barcelona.</li>
<li><strong>Lepas:</strong> otra firma de Chery, con SUV eléctricos de corte más premium.</li>
<li><strong>Denza:</strong> la marca premium de BYD, con Mercedes y Audi en el punto de mira.</li>
<li><strong>Exlantix:</strong> la apuesta de lujo del grupo Chery.</li></ul>
<p>La lección para el comprador es clara: más marcas significan más descuentos, pero también más incertidumbre sobre el valor de reventa y la red de talleres. Consulta la ficha de cada una en nuestra sección de <a href="/electricos-chinos/">eléctricos chinos</a>.</p>""",
 src=[("Think Big","https://blogthinkbig.com/que-marcas-chinas-de-coches-llegan-a-espana-en-2026")]),
]

GUIDES = [
dict(slug="etiquetas-dgt", img="guia-etiquetas",
 t="Etiquetas DGT explicadas: CERO, ECO, C y B",
 st="Qué etiqueta lleva cada tipo de coche y qué te permite en las zonas de bajas emisiones.",
 body="""<p>La DGT clasifica los vehículos en cuatro distintivos según sus emisiones. Los coches sin etiqueta son los más contaminantes y los que más restricciones sufren en las zonas de bajas emisiones (ZBE) de las ciudades.</p>
<h2><span class="tag cero">0</span> Etiqueta CERO</h2><p>Eléctricos de batería, eléctricos de autonomía extendida e híbridos enchufables con al menos 40 km de autonomía eléctrica. Acceso libre a las ZBE en la mayoría de ciudades y, a menudo, aparcamiento regulado gratuito o rebajado.</p>
<h2><span class="tag eco">ECO</span> Etiqueta ECO</h2><p>Híbridos convencionales, híbridos enchufables con menos de 40 km de autonomía eléctrica y coches de gas (GLP o GNC). Suelen tener acceso a las ZBE con algunas limitaciones.</p>
<h2><span class="tag c">C</span> Etiqueta C</h2><p>Gasolina matriculados desde 2006 y diésel desde septiembre de 2015, es decir, gasolina Euro 4, 5 y 6 y diésel Euro 6.</p>
<h2><span class="tag b">B</span> Etiqueta B</h2><p>Gasolina matriculados desde 2001 y diésel desde 2006, es decir, gasolina Euro 3 y diésel Euro 4 y 5.</p>
<h2>¿Y si mi coche no tiene etiqueta?</h2><p>Los gasolina anteriores a 2001 y los diésel anteriores a 2006 no tienen distintivo. Son los primeros en quedarse fuera de las ZBE.</p>
<p>Cada ayuntamiento decide qué puede hacer cada etiqueta en su ZBE, así que consulta siempre la ordenanza de tu ciudad. Puedes comprobar la etiqueta de tu coche con la matrícula en la web de la DGT.</p>"""),

dict(slug="cuanto-cuesta-cargar-coche-electrico-casa", img="guia-cargar-casa",
 t="Cuánto cuesta cargar un coche eléctrico en casa",
 st="La cuenta es sencilla: consumo por precio del kWh. Te enseñamos a hacerla con tu factura.",
 body="""<p>Cargar en casa es lo que hace que un eléctrico salga barato. La fórmula es simple: multiplica el consumo del coche (en kWh por cada 100 km) por lo que pagas por cada kWh de luz.</p>
<div class="fact k-guia">Ejemplo: un coche que gasta <b>15 kWh/100 km</b> con luz a <b>0,15 €/kWh</b> cuesta <b>2,25 €</b> cada 100 km. Un gasolina que gasta 6 L a 1,79 €/L cuesta <b>10,74 €</b>.</div>
<h2>Suma un poco por las pérdidas</h2><p>No toda la energía que sale del enchufe llega a la batería. Con un cargador de pared se pierde en torno a un 10 %, y con un enchufe doméstico algo más. Para una cuenta realista, súmale ese porcentaje al consumo.</p>
<h2>La tarifa importa más que el coche</h2><p>Con la tarifa de acceso 2.0TD, la luz es más barata de madrugada (de 0 a 8 h) y durante todo el fin de semana y los festivos. Programar la carga en ese periodo valle puede reducir mucho el precio por kWh. Muchas comercializadoras ofrecen además tarifas específicas para coche eléctrico.</p>
<h2>Potencia contratada y cargador</h2><p>Un cargador de pared habitual en una vivienda trabaja a 7,4 kW. Si tu potencia contratada es baja, puedes subirla o instalar un gestor de carga que reparte la potencia con el resto de la casa para que no salte el interruptor.</p>
<h2>Si vives en un piso</h2><p>Para instalar un punto de carga en tu plaza de garaje comunitario no necesitas permiso de la comunidad: basta con comunicarlo por escrito. Eso sí, la instalación tiene que hacerla un instalador autorizado. Pide al menos dos presupuestos, porque el precio cambia mucho según la distancia al contador.</p>
<p>¿Quieres ver cuánto ahorrarías con tus kilómetros? Prueba el <a href="/comparador/">comparador de coste real</a> y ajusta el porcentaje de carga en casa.</p>"""),

dict(slug="autonomia-real-coche-electrico-wltp", img="guia-autonomia",
 t="Autonomía real frente a la homologada: por qué no se cumple",
 st="El dato WLTP es una referencia para comparar, no una promesa. Así calculas la tuya.",
 body="""<p>Todos los coches nuevos se homologan con el ciclo WLTP, una prueba de laboratorio que mezcla ciudad, carretera y algo de autopista. Sirve para comparar coches entre sí en igualdad de condiciones, pero casi nadie conduce exactamente así.</p>
<h2>Lo que más consume</h2>
<ul><li><strong>La velocidad.</strong> A 120 km/h la resistencia del aire dispara el consumo. En autopista, la autonomía real suele quedarse claramente por debajo de la homologada.</li>
<li><strong>El frío.</strong> La batería rinde peor y la calefacción tira de ella. En invierno es normal perder bastante autonomía, sobre todo en trayectos cortos.</li>
<li><strong>El tamaño y las ruedas.</strong> Un SUV alto y unas llantas grandes gastan más que un compacto bajo con llanta pequeña.</li></ul>
<h2>Donde el eléctrico gana</h2><p>En ciudad pasa lo contrario que con un coche de gasolina: las frenadas recuperan energía y a baja velocidad el consumo es muy bajo. Muchos eléctricos superan su autonomía homologada en uso urbano.</p>
<h2>Cómo calcular la tuya</h2><p>Busca el consumo real del modelo en pruebas independientes y divide la capacidad útil de la batería entre ese consumo. Por ejemplo, 60 kWh útiles con un consumo de 20 kWh/100 km en autopista dan unos 300 km. Recuerda que en viaje no conviene bajar del 10 % ni cargar más allá del 80 % en cargadores rápidos, así que el tramo útil entre paradas es menor.</p>"""),

dict(slug="hibrido-o-electrico-cual-compensa", img="guia-hibrido-electrico",
 t="¿Híbrido o eléctrico? Cuál te sale más barato",
 st="Depende de cuántos kilómetros haces y de si puedes cargar en casa. Así lo decides.",
 body="""<p>Antes de comparar, conviene tener claros los tres tipos de coche electrificado que hay en el concesionario:</p>
<ul><li><strong>Híbrido (HEV):</strong> no se enchufa. Una batería pequeña ayuda al motor de gasolina y baja el consumo, sobre todo en ciudad. Etiqueta ECO.</li>
<li><strong>Híbrido enchufable (PHEV):</strong> tiene una batería mayor que se carga en la red y permite hacer decenas de kilómetros en eléctrico. Etiqueta CERO si supera los 40 km eléctricos.</li>
<li><strong>Eléctrico (BEV):</strong> solo batería y motor eléctrico. Etiqueta CERO.</li></ul>
<h2>El eléctrico compensa si...</h2><p>Puedes cargar en casa o en el trabajo, haces bastantes kilómetros al año y la mayoría de tus trayectos caben en una carga. Cuantos más kilómetros, más se nota el ahorro en energía y mantenimiento.</p>
<h2>El híbrido compensa si...</h2><p>No tienes dónde cargar, haces pocos kilómetros o viajas a menudo por zonas con pocos cargadores. Un buen híbrido gasta poco, no exige cambiar hábitos y suele mantener muy bien su valor de reventa.</p>
<h2>El enchufable, solo si lo enchufas</h2><p>Un híbrido enchufable que no se carga lleva una batería pesada a cuestas y puede gastar más que un híbrido normal. Tiene sentido si cargas a diario y tus trayectos habituales caben en su autonomía eléctrica.</p>
<p>La forma más fiable de decidir es poner tus números. En el <a href="/comparador/">comparador</a> puedes enfrentar un híbrido y un eléctrico con tus kilómetros, tus años y tu precio de la luz.</p>"""),

dict(slug="comprar-coche-electrico-segunda-mano", img="guia-segunda-mano",
 t="Comprar un eléctrico de segunda mano sin sustos",
 st="La batería es lo que más vale del coche. Esto es lo que tienes que comprobar.",
 body="""<p>Los eléctricos de ocasión se deprecian rápido, y eso los convierte en una compra muy interesante. La clave es saber qué mirar, porque la pieza más cara del coche es la batería.</p>
<h2>1. Pide el estado de salud de la batería</h2><p>El dato se llama SOH y se expresa en porcentaje de la capacidad original. Pide un informe de diagnóstico al vendedor o a un taller oficial. Por encima del 90 % es una batería en muy buen estado.</p>
<h2>2. Revisa la garantía de la batería</h2><p>La mayoría de marcas cubren la batería durante 8 años o 160.000 km, con un mínimo de capacidad garantizado. Comprueba la fecha de matriculación y si la garantía se transmite al nuevo dueño.</p>
<h2>3. Fíjate en la refrigeración</h2><p>Las baterías con refrigeración líquida aguantan mejor el calor y las cargas rápidas. Algunos modelos antiguos solo se enfrían por aire y su batería se degrada antes en climas calurosos.</p>
<h2>4. Comprueba la carga rápida</h2><p>Mira qué conector tiene (en Europa, CCS) y a qué potencia carga. Un coche que carga lento hace los viajes largos mucho más pesados.</p>
<h2>5. Lo de siempre, también</h2><p>Neumáticos (los eléctricos pesan y los gastan más), frenos, historial de mantenimiento y actualizaciones de software. Y prueba el coche con la batería bien cargada para ver la autonomía que marca.</p>"""),

dict(slug="renting-financiacion-o-contado", img="guia-renting",
 t="Renting, financiación o contado: qué te conviene",
 st="Cada fórmula encaja con un tipo de conductor. Te explicamos cuál es la tuya.",
 body="""<p>Hay tres formas principales de hacerte con un coche nuevo. Ninguna es mejor en todo: depende de cuánto tiempo lo vayas a tener y de cuánto quieras arriesgar.</p>
<h2>Contado</h2><p>Pagas el coche entero y es tuyo desde el primer día. No pagas intereses, pero inmovilizas mucho dinero y asumes toda la pérdida de valor. Ojo: muchas ofertas anunciadas solo valen financiando, y al contado el precio sube.</p>
<h2>Financiación clásica</h2><p>Pides un préstamo y pagas cuotas hasta terminar. Compara siempre la TAE, no solo la cuota, y revisa la comisión de apertura y si hay penalización por amortizar antes.</p>
<h2>Compra flexible (multiopción)</h2><p>Pagas cuotas bajas durante unos años y al final eliges: devolver el coche, cambiarlo por otro o pagar una cuota final grande y quedártelo. La marca garantiza un valor futuro del coche. Es útil si cambias de coche cada pocos años, pero exige permanencia y límites de kilómetros.</p>
<h2>Renting</h2><p>Pagas una cuota mensual que suele incluir seguro, mantenimiento, impuestos y asistencia. Nunca es tuyo. Te quita preocupaciones y el riesgo de depreciación, algo atractivo con eléctricos que evolucionan rápido, pero si te pasas de kilómetros o lo devuelves antes, penaliza.</p>
<p>Para comparar de verdad, suma todo lo que pagarías en cada caso durante los mismos años. El <a href="/comparador/">comparador de coste real</a> te ayuda con la parte de pérdida de valor y energía.</p>"""),
]

BRANDS = [
("BYD",1,"BYD Group",["Dolphin Surf","Atto 2","Atto 3 EVO","Seal U DM-i"],"Líder de las chinas en España y número uno en enchufables. Su fuerte son los híbridos enchufables con etiqueta CERO."),
("Leapmotor",1,"Stellantis (socio)",["T03","B05","B10","C10"],"Vende a través de la red de Stellantis y ya es la segunda china en eléctricos, con precios muy agresivos."),
("Geely",1,"Geely Holding",["E2","E5"],"Dueña de Volvo y Polestar. Recién llegada y con dos modelos ya en el top 10 de eléctricos."),
("MG",1,"SAIC",["MG4","MGS5","ZS"],"La pionera de las marcas chinas en España, con gama eléctrica, híbrida y de gasolina."),
("Deepal",1,"Changan",["S07","S05"],"La firma eléctrica de Changan, centrada en SUV con mucho equipamiento."),
("XPENG",1,"XPENG",["G6","G9","P7"],"Apuesta tecnológica: carga ultrarrápida y asistentes de conducción avanzados."),
("Omoda / Jaecoo",1,"Chery",["Omoda 5","Jaecoo 7"],"SUV con gama eléctrica e híbrida enchufable y precios ajustados."),
("Lynk & Co",1,"Geely Holding",["01","02","08"],"Nació con un modelo de suscripción y ahora también vende de forma tradicional."),
("Chery",0,"Chery",["Fabricación en Barcelona"],"La matriz de Omoda y Jaecoo llega con marca propia y producción en España."),
("Changan",0,"Changan",["SUV eléctricos"],"Desembarca con su propia marca tras abrir camino con Deepal."),
("Denza",0,"BYD Group",["Premium"],"La marca de lujo de BYD, pensada para competir con Mercedes y Audi."),
("Lepas",0,"Chery",["SUV eléctricos"],"Firma de Chery con un posicionamiento entre generalista y premium."),
]

TOP10 = [("Tesla Model 3",2529,0),("Tesla Model Y",1207,0),("BYD Dolphin Surf",625,1),("Kia EV3",558,0),("BYD Atto 3 EVO",535,1),("Leapmotor B10",486,1),("BYD Atto 2",475,1),("Toyota C-HR+",438,0),("Geely E5",383,1),("Geely E2",371,1)]


# ---------- noticias diarias: un archivo JSON por noticia en /noticias ----------
import json as _json, os as _os, glob as _glob
NOTICIAS_DIR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "noticias")
_MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
for _f in sorted(_glob.glob(_os.path.join(NOTICIAS_DIR, "*.json"))):
    _d = _json.load(open(_f, encoding="utf-8"))
    if any(a["slug"] == _d["slug"] for a in ARTICLES): continue
    _y, _m, _dd = _d["date"].split("-")
    _d.setdefault("dtxt", f"{int(_dd)} {_MESES[int(_m) - 1]} {_y}")
    _d.setdefault("img", "portada-" + _d["slug"][:60])
    _d.setdefault("fig", "")
    _d.setdefault("min", max(2, round(len(_d["body"].split()) / 200)))
    _d["src"] = [tuple(x) for x in _d.get("src", [])]
    ARTICLES.append(_d)
