# Kambu Campers — Topical Map

Derived from [`source-context.md`](./source-context.md). Conservation is applied
across every page under [`conservation-vector.md`](./conservation-vector.md).

Do not add pages without testing them against the Central Search Intent:

> Help a traveller who wants genuine comfort but not lodge prices to understand,
> compare, price, and book a permanent-tented-camp safari — primarily in the
> Masai Mara — from an operator whose footprint they can verify.

**Central entity:** the permanent tented camp safari.
**Contextual domain:** Kenya safari. **Dominant sub-domain:** Masai Mara.

**Total: 250 pages. Core = 85, Outer = 165.**

---

## What the 250-page cap changes

The map was drafted at 606 pages for full domain coverage. Capped at 250, the
strategy has to change — not just shrink. Cutting 60% evenly would have produced
thin coverage of everything, which is the worst available outcome: it widens the
site vector without deepening any part of it.

**The cut is therefore depth-preserving and breadth-sacrificing.**

| Kept whole | Cut hard | Cut entirely |
|---|---|---|
| All Core pillars (85) | Destination coverage 322 → 62 | Tier D remote parks (32) |
| Mara flagship depth | Wildlife 48 → 16 | Tier F conservancy clusters (32) |
| Month-by-month timing | Traveller segments 18 → 6 | Coast clusters 30 → 2 |
| Road-route information gain | Ecosystems 12 → 4 | Per-park 16-page template → 7 |

### The honest consequence for "Kenya safari"

**At 250 pages you will not win the head term.** SafariBookings, TourRadar and
the established operators cover that domain at four figures. Chasing it at this
scale means losing on both counts — too thin for the head term, too diffuse to
own anything else.

What 250 pages *can* win, and win properly:

- `masai mara camping safari`, `budget masai mara safari`, `tented camp masai mara`
- the accommodation-ladder cluster in full — nobody owns it
- `masai mara safari cost` and the whole cost-transparency cluster
- the Tier B park × cost × accommodation long tail
- the road-route and operational queries nobody with real data competes for

`/kenya-safari/` stays as the root hub because the hierarchy needs a parent and
it consolidates the site. Treat ranking for it as a **year-three byproduct**, not
a target. Revisit the cap before treating it as an objective.

---

## How to read this document

- **Section** — Core carries monetization and defines source context. Outer
  builds historical data and routes authority back to Core.
- **Phase** — publication order. **Complete every Core phase before starting
  Outer.**
- **IG** — information-gain asset per `source-context.md` §7.
- **Fresh** — H = review quarterly, M = annually, L = on change.

---

# CORE — 85 pages

## Root — the contextual domain
*Phase 1 · 1 page*

| URL | Page type | Schema | IG | Fresh |
|---|---|---|---|---|
| `/kenya-safari/` | **Root hub** | `ItemList`, `FAQPage` | 1,4 | H |

Structural parent of every pillar. Defines the domain, routes to all pillars,
states the contextual vector in two sentences. Do not iterate on it while Core
is incomplete.

## Pillar 0 — Entity home and trust
*Phase 1 · 9 pages*

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

## Pillar 1 — Kambu Mara Camp
*Phase 1 · 12 pages*

The most defensible cluster on the site. A distinct sub-entity, not a page
section. **Never stock photography.**

`/kambu-mara-camp/` (hub, `Campground`/`LodgingBusiness`) · `/tents/` ·
`/rates/` · `/dining/` · `/facilities/` · `/location-and-directions/` ·
`/gallery/` · `/families-and-groups/` · `/couples-and-honeymoon/` ·
`/accessibility/` · `/wifi-and-power/` · `/a-day-at-camp/`

## Pillar 2 — The accommodation ladder
*Phase 1 · 12 pages*

The comparison spine, and the biggest differentiator the site has. Rung 3 is the
only rung that profits from the ladder being explained accurately.

`/safari-accommodation-kenya/` (definitional hub) ·
`/what-is-a-permanent-tented-camp/` · `/glamping-safari-kenya/` ·
`/tented-camp-vs-lodge/` · `/tented-camp-vs-budget-camping/` ·
`/mid-range-safari-kenya/` · `/en-suite-safari-tents/` ·
`/is-glamping-safe-in-the-masai-mara/` · `/what-a-safari-tent-actually-looks-like/` ·
`/glamping-vs-luxury-camp/` · `/best-tented-camps-masai-mara/` ·
`/safari-comfort-checklist/`

## Pillar 3 — Safari packages
*Phase 2 · 18 pages*

One page per **genuinely distinct product**, never per keyword variant.

**Mara (6):** `/masai-mara-safari-packages/` (hub) · `/2-day-` · `/3-day-` ·
`/4-day-` · `/5-day-masai-mara-safari/` · `/masai-mara-migration-safari/`

**Multi-park (6):** `/kenya-safari-packages/` (hub) ·
`/masai-mara-lake-nakuru-safari/` · `/masai-mara-naivasha-safari/` ·
`/amboseli-masai-mara-safari/` · `/7-day-kenya-safari/` · `/10-day-kenya-safari/`

**Segments (6):** `/private-vs-group-joining-safari/` · `/solo-traveller-safari-kenya/` ·
`/family-safari-kenya/` · `/honeymoon-safari-kenya/` · `/small-group-safari-kenya/` ·
`/custom-safari-planning/`

*Cut from 20: 6-day Kenya safari (merged into 7-day) and photography safari
(now a Pillar 17 segment page).*

## Pillar 4 — Cost and pricing transparency
*Phase 2 · 10 pages*

Highest-IG cluster on the site. Kambu can publish real numbers because it owns
the cost base.

`/masai-mara-safari-cost/` (hub) · `/kenya-safari-cost-per-day/` ·
`/masai-mara-park-fees/` · `/whats-included-in-a-safari-price/` ·
`/cheap-safari-vs-affordable-safari/` · `/hidden-costs-on-safari/` ·
`/single-supplement-explained/` · `/tipping-on-safari-kenya/` ·
`/low-season-vs-high-season-pricing/` · `/how-to-budget-for-a-kenya-safari/`

## Pillar 5 — Vehicles, transport and self-drive
*Phase 3 · 11 pages*

`/safari-vehicle-hire-kenya/` (hub) · `/4x4-land-cruiser-hire/` ·
`/safari-minivan-vs-land-cruiser/` · `/campervan-hire-kenya/` ·
`/self-drive-safari-kenya/` · `/camping-gear-hire/` ·
**`/nairobi-to-masai-mara-road/`** · `/flying-vs-driving-to-masai-mara/` ·
`/masai-mara-airstrips/` · `/jkia-airport-transfers/` ·
`/driving-in-kenya-for-visitors/`

`/nairobi-to-masai-mara-road/` is the strongest single information-gain page on
the site. Date-stamp the road-condition section and show the date.

## Pillar 11 — Conservation and impact
*Phase 3 · 12 pages*

**Publication gate:** no page ships without a named partner, a number, a date, a
named project, or a photograph. See `source-context.md` §5.

`/conservation/` (hub) · `/wildlife/` · `/community/` · `/environment/` ·
**`/why-tented-camps-have-a-lower-footprint/`** ·
**`/shared-vehicles-and-wildlife-pressure/`** · **`/where-your-money-goes/`** ·
`/conservancy-fees-explained/` · `/our-team-and-local-employment/` ·
`/water-power-and-waste-at-camp/` · `/responsible-safari-code/` ·
`/impact-report/`

The three bold pages carry the pillar — they convert the conservation vector
into a commercial argument rather than a virtue claim. `/where-your-money-goes/`
fuses conservation with cost transparency; no reseller can write it.

*Cut from 13: local sourcing merged into `/community/`.*

---

# OUTER — 165 pages

## Pillar 6 — Masai Mara ecosystem and sub-entities
*Phase 4 · 26 pages*

The flagship. Every other cluster is measured against this one, so it stays the
deepest thing on the site. Operator angle required on every page — masaimara.ke
owns broad informational destination coverage.

**Base (14):** `/masai-mara/` · `/best-time-to-visit-masai-mara/` ·
`/wildebeest-migration-timing/` · `/masai-mara-gates/` ·
`/conservancies-vs-national-reserve/` · `/masai-mara-weather-by-month/` ·
`/big-five-in-the-masai-mara/` · `/what-happens-on-a-game-drive/` ·
`/night-game-drives-and-walking-safaris/` · `/balloon-safari-masai-mara/` ·
`/maasai-village-visit/` · `/mara-river-crossings/` ·
`/is-the-masai-mara-worth-it/` · `/masai-mara-map-and-sectors/`

**Gates (5):** Sekenani · Talek · Oloololo · Musiara · Sand River

**Features (4):** Mara Triangle · Musiara Marsh · Mara River · Oloololo Escarpment

**Conservancies (3):** Mara North · Naboisho · Olare Motorogi

Each gate page: where it is, what it accesses, which itineraries use it, drive
time from Nairobi and from camp, current road condition.

## Pillar 15 — Timing and seasonality
*Phase 4 · 13 pages*

`/best-time-for-a-kenya-safari/` (hub) + `/kenya-safari-in-{month}/` × 12.

High intent, evergreen, routes strongly into packages — which is why it sits
early. Each month page covers weather, wildlife, crowds, price, which parks are
at their best, and what Kambu recommends booking.

**These must differ substantively.** If January and February say the same thing,
one of them should not exist. This is the cluster most likely to be produced as
interchangeable filler.

## Pillar 7 — Preparation and practical
*Phase 5 · 12 pages*

`/safari-planning-guide/` (hub) · `/what-to-pack-for-a-safari/` ·
`/safari-clothing-and-colours/` · `/kenya-eta-and-entry-requirements/` ·
`/vaccinations-and-malaria-kenya/` · `/safety-on-safari/` ·
`/staying-connected-wifi-and-power/` · `/travelling-with-children-on-safari/` ·
`/safari-photography-tips/` · `/money-and-payments-in-kenya/` ·
`/what-to-expect-first-safari/` · `/laundry-showers-and-toilets-at-camp/`

## Pillar 12 — Wildlife
*Phase 5 · 16 pages*

The sub-entity class most safari searches resolve to. Cut from 48 by grouping
rather than by dropping coverage — the northern specials and the smaller
predators become grouped pages instead of one each.

`/wildlife/` (hub) · lion · leopard · elephant · buffalo · rhino (black and
white) · cheetah · giraffe · zebra · hippo · wild dog ·
`/northern-kenya-special-five/` (Grevy's zebra, reticulated giraffe, gerenuk,
beisa oryx, Somali ostrich) · `/wildebeest-migration/` · `/calving-season/` ·
`/flamingos-and-rift-valley-birds/` · **`/northern-white-rhino-ol-pejeta/`**

Species page template: what it is → where in Kenya, with named parks linked →
**best park and best month to see it** → conservation status → how Kambu's
itineraries reach it.

The northern white rhino page keeps its own URL despite the cut. Two animals, a
globally covered story, and you can drive guests to them — the strongest
available bridge between wildlife content and the conservation vector.

## Pillar 8 — Kenyan destination coverage
*Phase 6 · 62 pages*

Cut from 322. Tier D (remote parks) and Tier F (conservancy clusters) are
dropped entirely; the Tier B template drops from 16 pages to 7.

### Structural (2)
`/kenya-national-parks/` · `/kenya-safari-circuits/`

### Tier B — major parks: 7 × 7 = 49

**Amboseli · Tsavo East · Tsavo West · Lake Nakuru · Samburu · Ol Pejeta ·
Nairobi National Park**

Template: `/{park}/` · `/cost/` · `/best-time-to-visit/` · `/wildlife/` ·
`/where-to-stay/` · `/getting-there/` · `/things-to-do/`

Park fees fold into `/cost/`. Sectors and map fold into the hub. Tsavo East and
West stay split — distinct wildlife, access and character.

**Named sub-entities are mandatory** — they are what separates depth from
enumeration:

- **Amboseli** — Observation Hill, Enkongo Narok and Longinye swamps, big
  tuskers, Kilimanjaro views
- **Tsavo East** — Aruba Dam, Mudanda Rock, Lugard Falls, Yatta Plateau, red
  elephants
- **Tsavo West** — Mzima Springs, Shetani lava flow, Ngulia Rhino Sanctuary
- **Lake Nakuru** — Baboon Cliff, Makalia Falls, flamingo, Rothschild's giraffe,
  both rhino species
- **Samburu** — Ewaso Ng'iro River, Ololokwe, the Samburu Special Five
- **Ol Pejeta** — northern white rhino enclosure, Sweetwaters chimpanzee
  sanctuary, endangered species boma
- **Nairobi NP** — Ivory Burning Site, Hippo Pools, Athi Basin, Nairobi Safari Walk

Nairobi NP earns Tier B on commercial grounds, not prestige: 20 minutes from
base, genuine half-day product, high year-round demand.

### Tier C — secondary destinations: 8 × 1 = 8

One comprehensive page each. **Lake Naivasha · Hell's Gate · Aberdare ·
Mount Kenya · Meru · Shimba Hills · Lake Bogoria · Buffalo Springs and Shaba**

Promote any of these to a full cluster if it starts converting. Tier is a
resourcing decision, not a permanent judgement.

### Coast: 2

`/safari-and-beach-kenya/` · `/diani-after-safari/`

Deliberately reduced from a 30-page coast tier. Both pages are framed as **the
second half of a safari**. Still prohibited: resort reviews, diving as a primary
topic, "best beaches in Kenya" listicles. If a page would make sense on a site
that sells no safaris, it does not belong here.

### Conservancies: 1

`/kenya-conservancies/` — a single page covering the model, the named
conservancies, and why it costs what it costs. Links to
`/conservation/conservancy-fees-explained/`.

## Pillar 16 — Circuits and road routes
*Phase 6 · 9 pages*

**Circuits (3):** Southern · Rift Valley · Northern

**Road routes (6):** Nairobi–Masai Mara · Nairobi–Amboseli · Nairobi–Tsavo ·
Nairobi–Samburu · Nairobi–Nakuru · Nairobi–Ol Pejeta

Road routes are pure information gain — real distances, real drive times, real
current road condition, where to stop, where the fuel is. Kambu drives these;
almost nobody ranking for them does. Protected from the cut for that reason.

## Pillar 14 — Activities and experiences
*Phase 6 · 8 pages*

`/safari-activities/` (hub) · game drive · night game drive · walking safari ·
balloon safari · cultural visit · rhino tracking · birding safari

Each states which parks offer it, what it costs, whether Kambu operates or books
it, and its honest footprint. Balloon safaris must not be sold as low-impact.

## Pillar 13 — Ecosystems
*Phase 6 · 4 pages*

`/ecosystems/` (hub) · Great Rift Valley · Mara–Serengeti ecosystem ·
Amboseli–Tsavo ecosystem

Reduced to the three that carry structural weight. The Mara–Serengeti page is
the *reason* Pillar 9 exists.

## Pillar 17 — Traveller segments
*Phase 7 · 6 pages*

`/first-safari/` · `/over-60s-safari/` · `/accessible-safaris-kenya/` ·
`/women-travelling-alone/` · `/photography-safari-kenya/` ·
**`/kenyan-resident-rates/`**

Commercial segment pages already live in Pillar 3 and are not duplicated here.
`/kenyan-resident-rates/` is commercially underrated — resident rates are a real
product and the query has almost no serious competition.

## Pillar 9 — Tanzania bridge
*Phase 7 · 5 pages · **HARD CAP***

Admissible only because the Mara and Serengeti are one ecosystem. Every page is
framed as an extension of a Kenyan itinerary. **If the itinerary does not start
in Kenya, it does not get published.**

`/masai-mara-serengeti-safari/` (hub) · `/mara-vs-serengeti/` ·
`/isebania-border-crossing/` · `/ngorongoro-crater-extension/` ·
`/tanzania-park-fees-and-costs/`

## Pillar 10 — Decision and comparison
*Phase 8 · 4 pages*

`/kenya-vs-tanzania-safari/` · `/how-to-choose-a-safari-operator/` ·
`/questions-to-ask-before-booking/` · `/booking-direct-vs-through-an-agent/`

---

## Publication order

| Phase | Pillars | Section | Pages | Gate to proceed |
|---|---|---|---|---|
| 1 | Root, 0, 1, 2 | Core | 34 | Entity home indexed; camp cluster complete |
| 2 | 3, 4 | Core | 28 | All package + cost pages live and priced |
| 3 | 5, 11 | Core | 23 | Fleet complete; every conservation claim evidenced |
| — | — | — | **85** | **Core complete. Only now start Outer.** |
| 4 | 6, 15 | Outer | 39 | Mara sub-entities complete; 12 month pages distinct |
| 5 | 7, 12 | Outer | 28 | — |
| 6 | 8, 16, 14, 13 | Outer | 83 | Tier B templates applied evenly — no partial clusters |
| 7 | 17, 9 | Outer | 11 | — |
| 8 | 10 | Outer | 4 | Coverage reviewed; gaps recorded with reasons |
| — | — | — | **165** | Map complete |

Do not interleave. The commonest failure is publishing attractive Outer content —
migration guides, packing lists — before Core exists, which trains the site
vector on content the business cannot monetize.

---

## Scope discipline

250 is a **ceiling, not a quota**. 250 thin pages rank worse than 120
substantive ones. Every page must clear the Core bar:

- answers a question the searcher actually has;
- contains at least one fact not on page one of the current results;
- names real places, real numbers, real months;
- routes to a Kambu product or to a page that does.

A page that cannot clear it is a section of its parent, not a page. **Ship 120
excellent pages before ship 250 adequate ones** — the remaining 130 are a
backlog to earn, not a target to hit.

---

## Internal linking rules

1. Every Outer page links **up** to its Core parent within the first screen.
2. Every Pillar 2 page links to `/kambu-mara-camp/` and `/masai-mara-safari-packages/`.
3. Every package page links to the camp cluster, the relevant cost page, and at
   least one Pillar 2 comparison.
4. Every `/{park}/where-to-stay/` re-applies the Pillar 2 ladder — this is what
   keeps 62 destination pages tied to the central entity instead of floating free
   as a travel encyclopaedia.
5. Every wildlife page links to the named parks it mentions; every month page
   links to the parks it recommends. The links exist because the relationships
   are true.
6. Hubs link down to every child. Anchor text uses the canonical entity term.
7. No reciprocal links to sibling domains for ranking purposes.

---

## Volatility register

- **Quarterly (H):** all rates, park fees, migration timing, road conditions,
  border procedure, eTA requirements, `/reviews/`, every conservation figure
- **Annually (M):** itineraries, facilities, comparison tables, seasonality
- **On change (L):** definitional and experiential content

---

## Open items

1. Validate against Search Console and Ahrefs once API units reset. The map is
   derived from the business model, not current rankings — expect to merge or
   split 5–10 pages, and to re-tier at least one Tier C destination.
2. Agree the topic split with masaimara.ke before Phase 4 begins.
3. Confirm Kambu Mara Camp tent count, tent classes and current rack rates
   before Phase 1 ships.
4. Fill the evidence register in `conservation-vector.md` before Phase 3.
5. Revisit the 250 cap at the end of Phase 6. If Core is converting and Tier B
   is ranking, the case for extending toward full domain coverage — and for
   treating the head term as a real objective — can be made on data rather than
   ambition.
