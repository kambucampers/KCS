# Assumptions to confirm

The site no longer carries placeholders. To get there, some operating details had to be stated
rather than left blank. Everything below is a decision made on your behalf. Correct any of it and
the change is a one-line edit in the file named.

## Prices

All prices come from published market rates plus a 20 percent markup, computed in
`src/data/pricing.ts`. The method, the fee and vehicle components, the resulting tables and the
sources are in `PRICING.md`. These are market-derived prices, not rates you have confirmed, so
read that file before the site goes live.

## Operating details stated on the site

| Statement | Where it lives |
| --- | --- |
| Prices include park and attraction entry at non-resident rates | `src/data/pricing.ts`, tour pages |
| Private departures only, no seat-in-vehicle sharing | `src/pages/tours/index.astro` |
| Vehicles have pop-up roofs, bottled water and binoculars on board | tour page `included` arrays |
| Half day about 5 hours, full day about 9 hours | `src/data/site.ts` |
| Day trips run 11 to 14 hours | `src/data/site.ts` |
| Minimum layover accepted is 6 hours between flights | `src/pages/tours/airport-layover-tours.astro` |
| Cabin bags travel in the vehicle, checked bags go to JKIA left luggage | layover page FAQ |
| Child seats fitted on request, no wheelchair-accessible vehicle as standard | `src/pages/plan-your-day.astro` |
| Replies within one working day | `src/data/terms.ts`, contact page |

## Booking terms stated on the site

Set once in `src/data/terms.ts` and quoted on the contact, tours and about pages:

- 30 percent deposit to confirm, balance on the morning of the tour
- Bank transfer, M-Pesa, or cash in US dollars or Kenyan shillings
- Free cancellation more than 7 days ahead, 50 percent refund 3 to 7 days ahead, no refund inside
  72 hours
- Full refund if Nairobi Adventures cancels, or if a flight delay makes a layover tour unsafe

## Deliberately absent

These are not on the site because inventing them would misrepresent the business:

- **Phone or WhatsApp number.** Add it to `src/data/site.ts` and it appears in the footer, the
  contact page and the LocalBusiness schema automatically.
- **Founding story.** No date, founder or history is claimed anywhere.
- **Licensing, registration, insurance and industry membership.** No such claim is made. Send the
  real details and they belong on the about page, where they carry the most weight.
- **Testimonials, review counts and star ratings.** None are fabricated. Real reviews can be
  added later with `Review` schema.
- **Office address and opening hours.** The contact page states a reply time instead.

## Photography

Images are fetched by `npm run media` from Wikimedia Commons and the Pexels API. They are
generic Kenyan and Nairobi photography, correctly attributed, standing in until you supply
photographs of your own vehicles, guides and guests. Replacing a fetched file with your own
photograph of the same name in `public/images/` is enough; edit the credit in
`src/data/media.json` or delete that entry's credit fields when the photograph is yours.
