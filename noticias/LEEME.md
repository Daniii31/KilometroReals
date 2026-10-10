# Noticias diarias de Kilómetro Real

Cada noticia es un archivo JSON en esta carpeta: `AAAA-MM-DD-slug.json`.

```json
{
  "slug": "precio-gasolina-hoy-10-octubre-2026",
  "k": "mercado",                     // analisis, dgt, mercado, china, lanz, ayuda, guia (se pueden combinar: "lanz china")
  "date": "2026-10-10",
  "t": "Titular claro, con el dato y la palabra clave (máx. ~90 caracteres)",
  "st": "Entradilla de 1-2 frases que resume la noticia (máx. ~160 caracteres).",
  "fig": "1,52 €",                    // dato clave para la portada (opcional)
  "figl": "litro de gasolina hoy",    // texto bajo el dato (opcional)
  "body": "<p>…</p><div class=\"fact\">…</div><h2>…</h2><p>… con enlaces internos a /coches/…, /mejores/…, /calculadoras/…</p>",
  "src": [["Nombre de la fuente", "https://url-de-la-fuente"]]
}
```

- Sin `img`: se genera sola una portada de diseño con el titular y el dato clave.
- Con foto propia: guárdala en `img/` en formato .webp y pon `"img": "nombre-sin-extension"`.
- Luego: `python3 build.py`.
