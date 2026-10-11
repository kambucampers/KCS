# Sarova Mara Game Camp — accommodation guide

- **Staging URL:** https://staging9.kambucampers.com/accommodation/sarova-mara-game-camp/
- **Proposed live URL:** https://kambucampers.com/accommodation/sarova-mara-game-camp/ (confirm against the URL map)
- **Kambu stay class:** In-park (inside Masai Mara National Reserve, 2.4 km past Sekenani Gate)
- **Design system:** Executive Elegant, namespace `.kac` (reusable accommodation template)
- **SEO title:** Sarova Mara Game Camp Guide: Tents, Location & Rates
- **Meta description:** Sarova Mara Game Camp sits 2.4 km inside Sekenani Gate. Compare Deluxe, Club and Family tents, 2026 rate references, reserve fees and how Kambu books it.

## Files
- `block.html` — paste-ready Custom HTML block (CSS, JS and JSON-LD inline)
- `data-2026-10-11.json` — ratings, review stats and live rates pulled via Apify on 11 Oct 2026
- `images/` + `image-manifest.csv` — Sarova Hotels' own photos (via Booking.com / Tripadvisor) with alt text, for re-hosting in WP Media

## Open before going live
1. Confirm trade-media permission with Sarova for the camp photos; re-host them in WP Media and swap the CDN URLs.
2. SE Ranking keyword volumes/intent not yet pulled (Data API key needed).
3. Internal links: Kambu Mara Camp, Sekenani Gate and park-fees pages need their final URLs.
4. Block loads Google Fonts, Leaflet (on demand) and external images — not fully self-contained per CONVENTIONS.
5. Rates are dated references (Booking.com 3–5 Nov 2026, scraped 11 Oct 2026); refresh before promoting.
