# Kambu Guide components

Version 1.0 · 1 October 2026

Copy-ready markup for every component, with when to use it. The writing rules
that decide *whether* a component belongs are in
[writing-framework.md](writing-framework.md) sections 5 and 9. A worked page
using all of them is [`guides/10-day-kenya-safari-itinerary/`](../../../guides/10-day-kenya-safari-itinerary/index.html).

Load order in `<head>`:

```html
<link rel="stylesheet" href="../../design-system/kambu-guide/styles.css">
<link rel="stylesheet" href="../../design-system/kambu-guide/itinerary.css">
<link rel="stylesheet" href="../../design-system/kambu-guide/components.css">
<script src="../../design-system/kambu-guide/components.js" defer></script>
```

Everything below works without JavaScript; the script upgrades it.
`components.js` exposes `window.KambuGuide.init(element)` for content inserted
after load.

---

## Page furniture (base system)

These come from the original guide page and keep its class names.

| Block | Classes | Notes |
|---|---|---|
| Sticky header | `.site-header > nav.container.nav-row` with `.wordmark`, `.desktop-navigation .nav-button`, `.button.header-cta` (`.desktop-label` / `.mobile-label`) | Four jump links at most; the CTA always points at `#plan`. Add `<div class="kg-progress" data-kg-progress="#article" hidden></div>` as the header's last child for the reading bar. |
| Article header | `.article-header` → `.breadcrumbs ol`, `h1`, `.article-meta`, `.kg-reviewed` | One H1. The reviewed line carries the date of the last real fact check. |
| Layout | `.article-grid` → `article#article` + `aside.sidebar-column > .sidebar-sticky` | Single column below 1024 px; 360 px sidebar from 1024 px; 400 px from 1251 px; 1024 px reading column at 1600 px. |
| Hero | `figure.hero-figure > img + figcaption` | Eager, `fetchpriority="high"`, credit in the caption. Full-bleed under 600 px. |
| Route strip | `figure.route-figure` → `.route-heading`, `ol.route-stops > li > a` (`.route-number`, `strong`, `small`), `figcaption` | Five stops fit; the strip turns vertical under 700 px. Label it "planning route, not to scale". |
| Contents | `nav.contents > h2 + a…` | All H2s of the guide, in order. |
| Section | `section.article-section[aria-labelledby]` → `h2[id]`, `.prose` | `.section-kicker` above the H2 on day sections. |
| Day | `section.article-section.day-section` + `dl.day-summary` | Kicker reads `Day 04 / Substantial road transfer`. |
| Table | `div.table-scroll[role=region][aria-label][tabindex=0] > table > caption…` | Row headers `th[scope=row]`; `td.numeric` for money. |
| Note | `aside.note > p` | Scope limits and cautions. |
| Allocation | `p.allocation` | One arithmetic line: `1 Nairobi + 2 Amboseli + … = 9 nights.` |
| Planning card | `section.planning-card` with `.fact-number` rows, `.button`, `.sidebar-note` | Three facts, all true for the whole page. |
| Shortcuts | `nav.sidebar-contents[data-kg-spy] > a` | Six to eight links; the one for the section in view is marked. |
| Editorial drawer | `aside.editorial-notes > details` | Drafts only. Remove before publishing. |

---

## 1. Direct answer — `.kg-answer`

The first paragraph of `.introduction`. 40–80 words that resolve the entity,
the question and the deciding factors.

```html
<p class="kg-answer">Our recommended <strong>10-day Kenya safari itinerary</strong> combines …</p>
```

Never inside a tab or accordion.

## 2. Horizontal tabs — `.kg-tabs`

For 2–4 **alternative views of one decision** (route versions, seasons,
road vs fly-in, traveller types). Not for options a reader needs to compare
side by side; use a table for that.

```html
<div class="kg-tabs" data-kg-tabs data-kg-label="Route version">
  <div class="kg-tabs__list" hidden>
    <button type="button" class="kg-tabs__tab" data-kg-tab="route-balanced" aria-selected="true">
      <span><span class="kg-tabs__label">Balanced route</span><span class="kg-tabs__sub">2 Naivasha · 3 Mara nights</span></span>
    </button>
    <button type="button" class="kg-tabs__tab" data-kg-tab="route-wildlife" style="--kg-swatch: var(--k-teal)">
      <span><span class="kg-tabs__label">Wildlife-intensive</span><span class="kg-tabs__sub">1 Naivasha · 4 Mara nights</span></span>
    </button>
  </div>
  <section class="kg-tabs__panel" id="route-balanced" aria-labelledby="route-balanced-h">
    <h3 id="route-balanced-h">Balanced route: three full wildlife days and a Naivasha activity day</h3>
    …
  </section>
  <section class="kg-tabs__panel" id="route-wildlife" aria-labelledby="route-wildlife-h">
    <h3 id="route-wildlife-h">Wildlife-intensive route: four full wildlife days</h3>
    …
  </section>
</div>
```

- Each panel has its **own heading**, so without JavaScript the panels stack
  as ordinary headed sections and nothing is lost.
- `aria-selected="true"` (or `data-kg-default`) marks the default tab.
- The script adds `role="tablist"/"tab"/"tabpanel"`, `aria-controls`, roving
  `tabindex`, ←/→ and Home/End keys, and opens the right tab when the URL hash
  points inside a panel.
- The strip scrolls sideways on phones with a fade that shows more tabs exist.
- Print shows every panel.
- Event: `tab_select {group, tab}`.

## 3. Sidebar tabs — `.kg-tabs.kg-tabs--vertical`

Same engine, vertical rail. Use for 4–6 alternatives, labels that need a
second line, or when each option deserves a wayfinding colour. Collapses to a
horizontal strip whenever **its own width** drops under 640 px (container
query), so it behaves inside the article column, not only on phones.

```html
<div class="kg-tabs kg-tabs--vertical" data-kg-tabs data-kg-label="Alternative routes">
  <div class="kg-tabs__list" hidden>
    <p class="kg-tabs__eyebrow">Choose a variation</p>
    <button type="button" class="kg-tabs__tab" data-kg-tab="alt-mara" aria-selected="true" style="--kg-swatch: var(--k-teal)">
      <i class="kg-tabs__swatch"></i><span><span class="kg-tabs__label">Four Mara nights</span><span class="kg-tabs__sub">More wildlife</span></span>
    </button>
    …
  </div>
  <section class="kg-tabs__panel" id="alt-mara" aria-labelledby="four-mara-nights">
    <h3 id="four-mara-nights">More wildlife: increase the Mara to four nights</h3>
    <div class="kg-split">
      <div class="prose">…</div>
      <ul class="kg-facts">
        <li><b>Allocation</b>1 Nairobi + 2 Amboseli + 1 Naivasha + 4 Mara + 1 Nairobi = 9 nights</li>
        <li><b>Full wildlife days</b>Four</li>
        <li><b>You give up</b>The Naivasha activity day</li>
      </ul>
    </div>
  </section>
  …
</div>
```

- Swatches use the accent five (`--k-teal`, `--k-gold`, `--k-magenta`,
  `--k-blue`, `--k-coral`), one per tab in a fixed order, or none at all.
- Keys: ↑/↓ (and ←/→) move between tabs.
- `.kg-split` puts prose beside a fact grid when the tab set is wider than
  980 px and stacks them otherwise. `.kg-facts` is a hairline grid; an odd
  last cell spans both columns.
- Unlike the CSS-only `sidebar-tabs` skill, these panels stay readable without
  JavaScript and carry real tab semantics, which the content-architect gate
  requires.

## 4. Accordion / FAQ — `.kg-acc`

Native `<details>`. For residual questions, policies, logistics and optional
depth. About eight FAQ questions, the first one open, answers in prose that
open with the answer.

```html
<div class="kg-acc">
  <details class="kg-acc__item" id="ten-days-enough" open>
    <summary><h3 class="kg-acc__q">Is ten days enough for a first Kenya safari?</h3></summary>
    <div class="kg-acc__body prose"><p><strong>Ten days is enough for …</strong> …</p></div>
  </details>
  …
</div>
```

- The heading inside `<summary>` is valid HTML and keeps the question in the
  document outline.
- Ids on `<details>` make each question linkable; a deep link opens it.
- Opens smoothly where the browser supports `interpolate-size`; instantly
  elsewhere and under reduced motion. Find-in-page reaches closed answers.
- Event: `disclosure_open {id, label}`.

## 5. Gallery and lightbox — `.kg-gallery`

A scroll-snap strip with ‹ › buttons, a "2 / 4" counter, keyboard arrows,
swipe, and a full-screen viewer with its own arrows. One per page; two on a
long guide. Use it only for photos that let the reader judge something (the
tent, the bathroom, the road), with captions that say what the photo shows
and a credit.

```html
<figure class="kg-gallery" data-kg-gallery aria-label="Inside a Kambu Mara Camp tent" style="--kg-ratio: 4 / 3">
  <div class="kg-gallery__head">
    <p class="kg-gallery__title">Inside a Kambu Mara Camp tent</p>
    <div class="kg-gallery__controls" hidden>
      <button type="button" class="kg-iconbtn" data-kg-prev aria-label="Previous photo">&lsaquo;</button>
      <span class="kg-gallery__count" aria-live="polite">1 / 4</span>
      <button type="button" class="kg-iconbtn" data-kg-next aria-label="Next photo">&rsaquo;</button>
    </div>
  </div>
  <div class="kg-gallery__viewport" tabindex="0" aria-label="Photos of a Kambu Mara Camp tent; use the arrow keys to move between them">
    <ul class="kg-gallery__track">
      <li class="kg-gallery__slide">
        <figure>
          <a class="kg-gallery__open" href="assets/photo-1200.webp">
            <img src="assets/photo-800.webp" srcset="assets/photo-400.webp 400w, assets/photo-800.webp 800w, assets/photo-1200.webp 1200w"
                 sizes="(max-width: 1023px) calc(100vw - 32px), (max-width: 1250px) calc(100vw - 432px), (max-width: 1599px) calc(100vw - 576px), 1024px"
                 width="800" height="600" alt="What is in the photo, and where" loading="lazy" decoding="async">
          </a>
          <figcaption><b>One-line point.</b> What the reader can judge from it. <span class="kg-credit">Photo: Kambu Campers</span></figcaption>
        </figure>
      </li>
      …
    </ul>
  </div>
  <div class="kg-gallery__dots" aria-hidden="true" hidden></div>
</figure>
```

- `--kg-ratio` sets the frame (default `3 / 2`; camp phone photos are `4 / 3`).
- `.kg-gallery--peek` shows a sliver of the next slide.
- Without JavaScript the strip still scrolls and each link opens the full
  image. With it, links open the lightbox (Esc, ←/→, swipe, backdrop click;
  focus returns to the photo you opened), and ctrl/cmd-click still opens a
  new tab.
- Photo rules: Kambu's own photos for the camp, fleet and team; Wikimedia or
  Pexels placeholders elsewhere with photographer and licence, marked
  `data-placeholder="true"`; never stock people standing in for staff; open
  every photo before using it.
- Events: `gallery_open {gallery, index}`, `gallery_nav {gallery, index, view}`.

## 6. Field note — `.kg-fieldnote`

First-party experience at a judgement call. One to three per page. Carries the
page's single entity-home link.

```html
<aside class="kg-fieldnote" aria-label="Field note from Kambu Mara Camp">
  <span class="kg-fieldnote__label">From Kambu Mara Camp, near Sekenani</span>
  <p>At <a href="https://kambucampers.com/">Kambu Campers</a> we route Mara days from our own camp …</p>
  <p>We cannot promise …</p>
</aside>
```

Every fact in it must trace to `experience_basis` in the framework.

## 7. Suitability — `.kg-suit`

```html
<div class="kg-suit">
  <div class="kg-suit__yes"><h3 id="suits-you">This route suits you if</h3><ul><li>…</li></ul></div>
  <div class="kg-suit__no"><h3 id="choose-else">Choose a different plan if</h3><ul><li>…</li></ul></div>
</div>
```

Both sides always. The "no" side links to the alternative that fits.

## 8. Decision rule — `.kg-choose`

```html
<div class="kg-choose">
  <div style="--kg-swatch: var(--brass)"><p><b>Choose the balanced route if…</b>you want …</p></div>
  <div style="--kg-swatch: var(--k-teal)"><p><b>Choose four Mara nights if…</b>wildlife time …</p></div>
</div>
```

Ends every comparison. No universal winner.

## 9. Day navigation — `.kg-daynav`

At the end of each day section. Furniture, exempt from anchor discipline.

```html
<nav class="kg-daynav" aria-label="Day 4 navigation">
  <a href="#day-3" rel="prev"><small>&larr; Day 3</small><span>A full day in Amboseli</span></a>
  <a href="#day-5" rel="next"><small>Next &middot; Day 5</small><span>Choose your Naivasha experience &rarr;</span></a>
</nav>
```

## 10. Sources register — `.kg-sources`

At the foot, before the editorial drawer. One row per source with its grade.

```html
<ul class="kg-gradekey" aria-label="Evidence grades"><li><b>A</b> official instrument</li>…</ul>
<ol class="kg-sources">
  <li><span class="kg-grade" title="Authority notice">B</span><span><a href="…">Kenya Wildlife Service: Amboseli National Park</a><br><small>What it supports</small></span></li>
</ol>
```

## 11. Freshness — `.kg-reviewed`

```html
<p class="kg-reviewed">Fees, travel times and sources checked <time datetime="2026-09-15">15 September 2026</time></p>
```

Change the date only after an actual check.

## 12. Wayfinding switches

| Attribute | Where | Does |
|---|---|---|
| `data-kg-progress="#article"` | `.kg-progress` inside `.site-header` | Reading-progress bar; fires `scroll_depth_25/50/75/90` once each |
| `data-kg-spy` | any nav of `#` links | Sets `aria-current` on the link for the section in view |
| `data-kg-anchors` | `article` | Adds a `#` copy-link button to each `h2[id]`; event `copy_section_link` |
| `data-kg-totop` | `body` | Floating back-to-top button on screens under 1024 px |

Anchored headings land below the sticky header (`scroll-margin-top`), and a
deep-linked heading flashes briefly.

---

## Analytics

Every interaction dispatches a `kg:track` event on `document` and, when
`window.dataLayer` exists, pushes the same object:

```js
document.addEventListener('kg:track', e => console.log(e.detail));
// { event: 'tab_select', group: 'Route version', tab: 'Wildlife-intensive' }
```

Events: `tab_select`, `disclosure_open`, `gallery_open`, `gallery_nav`,
`copy_section_link`, `scroll_depth_25`, `scroll_depth_50`, `scroll_depth_75`,
`scroll_depth_90`. Read them together with engaged time and enquiries: lots
of clicks with no enquiries can mean curiosity, not usefulness.

## Accessibility contract

- Real `<button>` for state, `<a>` for navigation; 44 px touch targets.
- Visible 3 px teal focus rings on every control; never removed.
- Tabs follow the WAI-ARIA tabs pattern; the gallery uses
  `aria-roledescription="carousel"` and labelled slides; the lightbox is a
  modal `<dialog>` that restores focus.
- No hover-only content; no autoplay; `prefers-reduced-motion` turns off
  transitions and smooth scrolling.
- Contrast: body 16.6:1, secondary text 6.0:1, buttons 5.9:1, focus ring
  4.8:1 against the page.

## Browser support

Current Chrome, Edge, Safari and Firefox. Container queries (sidebar tabs),
`<dialog>` (lightbox) and `interpolate-size` (smooth accordions) are
progressive: where one is missing, the component falls back to its static
form.
