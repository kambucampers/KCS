import pw from '/opt/npm-tools/node_modules/playwright/index.js';
const [,, file, out]=process.argv;
const b=await pw.chromium.launch();
for (const w of [1440,390]) {
const p=await b.newPage({viewport:{width:w,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text().slice(0,120))});
await p.goto('file://'+file,{waitUntil:'load',timeout:90000});
await p.evaluate(()=>{const n=document.querySelector('.kcm__snav');if(n)n.style.position='static';});
const r={};
const pin=await p.$('#masai-mara-campsites .kcm__mpin[data-sid="site-oloololo-public-campsite"]');
await pin.scrollIntoViewIfNeeded();await pin.click();await p.waitForTimeout(300);
r.popup=(await p.textContent('#masai-mara-campsites .kcm__mpop')).slice(0,260);
const fig=await p.$('#masai-mara-campsites .kcm__rmap');await fig.screenshot({path:`${out}/${w}-pin-popup.png`});
await p.click('#masai-mara-campsites .kcm__mpop-more');await p.waitForTimeout(800);
r.hash=await p.evaluate(()=>location.hash);r.cardInView=await p.evaluate(()=>{const c=document.getElementById('site-oloololo-public-campsite').getBoundingClientRect();return c.top>-5&&c.top<400});
// keyboard on a region pin
await p.focus('#mount-kenya-campsites .kcm__mpin');await p.keyboard.press('Enter');await p.waitForTimeout(200);
r.kbdPopup=await p.evaluate(()=>{const m=document.querySelector('#mount-kenya-campsites .kcm__mpop');return !!m&&!m.hidden&&document.activeElement.classList.contains('kcm__mpop-more')});
await p.keyboard.press('Escape');r.escClosed=await p.evaluate(()=>document.querySelector('.kcm__mpop').hidden);
// national map pin
const np=await p.$('#types .kcm__mpin[data-sid="site-eliye-springs-tents"]');await np.scrollIntoViewIfNeeded();await np.click();await p.waitForTimeout(200);r.natPopup=(await p.textContent('#types .kcm__mpop')).slice(0,80);
// leaflet
await p.evaluate(()=>document.getElementById('kcm-map').scrollIntoView());await p.waitForTimeout(3500);
r.wm=await p.evaluate(()=>!!document.querySelector('#kcm-map .kcm__mapwm')&&!!document.querySelector('#kcm-map .kcm__mapwm-t'));
await p.fill('#kcm-q','naiburta');await p.waitForTimeout(500);await p.click('#kcm-results .kcm__res');await p.waitForTimeout(1300);
r.leaflet=(await p.evaluate(()=>(document.querySelector('.leaflet-popup-content')||{}).textContent||'')).slice(0,300);
const mp=await p.$('#kcm-map');await mp.screenshot({path:`${out}/${w}-leaflet-popup.png`});
// review block present
r.revBlocks=await p.evaluate(()=>document.querySelectorAll('.kcm__rev').length);r.pc=await p.evaluate(()=>document.querySelectorAll('.kcm__pc').length);
r.conf=await p.evaluate(()=>document.querySelectorAll('.kcm__conf').length);
r.overflow=await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
console.log(w,JSON.stringify(r,null,1),errs);
const card=await p.$('#site-naiburta-public-campsite');await card.screenshot({path:`${out}/${w}-card-reviews.png`});
await p.close();}
await b.close();
