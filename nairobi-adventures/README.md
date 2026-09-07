# Nairobi Adventures

Static marketing site for Nairobi Adventures, a Nairobi tour operator running day
excursions in the city and day tours starting from it.

Built with **Astro 7** and **Tailwind CSS 4**, output as a fully static site in `dist/`
and deployable to Cloudflare Pages with no server, database or paid tooling.

## Run it locally

```bash
npm install
cp .env.example .env          # then paste your Pexels key into it
npm run media                 # fetch photographs into public/images/
npm run dev                   # http://localhost:4321
npm run build                 # static output in dist/
npm run preview               # serve the built dist/ locally
```

The site builds and runs without the media step. Until photographs are fetched, each image slot
renders a quiet landscape graphic in the same palette, so nothing looks broken and no layout
shifts when the photographs arrive.

`dist/` must be served by a web server. Do not open `dist/index.html` from the file
system: clean URLs such as `/tours/` only resolve when a host serves the folder.

## Pages

| Route | Purpose | Primary call to action |
| --- | --- | --- |
| `/` | Positioning and the four excursions | Request a booking |
| `/tours/` | Overview and comparison of all excursions | Pick a tour |
| `/tours/nairobi-national-park-game-drive/` | Flagship park game drive | Request a booking |
| `/tours/nairobi-city-excursions/` | Karen and Lang'ata attractions | Request a booking |
| `/tours/day-trips-from-nairobi/` | Rift Valley and Amboseli day trips | Request a booking |
| `/tours/airport-layover-tours/` | JKIA layover excursions | Send flight numbers |
| `/plan-your-day/` | Practical planning guide | Request a booking |
| `/about/` | Who runs the business and how | Contact |
| `/contact/` | Booking form and direct contact | Send booking request |
| `404` | Not found, routes back into the tours | Request a booking |

## Design system

Defined once in `src/styles/global.css` as Tailwind v4 theme tokens.

- **Colour**: Ink `#14231C`, Acacia `#17513A`, Acacia bright `#1F6B4B`, Marigold `#E0A33E`,
  Marigold soft `#F2CE8C`, Clay `#B5502F`, Bone `#F7F3EA`, Sand `#E8DFCE`, Slate `#4A554E`.
- **Type**: Fraunces Variable for display, Hanken Grotesk Variable for body, both self-hosted
  through `@fontsource-variable` so no external font request is made at runtime.
- **Spacing**: 4px base, section rhythm 20 / 24 / 32 (Tailwind `py-16` to `py-28`), 78rem
  container, 68ch prose measure.

## Content and structure

- `src/data/site.ts` holds contact details, navigation and the tour list. Editing the tour
  array updates the header, footer, home page, tours index, booking form and 404 page.
- `src/layouts/BaseLayout.astro` owns the `<head>`: title, meta description, canonical,
  Open Graph, Twitter card and the Organization, TravelAgency, LocalBusiness and WebSite
  JSON-LD graph.
- `src/layouts/TourPageLayout.astro` is the shared tour template and emits BreadcrumbList,
  Product, TouristTrip and FAQPage schema per tour.
- `sitemap-index.xml` and `sitemap-0.xml` are generated at build time by `@astrojs/sitemap`.
  `public/robots.txt` points at them.

## The booking form

`src/components/BookingForm.astro` works with no backend: on submit it composes a structured
email to `bookings@nairobiadventures.com` and opens the visitor's mail client, which is why
a static host is enough.

To capture submissions server-side instead, create a free endpoint (Formspree, Web3Forms or
a Cloudflare Pages Function) and set `FORM_ENDPOINT` at the top of that component. The form
then posts normally and the mailto fallback is skipped automatically.

## Photography

`npm run media` fills every image slot defined in `src/data/media-sources.json`, writing files to
`public/images/` and a manifest to `src/data/media.json`.

Two sources, in this order per slot:

1. **Wikimedia Commons** for named Nairobi places, filtered to free licences only (CC0, public
   domain, CC BY and CC BY-SA). The author and licence are recorded and rendered as a credit.
2. **Pexels** for general wildlife and travel photography, using `PEXELS_API_KEY` from `.env`.

```bash
npm run media                      # fetch anything missing
npm run media:force                # refetch everything
npm run media -- --only=rhino,amboseli
```

Alt text lives with the slot in `src/data/media-sources.json`, not with the fetched file, so it
stays accurate whichever photograph comes back. Replace any fetched file with your own
photograph of the same name to use real Nairobi Adventures imagery.

## Pricing

Prices are generated, not typed into pages. `src/data/pricing.ts` holds the entry fees, the
vehicle day rates and a `MARKUP` constant of 1.2, and every price table, "from" figure and
schema.org offer is derived from it. `PRICING.md` documents the method, the market anchors and
the sources.

## Before going live

1. Set the production domain in `astro.config.mjs` (`site`) and in `public/robots.txt`.
   Canonical URLs, Open Graph URLs, the sitemap and schema all derive from that one value.
2. Read `ASSUMPTIONS.md` and correct anything stated on your behalf, prices included.
3. Run `npm run media`, then replace any fetched photograph with your own where you have one.
4. Add a phone or WhatsApp number in `src/data/site.ts` and it appears in the footer, the
   contact page and the LocalBusiness schema automatically.

## Deploy to Cloudflare Pages

**Option A, connect the GitHub repo (recommended):**

1. Cloudflare dashboard, Workers & Pages, Create, Pages, Connect to Git.
2. Pick this repository and the branch you want to deploy.
3. Framework preset: Astro. Build command: `npm run build`. Output directory: `dist`.
   Root directory: `nairobi-adventures` (this folder, since the repo holds other projects).
4. Save and Deploy, then add the custom domain under the project's Custom domains tab.

**Option B, deploy from your machine:**

```bash
npm run build
npx wrangler pages deploy ./dist --project-name nairobi-adventures
```

## The built site is committed

`dist/` is checked into this repository so the finished static site can be pulled and
uploaded to a host without running a build first. After editing anything in `src/`, run
`npm run build` and commit the regenerated `dist/` alongside the source change, otherwise
the two fall out of step.
