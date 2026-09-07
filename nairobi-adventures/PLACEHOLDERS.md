# Placeholders to fill before launch

Every item below is marked `[PLACEHOLDER: ...]` in the source. Nothing here was invented,
because guessing prices, durations or credentials would put wrong facts in front of customers.

## Business details (`src/data/site.ts`)

- Phone or WhatsApp number
- Office street address, if one is listed publicly
- Social profile URLs (Instagram, Facebook, Tripadvisor)

## Tour facts (`src/data/site.ts`)

- Nairobi National Park game drive: duration
- Nairobi city excursions: duration
- Day trips from Nairobi: typical departure and return times
- Airport layover tours: minimum layover length accepted

## Commercial terms

- Price range for LocalBusiness schema (`src/layouts/BaseLayout.astro`)
- Accepted payment methods, deposit requirements, cancellation policy (`/contact/`, `/tours/`)
- Response time to enquiries (`/contact/`)
- Whether shared or seat-in-vehicle departures are offered (`/tours/`)
- Whether prices include park and attraction entry fees, per tour page
- Amendment and refund policy for flight delays (`/tours/airport-layover-tours/`)
- Luggage arrangement during layover tours (`/tours/airport-layover-tours/`)
- Whether a day room, shower or restaurant stop can be arranged on a layover
- Whether an accessible vehicle or child seats can be arranged (`/plan-your-day/`)
- Office hours and time zone (`/contact/`)

## About page (`src/pages/about.astro`)

- Founding story: who started Nairobi Adventures, in what year, and why
- Verifiable credentials: company registration, tourism licensing, industry membership,
  insurance cover, guiding qualifications
- Fleet description: vehicle types, pop-up roofs, seat numbers, child seats

## Photography

Every image on the site is currently an illustrated placeholder with the alt text already
written. Replace with real photographs of:

- Wildlife with the Nairobi skyline behind (home hero and park tour)
- A game drive in progress
- The Giraffe Centre or the elephant orphanage
- Lake Naivasha, Hell's Gate or Lake Nakuru
- The vehicle at JKIA
- The team or guides
- Early morning light on the plains

## Adding real prices

Once rates are confirmed, add an `offers` block to the Product schema in
`src/layouts/TourPageLayout.astro` so prices are eligible for rich results, and replace the
duration placeholders in `src/data/site.ts`.
