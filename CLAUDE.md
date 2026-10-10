# Kilómetro Real · instrucciones para Claude

Web estática de kilometroreal.com: el coste real de tener un coche en España (€/km). Todo se genera con Python.

## Estructura
- `build.py`: generador. `python3 build.py` crea la web completa en `dist/`.
- `models.py`: datos de los coches. `fuel.py`: precios medios de los carburantes de hoy.
- `content.py`: noticias y guías antiguas. **Las noticias nuevas van en `noticias/AAAA-MM-DD-slug.json`** (formato en `noticias/LEEME.md`).
- `pages_extra.py`: página de precio de la gasolina y comparativas A vs B (`vs_pairs.py`).
- `covers.mjs`: genera la portada de diseño de las noticias sin foto (necesita Playwright; si no está, se omite).
- `dist/`: la web generada. **El servidor publica `dist/` automáticamente** desde la rama `main` cada 30 minutos.

## Rutina diaria de noticias
1. Busca las noticias del motor en España del día, con fuentes fiables: matriculaciones (ANFAC), DGT, ayudas, precios, lanzamientos y marcas chinas.
2. Escribe 2 o 3 noticias **propias**: redactadas desde cero, en español claro, con datos y fuente enlazada. Nada copiado. Cada noticia enlaza a fichas de `/coches/…`, rankings `/mejores/…` o calculadoras.
3. Actualiza `fuel.py` con el precio medio de hoy (gasolina 95, 98, diésel, diésel premium y GLP). Fuente: dieselogasolina.com o el Geoportal del Ministerio. Mueve los valores anteriores a `prev`.
4. Ejecuta `python3 build.py` y comprueba que termina con "OK N páginas".
5. Haz commit de todo, incluido `dist/`, y push a `main`.

## Reglas
- No cambiar las URLs existentes, el código de AdSense (`ca-pub-8706325038832951`) ni `ads.txt`.
- No inventar cifras: cada número de una noticia sale de una fuente abierta y citada.
- Todo en español de España. Sin rayas largas (—) en el texto.
