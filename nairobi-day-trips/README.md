# Nairobi Day Trips (nairobidaytrips.com)

A static Astro + Tailwind site for Nairobi Day Trips, built to deploy on
Cloudflare Pages. No database, no CMS, no server. `npm run build` produces a
`dist/` folder that any static host can serve.

## Run it locally

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # static output in dist/
npm run preview  # serve the built dist/ locally
```

## Fill in the placeholders before going live

Everything the business still needs to supply is marked `[PLACEHOLDER: ...]`
and lives in one file, `src/data/site.ts`. Editing it updates the header,
footer, contact page, booking form and the JSON-LD schema at once.

| Field | What to put there |
| --- | --- |
| `phone` / `phoneHref` | Public number, plus `tel:+254...` |
| `whatsapp` / `whatsappHref` | WhatsApp number, plus `https://wa.me/254...` |
| `email` / `emailHref` | Booking inbox, plus `mailto:...` |
| `street` / `postalCode` | Office address, used in LocalBusiness schema |
| `openingHours` | When enquiries are answered |
| `formEndpoint` | See "Connect the booking form" below |

Two further placeholders sit in page copy rather than config:

- **Pricing** appears on every tour page and in the FAQ. Search for
  `[PLACEHOLDER: pricing]` once prices are set.
- **Company registration, tourism licence, insurance, payment terms and the
  cancellation policy** are in `src/pages/about.astro`, `src/pages/faq.astro`
  and `src/pages/contact.astro`.

## Connect the booking form

The booking form is the site's single conversion goal, and a static site
cannot process a form on its own, so it needs a free third-party endpoint.

1. Create a free form at [Formspree](https://formspree.io) or
   [Web3Forms](https://web3forms.com).
2. Paste the endpoint URL into `formEndpoint` in `src/data/site.ts`.
   For Web3Forms, also paste the access key into `formAccessKey`.
3. Rebuild and submit a test enquiry.

Until an endpoint is set, the form still validates and tells the visitor to
email instead, so no enquiry is silently lost.

## Deploy to Cloudflare Pages

Connect the GitHub repository in the Cloudflare dashboard:

1. Cloudflare dashboard, then **Workers & Pages**, then **Create**, then
   **Pages**, then **Connect to Git**.
2. Pick this repository and the branch to deploy.
3. Framework preset **Astro**, build command **`npm run build`**, output
   directory **`dist`**, root directory the folder holding this README.
4. **Save and Deploy**, then add `nairobidaytrips.com` under **Custom domains**.

Or deploy the built folder straight from a terminal:

```bash
npm run build
npx wrangler pages deploy ./dist --project-name nairobi-day-trips
```

## How the site is put together

```
src/
  data/site.ts        business details and the form endpoint, single source of truth
  data/tours.ts       all eight tours: copy, itineraries, FAQs, cost factors
  layouts/            BaseLayout: head tags, Open Graph, JSON-LD graph
  components/         Header, Footer, BookingForm, TourCard, SceneArt, FaqList
  pages/              one file per route; tours/[slug].astro builds all eight tour pages
  styles/global.css   the design system: colour, type, spacing, component classes
public/
  fonts/              Fraunces and Figtree, self-hosted so no third-party request
  robots.txt          points at the generated sitemap
```

Adding a tour means adding one object to `src/data/tours.ts`. The route, the
card, the comparison table, the footer link, the sitemap entry and the booking
form dropdown all follow automatically.

## Design system

| Token | Value | Use |
| --- | --- | --- |
| Ink | `#23201C` | Body text |
| Paper | `#FBF6EE` | Page background |
| Sand | `#F0E4D2` | Alternating section bands |
| Acacia green | `#14523C` / `#0E3A2A` | Dark bands, headings, links |
| Sunrise amber | `#E4572E` | The one action colour, primary buttons only |

Type is Fraunces for display and Figtree for body, both self-hosted as
variable-font woff2 subsets, preloaded, roughly 140KB combined.

Section rhythm runs on a 4px base with sections at 64, 96 and 128px.

## Images

Tour artwork is hand-built SVG in `src/components/SceneArt.astro` rather than
stock photography, so the pages carry no image weight and nothing is licensed
from anywhere. Replace any `<SceneArt ... />` with an `<img>` when real
photographs of the tours are available; nothing else depends on that component.

## SEO

Every page has one `<h1>`, a unique title and meta description, a canonical
URL, Open Graph and Twitter tags, and breadcrumbs. JSON-LD covers
Organization, TravelAgency, TouristInformationCenter, WebSite, TouristTrip
per tour, FAQPage and BreadcrumbList. `sitemap-index.xml` is generated at build
time and `robots.txt` points at it.
