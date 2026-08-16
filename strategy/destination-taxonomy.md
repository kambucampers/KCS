# Kenya Destination Taxonomy

Replaces Pillar 8 of [`topical-map.md`](./topical-map.md). Governed by
[`source-context.md`](./source-context.md).

The contextual domain is **Kenya safari**. Comprehensive coverage of that domain
means every destination entity gets treated at a depth proportional to its
commercial and search significance — and treated *consistently* within its tier.
Uneven coverage of a domain reads as an unfocused source; that is what tiering
prevents.

**Total: 322 pages across 6 tiers.**

---

## Tiering principle

Tier is set by commercial value to Kambu × search demand × operational reality.
It is **not** set by park size or prestige. Nairobi National Park is Tier B
despite being the smallest park on the list, because it is 20 minutes from your
base, it is a genuine half-day product, and it has high year-round demand.

| Tier | What it is | Cluster depth | Count | Pages |
|---|---|---|---|---|
| A | Flagship — Masai Mara | Pillars 1, 2, 6 | 1 | *(see below)* |
| B | Major parks | 16 pages | 7 | 112 |
| C | Secondary parks and reserves | 8 pages | 14 | 112 |
| D | Remote and specialist | 4 pages | 8 | 32 |
| E | Coast — extension-framed only | 6 pages | 5 | 30 |
| F | Conservancies | 4 pages | 8 | 32 |
| — | Structural | — | 4 | 4 |

---

## Tier A — Masai Mara (flagship)

Already carried by Pillar 1 (camp), Pillar 2 (ladder) and Pillar 6 (ecosystem).
Pillar 6 expands from 14 to **40 pages** to cover the Mara's own sub-entities at
the depth a flagship requires — the sub-entity layer is what was thin.

**Gates** (5): Sekenani · Talek · Oloololo/Oloolaimutia · Musiara · Sand River
**Sectors and features** (9): Mara Triangle · Musiara Marsh · Rhino Ridge ·
Paradise Plain · Oloololo Escarpment · Mara River · Talek River · Sand River ·
Burrungat Plains
**Mara conservancies** (6): Mara North · Naboisho · Olare Motorogi · Ol Kinyei ·
Lemek · Enonkishu — *(Pardamat, Siana, Isaaten as one overflow page)*

Each gate and feature page answers: where it is, what it accesses, which
itineraries use it, drive time from Nairobi and from camp, and what the road is
like now. That is information a reseller cannot write.

---

## Tier B — Major parks (7 × 16 = 112)

**Amboseli · Tsavo East · Tsavo West · Samburu · Ol Pejeta · Lake Nakuru ·
Nairobi National Park**

Tsavo East and Tsavo West are split, not merged. They are distinct entities with
distinct wildlife, access and character, and merging them was an error in the
previous draft.

### The 16-page cluster template

Applied identically to all seven. Consistency is the signal.

| Slug | Page type | Schema | Fresh |
|---|---|---|---|
| `/{park}/` | Cluster hub | `Place`, `TouristAttraction` | H |
| `/{park}/safari-packages/` | **Commercial** | `TouristTrip`, `Offer` | H |
| `/{park}/cost/` | **Commercial** | `FAQPage` | **H** |
| `/{park}/park-fees/` | Reference | — | **H** |
| `/{park}/where-to-stay/` | **Ladder applied** | `ItemList` | H |
| `/{park}/camping/` | Accommodation | — | M |
| `/{park}/best-time-to-visit/` | Planning | `FAQPage` | M |
| `/{park}/weather-by-month/` | Planning | — | M |
| `/{park}/wildlife/` | Sub-entity | — | L |
| `/{park}/birds/` | Sub-entity | — | L |
| `/{park}/gates-and-entry/` | Operational | `Place` | H |
| `/{park}/getting-there/` | Operational | `FAQPage` | **H** |
| `/{park}/map-and-sectors/` | Sub-entity | — | M |
| `/{park}/things-to-do/` | Activities | `ItemList` | M |
| `/{park}/history-and-conservation/` | Depth | — | L |
| `/{park}/vs-masai-mara/` | Comparison | `FAQPage` | M |

### Per-park sub-entities to name explicitly

Named features are the difference between coverage and depth. Each `/map-and-sectors/`
and `/wildlife/` page must name its own:

- **Amboseli** — Observation Hill, Enkongo Narok swamp, Longinye swamp, Lake
  Amboseli, Sinet Delta; big tuskers, Kilimanjaro views, Amboseli Trust elephants
- **Tsavo East** — Aruba Dam, Mudanda Rock, Lugard Falls, Yatta Plateau, Galana
  River; red elephants
- **Tsavo West** — Mzima Springs, Shetani lava flow, Chaimu Crater, Ngulia Rhino
  Sanctuary, Roaring Rocks; black rhino
- **Samburu** — Ewaso Ng'iro River, Koitogor, Sabache/Ololokwe; the Samburu
  Special Five
- **Ol Pejeta** — northern white rhino enclosure, Sweetwaters chimpanzee
  sanctuary, Morani information centre, endangered species boma
- **Lake Nakuru** — Baboon Cliff, Makalia Falls, Out of Africa lookout; flamingo,
  Rothschild's giraffe, both rhino species
- **Nairobi NP** — Ivory Burning Site, Nagolomon Dam, Hippo Pools, Athi Basin,
  Nairobi Safari Walk, animal orphanage

---

## Tier C — Secondary parks and reserves (14 × 8 = 112)

**Lake Naivasha · Hell's Gate · Mount Longonot · Aberdare · Mount Kenya · Meru ·
Shaba · Buffalo Springs · Lake Bogoria · Lake Baringo · Shimba Hills · Ruma ·
Mount Elgon · Chyulu Hills**

### The 8-page cluster template

`/{park}/` · `/cost/` · `/best-time-to-visit/` · `/wildlife/` ·
`/where-to-stay/` · `/getting-there/` · `/things-to-do/` · `/park-fees/`

Promote any Tier C destination to Tier B if it starts converting. The tier is a
resourcing decision, not a permanent judgement.

Shimba Hills is deliberately in Tier C rather than treated as coastal — it is
the bridge entity between the safari domain and the coast extension, and it is
what makes a Diani itinerary a *safari* itinerary.

---

## Tier D — Remote and specialist (8 × 4 = 32)

**Sibiloi and Lake Turkana · Marsabit · Kakamega Forest · Saiwa Swamp ·
Arabuko-Sokoke · Mwea · Ndere Island · Kora**

`/{park}/` · `/wildlife/` · `/getting-there/` · `/where-to-stay/`

These will not convert and are not expected to. They exist to complete the
domain. A site claiming Kenya safari authority that has never heard of Saiwa
Swamp is not covering the domain — it is covering the popular subset of it. This
tier is cheap to produce and is the clearest signal of genuine completeness.

**Do not pad them.** Four honest pages beat eight thin ones.

---

## Tier E — Coast (5 × 6 = 30) — extension-framed only

**Diani · Watamu · Mombasa · Kilifi · Lamu**

A note on the earlier boundary: the previous draft capped the coast at one page,
because beach travel is a different central entity from safari. That was correct
as a default and it is being relaxed deliberately, not accidentally — *bush and
beach* is one of the most common Kenyan itinerary patterns, and the coast is a
real extension of a safari the traveller is already booking with you.

The relaxation is bounded. Every coast page is framed as **the second half of a
Kenyan safari**, never as a standalone beach destination.

| Slug | Framing |
|---|---|
| `/{coast}/` | Hub — as a safari extension |
| `/{coast}/safari-and-beach/` | **Commercial** — the combined itinerary |
| `/{coast}/getting-there-from-safari/` | Operational — the transfer or flight |
| `/{coast}/best-time-to-visit/` | Planning — aligned to safari seasons |
| `/{coast}/where-to-stay/` | Accommodation |
| `/{coast}/things-to-do/` | Activities |

**Still prohibited:** standalone beach-hotel comparison, resort reviews, diving
or watersports as a primary topic, "best beaches in Kenya" listicles. If a page
would make sense on a site that sells no safaris, it does not belong here.

---

## Tier F — Conservancies (8 × 4 = 32)

**Lewa · Borana · Il Ngwesi · Namunyak · Loisaba · Solio · Selenkay · Ol Kinyei**

*(Mara conservancies are covered in Tier A, not here.)*

`/{conservancy}/` · `/wildlife/` · `/where-to-stay/` · `/community-and-conservation/`

This tier carries disproportionate weight for the conservation vector. The
`/community-and-conservation/` page in each cluster is where the conservancy
model — landowner leases, bed-night fees, community ownership — is explained
with real numbers. It links directly to
`/conservation/conservancy-fees-explained/` and
`/conservation/where-your-money-goes/`.

Conservancies are also the strongest available answer to "why does a low-impact
operator cost what it costs", which makes this tier commercially useful as well
as reputationally so.

---

## Structural pages (4)

`/kenya-national-parks/` · `/kenya-national-reserves/` ·
`/kenya-conservancies/` · `/kenya-safari-circuits/`

Each is an `ItemList` routing hub and the parent of its tier.

---

## Rules that hold across all tiers

1. **Every destination page states its accommodation class.** The central entity
   is the tented camp safari; a destination page that never mentions where you
   sleep has drifted off it.
2. **Every destination page carries one page-specific conservation consequence**
   — per `conservation-vector.md`, never a repeated block.
3. **Every cluster has at least one commercial page** routing to a Kambu product.
   Tier D is the sole exception.
4. **Complete a cluster or do not start it.** Partial clusters are worse than
   absent ones.
5. **`/where-to-stay/` always re-applies the Pillar 2 ladder** — this is the
   mechanism that keeps 322 destination pages tied to the central entity instead
   of floating free as a travel encyclopaedia.
