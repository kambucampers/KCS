#!/usr/bin/env python3
"""Build Nairobi.guide as a static site into ./dist.

Usage:  python3 build.py            (writes dist/)
        python3 -m http.server -d dist 8000   to preview
"""
from __future__ import annotations

import html
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from data import AREAS, EXPERIENCES, GUIDES, LISTINGS, SECTIONS, SITE  # noqa: E402

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

AREA_BY_SLUG = {a["slug"]: a for a in AREAS}
e = html.escape


# --------------------------------------------------------------------------
# Shared chrome
# --------------------------------------------------------------------------
CSS = """
:root{
  --bg:#f7f3ea;--surface:#fffdf8;--ink:#1d1a16;--muted:#6b6358;--line:#e4dccd;
  --brand:#8a3b12;--brand-ink:#fff;
  --ochre:#c2651b;--forest:#2f5d3a;--savanna:#9a7b1c;--dusk:#4b3a6e;
  --radius:14px;--max:1180px;
}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){
  --bg:#15130f;--surface:#1f1b16;--ink:#f1ebe0;--muted:#a79d8f;--line:#332d25;
  --brand:#e08a4d;--brand-ink:#1a120c;}}
:root[data-theme=dark]{
  --bg:#15130f;--surface:#1f1b16;--ink:#f1ebe0;--muted:#a79d8f;--line:#332d25;
  --brand:#e08a4d;--brand-ink:#1a120c;}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.55 "Inter",system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:inherit;text-decoration:none}
a:hover{text-decoration:underline}
img{max-width:100%;display:block}
.wrap{max-width:var(--max);margin:0 auto;padding:0 16px}
h1,h2,h3{font-family:"Fraunces",Georgia,serif;font-weight:600;line-height:1.15;margin:0 0 .4em;letter-spacing:-.01em}
h1{font-size:clamp(2rem,5vw,3.4rem)}
h2{font-size:clamp(1.5rem,3vw,2.1rem)}
h3{font-size:1.2rem}
p{margin:0 0 1em}
.muted{color:var(--muted)}
.eyebrow{font-size:.78rem;text-transform:uppercase;letter-spacing:.12em;color:var(--brand);font-weight:600;margin-bottom:.5rem}

/* header */
.site-head{border-bottom:1px solid var(--line);background:var(--surface);position:sticky;top:0;z-index:10}
.site-head .wrap{display:flex;align-items:center;gap:1.25rem;min-height:60px;flex-wrap:wrap}
.logo{font-family:"Fraunces",Georgia,serif;font-size:1.3rem;font-weight:700}
.logo span{color:var(--brand)}
nav.main{display:flex;gap:1rem;flex-wrap:wrap;font-size:.95rem}
nav.main a{padding:.35rem 0;border-bottom:2px solid transparent}
nav.main a[aria-current]{border-color:var(--brand)}
.head-right{margin-left:auto;display:flex;gap:1rem;font-size:.9rem}
@media(max-width:720px){.head-right{display:none}nav.main{width:100%;overflow-x:auto;padding-bottom:.5rem}}

/* hero */
.hero{padding:3.5rem 0 2.5rem;display:grid;gap:2rem;grid-template-columns:1.1fr .9fr;align-items:center}
.hero h1 em{font-style:italic;color:var(--brand)}
.hero .lede{font-size:1.15rem;max-width:36rem}
.hero-art{aspect-ratio:4/3;border-radius:var(--radius);overflow:hidden;box-shadow:0 20px 50px -25px rgba(0,0,0,.5)}
.hero-art svg{width:100%;height:100%;display:block}
@media(max-width:860px){.hero{grid-template-columns:1fr;padding-top:2rem}}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem}
.chip{border:1px solid var(--line);background:var(--surface);border-radius:999px;padding:.35rem .85rem;font-size:.88rem}
.chip:hover{border-color:var(--brand);text-decoration:none}
.search{display:flex;gap:.5rem;margin-top:1.5rem;max-width:34rem}
.search input{flex:1;padding:.8rem 1rem;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink);font:inherit}
.btn{background:var(--brand);color:var(--brand-ink);border:0;border-radius:10px;padding:.8rem 1.2rem;font:inherit;font-weight:600;cursor:pointer}
.btn:hover{text-decoration:none;filter:brightness(1.08)}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line)}

/* sections */
section.band{padding:2.75rem 0;border-top:1px solid var(--line)}
.band-head{display:flex;justify-content:space-between;align-items:end;gap:1rem;margin-bottom:1.25rem;flex-wrap:wrap}
.band-head p{margin:0;max-width:40rem}
.more{font-weight:600;color:var(--brand);white-space:nowrap}
.grid{display:grid;gap:1rem;grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}
.grid.two{grid-template-columns:repeat(auto-fill,minmax(320px,1fr))}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;display:flex;flex-direction:column}
.card:hover{text-decoration:none;border-color:var(--brand)}
.card .art{height:140px;display:flex;align-items:flex-end;padding:1rem;color:#fff;font-family:"Fraunces",Georgia,serif;font-size:1.4rem;font-weight:600;text-shadow:0 1px 6px rgba(0,0,0,.45)}
.art.ochre{background:linear-gradient(160deg,#e0862f,#8a3b12)}
.art.forest{background:linear-gradient(160deg,#5c8f63,#1f3f28)}
.art.savanna{background:linear-gradient(160deg,#d9b24a,#7a5f10)}
.art.dusk{background:linear-gradient(160deg,#7c62a8,#2e2247)}
.art.area{background:linear-gradient(160deg,#7f8d78,#3a4a38)}
.card .body{padding:1rem 1.1rem 1.2rem}
.card .body h3{margin-bottom:.3rem}
.card .body p{margin:0;color:var(--muted);font-size:.95rem}
.meta{display:flex;gap:.5rem;flex-wrap:wrap;font-size:.8rem;color:var(--muted);margin-bottom:.4rem}
.meta b{color:var(--ink);font-weight:600}
.price{letter-spacing:.05em}
.linklist{list-style:none;margin:0;padding:0;display:grid;gap:.4rem}
.linklist a{display:flex;justify-content:space-between;gap:1rem;padding:.65rem .9rem;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
.linklist a small{color:var(--muted)}
.linklist a:hover{border-color:var(--brand);text-decoration:none}
.split{display:grid;gap:2rem;grid-template-columns:1fr 1fr}
@media(max-width:860px){.split{grid-template-columns:1fr}}

/* page layouts */
.page-head{padding:2.5rem 0 1.5rem}
.page-head .lede{font-size:1.1rem;max-width:44rem}
.crumbs{font-size:.85rem;color:var(--muted);margin-bottom:.75rem}
.crumbs a:hover{color:var(--brand)}
.filters{display:flex;gap:.5rem;flex-wrap:wrap;margin:1rem 0 1.5rem}
.detail{display:grid;gap:2.5rem;grid-template-columns:minmax(0,1fr) 300px;padding-bottom:3rem}
@media(max-width:860px){.detail{grid-template-columns:1fr}}
.detail article p{font-size:1.05rem}
aside .box{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:1.1rem 1.2rem;margin-bottom:1rem}
aside .box h3{font-size:1rem;margin-bottom:.6rem}
aside .box ul{margin:0;padding-left:1.1rem;color:var(--muted);font-size:.95rem}
aside .box li{margin-bottom:.35rem}
.tags{display:flex;gap:.4rem;flex-wrap:wrap}
.tag{font-size:.78rem;border:1px solid var(--line);border-radius:6px;padding:.15rem .5rem;color:var(--muted)}
.guide-body h2{margin-top:2rem;font-size:1.45rem}
.guide-body{max-width:46rem;padding-bottom:3rem}
.notice{background:var(--surface);border:1px dashed var(--line);border-radius:10px;padding:.9rem 1rem;font-size:.9rem;color:var(--muted)}

/* footer */
footer{border-top:1px solid var(--line);background:var(--surface);padding:2.5rem 0 2rem;margin-top:2rem;font-size:.9rem}
.foot-grid{display:grid;gap:1.5rem;grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}
footer h4{margin:0 0 .6rem;font-size:.85rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
footer ul{list-style:none;margin:0;padding:0;display:grid;gap:.35rem}
.foot-bottom{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;margin-top:2rem;padding-top:1.25rem;border-top:1px solid var(--line);color:var(--muted)}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500'
         '&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')


def nav_links(current: str = "") -> str:
    items = [("eat", "Eat"), ("stay", "Stay"), ("visit", "Visit"), ("play", "Play"),
             ("areas", "Areas"), ("guides", "Guides"), ("experiences", "Experiences")]
    out = []
    for slug, label in items:
        cur = ' aria-current="page"' if slug == current else ""
        out.append(f'<a href="/{slug}/"{cur}>{label}</a>')
    return "".join(out)


def layout(title: str, body: str, *, current: str = "", description: str = "", path: str = "/") -> str:
    desc = description or SITE["description"]
    full = f"{title} · {SITE['name']}" if title != SITE["name"] else f"{SITE['name']} — {SITE['tagline']}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="https://{SITE['domain']}{path}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://{SITE['domain']}{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="site-head"><div class="wrap">
  <a class="logo" href="/">Nairobi<span>.guide</span></a>
  <nav class="main" aria-label="Main">{nav_links(current)}</nav>
  <div class="head-right"><a href="/guides/getting-around-nairobi/">Plan</a><a href="/about/">About</a></div>
</div></header>
<main>{body}</main>
<footer><div class="wrap">
  <div class="foot-grid">
    <div><h4>Eat</h4><ul>{footer_types('eat')}</ul></div>
    <div><h4>Stay</h4><ul>{footer_types('stay')}</ul></div>
    <div><h4>Visit</h4><ul>{footer_types('visit')}</ul></div>
    <div><h4>Play</h4><ul>{footer_types('play')}</ul></div>
    <div><h4>Areas</h4><ul>{''.join(f'<li><a href="/areas/{a["slug"]}/">{e(a["name"])}</a></li>' for a in AREAS[:6])}</ul></div>
    <div><h4>Guides</h4><ul>{''.join(f'<li><a href="/guides/{g["slug"]}/">{e(g["title"])}</a></li>' for g in GUIDES)}</ul></div>
  </div>
  <div class="foot-bottom">
    <span>© 2026 {SITE['name']} · Written in Nairobi</span>
    <span><a href="/about/">About</a> · <a href="/about/#how-we-choose">How we choose</a> · <a href="/about/#contact">Contact</a></span>
  </div>
</div></footer>
</body></html>"""


def footer_types(section: str) -> str:
    s = SECTIONS[section]
    items = [f'<li><a href="/{section}/">All {s["title"].lower()}</a></li>']
    items += [f'<li><a href="/{section}/{t}/">{e(label)}</a></li>' for t, label in s["types"].items()]
    return "".join(items)


# --------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------
def price_marks(n: int) -> str:
    return "$" * n


def listing_card(l: dict) -> str:
    sec = SECTIONS[l["section"]]
    area = AREA_BY_SLUG[l["area"]]["name"]
    return f"""<a class="card" href="/{l['section']}/{l['type']}/{l['slug']}/">
  <div class="art {sec['tone']}">{e(l['name'])}</div>
  <div class="body">
    <div class="meta"><b>{e(sec['types'][l['type']])}</b> · {e(area)} · <span class="price">{price_marks(l['price'])}</span></div>
    <p>{e(l['summary'])}</p>
  </div></a>"""


def area_card(a: dict) -> str:
    return f"""<a class="card" href="/areas/{a['slug']}/">
  <div class="art area">{e(a['name'])}</div>
  <div class="body"><p>{e(a['vibe'])}</p></div></a>"""


def guide_row(g: dict) -> str:
    return f'<li><a href="/guides/{g["slug"]}/"><span>{e(g["title"])}</span><small>Guide</small></a></li>'


def crumbs(*parts: tuple[str, str]) -> str:
    out = ['<a href="/">Home</a>']
    for label, href in parts:
        out.append(f'<a href="{href}">{e(label)}</a>' if href else e(label))
    return '<div class="crumbs">' + " › ".join(out) + "</div>"


HERO_SVG = """<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stylised Nairobi skyline with giraffes on the plains">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4b36a"/><stop offset=".6" stop-color="#d9694a"/><stop offset="1" stop-color="#6b2a44"/></linearGradient>
<linearGradient id="grass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b78a3a"/><stop offset="1" stop-color="#5e4616"/></linearGradient></defs>
<rect width="800" height="600" fill="url(#sky)"/>
<circle cx="600" cy="190" r="70" fill="#ffd9a0" opacity=".9"/>
<g fill="#3a1f33" opacity=".85">
<rect x="80" y="300" width="40" height="110"/><rect x="130" y="260" width="30" height="150"/><rect x="170" y="320" width="60" height="90"/>
<rect x="245" y="230" width="36" height="180"/><rect x="290" y="290" width="50" height="120"/>
<path d="M360 410 V250 a25 25 0 0 1 50 0 V410Z"/><path d="M420 410 L440 290 L460 410Z"/>
<rect x="475" y="300" width="45" height="110"/><rect x="530" y="270" width="28" height="140"/><rect x="570" y="320" width="70" height="90"/>
<rect x="650" y="290" width="40" height="120"/><rect x="700" y="330" width="60" height="80"/></g>
<rect y="400" width="800" height="200" fill="url(#grass)"/>
<g fill="#2a1a10">
<path d="M150 540 l0 -70 l10 -60 l6 0 l-4 60 l20 0 l-4 -60 l6 0 l10 60 l0 70 l-8 0 l0 -60 l-28 0 l0 60z"/>
<path d="M176 410 l4 -40 l6 -4 l6 4 l-2 40z"/>
<path d="M620 560 l0 -90 l12 -80 l8 0 l-5 80 l26 0 l-5 -80 l8 0 l12 80 l0 90 l-10 0 l0 -78 l-36 0 l0 78z"/>
<path d="M654 390 l5 -52 l8 -5 l8 5 l-3 52z"/></g>
<g fill="#2a1a10" opacity=".8"><ellipse cx="420" cy="470" rx="90" ry="6"/><path d="M380 470 l0 -30 l80 0 l0 30"/><path d="M400 440 q20 -40 50 -30 q10 20 -10 30"/></g>
</svg>"""


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def page_home() -> str:
    popular = [("Nyama choma", "/eat/nyama-choma/"), ("Nairobi National Park", "/visit/wildlife/nairobi-national-park/"),
               ("Westlands nightlife", "/areas/westlands/"), ("Karura Forest", "/visit/nature/karura-forest/"),
               ("Getting around", "/guides/getting-around-nairobi/"), ("Day trips", "/guides/day-trips-from-nairobi/")]
    sections = "".join(
        f'<a class="card" href="/{k}/"><div class="art {s["tone"]}">{s["title"]}</div>'
        f'<div class="body"><p>{e(s["blurb"])}</p></div></a>' for k, s in SECTIONS.items())
    picks = [next(l for l in LISTINGS if l["slug"] == s) for s in
             ("nairobi-national-park", "mama-oliech", "fairmont-the-norfolk", "karura-forest")]
    essentials = "".join(guide_row(g) for g in GUIDES[:5])
    exp = "".join(
        f'<a class="card" href="/experiences/#{x["slug"]}"><div class="body">'
        f'<div class="meta"><b>{e(x["category"])}</b> · {e(x["duration"])}</div><h3>{e(x["name"])}</h3>'
        f'<p>{e(x["summary"])}</p></div></a>' for x in EXPERIENCES[:4])
    body = f"""
<div class="wrap">
<div class="hero">
  <div>
    <div class="eyebrow">Restaurants · Hotels · Wildlife · Nights out</div>
    <h1>Know <em>Nairobi</em> like you live here</h1>
    <p class="lede">An independent guide to the city: where to eat, sleep, explore and go out, neighbourhood by neighbourhood. No paid placements, no star ratings copied from elsewhere, just plain advice.</p>
    <form class="search" action="/search/" method="get" role="search">
      <input type="search" name="q" placeholder="Search Nairobi.guide" aria-label="Search">
      <button class="btn" type="submit">Search</button>
    </form>
    <div class="chips">{''.join(f'<a class="chip" href="{h}">{e(t)}</a>' for t, h in popular)}</div>
  </div>
  <div class="hero-art">{HERO_SVG}</div>
</div>
</div>

<section class="band"><div class="wrap">
  <div class="band-head"><div><div class="eyebrow">Start here</div><h2>Browse by what you want to do</h2></div></div>
  <div class="grid">{sections}</div>
</div></section>

<section class="band"><div class="wrap split">
  <div>
    <div class="eyebrow">Visiting Nairobi</div>
    <h2>Planning the trip</h2>
    <p class="muted">The practical bits, from people who live here.</p>
    <ul class="linklist">{essentials}</ul>
  </div>
  <div>
    <div class="eyebrow">In the city</div>
    <h2>Out in Nairobi</h2>
    <p class="muted">Tonight, this weekend and Sunday lunch.</p>
    <ul class="linklist">
      <li><a href="/play/bars/"><span>Bars &amp; lounges tonight</span><small>Play</small></a></li>
      <li><a href="/play/live-music/"><span>Live music</span><small>Play</small></a></li>
      <li><a href="/eat/brunch-cafes/"><span>Weekend brunch</span><small>Eat</small></a></li>
      <li><a href="/play/arts/"><span>Theatre &amp; arts</span><small>Play</small></a></li>
      <li><a href="/visit/"><span>Things to see</span><small>Visit</small></a></li>
    </ul>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="band-head"><div><div class="eyebrow">Discover by neighbourhood</div><h2>Where in Nairobi?</h2></div><a class="more" href="/areas/">All areas →</a></div>
  <div class="grid">{''.join(area_card(a) for a in AREAS[:4])}</div>
</div></section>

<section class="band"><div class="wrap">
  <div class="band-head"><div><div class="eyebrow">The Nairobi.guide edit</div><h2>Four places we'd send a friend first</h2>
  <p class="muted">Chosen by us, not by rating or review count. <a href="/about/#how-we-choose">How we choose</a>.</p></div></div>
  <div class="grid">{''.join(listing_card(l) for l in picks)}</div>
</div></section>

<section class="band"><div class="wrap">
  <div class="band-head"><div><div class="eyebrow">Experiences</div><h2>Days out</h2></div><a class="more" href="/experiences/">All experiences →</a></div>
  <div class="grid">{exp}</div>
</div></section>

<section class="band"><div class="wrap">
  <h2>How this guide works</h2>
  <ul class="linklist">
    <li><a href="/about/#how-we-choose"><span>Every place is here because we'd go back, not because it paid</span><small>Editorial</small></a></li>
    <li><a href="/about/#ratings"><span>We don't republish third-party ratings; check live reviews and hours on the venue's own channels</span><small>Ratings</small></a></li>
    <li><a href="/about/#contact"><span>Spotted a change? Tell us and we'll fix it</span><small>Contact</small></a></li>
  </ul>
</div></section>
"""
    return layout(SITE["name"], body, current="", path="/")


def page_section(key: str) -> str:
    s = SECTIONS[key]
    items = [l for l in LISTINGS if l["section"] == key]
    filters = "".join(f'<a class="chip" href="/{key}/{t}/">{e(label)}</a>' for t, label in s["types"].items())
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs((s['title'], ''))}<h1>{e(s['headline'])}</h1><p class="lede">{e(s['intro'])}</p>
  <div class="filters"><a class="chip" href="/{key}/" aria-current="page">All</a>{filters}</div></div>
  <div class="grid">{''.join(listing_card(l) for l in items)}</div>
  <section class="band"><div class="band-head"><h2>By neighbourhood</h2></div>
  <div class="grid">{''.join(area_card(a) for a in AREAS)}</div></section>
</div>"""
    return layout(s["headline"], body, current=key, description=s["intro"], path=f"/{key}/")


def page_type(key: str, t: str) -> str:
    s = SECTIONS[key]
    label = s["types"][t]
    items = [l for l in LISTINGS if l["section"] == key and l["type"] == t]
    filters = "".join(
        f'<a class="chip" href="/{key}/{tt}/"{" aria-current=page" if tt == t else ""}>{e(ll)}</a>'
        for tt, ll in s["types"].items())
    title = f"{label} in Nairobi"
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs((s['title'], f'/{key}/'), (label, ''))}<h1>{e(title)}</h1>
  <p class="lede muted">{len(items)} place{'s' if len(items) != 1 else ''} we'd recommend.</p>
  <div class="filters"><a class="chip" href="/{key}/">All</a>{filters}</div></div>
  <div class="grid">{''.join(listing_card(l) for l in items) or '<p class="notice">We are still writing this section.</p>'}</div>
</div>"""
    return layout(title, body, current=key, path=f"/{key}/{t}/")


def page_listing(l: dict) -> str:
    s = SECTIONS[l["section"]]
    area = AREA_BY_SLUG[l["area"]]
    nearby = [x for x in LISTINGS if x["area"] == l["area"] and x["slug"] != l["slug"]][:5]
    tips = "".join(f"<li>{e(t)}</li>" for t in l["tips"])
    path = f"/{l['section']}/{l['type']}/{l['slug']}/"
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs((s['title'], f'/{l["section"]}/'), (s['types'][l['type']], f'/{l["section"]}/{l["type"]}/'), (l['name'], ''))}
    <div class="meta"><b>{e(s['types'][l['type']])}</b> · <a href="/areas/{area['slug']}/">{e(area['name'])}</a> · <span class="price" title="Price band">{price_marks(l['price'])}</span></div>
    <h1>{e(l['name'])}</h1><p class="lede">{e(l['summary'])}</p></div>
  <div class="detail">
    <article>
      <div class="art {s['tone']}" style="height:220px;border-radius:var(--radius);margin-bottom:1.5rem">{e(l['name'])}</div>
      <p>{e(l['body'])}</p>
      <h2 style="font-size:1.3rem;margin-top:2rem">Good to know</h2>
      <ul>{tips}</ul>
      <p class="notice">Hours, prices and bookings change. Check the venue's own website or socials before you go, and tell us if something here is out of date.</p>
      <div class="tags">{''.join(f'<span class="tag">{e(t)}</span>' for t in l['tags'])}</div>
    </article>
    <aside>
      <div class="box"><h3>Neighbourhood</h3><p><a href="/areas/{area['slug']}/"><b>{e(area['name'])}</b></a><br><span class="muted">{e(area['vibe'])}</span></p></div>
      <div class="box"><h3>Also in {e(area['name'])}</h3><ul>{''.join(f'<li><a href="/{x["section"]}/{x["type"]}/{x["slug"]}/">{e(x["name"])}</a></li>' for x in nearby) or '<li>More coming soon</li>'}</ul></div>
      <div class="box"><h3>Price bands</h3><ul><li>$ budget</li><li>$$ mid-range</li><li>$$$ upmarket</li><li>$$$$ splurge</li></ul></div>
    </aside>
  </div>
</div>"""
    return layout(l["name"], body, current=l["section"], description=l["summary"], path=path)


def page_areas() -> str:
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs(('Areas', ''))}<h1>Nairobi by neighbourhood</h1>
  <p class="lede">Where you stay shapes your whole trip, mostly because of traffic. Here's how the main neighbourhoods differ.</p></div>
  <div class="grid two">{''.join(area_card(a) for a in AREAS)}</div>
</div>"""
    return layout("Areas", body, current="areas", path="/areas/")


def page_area(a: dict) -> str:
    items = [l for l in LISTINGS if l["area"] == a["slug"]]
    by_sec = {k: [l for l in items if l["section"] == k] for k in SECTIONS}
    blocks = ""
    for k, ls in by_sec.items():
        if not ls:
            continue
        blocks += f'<section class="band"><div class="band-head"><h2>{SECTIONS[k]["title"]} in {e(a["name"])}</h2><a class="more" href="/{k}/">All {SECTIONS[k]["title"].lower()} →</a></div><div class="grid">{"".join(listing_card(l) for l in ls)}</div></section>'
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs(('Areas', '/areas/'), (a['name'], ''))}<div class="eyebrow">{e(a['vibe'])}</div><h1>{e(a['name'])}</h1>
  <p class="lede">{e(a['body'])}</p>
  <div class="chips">{''.join(f'<span class="chip">{e(g)}</span>' for g in a['good_for'])}</div></div>
  {blocks}
  <section class="band"><div class="band-head"><h2>Other neighbourhoods</h2></div>
  <div class="grid">{''.join(area_card(x) for x in AREAS if x['slug'] != a['slug'])}</div></section>
</div>"""
    return layout(a["name"], body, current="areas", description=a["vibe"], path=f"/areas/{a['slug']}/")


def page_guides() -> str:
    cards = "".join(
        f'<a class="card" href="/guides/{g["slug"]}/"><div class="body"><div class="eyebrow">Guide</div><h3>{e(g["title"])}</h3><p>{e(g["dek"])}</p></div></a>'
        for g in GUIDES)
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs(('Guides', ''))}<h1>Nairobi travel guides</h1>
  <p class="lede">The practical side of the city: arriving, getting around, when to come and where to go for the day.</p></div>
  <div class="grid two">{cards}</div>
</div>"""
    return layout("Travel guides", body, current="guides", path="/guides/")


def page_guide(g: dict) -> str:
    content = ""
    for heading, paras in g["sections"]:
        content += f"<h2>{e(heading)}</h2>" + "".join(f"<p>{e(p)}</p>" for p in paras)
    others = "".join(guide_row(x) for x in GUIDES if x["slug"] != g["slug"])
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs(('Guides', '/guides/'), (g['title'], ''))}<h1>{e(g['title'])}</h1><p class="lede">{e(g['dek'])}</p></div>
  <div class="detail">
    <article class="guide-body">{content}
      <p class="notice">Fees, schedules and official requirements change. Treat this as orientation and confirm specifics with the official source before you travel.</p></article>
    <aside><div class="box"><h3>More guides</h3><ul class="linklist" style="list-style:none;padding:0">{others}</ul></div></aside>
  </div>
</div>"""
    return layout(g["title"], body, current="guides", description=g["dek"], path=f"/guides/{g['slug']}/")


def page_experiences() -> str:
    cards = "".join(
        f'<div class="card" id="{x["slug"]}"><div class="body"><div class="meta"><b>{e(x["category"])}</b> · {e(x["duration"])}</div>'
        f'<h3>{e(x["name"])}</h3><p>{e(x["summary"])}</p></div></div>' for x in EXPERIENCES)
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs(('Experiences', ''))}<h1>Experiences &amp; days out</h1>
  <p class="lede">Ways to spend a half day or a full one. We describe the experience and leave you to pick an operator; many are easy to do independently.</p></div>
  <div class="grid two">{cards}</div>
  <p class="notice" style="margin-top:2rem">We don't take commission from operators. For guided options, ask your hotel for a licensed operator or driver-guide.</p>
</div>"""
    return layout("Experiences", body, current="experiences", path="/experiences/")


def page_about() -> str:
    body = f"""
<div class="wrap">
  <div class="page-head">{crumbs(('About', ''))}<h1>About Nairobi.guide</h1>
  <p class="lede">{e(SITE['description'])}</p></div>
  <div class="guide-body">
    <h2 id="how-we-choose">How we choose</h2>
    <p>Everything listed is somewhere we'd happily send a friend. Nobody pays to be included, and we don't run sponsored listings. When we're unsure about a place, we leave it out rather than hedge.</p>
    <h2 id="ratings">Why we don't show star ratings</h2>
    <p>Ratings and review counts belong to the platforms that collect them, and they go stale the moment they're copied. We describe what a place is and who it suits, and point you to the venue's own channels for live hours, prices and reviews.</p>
    <h2 id="prices">Price bands</h2>
    <p>$ budget · $$ mid-range · $$$ upmarket · $$$$ splurge. They're relative to Nairobi, not to London or New York.</p>
    <h2 id="contact">Contact</h2>
    <p>Spotted something out of date, or think we've missed a gem? Write to <a href="mailto:hello@{SITE['domain']}">hello@{SITE['domain']}</a>.</p>
  </div>
</div>"""
    return layout("About", body, path="/about/")


def page_search() -> str:
    # Client-side search over a generated JSON index.
    body = """
<div class="wrap">
  <div class="page-head"><h1>Search</h1>
  <form class="search" action="/search/" method="get" role="search">
    <input id="q" type="search" name="q" placeholder="Try nyama choma, Karen, rhino…" aria-label="Search">
    <button class="btn" type="submit">Search</button></form></div>
  <div id="results" class="grid"></div>
  <p id="empty" class="notice" hidden>No matches. Try a neighbourhood, a dish or a type of place.</p>
</div>
<script>
(async function(){
  const idx = await (await fetch('/assets/search.json')).json();
  const q = new URLSearchParams(location.search).get('q') || '';
  const input = document.getElementById('q'); input.value = q;
  const out = document.getElementById('results'), empty = document.getElementById('empty');
  const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  function run(term){
    const t = term.trim().toLowerCase(); out.innerHTML=''; empty.hidden = true;
    if(!t) return;
    const hits = idx.filter(x => x.text.includes(t));
    if(!hits.length){ empty.hidden=false; return; }
    out.innerHTML = hits.map(x => `<a class="card" href="${x.url}"><div class="body"><div class="meta"><b>${esc(x.kind)}</b></div><h3>${esc(x.title)}</h3><p>${esc(x.summary)}</p></div></a>`).join('');
  }
  run(q); input.addEventListener('input', e => run(e.target.value));
})();
</script>"""
    return layout("Search", body, path="/search/")


def page_404() -> str:
    body = """<div class="wrap"><div class="page-head"><h1>Lost in traffic</h1>
<p class="lede">That page isn't here. Try the <a href="/">home page</a> or <a href="/search/">search</a>.</p></div></div>"""
    return layout("Not found", body, path="/404.html")


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------
def write(path: str, content: str) -> None:
    out = DIST / path.lstrip("/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")


def search_index() -> str:
    import json
    rows = []
    for l in LISTINGS:
        rows.append({"title": l["name"], "kind": SECTIONS[l["section"]]["types"][l["type"]],
                     "summary": l["summary"], "url": f"/{l['section']}/{l['type']}/{l['slug']}/",
                     "text": " ".join([l["name"], l["summary"], l["body"], AREA_BY_SLUG[l["area"]]["name"], *l["tags"]]).lower()})
    for a in AREAS:
        rows.append({"title": a["name"], "kind": "Area", "summary": a["vibe"], "url": f"/areas/{a['slug']}/",
                     "text": " ".join([a["name"], a["vibe"], a["body"]]).lower()})
    for g in GUIDES:
        rows.append({"title": g["title"], "kind": "Guide", "summary": g["dek"], "url": f"/guides/{g['slug']}/",
                     "text": " ".join([g["title"], g["dek"]] + [p for _, ps in g["sections"] for p in ps]).lower()})
    for x in EXPERIENCES:
        rows.append({"title": x["name"], "kind": x["category"], "summary": x["summary"], "url": f"/experiences/#{x['slug']}",
                     "text": " ".join([x["name"], x["summary"], x["category"]]).lower()})
    return json.dumps(rows, ensure_ascii=False)


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#8a3b12"/><text x="32" y="44" font-family="Georgia,serif" font-size="36" font-weight="700" text-anchor="middle" fill="#fff">N</text></svg>"""


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    urls: list[str] = []

    def put(path: str, content: str) -> None:
        write(path + ("index.html" if path.endswith("/") else ""), content)
        urls.append(path)

    put("/", page_home())
    for key in SECTIONS:
        put(f"/{key}/", page_section(key))
        for t in SECTIONS[key]["types"]:
            put(f"/{key}/{t}/", page_type(key, t))
    for l in LISTINGS:
        put(f"/{l['section']}/{l['type']}/{l['slug']}/", page_listing(l))
    put("/areas/", page_areas())
    for a in AREAS:
        put(f"/areas/{a['slug']}/", page_area(a))
    put("/guides/", page_guides())
    for g in GUIDES:
        put(f"/guides/{g['slug']}/", page_guide(g))
    put("/experiences/", page_experiences())
    put("/about/", page_about())
    put("/search/", page_search())
    write("/404.html", page_404())

    write("/assets/site.css", CSS.strip() + "\n")
    write("/assets/search.json", search_index())
    write("/favicon.svg", FAVICON)
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: https://{SITE['domain']}/sitemap.xml\n")
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>https://{SITE['domain']}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    print(f"Built {len(urls)} pages into {os.path.relpath(DIST)}")


if __name__ == "__main__":
    main()
