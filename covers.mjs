// Kilómetro Real · genera portadas de diseño (1600x900 y 800x450) para las noticias sin foto.
// Uso: node covers.mjs covers.json   (lista de {name, kicker, kind, title, fig, figl})
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
// Busca Playwright en varias rutas (entorno local o tarea programada)
let chromium;
for (const m of [process.env.PW_MODULE, '/home/claude/.npm-global/lib/node_modules/playwright/index.mjs', 'playwright'].filter(Boolean)) {
  try { ({ chromium } = await import(m)); break; } catch (e) {}
}
if (!chromium) { console.error('Playwright no disponible: portadas omitidas'); process.exit(0); }
const HERE = path.dirname(fileURLToPath(import.meta.url));
const list = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const logo = fs.readFileSync(path.join(HERE, 'brand/logo.svg'), 'utf8')
  .replace('<svg ', '<svg style="height:58px;width:auto" ')
  .replace('fill="#101D33"', 'fill="#FFFFFF"').replace('<g fill="#fff"', '<g fill="#101D33"');
const TINT = { mercado: '#1d3a7a', dgt: '#24553a', ayuda: '#6b5512', china: '#6e2222', lanz: '#3b2a75', analisis: '#1d3a7a', guia: '#1f5560' };
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
for (const c of list) {
  const t = TINT[c.kind] || '#1d3a7a';
  const size = c.title.length > 95 ? 62 : c.title.length > 70 ? 70 : 80;
  const fsz = !c.fig ? 0 : c.fig.length > 6 ? 120 : 150;
  const fig = c.fig ? `<div style="position:absolute;right:96px;bottom:96px;text-align:right"><div style="font-weight:800;font-size:${fsz}px;line-height:1;color:#F2C314;letter-spacing:-6px;font-variant-numeric:tabular-nums">${esc(c.fig)}</div><div style="font-size:30px;color:#c8d2e3;margin-top:10px;font-weight:600;max-width:520px;margin-left:auto">${esc(c.figl || '')}</div></div>` : '';
  const html = `<html><body style="margin:0;width:1600px;height:900px;font-family:Inter,sans-serif;color:#fff;background:radial-gradient(1400px 900px at 100% 0%,${t} 0%,#101D33 58%);position:relative;overflow:hidden">
  <svg style="position:absolute;right:-120px;bottom:-60px;opacity:.07" width="900" height="900" viewBox="0 0 100 100"><path d="M40 0h6L20 100H0zM54 0h6l40 100H80z" fill="#fff"/><path d="M48 8h4l1 12h-6zM47 32h6l1.5 18h-9zM45 62h10l2 30H43z" fill="#fff"/></svg>
  <div style="position:absolute;left:96px;top:84px;display:flex;align-items:center;gap:18px">${logo}<span style="font-size:34px;font-weight:800;letter-spacing:-1px">Kilómetro Real</span></div>
  <div style="position:absolute;left:96px;top:230px;font-size:26px;font-weight:800;letter-spacing:3px;color:#F2C314;text-transform:uppercase">${esc(c.kicker)}</div>
  <div style="position:absolute;left:96px;top:280px;width:${c.fig ? 780 : 1300}px;font-size:${size}px;line-height:1.06;font-weight:800;letter-spacing:-2.5px;text-wrap:balance">${esc(c.title)}</div>
  ${fig}
  <div style="position:absolute;left:0;right:0;bottom:0;height:18px;background:#0b1424"></div><div style="position:absolute;left:0;width:420px;bottom:0;height:18px;background:#F2C314"></div>
  </body></html>`;
  await p.setContent(html);
  await p.waitForTimeout(80);
  const out = path.join(HERE, 'img', c.name + '.png');
  await p.screenshot({ path: out });
  console.log('portada', c.name);
}
await b.close();
