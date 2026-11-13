# SEO Audit: kambumaracamp.com

**Date:** 13 November 2026
**Business type:** Local hospitality (tented camp and campsite near Sekenani Gate, Masai Mara), with safari packages
**SEO Health Score:** **63 / 100**

| Category | Weight | Score |
|---|---|---|
| Technical SEO | 22% | 45 |
| Content Quality | 23% | 80 |
| On-Page SEO | 20% | 50 |
| Schema / Structured Data | 10% | 55 |
| Performance (estimated) | 10% | 75 |
| AI Search Readiness | 10% | 70 |
| Images | 5% | 85 |

## How this audit was done, and its limits

- The audit sandbox can't connect to the site directly, so every page was fetched through Firecrawl. Pages checked: robots.txt, the sitemap index and all 3 child sitemaps, the homepage, `/tents/`, `/rates/`, `/3-day-masai-mara-safari/`, `/masai-mara-guide/`, `/reviews/`, `/v2/`, `/v2/tents/`, `/sample-page/`, `/hello-world/` and `/10-2/`. It also checked an http/www redirect, a made-up URL and `/llms.txt`.
- **There are no measured Core Web Vitals.** The PageSpeed Insights API had used up its daily limit, no Google API credentials are set up, and Chromium couldn't be installed here. The Performance score comes from the page source only.
- Not checked: HTTP response headers (HSTS, CSP, caching), Search Console data and backlinks.

## Executive summary

The content is strong. Pages answer real traveller questions in their headings, quote specific prices, and are clearly written by the people who run the camp. The technical setup lets that content down.

**Top 5 issues**
1. **A full duplicate of the site is live and in the sitemap.** All 32 pages under `/v2/` are indexable, canonicalise to themselves, and appear in `page-sitemap1.xml`. `/v2/tents/` has the same title, H1 and headings as `/tents/`.
2. **Three systems write tags into every page's `<head>`:** BeyondSEO, a second SEO/meta output, and the theme's own description. Each page ends up with three meta descriptions, two canonicals, and two sets of og:title and twitter tags. The first two descriptions are scraped menu text, e.g. "Skip to contentWhatsAppBook nowHomeThe camp at a glance…". Google may show those as your search snippet.
3. **WordPress's default pages are live and indexable:** `/hello-world/` ("Welcome to WordPress…"), `/sample-page/`, an untitled `/10-2/`, and `/category/uncategorized/`. All are listed in the sitemap.
4. **No analytics is running.** The page source contains `<!-- No tracking code set -->` from MonsterInsights, so organic traffic and enquiries aren't being measured.
5. **Weak titles:** the homepage title is just "Home". Every other title adds the 64-character site name, so `Tents - Kambu Mara Camp - Affordable Masai Mara Camping Accommodation Near Sekenani` runs to about 83 characters and gets truncated.

**Top 5 quick wins**
1. Set `/v2/` to noindex and remove it from the sitemap, or remove it from the live site and finish the redesign on staging.
2. Delete Hello World, Sample Page, `/10-2/` and the empty Uncategorized category.
3. Turn off the meta-description and Open Graph output of every source except one.
4. Shorten the site title to "Kambu Mara Camp" and give the homepage a proper title.
5. Connect GA4 in MonsterInsights and verify the site in Search Console.

## Technical SEO: 45

**What works**
- `http://www.` redirects to `https://kambumaracamp.com/`.
- Missing pages return a real **404**.
- robots.txt is clean: it blocks only `/wp-admin/` and points to `/sitemaps.xml`.
- `/sitemap.xml` and `/wp-sitemap.xml` both redirect to the same sitemap index, which loads without errors.
- Pages are served as plain HTML, with no client-side rendering that crawlers could miss.

**Findings**
| Severity | Finding | Evidence |
|---|---|---|
| Critical | `/v2/` duplicate site is indexable and listed in the sitemap | `/v2/` and `/v2/tents/` return 200 with `index, follow` and self-canonicals. 32 `/v2/` URLs are in `page-sitemap1.xml`. `/v2/` also loads a `kambu-mara-camp-v2` plugin. |
| High | WordPress default pages are indexable and listed in the sitemap | `/hello-world/`, `/sample-page/`, `/10-2/` (empty title) and `/category/uncategorized/` |
| High | Duplicate canonical, description, OG and Twitter tags on every page | Two `rel=canonical` (same URL), three `meta name=description`, two og:title |
| High | No analytics | `<!-- No tracking code set -->` (MonsterInsights) |
| Medium | WordPress login name is published | `<meta name="author" content="Admin-JQPbu">` and `article:author` show the admin username to anyone, which makes it easier to try guessing the password |
| Low | `xmlrpc.php` is advertised (RSD link) | Disable it unless the Jetpack or WordPress app needs it |
| Info | `/llms.txt` returns 404 | Optional. Google ignores it. |

## Content quality: 80

**What works**
- H2s are phrased as the questions travellers actually ask, e.g. "How much does it cost to stay at Kambu Mara Camp?", "What are the Masai Mara entry fees in 2026?" and "Should you stay inside or outside the Masai Mara Reserve?".
- Pages give specific facts: tents from $45, campsite $15 per person, "12-15 minutes from Sekenani Gate", 9.4 from 251 Booking.com reviews, prices for the 3-day safari.
- Strong first-hand experience signals: the camp is local and owner-run, with its own guides and Land Cruisers.
- Main pages run to about 2,400–3,300 words each.

**Findings**
| Severity | Finding | Evidence |
|---|---|---|
| Medium | Overlap with the sister site kambucampers.com | Both sites have a 3-day Masai Mara safari page (`/3-day-masai-mara-safari/` here, `/3-day-masai-mara-budget-camping-safari/` there). kambucampers.com also has `/kambu-campers-mara-camp/`. They compete for the same searches. |
| Medium | Ratings differ between the two sites | This site says "9.4 from 251 Booking.com guests, 4.9 on Google". kambucampers.com's schema says "Kambu Campers Mara Camp", 4.8 from 412 reviews. Agree on one set of figures. |
| Low | The reviews page is very large | `/reviews/`: about 680 KB of HTML, about 41,000 words, 239 images. Paginate it, or load reviews in batches. |

## On-page SEO: 50

| Severity | Finding | Evidence |
|---|---|---|
| High | Homepage title is "Home" | `<title>Home</title>` |
| High | Titles are too long because the full site name is appended | Site title is "Kambu Mara Camp - Affordable Masai Mara Camping Accommodation Near Sekenani" (64 characters) |
| High | Scraped menu text used as meta description | The first description on each page begins "Skip to contentWhatsAppBook now…". A good description (from the theme) exists but comes third. |
| Medium | Short, generic og:title | og:title is "Home", "Tents", "3-day safari" |
| Info | H1s are good | e.g. "Tents by the Masai Mara Classic, Comfort and Family" and "3-Day Masai Mara safari From Nairobi, staying at Kambu Mara Camp" |

## Schema and structured data: 55

**What works:** The site has `Campground` markup with an address (Kambu Close, Sekenani, Narok County, 00517), map coordinates, phone number, priceRange "USD 15-220 per night" and 10 amenity features. `/tents/` describes 4 `Accommodation` types with bed details. FAQ and breadcrumb markup are present.

| Severity | Finding | Evidence |
|---|---|---|
| High | Three overlapping schema blocks | BeyondSEO outputs Organization, WebSite, WebPage and BreadcrumbList. A second block outputs an `Organization` whose `name` is empty (`"name": ""`). A third outputs WebSite, WebPage, BreadcrumbList and SearchAction. The theme outputs its own BreadcrumbList, WebPage and Campground. Result: 2 Organizations with different `@id` casing (`#organization` vs `#Organization`) and 3 BreadcrumbLists. |
| Medium | Organization name is the full tagline | "Kambu Mara Camp - Affordable Masai Mara Camping Accommodation Near Sekenani" |
| Medium | Campground markup is missing useful properties | No `image`, `sameAs` (Booking.com, Google Maps, TripAdvisor) or `checkinTime`/`checkoutTime`. Leave out `aggregateRating`: Google doesn't show star ratings for reviews a business shows about itself. |
| Low | FAQ markup won't produce rich results | Since 2023 Google shows FAQ rich results only for government and health sites. The markup is harmless; just don't expect it to show in search. |

## Performance (estimated, no field or lab data): 75

**What works:** 4 stylesheets and about 12 scripts per page, and none of the scripts block rendering in `<head>`. Images are WebP with `width` and `height` set, and below-the-fold images are lazy-loaded.

| Severity | Finding | Evidence |
|---|---|---|
| Medium | Large pages | Homepage about 200 KB of HTML, `/v2/` about 490 KB, `/reviews/` about 680 KB with 239 images |
| Low | Fonts load from two services | Fontshare and Google Fonts. Self-host them, or preload one family. |
| Action | Measure real Core Web Vitals | Run PageSpeed Insights or connect Search Console |

## Images: 85
- Pages checked: 0 images missing an `alt` attribute. 2 decorative images have `alt=""` (correct). Almost every image is WebP, and every one has width and height set.
- **There's no `og:image` on any page checked**, so links shared on WhatsApp, Facebook and similar get no preview picture. Add a default social image plus one per page.

## AI search readiness: 70
- Strengths: question-style headings, specific facts such as prices, distances and fees, and plain HTML.
- Gaps: the scraped descriptions confuse search and AI summaries, there's no og:image, the camp's name and ratings differ between the two Kambu sites, and there's no `sameAs` linking the site to its Booking.com and Google listings. llms.txt is optional.
