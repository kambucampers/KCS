# Page blocks

Publication-ready WordPress **Custom HTML** blocks. Each file is self-contained:
scoped CSS, no build step, no external stylesheet, no framework. Paste the whole
file into one Custom HTML block on the target page.

| File | Page | Status |
|---|---|---|
| `homepage.html` | `/` — Private Kenya Safaris by Kambu Campers | Ready, pending photography and fact verification |

## homepage.html

Everything is scoped under `.kambu-wrap` and every class, id and custom property
is prefixed `kambu-`, so nothing can collide with Astra or another block.

### Interaction model

One primary interaction, three supporting, one navigation aid — per the
`kambu-semantic-content-architect` gate.

| Element | Pattern | Behaviour without JavaScript |
|---|---|---|
| Destination selector | Vertical side tabs, radio inputs + `:checked ~` selectors | Fully working — it never used script |
| Safari styles | Horizontal tabs (`role="tablist"`, arrow keys, Home/End) | Tab strip hides, all four panels stack as prose |
| Trip length | Same pattern, segmented control | As above |
| FAQs | Native `<details>` / `<summary>` | Fully working |
| Section rail | Sticky, `IntersectionObserver` scroll-spy | Plain anchor links |
| Orientation map | Optional Mapbox GL | Designed destination legend stands on its own |

Every panel's content is in the served HTML, so nothing is hidden from crawlers
or assistive technology. The direct answer, price basis, access notes and the
primary CTA all sit outside the interactive components.

### Before publishing

1. Replace the three `.kambu-imgslot` placeholders with original Kambu
   photographs — camp, vehicle, hero. Never stock imagery for owned assets.
2. Optional: paste a Mapbox **public** token into `KAMBU_MAPBOX_TOKEN`.
3. Set the domain in the JSON-LD graph if the site is not yet on
   `kambucampers.com`.
4. Verify the facts added on this build and listed at the foot of the file:
   the 8 km camp-to-gate distance, the fleet description, the accommodation
   ladder rates, and the per-destination "typical stay" figures.
5. If the theme header is sticky, raise `--kambu-sticky-top` so the section rail
   sits below it.

### Structured data

`TravelAgency` + `WebSite` + `FAQPage`, mirroring visible content only. No
`Product` or `Offer` markup on the homepage, per the publication controls.
