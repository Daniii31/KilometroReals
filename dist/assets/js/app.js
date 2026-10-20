/* Kilómetro Real · herramientas e interfaz. Datos orientativos en /assets/data/coches.json */
(function(){
"use strict";
const $=s=>document.querySelector(s), $$=s=>Array.from(document.querySelectorAll(s));
const EN=document.documentElement.lang==="en";
const sepT=EN?",":".", sepD=EN?".":",";
const num=v=>String(Math.round(v)).replace(/\B(?=(\d{3})+(?!\d))/g,sepT);
const dec=(v,n)=>{const s=v.toFixed(n).split(".");return s[0].replace(/\B(?=(\d{3})+(?!\d))/g,sepT)+(n?sepD+s[1]:"")};
const eur=v=>EN?"€"+num(v):num(v)+" €";
const e2=v=>EN?"€"+dec(v,2):dec(v,2)+" €";
const pk=v=>dec(v,3);
const PK=v=>EN?"€"+pk(v):pk(v)+" €";
const L=EN?{
 type:{ev:"Electric",phev:"Plug-in hybrid",hev:"Hybrid",mhev:"Mild hybrid",ice:"Combustion"},cheaper:"CHEAPER",perMonth:"a month",in:"in",years:"years",
 verdict:(km,w,d,y,m)=>`At ${km} km a year, the <strong>${w}</strong> saves you <b>${d}</b> over ${y} years, about <b>${m} a month</b>.`,
 shareTxt:(w,d,l)=>`The ${w} would save me ${d} compared with the ${l}. Check it:`,share:"Share",fullBreak:"See the full breakdown",
 cars:"/en/cars/",compare:"/en/compare/",value:"value",energy:"energy",insurance:"insurance",service:"servicing",
 rows:["List price","Cost per km","Cost a month","Depreciation","Energy","Power","Boot","Range","Consumption"],
 notFound:"We can't find that model. Pick one from the list.",copied:"Link copied",models:"models",
 picks:["Best choice","Second choice","Third choice"],top3:"Your 3 cars with the lowest real cost",withKm:km=>`a month with your ${km} km a year`,
 cmp2:"Compare the top two",none:"No models match. Try a higher budget.",dataErr:"We couldn't load the data. Reload the page.",
 totalTrip:"total cost",perPerson:"per person",fuel:"of fuel",elec:"of electricity",per100:"per 100 km",
 tripSay:(km,r)=>`That's <b>${km} km</b>${r?" there and back":""}.`,tripShare:(km,p)=>`Our ${km} km trip costs ${p} per person.`,
 thisCharge:"this charge",toBat:"into the battery",rangeAdd:"of approximate range",
 monthly:"monthly payment",totalPaid:"total paid",interest:"interest and fees",apr:"approx. APR",
 finSay:(P,n,cash,extra)=>`You finance <b>${P}</b> over ${n} months. Paying cash would cost ${cash}: financing costs you ${extra} more.`,
 pick2:"Choose two cars from the list.",save:"you save",pay:"you pay more",withKmY:km=>`at ${km} km/year`,
 beFirst:(a,b)=>`The <b>${a}</b> is cheaper <b>from the very first kilometre</b> compared with the ${b}.`,
 beAt:(a,km,b)=>`The <b>${a}</b> pays off from <b>${km} km a year</b> compared with the ${b}.`,
 beNever:(a,b)=>`With these figures, the ${a} doesn't pay off against the ${b} even at 60,000 km a year.`,
 beNote:(y,a)=>`Total difference over ${y} years with the ${a}. Highlighted when you save.`,
 lab:{cero:"ZERO label: free access to almost every low-emission zone and parking perks in many cities.",eco:"ECO label: can enter most low-emission zones, sometimes with limits.",
  gC:"C label: Euro 4 petrol or newer.",gB:"B label: Euro 3 petrol.",none:"No label: among the first to be banned from low-emission zones.",
  dC:"C label: Euro 6 diesel.",d15:"It depends on the date: from September 2015 it usually has the C label; before that, the B.",dB:"B label: Euro 4 or Euro 5 diesel."},
 labNote:"Approximate. Check your number plate on the DGT website.",
 req:"Fill in this field.",mail:"Enter a valid email address.",short:"Write a little more (at least 20 characters).",consent:"You need to accept the privacy policy.",
 sending:"Sending…",sent:"Thanks! We've received your message and will reply soon.",sendErr:"It couldn't be sent. Try again in a few minutes or email us directly.",
 badNum:"Enter a valid number."
}:{
 type:{ev:"Eléctrico",phev:"Híbrido enchufable",hev:"Híbrido",mhev:"Microhíbrido",ice:"Combustión"},cheaper:"MÁS BARATO",perMonth:"al mes",in:"en",years:"años",
 verdict:(km,w,d,y,m)=>`Con ${km} km al año, el <strong>${w}</strong> te ahorra <b>${d}</b> en ${y} años, unos <b>${m} al mes</b>.`,
 shareTxt:(w,d,l)=>`El ${w} me ahorraría ${d} frente al ${l}. Compruébalo:`,share:"Compartir",fullBreak:"Ver el desglose completo",
 cars:"/coches/",compare:"/comparador/",value:"valor",energy:"energía",insurance:"seguro",service:"taller",
 rows:["Precio de tarifa","Coste por km","Coste al mes","Pérdida de valor","Energía","Potencia","Maletero","Autonomía","Consumo"],
 notFound:"No encontramos ese modelo. Elige uno de la lista.",copied:"Enlace copiado",models:"modelos",
 picks:["Mejor opción","Segunda opción","Tercera opción"],top3:"Tus 3 coches con menor coste real",withKm:km=>`al mes con tus ${km} km al año`,
 cmp2:"Comparar los dos primeros",none:"No hay modelos con esas condiciones. Prueba a subir el presupuesto.",dataErr:"No se han podido cargar los datos. Recarga la página.",
 totalTrip:"coste total",perPerson:"por persona",fuel:"de combustible",elec:"de electricidad",per100:"cada 100 km",
 tripSay:(km,r)=>`Son <b>${km} km</b>${r?" ida y vuelta":""}.`,tripShare:(km,p)=>`Nuestro viaje de ${km} km sale a ${p} por persona.`,
 thisCharge:"esta carga",toBat:"energía a la batería",rangeAdd:"de autonomía aproximada",
 monthly:"cuota al mes",totalPaid:"pagas en total",interest:"intereses y comisión",apr:"TAE aproximada",
 finSay:(P,n,cash,extra)=>`Financias <b>${P}</b> a ${n} meses. Al contado pagarías ${cash}: financiar te cuesta ${extra} más.`,
 pick2:"Elige dos coches de la lista.",save:"ahorras",pay:"pagas de más",withKmY:km=>`con ${km} km/año`,
 beFirst:(a,b)=>`El <b>${a}</b> sale más barato <b>desde el primer kilómetro</b> frente al ${b}.`,
 beAt:(a,km,b)=>`El <b>${a}</b> compensa a partir de <b>${km} km al año</b> frente al ${b}.`,
 beNever:(a,b)=>`Con estos datos, el ${a} no llega a compensar frente al ${b} ni con 60.000 km al año.`,
 beNote:(y,a)=>`Diferencia total en ${y} años con el ${a}. En azul, cuando ahorras.`,
 lab:{cero:"Etiqueta CERO: acceso libre a casi todas las zonas de bajas emisiones y ventajas de aparcamiento en muchas ciudades.",eco:"Etiqueta ECO: puede entrar en la mayoría de zonas de bajas emisiones, a veces con limitaciones.",
  gC:"Etiqueta C: gasolina Euro 4 o posterior.",gB:"Etiqueta B: gasolina Euro 3.",none:"Sin etiqueta: es de los primeros en quedarse fuera de las zonas de bajas emisiones.",
  dC:"Etiqueta C: diésel Euro 6.",d15:"Depende de la fecha: si se matriculó desde septiembre de 2015 suele tener la C; si es anterior, la B.",dB:"Etiqueta B: diésel Euro 4 o Euro 5."},
 labNote:"Orientativo. Confirma con tu matrícula en la sede electrónica de la DGT.",
 req:"Rellena este campo.",mail:"Escribe un correo válido.",short:"Cuéntanos un poco más (mínimo 20 caracteres).",consent:"Tienes que aceptar la política de privacidad.",
 sending:"Enviando…",sent:"¡Gracias! Hemos recibido tu mensaje y te responderemos pronto.",sendErr:"No se ha podido enviar. Prueba de nuevo en unos minutos o escríbenos directamente.",
 badNum:"Escribe un número válido."
};
const LAB={cero:"0",eco:"ECO",c:"C"};
const D={km:15000,y:5,home:80,gas:1.766,die:1.887,glp:1.099,ph:0.15,pp:0.49};
let CARS=[],BY={},BYNAME={};

function cost(c,S){
  S=S||D;
  const resid=c.p*Math.pow(Math.pow(c.res,1/5),S.y),dep=c.p-resid,h=S.home/100,elec=h*S.ph+(1-h)*S.pp,km=S.km*S.y;
  const fuel={g:S.gas,d:S.die,glp:S.glp}[c.f]||S.gas;let energy;
  if(c.t==="ev")energy=c.c/100*km*elec;
  else if(c.t==="phev"){const sh=Math.min(.8,c.rng*.75*240/S.km)*h;energy=km*(sh*18/100*S.ph+(1-sh)*c.c/100*fuel)}
  else energy=c.c/100*km*fuel;
  const ins=c.ins*S.y,mnt=c.mnt*S.y,tax=c.tax*S.y,total=dep+energy+ins+mnt+tax;
  return{dep,energy,ins,mnt,tax,total,resid,perKm:total/km,month:total/S.y/12};
}
const tag=c=>`<span class="tag ${c.lab}">${LAB[c.lab]}</span>`;
const findBrand=v=>{if(!v)return null;const n=x=>x.normalize("NFD").replace(/[\u0300-\u036f]/g,"").trim().toLowerCase(),t=n(v);const c=CARS.find(c=>n(c.b)===t);return c?c.b:null};
const brandSlug=b=>b.normalize("NFKD").replace(/[\u0300-\u036f]/g,"").toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"");
const findCar=v=>{if(!v)return null;v=v.trim().toLowerCase();if(!v)return null;return BYNAME[v]||CARS.find(c=>c.n.toLowerCase().includes(v))||null};
/* buscador de coches propio: el <datalist> nativo va mal en el móvil (iOS solo enseña 3 sugerencias y "change" no salta hasta salir del campo) */
const nrm=x=>String(x).normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase().replace(/[^a-z0-9#.+ ]/g," ").replace(/\s+/g," ").trim();
function acMatches(q,brands){const t=nrm(q).split(" ").filter(Boolean);if(!t.length)return[];
  const out=[];if(brands){const seen=new Set();for(const c of CARS){if(seen.has(c.b))continue;seen.add(c.b);const b=nrm(c.b);if(t.every(w=>b.includes(w)))out.push({v:c.b,s:EN?"Brand":"Marca"})}}
  const hit=CARS.filter(c=>{const h=nrm(c.n);return t.every(w=>h.includes(w))}).sort((a,b)=>{const x=nrm(a.n).startsWith(t[0])?0:1,y=nrm(b.n).startsWith(t[0])?0:1;return x-y||a.n.length-b.n.length});
  return out.slice(0,2).concat(hit.slice(0,8).map(c=>({v:c.n,s:""})))}
function acAttach(inp){if(inp._ac)return;inp._ac=1;inp.removeAttribute("list");inp.setAttribute("autocomplete","off");inp.setAttribute("autocorrect","off");inp.setAttribute("autocapitalize","off");inp.setAttribute("spellcheck","false");
  inp.setAttribute("role","combobox");inp.setAttribute("aria-autocomplete","list");inp.setAttribute("aria-expanded","false");
  const wrap=inp.parentElement;if(getComputedStyle(wrap).position==="static")wrap.style.position="relative";
  const ul=document.createElement("ul");ul.className="acl";ul.setAttribute("role","listbox");ul.hidden=true;inp.insertAdjacentElement("afterend",ul);
  const brands=inp.classList.contains("carsearch");let items=[],act=-1;
  const close=()=>{ul.hidden=true;act=-1;inp.setAttribute("aria-expanded","false")};
  const pick=v=>{inp.value=v;close();inp.dispatchEvent(new Event("change",{bubbles:true}))};
  const draw=()=>{items=acMatches(inp.value,brands);if(!items.length){ul.innerHTML=inp.value.trim()?`<li class="acn">${EN?"No matches":"Sin resultados"}</li>`:"";ul.hidden=!inp.value.trim();return}
    ul.innerHTML=items.map((it,i)=>`<li role="option" data-i="${i}" class="${i===act?"on":""}">${it.v.replace(/</g,"&lt;")}${it.s?`<small>${it.s}</small>`:""}</li>`).join("");ul.hidden=false;inp.setAttribute("aria-expanded","true")};
  inp.addEventListener("input",()=>{act=-1;draw()});
  inp.addEventListener("focus",()=>{if(findCar(inp.value)&&BYNAME[inp.value.trim().toLowerCase()]){setTimeout(()=>{try{inp.select()}catch(e){}},0)}});
  inp.addEventListener("keydown",e=>{if(ul.hidden&&e.key!=="Enter")return;
    if(e.key==="ArrowDown"||e.key==="ArrowUp"){e.preventDefault();act=(act+(e.key==="ArrowDown"?1:-1)+items.length)%items.length;draw()}
    else if(e.key==="Enter"){if(!ul.hidden&&items.length){e.preventDefault();pick(items[Math.max(act,0)].v)}}
    else if(e.key==="Escape")close()});
  ul.addEventListener("pointerdown",e=>e.preventDefault());ul.addEventListener("mousedown",e=>e.preventDefault());
  ul.addEventListener("click",e=>{const li=e.target.closest("li[data-i]");if(li)pick(items[+li.dataset.i].v)});
  inp.addEventListener("blur",()=>setTimeout(close,120))}
function datalist(){$$('input[list="cars"]').forEach(acAttach)}
function toast(msg){let t=$(".toast");if(!t){t=document.createElement("div");t.className="toast";t.setAttribute("role","status");document.body.appendChild(t)}t.textContent=msg;t.classList.add("show");clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove("show"),2200)}
function fieldErr(inp,msg){inp.classList.toggle("bad",!!msg);let e=inp.parentElement.querySelector(".err");if(msg){if(!e){e=document.createElement("p");e.className="err";inp.parentElement.appendChild(e)}e.textContent=msg;inp.setAttribute("aria-invalid","true")}else{if(e)e.remove();inp.removeAttribute("aria-invalid")}}
function carInput(inp,cb){inp.addEventListener("change",()=>{const c=findCar(inp.value);if(c){fieldErr(inp,"");if(inp.value!==c.n)inp.value=c.n;cb(c)}else fieldErr(inp,L.notFound)})}


/* ---------- ¿cuánto me cuesta mi coche? ---------- */
const VSP=new Set(window.KR_VS||[]);
function initMiCoche(){
  const f=$("#micoche");if(!f)return;datalist();
  const inp=$("#mc-car"),km=$("#mc-km"),yy=$("#mc-y"),out=$("#mc-res");let car=null;
  const parts=[["dep","Pérdida de valor"],["energy","Energía"],["ins","Seguro"],["mnt","Mantenimiento"],["tax","Impuesto"]];
  const render=()=>{if(!car)return;const S={...D,km:+km.value,y:+yy.value},k=cost(car,S);
    const bar=parts.map(([p,n],i)=>`<i class="b${i}" style="width:${(k[p]/k.total*100).toFixed(1)}%" title="${n}"></i>`).join("");
    const leg=parts.map(([p,n],i)=>`<li><span class="dot b${i}"></span>${n}<b>${eur(k[p]/S.y/12)}/mes</b></li>`).join("");
    const alts=CARS.filter(c=>c.id!==car.id&&c.body===car.body).map(c=>({c,k:cost(c,S)})).filter(x=>x.k.total<k.total).sort((a,b)=>a.k.total-b.k.total);
    const pick=[];const seen=new Set();for(const x of alts){if(seen.has(x.c.b))continue;seen.add(x.c.b);pick.push(x);if(pick.length===3)break}
    const altH=pick.length?`<h3 class="mc-h">Con estos ${car.body.startsWith("suv")?"SUV":"coches"} parecidos ahorrarías</h3><div class="mc-alts">${pick.map(x=>{const save=(k.total-x.k.total)/S.y/12,slug=VSP.has(car.id+"-vs-"+x.c.id)?`/comparar/${car.id}-vs-${x.c.id}/`:VSP.has(x.c.id+"-vs-"+car.id)?`/comparar/${x.c.id}-vs-${car.id}/`:`/comparador/#${car.id}-vs-${x.c.id}`;return `<a class="mc-alt" href="${slug}"><span class="nm">${x.c.n}</span><span class="muted">${eur(x.c.p)} · ${eur(x.k.month)}/mes</span><b class="good-t">−${eur(save)} al mes</b></a>`}).join("")}</div>`:`<p class="mc-best">Es de los más baratos de tener en su categoría. Buena elección.</p>`;
    out.innerHTML=`<div class="mc-top"><div><span class="muted">Tu ${car.n} te cuesta</span><b class="mc-big">${eur(k.month)}<small> al mes</small></b><span class="muted">${PK(k.perKm)} por km · ${eur(k.total)} en ${S.y} años</span></div><a class="btn ghost" href="${L.cars}${car.id}/">Ver ficha</a></div>
      <div class="mc-bar" aria-hidden="true">${bar}</div><ul class="mc-leg">${leg}</ul>${altH}`;
    try{history.replaceState(null,"","?coche="+car.id+"&km="+S.km+"&y="+S.y)}catch(e){}};
  carInput(inp,c=>{car=c;render()});[km,yy].forEach(x=>x.addEventListener("change",render));
  const p=new URLSearchParams(location.search);if(p.get("km"))km.value=p.get("km");if(p.get("y"))yy.value=p.get("y");
  if(p.get("coche")&&BY[p.get("coche")]){car=BY[p.get("coche")];inp.value=car.n;render()}
}

/* ---------- duelo ---------- */
function duelHTML(A,B,S){
  const ka=cost(A,S),kb=cost(B,S),wA=ka.total<=kb.total,d=Math.abs(ka.total-kb.total);
  const side=(c,k,w)=>`<div class="side-res${w?" win":""}">${w?`<span class="crown">${L.cheaper}</span>`:""}<div class="nm"><a href="${L.cars}${c.id}/">${c.n}</a></div><div class="meta" style="display:flex;gap:6px;align-items:center;margin-top:4px">${tag(c)}<span class="type t-${c.t}">${L.type[c.t]}</span></div><div class="pk">${EN?"€":""}<span data-count="${k.perKm.toFixed(3)}" data-dec="3">${pk(k.perKm)}</span>${EN?"":" €"}<small>/km</small></div><div class="mo">${eur(k.month)} ${L.perMonth} · ${eur(k.total)} ${L.in} ${S.y} ${L.years}</div></div>`;
  const w=wA?A:B,l=wA?B:A;
  return `<div class="duel">${side(A,ka,wA)}${side(B,kb,!wA)}</div><p class="verdict">${L.verdict(num(S.km),w.n,eur(d),S.y,eur(d/S.y/12))} <button type="button" class="btn ghost share" style="padding:6px 12px;margin-left:4px" data-text="${L.shareTxt(w.n,eur(d),l.n)}">${L.share}</button></p>`;
}
function initHomeDuel(){
  const box=$("#duel");if(!box)return;datalist();
  const a=$("#qa"),b=$("#qb"),out=$("#duelres");let A=findCar(a.value),B=findCar(b.value);
  const run=()=>{if(A&&B){out.innerHTML=duelHTML(A,B,D)+`<p style="margin-top:12px"><a class="btn" href="${L.compare}#${A.id}-vs-${B.id}">${L.fullBreak}</a></p>`;countUp(out)}};
  carInput(a,c=>{A=c;run()});carInput(b,c=>{B=c;run()});
  box.addEventListener("submit",e=>{e.preventDefault();run()});
  $$("[data-pair]").forEach(x=>x.addEventListener("click",()=>{const[p,q]=x.dataset.pair.split("|");A=BY[p];B=BY[q];a.value=A.n;b.value=B.n;fieldErr(a,"");fieldErr(b,"");run()}));
  run();
}

/* ---------- comparador ---------- */
function initComparador(){
  const root=$("#comparador");if(!root)return;datalist();
  const S={...D},a=$("#ca"),b=$("#cb");
  const m=(location.hash||"").slice(1).split("-vs-");
  let A=BY[m[0]]||BY["geely-e2"],B=BY[m[1]]||BY["seat-ibiza-1-0-tsi"];
  a.value=A.n;b.value=B.n;
  ["km","y","home","gas","die","glp","ph","pp"].forEach(id=>{const el=$("#s-"+id);if(el)el.value=S[id]});
  const draw=()=>{
    $("#v-km").textContent=num(S.km);$("#v-y").textContent=S.y;$("#v-home").textContent=S.home+" %";
    $("#cres").innerHTML=duelHTML(A,B,S);countUp($("#cres"));addRecent(A.id,B.id);showRecent();
    const ka=cost(A,S),kb=cost(B,S),mx=Math.max(ka.total,kb.total);
    const seg=k=>[["dep","c-dep"],["energy","c-energy"],["ins","c-ins"],["mnt","c-mnt"],["tax","c-tax"]].map(([x,c])=>`<span class="${c}" style="width:${k[x]/mx*100}%" title="${eur(k[x])}"></span>`).join("");
    $("#cbars").innerHTML=[[A,ka],[B,kb]].map(([c,k])=>`<div><div class="bl"><strong>${c.n}</strong><span class="muted">${L.value} ${eur(k.dep)} · ${L.energy} ${eur(k.energy)} · ${L.insurance} ${eur(k.ins)} · ${L.service} ${eur(k.mnt)}</span></div><div class="bar">${seg(k)}</div></div>`).join("");
    const R=L.rows,rows=[[R[0],c=>c.p,eur,"min"],[R[1],c=>cost(c,S).perKm,PK,"min"],[R[2],c=>cost(c,S).month,eur,"min"],
      [R[3],c=>cost(c,S).dep,eur,"min"],[R[4],c=>cost(c,S).energy,eur,"min"],[R[5],c=>c.cv,v=>v+(EN?" hp":" CV"),"max"],
      [R[6],c=>c.trunk,v=>v?v+" L":"—","max"],[R[7],c=>c.t==="ev"||c.t==="phev"?c.rng:0,v=>v?v+" km":"—","max"],
      [R[8],c=>c.c,(v,c)=>dec(v,1)+(c.t==="ev"?" kWh":" L")+"/100 km",null]];
    $("#cspecs").innerHTML=`<thead><tr><th></th><th>${A.n}</th><th>${B.n}</th></tr></thead><tbody>`+rows.map(([l,f,fmt,best])=>{const va=f(A),vb=f(B);const ba=best&&va!==vb&&((best==="min")===(va<vb)),bb=best&&va!==vb&&!ba;return `<tr><th>${l}</th><td class="${ba?"better":""}">${fmt(va,A)}</td><td class="${bb?"better":""}">${fmt(vb,B)}</td></tr>`}).join("")+"</tbody>";
    const rivals=CARS.filter(c=>c.body===A.body&&c.id!==A.id&&c.id!==B.id).map(c=>({c,k:cost(c,S)})).sort((x,y)=>x.k.perKm-y.k.perKm).slice(0,6);
    $("#crivals").innerHTML=rivals.map(({c,k})=>`<li><span><a href="#${A.id}-vs-${c.id}" data-swap="${c.id}">${c.n}</a><span class="sub">${L.type[c.t]} · ${eur(c.p)}</span></span><span class="num">${PK(k.perKm)}/km</span></li>`).join("");
    try{history.replaceState(null,"","#"+A.id+"-vs-"+B.id)}catch(e){}
    document.title=`${A.n} vs ${B.n}: ${EN?"real cost":"coste real"} | Kilómetro Real`;
  };
  carInput(a,c=>{A=c;draw()});carInput(b,c=>{B=c;draw()});
  root.addEventListener("input",e=>{const id=(e.target.id||"").replace("s-","");if(id in S&&e.target.id.startsWith("s-")){const v=+String(e.target.value).replace(",",".");if(isNaN(v)||v<0){fieldErr(e.target,L.badNum);return}fieldErr(e.target,"");S[id]=v;draw()}});
  $("#swap").addEventListener("click",()=>{[A,B]=[B,A];a.value=A.n;b.value=B.n;draw()});
  root.addEventListener("click",e=>{const s=e.target.closest("[data-swap]");if(s){e.preventDefault();B=BY[s.dataset.swap];b.value=B.n;draw();$("#cres").scrollIntoView({behavior:"smooth",block:"center"})}});
  $("#share").addEventListener("click",async()=>{try{await navigator.clipboard.writeText(location.href);toast(L.copied)}catch(e){$("#sharemsg").textContent=location.href}});
  window.addEventListener("hashchange",()=>{const m=location.hash.slice(1).split("-vs-");if(BY[m[0]]&&BY[m[1]]){A=BY[m[0]];B=BY[m[1]];a.value=A.n;b.value=B.n;draw()}});
  draw();
}

/* ---------- catálogo ---------- */
function initCatalogo(){
  const t=$("#catalogo");if(!t)return;
  const rows=$$("#catalogo tbody tr"),q=$("#f-q"),ty=$("#f-t"),bo=$("#f-b"),pr=$("#f-p"),cnt=$("#f-count");
  const tpl=$("#kr-brands"),fb=$("#f-brand"),nrm=x=>x.normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase();
  const brandBox=s=>{if(!tpl||!fb)return;fb.innerHTML="";const v=nrm(s);if(v.length<2)return;const m=[...tpl.content.querySelectorAll(".bbanner")].find(a=>nrm(a.dataset.b)===v||(v.length>=3&&nrm(a.dataset.b).startsWith(v)));if(m)fb.appendChild(m.cloneNode(true))};
  const apply=()=>{const s=q.value.trim().toLowerCase();brandBox(s);let n=0;rows.forEach(r=>{const ok=(!s||r.dataset.n.includes(s))&&(!ty.value||r.dataset.t===ty.value)&&(!bo.value||r.dataset.body===bo.value)&&(!pr.value||+r.dataset.p<=+pr.value);r.classList.toggle("hide",!ok);if(ok)n++});cnt.textContent=n+" "+L.models};
  [q,ty,bo,pr].forEach(el=>el.addEventListener("input",apply));
  let dir={};
  $$("#catalogo th button").forEach(btn=>btn.addEventListener("click",()=>{const k=btn.dataset.k;dir[k]=!dir[k];const tb=$("#catalogo tbody");rows.sort((x,y)=>{const a=x.dataset[k],b=y.dataset[k];const v=isNaN(+a)?a.localeCompare(b,"es"):(+a)-(+b);return dir[k]?v:-v}).forEach(r=>tb.appendChild(r))}));
  const p=new URLSearchParams(location.search);if(p.get("tipo"))ty.value=p.get("tipo");if(p.get("carroceria"))bo.value=p.get("carroceria");if(p.get("q"))q.value=p.get("q");
  apply();
}

/* ---------- test ---------- */
function initFinder(){
  const f=$("#finder");if(!f)return;
  const ans={budget:30000,km:15000,home:"si",body:"any"};
  $$("#finder .opt").forEach(o=>o.addEventListener("click",()=>{const q=o.dataset.q;$$(`#finder .opt[data-q="${q}"]`).forEach(x=>x.setAttribute("aria-pressed",x===o));ans[q]=isNaN(+o.dataset.v)?o.dataset.v:+o.dataset.v;run()}));
  const run=()=>{
    const S={...D,km:ans.km,home:ans.home==="si"?85:0};
    let list=CARS.filter(c=>c.p<=ans.budget);
    if(ans.body!=="any")list=list.filter(c=>ans.body.split(",").includes(c.body));
    if(ans.home==="no")list=list.filter(c=>c.t!=="phev");
    const top=list.map(c=>({c,k:cost(c,S)})).sort((a,b)=>a.k.perKm-b.k.perKm).slice(0,3);
    $("#fres").innerHTML=top.length?`<h2 style="margin-bottom:16px">${L.top3}</h2><div class="cards">`+top.map(({c,k},i)=>`<a class="card" href="${L.cars}${c.id}/"><div class="meta"><span class="eyebrow">${L.picks[i]}</span></div><h3>${c.n}</h3><div class="meta">${tag(c)}<span class="type t-${c.t}">${L.type[c.t]}</span></div><div class="foot"><span class="price">${eur(c.p)}</span><span class="perkm"><b>${PK(k.perKm)}</b>/km</span></div><p>${eur(k.month)} ${L.withKm(num(S.km))}</p></a>`).join("")+`</div><p style="margin-top:16px"><a class="btn" href="${L.compare}#${top[0].c.id}-vs-${(top[1]||top[0]).c.id}">${L.cmp2}</a></p>`:`<p class="notice bad">${L.none}</p>`;
  };
  run();
}

/* ---------- ficha ---------- */
function initCarCalc(){
  const box=$("#carcalc");if(!box)return;const c=BY[box.dataset.id];if(!c)return;
  const S={...D};
  const draw=()=>{const k=cost(c,S);$("#cc-km").textContent=num(S.km);$("#cc-home")&&($("#cc-home").textContent=S.home+" %");$("#cc-pk").textContent=PK(k.perKm);$("#cc-mo").textContent=eur(k.month);$("#cc-tot").textContent=eur(k.total)};
  box.addEventListener("input",e=>{const id=e.target.id.replace("cc-in-","");if(id in S){S[id]=+e.target.value;draw()}});
  draw();
}

/* ---------- compartir ---------- */
function share(text){
  const url=location.href;
  if(navigator.share){navigator.share({title:document.title,text,url}).catch(()=>{});return}
  window.open("https://wa.me/?text="+encodeURIComponent(text+" "+url),"_blank","noopener");
}
document.addEventListener("click",async e=>{
  const b=e.target.closest(".share");if(b){e.preventDefault();share(b.dataset.text||document.title);return}
  const c=e.target.closest(".copylink");if(c){e.preventDefault();try{await navigator.clipboard.writeText(c.dataset.url||location.href);toast(L.copied)}catch(err){toast(c.dataset.url||location.href)}}
});

/* ---------- recientes ---------- */
function addRecent(a,b){try{let r=JSON.parse(localStorage.getItem("kr_recent")||"[]").filter(x=>x!==a+"|"+b);r.unshift(a+"|"+b);localStorage.setItem("kr_recent",JSON.stringify(r.slice(0,6)))}catch(e){}}
function showRecent(){const box=$("#crecent");if(!box)return;let r=[];try{r=JSON.parse(localStorage.getItem("kr_recent")||"[]")}catch(e){}
  r=r.map(x=>x.split("|")).filter(([a,b])=>BY[a]&&BY[b]);
  box.closest(".panel").classList.toggle("hide",r.length<2);
  box.innerHTML=r.slice(1).map(([a,b])=>`<a href="#${a}-vs-${b}">${BY[a].n} vs ${BY[b].n}</a>`).join("")}

/* ---------- cifras que suben ---------- */
function countUp(root){
  if(matchMedia("(prefers-reduced-motion: reduce)").matches)return;
  root.querySelectorAll("[data-count]").forEach(el=>{const to=+el.dataset.count,d=+el.dataset.dec||0;const t0=performance.now(),from=to*.7;
    const step=t=>{const p=Math.min(1,(t-t0)/450),v=from+(to-from)*(1-Math.pow(1-p,3));el.textContent=d?dec(v,d):num(v);if(p<1)requestAnimationFrame(step)};requestAnimationFrame(step)})}

/* ---------- calculadoras ---------- */
const val=id=>{const e=$("#"+id);return e?(e.type==="checkbox"?e.checked:+String(e.value).replace(",",".")):0};
const out=(cells,say)=>`<div class="out">${cells.map(([v,l,h])=>`<div${h?' class="hl"':""}><b>${v}</b><span>${l}</span></div>`).join("")}</div>${say?`<p class="say">${say}</p>`:""}`;
function guard(root){let ok=true;root.querySelectorAll('input[type=number]').forEach(i=>{const v=+String(i.value).replace(",",".");const bad=i.value===""||isNaN(v)||v<0||(i.max&&v>+i.max);fieldErr(i,bad?L.badNum:"");if(bad)ok=false});return ok}
function initCalcs(){
  const vj=$("#calc-viaje");
  if(vj){datalist();const run=()=>{if(!guard(vj))return;const km=val("v-km")*(val("v-ret")?2:1),u=$("#v-u").value,qty=km*val("v-c")/100,fuel=qty*val("v-p"),tot=fuel+val("v-t"),n=Math.max(1,val("v-n"));
      $("#v-res").innerHTML=out([[e2(tot),L.totalTrip,1],[e2(tot/n),L.perPerson],[dec(qty,1)+" "+(u==="L"?"L":"kWh"),u==="L"?L.fuel:L.elec],[e2(km?fuel/km*100:0),L.per100]],
      `${L.tripSay(num(km),val("v-ret"))} <button type="button" class="btn ghost share" style="padding:6px 12px;margin-left:6px" data-text="${L.tripShare(num(km),e2(tot/n))}">${L.share}</button>`)};
    carInput($("#v-car"),c=>{if(c.t==="ev"){$("#v-u").value="kWh";$("#v-c").value=c.c;$("#v-p").value=D.ph}else{$("#v-u").value="L";$("#v-c").value=c.c;$("#v-p").value={g:D.gas,d:D.die,glp:D.glp}[c.f]}run()});
    $("#v-u").addEventListener("change",()=>{if($("#v-u").value==="kWh"){$("#v-c").value=16;$("#v-p").value=D.ph}else{$("#v-c").value=6;$("#v-p").value=D.gas}run()});
    vj.addEventListener("input",e=>{if(e.target.id!=="v-car")run()});run()}
  const cg=$("#calc-carga");
  if(cg){datalist();const run=()=>{if(!guard(cg))return;const kwh=Math.max(0,val("c-to")-val("c-from"))/100*val("c-bat"),cost=kwh*1.1*val("c-p"),km=kwh/Math.max(1,val("c-cons"))*100;
      $("#c-res").innerHTML=out([[e2(cost),L.thisCharge,1],[dec(kwh,1)+" kWh",L.toBat],[num(km)+" km",L.rangeAdd],[e2(val("c-cons")*val("c-p")*1.1),L.per100]])};
    $("#c-where").addEventListener("change",()=>{$("#c-p").value=$("#c-where").value;run()});
    carInput($("#c-car"),c=>{if(c.bat){$("#c-bat").value=c.bat;$("#c-cons").value=c.c;run()}});
    cg.addEventListener("input",e=>{if(e.target.id!=="c-car")run()});run()}
  const fn=$("#calc-fin");
  if(fn){const run=()=>{if(!guard(fn))return;const P=Math.max(0,val("f-p")-val("f-e")),n=+$("#f-m").value,i=val("f-tin")/100/12,com=P*val("f-com")/100;
      const q=i?P*i/(1-Math.pow(1+i,-n)):P/n;let r=i||.005;for(let k=0;k<60;k++){let f=-(P-com),d=0;for(let t=1;t<=n;t++){f+=q/Math.pow(1+r,t);d-=t*q/Math.pow(1+r,t+1)}r-=f/d}
      const tae=(Math.pow(1+r,12)-1)*100,total=q*n+com+val("f-e");
      const cs=$("#f-cur"),sym=cs?cs.value:"€",M=v=>EN?sym+num(v):num(v)+" "+sym,M2=v=>EN?sym+dec(v,2):dec(v,2)+" "+sym;
      let bal=P,rows="",yi=0,yp=0;for(let t=1;t<=n;t++){const it=bal*i;bal=Math.max(0,bal-(q-it));yi+=it;yp+=q-it;if(t%12===0||t===n){rows+=`<tr><td>${Math.ceil(t/12)}</td><td class="n">${M(yp)}</td><td class="n">${M(yi)}</td><td class="n">${M(bal)}</td></tr>`;yi=0;yp=0}}
      const th=EN?["Year","Principal paid","Interest paid","Balance left"]:["Año","Capital pagado","Intereses","Te queda por pagar"];
      $("#f-res").innerHTML=out([[M2(q),L.monthly,1],[M(total),L.totalPaid],[M(q*n-P+com),L.interest],[dec(tae,2)+" %",L.apr]],L.finSay(M(P),n,M(val("f-p")),M(total-val("f-p"))))
        +`<h3 class="amh">${EN?"Year-by-year breakdown":"Cómo se amortiza año a año"}</h3><div class="tablewrap"><table class="list fit amort"><thead><tr>${th.map((x,j)=>`<th${j?' class="n"':""}>${x}</th>`).join("")}</tr></thead><tbody>${rows}</tbody></table></div>`};
    fn.addEventListener("input",run);fn.addEventListener("change",run);run()}
  const et=$("#calc-eti");
  if(et){const run=()=>{if(!guard(et))return;const t=$("#e-t").value,y=val("e-y"),T=L.lab;let l,txt;
      if(t==="ev"||t==="phev"){l="cero";txt=T.cero}
      else if(t==="hev"||t==="glp"||t==="phev-"){l="eco";txt=T.eco}
      else if(t==="g"){l=y>=2006?"c":y>=2001?"b":"none";txt=y>=2006?T.gC:y>=2001?T.gB:T.none}
      else{l=y>=2016?"c":y===2015?"c?":y>=2006?"b":"none";txt=y>=2016?T.dC:y===2015?T.d15:y>=2006?T.dB:T.none}
      const tagh=l==="none"?'<span class="tag" style="background:#8a94a3">—</span>':l==="c?"?'<span class="tag c">C</span><span class="tag b">B</span>':`<span class="tag ${l}">${{cero:"0",eco:"ECO",c:"C",b:"B"}[l]}</span>`;
      $("#e-res").innerHTML=`<div class="bigtag">${tagh}<p>${txt}</p></div><p class="note" style="margin-top:10px">${L.labNote}</p>`};
    et.addEventListener("input",run);et.addEventListener("change",run);run()}
  const am=$("#calc-amo");
  if(am){datalist();let A=findCar($("#a-ev").value),B=findCar($("#a-ice").value);
    const run=()=>{if(!guard(am))return;if(!A||!B){$("#a-res").innerHTML=`<p class="notice bad">${L.pick2}</p>`;return}
      const y=Math.max(1,val("a-y")),h=val("a-h");const tot=(c,km)=>cost(c,{...D,km,y,home:h}).total;let be=null;
      for(let km=1000;km<=60000;km+=500){if(tot(A,km)<=tot(B,km)){be=km;break}}
      const say=be===1000?L.beFirst(A.n,B.n):be?L.beAt(A.n,num(be),B.n):L.beNever(A.n,B.n);
      $("#a-res").innerHTML=out([10000,15000,20000,30000].map(km=>{const d=tot(B,km)-tot(A,km);return[eur(Math.abs(d)),(d>=0?L.save:L.pay)+" "+L.withKmY(num(km)),d>=0]}),say+` <span class="note">${L.beNote(y,A.n)}</span>`)};
    carInput($("#a-ev"),c=>{A=c;run()});carInput($("#a-ice"),c=>{B=c;run()});
    am.addEventListener("input",e=>{if(e.target.type==="number")run()});run()}
}

/* ---------- buscador de cabecera y 404 ---------- */
function initSearch(){
  $$(".carsearch").forEach(inp=>{datalist();const go=()=>{const br=findBrand(inp.value);if(br&&!document.documentElement.lang.startsWith("en")){location.href="/marcas/"+brandSlug(br)+"/";return}const c=findCar(inp.value);if(c)location.href=L.cars+c.id+"/";else if(inp.value.trim())location.href=L.cars+"?q="+encodeURIComponent(inp.value.trim())};
    inp.addEventListener("change",go);inp.form&&inp.form.addEventListener("submit",e=>{e.preventDefault();go()})});
}

/* ---------- formulario de contacto ---------- */
function initContact(){
  const f=$("#contactform");if(!f)return;const t0=Date.now();const stamp=()=>{if(f.elements.t)f.elements.t.value=Math.round((Date.now()-t0)/1000)};f.addEventListener("submit",stamp,true);f.addEventListener("input",stamp);
  const st=$("#formstatus");
  const check=()=>{let ok=true;
    const n=f.elements.name,m=f.elements.email,t=f.elements.message,c=f.elements.consent;
    if(!n.value.trim()){fieldErr(n,L.req);ok=false}else fieldErr(n,"");
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(m.value.trim())){fieldErr(m,L.mail);ok=false}else fieldErr(m,"");
    if(t.value.trim().length<20){fieldErr(t,L.short);ok=false}else fieldErr(t,"");
    if(!c.checked){fieldErr(c,L.consent);ok=false}else fieldErr(c,"");
    return ok};
  f.addEventListener("blur",e=>{if(e.target.name&&f.dataset.tried)check()},true);
  f.addEventListener("submit",async e=>{e.preventDefault();f.dataset.tried=1;if(!check()){const b=f.querySelector(".bad");b&&b.focus();return}
    const btn=f.querySelector("button[type=submit]");btn.disabled=true;const old=btn.textContent;btn.textContent=L.sending;st.className="notice";st.textContent="";
    try{const r=await fetch(f.action,{method:"POST",body:new FormData(f),headers:{"Accept":"application/json"}});const j=await r.json().catch(()=>({}));
      if(r.ok&&j.ok){st.className="notice ok";st.textContent=L.sent;f.reset()}else{st.className="notice bad";st.textContent=j.error||L.sendErr}}
    catch(err){st.className="notice bad";st.textContent=L.sendErr}
    btn.disabled=false;btn.textContent=old});
  const p=new URLSearchParams(location.search).get("motivo");if(p&&f.elements.topic){f.elements.topic.value=p}
}

/* ---------- interfaz general ---------- */
function initUI(){
  // menú móvil
  const mb=$(".menu-btn"),nav=$("nav.main");
  if(mb&&nav){mb.addEventListener("click",()=>{const o=nav.classList.toggle("open");mb.setAttribute("aria-expanded",o);document.body.classList.toggle("menu-open",o)});
    nav.addEventListener("click",e=>{if(e.target.closest("a")){nav.classList.remove("open");document.body.classList.remove("menu-open");mb.setAttribute("aria-expanded","false")}});
    document.addEventListener("keydown",e=>{if(e.key==="Escape"&&nav.classList.contains("open")){nav.classList.remove("open");document.body.classList.remove("menu-open");mb.setAttribute("aria-expanded","false");mb.focus()}})}
  // tema
  const tb=$(".theme-btn");if(tb){tb.addEventListener("click",()=>{const d=document.documentElement.dataset.theme==="dark"?"light":"dark";document.documentElement.dataset.theme=d;tb.setAttribute("aria-pressed",d==="dark");try{localStorage.setItem("kr_theme",d)}catch(e){}});tb.setAttribute("aria-pressed",document.documentElement.dataset.theme==="dark")}
  // volver arriba y barra de lectura
  const hdr=$("header.top"),top=$(".totop"),bar=$(".readbar"),art=$(".article .body");
  let tick=false;const onScroll=()=>{if(tick)return;tick=true;requestAnimationFrame(()=>{const y=scrollY;top&&top.classList.toggle("show",y>700);hdr&&hdr.classList.toggle("scrolled",y>8);
    if(bar&&art){const r=art.getBoundingClientRect(),h=r.height-innerHeight*.6;bar.style.width=Math.max(0,Math.min(100,(-r.top+innerHeight*.2)/Math.max(1,h)*100))+"%"}tick=false})};
  addEventListener("scroll",onScroll,{passive:true});onScroll();
  top&&top.addEventListener("click",()=>scrollTo({top:0,behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"}));
  // aparición al hacer scroll
  $$(".reveal.cards,.reveal.cgrid,.reveal.rankgrid,.reveal.newslist,.reveal.guides,.reveal.rank").forEach(g=>{g.classList.add("stag");[...g.children].forEach((ch,i)=>ch.style.setProperty("--i",Math.min(i,8)))});
  // imágenes con fundido
  $$("img.thumb,figure img").forEach(im=>{const ok=()=>im.classList.add("ok");if(im.complete&&im.naturalWidth)ok();else{im.addEventListener("load",ok);im.addEventListener("error",ok)}});
  // pulso al cambiar resultados
  if("MutationObserver" in window){const mo=new MutationObserver(ms=>ms.forEach(m=>{const el=m.target.nodeType===1?m.target:m.target.parentElement;const big=el&&el.closest(".cres,.bigfig,.verdict");if(big&&!big.classList.contains("pulse")){big.classList.add("pulse");setTimeout(()=>big.classList.remove("pulse"),460)}}));$$(".cres,.bigfig,.verdict").forEach(e=>mo.observe(e,{childList:true,characterData:true,subtree:true}))}
  const els=$$(".reveal");
  if("IntersectionObserver" in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}}),{rootMargin:"0px 0px -8% 0px",threshold:.05});els.forEach(e=>io.observe(e))}
  else els.forEach(e=>e.classList.add("in"));
}

initUI();initContact();initConsent();
/* ---------- aviso de cookies (se aparta si aparece el aviso oficial de Google) ---------- */
const CK=EN?{t:"Cookies and ads",p:"We use Google AdSense to keep this site free. With your permission, ads are personalised using cookies. If you say no, you will still see ads, just not based on your activity.",a:"Accept",r:"Reject",m:"More information",u:"/en/cookies/",ok:"Saved. You can change it anytime from the footer."}
 :{t:"Cookies y anuncios",p:"Usamos Google AdSense para que la web sea gratis. Con tu permiso, los anuncios se personalizan con cookies. Si dices que no, verás anuncios igualmente, pero no basados en tu actividad.",a:"Aceptar",r:"Rechazar",m:"Más información",u:"/cookies/",ok:"Guardado. Puedes cambiarlo cuando quieras desde el pie de página."};
function getConsent(){try{return localStorage.getItem("kr_consent")}catch(e){return null}}
function setConsent(v){try{localStorage.setItem("kr_consent",v)}catch(e){}
  const ag=window.adsbygoogle=window.adsbygoogle||[];ag.requestNonPersonalizedAds=v==="all"?0:1;ag.pauseAdRequests=0;
  const ok=v==="all"?"granted":"denied";if(window.gtag)gtag("consent","update",{ad_storage:ok,ad_user_data:ok,ad_personalization:ok,analytics_storage:ok})}
const googleCMP=()=>!!(window.googlefc&&googlefc.callbackQueue)||typeof window.__tcfapi==="function";
function showConsent(){if($(".consent"))return;
  const d=document.createElement("div");d.className="consent";d.setAttribute("role","dialog");d.setAttribute("aria-live","polite");d.setAttribute("aria-label",CK.t);
  d.innerHTML=`<div class="consent-in"><div><b>${CK.t}</b><p>${CK.p} <a href="${CK.u}">${CK.m}</a></p></div><div class="consent-btns"><button type="button" class="cbtn" data-c="npa">${CK.r}</button><button type="button" class="cbtn" data-c="all">${CK.a}</button></div></div>`;
  document.body.appendChild(d);requestAnimationFrame(()=>d.classList.add("show"));
  d.addEventListener("click",e=>{const b=e.target.closest("[data-c]");if(!b)return;setConsent(b.dataset.c);d.classList.remove("show");setTimeout(()=>d.remove(),260);toast(CK.ok)})}
function initConsent(){if(getConsent())return;setTimeout(()=>{if(!googleCMP()&&!getConsent())showConsent()},1200)}
document.addEventListener("click",e=>{const b=e.target.closest(".cookie-prefs");if(!b)return;e.preventDefault();
  if(window.googlefc&&googlefc.callbackQueue){googlefc.callbackQueue.push(googlefc.showRevocationMessage)}else showConsent()});
fetch("/assets/data/coches.json").then(r=>{if(!r.ok)throw 0;return r.json()}).then(d=>{
  CARS=d;BY=Object.fromEntries(d.map(c=>[c.id,c]));BYNAME=Object.fromEntries(d.map(c=>[c.n.toLowerCase(),c]));
  document.body.classList.add("loaded");
  initHomeDuel();initMiCoche();initComparador();initCatalogo();initFinder();initCarCalc();initCalcs();initSearch();
}).catch(()=>{document.body.classList.add("loaded");$$(".needs-js").forEach(e=>e.insertAdjacentHTML("beforeend",`<p class="notice bad">${L.dataErr}</p>`))});
})();
/* ---------- copiar texto (informes) ---------- */
document.addEventListener("click",e=>{const b=e.target.closest("[data-copy]");if(!b)return;const el=document.querySelector(b.dataset.copy);if(!el)return;const t=el.innerText.trim();const done=()=>{const o=b.textContent;b.textContent="Copiado";setTimeout(()=>b.textContent=o,1600)};if(navigator.clipboard)navigator.clipboard.writeText(t).then(done,()=>{});else{const r=document.createRange();r.selectNodeContents(el);const sel=getSelection();sel.removeAllRanges();sel.addRange(r);try{document.execCommand("copy");done()}catch(x){}}});
