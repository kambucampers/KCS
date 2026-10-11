import pw from '/opt/npm-tools/node_modules/playwright/index.js';
const url='file://'+process.argv[2], outdir=process.argv[3];
const browser=await pw.chromium.launch();const res={};
for (const [w,h] of [[1440,1000],[768,1024],[390,844]]) {
  const page=await browser.newPage({viewport:{width:w,height:h}});
  const errors=[];page.on('console',m=>{if(m.type()==='error')errors.push(m.text().slice(0,160))});page.on('pageerror',e=>errors.push('PAGEERR '+e.message));
  await page.goto(url,{waitUntil:'load',timeout:90000});
  const H=await page.evaluate(()=>document.body.scrollHeight);
  for(let y=0;y<H;y+=1500){await page.evaluate(y=>window.scrollTo(0,y),y);await page.waitForTimeout(25);}
  await page.evaluate(()=>document.getElementById('kcm-map').scrollIntoView());await page.waitForTimeout(3000);
  const r=await page.evaluate(()=>{const d=document.documentElement;const imgs=[...document.querySelectorAll('.kcm img')];
    const ids=[...document.querySelectorAll('section[id$="-campsites"]')].map(s=>s.id);
    return {overflow:d.scrollWidth-d.clientWidth,h1:document.querySelectorAll('.kcm h1').length,h2:document.querySelectorAll('.kcm h2').length,h3:document.querySelectorAll('.kcm h3').length,
      broken:imgs.filter(i=>!(i.complete&&i.naturalWidth>0)).length,regionIds:ids.length,firstIds:ids.slice(0,3),mapReady:!!document.querySelector('#kcm-map[data-ready]'),
      paths:document.querySelectorAll('#kcm-map path.leaflet-interactive').length,count:document.getElementById('kcm-count').textContent,calc:document.getElementById('kcm-c-total').textContent,
      cards:document.querySelectorAll('.kcm__site').length,height:document.body.scrollHeight}});
  const it={};
  await page.selectOption('#kcm-region','masai-mara-campsites');await page.waitForTimeout(600);it.mara=await page.textContent('#kcm-count');
  await page.click('#kcm-reset');await page.selectOption('#kcm-veh','2wd');await page.waitForTimeout(300);it.twowd=await page.textContent('#kcm-count');
  await page.click('#kcm-reset');await page.check('#kcm-f-inactive');await page.waitForTimeout(300);it.all=await page.textContent('#kcm-count');
  await page.click('#kcm-reset');await page.fill('#kcm-q','pejeta');await page.waitForTimeout(600);it.search=await page.textContent('#kcm-count');
  await page.click('#kcm-results .kcm__res');await page.waitForTimeout(1200);it.popup=(await page.evaluate(()=>(document.querySelector('.leaflet-popup-content')||{}).textContent||'')).slice(0,140);
  await page.click('#kcm-reset');
  await page.evaluate(()=>document.getElementById('kcm-calc').scrollIntoView());
  const opts=await page.$$eval('#kcm-c-site option',o=>o.map(x=>[x.value,x.textContent]));
  const amb=opts.find(o=>o[1].startsWith('Amboseli'));await page.selectOption('#kcm-c-site',amb[0]);await page.fill('#kcm-c-n','1');await page.fill('#kcm-c-ad','1');await page.fill('#kcm-c-v','0');await page.waitForTimeout(200);
  it.calcAmb1=await page.textContent('#kcm-c-total');
  const sp=opts.find(o=>o[1].startsWith('Chui'));await page.selectOption('#kcm-c-site',sp[0]);await page.fill('#kcm-c-n','3');await page.fill('#kcm-c-ad','2');await page.fill('#kcm-c-v','1');await page.waitForTimeout(200);
  it.calcChui=await page.textContent('#kcm-c-total');it.calcRows=await page.$$eval('#kcm-c-rows tr',r=>r.map(x=>x.textContent));
  await page.evaluate(()=>document.getElementById('gallery').scrollIntoView());await page.click('.kcm__arrow[data-dir="1"]');await page.waitForTimeout(900);it.gal=await page.textContent('.kcm__gal-count');
  res[w]={...r,it,errors:errors.slice(0,6)};
  await page.evaluate(()=>window.scrollTo(0,0));
  for (const id of ['answer','map','types','costs','regions','masai-mara-campsites','mount-kenya-campsites','samburu-northern-kenya-campsites','access','seasons','safety','rules','gear','choose','book','checked']) {
    const el=await page.$('#'+id); if(el) await el.screenshot({path:`${outdir}/${w}-${id}.png`});
  }
  const hero=await page.$('.kcm__hero');await hero.screenshot({path:`${outdir}/${w}-hero.png`});
  await page.close();
}
console.log(JSON.stringify(res,null,1));await browser.close();
