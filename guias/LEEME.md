# Guías de Kilómetro Real

Cada guía es un archivo JSON en esta carpeta: `slug.json`. Responden a una pregunta que la gente busca y no caducan.

```json
{
  "slug": "cuanto-cuesta-mantener-un-coche-al-ano",
  "date": "2026-10-13",                 // fecha de la última actualización
  "t": "Título con la pregunta o la palabra clave (máx. ~70 caracteres)",
  "st": "Entradilla de 1-2 frases (máx. ~160 caracteres).",
  "fig": "5.650 €",                    // dato para la portada automática (opcional)
  "figl": "al año, un compacto de gasolina",
  "body": "<p>…</p><div class=\"fact\">…</div><h2>…</h2> con enlaces a /coches/…, /mejores/…, /calculadoras/…",
  "faq": [["Pregunta", "Respuesta corta"]],   // salen como FAQ y como datos estructurados
  "src": [["Fuente", "https://…"]]            // opcional si todo sale de nuestro cálculo
}
```

Para actualizar una guía, edita su JSON y cambia `date`. La URL (`/guias/<slug>/`) no cambia nunca.
