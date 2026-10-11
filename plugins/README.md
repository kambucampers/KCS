# Kambu Campers visitor-facing WordPress plugins

Loaded 11 October 2026 from the Google Drive of bookings@kambucampers.com. These are
**snapshots**, not the working copies. The working copies are local git repos on the Mac
with no remote (`~/kambu-safari-local-v2/wp-plugin/`, about 50 plugins) and cannot be
reached from a cloud session. See "Loading the rest" at the end.

## What is here

| Folder | Plugin | Snapshot version | Mac version | Role for visitors |
|---|---|---|---|---|
| `kambu-safaris/` | Kambu Campers Safari Booking | 2.0.0 (5 Sep 2026) | 5.3.0 | `[kambu_safaris]` booking tool, `[kambu_safaris_browse]` catalogue, `[kambu_safaris_map]` planner. 61 safaris, live party-size pricing. |
| `kambu-product-assets/` | Kambu Product Page Assets | 1.0.0 (18 Sep 2026) | same | Enqueues the shared `.kpm` product-page CSS/JS once, on pages whose content carries `class="kpm"`. |
| `kambu-static-content-publisher/` | Kambu Static Content Publisher | 1.0.0 (10 Sep 2026) | unknown | Publishes 14 self-contained guide blocks (booking direct vs agent, hidden costs, Diani to Mara, etc.) as posts or pages, bypassing Gutenberg and `wpautop`. |

Each folder has a `DRIVE-SOURCES.md` naming the files that were **not** loaded (HTML fragments,
CSS, JS, content blocks) with their Drive file ids.

Not loaded, deliberately, because they are not visitor-facing: the Drive folder
"Kambu Plugins for Staff and Suppliers" (`kambu-safari-log-wordpress.zip`,
`kambu-cashbook-generatepress.zip`, `kambu-supplier-portal.zip`), `kambu-driver-availability.php`
and `kambu-enquiry-responder.zip`. Also not loaded: the plugins that exist only on the Mac
(`kambu-campers-maps`, `kambu-product-pages` (superseded), the ~45 destination, duration and
theme hub plugins, and the 27-product plugin being built from `VSCODE-PROMPT-27-PLUGIN.md`).

## Review

Run against `engineering/CONVENTIONS.md` (pass 1), then correctness and security (pass 2).
Pass 3 (page quality) could not run: the rendered HTML fragments and guide blocks were not loaded.

### Convention failures (blocking)

| # | Where | Issue |
|---|---|---|
| C1 | `kambu-product-assets.php` whole design | Deliberately breaks the "everything inline, self-contained" rule by serving the `.kpm` CSS and JS as two separate enqueued files. `SHARED-ASSETS.md` in Drive argues the case (125 KB vs 174 KB per page, cached across pages). Same-origin, not a third-party request, so the intent of the rule holds; but it is a documented exception and should be recorded as a decision, not left implicit. |
| C2 | `kambu-static-content-publisher/manifest.json` item 6 | Title "Kenya Safari Budget by Duration", slug `kenya-safari-budget-by-duration`. "Budget" here is a cost concept, not a tier label, so it is probably fine, but it needs a deliberate check against the "budget is not a tier label" rule before it is published. |
| C3 | `kambu-safaris.php` lines 29, 52, 67 | WhatsApp fallback number `+254 769 103 670` matches the house CTA. Pass. The 135 KB fragment it returns was not reviewable; its CSS scoping (`.kjs-root`), fonts and JSON-LD are unverified. |

### Bugs and risks

| # | Where | Issue | Severity |
|---|---|---|---|
| B1 | `kambu-static-content-publisher.php` 100-103 | A manifest item with `type: page` and **no slug** resolves `$existing` to `page_on_front`, so a re-sync silently overwrites the live homepage's content with `[kambu_static_content]` and swaps its template. The current manifest avoids it only because the homepage entry has a slug. A footgun with no guard. | High |
| B2 | `kambu-static-content-publisher.php` 123, 128-129 | When the post is matched by its `_kambu_static_source` meta (the normal re-sync path), `post_status` is overwritten with the chosen status. Choosing "Create/update as drafts" on a second sync **unpublishes every live guide**. The slug and title match paths preserve the existing status; this one does not. | High |
| B3 | `kambu-static-content-publisher.php` 67-76 and `template-static.php` 8-17 | Fallback matches any singular post whose **title equals** a manifest title, even one the plugin never created. A page titled "Kambu Campers" (manifest item 1) anywhere on the site has its template hijacked and its content replaced by the homepage preview file. Match on the meta key only. | High |
| B4 | `kambu-static-content-publisher.php` 88-90 | `kambu_static_assign_template()` always writes `_wp_page_template = essential-blocks-fullwidth-template.php`. If Essential Blocks is not installed the editor shows a missing-template warning, and the value is dead anyway because `template_include` overrides it at `PHP_INT_MAX`. README claims "when that template is available"; the code does not check. | Medium |
| B5 | `kambu-static-content-publisher.php` 41-58 vs 60-86 | Two independent render paths do the same job: a `the_content` filter that replaces the content with the raw file, and a `template_include` swap that echoes the raw file directly. On a matched post only the template path runs (the template never calls `the_content`), so the filter is dead code on the intended path and live code only if `template-static.php` goes missing. Pick one. | Medium |
| B6 | `kambu-static-content-publisher.php` 131, 210 | `$item['slug']` read without `isset()`. A manifest item without a slug raises an "Undefined index" warning in the admin table and in `get_page_by_path()`. | Low |
| B7 | `kambu-product-assets.php` 18, 26 | Marker test is the exact string `class="kpm"`. A block written as `class="kpm kpm--wide"`, with single quotes, or served by a virtual route whose post content is only a shortcode gets **no CSS or JS**. Use a regex on `\bkpm\b` within a class attribute and wrap the result in `apply_filters('kambu_product_page_has_block', ...)` so routed pages can opt in. The 27-plugin brief already names this gap. | Medium |
| B8 | `kambu-safaris.php` 33-40 | The optional `sheet` attribute is only validated as starting with `https://docs.google.com/`; it is then injected as a `data-sheet` attribute, so pricing comes from whatever the editor pastes. `esc_attr()` prevents attribute break-out, so no XSS, but there is no server-side cache or fallback: if Google is slow or the sheet is unpublished the visitor sees whatever the fragment JS does on fetch failure, which was not reviewable here. | Medium |
| B9 | `kambu-safaris.php` 24-43 | No `Requires at least`, `Requires PHP` or `readme.txt`; no activation hook. Fine for a shortcode-only 2.0.0, but 5.3.0 registers rewrite rules and the brief asks for flush-on-activate, a rewrite-version constant and a kill switch. Confirm those exist in the Mac copy before shipping anything from here. | Low |

### Suggestions

| # | Where | Suggestion |
|---|---|---|
| S1 | all three | Add `Requires at least`, `Requires PHP`, `License` (static publisher has none) and `Text Domain` headers so the three read the same way in the Plugins list. |
| S2 | `kambu-static-content-publisher.php` 184-193 | The sync loop reports success per item but never reports which existing post id it matched and by what rule (meta, slug or title). Print the rule; B3 would have been visible in the admin notice. |
| S3 | `kambu-safaris.php` | The three shortcodes are the same function with a different filename and fallback string. One helper, three one-line registrations. |
| S4 | `kambu-product-assets.php` 42, 45 | `filemtime()` cache-busting is right. Consider `wp_register_*` plus `wp_script_add_data(..., 'defer')` only if the `.kpm` JS does not need DOM-ready ordering with inline `window.KambuPricing`; otherwise leave as is. |

### Good

- `kambu-static-content-publisher.php` admin page: nonce via `check_admin_referer`, capability via `current_user_can('manage_options')`, strict comparisons on `$_POST`, every echo escaped. The write path is correctly guarded.
- `basename()` on every manifest `source` before building a path. No traversal.
- `kambu-product-assets.php` is small, has one job, enqueues in the footer, and uses `filemtime()` so an upload is live at once.
- `kambu-safaris.php` degrades gracefully: a missing fragment yields a plain sentence with the WhatsApp number instead of a fatal.
- All four PHP files pass `php -l`.

### Verdict

**Fix first** for `kambu-static-content-publisher` (B1, B2, B3 before any further sync on the live site).
**Needs a decision** for `kambu-product-assets` (C1: record the shared-asset exception; B7: widen the marker before the 27-product plugin depends on it).
**Cannot ship-review** `kambu-safaris` from this snapshot: it is three major versions behind the Mac and its fragments were not loaded.

## Loading the rest

Everything below is on the Mac and not in Drive or GitHub. Any of these makes it reachable:

1. Push `~/kambu-safari-local-v2` (or just its `wp-plugin/` folder) to a GitHub repo and add
   it to the session. The conventions file says these repos "stay where they are", so a
   mirror remote is the smallest change.
2. Zip `wp-plugin/` and drop it into the Drive folder "Kambu Plugins for Staff and Suppliers"
   or a new "Kambu Plugins for Visitors" folder. Files above roughly 50 KB cannot be pulled
   through the Drive connector in one piece, so split zips per plugin.
3. Paste individual files into the chat.

Untracked gaps worth closing regardless: `kambu-product.js` is not in Drive at all, and the
only copy of `kambu-safaris` 5.3.0 is the Mac.
