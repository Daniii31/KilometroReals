import { chromium } from '/home/claude/.npm-global/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
for (const [s,n] of [[32,'favicon-32.png'],[180,'apple-touch-icon.png'],[192,'icon-192.png'],[512,'icon-512.png']]) {
  const p = await b.newPage({viewport:{width:s,height:s}});
  const r = s<64? s*0.18 : s*0.2;
  await p.setContent(`<body style="margin:0"><div style="width:${s}px;height:${s}px;background:#0d1726;border-radius:${n.startsWith('apple')?0:r}px;display:flex;align-items:center;justify-content:center;font-family:monospace;font-weight:700;color:#ffcc29;font-size:${s*0.27}px">€/km</div></body>`);
  await p.screenshot({path:'/home/claude/kr-build/icons/'+n, omitBackground:true});
}
await b.close();
