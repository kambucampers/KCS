import pw from '/opt/node-tools/node_modules/playwright/index.js';
const { chromium } = pw;
import path from 'node:path';
import fs from 'node:fs';
const here = path.dirname(new URL(import.meta.url).pathname);
const url = 'file://' + path.join(here, 'render', 'index.html');
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] }).catch(async () => chromium.launch());
let bad = 0;
for (const [w, h, tag] of [[1440, 1000, 'desktop'], [390, 844, 'mobile']]) {
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  const errors = [];
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', e => errors.push(String(e)));
  await page.goto(url, { waitUntil: 'load' });
  // scroll to defeat lazy loading
  await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } window.scrollTo(0, 0); });
  await page.waitForTimeout(600);
  const r = await page.evaluate(() => {
    const imgs = [...document.images];
    const broken = imgs.filter(i => !i.complete || i.naturalWidth === 0).map(i => i.getAttribute('src'));
    const overflow = document.documentElement.scrollWidth > document.documentElement.clientWidth + 1;
    const h1 = document.querySelectorAll('h1').length;
    const heads = [...document.querySelectorAll('h1,h2,h3,h4')].map(h => +h.tagName[1]);
    let order = true; for (let i = 1; i < heads.length; i++) if (heads[i] > heads[i - 1] + 1) order = false;
    // clipped text: elements whose scrollWidth exceeds clientWidth with overflow hidden
    const clipped = [...document.querySelectorAll('.kti h1,.kti h2,.kti h3,.kti p,.kti li,.kti td,.kti th')].filter(e => e.scrollWidth > e.clientWidth + 2 && getComputedStyle(e).overflowX !== 'visible').length;
    const wide = [...document.querySelectorAll('.kti *')].filter(e => e.getBoundingClientRect().right > document.documentElement.clientWidth + 1 && getComputedStyle(e).position !== 'fixed').map(e => e.className).slice(0, 5);
    return { broken, overflow, h1, order, clipped, wide, height: document.body.scrollHeight };
  });
  const fontsBlocked = errors.filter(e => /fonts\.g|ERR_/.test(e));
  const real = errors.filter(e => !/fonts\.g|ERR_/.test(e));
  console.log(tag, JSON.stringify({ ...r, consoleErrors: real.length, fontErrors: fontsBlocked.length }));
  if (r.broken.length || r.overflow || r.h1 !== 1 || !r.order || real.length) bad++;
  fs.mkdirSync(path.join(here, 'render', 'shots'), { recursive: true });
  await page.screenshot({ path: path.join(here, 'render', 'shots', `full-${tag}.png`), fullPage: true });
  // per-section crops
  const ids = await page.$$eval('section[id], header.kti__hero, section.kti__final, section.kti__rel, div.kti__ctastrip', els => els.map((e, i) => e.id || e.className.split(' ')[0] + i));
  const els = await page.$$('section[id], header.kti__hero, section.kti__final, section.kti__rel, div.kti__ctastrip');
  for (let i = 0; i < els.length; i++) {
    await els[i].scrollIntoViewIfNeeded();
    await els[i].screenshot({ path: path.join(here, 'render', 'shots', `${tag}-${String(i).padStart(2, '0')}-${ids[i]}.png`) }).catch(e => console.log('crop fail', ids[i], e.message));
  }
  await page.close();
}
await browser.close();
process.exit(bad ? 1 : 0);
