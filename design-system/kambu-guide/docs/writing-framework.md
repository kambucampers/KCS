# Kambu Guide writing framework

Version 1.0 · 1 October 2026

How a Kambu Campers safari guide is researched, written and checked before it
is rendered in the Kambu Guide design system. This is the writing half of the
system; [components.md](components.md) is the markup half.

It adapts, for guides, the rules in these skills (read them for anything this
file compresses): `semantic-authority-writer`, `kambu-semantic-content-architect`,
`kambu-brand-voice`, `kambu-guides` (G01–G40 / T01–T10), `kambu-page-build`,
`page-build-defaults` and `website-topical-authority`. The site charter itself is
[`strategy/source-context.md`](../../../strategy/source-context.md) and the page
inventory is [`strategy/topical-map.md`](../../../strategy/topical-map.md).

Guides inform. Products sell. A page that does both fails both, so exact
bookable packages go through `kambu-products` instead.

---

## 1. Precedence

When two rules conflict, the higher one wins. Most of this framework is
restraint; additions (depth, images, tabs) lose to restraint by default.

1. **Accuracy.** No invented fact, figure, citation, credential, guide
   statement or image subject. A gap stated on the page beats a gap filled by
   guessing.
2. **The dominant answer.** The page's main question is answered in visible
   prose, early, and never displaced by a tab, an image, a research block or a
   call to action.
3. **Bounded coverage.** One dominant intent. Adjacent intents stay on the
   pages that own them (see the register in `topical-map.md`).
4. **Reader sequence.** Answer, then explain, then compare, then convert.
5. **Enrichment.** Subject depth, field notes, images, maps, interaction.
6. **Engagement styling.** Component prominence, galleries, motion.

## 2. The Kambu charter (filled; do not re-derive per page)

> Kambu Campers is a Kenyan-registered tour operator that owns and operates a
> permanent tented camp near Sekenani Gate and runs its own safari fleet,
> helping first- and second-time safari travellers plan comfortable,
> transparently priced Kenya safaris through route-led planning from people
> who run the camp and the vehicles.

```yaml
site: kambucampers.com
brand_identity: Kambu Campers (Kambu Campers Ltd); sub-entity Kambu Mara Camp
brand_short_forms: [Kambu, Kambu Campers, the team at Kambu]
source_type: owner-operator (camp + fleet), not a marketplace or affiliate
central_entity: the permanent tented camp safari, Masai Mara dominant
contextual_domain: Kenya safari (structural parent, not a ranking target)
primary_audiences: [independent travellers 25-55 on a first or second safari,
  couples who reject dome tents but not lodge prices, families and small groups
  needing en-suite rooms, Kenyan residents and expats on short Mara trips]
conversion_paths: [tailored quotation via bookings@kambucampers.com,
  product pages for exact packages, Kambu Mara Camp stays]
evidence_standard: graded A/B/C/D/S/K (section 8); dated; conflicts shown
design_system: Kambu Guide v1.0 (this folder)
cms_or_output_format: standalone HTML now; WordPress block via build step later

experience_basis:            # source: kambu-brand-voice v1, 15 Sep 2026
  who: [Mara driver-guides, park-specialist guides for other parks, the founders]
  based_where: Kambu Mara Camp, about 9.0 km before Sekenani Gate on the
    road from Narok; Nairobi office
  how_they_know:
    - Mara driver-guides live at the camp near Sekenani, not in Nairobi
    - before Kambu, the founders spent roughly a year travelling Kenya's safari
      destinations (mostly the Masai Mara, Tsavo East and Amboseli), learning
      transfer timing, park routes, game-drive planning, layovers and return
      flights
  owned_assets: [Kambu Mara Camp permanent tents, safari fleet (4x4 Land
    Cruisers, minivans, buses, the "Cheyat" campervan)]
  operating_facts:
    - Nairobi to the Mara by road is about 5-6 hours each way
    - returning to camp between a morning and an afternoon drive can cost up
      to an hour of transport
    - one transparent rate for resident and non-resident guests
  years_operating: NOT SUPPLIED - ask before using
  what_they_will_not_claim: see section 7 (Never claim)
  verified_by: kambu-brand-voice v1 (Nathan's voice and business profile)
```

If a page needs an experience fact that is not in this block, **ask**; do not
infer it. Do not say the founders' year was "in a campervan" until confirmed.

## 3. Working order (with stops)

1. **Brief and contract** (section 4). Stop if the one-sentence test fails.
2. **Coverage ledger** (section 5). Stop until it exists as a written table.
3. **Evidence**: Kambu's own records first (repo, Drive, brand voice), then
   official sources, then expert secondary. Research ends here.
4. **Write**: answer, entity facts, explanation, comparison, exceptions,
   decision, conversion, residual FAQs.
5. **Interaction blueprint** (section 9): choose components for content that
   now exists.
6. **Media**: only to match content that exists. Kambu's own photos for the
   camp, vehicles and team; credited Wikimedia/Pexels placeholders elsewhere,
   marked `data-placeholder`. Never a stock photo standing in for Kambu staff.
7. **Render** from `guides/_template/index.html`.
8. **Gates**: run `tools/check_guide.py`, then the manual gates in section 12,
   then look at the page at 1440 px and 390 px.

Reaching for components before the content exists produces pages built
around their decoration.

## 4. The page contract

Record it in the HTML head comment of every guide (the template has the slot)
and in the guide's `HANDOFF.md`.

```yaml
url:                    # existing to preserve, or "proposed"
archetype:              # destination | planning | itinerary | comparison |
                        # cost | accommodation | wildlife | trust | help
dominant_intent:
primary_query:
searcher:               # their situation and knowledge
journey_stage:          # orient | plan | compare | ready
parent_hub:             # owning URL from topical-map.md
required_subentities: []
explicit_exclusions: [] # with the URL that owns each
facts_to_verify: []
commercial_destination: # the specific product or hub a ready reader goes to
advice_moments: []      # the 1-3 judgement calls this page makes
experience_credential:  # which experience_basis line earns those calls
information_gain:       # what this page says that the ranking set does not
last_reviewed:          # date of the last substantive fact check
```

The one-sentence test:

> This page helps **[specific reader]** answer **[one question]** so they can
> **[a Kenya travel or Kambu decision]**, while routing **[excluded tasks]** to
> their owning pages.

If the sentence needs "and" to join unrelated tasks, split the page.

## 5. Entity coverage ledger

Before drafting, one row per topic:

| Topic | Relationship to central entity | Decision it affects | Treatment | Evidence needed | Owning URL |
|---|---|---|---|---|---|

**Relationship** is a predicate: *is-a, forms part of, is reached from, is
priced by, requires, restricts, depends on, differs from, excludes*.

**Treatment codes** map straight to components:

| Code | Means | Renders as |
|---|---|---|
| `H2` / `H3` | own section / sub-question | `.article-section` / `h3` in `.prose` |
| `ANS` | the direct answer | `.kg-answer` |
| `TBL` | comparison or schedule row | `.table-scroll > table` |
| `DAY` | itinerary day | `.day-section` + `.day-summary` + `.kg-daynav` |
| `TAB` | alternative view of one decision | `.kg-tabs` (2-4) or `.kg-tabs--vertical` (4-6, long labels) |
| `ACC` | optional depth, FAQ, policy | `.kg-acc` native `<details>` |
| `FACT` | short parallel attributes | `.kg-facts` / `.planning-card` |
| `NOTE` | caution or scope limit | `.note` |
| `FIELD` | first-party experience | `.kg-fieldnote` (max 3 per page) |
| `SUIT` | who it suits / does not | `.kg-suit` |
| `CHOOSE` | decision rule between options | `.kg-choose` |
| `IMG` | photo the reader needs to judge something | `.kg-gallery` or figure |
| `LNK` | link only; another URL owns it | contextual prose link |
| `EXC` | deliberately excluded | named exclusion sentence |
| `SRC` | source | `.kg-sources` row |

Tag rows `flagged` where an input from Nathan is missing. Every non-self
owning URL must appear as a link in the finished page. The count of `H2`/`H3`
rows is the number of headed units the page needs; write that many, not more.

## 6. Writing rules

### Answer first

- The first sentence under any heading answers it. Section-opening answers run
  40-55 words. Resolve the entity, the question and the deciding factors in
  the first 100 words of the page.
- State scope, place, timing, units and conditions in the answer itself, then
  the mechanism, exceptions and advice.

### Fact, mechanism, consequence, advice

> Wilson Airport serves most domestic safari flights, **so** passengers landing
> at JKIA need a timed road transfer between the two airports.

One sentence can carry the chain. Label inference as inference.

### Headings state something

"Why the 15 kg limit is not negotiable" beats "Baggage overview". A reader who
reads only the headings should get the page's argument. No bare labels:
*Overview, Introduction, Information, Details, About*.

### Controlled vocabulary (from kambu-brand-voice)

| Always | Never |
|---|---|
| guests | customers, clients (B2B only) |
| driver-guide | "driver" or "guide" alone when the person guides |
| game drive | safari drive |
| the Reserve (Masai Mara National Reserve) | the reserve, the park (for the Mara) |
| permanent tented camp (canonical); glamping only on its own pages | luxury camping as a synonym |
| per tent / per vehicle / per person in the same sentence as every price | a bare price |
| standard full-day (ends ~16:00), extended full-day (ends ~18:00) | "8 hours", "12 hours of viewing" |

British spelling. `~` for approximate, en dashes for ranges (Jul–Oct), units
stated (km, USD, KES). Do not rotate synonyms; keep distinctions (camp vs
campsite, Reserve vs conservancy, nights vs days, admission days vs nights).

### Cut on sight

- Sentences about the page itself: "this guide covers", "in this article we",
  "every link below".
- SEO register: nestled, boasts, when it comes to, look no further, in today's
  world, whether you're X or Y, world-class, unparalleled, once-in-a-lifetime,
  breathtaking openers.
- Link text: click here, read more, learn more.
- More than four prose paragraphs without a structural break.
- Bold used for emphasis rather than for a limit, a cost, a deadline or a
  refusal.

### Name the constraint, decline something

Every guide names its own trade-offs and says at least one thing it will not
promise (a view, a crossing, a species, a time). Comparisons end with
**Choose A if… / Choose B if…**, never a universal winner. Suitability
sections give both **This suits you if** and **Choose something else if**.

## 7. Earning the right to give advice

Advice needs a basis. Use one experience credential per advice moment, one to
three per page, placed at the judgement call, built from `experience_basis`
only.

Anatomy: **who** (Mara driver-guides) · **where based** (Kambu Mara Camp, ~9 km
before Sekenani Gate) · **how they know** (live at the camp) · then advice only
that person could give, with one operational detail nobody writes from a desk.

```html
<aside class="kg-fieldnote" aria-label="Field note from Kambu Mara Camp">
  <span class="kg-fieldnote__label">From Kambu Mara Camp, near Sekenani</span>
  <p>At <a href="https://kambucampers.com/">Kambu Campers</a> we route Mara days
  from our own camp, and our Mara driver-guides are based there rather than in
  Nairobi. …</p>
</aside>
```

- **Entity-home link**: once per page, on the first credential, brand-name
  anchor, varied phrasing elsewhere. Never on the homepage.
- **Never write "our guides recommend"** for advice no guide gave. Where no
  credential exists, cite the authority and drop the first person.
- Factual sections need no credential (a park's area is not a guide's opinion).

### Never claim (from kambu-brand-voice and page-build-defaults)

KATO membership or any trade-body badge · KPSGA guide grading · TRA licence
numbers not checked against the certificates · response-time promises ·
group sizes, success rates or departure counts not in a dated log · a fixed
share of bookings funding conservation · community ownership or benefit ·
wheelchair access or allergen-free kitchens (case by case) · guaranteed
sightings, crossings or views · ratings or testimonials not pulled fresh with
permission · camp mobile or internet signal (say "variable") · "budget" or
"luxury" as a description of Kambu.

Facts that are easy to get wrong: Kambu Mara Camp is **about 9.0 km before
Sekenani Gate coming from Narok** (the old "8 km / 14 minutes" and "1 km"
figures are wrong); the Nairobi–Mara road transfer is **about 5–6 hours** each
way.

## 8. Evidence

### Grades (print one beside every source in the register)

| Grade | Meaning | Examples |
|---|---|---|
| **A** | primary instrument | statute, gazette notice, management plan |
| **B** | authority notice | KWS park page, KMD report, Mara Conservancy notice |
| **C** | first-party subject | an airline's own baggage page, a sanctuary's visiting hours |
| **D** | expert secondary | route guides, research stations, marketplace benchmarks |
| **S** | visitor sentiment | trip reports, reviews (labelled as sentiment) |
| **K** | Kambu field record | odometer readings, camp measurements, pricing corpus |

### Rules

- Kambu's own figures beat published ones: odometer over routed distance,
  logged drive times over a mapping app.
- **Do not cite the publisher network** (masaimara.ke, masaimarasafari.travel,
  tourwithpipi.com, maramasai.com, masaimara.or.ke, marareserve.org,
  masaimara.travel and siblings). Citing them is citing yourself.
- When sources disagree on a material value, publish the dominant one and the
  variant in place. Never average.
- Every price states its basis in the same sentence. Park, reserve and
  conservancy fees never share a table with package rates.
- A citation ships only if it was fetched and read in that session. A blocked
  fetch is blocked: route around it and say so.
- Print a visible **last reviewed** line (`.kg-reviewed`) and the graded
  register (`.kg-sources`) at the foot. Update the date only after a real
  check.
- Sensitive locations: no rhino or pangolin locations, no per-sanctuary rhino
  counts. Say the omission is deliberate.

## 9. Interaction blueprint

Complete this before choosing components. Most guides need one primary
interaction, one to three supporting ones and one navigation aid. A static
section is better than a decorative control.

```text
Page type:
Primary visitor decision:
Primary interaction:                  (e.g. route-version tabs)
Supporting interactions:              (e.g. FAQ accordion, camp gallery)
Navigation aid:                       (sidebar section tracker, day navigation)
Conversion action:                    (one named destination)
Visible in the first layer:           (answer, location, duration, price basis,
                                       access, suitability, restrictions)
Behind tabs/accordions:               (alternative views, optional depth only)
Rejected interactions and why:
Analytics events:                     (from components.md)
```

### What a tab or accordion may never hold

The page's direct answer · the only mention of a fact · the price basis ·
access restrictions · safety information · dates or eligibility rules · the
primary CTA. Tabs are for **alternative views** (route versions, seasons,
traveller types, road vs fly-in); if readers need to compare options side by
side, use a table instead. Accordions are for FAQs, policies, logistics and
secondary depth, never the core sections.

### Choosing between components

| Content | Use |
|---|---|
| 2-4 alternative versions of one plan | horizontal `.kg-tabs` |
| 4-6 alternatives with sub-labels, or long labels | `.kg-tabs--vertical` (sidebar tabs) |
| Options compared simultaneously | table |
| Residual questions | `.kg-acc` FAQ, first item open, ~8 questions |
| Photos that let a reader judge a place or room | `.kg-gallery` (one per page, two on long guides) |
| Day-by-day itinerary | visible day sections + `.kg-daynav`, summary table above |
| Long page | sidebar `[data-kg-spy]` nav + `[data-kg-progress]` |

## 10. Links

- Add a link only when the destination answers the natural next question.
  Write the bridge first: *connecting fact → consequence → destination*.
- Five directions: up to the parent hub, down to children, sideways to
  alternatives, forward to the commercial destination, and home once from a
  credential.
- Anchor discipline: one phrase → one URL site-wide; no phrase twice on a page;
  no URL under two phrases. Furniture (header, sidebar, footer, breadcrumbs,
  day navigation) is exempt.
- Never link to a page that does not exist yet. Record it in the handoff as
  proposed.
- External citations sit at the end of the claim they support.

## 11. Conversion and metadata

- Name the **commercial destination** in the contract. Reach it through prose
  at the moment the need appears, then once with a button near the end.
- Informational guides answer fully before offering the next step. One primary
  CTA; the header and planning-card buttons point at the same `#plan`
  section.
- No false urgency, no live-booking tickers, no pop-up forms.
- Every guide ships an **H1, SEO title, meta description, URL decision and
  excerpt**. Titles reflect the task, not an unverified price. Example:
  H1 "10-Day Kenya Safari Itinerary: Amboseli, Naivasha and Masai Mara";
  title "10-Day Kenya Safari Itinerary: Route, Costs & Tips".
- Structured data mirrors visible content only: `Article` + `BreadcrumbList`,
  `about` the places, `mentions` Kambu Mara Camp. No `Product`/`Offer` on a
  guide, no FAQ rich-result promises.

## 12. Quality gates

`tools/check_guide.py` automates the ones marked **[auto]**. The rest need a
person reading the page. A failed gate blocks publication regardless of
score.

**Intent and scope**
1. One dominant intent and archetype; the one-sentence test passes.
2. Every ledger row has a treatment; adjacent intents link to their owners.
3. The direct answer is in visible prose in the first 100 words. [auto: `.kg-answer` present]
4. No sentence describes the page itself. [auto: phrase scan]

**Accuracy and evidence**
5. No Never-claim item. [auto: KATO, KPSGA, "8 km" near Sekenani]
6. Every price has its basis and date; fees separate from package rates.
7. Conflicts disclosed, not averaged.
8. Graded sources register and last-reviewed line present. [auto]
9. Each credential traces to `experience_basis`; at least one thing is
   explicitly not promised.
10. No citation to the publisher network. [auto]

**Writing**
11. Headings state claims; no bare-label H2s. [auto]
12. Controlled vocabulary and British spelling. [auto: common slips]
13. No banned phrases or link text. [auto]
14. Comparisons end with Choose A / Choose B; suitability has both sides.

**Structure and interaction**
15. One H1; logical H2/H3 order; unique ids. [auto]
16. Every section has `aria-labelledby` pointing at a real heading. [auto]
17. Tabs: each `data-kg-tab` points at a panel with its own heading; one
    default; nothing essential only inside a panel. [auto: wiring]
18. FAQ: first item open, answers open with the answer, no lists inside.
    [auto: first open]
19. Images: alt text, width and height, lazy below the fold, credit in the
    caption. [auto]
20. External links have a reason; no `target="_blank"` without
    `rel="noopener"`. [auto]
21. No template markers left. [auto: `[[`, `TODO`, `{{`]

**Render**
22. Viewed at 1440 px and 390 px; no horizontal page scroll; zero broken
    images; tabs, gallery, lightbox and accordions work by keyboard; the page
    reads completely with JavaScript off.
23. Would a senior editor at a serious publication put their name on it?

## 13. Deliverables per guide

In `guides/<slug>/`:

1. `index.html` — the page, with the contract in its head comment.
2. `assets/` — WebP at 400/800/1200 widths, EXIF stripped, SEO filenames.
3. `HANDOFF.md` — contract, coverage ledger, interaction blueprint, metadata,
   link table, sources with grades and dates, credentials used and the
   charter line each rests on, changes made, open items, gate results and a
   publication decision: **Approved**, **Approved with revisions** or **Not
   approved**.
