# Kenya campsites map v3: build record (11 Oct 2026)

**URL (proposed):** /ke/guides/kenya-campsites-map/
**Namespace:** `.kcm` (Executive Elegant)
**Block size:** about 1.2 MB uncompressed (about 200 KB gzipped)

## Coverage against your 24-cluster topic map

| # | Cluster | Treatment on the page |
|---|---|---|
| 1 | Geographic entities | 16 H2 region sections with anchors (listed below), each with a boundary map and campsite profiles |
| 2 | Protected-area classifications | The "Who runs them" table: KWS public and special, Mount Kenya hut camps, Masai Mara (Triangle and Narok side), conservancies, private sites. A callout covers KFS forest reserves |
| 3 | Accommodation types | "Camping styles" table: ground tent, rooftop tent, campervan, overland truck, trekking, guided |
| 4 | Geospatial information | Each campsite has GPS, altitude, county, protected-area containment or distance to the nearest boundary, routed drive distance and time from Nairobi, and how far the road ends from the pin. The interactive map shows boundaries; there are 16 regional SVG maps plus one national map |
| 5 | Facilities | Listed per campsite, from the operator or KWS |
| 6 | Costs | KWS camping and park-entry tables (LN 160 of 2025), a KWS calculator, and separate fee cards for each other authority. Every profile carries a cost line |
| 7 | Access and roads | Per-campsite access, road surface, vehicle needs and seasonal notes. The Access section has vehicle counts and the vehicle recovery fee |
| 8 | Wildlife safety | Safety section: KWS guidelines, a ranger requirements table, Naivasha hippos |
| 9 | Seasons | KMD rain seasons as a month strip, the 2023–24 El Niño, Mara floods in 2024 and 2026, the OND 2026 outlook, altitude cold |
| 10 | Itineraries | Linked out to the packages catalogue (owned there, to avoid cannibalisation) |
| 11 | Routes and circuits | Six circuits with routed legs |
| 12 | Travel styles | Styles table, suitability block |
| 13–14 | Environments and activities | Covered through the region intros, profile notes and the "best for" shortlists |
| 15 | Booking | A 7-step booking guide by operator |
| 16–17 | Equipment and vehicles | Checklist and the KWS vehicle fee classes |
| 18 | Responsible camping | Rules section: plastic-free parks, firewood, leave no trace |
| 19 | Rules | Gate hours, off-road ban, drones, Mount Kenya guide rule, payment |
| 20 | Comparisons | "Choose by what matters" shortlists computed from the data, plus camping vs lodge suitability |
| 21 | Campsite profiles | All fields except capacity, which is published for the Mara Triangle sites only |
| 22 | Map filters | Operator, region, vehicle, "published cost only", status, boundaries, search |
| 23 | FAQs | 12 questions with matching FAQ schema |

**Not covered on this page:**
- Cluster 10 (itinerary lengths) belongs on the package pages.
- Gear and vehicle rental in Nairobi is not covered; it needs its own page.
- Mobile coverage maps and fuel stations aren't covered. There's no reliable source for them.

**Region anchors (16):**
- #masai-mara-campsites
- #nairobi-campsites
- #lake-naivasha-campsites
- #lake-nakuru-elementaita-campsites
- #lake-bogoria-baringo-campsites
- #aberdare-campsites
- #mount-kenya-campsites
- #mwea-sagana-campsites
- #laikipia-campsites
- #samburu-northern-kenya-campsites
- #lake-turkana-campsites
- #meru-kora-campsites
- #amboseli-chyulu-campsites
- #tsavo-campsites
- #kenya-coast-campsites
- #western-kenya-campsites

## Method

### Research
I ran eight parallel research passes, one per region group, plus one for reference facts (fees, rules, seasons, safety). The sources used:
- KWS 2026 park pages and the tariff sheet
- Legal Notice 160 of 2025
- Operator sites: Mara Bookings, the Ol Pejeta 2026 tariff, The Big North
- OpenStreetMap / Nominatim
- Recent trip reports, graded S

The publisher-network domains and samburureserve.org are excluded.

### Results
- **Status:** 148 operating, 36 unconfirmed, 3 closed.
- **Removed:** Kisiwa, whose pin is in a residential area with no campsite.
- **Corrected:** 15 pins moved and several categories changed (see "What we checked" on the page).

### Computed data
- **Boundaries:** UNEP-WCMC WDPA (51 areas) plus OpenStreetMap (12 conservancies and the Mara Triangle), simplified.
- **Altitude:** Mapbox terrain-rgb tiles, used only where no source gives the altitude.
- **Drive distance and time:** Mapbox Directions from Nairobi CBD. These are labelled as routed, not measured.

### KWS costs per campsite
Each KWS profile's cost is the LN 160 camping fee plus park entry for that park's fee band. The calculator was spot-checked:
- Amboseli, 1 adult, 1 night: USD 120.
- Chui (Lake Nakuru special site), 2 adults, 3 nights: USD 840 + KES 11,800.

### Interactive maps (v3)
- **Clickable pins on all 17 maps** (16 regional maps plus the national map). Each pin opens a pop-up overview showing type, region, cost, drive time, vehicle and the Google rating. A "Read more" link jumps to that campsite's profile card and highlights it. The pins work by keyboard (Enter opens, Escape closes).
- **Interactive Mapbox map:** uses the same pop-up and link. It also carries a faint Kambu logo and an italic @kambucampers.com.
- **Logo watermark** on every SVG map: opacity 0.14 on the regional maps, 0.12 on the national map.
- **Confidence labels** have been removed everywhere. The evidence trail still sits in "What we checked" and in the CSV.

### Reviews (Apify, 11 Oct 2026)
- **Google Maps Scraper:** 114 results. These were matched to campsites by name and distance, then checked by hand.
  - 59 matches were kept.
  - 9 were dropped because they matched a gate, a park or an unrelated business: Casuarina, Lake Jipe, Ekime, Fisi, Sirimon Gate, Kisoi Munyao, Shamata, Sitatunga and Central Island.
- **Pros and cons (first pass):** 39 campsites had 3 or more written reviews. Each of these gets a "Reviewers like / Reviewers flag" summary written by Kambu, with its basis stated, for example "4 Google reviews, 2018–2025".
- **Second pass (11 Oct, about $1.92):**
  - The 128 campsites without a match were searched by name, biased to each pin's coordinates, keeping the top 3 results.
  - 70 candidates came back. 14 were dropped because they were a park, a swamp, a ranger post, a different lodge or had no rating: Mombasa Marine, Ndololo Safari Camp, Kanderi Swamp, Amboseli Mountain View, Central Island NP, Sitatunga Rangers, Soroi Cheetah, Korosin turnoff and the six unrated listings.
  - 56 were kept, which brings the total to 115 campsites with Google stats and 90 with pros and cons.
  - Where the listing is a lodge, resort, restaurant or bandas rather than the campsite itself, a scope note says so.
  - Kikopey Beach Camp's Google pin is 10 km from ours and Kianjata Springs' is 7 km. Check both pins.
- **Tripadvisor:** almost no Kenyan public campsites are listed. The two hits were other properties, so none was used.
- **Photos:** not embedded. Google and Tripadvisor photos belong to the people who posted them. Each card links to "Photos and reviews on Google Maps" instead. Up to five photo URLs per campsite are in the CSV (`photo_urls_to_license`) so you can request permission or shoot your own.
- **Apify usage:** the account was at $90.18 when the limit was raised to $100; after the second pass it stands at $92.10. The cycle resets on 12 Oct.

## Data file
`kenya-campsites-database.csv` holds every campsite and every researched field with its source URLs, plus Google rating, review count, Maps link, review summary, pros/cons and photo URLs to license (the confidence column is removed). It's suitable for Airtable or a future map plugin.

## Open items for Nathan
1. **Provenance of the source map.** Confirm the "Campsites en Route" layer is Kambu's own data.
2. **Unconfirmed campsites.** 36 profiles carry an "unconfirmed" status. A phone round to the private operators would settle most of them. They are all in the CSV.
3. **KWS fee litigation.** The page treats LN 160 as current, with the court note. Check against your saved tariff file.
4. **Narok County rates for Kenyan citizens.** Sources conflict, so both figures are shown. Mara Triangle ranger fees aren't readable online.
5. **Mapbox token.** It sits in the source by design; restrict it to kambucampers.com and staging9. The interactive map uses `outdoors-v12`; switch to `light-v11` with the `data-mbstyle` attribute if you prefer the plainer look.
6. **Photographs.** Watermarking is on Kambu-made maps only. Each placeholder photo has `data-own="false"`; add class `kcm__own` to its figure once a Kambu photo replaces it.
7. **Keyword data.** None was used: Ahrefs' plan excludes it and no SE Ranking key was supplied.
8. **Page length.** The page runs to 187 profiles (~85,000 px tall on desktop). If that's too long, the profiles could become a collapsed list per region, at some cost in crawlable depth.
9. **Your KWS fees page.** It gives the 2024 Premium non-resident fee as USD 60 in its intro but USD 43 in its table. Fix one of them.
