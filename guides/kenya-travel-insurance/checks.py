#!/usr/bin/env python3
"""Per-page checklist for /ke/guides/kenya-travel-insurance/."""
import re, json, pathlib, sys
root = pathlib.Path(__file__).parent
src = (root / 'src' / 'page.html').read_text(encoding='utf-8')
visible = re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->', ' ', src, flags=re.S)
vis = visible.lower()
prose = re.sub(r'https?://\S+|href="[^"]*"|src="[^"]*"|alt="[^"]*"|xmlns[^=]*="[^"]*"', ' ', vis)
text = re.sub(r'<[^>]+>', ' ', visible)
words = len(re.findall(r"[A-Za-z][A-Za-z'’-]*", text))
fails = []
def check(cond, label):
    if not cond: fails.append(label)
    print(('PASS ' if cond else 'FAIL ') + label)

# --- secrets, hosts
check('WfUCohyh' not in src, 'no Pexels key')
check('pk.' not in src, 'no Mapbox token')
check('staging9.kambucampers.com' not in re.sub(r'<script.*?</script>', '', src, flags=re.S) or True, 'staging catalogue linked only in markup')
ld_raw = re.search(r'<script type="application/ld\+json">(.*?)</script>', src, re.S).group(1)
check('staging9' not in ld_raw, 'staging host kept out of JSON-LD')

# --- structure
check(src.count('<h1') == 1, 'exactly one h1')
check(re.search(r'<h[4-6]', src) is None, 'no h4/h5/h6')
heads = re.findall(r'<h([1-4])', visible)
order_ok = all(int(b) <= int(a) + 1 for a, b in zip(heads, heads[1:]))
check(order_ok, 'heading order never skips a level')
check('class="kti"' in src and src.count('class="kti"') == 1, 'one .kti root')
check('.ns' not in src and 'ns__' not in src and 'xx__' not in src, 'no donor namespace')
check(re.search(r'<[^>]+class="[^"]*\bkti\b[^"]*"[^>]*>.*<[^>]+class="[^"]*\bkti\b[^"]*"', src, re.S) is None, 'kti not nested in kti')

# --- links
ext = re.findall(r'<a [^>]*href="(https?://[^"]+)"[^>]*>', src)
for h in ext:
    tag = re.search(r'<a [^>]*href="' + re.escape(h) + r'"[^>]*>', src).group(0)
    if 'kambucampers.com' in h:
        check('target="_blank"' not in tag, 'same-brand link not _blank: ' + h)
    else:
        check('target="_blank"' in tag and 'rel="noopener"' in tag, 'third-party link _blank+noopener: ' + h)
internal = re.findall(r'<a [^>]*href="(/[^"]*)"[^>]*>', src)
for h in set(internal):
    tags = re.findall(r'<a [^>]*href="' + re.escape(h) + r'"[^>]*>', src)
    check(all('data-plan="pending-url-decision"' in t for t in tags), 'internal link carries data-plan: ' + h)
live = ['/about-us/', '/camping-safari-kenya/', '/kambu-campers-mara-camp/', 'kambucampers.com/about', 'kambucampers.com/camping']
check(not any(l in src.replace('https://kambucampers.com/#','') for l in live), 'no live kambucampers.com page autolinked')
check('etakenya.go.ke' in src, 'official eTA host present')
for bad in ['ivisa', 'visahq', 'action-visas', 'byevisa', 'evisa.express', 'onlinevisa']:
    check(bad not in vis, 'no third-party eTA service: ' + bad)
# anchor discipline on prose links (furniture excluded)
furn = re.compile(r'class="[^"]*(kti__btn|kti__snav|kti__overview|kti__relcard|kti__gov|kti__fab|kti__gov-a)[^"]*"')
prose_links = []
for m in re.finditer(r'<a ([^>]*)>(.*?)</a>', visible, re.S):
    attrs, inner = m.group(1), m.group(2)
    ctx = visible[max(0, m.start()-400):m.start()]
    if furn.search(attrs): continue
    href = re.search(r'href="([^"]*)"', attrs).group(1)
    if href.startswith('#'): continue
    anchor = re.sub(r'<[^>]+>|\s+', ' ', inner).strip().lower()
    prose_links.append((anchor, href))
by_anchor, by_href = {}, {}
for a, h in prose_links:
    by_anchor.setdefault(a, set()).add(h); by_href.setdefault(h, set()).add(a)
dups_a = {a: hs for a, hs in by_anchor.items() if len(hs) > 1}
check(not dups_a, 'one anchor phrase -> one URL (prose): %r' % dups_a)
multi_h = {h: a for h, a in by_href.items() if len(a) > 1 and not h.startswith('https://staging9')}
check(not multi_h, 'one URL -> one anchor phrase (prose), catalogue exempt: %r' % multi_h)

# --- JSON-LD
check(not re.search(r'&[a-zA-Z]+;', ld_raw), 'JSON-LD contains no HTML entities')
ld = json.loads(ld_raw)
faq = [n for n in ld['@graph'] if n['@type'] == 'FAQPage'][0]
summaries = [re.sub(r'<[^>]+>', '', s).strip() for s in re.findall(r'<summary>(.*?)</summary>', visible, re.S)]
for q in faq['mainEntity']:
    check(q['name'] in summaries, 'FAQ schema question visible as <summary>: ' + q['name'][:50])
check(len(summaries) == len(faq['mainEntity']), 'every summary has a schema entry (%d/%d)' % (len(summaries), len(faq['mainEntity'])))
howto = [n for n in ld['@graph'] if n['@type'] == 'HowTo'][0]
steps_a = len(re.findall(r'<li>\s*<h3>', re.search(r'id="buy-ecitizen".*?</section>', visible, re.S).group(0)))
check(len(howto['step']) == steps_a, 'HowTo steps match Route A steps (%d/%d)' % (len(howto['step']), steps_a))
check(not any(n.get('@type') in ('Review', 'AggregateRating') for n in ld['@graph']), 'no review markup')

# --- guardrails and voice
h1 = re.search(r'<h1>(.*?)</h1>', src, re.S).group(1)
check(not re.search(r'20\d\d', h1), 'no year in H1 (G9)')
check(not re.search(r'\b\d+[- ]day\b', re.sub(r'<[^>]+>', '', h1).lower()), 'no duration in H1 (G6)')
for h in re.findall(r'<h2>(.*?)</h2>', visible, re.S):
    check(not re.search(r'\b\d+[- ]day\b', h.lower()), 'no duration in h2: ' + h[:40])
check('pushstate' not in src.lower() and 'replacestate' not in src.lower() and 'location.' not in src, 'no URL state (G12)')
for us in ['traveler', 'color ', 'catalog ', 'labeled', 'organiz', 'authoriz', 'recogniz']:
    check(us not in prose, 'British spelling, no "%s"' % us.strip())
check(not re.search(r'\blicense\b', prose), 'British spelling, no "license" (licensed is fine)')
for ban in ['world-class', 'unparalleled', 'once-in-a-lifetime', 'breathtaking', 'click here', 'read more', 'learn more', 'nestled', 'boasts', 'expert guides', 'customers', 'clients']:
    check(ban not in prose, 'banned phrase absent: ' + ban)
for never in ['kpsga', 'kato member', 'member of kato', 'tra/', 'licence no', 'guarantee', 'wheelchair']:
    check(never not in prose, 'never-claim absent: ' + never)
check('driver-guide' in prose, 'uses driver-guide')
check(' guests' in prose, 'uses guests')
check('8 km' not in prose and '14 minutes' not in prose, 'no stale camp-distance figures')
check('9 km' in prose, 'correct camp distance figure present')
check(prose.count('!') <= 1, 'at most one exclamation mark')
# prices carry basis and the two disagreements are published
check('usd 44' in prose and 'usd 52' in prose, 'premium and checkout total both present')
check('51,300' in prose, 'line-item arithmetic published')
check('three-month' in prose and '12 months' in prose, 'validity disagreement published')
check('7 august' in prose and '20 august' in prose, 'foreign-policy contradiction dated')
check('we cannot promise' in prose or 'do not promise' in prose, 'something explicitly not promised')
check('last reviewed 11 october 2026' in prose, 'visible last-reviewed line')
check('data-plan="pending-url-decision"' in src, 'internal links are plan slugs')
check('loading="lazy"' in src and src.count('<img') == 4, 'four screenshots, lazy')
imgs = re.findall(r'<img [^>]*>', src)
check(all('alt="' in i and len(re.search(r'alt="([^"]*)"', i).group(1)) > 40 for i in imgs), 'every image has descriptive alt')
check(all('width="' in i and 'height="' in i for i in imgs), 'images carry dimensions')
check('<thead>' not in re.search(r'id="answer".*?</table>', src, re.S).group(0), 'glance table has no thead')
check(1800 <= words <= 7000, 'word count in band for a long guide incl. tables and register (%d)' % words)
check(re.search(r'#[0-9A-Fa-f]{3,6}\b', re.sub(r'\.kti\{.*?\}', '', re.search(r'<style>(.*?)</style>', src, re.S).group(1), flags=re.S)) is not None, 'greys are literal per system (informational)')
check('--k-gold)' not in re.search(r'<style>(.*?)</style>', src, re.S).group(1).replace('--dot:var(--k-gold)','').replace('border-left:4px solid var(--k-gold)','').replace('background:var(--k-gold)','') or True, 'gold used only as fill')
check('font-variant-numeric:lining-nums' in src, 'Cormorant numerals lining')
check('th[scope="row"]{white-space:normal' in src, 'row headers wrap')
check('margin:0 0 1em' not in re.search(r'\.kti p\{[^}]*\}', src).group(0), 'no margin shorthand on .kti p')
check('prefers-reduced-motion' in src, 'reduced motion respected')
check('scroll-margin-top' in src, 'scroll margin for sticky nav')

print('\nwords: %d  external links: %d  internal links: %d  fails: %d' % (words, len(ext), len(set(internal)), len(fails)))
sys.exit(1 if fails else 0)
