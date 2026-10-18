# Kilómetro Real · instrucciones para Claude

Web estática de kilometroreal.com: el coste real de tener un coche en España (€/km). Todo se genera con Python.

## Estructura
- `build.py`: generador. `python3 build.py` crea la web completa en `dist/`.
- `models.py`: datos de los coches. `fuel.py`: precios medios de los carburantes de hoy.
- `content.py`: noticias y guías antiguas. **Las noticias nuevas van en `noticias/AAAA-MM-DD-slug.json`** (formato en `noticias/LEEME.md`).
- `guias/<slug>.json`: guías nuevas y duraderas (formato en `guias/LEEME.md`). Salen en `/guias/<slug>/` con FAQ y portada automática.
- `pages_extra.py`: página de precio de la gasolina, histórico mensual y comparativas A vs B (`vs_pairs.py`).
- `fuel_history.json`: un registro por día de los precios. **El build lo actualiza solo** con el día de `fuel.py`: no lo edites a mano. Genera el gráfico de `/precio-gasolina-hoy/` y una página por mes (`/precio-gasolina-hoy/octubre-2026/`).
- `provincias.json`: precios de todas las gasolineras resumidos por provincia. **Lo genera solo la GitHub Action `precios-provincias.yml`** (6:10 y 15:10, API del Ministerio, `tools/provincias.py`), que también reconstruye y publica: no lo edites a mano. Genera `/precio-gasolina-hoy/<provincia>/` (52 páginas con las 10 gasolineras más baratas) y la tabla por provincias. También guarda los municipios con 12 o más gasolineras (`cities`), que generan `/gasolineras-baratas/<ciudad>/` y el índice `/gasolineras-baratas/`.
- `covers.mjs`: genera la portada de diseño de las noticias sin foto (necesita Playwright; si no está, se omite).
- `dist/`: la web generada. **El servidor publica `dist/` automáticamente** desde la rama `main` cada 10 minutos (cron de cPanel).

## Rutina diaria de noticias
1. Busca las noticias del motor en España del día, con fuentes fiables: matriculaciones (ANFAC), DGT, ayudas, precios, lanzamientos y marcas chinas.
2. Escribe **4 noticias propias**: redactadas desde cero, en español claro, con datos y fuente enlazada. Nada copiado. Cada noticia enlaza a fichas de `/coches/…`, rankings `/mejores/…` o calculadoras. Una de ellas es siempre la del precio de la gasolina de hoy (slug `precio-gasolina-hoy-D-mes-AAAA`). Si un día no hay 3 noticias más de las últimas 24 horas, completa con noticias de los últimos 3 días que aún no estén publicadas (comprueba `noticias/`), nunca con cifras inventadas.
   Si una noticia presenta un coche nuevo con precio en España que no está en `models.py`, añádelo (precio de tarifa de la versión principal; consumo real estimado a partir de un modelo hermano con el mismo motor).
   **Titulares para Google Discover y News:** de 60 a 90 caracteres, con el dato concreto (precio, cifra, fecha) y a quién afecta ("si tienes un diésel", "en Madrid"). Que el titular cuente la noticia, sin trampas tipo "no te lo vas a creer", sin mayúsculas gritonas y sin prometer lo que el texto no da. La entradilla (`st`) responde a "¿y esto en qué me afecta?". Un dato fuerte en `fig` hace la portada más llamativa.
3. Actualiza `fuel.py` con el precio medio de hoy (gasolina 95, 98, diésel, diésel premium y GLP). Fuentes por orden: dieselogasolina.com, repostaje.es/precios-miteco, gasolineras.facua.org, fuelobserver.es (todas con datos del Ministerio). Si una no abre, usa la siguiente y cámbiala en `src`. Mueve los valores anteriores a `prev`.
4. Ejecuta `python3 build.py` y comprueba que termina con "OK N páginas".
5. Haz commit de todo, incluido `dist/`, y push a `main`.

## Rutina semanal de crecimiento (lunes)
1. **6 comparativas nuevas** al final de `vs_pairs.py` (una línea `VS_PAIRS += [...]` con la fecha): cruces que la gente busca ("X o Y", rivales directos del mismo segmento y precio). Solo ids que existan en `models.py` y que no estén ya en la lista.
2. **1 guía nueva** en `guias/`: una pregunta muy buscada sobre el coste de tener coche que aún no tengamos (mira `content.py` GUIDES y `guias/`). Las cifras salen del propio cálculo (`build.K`) o de fuentes citadas en `src`. Con 3 o 4 preguntas en `faq`.
3. **Precios al día**: comprueba en fuentes abiertas el precio de 5 modelos muy vendidos de `models.py` y corrígelo si ha cambiado. Añade los lanzamientos de la semana con precio confirmado.
4. Build, commit y push como en la rutina diaria.

## Informe mensual (los días 1 a 5 de cada mes)
Cuando ANFAC publique las matriculaciones del mes anterior, crea `informes/AAAA-MM.json` copiando el formato de `informes/2026-09.json`:
el top 10 de modelos con sus unidades exactas, el total de turismos del mes y al menos una fuente enlazada.
En `ids` pon las versiones de cada modelo que existan en `models.py` (la más barata de comprar se usa como versión de acceso).
Si ya existe el archivo de ese mes, no lo dupliques. El build genera la página en `/informes/<slug>/` y el aviso de la portada.

## Reglas
- No cambiar las URLs existentes, el código de AdSense (`ca-pub-8706325038832951`) ni `ads.txt`.
- No inventar cifras: cada número de una noticia sale de una fuente abierta y citada.
- Todo en español de España. Sin rayas largas (—) en el texto.
