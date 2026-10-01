# Handoff: 10-day Kenya safari itinerary

Design-system pass · 1 October 2026 · source draft dated 15 September 2026

**Publication decision: Not approved yet.** The page is a complete reference
build, but two blockers remain (hero image files, Mara fee schedule for a
Sekenani-based stay) and the editorial drawer must come out before release.

## Page contract

```yaml
url: /10-day-kenya-safari-itinerary/ (proposed)
archetype: itinerary / planning guide (non-product)
dominant_intent: plan a ten-day Kenya safari route and judge its pace
primary_query: kenya itinerary 10 days / 10 day kenya safari itinerary
searcher: first-time visitor with ten days including flights
journey_stage: plan
parent_hub: /kenya-safari/ (root hub; final URL unconfirmed)
explicit_exclusions:
  - live package prices -> product pages (e.g. /8-day-kenya-budget-safari/)
  - Kenya + Tanzania routes -> separate cross-border plan (no URL yet)
  - full Mara destination guide -> /masai-mara-national-reserve/
commercial_destination: tailored quotation via bookings@kambucampers.com
advice_moments: [packed lunch vs camp lunch on Mara days]
experience_credential: Mara driver-guides based at Kambu Mara Camp; camp ~9 km before Sekenani Gate
information_gain: separates arrival, transfer and full viewing days; counts admission days apart from nights; gives both overnight allocations side by side
last_reviewed: 2026-09-15 (facts); 2026-10-01 (camp distance)
```

> This page helps a first-time visitor with ten days choose how to spend nine
> nights across Amboseli, Naivasha and the Mara, while routing live prices to
> product pages and cross-border trips to a separate plan.

## Interaction blueprint

| Field | Decision |
|---|---|
| Primary interaction | Route-version tabs (balanced / wildlife-intensive) on the at-a-glance table |
| Supporting | Sidebar tabs for the four variations; FAQ accordion; camp-tent gallery with lightbox |
| Navigation aid | Sidebar section tracker, reading-progress line, day-to-day navigation, copy-link anchors |
| Conversion | One destination: tailored quotation (`#plan`), reached from the header, the planning card and the prose |
| First layer (always visible) | Direct answer, nine-night allocation, scope note, balanced day table, both allocations in the alternatives table, fees, travel times |
| Behind interaction | The wildlife-intensive day table (also summarised in prose and the alternatives table); variation detail; FAQ answers after the first |
| Rejected | Collapsing day sections into accordions (they are the page's core content); a cost calculator (no verified package rates); an interactive map (no verified route geometry for all legs) |
| Analytics | `tab_select`, `disclosure_open`, `gallery_open`, `gallery_nav`, `copy_section_link`, `scroll_depth_25/50/75/90` |

## What changed from the supplied draft

| Change | Why |
|---|---|
| Kambu Mara Camp "approximately 8 kilometres from Sekenani Gate" → "about 9 km before Sekenani Gate on the road from Narok" | kambu-brand-voice records ~9.0 km and lists the 8 km figure as wrong |
| "guide" → "driver-guide" where the person drives and guides (Days 2, 7, 8; cost and transport tables) | Brand-voice terminology |
| "reserve" → "the Reserve" for the Masai Mara National Reserve | Brand-voice terminology |
| First paragraph styled as `.kg-answer` | Direct answer is the first layer |
| Route-version tabs with a new wildlife-intensive day table | The draft's brief asked for this toggle; both allocations stay visible in the alternatives table |
| Day-to-day navigation on Days 1–10 | Long day-by-day section |
| Gallery of four Kambu Mara Camp photos (own photos, Drive) | Shows what "furnished tent accommodation" means; replaces a citation link |
| Alternatives rebuilt as sidebar tabs with fact grids, plus a Choose A / Choose B rule | Four parallel alternatives with sub-labels |
| Suits / choose-something-else split | Brand-voice web convention |
| One field note (packed lunch vs camp lunch) carrying the only entity-home link | Experience credential at the page's judgement call; replaces two bare "Kambu Campers" citation links |
| FAQ turned into an accordion and an eighth question added ("Can I leave for Amboseli on the day I land?") | FAQ convention; the answer restates the page's own Day 1 logic |
| Graded sources register and last-reviewed line | Evidence standard |
| Sidebar shortcuts extended from four to eight and made to track the section in view | Wayfinding on a long page |
| JSON-LD `Article` + `BreadcrumbList` | Mirrors visible content only |

## Sources

All retained from the draft; not re-fetched on 1 October 2026 (the build
environment blocks most external hosts). Grades as printed on the page.

| Grade | Source | Supports |
|---|---|---|
| B | KWS: Amboseli National Park | gates, habitats, visitor guidance, US$90 |
| B | KWS: Hell's Gate National Park | activities, US$50 |
| B | KWS: Lake Nakuru National Park | rhino role |
| B | Mara Conservancy: wildebeest migration | migration variability; seasonal fee schedule |
| B | Magical Kenya: Maasai Mara | ballooning as an activity |
| B | KMD: State of the Climate 2024 | rainy seasons |
| C | Sheldrick Wildlife Trust: nursery visit | 11 a.m.–noon visiting hour |
| C | Safarilink: baggage allowance | 15 kg including hand baggage |
| D | Roadtrip Africa: Roads, Rails and Waves | ~8 h Naivasha–Amboseli; ~4½ h Sekenani–Naivasha |
| D | SafariBookings: 10-day Kenya tours | from about US$2,500 per person benchmark |
| S | xo, Kelly Chen trip report | one traveller's experience |
| K | Kambu Campers: Mara access, day trips; kambu-brand-voice | 5–6 h Nairobi–Mara; 4–4½ h Nairobi–Amboseli; camp ~9 km before Sekenani |

## Credentials used

| Where | Claim | Charter line |
|---|---|---|
| Day 7 field note | Kambu's Mara driver-guides are based at Kambu Mara Camp, not in Nairobi | experience_basis.how_they_know[0] |
| Day 7 field note | Camp ~9 km before Sekenani Gate; returning to camp between drives can cost up to an hour | experience_basis.based_where, operating_facts[1] |
| Day 7 field note | We cannot promise what that hour would have turned into | the page's explicit refusal |

## Photographs

Four Kambu Mara Camp photos from Drive (folder of camp photos uploaded 15 Sep
2026), all opened and checked: genuine phone photos, no people, no other
branding, no GPS data. Converted to WebP at 400/800/1200 (smaller originals
not upscaled); the lounge photo was cropped to remove a post and a blurred
foreground. Rejected: a sideways duplicate of the doorway photo and two
low-resolution images (512 px and 384 px wide).

## Open items

1. **Hero image files missing**: `assets/amboseli-elephants-400.webp` and
   `-800.webp` from the original draft (Amoghavarsha JS, CC BY-SA 3.0,
   Wikimedia Commons). Add them to `assets/`; the checker fails until then.
2. **Mara fee schedule**: Sekenani is a Narok County gate, but the fee row
   cites the Mara Conservancy (Mara Triangle) schedule. Confirm which schedule
   applies to a Sekenani-based stay and link the fee-schedule page itself.
3. **Re-check dated facts** (fees, Safarilink allowance, nursery hour, travel
   times) before publication; update the last-reviewed line only after that.
4. **Parent hub URL** `/kenya-safari/` and the broader Kenya itineraries guide
   are unconfirmed; no link added until they exist.
5. **Crescent Island** description still has no separate source.
6. Remove the editorial drawer and `noindex` at publication.

## Checker result (1 October 2026)

`check_guide.py`: 37 pass, 1 warn (editorial drawer present), 1 fail (hero
image files missing). Rendered at 1440 px and 390 px in Chromium: no
horizontal scroll; tabs, sidebar tabs (keyboard included), gallery arrows,
lightbox (arrows, Esc, focus return), FAQ, deep links into closed panels,
section tracker and progress bar all work; with JavaScript off every tab
panel is visible.
