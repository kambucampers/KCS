# Pricing

Every price on the site is generated from `src/data/pricing.ts`. Nothing is hard-coded into a
page, so changing one number there updates the price tables, the "from" figures, the comparison
table on `/tours/` and the schema.org offers on the next build.

## Method

```
market price per person = (vehicle and guide day rate + entry fees x travellers) / travellers
listed price per person = market price x MARKUP, rounded to the nearest USD 5
```

`MARKUP` is `1.2`, the 20 percent uplift on comparable market rates.

Two components feed it:

1. **Entry fees**, charged per person per day at published non-resident rates.
2. **Vehicle day rate**, the private vehicle, fuel, driver guide and tolls for the whole day,
   charged once and shared by everyone in the car. This is why the per-person price falls
   steeply with group size while the fee portion does not.

## Entry fees used (non-resident adult, 2026)

| Item | USD per person per day |
| --- | --- |
| Nairobi National Park conservation fee | 80 |
| Lake Nakuru National Park | 90 |
| Amboseli National Park | 90 |
| Hell's Gate National Park | 30 |
| Mount Longonot | 30 |
| Ngong Hills | 12 |
| Sheldrick elephant orphanage | 12 |
| Giraffe Centre | 12 |
| Karen Blixen Museum | 10 |
| Bomas of Kenya | 10 |
| Naivasha boat ride and Crescent Island walk | 45 |

Kenya Wildlife Service raised park rates for 2025/2026 and moved collection to eCitizen. The
Nairobi National Park non-resident rate rose from about USD 43 to USD 80, which is why these
prices sit above older published tour rates. Citizens and East African residents pay
substantially less, which is why the site asks about residency before confirming.

## Vehicle and guide day rates used

| Day type | USD, whole vehicle |
| --- | --- |
| Nairobi half day, about 5 hours | 170 |
| Nairobi full day, about 9 hours | 250 |
| Layover, timed to the connection | 190 |
| Rift Valley day trip, Naivasha and Hell's Gate | 320 |
| Lake Nakuru day trip | 340 |
| Amboseli day trip | 420 |
| Mount Longonot day | 280 |
| Ngong Hills day | 190 |

## Resulting listed prices, USD per person

| Tour | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Nairobi NP half-day game drive | 300 | 200 | 165 | 145 | 135 | 130 |
| Nairobi NP full day with Karen | 435 | 285 | 235 | 210 | 195 | 185 |
| City excursion, half day | 245 | 145 | 110 | 90 | 80 | 75 |
| City excursion, full day | 355 | 205 | 155 | 130 | 115 | 105 |
| Naivasha and Hell's Gate | 475 | 280 | 220 | 185 | 165 | 155 |
| Lake Nakuru | 515 | 310 | 245 | 210 | 190 | 175 |
| Amboseli | 610 | 360 | 275 | 235 | 210 | 190 |
| Layover, game drive | 325 | 210 | 170 | 155 | 140 | 135 |
| Layover, city | 255 | 145 | 105 | 85 | 75 | 65 |

## Market anchors these were checked against

Advertised 2026 rates for comparable day tours from Nairobi:

- SafariBookings day-trip listings for Nairobi National Park, roughly USD 162 to 205 per person,
  with some operators to USD 305: https://www.safaribookings.com/tours/nairobi-np/day-trips
- Combined park, orphanage and Giraffe Centre day tours quoted per group, from USD 260 for one
  traveller down to about USD 56 per person at eight
- Naivasha and Hell's Gate day trips advertised from about USD 150 to 239 per person
- Lake Nakuru day trips from about USD 150 to 180 per person plus park fees
- Amboseli day trips from about USD 150 to 200 per person
- JKIA layover tours advertised from about USD 90 to 165 per person, or from USD 160 per vehicle
- Nairobi National Park non-resident conservation fee, USD 80 for 2026

Sources consulted: SafariBookings day-trip listings, Viator and GetYourGuide private departures
for Nairobi, and published Kenya Wildlife Service and attraction rates as reported by
masaimara.travel, nairobipark.org, lakenakurupark.org, ajkenyasafaris.com, sojournsafaris.co.ke
and jkiairport.com.

## To change prices

- Adjust one number in `src/data/pricing.ts` and rebuild.
- To drop the markup to cost, set `MARKUP = 1`.
- To add a new tour option, add an entry to `options` and pass its key in the page's `priceKeys`.
