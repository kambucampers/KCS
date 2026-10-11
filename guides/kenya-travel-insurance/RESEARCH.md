# Kenya travel insurance guide: build record

Page: `/ke/guides/kenya-travel-insurance/` (proposed). Built 11 October 2026.
Namespace `.kti`. Design system: Executive Elegant. Voice: kambu-brand-voice v1.

## What was asked, and what was actually built

The brief was to convert a local HTML draft (`kenya_travel_insurance_guide (2).html`
on Nathan's machine) into the guide format used at
`staging9.kambucampers.com/ke/guides/`, expand it into numbered purchase steps,
place the four eCitizen screenshots, cite government sources and VisasNews, and
optimise for the questions people search.

Two inputs were not reachable from the build environment:

1. **The source HTML file.** It lives on Nathan's Mac and was not in the
   repository or the session uploads. The page was therefore researched and
   written from primary and secondary sources rather than converted. Nothing from
   the draft survives because nothing from the draft was available.
2. **staging9.kambucampers.com.** The host is robots-disallowed and blocked at the
   proxy. The reference guide could not be read. The page follows the Executive
   Elegant system because the brand-voice skill (15 Sep 2026) records it as the
   canonical system for kambucampers.com. If `/ke/guides/` uses a different
   stylesheet, the content is namespaced and can be re-skinned without rewriting.

## Register row and ownership

| Field | Value |
|---|---|
| Register row | `strategy/topical-map.md` Pillar 0 `/travel-insurance/` (Trust, schema none, freshness M). The topical map predates the October rule; this page is the planning guide that row now needs. Slug decision is Nathan's. |
| Cluster | Pillar 7 Preparation and practical. Sibling `/kenya-eta-and-entry-requirements/` owns the eTA itself. |
| Dominant intent | Understand and satisfy Kenya's mandatory inbound travel health insurance before a safari that starts in Nairobi. |
| Owns | The insurance rule: who, what it costs, what it covers, how to buy it (both routes), proof at JKIA, exemptions, legal status. |
| Hands off | eTA mechanics, vaccinations, airport transfers, the Nairobi–Mara road, cancellation terms, package prices. |
| Commercial destination | `https://staging9.kambucampers.com/safari-packages/` (private safaris from Nairobi), reached from the Route A steps, the CTA strip and the final band. |
| Information gain | (1) both purchase routes as numbered steps with real screenshots; (2) three disagreeing figures published side by side instead of averaged; (3) the 7 Aug / 20 Aug / 6 Oct contradiction as a dated timeline; (4) what it means at JKIA for a guest with a dawn arrival and a morning departure to the Mara. |

## SERP read

Ranking pages on 11 October 2026 (VisasNews, VisasUpdate, Fragomen, WKA,
Governors' Camp, Wild Springs) fall into two groups: news posts that report the
portal change, and operator notices that summarise it in six bullets. None of
them:

- writes the eCitizen route as steps with screenshots;
- publishes the USD 52 fee stack alongside the USD 44 premium in a table;
- states that the line items sum to USD 51,300 against a USD 50,000 cumulative floor;
- gives the validity disagreement (12 months vs three months vs the framework's
  30/60-day tiers);
- says anything about what the check means on the day at JKIA.

## Claims and their grades

| Claim | Grade | Source |
|---|---|---|
| Non-Kenyans staying under 12 months must hold travel health insurance | A (via D) | SHI Act 2023 s.26(6), as quoted by Clyde & Co, VisasNews, Eastleigh Voice |
| Cover must run the whole stay; may be bought at point of entry | A (via D) | SHI Regulations 2024 reg 70, as quoted by Clyde & Co and VisasNews |
| Gazette Notice No. 11492 dated 29 July, published 30 July 2026, signed by CS Health Aden Duale | A (via D) | Clyde & Co (29 July), VisasNews (30 July publication), Eastleigh Voice |
| Minimum benefits: 20,000 / 25,000 / 5,000 / 1,000 / 300; cumulative 50,000 | A (via D) | Same three sources agree |
| Insurers must be licensed under the Insurance Act (Cap. 487), IRA-regulated | A (via D) | Clyde & Co; KATA briefing |
| Enforcement on eTA portal from 6 Oct 2026; screen wording; Search Status / Get Now; "Insurance REF: None" | D | VisasNews 6 Oct; VisasUpdate 7 Oct; WKA 10 Oct |
| USD 44 premium; USD 1 access fee; gateway fee; USD 52 total | D | VisasNews 6 and 7 Oct (two transactions); Governors' Camp (USD 8 "convenience and gateway") |
| eCitizen route: five stages, biometric comparison, reference number, "Valid", auto-detected by eTA within minutes | D | VisasNews 7 Oct |
| No downloadable certificate issued | D | VisasNews 7 Oct; Governors' Camp |
| Approved eTA PDF does not mention insurance | D | VisasNews 7 Oct |
| Validity 12 months incl. repeat trips | D | Fragomen 9 Oct; WKA; KATA (20 Aug briefing) |
| Validity three months on quote | D | VisasNews 7 Oct |
| Framework tiers up to 30 / 31–60 / IPMI beyond 60 days | D | Clyde & Co citing the Nov 2025 framework |
| MoH 7 Aug: foreign policies acceptable if compliant; upload with eTA | B (via D) | VisasNews 7 Aug (embeds the MoH statement); Eastleigh Voice |
| 20 Aug briefing: foreign policies not acceptable; USD 44; eCitizen for eTA-exempt; child rates differentiated | D | KATA |
| Suspension 24 Aug by Justice Francis Rayola Olel | D | VisasNews; VisasUpdate |
| Petition dismissed 7 Oct, notice upheld, each party bears own costs | B (via D) | Eastleigh Voice (named judge, petitioners, holdings); VisasNews |
| eTA fee USD 30, expedited +USD 100, 3 working days, apply 2 weeks ahead, documents list | B | etakenya.go.ke FAQ and General Information, read in full |
| eTA exemption lists (EAC 180 days; 90-day and 60-day lists) | B | etakenya.go.ke General Information, read in full |
| eTA-exempt nationals not currently asked for insurance "for now" | D | Governors' Camp |
| Card payments failing on 6 Oct; terms unreadable | S | Reader comments on VisasNews, labelled as sentiment on the page |
| Nairobi–Mara ≈5–6 h; camp ~9 km before Sekenani Gate; pick-up at JKIA after immigration; Nairobi office | K | kambu-brand-voice skill facts |
| Zanzibar USD 44 since 1 Oct 2024; mainland Tanzania introduced its rule early Oct 2026 | D | VisasNews 3 Aug and 6 Oct; Fragomen |

Spelling of the judge's surname differs between sources (Olel / Olele). The page
uses "Olel" in the timeline, as VisasNews and VisasUpdate have it; Eastleigh Voice
uses "Olele". Nathan may wish to check the cause list.

## Disagreements published, not averaged

1. **USD 44 vs USD 52.** Premium vs amount charged. Table in `#cost`.
2. **12 months vs 3 months vs tiered.** Three cards in `#cost`.
3. **50,000 vs 51,300.** Callout in `#cover`, labelled as our arithmetic.
4. **Foreign policies accepted (7 Aug) vs not (20 Aug and the live portal).**
   Timeline in `#own-policy`.
5. **eTA-exempt nationals: required in law vs not being asked.** Table in
   `#exemptions`.

## Held back, and why

- **Underwriting insurer.** Not published anywhere; the purchase page shows only
  the IRA mark. Page says so.
- **A sales desk at JKIA.** The Regulations allow purchase at the point of entry;
  nobody has confirmed a desk exists or takes cards. Page says plan on it not
  existing.
- **Child rate.** Announced as "differentiated" on 20 Aug; never priced. Page says
  budget USD 52 per child until published.
- **Whether EAC citizens are checked at land borders.** Undocumented. Page says so.
- **Screenshots of the eTA-side screens.** None supplied; VisasNews' images are
  theirs. The two eTA screens are described in text boxes with quoted UI strings
  and marked "screen observed on 6 October 2026". Nathan can replace them with
  captures.
- **Any Kambu requirement that guests hold insurance.** Phrased as "we ask every
  guest to travel with their own comprehensive travel insurance". If booking
  terms say "require", change the verb.
- **TRA licence number, KPSGA, KATO.** Not claimed. Trust bar says "a licensed
  Kenyan tour operator".
- **The brand-name link to the entity home.** The semantic-authority writer
  wants one link from a credential to the homepage. The standing rule forbids
  autolinking any live kambucampers.com URL. The credential sentence is left
  unlinked. Nathan to decide at cutover.

## Design decisions

- Executive Elegant, namespace `.kti`, tokens unchanged from the system.
- Hero and final band are solid `--forest-d` with the tint only. No verified
  safari photograph was available and the system forbids stock. Add a
  background image to `.kti__hero` and `.kti__final` when one exists.
- Band order: plan / commerce / exp / plan / commerce / strip / exp / plan /
  commerce / exp / plan / final / related. No two identical adjacent.
- Heading tree is h1 > h2 > h3 only. Part dividers, card titles, suitability
  column heads and related-card titles are styled `<p>` elements, because the
  page-build skill forbids `<h4>` and the heading-order check would otherwise
  fail on furniture.
- `.kti__ui` chips (quoted portal labels) wrap; the first build had them
  `nowrap`, which produced a 62px horizontal overflow at 390px on the long
  "Mandatory Inbound Travel Health Insurance Requirement" string.
- `.kti__price` is `nowrap` so "~USD 52" does not break across lines in a
  narrow table column.
- Government link grid is fixed at three columns so six links sit 3 + 3 rather
  than 4 + 2.
- Images: four first-party screenshots, `width`/`height` set, lazy, alt text
  describes the stage and the visible UI. Deliverable paths are
  `/wp-content/uploads/2026/10/<name>.webp`; upload the files in `img/` with
  those names.
- Spelling: British, per the brand-voice skill (which post-dates the page-build
  skill's US-English rule). Open item below.

## Verification

See `VERIFY.txt`. Gates: `checks.py` (134 assertions), `shot.mjs` at 1440×1000
and 390×844 (zero broken images, zero console errors, no horizontal overflow,
one h1, heading order valid), and every per-section crop opened and looked at.
No interaction test: the page has no tabs or scripted controls beyond the
scroll-spy; accordions are native `<details>`.

`validate_palette.py` was not run: the page introduces no new colours beyond the
system's tokens and documented greys, and no SVG.

## Open items for Nathan

1. **Slug.** `/ke/guides/kenya-travel-insurance/` as built, or the register's
   `/travel-insurance/`. Canonical and breadcrumb in the JSON-LD assume the
   former.
2. **Spelling.** The brand-voice skill says British; the page-build skill's
   standing rules say US. The page is British. Say which wins and the check
   flips.
3. **Hero image.** None shipped. A JKIA arrivals or Narok-road photograph you
   own would carry the arrival-day framing.
4. **eTA-side screenshots.** Capture the two eTA screens (the insurance
   requirement page and the IRA purchase page) and replace the two dashed
   "screen observed" boxes in Route B.
5. **"We ask" vs "we require."** Confirm the booking terms' wording on guests'
   own insurance.
6. **Judge's surname.** Olel or Olele.
7. **The source draft.** If the local HTML held anything not covered here,
   send it and it can be merged.
8. **Re-check cadence.** Weekly until the Ministry publishes the insurer,
   child rate and validity; then quarterly per the register's "H" class for
   entry requirements.
