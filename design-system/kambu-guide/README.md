# Kambu Guide design system

Version 1.0 · 1 October 2026

The page system for Kambu Campers safari **guides**: planning guides,
itineraries, destination guides, cost explainers and comparisons. It was saved
from the 10-day Kenya safari itinerary draft of 15 September 2026, kept its
markup and class names, and adds an interactive layer and a writing
framework.

Products (exact bookable packages) are out of scope; they use the product
skills.

## What is here

| File | Job |
|---|---|
| `styles.css` | Site chrome, type, layout grid, tables, notes, sidebar, footer |
| `itinerary.css` | Route strip, "In this guide" contents, day sections, allocation lines, editorial drawer |
| `components.css` | The `.kg-` layer: tabs, sidebar tabs, accordions, gallery and lightbox, answer box, field note, suitability, decision rule, day navigation, sources register, wayfinding |
| `components.js` | Progressive enhancement for the `.kg-` layer, with analytics events. No dependencies |
| `docs/writing-framework.md` | **How a guide is written**: charter, page contract, coverage ledger, writing rules, credentials, evidence grades, interaction blueprint, quality gates |
| `docs/components.md` | **How a guide is built**: copy-ready markup for every component and when to use it |
| `tools/check_guide.py` | Automated pre-publication gates (structure, wiring, never-claim terms, phrasing, sources, images) |
| `tools/build_standalone.py` | Bundles a guide into one HTML file (optionally with images embedded) |
| `reference/original-10-day-itinerary.html` | The page exactly as supplied, kept for reference |

Pages live in `guides/<slug>/index.html` with their photos in
`guides/<slug>/assets/`. Start from `guides/_template/`. The worked example
is `guides/10-day-kenya-safari-itinerary/`.

## Start a new guide

```bash
cp -r guides/_template guides/<slug>
# 1. fill the page contract in the head comment and build the coverage ledger (writing-framework.md §4–5)
# 2. write the copy into the template, deleting modules the page does not need
# 3. add photos to guides/<slug>/assets/ as WebP at 400/800/1200 widths
python3 design-system/kambu-guide/tools/check_guide.py guides/<slug>/index.html
python3 -m http.server 8000   # then open http://localhost:8000/guides/<slug>/
```

`check_guide.py` exits non-zero while any `[[…]]` placeholder, missing image,
broken in-page link or never-claim term remains.

Or ask Claude: the repo skill in `.claude/skills/kambu-safari-guide/` runs the
whole process (contract, ledger, research, writing, build, checks, handoff).

## What changed from the supplied page

The fonts, colours, class names and layout of the original are kept. The
additions are deliberately quiet:

- **Toggle tabs** for genuinely alternative views (balanced vs
  wildlife-intensive route). Without JavaScript every panel shows under its
  own heading.
- **Sidebar tabs** for four to six alternatives with sub-labels and colour
  swatches; they become a scrolling strip whenever their column is narrow.
- **Accordions** for the FAQ (first answer open, deep-linkable, smooth where
  supported).
- **Image gallery** with ‹ › arrows, a counter, keyboard and swipe, and a
  full-screen viewer with its own arrows.
- **Wayfinding**: a reading-progress line under the header, the sidebar
  highlights the section in view, copy-link anchors on headings, previous and
  next links between itinerary days, a back-to-top button on phones, and
  anchored headings that land below the sticky header.
- **Editorial blocks** the framework requires: direct-answer box, field note
  for first-party experience, suits / choose-something-else split, Choose A /
  Choose B rule, graded sources register, last-reviewed line.

## The original stylesheets

The supplied page linked `styles.css` and `itinerary.css`, which were not
supplied with it and were not found in the repo, Drive or artifacts. The two
files here are **rebuilt** from the page's own markup and from the layout its
`<img sizes>` attribute encodes: one column below 1024 px, a 360 px sidebar
from 1024 px, 400 px from 1251 px, and a 1024 px reading column at 1600 px.
Fonts and colours follow Executive Elegant (Cormorant Garamond with Inter;
forest, brass and ivory), the system recorded as canonical for
kambucampers.com on 15 September 2026.

**If you have the original files, drop them in over these two.**
`components.css` only reads the tokens below and falls back sensibly when one
is missing, so nothing else changes.

| Token | Value | Role |
|---|---|---|
| `--font-display` | Cormorant Garamond | headings, numbers |
| `--font-body` | Inter | body, UI, tables |
| `--ink` | `#191b18` | body text (16.6:1 on paper) |
| `--muted` | `#5a6259` | secondary text (6.0:1) |
| `--forest` / `--forest-d` | `#233a31` / `#16261f` | headings, dark card, footer |
| `--brass` / `--brass-d` / `--brass-l` | `#ad8b54` / `#7b5f37` / `#c7a874` | rules / kickers and CTA / emphasis on dark |
| `--teal-d` | `#0e7c78` | focus ring, active state |
| `--paper` / `--surface` / `--ivory` / `--bone` | `#fcfaf4` / `#fff` / `#f8f4ec` / `#f1e9db` | surfaces |
| `--line` / `--line-strong` | `#e4dbca` / `#c9bba1` | hairlines / control borders |
| `--k-teal --k-gold --k-magenta --k-blue --k-coral` | accent five | wayfinding swatches only |
| `--h2-align` | `left` | set to `center` to follow page-build-defaults §7 |

## Browser support and fallbacks

Current Chrome, Edge, Safari and Firefox. Container queries, `<dialog>` and
`interpolate-size` are progressive enhancements; each component falls back
to its static form without them, and the whole page reads with JavaScript
off. Print shows every tab panel and accordion answer.

## Not yet done

- **WordPress delivery.** These pages are standalone HTML with global class
  names. A Custom HTML block on the Astra theme needs a scoped build (every
  selector under one wrapper class, `body`/`:root` rules moved onto it). Not
  built yet.
- **Hero image for the example.** `guides/10-day-kenya-safari-itinerary/assets/`
  is missing `amboseli-elephants-400.webp` and `-800.webp` from the original
  draft; Wikimedia was not reachable from the build environment.
- The canonical design decision: kambu-brand-voice names Executive Elegant;
  kambu-campers-design describes the roller palette. This system follows
  Executive Elegant and keeps every colour in one token block so it can be
  switched.

## Changelog

- **1.0 · 1 Oct 2026** — saved from the 10-day itinerary draft; rebuilt base
  CSS; added the `.kg-` component layer, writing framework, template, checker
  and bundler.
