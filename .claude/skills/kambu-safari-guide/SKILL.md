---
name: kambu-safari-guide
description: "Write and build a Kambu Campers safari guide page (planning guide, itinerary, destination guide, cost explainer, comparison, accommodation or wildlife guide) in the Kambu Guide design system saved in this repo: semantic-authority writing adapted for Kambu, the brand voice, graded evidence, and the .kg- interactive layer (toggle tabs, sidebar tabs, accordions, image gallery with arrows and lightbox, section tracker). Use whenever the user asks for a Kambu guide, a guide page, an itinerary guide, a destination or planning article for kambucampers.com, or to apply 'the guide design system'. Not for exact bookable package pages (use kambu-products / kambu-product-page)."
---

# Kambu safari guide

Builds one guide page in `guides/<slug>/` from the system in
`design-system/kambu-guide/`. The writing rules live in
`design-system/kambu-guide/docs/writing-framework.md`; the markup lives in
`design-system/kambu-guide/docs/components.md`. Read both before starting:
this file is the running order, not a substitute for them.

## Precedence

Accuracy → the dominant answer → bounded coverage → reader sequence →
enrichment → styling. Restraint beats addition. When this repo's files and a
synced skill disagree on **visuals**, this design system wins; on **Kambu
wording and claims**, `kambu-brand-voice` wins; on anything else, ask.

## Running order (do not skip the stops)

1. **Load the writing skills first, not the visual ones**: `semantic-authority-writer`,
   `kambu-semantic-content-architect`, `kambu-brand-voice`, and `kambu-guides`
   if available. Read `strategy/source-context.md` and find the page's row in
   `strategy/topical-map.md` (it says what the URL may own and must hand off).
2. **Page contract** (framework §4). Write the one-sentence test. **Stop** if
   it needs "and" to join unrelated tasks.
3. **Coverage ledger** (framework §5) with treatment codes. **Stop** until it
   exists as a written table; it goes into the guide's `HANDOFF.md`.
4. **Evidence**: Kambu's own records first (this repo, Drive, brand voice),
   then official sources (KWS, KMD, Mara Conservancy, Narok County), then
   expert secondary. Grade every source A/B/C/D/S/K. Never cite the publisher
   network. A blocked fetch stays blocked; say so in the handoff.
5. **Write** into a copy of `guides/_template/index.html`: answer first,
   facts, mechanism, comparison, exceptions, decision, conversion, then ~8
   residual FAQs. Use only `experience_basis` facts for field notes; ask when
   one is missing. Delete template modules the page does not need.
6. **Interaction blueprint** (framework §9): one primary interaction, one to
   three supporting, one navigation aid. Nothing essential only inside a tab
   or accordion.
7. **Media**: Kambu's own photos for the camp, fleet and team; credited
   placeholders elsewhere (`data-placeholder="true"`); open every photo before
   using it; WebP at 400/800/1200, EXIF stripped (`kambu-image-metadata` if
   available).
8. **Check**: `python3 design-system/kambu-guide/tools/check_guide.py guides/<slug>/index.html`
   until it reports no FAIL; resolve or justify every WARN.
9. **Render**: serve the repo (`python3 -m http.server`) and look at the page
   at 1440 px and 390 px. Click every tab, the gallery arrows and lightbox,
   and the FAQ; confirm no sideways scroll and zero broken images; reload
   with JavaScript off and confirm every panel reads.
10. **Handoff**: write `guides/<slug>/HANDOFF.md` (framework §13) with a
    publication decision: Approved, Approved with revisions, or Not approved.

## Hard rules that are easy to break

- One H1. H2s state claims, not labels. First sentence under a heading answers it.
- Every price has its basis in the same sentence; fees never share a table with package rates.
- Kambu Mara Camp is **about 9.0 km before Sekenani Gate from Narok** (never "8 km" or "14 minutes"). Nairobi–Mara by road is about 5–6 hours.
- Never claim KATO, KPSGA, unverified TRA numbers, response-time promises, group sizes, guaranteed sightings, or "budget"/"luxury" for Kambu.
- guests, driver-guide, game drive, the Reserve; British spelling.
- Entity-home link once, from the first field note. One phrase per URL.
- Each page declines to promise at least one thing.
- Guides inform; products sell. Route the ready reader to one named destination.

## Delivering

Commit the guide folder (page, assets, HANDOFF.md). For a single-file preview
or share copy:
`python3 design-system/kambu-guide/tools/build_standalone.py guides/<slug>/index.html --embed-images`
(writes `dist/<slug>.html`, which is git-ignored). Keep `noindex` until the
handoff says Approved.
