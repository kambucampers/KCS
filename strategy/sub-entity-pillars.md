# Cross-Cutting Sub-Entity Pillars

New pillars 12–17 for [`topical-map.md`](./topical-map.md). Governed by
[`source-context.md`](./source-context.md).

**Total: 130 pages.**

---

## Why these exist

The destination taxonomy covers the domain **by place**. That is one axis. A
domain is not comprehensively covered until it is also covered by the other
axes a searcher actually uses:

- by **animal** — "where to see wild dogs in Kenya"
- by **activity** — "walking safari Kenya"
- by **time** — "Kenya safari in February"
- by **ecosystem** — "Great Rift Valley"
- by **route** — "northern circuit Kenya"
- by **traveller** — "safari for over 60s"

These pillars are also the highest-value internal linking substrate on the site.
A species page legitimately links to eleven destination clusters; a month page
legitimately links to every park with a seasonal argument. That is real
contextual flow, not a link scheme — the links exist because the relationships
are true.

---

## Pillar 12 — Wildlife (48 pages)
*Section: Outer · Phase 5*

The single largest coverage gap in the previous map. Wildlife is the sub-entity
class most safari searches actually resolve to.

### Structure

| Group | Pages |
|---|---|
| Hub | `/wildlife/` |
| Big Five | lion · leopard · elephant · buffalo · black & white rhino (2 pages) |
| Big Nine extension | cheetah · giraffe · zebra · hippo |
| Predators | spotted hyena · striped hyena · wild dog · serval · caracal · genet |
| Northern specials | Grevy's zebra · reticulated giraffe · gerenuk · beisa oryx · Somali ostrich |
| Endangered & rare | northern white rhino · bongo · sitatunga · sable · roan · hirola · Rothschild's giraffe |
| Birds | `/birds/` hub · flamingo · secretary bird · vultures · kori bustard · crowned crane · birding-by-season |
| Events & behaviour | wildebeest migration · Mara river crossings · calving season · elephant tuskers · big cat territories |
| Marine | dolphins · whale sharks · turtles *(coast extension only)* |

### The template that makes this convert

Every species page follows the same shape, and the third section is what ties it
to the business:

1. What it is — identification, size, behaviour, status
2. Where it lives in Kenya — **named parks, linked to their clusters**
3. **Best park and best month to see it** — the decision the searcher came for
4. Conservation status and what threatens it — the vector, page-specific
5. How Kambu's itineraries reach it

Add `/wildlife/where-to-see-{species}/` as a distinct page only where search
demand genuinely splits from the species page itself — for the flagship species
(lion, leopard, rhino, cheetah, wild dog, flamingo) it does. Elsewhere it is a
section, not a page.

**Ol Pejeta's northern white rhinos deserve their own page.** Two animals, a
globally covered story, and you can drive guests to them. There is no stronger
single asset for connecting wildlife content to the conservation vector.

---

## Pillar 13 — Ecosystems and landscapes (12 pages)
*Section: Outer · Phase 6*

The parent entities that destinations belong to. These give the destination
layer a hierarchy instead of a flat list, and they are how a site demonstrates
it understands the domain rather than just enumerating it.

`/ecosystems/` hub · Great Rift Valley · Mara–Serengeti ecosystem ·
Amboseli–Tsavo ecosystem · Laikipia Plateau · Northern Frontier ·
Rift Valley Lakes (UNESCO) · Mount Kenya massif · Aberdare Range ·
Chyulu Hills · Kenyan coast and marine · Western Kenya and Lake Victoria basin

Each names its constituent parks and conservancies and links down to them. This
is the layer that makes the Tanzania bridge coherent — the Mara–Serengeti
ecosystem page is the *reason* Pillar 9 exists.

---

## Pillar 14 — Activities and experiences (16 pages)
*Section: Outer · Phase 5*

`/safari-activities/` hub · game drive · night game drive · walking safari ·
balloon safari · horseback safari · camel safari · fly-camping · birding safari ·
photographic safari and hides · rhino tracking · chimpanzee sanctuary ·
cultural visit (Maasai) · cultural visit (Samburu) · conservation experience ·
sundowners and bush meals

Each page states which parks and conservancies offer it, what it costs, whether
Kambu operates it directly or books it, and its honest footprint. Balloon
safaris in particular must not be sold as low-impact — per
`conservation-vector.md`, that is a prohibited construction.

---

## Pillar 15 — Timing and seasonality (22 pages)
*Section: Outer · Phase 4*

High-intent, evergreen, and it compounds. Phase 4 rather than later because
these pages route strongly into packages.

**Months (12):** `/kenya-safari-in-{month}/` — one per month. Each covers
weather, wildlife, crowds, price, which parks are at their best, and what Kambu
would recommend booking.

**Seasons and periods (9):** dry season · long rains · short rains · green
season · calving season · migration season · shoulder season · Christmas and New
Year · Easter

**Hub (1):** `/best-time-for-a-kenya-safari/`

The month pages are the cluster most likely to be written as thin, interchangeable
filler. They must differ substantively from one another — if January and February
say the same thing, one of them should not exist.

---

## Pillar 16 — Circuits and routes (14 pages)
*Section: Outer · Phase 6*

**Circuits (6):** Southern · Rift Valley · Northern · Coastal · Western ·
Mara–Serengeti cross-border

**Road routes (8):** Nairobi–Masai Mara · Nairobi–Amboseli · Nairobi–Tsavo ·
Nairobi–Samburu · Nairobi–Nakuru · Nairobi–Ol Pejeta · Mombasa–Tsavo ·
Amboseli–Tsavo

The road-route pages are pure information gain — real distances, real drive
times, real current road condition, where to stop, where the fuel is. You drive
these; almost nobody ranking for them does. Date-stamp the condition section and
show the date.

---

## Pillar 17 — Traveller segments (18 pages)
*Section: Outer · Phase 7*

Intent-axis coverage. Several already exist in Pillar 3 as commercial pages —
those are not duplicated here; this pillar covers the *informational* half.

first safari · solo travellers · couples · honeymoon · families with toddlers ·
families with teenagers · multi-generational · over 60s · accessible safaris ·
women travelling alone · groups of friends · small groups · large groups ·
students and gap year · photographers · birders · repeat visitors ·
Kenyan residents and expats

Each answers: what changes for this traveller, which parks and accommodation
classes suit them, what it costs, and what to avoid. `/kenyan-residents/` is
commercially underrated — resident rates are a genuine product and the query
has almost no serious competition.

---

## Coverage matrix — the completeness test

The domain is comprehensively covered when every cell that should be true has a
page or a section:

| | Place | Species | Activity | Month | Traveller |
|---|---|---|---|---|---|
| **Place** | vs-comparisons | `/{park}/wildlife/` | `/{park}/things-to-do/` | `/{park}/best-time/` | `/{park}/where-to-stay/` |
| **Species** | where-to-see | — | rhino tracking, birding | migration, calving | photographers, birders |
| **Activity** | by park | by species | — | seasonal availability | by segment |
| **Month** | by park | by event | by activity | — | school holidays |

Run this matrix quarterly. Empty cells that *should* be filled are the next
content brief. Cells that should stay empty are a judgement — record why, so the
decision is not relitigated every quarter.

---

## A warning worth heeding

This map is now large. **600+ pages of thin content ranks worse than 150 pages
of substantive content**, and it damages the site vector rather than deepening
it. Every page in these pillars must clear the same bar as a Core page:

- it answers a question the searcher actually has;
- it contains at least one fact not available on the first page of results;
- it names real places, real numbers, real months;
- it routes to a Kambu product or to a page that does.

If a page cannot clear that bar, it is a section of its parent, not a page. The
map is a ceiling on scope, not a production quota.
