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

- Pillars are numbered by identity and presented in **publication order**, so the
  numbering is not sequential down the page.

Totals: **17 pillars, 606 pages.** Core = 88, Outer = 518.

Two pillars are large enough to live in their own files:

- **Pillar 8** — destination coverage, 322 pages →
  [`destination-taxonomy.md`](./destination-taxonomy.md)
- **Pillars 12–17** — cross-cutting sub-entities, 130 pages →
  [`sub-entity-pillars.md`](./sub-entity-pillars.md)

The conservation angle is applied across all 606 pages under the rules in
[`conservation-vector.md`](./conservation-vector.md).

---

## Root — the contextual domain

*Section: Core · Phase 1*

`/kenya-safari/` is the **structural parent of the entire site** and the page
that carries the commercial objective of ranking for the domain head term. It is
not a package page and it does not sit inside Pillar 3.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/kenya-safari/` | **Root hub** | `ItemList`, `FAQPage` | 1,4 | H |

It must do four things and nothing else: define the domain, route to all eleven
pillars, state the Kambu contextual vector (affordable comfort, low footprint)
in two sentences, and carry the decision framework a first-time visitor needs.

**It will not rank early, and that is expected.** The head term is won by the
aggregate coverage beneath it plus historical data — never by optimising the hub
itself. Do not iterate on this page while Core pillars are incomplete.

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

Responsible-tourism content is **not** a single trust page here — it is Pillar 11.

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
| `/kenya-safari-packages/` | Hub (child of root) | `ItemList` | — | H |
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

## Pillar 11 — Conservation and impact
*Section: Core · Phase 3*

Core, not Outer. Conservation is part of the source context, so it has to be
established as a property of the brand before the rest of the site references it.

**Publication gate:** no page in this pillar ships without a named partner, a
number, a date, a named project, or a photograph of the thing described. See
`source-context.md` §5, the unsubstantiated-claim rule. A pillar of unsupported
claims is worse than no pillar at all — legally, editorially and commercially.

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/conservation/` | **Cluster hub / impact charter** | `AboutPage` | 7 | M |
| `/conservation/wildlife/` | Evidence | — | 7 | H |
| `/conservation/community/` | Evidence | — | 7 | H |
| `/conservation/environment/` | Evidence | — | 7 | H |
| `/conservation/why-tented-camps-have-a-lower-footprint/` | **Argument** | `FAQPage` | 3,7 | M |
| `/conservation/shared-vehicles-and-wildlife-pressure/` | **Argument** | `FAQPage` | 4,7 | M |
| `/conservation/where-your-money-goes/` | Transparency | `FAQPage` | 1,2,7 | **H** |
| `/conservation/conservancy-fees-explained/` | Reference | — | 2,7 | **H** |
| `/conservation/our-team-and-local-employment/` | Evidence | — | 7 | M |
| `/conservation/local-sourcing-and-supply/` | Evidence | — | 7 | M |
| `/conservation/water-power-and-waste-at-camp/` | Evidence | — | 3,7 | M |
| `/conservation/responsible-safari-code/` | Guest conduct | `HowTo` | 7 | L |
| `/conservation/impact-report/` | **Dated report** | `Report` | 7 | **H** |

### The two argument pages carry the pillar

`/conservation/why-tented-camps-have-a-lower-footprint/` and
`/conservation/shared-vehicles-and-wildlife-pressure/` are the pages that convert
the conservation vector into a *commercial* argument rather than a virtue claim.
They connect directly to the accommodation ladder in Pillar 2 and the vehicle
cluster in Pillar 5:

- No concrete foundations, reversible siting, lower water demand, solar-viable
  load — a tented camp is the low-impact rung of the ladder.
- Fewer vehicles per guest lowers both emissions per guest and pressure at
  sightings, vehicle crowding being a documented welfare problem in the Mara.

`/conservation/where-your-money-goes/` is the highest-value page in the pillar
because it fuses conservation with the cost-transparency cluster in Pillar 4.
Nobody reselling product can write it.

`/conservation/impact-report/` must be dated and republished annually. An
undated impact report ages into a liability.

---

## Pillar 6 — Masai Mara ecosystem
*Section: Outer · Phase 4 · **expands to 40 pages***

The 14 pages below are the base. As the flagship (Tier A), the Mara also needs
its own sub-entity layer — 5 gates, 9 sectors and features, 6 conservancies,
enumerated in [`destination-taxonomy.md`](./destination-taxonomy.md) — bringing
the pillar to 40. Every other cluster on the site is measured against this one,
so it has to be the deepest.

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

## Pillar 8 — Kenyan destination coverage
*Section: Outer · Phase 6 · **322 pages** → [`destination-taxonomy.md`](./destination-taxonomy.md)*

**This pillar is what makes the head term reachable.** Six tiers, from the Mara
flagship down to remote parks that will never convert but without which the
domain is not covered:

| Tier | Scope | Depth | Count | Pages |
|---|---|---|---|---|
| A | Masai Mara — flagship | Pillars 1, 2, 6 | 1 | *(P6 → 40)* |
| B | Major parks | 16-page cluster | 7 | 112 |
| C | Secondary parks and reserves | 8-page cluster | 14 | 112 |
| D | Remote and specialist | 4-page cluster | 8 | 32 |
| E | Coast — extension-framed | 6-page cluster | 5 | 30 |
| F | Conservancies | 4-page cluster | 8 | 32 |
| — | Structural hubs | — | 4 | 4 |

Tier B: Amboseli · Tsavo East · Tsavo West · Samburu · Ol Pejeta · Lake Nakuru ·
**Nairobi National Park**.

All of it is hierarchical expansion — every destination is a genuine child of
`/kenya-safari/` and a genuine sibling of the Mara cluster — so it deepens the
site vector rather than widening it. Full templates, per-park named sub-entities
and the coast boundary are in the taxonomy file.

---

## Pillars 12–17 — Cross-cutting sub-entities
*Section: Outer · Phases 4–7 · **130 pages** → [`sub-entity-pillars.md`](./sub-entity-pillars.md)*

The destination taxonomy covers the domain **by place**. These pillars cover the
other axes searchers actually use, and they supply the site's richest internal
linking substrate.

| # | Pillar | Pages | Phase |
|---|---|---|---|
| 12 | Wildlife — species, events, behaviour | 48 | 5 |
| 13 | Ecosystems and landscapes | 12 | 6 |
| 14 | Activities and experiences | 16 | 5 |
| 15 | Timing and seasonality | 22 | 4 |
| 16 | Circuits and road routes | 14 | 6 |
| 17 | Traveller segments | 18 | 7 |

Pillar 12 was the largest gap in the previous draft — wildlife is the sub-entity
class most safari searches actually resolve to. Pillar 15 sits early because the
month pages route strongly into packages.

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
| 1 | Root, 0, 1, 2 | Core | 34 | Entity home indexed; camp cluster complete |
| 2 | 3, 4 | Core | 30 | All package + cost pages live and priced |
| 3 | 5, 11 | Core | 24 | Fleet cluster complete; every conservation claim evidenced |
| — | — | — | **88** | **Core complete. Only now start Outer.** |
| 4 | 6 (→40), 15 | Outer | 62 | Mara sub-entities complete; all 12 month pages substantively distinct |
| 5 | 7, 12, 14 | Outer | 78 | — |
| 6 | 8 (B, C, F), 13, 16 | Outer | 282 | Tier templates applied evenly — no partial clusters |
| 7 | 8 (D, E), 9, 17 | Outer | 85 | — |
| 8 | 10 | Outer | 11 | Coverage matrix run; remaining gaps recorded with reasons |
| — | — | — | **518** | Domain coverage complete |

**Phase 6 is the head-term phase.** It is the largest and least immediately
rewarding, which is why it sits after every monetizing cluster is live. Do not
part-build it: seven complete Tier B clusters beat fourteen partial ones,
because uneven coverage of a domain reads as an unfocused source.

### Scope discipline

606 pages is a multi-year programme, and the map is a **ceiling on scope, not a
production quota**. 600 thin pages rank worse than 150 substantive ones and
actively damage the site vector. Every page must clear the Core bar: it answers
a real question, contains at least one fact not on page one of the results, names
real places and numbers, and routes to a Kambu product or to a page that does.
A page that cannot clear it is a section of its parent.

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
