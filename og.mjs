import { chromium } from '/home/claude/.npm-global/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1200,height:630}});
await p.setContent(`<body style="margin:0;width:1200px;height:630px;background:linear-gradient(180deg,#f5f7fa,#fff);font-family:Arial,Helvetica,sans-serif;color:#0d1726;display:flex;flex-direction:column;justify-content:center;padding:0 90px;box-sizing:border-box">
<div style="display:flex;align-items:center;gap:16px;font-weight:800;font-size:40px"><span style="background:#0d1726;color:#ffcc29;font-family:monospace;font-size:26px;padding:8px 12px;border-radius:12px">€/km</span>Kilómetro Real</div>
<div style="font-size:72px;font-weight:800;line-height:1.05;margin-top:40px;letter-spacing:-2px">¿Cuánto te cuesta <span style="background:linear-gradient(transparent 62%,#ffcc29 62%,#ffcc29 92%,transparent 92%)">de verdad</span><br>tu próximo coche?</div>
<div style="font-size:30px;color:#2b3747;margin-top:30px">Compara 169 coches en euros por kilómetro</div>
<div style="margin-top:44px;border-bottom:4px dashed #c9d3e1;width:520px"></div></body>`);
await p.screenshot({path:'/home/claude/kr-build/img/og.png'}); await b.close();
