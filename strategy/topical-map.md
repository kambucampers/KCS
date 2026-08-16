# Kambu Campers — Topical Map

Derived from [`source-context.md`](./source-context.md). Do not add pages to this
map without testing them against the Central Search Intent:

> Help a traveller who wants genuine comfort but not lodge prices to understand,
> compare, price, and book a permanent-tented-camp safari — primarily in the
> Masai Mara.

**Central entity:** the permanent tented camp safari.
**Dominant contextual domain:** Masai Mara.

---

## How to read this document

- **Section** — Core carries monetization and defines source context. Outer
  builds historical data and relevance, and routes authority back to Core.
- **Phase** — publication order. **Complete every Core phase before starting
  Outer.** An unfinished core alongside a sprawling outer section reads as an
  unfocused source and depresses site focus.
- **IG** — the information-gain asset the page must draw on (numbered per
  charter §7). Pages with no IG marker are structural or definitional.
- **Freshness** — H = high volatility, review quarterly. M = annually. L = static.

Totals: **9 pillars, 94 pages.** Core = 46, Outer = 48.

---

## Pillar 0 — Entity home and trust
*Section: Core · Phase 1*

Establishes source context before any commercial page is crawled. Ship first.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/about-us/` | **Entity home** | `Organization` + `@id` + `sameAs` | 5 | M |
| `/about-us/our-story/` | Narrative | `AboutPage` | 5 | L |
| `/about-us/team-and-guides/` | People | `Person` × n | 5 | M |
| `/about-us/licensing-and-registration/` | Trust | — | — | M |
| `/reviews/` | Aggregated proof | `Review`, `AggregateRating` | 6 | H |
| `/contact/` | Transactional | `ContactPoint` | — | L |
| `/booking-and-payment/` | Transactional | — | — | M |
| `/cancellation-policy/` | Trust | — | — | M |
| `/travel-insurance/` | Trust | — | — | M |
| `/responsible-tourism/` | Trust | — | 5 | L |

---

## Pillar 1 — Kambu Mara Camp (owned asset)
*Section: Core · Phase 1*

The most defensible cluster on the site. Kambu Mara Camp is a distinct
sub-entity — treat it as such. **Never use stock photography here.**

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/kambu-mara-camp/` | **Cluster hub** | `Campground`/`LodgingBusiness` | 1,3 | H |
| `/kambu-mara-camp/tents/` | Product detail | `Accommodation` | 3 | M |
| `/kambu-mara-camp/rates/` | Commercial | `Offer` | 1 | **H** |
| `/kambu-mara-camp/dining/` | Attribute | — | 3 | M |
| `/kambu-mara-camp/facilities/` | Attribute | `amenityFeature` | 3 | M |
| `/kambu-mara-camp/location-and-directions/` | Operational | `Place`, `GeoCoordinates` | 4 | H |
| `/kambu-mara-camp/gallery/` | Proof | `ImageObject` | 3 | M |
| `/kambu-mara-camp/families-and-groups/` | Segment | — | 6 | M |
| `/kambu-mara-camp/couples-and-honeymoon/` | Segment | — | 6 | M |
| `/kambu-mara-camp/accessibility/` | Attribute | — | 3 | L |
| `/kambu-mara-camp/wifi-and-power/` | Attribute | — | 3 | M |
| `/kambu-mara-camp/a-day-at-camp/` | Experience | — | 4,6 | L |

**Linking rule:** every page in Pillars 2 and 3 links to `/kambu-mara-camp/`
within the first screen.

---

## Pillar 2 — The accommodation ladder (the wedge)
*Section: Core · Phase 1*

The comparison spine. This pillar is where the source context is argued, and it
is the single biggest differentiator the site has. Write it honestly — the
comparison only works because it is accurate.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/safari-accommodation-kenya/` | **Definitional hub** | `FAQPage` | 1 | M |
| `/what-is-a-permanent-tented-camp/` | Definitional | — | 3 | L |
| `/glamping-safari-kenya/` | Alias surface | — | 1,3 | M |
| `/tented-camp-vs-lodge/` | Comparison | `FAQPage` | 1 | M |
| `/tented-camp-vs-budget-camping/` | Comparison | `FAQPage` | 1 | M |
| `/mid-range-safari-kenya/` | Positioning | — | 1 | M |
| `/en-suite-safari-tents/` | Attribute | — | 3 | L |
| `/is-glamping-safe-in-the-masai-mara/` | Objection | `FAQPage` | 4,6 | L |
| `/what-a-safari-tent-actually-looks-like/` | Proof | `ImageObject` | 3 | L |
| `/glamping-vs-luxury-camp/` | Comparison | — | 1 | M |
| `/best-tented-camps-masai-mara/` | Commercial comparison | `ItemList` | 1,4 | H |
| `/safari-comfort-checklist/` | Decision tool | — | 6 | L |

---

## Pillar 3 — Safari packages
*Section: Core · Phase 2*

Primary monetization. One page per **genuinely distinct product**, never per
keyword variant. If two durations produce the same itinerary logic, merge them
and use a table.

### Masai Mara core

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/masai-mara-safari-packages/` | **Cluster hub** | `ItemList` | 6 | H |
| `/2-day-masai-mara-safari/` | Product (resident/weekend) | `TouristTrip`,`Offer` | 6 | H |
| `/3-day-masai-mara-safari/` | Product | `TouristTrip`,`Offer` | 6 | H |
| `/4-day-masai-mara-safari/` | Product | `TouristTrip`,`Offer` | 6 | H |
| `/5-day-masai-mara-safari/` | Product | `TouristTrip`,`Offer` | 6 | H |
| `/masai-mara-migration-safari/` | Seasonal product | `TouristTrip` | 4,6 | **H** |

### Multi-park Kenya

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/kenya-safari-packages/` | Hub | `ItemList` | — | H |
| `/masai-mara-lake-nakuru-safari/` | Product | `TouristTrip` | 6 | H |
| `/masai-mara-naivasha-safari/` | Product | `TouristTrip` | 6 | H |
| `/6-day-kenya-safari/` | Product | `TouristTrip` | 6 | H |
| `/7-day-kenya-safari/` | Product | `TouristTrip` | 6 | H |
| `/10-day-kenya-safari/` | Product | `TouristTrip` | 6 | H |
| `/amboseli-masai-mara-safari/` | Product | `TouristTrip` | 6 | H |

### Segment pages

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/private-vs-group-joining-safari/` | Decision | `FAQPage` | 6 | M |
| `/solo-traveller-safari-kenya/` | Segment | — | 6 | M |
| `/family-safari-kenya/` | Segment | — | 6 | M |
| `/honeymoon-safari-kenya/` | Segment | — | 6 | M |
| `/photography-safari-kenya/` | Segment | — | 6 | M |
| `/small-group-safari-kenya/` | Segment | — | 6 | M |
| `/custom-safari-planning/` | Conversion | — | 6 | L |

---

## Pillar 4 — Cost and pricing transparency
*Section: Core · Phase 2*

The highest information-gain cluster on the site. Kambu can publish real numbers
because it owns the cost base. Competitors quoting resold product cannot.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/masai-mara-safari-cost/` | **Cluster hub** | `FAQPage` | 1,2 | **H** |
| `/kenya-safari-cost-per-day/` | Breakdown | — | 1,2 | **H** |
| `/masai-mara-park-fees/` | Reference | — | 2 | **H** |
| `/whats-included-in-a-safari-price/` | Transparency | `FAQPage` | 1 | M |
| `/cheap-safari-vs-affordable-safari/` | Objection | — | 1,6 | M |
| `/hidden-costs-on-safari/` | Trust | `FAQPage` | 1,6 | M |
| `/single-supplement-explained/` | Detail | — | 1 | M |
| `/tipping-on-safari-kenya/` | Practical | `FAQPage` | 4 | M |
| `/low-season-vs-high-season-pricing/` | Commercial | — | 1 | H |
| `/how-to-budget-for-a-kenya-safari/` | Planning tool | — | 1,6 | M |

---

## Pillar 5 — Vehicles, transport and self-drive
*Section: Core · Phase 3*

Second revenue line, second audience. Keep every page tied to the tented-camp
central entity — vehicle hire is *how you reach the camp*, not a separate business.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/safari-vehicle-hire-kenya/` | **Cluster hub** | `Service`,`Offer` | 1,5 | H |
| `/4x4-land-cruiser-hire/` | Product | `Vehicle`,`Offer` | 3,5 | H |
| `/safari-minivan-vs-land-cruiser/` | Decision | `FAQPage` | 4,5 | M |
| `/campervan-hire-kenya/` | Product ("Cheyat") | `Vehicle`,`Offer` | 3,5 | H |
| `/self-drive-safari-kenya/` | Segment | — | 4 | M |
| `/camping-gear-hire/` | Product | `Offer` | 1,3 | M |
| `/nairobi-to-masai-mara-road/` | **Operational** | `FAQPage` | **4** | **H** |
| `/flying-vs-driving-to-masai-mara/` | Decision | `FAQPage` | 4 | H |
| `/masai-mara-airstrips/` | Reference | `Place` | 4 | M |
| `/jkia-airport-transfers/` | Service | `Service` | — | M |
| `/driving-in-kenya-for-visitors/` | Practical | — | 4 | M |

`/nairobi-to-masai-mara-road/` is the single strongest information-gain page on
the site. Kambu drives that road weekly; almost nobody ranking for it does.
Update the road-condition section by date and show the date.

---

## Pillar 6 — Masai Mara ecosystem
*Section: Outer · Phase 4*

**Cross-domain caution:** masaimara.ke owns broad informational destination
coverage. Every page here must carry an operator angle — first-hand observation,
operational consequence, or a booking decision — or it does not belong on this
domain.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/masai-mara/` | Hub (operator framing) | `Place` | 4 | M |
| `/best-time-to-visit-masai-mara/` | Planning | `FAQPage` | 4,6 | M |
| `/wildebeest-migration-timing/` | Planning | — | 4 | **H** |
| `/masai-mara-gates/` | Operational | `Place` × n | 4 | H |
| `/sekenani-gate/` | Operational | `Place` | 4 | H |
| `/conservancies-vs-national-reserve/` | Decision | `FAQPage` | 4 | M |
| `/masai-mara-weather-by-month/` | Planning | — | 4 | M |
| `/big-five-in-the-masai-mara/` | Wildlife | — | 4 | L |
| `/what-happens-on-a-game-drive/` | Experience | — | 4,6 | L |
| `/night-game-drives-and-walking-safaris/` | Activity | — | 4 | M |
| `/balloon-safari-masai-mara/` | **Upsell** | `Offer` | 1 | H |
| `/maasai-village-visit/` | **Upsell** | `Offer` | 1 | M |
| `/mara-river-crossings/` | Wildlife | — | 4 | H |
| `/is-the-masai-mara-worth-it/` | Objection | `FAQPage` | 6 | L |

---

## Pillar 7 — Preparation and practical
*Section: Outer · Phase 5*

Builds historical data and answers pre-booking anxiety. Every page routes back
to Pillar 1 or 3.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/safari-planning-guide/` | **Cluster hub** | — | 6 | M |
| `/what-to-pack-for-a-safari/` | Practical | `ItemList` | 6 | L |
| `/safari-clothing-and-colours/` | Practical | — | 4 | L |
| `/kenya-eta-and-entry-requirements/` | Reference | `FAQPage` | — | **H** |
| `/vaccinations-and-malaria-kenya/` | Health | `FAQPage` | — | M |
| `/safety-on-safari/` | Objection | `FAQPage` | 4,6 | M |
| `/staying-connected-wifi-and-power/` | Practical | — | 3 | M |
| `/dietary-requirements-on-safari/` | Practical | — | 6 | L |
| `/travelling-with-children-on-safari/` | Segment | `FAQPage` | 6 | L |
| `/safari-photography-tips/` | Practical | — | 4 | L |
| `/money-and-payments-in-kenya/` | Practical | — | — | M |
| `/what-to-expect-first-safari/` | Reassurance | — | 6 | L |
| `/laundry-showers-and-toilets-at-camp/` | Objection | `FAQPage` | 3 | L |
| `/electricity-and-charging-on-safari/` | Practical | — | 3 | L |

---

## Pillar 8 — Other Kenyan circuits
*Section: Outer · Phase 6*

Tented-camp framed only. These extend the central entity geographically; they do
not introduce a new one. Each page must state the accommodation class used.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/kenya-safari-circuits/` | Hub | `ItemList` | — | M |
| `/amboseli-safari/` | Destination product | `TouristTrip` | 6 | H |
| `/tsavo-east-and-west-safari/` | Destination product | `TouristTrip` | 6 | H |
| `/lake-nakuru-safari/` | Destination product | `TouristTrip` | 6 | H |
| `/lake-naivasha-and-hells-gate/` | Destination product | `TouristTrip` | 6 | H |
| `/samburu-safari/` | Destination product | `TouristTrip` | 6 | H |
| `/ol-pejeta-conservancy/` | Destination product | `TouristTrip` | 6 | H |
| `/aberdares-and-mount-kenya/` | Destination product | `TouristTrip` | 6 | M |
| `/safari-and-beach-kenya/` | Extension — **one page only** | `TouristTrip` | 6 | M |

`/safari-and-beach-kenya/` is a deliberate single-page exception. Do **not**
expand it into a Diani/Watamu/Mombasa cluster — that is a different central
entity and it will widen the site vector.

---

## Pillar 9 — Tanzania bridge
*Section: Outer · Phase 7 · **HARD CAP: 5 pages***

Admissible only because the Mara and Serengeti are one ecosystem and the
migration crosses it. Every page must be framed as an **extension of a Kenyan
itinerary**. If the itinerary does not start in Kenya, it does not get published.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/masai-mara-serengeti-safari/` | **Bridge hub** | `TouristTrip` | 6 | H |
| `/mara-vs-serengeti/` | Comparison | `FAQPage` | 4,6 | M |
| `/isebania-border-crossing/` | Operational | `FAQPage` | 4 | **H** |
| `/ngorongoro-crater-extension/` | Add-on product | `TouristTrip` | 6 | H |
| `/tanzania-park-fees-and-costs/` | Reference | — | 2 | **H** |

---

## Pillar 10 — Decision and comparison
*Section: Outer · Phase 8*

Bottom-funnel. Publish last, once the Core is complete and the site has
established what kind of source it is.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/kenya-vs-tanzania-safari/` | Comparison | `FAQPage` | 4 | M |
| `/how-to-choose-a-safari-operator/` | Decision | `FAQPage` | 6 | M |
| `/questions-to-ask-before-booking/` | Decision | `FAQPage` | 6 | L |
| `/booking-direct-vs-through-an-agent/` | Positioning | — | 1,6 | M |
| `/common-safari-booking-mistakes/` | Trust | — | 6 | M |

---

## Publication order

| Phase | Pillars | Section | Pages | Gate to proceed |
|---|---|---|---|---|
| 1 | 0, 1, 2 | Core | 34 | Entity home indexed; camp cluster complete |
| 2 | 3, 4 | Core | 30 | All package + cost pages live and priced |
| 3 | 5 | Core | 11 | Fleet cluster complete |
| — | — | — | — | **Core complete. Only now start Outer.** |
| 4 | 6 | Outer | 14 | — |
| 5 | 7 | Outer | 14 | — |
| 6 | 8 | Outer | 9 | — |
| 7 | 9 | Outer | 5 | — |
| 8 | 10 | Outer | 5 | — |

Do not interleave. The most common failure mode in this framework is publishing
attractive Outer content — migration guides, packing lists — before the Core
exists, which trains the site vector on informational content the business
cannot monetize.

---

## Internal linking rules

1. Every Outer page links **up** to its Core parent within the first screen.
2. Every Pillar 2 page links to `/kambu-mara-camp/` and to
   `/masai-mara-safari-packages/`.
3. Every package page links to the camp cluster, the relevant cost page, and at
   least one comparison page in Pillar 2.
4. Hubs link **down** to every child. Children link **across** only where the
   comparison is genuinely useful to a reader.
5. Anchor text uses the canonical entity term, not rotated synonyms.
6. No reciprocal links to sibling domains for ranking purposes. Cross-domain
   links only where they materially help the reader.

---

## Volatility register

Review on a fixed cadence and stamp the page with a visible review date:

- **Quarterly (H):** all rates, park fees, migration timing, road condition,
  border-crossing procedure, eTA requirements, `/reviews/`
- **Annually (M):** itineraries, facilities, comparison tables, seasonality
- **On change only (L):** definitional and experiential content

---

## Open items

1. Validate against Search Console and Ahrefs once API units reset — the map is
   derived from the business model, not from current rankings. Expect to merge
   or split 5–10 pages after that check.
2. Confirm the exact sibling-domain inventory and agree the topic split with
   masaimara.ke before Phase 4 begins.
3. Confirm Kambu Mara Camp tent count, tent classes and current rack rates
   before Phase 1 ships.
4. Decide whether campervan hire warrants its own subdomain or stays in Pillar 5.
   Recommendation: keep it in Pillar 5 — it shares the audience and splitting it
   would fragment the site vector.
