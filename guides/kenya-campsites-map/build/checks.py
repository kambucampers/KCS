import re, json, sys, html
src = open(sys.argv[1]).read()
ok = []; bad = []
def T(name, cond):
    (ok if cond else bad).append(name)
visible = re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->', ' ', src, flags=re.S)
vis = html.unescape(re.sub(r'<[^>]+>', ' ', visible)).lower()
prose = re.sub(r'https?://\S+', ' ', vis)
T('ascii only', all(ord(c) < 128 for c in src))
import os
tok = os.environ['MAPBOX_TOKEN']
T('only the Mapbox pk token, once, in data-mbtoken', src.count('pk.eyJ') == 1 and 'data-mbtoken="%s"' % tok in src)
T('no secret token (sk.)', 'sk.eyJ' not in src)
T('no access_token literal outside JS builder', src.count('access_token=') == 1)
T('no Pexels key', 'wfucohyh' not in src.lower())
T('no KATO', 'kato' not in src.lower()); T('no KPSGA', 'kpsga' not in src.lower())
T('one h1', len(re.findall(r'<h1[\s>]', src)) == 1); T('no h4', '<h4' not in src)
for t in ['div', 'section', 'details', 'table', 'ul', 'ol', 'figure', 'a', 'p']:
    T('balance ' + t, len(re.findall(r'<%s[\s>]' % t, visible)) == len(re.findall(r'</%s>' % t, visible)))
ids = re.findall(r'\sid="([^"]+)"', src); T('unique ids', len(ids) == len(set(ids)))
lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
T('one ld+json', len(lds) == 1)
raw = lds[0]; T('ld no entities', not re.search(r'&[a-zA-Z]+;', raw))
g = json.loads(raw)
faq = [n for n in g['@graph'] if n['@type'] == 'FAQPage'][0]
sums = [html.unescape(s) for s in re.findall(r'<summary>(.*?)</summary>', src)]
T('faq questions visible', all(q['name'] in sums for q in faq['mainEntity']))
T('staging host not in graph', 'staging9' not in raw)
anchors = re.findall(r'<a\s([^>]*)>', visible)
for a in anchors:
    h = re.search(r'href="([^"]*)"', a).group(1)
    if h.startswith('#') or h.startswith('mailto:'): continue
    if h.startswith('/'):
        if 'data-plan="pending-url-decision"' not in a: bad.append('internal no data-plan ' + h)
    elif 'kambucampers.com' in h and 'staging9' not in h:
        bad.append('live kambu autolink ' + h)
    else:
        if 'target="_blank"' not in a or 'rel="noopener"' not in a: bad.append('external w/o blank ' + h)
T('no history API', not re.search(r'pushState|replaceState|location\.(href|search|hash)\s*=', src))
for w in ['budget', 'luxury', 'world-class', 'unparalleled', 'nestled', 'boasts', 'click here', 'read more', 'learn more', 'we guarantee', 'guaranteed sighting', 'evisa', 'e-visa', 'expert guides', ' customers ']:
    T('no "%s"' % w, w not in prose)
for us in ['color ', 'center ', 'traveler', 'favorite', 'organize', 'catalog ', 'license ']:
    T('british: no "%s"' % us.strip(), us not in prose)
T('fees basis sentence', 'per person per night' in prose)
T('last reviewed', 'last reviewed 11 october 2026' in prose)
T('placeholders marked', src.count('data-placeholder="true"') >= 8)
T('every img alt', all('alt="' in i for i in re.findall(r'<img[^>]*>', src)))
T('reduced motion', 'prefers-reduced-motion' in src)
T('no blank lines (wpautop)', not re.search(r'\n\s*\n', src.split('<!-- wp:html -->', 1)[1]))
words = len(re.findall(r"[a-z0-9']+", prose)); T('word count >= 3500', words >= 3500)
# KWS table holds KWS only
fees = re.search(r'id="costs".*?</table>', src, re.S).group(0).lower()
T("fee table KWS only", "pejeta" not in fees and "triangle" not in fees and "narok" not in fees)
for bd in ["masaimara.ke","masaimarasafari.travel","tourwithpipi.com","maramasai.com","masaimara.or.ke","marareserve.org","masaimara.travel","kenyatourism.in","masai-mara.in","masaimara.co.ke","masaimarasafari.in","masaimara.com/","samburureserve.org"]: T("no banned "+bd, bd not in src)
T("16 region anchors", len(re.findall(r"<section class=\"kcm__sec[^\"]*\" id=\"[a-z-]+-campsites\"", src))==16)
T("no live kambu <a> links", not re.search(r"<a [^>]*href=\"https://kambucampers.com", visible))
print('words', words, '| passed', len(ok), '| failed', len(bad))
for b in bad: print('FAIL', b)
