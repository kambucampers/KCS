# Nairobi.guide

A static city guide to Nairobi, modelled on the structure of a directory site
(Eat / Stay / Visit / Play / Areas / Guides / Experiences) but with its own
name, design and copy.

## What's in here

- `data.py` — all content: sections, neighbourhoods, listings, experiences and
  long-form guides. Edit this to add or change places.
- `build.py` — a dependency-free Python generator that renders `dist/`.
- `dist/` — build output (not committed).

## Build and preview

```sh
cd nairobi-guide
python3 build.py
python3 -m http.server -d dist 8000
```

Then open <http://localhost:8000/>. The output is plain HTML/CSS with one small
script for the client-side search page, so it deploys to any static host
(Cloudflare Pages, Netlify, GitHub Pages, S3). Point the `nairobi.guide` domain
at the host and set `404.html` as the not-found page.

## Site map

```
/                       home
/eat/  /stay/  /visit/  /play/        section hubs
/eat/<type>/            e.g. /eat/nyama-choma/
/eat/<type>/<slug>/     listing detail
/areas/  /areas/<slug>/ neighbourhoods
/guides/ /guides/<slug>/ long-form guides
/experiences/           days out
/about/  /search/       editorial policy, client-side search
/sitemap.xml /robots.txt
```

## Editorial notes

- Copy is original; nothing is scraped from other sites.
- No third-party ratings or review counts are shown. Listings describe what a
  place is and who it suits, and point readers to the venue's own channels for
  live hours and prices.
- Card images are generated gradients. Replace the `.art` blocks in
  `build.py` with real photographs you have the rights to when available.
