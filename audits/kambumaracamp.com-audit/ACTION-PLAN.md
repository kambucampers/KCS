# Action plan: kambumaracamp.com

## Critical (this week)
1. **Get the `/v2/` site out of the index.** If it's a redesign in progress, move it to a staging site. Otherwise set every `/v2/` page to noindex and exclude them from the BeyondSEO sitemap. When v2 replaces the live site, 301-redirect each `/v2/x/` to `/x/`.
2. **Delete the WordPress default content:** the Hello World post, Sample Page and `/10-2/`. Then remove the empty Uncategorized category from the sitemap. Check the sitemap afterwards to confirm they're gone.

## High (within 1–2 weeks)
3. **Keep only one source of tags.** Keep the theme's hand-written descriptions, or move them into BeyondSEO, and turn off the meta and Open Graph output from the other sources. The goal is one title, one description, one canonical and one og:title per page.
4. **Rewrite titles.** Change the site title to "Kambu Mara Camp". Set the homepage title to something like "Kambu Mara Camp: Affordable Tented Camp near Sekenani Gate, Masai Mara". Keep page titles under about 60 characters.
5. **Turn on analytics.** Connect GA4 in MonsterInsights, add the site to Google Search Console, and submit `https://kambumaracamp.com/sitemaps.xml`.
6. **Merge the schema into one block.** Remove the empty-name Organization, set Organization `name` to "Kambu Mara Camp", keep a single BreadcrumbList, and add `image`, `sameAs` and check-in/check-out times to the Campground.

## Medium (within a month)
7. Add `og:image`: a default image plus one per page (1200×630).
8. Hide the WordPress username: change the display name so `Admin-JQPbu` no longer appears in the `author` meta tag.
9. Divide topics between kambucampers.com and kambumaracamp.com. Decide which site ranks for "3-day Masai Mara safari" and for the camp itself. Point the other site's page to it, with a link and a cross-domain canonical or a 301.
10. Use the same review figures on both sites.
11. Make `/reviews/` smaller: paginate or load in batches, aiming for under about 60 images on first load.

## Low and ongoing
12. Disable XML-RPC if nothing uses it.
13. Use one font service, self-hosted.
14. Check real Core Web Vitals in PageSpeed Insights or Search Console once a month.
15. Optional: add `/llms.txt` summarising the camp's facts.
