import json, re, html, os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from maps2 import region_svg, national_svg, COL

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'sites4.json')))
KEN = json.load(open(os.path.join(HERE, 'kenya.json')))
CSS = open(os.path.join(HERE, 'base.css')).read() + open(os.path.join(HERE, 'base2.css')).read()
JS = open(os.path.join(HERE, 'page2.js')).read()
IMG = {i['title']: i for i in json.load(open(os.path.join(HERE, '..', 'img', 'chosen.json')))}
TOK = os.environ['MAPBOX_TOKEN']
esc = html.escape
GM = {int(k): v for k, v in json.load(open(os.path.join(HERE, '..', 'apify', 'gm_final.json'))).items()}
PC = {int(k): v for k, v in json.load(open(os.path.join(HERE, '..', 'apify', 'pros_cons.json'))).items()}
for _i, _s in enumerate(D['sites']):
    if _i in GM: _s['gm'] = GM[_i]
    if _i in PC: _s['pc'] = PC[_i]
def deconf(t):
    if not isinstance(t, str): return t
    t = re.sub(r'\s*[,;:\u2013\u2014-]*\s*(?:is\s+)?(?:very\s+)?(?:low|lower|medium|high)[- ]confidence\b', '', t, flags=re.I)
    t = re.sub(r'Price is\s*;?\s*confirm', 'Confirm the price', t)
    return re.sub(r'\(\s*\)', '', t).replace(' ,', ',').replace(',,', ',')
for _s in D['sites']:
    for _k in ('notes', 'se', 'acc', 'book', 'seas'):
        if _s.get(_k): _s[_k] = deconf(_s[_k])
    if _s.get('price'): _s['price']['basis'] = deconf(_s['price'].get('basis', ''))
SITES = D['sites']; CAMPS = [s for s in SITES if s['t'] != 'kmc']
REGIONS = D['regions2']; RNAME = {k: n for k, n, _ in REGIONS}; RSHORT = {k: sh for k, _, sh in REGIONS}
PEND = ' data-plan="pending-url-decision"'
BANNED = ['masaimara.ke', 'masaimarasafari.travel', 'tourwithpipi.com', 'maramasai.com', 'masaimara.or.ke', 'marareserve.org', 'masaimara.travel',
          'kenyatourism.in', 'masai-mara.in', 'masaimara.co.ke', 'masaimarasafari.in', 'masaimara.com', 'kambucampers.com', 'samburureserve.org']
WA = 'https://wa.me/254769103670'; CATALOGUE = 'https://staging9.kambucampers.com/safari-packages/'
URL = 'https://kambucampers.com/ke/guides/kenya-campsites-map/'

def ilink(href, text, evt=None):
    return '<a href="%s"%s%s>%s</a>' % (href, PEND, ' data-evt="%s"' % evt if evt else '', text)
def xlink(href, text, evt=None):
    return '<a href="%s" target="_blank" rel="noopener"%s>%s</a>' % (esc(href, quote=True), ' data-evt="%s"' % evt if evt else '', text)
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
def img_url(title, w=960):
    u = IMG[title]['thumb'].split('?')[0].replace('https://thumb.wikimedia.org/', 'https://upload.wikimedia.org/')
    return re.sub(r'/\d+px-', '/%dpx-' % w, u)
def credit(title):
    i = IMG[title]; return '%s, %s via Wikimedia Commons' % (esc(i['artist'].split(' from ')[0]), esc(i['lic']))
def hm(mins):
    h, m = divmod(int(mins), 60); return ('%d h %02d min' % (h, m)) if h else '%d min' % m
def fmt(n): return '{:,}'.format(n)

# ------------------------------------------------------------------ fees (LN 160 of 2025)
# order: EA citizen KES, Kenya resident KES, non-resident USD, African citizen USD ; (adult, child)
ENTRY = {'premium': ((1500, 750), (2025, 1050), (90, 45), (50, 25)), 'wildA': ((1000, 500), (1350, 675), (80, 40), (40, 20)),
         'wildB': ((800, 500), (1100, 675), (70, 40), (40, 20)), 'mountain': ((800, 400), (1100, 550), (70, 35), (30, 15)),
         'scenic': ((500, 250), (675, 350), (50, 25), (20, 10)), 'special': ((500, 250), (675, 350), (40, 20), (20, 10)),
         'sanct': ((300, 200), (405, 300), (25, 15), (15, 10)), 'marine': ((500, 250), (675, 350), (25, 15), (15, 10))}
CATNAME = {'premium': 'Premium', 'wildA': 'Wilderness A', 'wildB': 'Wilderness B', 'mountain': 'Mountain', 'scenic': 'Scenic',
           'special': 'Special interest', 'sanct': 'Sanctuary', 'marine': 'Marine'}
CAMPFEE = {('p', True): ((250, 200), (350, 250), (30, 25), (15, 13)), ('p', False): ((200, 150), (300, 200), (20, 15), (10, 8)),
           ('s', True): ((500, 250), (700, 350), (50, 25), (25, 15)), ('s', False): ((250, 200), (350, 250), (35, 20), (20, 10))}
VIS = ['East African citizen', 'Kenya resident', 'Non-resident', 'African citizen']
CUR = ['KES', 'KES', 'USD', 'USD']

def kws_cost(s):
    cat = s.get('kcat')
    if not cat: return None
    park, c = cat
    e = ENTRY[c]
    if s['t'] == 'mtn':
        return ('Park entry <b>USD %d</b> per non-resident adult or <b>KES %s</b> per Kenyan citizen adult for each 24 hours, plus the hut or camp fee charged by the operator (not published by KWS). Kenyan rules require a licensed guide on the mountain.' % (e[2][0], fmt(e[0][0])))
    kind = 'p' if s['t'] == 'kws-p' else 's'
    prem = c == 'premium'
    cf = CAMPFEE[(kind, prem)]
    nr = cf[2][0] + e[2][0]; ea = cf[0][0] + e[0][0]
    txt = ('Non-resident adult: USD %d camping + USD %d park entry = <b>USD %d per night</b>. Kenyan citizen adult: KES %s + KES %s = <b>KES %s</b>.'
           % (cf[2][0], e[2][0], nr, fmt(cf[0][0]), fmt(e[0][0]), fmt(ea)))
    if kind == 's':
        txt += ' Add the <b>KES 10,000</b> non-refundable reservation fee per week of exclusive use.'
    txt += ' Vehicle KES 600 per day (under 6 seats). %s band, LN 160 of 2025.' % CATNAME[c]
    return txt

def other_cost(s):
    a = s.get('a') or ''
    extra = ''
    if 'Ol Pejeta' in a:
        extra = ' Plus Ol Pejeta entry: USD 110 per non-resident adult or KES 2,000 per Kenyan citizen adult per 24 hours, and an armed ranger at KES 5,000 per night (2026 tariff).'
    elif 'Triangle' in a:
        extra = ' Plus the Mara Triangle conservation fee (a 12-hour ticket bought through KAPS; cashless). Campers must hire two rangers for the night.'
    elif 'Narok' in a or (s['t'] == 'mara'):
        extra = ' Plus reserve entry on the Narok County side: USD 100 (January to June) or USD 200 (July to December) per non-resident adult per 12 hours, per several 2026 secondary sources.'
    elif 'NRT' in a or 'Ngilai' in a or (s.get('b') == 'nrt'):
        extra = ' Rangers cost about KES 1,000 to 1,500 per day extra (The Big North).'
    p = s.get('price')
    if p and 'Triangle' in a:
        return '<b>USD 40</b> per non-resident adult per night (child USD 20); the booking system also lists KES rates for Kenyan citizens and East African residents. Seen 2026 (%s).%s' % (xlink(p['url'], 'source'), extra)
    if p:
        u = p.get('url') or ''
        src = '' if (not u or any(b in u for b in BANNED)) else ' (%s)' % xlink(u, 'source')
        return '<b>%s</b> %s, seen %s%s.%s' % (esc(p['amount']), esc(p['basis']).rstrip('.'), esc(str(p.get('seen') or 'n.d.')), src, extra)
    if s['t'] == 'kmc':
        return 'Quoted per booking; park fees are always itemised separately.'
    return 'No camping price published; ask the operator.' + extra

# ------------------------------------------------------------------ number sites per region
BYREG = {}
for k, _, _ in REGIONS:
    ss = sorted([s for s in SITES if s['g'] == k], key=lambda s: (s['s'] == 'closed', s['t'] == 'kmc', s['s'] != 'open', s['n']))
    for i, s in enumerate(ss): s['num'] = i + 1
    BYREG[k] = ss
for s in SITES:
    s['sid'] = 'site-' + slug(s['n'])
ids = [s['sid'] for s in SITES]; assert len(ids) == len(set(ids)), 'dup site ids'

N = len(CAMPS); N_OPEN = sum(1 for s in CAMPS if s['s'] == 'open'); N_TBC = sum(1 for s in CAMPS if s['s'] == 'tbc'); N_CLOSED = sum(1 for s in CAMPS if s['s'] == 'closed')
N_MOVED = sum(1 for s in CAMPS if s.get('coord') == 'moved'); N_PRICED = sum(1 for s in CAMPS if s.get('price') or kws_cost(s))
N_KWS = sum(1 for s in CAMPS if s['t'] in ('kws-p', 'kws-s', 'mtn'))
N_NAMED = sum(s['c'] for s in CAMPS)
def cnt(t): return sum(1 for s in CAMPS if s['t'] == t)
VEH = {}
for s in CAMPS: VEH[s.get('veh', 'unknown')] = VEH.get(s.get('veh', 'unknown'), 0) + 1
KWS_PARKS = sorted(set(s['kcat'][0] for s in CAMPS if s.get('kcat')))

TYPES = {'kws-p': 'KWS public campsite', 'kws-s': 'KWS special campsite', 'mtn': 'Mount Kenya hut camp (private operator)',
         'mara': 'Masai Mara reserve campsite', 'cons': 'Conservancy or ranch campsite', 'priv': 'Private campsite', 'kmc': 'Kambu Mara Camp'}
TSHORT = {'kws-p': 'KWS public', 'kws-s': 'KWS special', 'mtn': 'Mountain hut camp', 'mara': 'Masai Mara', 'cons': 'Conservancy', 'priv': 'Private', 'kmc': 'Kambu Mara Camp'}
STATUS = {'open': 'Operating', 'tbc': 'Unconfirmed', 'closed': 'Closed'}
VEHL = {'2WD ok': '2WD possible', '4WD recommended': '4WD recommended', '4WD required': '4WD required', 'boat': 'Boat access', 'on foot': 'On foot', 'unknown': 'Vehicle needs unknown'}

# ------------------------------------------------------------------ reviews (Google Maps via Apify, read 11 Oct 2026)
def review_line(s):
    g = s.get('gm')
    if not g or not g.get('score') or not g.get('cnt'): return ''
    return 'Google Maps: %.1f out of 5 from %s review%s' % (g['score'], fmt(g['cnt']), '' if g['cnt'] == 1 else 's')
def review_block(s):
    g = s.get('gm')
    if not g or not g.get('score'): return ''
    pc = s.get('pc')
    h = '<div class="kcm__rev"><p class="kcm__rev-h"><b>%.1f / 5</b><span>%s Google Maps review%s, read 11 Oct 2026%s</span> %s</p>' % (
        g['score'], fmt(g['cnt']), '' if g['cnt'] == 1 else 's', (' &middot; listing: %s' % esc(g['title'])) if g.get('title') and g['title'].lower() != s['n'].lower() else '',
        xlink(g['url'], 'Photos and reviews on Google Maps', 'reviews_link'))
    if pc:
        h += '<p style="margin:0">%s</p>' % esc(pc['summary'])
        if pc.get('scope_note'): h += '<p style="margin:4px 0 0;color:#5F655D;font-size:.78rem">%s</p>' % esc(pc['scope_note'])
        h += '<div class="kcm__pc"><div class="kcm__pro"><p>Reviewers like</p><ul>%s</ul></div><div class="kcm__con"><p>Reviewers flag</p><ul>%s</ul></div></div>' % (
            ''.join('<li>%s</li>' % esc(x) for x in pc['pros']), ''.join('<li>%s</li>' % esc(x) for x in pc['cons']))
        h += '<p style="margin:6px 0 0;color:#5F655D;font-size:.74rem">Summarised by Kambu Campers from %s.</p>' % esc(pc['basis'])
    elif g['cnt'] < 3:
        h += '<p style="margin:0;color:#5F655D;font-size:.8rem">Too few reviews to summarise.</p>'
    return h + '</div>'

def short_cost(s):
    if s['t'] in ('kws-p', 'kws-s', 'mtn') and s.get('kcat'):
        park, c = s['kcat']; e = ENTRY[c]
        if s['t'] == 'mtn': return 'Park entry USD %d per non-resident adult a day, plus the hut fee' % e[2][0]
        cf = CAMPFEE[('p' if s['t'] == 'kws-p' else 's', c == 'premium')]
        t = 'USD %d per non-resident adult a night incl. park entry (KES %s for Kenyan citizens)' % (cf[2][0] + e[2][0], fmt(cf[0][0] + e[0][0]))
        return t + (', plus the special-site reservation' if s['t'] == 'kws-s' else '')
    if 'Triangle' in (s.get('a') or '') and s.get('price'): return 'USD 40 per non-resident adult a night, plus reserve fee and rangers'
    p = s.get('price')
    if p:
        basis = re.split(r'[(;]', p.get('basis', ''))[0].strip().rstrip(',.')
        return '%s %s (%s)' % (p['amount'], basis[:60], p.get('seen') or 'n.d.')
    if s['t'] == 'kmc': return 'Quoted per booking'
    return 'Not published; ask the operator'

# ------------------------------------------------------------------ campsite card
def location_line(s):
    bits = []
    if s.get('a'): bits.append(esc(s['a']))
    if s.get('county'): bits.append('%s County' % esc(s['county'].replace(' County', '')))
    pa = s.get('pa_in') or []
    if not pa and s.get('pa_near') and s['pa_near'][1] <= 10:
        nm, dd = s['pa_near'][0].split('|'); bits.append('%.1f km outside the %s %s boundary' % (s['pa_near'][1], esc(nm), esc(dd)))
    alt = s.get('alt') or s.get('elev')
    t = '. '.join(bits) + ('. ' if bits else '')
    t += 'GPS %.5f, %.5f' % (s['la'], s['lo'])
    if alt: t += '. Altitude about %s m%s' % (fmt(int(round(alt, -1))), '' if s.get('alt') else ' (terrain model)')
    if s.get('coord') == 'moved': t += '. <b>Pin corrected</b>: %s' % esc((s.get('moved') or '')[:180])
    elif s.get('coord') == 'unconfirmed': t += '. Position not independently confirmed'
    return t + '.'

def drive_line(s):
    km, mins, snap = s.get('drv') or [None, None, None]
    if not km: return 'No road route found from Nairobi; ask the operator.'
    t = '%s km, about %s from Nairobi CBD (routed by Mapbox; murram sections usually take longer)' % (fmt(km), hm(mins))
    if snap and snap > 1500:
        if s.get('veh') == 'boat': t += '. The road ends about %.0f km away; the last stretch is by boat' % (snap / 1000)
        elif s.get('veh') == 'on foot' or s['t'] == 'mtn': t += '. The road ends about %.0f km away; the rest is on foot' % (snap / 1000)
        else: t += '. The nearest mapped road ends about %.0f km from the pin; the last stretch is an unmapped track' % (snap / 1000)
    return t + '.'

def card(s):
    off = s['s'] != 'open'
    tags = ['<span class="kcm__tag"><span class="kcm__t kcm__t--%s">%s</span></span>' % (s['t'], TSHORT[s['t']])]
    if s['s'] == 'tbc': tags.append('<span class="kcm__tag kcm__tag--warn">Unconfirmed status</span>')
    if s['s'] == 'closed': tags.append('<span class="kcm__tag kcm__tag--off">Closed</span>')
    if s.get('veh') and s['veh'] != 'unknown': tags.append('<span class="kcm__tag">%s</span>' % VEHL.get(s['veh'], esc(s['veh'])))
    alt = s.get('alt') or s.get('elev')
    if alt and alt > 2400: tags.append('<span class="kcm__tag">~%s m</span>' % fmt(int(round(alt, -1))))
    if s['t'] in ('kws-s',) or ('Ol Pejeta' in (s.get('a') or '')): tags.append('<span class="kcm__tag">Exclusive use</span>')
    cost = kws_cost(s) if s['t'] in ('kws-p', 'kws-s', 'mtn') else other_cost(s)
    if cost is None: cost = 'Park and camping fees: confirm with KWS.'
    acc = esc(s.get('acc') or 'No verified access description yet.')
    if s.get('road'): acc += ' Road: %s.' % esc(s['road'].rstrip('.'))
    book = esc(s.get('book') or 'Direct with the operator.')
    bu = s.get('burl')
    if bu and not any(b in bu for b in BANNED): book += ' ' + xlink(bu, 'Booking page', 'booking_link')
    if s['t'] == 'kmc':
        acc = 'On the Narok to Sekenani road, about 9 km before Sekenani Gate; game drives enter the reserve through Sekenani.'
        book = 'Through Kambu Campers: ' + ilink('/ke/kambu-mara-camp/', 'see the camp page') + ' or ' + xlink(WA, 'message us on WhatsApp', 'enquiry_start') + '.'
    name = esc(s['n'])
    alias = '<span class="kcm__alias">%s</span>' % esc(s['alias'][0].upper() + s['alias'][1:]) if s.get('alias') else ''
    det = []
    fac = s.get('fac')
    if fac: det.append('<p><b>Facilities listed:</b> %s.</p>' % esc(', '.join(fac)))
    elif s.get('f') == []: det.append('<p><b>Facilities:</b> none. Bring water, fuel and food.</p>')
    if s.get('seas'): det.append('<p><b>Seasonal:</b> %s</p>' % esc(s['seas']))
    if s.get('notes'): det.append('<p><b>Good to know:</b> %s</p>' % esc(s['notes']))
    if s.get('q'): det.append('<p><b>Checked:</b> %s</p>' % esc(s['q']))
    if s.get('se'): det.append('<p><b>Status evidence:</b> %s</p>' % esc(s['se']))
    srcs = [x for x in (s.get('src') or []) if x.get('url') and not any(b in x['url'] for b in BANNED)][:2]
    if srcs:
        det.append('<p class="kcm__srcs">Sources: %s.</p>' % '; '.join('%s (%s)' % (xlink(x['url'], esc((x.get('title') or 'source')[:56])), esc(x.get('grade', ''))) for x in srcs))
    detail = ('<details><summary>Facilities, notes and sources</summary><div class="kcm__ans">%s</div></details>' % ''.join(det)) if det else ''
    detail = review_block(s) + detail
    return ('<article class="kcm__site kcm__site--%s%s" id="%s" data-g="%s"><div class="kcm__site-h"><span class="kcm__pin" aria-hidden="true">%d</span><div><h3>%s</h3>%s</div></div>'
            '<div class="kcm__tags">%s</div><dl class="kcm__kv"><dt>Where</dt><dd>%s</dd><dt>Drive</dt><dd>%s</dd><dt>Access</dt><dd>%s</dd><dt>Cost</dt><dd>%s</dd><dt>Book</dt><dd>%s</dd></dl>%s</article>'
            % (s['t'], ' kcm__site--off' if off else '', s['sid'], s['g'], s['num'], name, alias, ''.join(tags), location_line(s), drive_line(s), acc, cost, book, detail))

# ------------------------------------------------------------------ region intros
INTRO = {
 'masai-mara-campsites': "Eleven of the reserve's campsites sit in the Mara Triangle and are booked online through the Mara Conservancy at USD 40 per non-resident adult per night (2026). Campers must hire two rangers for the night. Olakira and Tor's are on the Narok County side; Tor's now runs as a tented camp, so check before bringing your own tent.",
 'nairobi-campsites': "Nairobi's overland camps (Jungle Junction, Wildebeest Eco Camp, Indaba, Rowallan) are where most road trips start and finish. Within two to four hours are Ol Donyo Sabuk's Turacco public campsite, Mount Suswa's two community campgrounds (KES 1,000 per adult, cash only) and Swara Plains.",
 'lake-naivasha-campsites': "Hell's Gate has two public campsites that need no booking (Naiburta and Ol Dubai) and one special site, Endachata, booked through the warden or reservations@kws.go.ke. The south-shore private camps are reached on tarmac. KWS reported in July 2026 that rising water had pushed hippos into lakeshore areas, so stay in camp after dark.",
 'lake-nakuru-elementaita-campsites': "Lake Nakuru is a premium-fee park with one public campsite (Makalia) and seven special sites. KWS warns its campsites can flood, and the risen lake has submerged the old Main Gate. Soysambu Conservancy has three campsites near Lake Elementaita, and Kikopey, Eagles Point and Kembu are private.",
 'lake-bogoria-baringo-campsites': "Roberts Camp on the Lake Baringo shore is the confirmed option here (KES 800 per person, operator site, 2024). Korosin, Desert Rose, Netbon Kudu and Hannington near Lake Bogoria could not be confirmed as operating, so call ahead before driving the murram.",
 'aberdare-campsites': "The 2026 KWS Aberdare list names Reedbuck and Ruhuruini as public campsites, with special sites around Ruhuruini Gate (Nyati, Muringato, Kiguru) and near Shamata. Honi, Shamata public and Bill Woodley are no longer on KWS's list. Campsites sit at roughly 2,000 to 3,400 m, so nights are cold and tracks are often 4WD only.",
 'mount-kenya-campsites': "KWS lists Kisoi Munyao (at Naro Moru Gate), Kinondoni, Mathenge, Solo and Majors as Mount Kenya's public campsites, and camping is also reported at Sirimon Gate and Chogoria Road Head. The high camps on the trekking routes (Old Moses, Shipton's, Mackinder's, Met Station) are privately run huts that charge their own fee. KWS requires a licensed guide.",
 'mwea-sagana-campsites': "Mwea National Reserve, about four hours' drive from Nairobi, has Mbogo public campsite and special sites at Silvester and Mavuria. KWS's 2026 list names a Kiithesu site rather than Githechu. The Sagana river camps take campers alongside white-water rafting.",
 'laikipia-campsites': "Ol Pejeta's five campsites are exclusive-use at KES 3,500 per adult per night, plus conservancy entry and an armed ranger at KES 5,000 per night (2026 tariff). The Naibunga community sites cost KES 2,000 per adult through The Big North. Ngare Ndare Forest charges KES 3,000 for residents and KES 5,000 for non-residents, with a mandatory ranger.",
 'samburu-northern-kenya-campsites': "Most northern camping is on community conservancies (Westgate, Kalama, Sera, Nakuprat-Gotu, Ngilai) booked through The Big North, typically KES 2,000 per adult per night plus rangers. Several pins here were corrected by 5 to 19 km using OpenStreetMap campsite points. Lake Paradise in Marsabit is still listed by KWS.",
 'lake-turkana-campsites': "Central Island and South Island are KWS campsites reached only by boat; KWS lists South Island as a special campsite. On the shore, Eliye Springs on the west side (KES 1,500 per person, operator site) and Palm Shade at Loiyangalani on the east side take campers.",
 'meru-kora-campsites': "Meru's public campsite, Bwatherongi, lists water, toilets, a bathroom and a grill. Its special campsites line the Rojewero and Murera rivers, and KWS gives exact positions only on booking. Kora's Ekime special site is remote, with no facilities.",
 'amboseli-chyulu-campsites': "Amboseli has a single KWS public campsite in the premium fee band, so a night there costs a non-resident adult USD 120 in KWS fees. The Chyulu Hills have Kithasyo, Kiboko and Satellite public campsites. Elerai and Olchani, outside the park, are closed.",
 'tsavo-campsites': "Tsavo West has Komboyo, Chyulu and Lake Jipe public campsites plus special sites (Kudu, Palm Tree, Little Royal, Simba). Kenge, Professional and Tsavo East's Kanderi are not on the 2026 KWS lists. Tsavo East's public campsite is Ndololo near Voi Gate, and the Taita conservancies lie between the two parks.",
 'kenya-coast-campsites': "Coastal camping is thin. KWS says the Mombasa Marine park now has no camping, and most Shimba Hills sites are missing from the 2026 KWS list. The confirmed options are the KWS campsites at Malindi, at Shimoni (Kisite) and the Professional site in Shimba Hills, plus backpacker camping at Diani (KES 600 per person, 2026).",
 'western-kenya-campsites': "Western Kenya's KWS campsites are some of the best equipped: Kakamega Forest (Udo, Biota), Saiwa Swamp (Sitatunga) and Mount Elgon (Chorlim, Rongai, Nyati) list kitchens and bathrooms. KWS lists Ruma's Nyati as a special site; its public campsite is Fig Tree, which is not yet pinned.",
}
assert set(INTRO) == set(RNAME)

def rfacts(k):
    ss = [s for s in BYREG[k] if s['t'] != 'kmc']
    op = sum(1 for s in ss if s['s'] == 'open')
    drv = [s['drv'][1] for s in ss if s.get('drv') and s['drv'][1]]
    lo, hi = (min(drv), max(drv)) if drv else (None, None)
    tt = '%d&ndash;%d h' % (round(lo / 60), round(hi / 60)) if drv and round(lo / 60) != round(hi / 60) else ('%d h' % round(lo / 60) if drv else 'n/a')
    return ('<div class="kcm__rfacts"><div><b>%d</b><span>campsite pins</span></div><div><b>%d</b><span>confirmed operating</span></div><div><b>%s</b><span>routed drive from Nairobi</span></div></div>' % (len(ss), op, tt))

def region_section(i, k, name, short):
    ss = BYREG[k]
    uid = 'kcmr%d' % i
    svg = region_svg(ss, D['bounds'], name, uid)
    alt = 'exp' if i % 2 else 'plan'
    cards = ''.join(card(s) for s in ss)
    return ('<section class="kcm__sec kcm__sec--%s" id="%s" aria-labelledby="%s-h"><div class="kcm__in">'
            '<p class="kcm__chap"><b>%d</b> Region %d of %d</p>'
            '<h2 id="%s-h">%s</h2>'
            '<div class="kcm__rhead"><div><div class="kcm__answer"><p>%s</p></div>%s'
            '<p class="kcm__note" style="text-align:left;margin:0">Numbers on the map match the profiles below. Faded pins are unconfirmed or closed.</p></div>'
            '<figure class="kcm__rmap kcm__own-svg"><div class="kcm__scroll" tabindex="0" role="region" aria-label="Map of %s">%s</div></figure></div>'
            '<div class="kcm__sites">%s</div></div></section>\n'
            % (alt, k, k, i, i, len(REGIONS), k, esc(name), esc(INTRO[k]), rfacts(k), esc(name), svg, cards))

# ------------------------------------------------------------------ HERO + nav
HERO = "File:Cliff on the Hells Gate Game Park.jpg"
rtiles = ''
for i, (k, name, short) in enumerate(REGIONS):
    ss = [s for s in BYREG[k] if s['t'] != 'kmc']
    seg = ''.join('<u style="width:%.1f%%;background:%s"></u>' % (sum(1 for s in ss if s['t'] == t) / len(ss) * 100, COL[t]) for t in ['kws-p', 'kws-s', 'mtn', 'mara', 'cons', 'priv'] if any(s['t'] == t for s in ss))
    rtiles += '<a class="kcm__rtile" href="#%s"><b>%s</b><span>%d campsites</span><i aria-hidden="true">%s</i></a>' % (k, esc(short), len(ss), seg)

hero = '''<header class="kcm__hero">
<div class="kcm__hero-bg" style="background-image:url('%(bg)s')" data-placeholder="true" role="img" aria-label="Basalt cliffs above the grassland floor of Hell's Gate National Park"></div>
<div class="kcm__hero-tint"></div>
<div class="kcm__hero-in">
<span class="kcm__pill">Kenya safari accommodation &middot; campsite guide</span>
<h1>Kenya campsites map: <em>every campsite, what it costs and how to get there</em></h1>
<p class="kcm__lead">Kenya has <b>at least %(named)d named campsites</b> on safari routes. They range from <b>Kenya Wildlife Service (KWS) sites in %(nparks)d parks and reserves</b> to <b>Masai Mara, conservancy, mountain and private campsites</b>. We checked every one in October 2026 for its status, position, access and price. Below you'll find %(n)d profiles across 16 regions, with protected-area maps and a KWS fee calculator.</p>
<div class="kcm__stats kcm__stats--hero" role="list">
<div class="kcm__stat" role="listitem"><b>%(n)d</b><span>campsite profiles</span></div>
<div class="kcm__stat" role="listitem"><b>%(open)d</b><span>confirmed operating</span></div>
<div class="kcm__stat" role="listitem"><b>%(moved)d</b><span>map pins corrected</span></div>
<div class="kcm__stat" role="listitem"><b>%(priced)d</b><span>with a nightly cost</span></div>
</div>
<div class="kcm__hero-cta"><a class="kcm__btn kcm__btn--brass" href="#map" data-evt="hero_open_map">Open the campsite map</a><a class="kcm__btn kcm__btn--ghost" href="#costs">Work out KWS camping fees</a></div>
</div>
<div class="kcm__trust"><div class="kcm__trust-in">
<div class="kcm__trust-i"><b>Researched site by site</b><span>Operator, KWS and OSM sources, 11 Oct 2026</span></div>
<div class="kcm__trust-i"><b>Real boundaries</b><span>WDPA and OpenStreetMap protected areas</span></div>
<div class="kcm__trust-i"><b>Fees kept apart</b><span>KWS, Mara and conservancy fees never mixed</span></div>
<div class="kcm__trust-i"><b>Doubts published</b><span>%(tbc)d unconfirmed and %(closed)d closed sites flagged</span></div>
</div></div>
</header>
<nav class="kcm__snav" aria-label="On this page" data-spy><div class="kcm__snav-in">
<a href="#answer">Quick answer</a><a href="#map">Map</a><a href="#types">Who runs them</a><a href="#costs">Costs</a><a href="#regions">Regions</a><a href="#access">Access</a><a href="#seasons">Seasons</a><a href="#safety">Safety</a><a href="#rules">Rules</a><a href="#gear">Gear</a><a href="#book">Booking</a><a href="#faq">FAQ</a>
</div></nav>
''' % dict(bg=img_url(HERO, 1280), named=N_NAMED, nparks=len(KWS_PARKS), n=N, open=N_OPEN, moved=N_MOVED, priced=N_PRICED, tbc=N_TBC, closed=N_CLOSED)

answer = '''<section class="kcm__sec kcm__sec--commerce" id="answer" aria-labelledby="kcm-h-answer"><div class="kcm__in">
<p class="kcm__kicker">The quick answer</p>
<h2 id="kcm-h-answer">Where can you camp in Kenya, and <em>what does it cost</em>?</h2>
<p class="kcm__sub">Inside most national parks, in the Masai Mara, on conservancies and at private sites near the parks. Each kind is booked and priced by a different authority.</p>
<div class="kcm__answer">
<p><b>You can camp at KWS campsites in %(nparks)d Kenyan parks and reserves, in the Masai Mara (mostly the Mara Triangle), on private and community conservancies, at Mount Kenya's trekking camps and at private campsites near the parks.</b> A non-resident adult pays KWS USD 20 to 50 a night to camp, plus park entry of USD 25 to 90 for each 24 hours. Mara Triangle campsites cost USD 40 a night plus the reserve fee, and community conservancy sites in the north about KES 2,000.</p>
<p>KWS public campsites are shared and need no booking. KWS special campsites are exclusive, must be booked ahead with a non-refundable KES 10,000 weekly reservation, and have no facilities. Conservancy, Mara and private sites are booked with whoever runs them.</p>
</div>
<div class="kcm__copy">
<div class="kcm__fieldnote"><p><b>Why we built it this way.</b> Before %(home)s existed, its founders spent about a year travelling Kenya's safari destinations in a campervan, mostly the Masai Mara, Tsavo East and Amboseli. That year taught them how transfer times, park routes and gate hours shape a day on the road. That is why every profile below starts with who runs the site, how you get in and what you pay, and only then describes the site itself. Our own base in the Mara is %(kmc)s, about 9 km before Sekenani Gate on the Narok road.</p></div>
</div>
<p class="kcm__kicker" style="margin-top:34px">Jump to a region</p>
<div class="kcm__rgrid">%(tiles)s</div>
</div></section>
''' % dict(nparks=len(KWS_PARKS), home=ilink('/', 'Kambu Campers'), kmc=ilink('/ke/kambu-mara-camp/', 'Kambu Mara Camp'), tiles=rtiles)

# ------------------------------------------------------------------ interactive map
chips = ''.join('<button type="button" class="kcm__chip" data-type="%s" aria-pressed="true" style="--c:%s"><i aria-hidden="true"></i>%s <span>(%d)</span></button>' % (t, COL[t], TSHORT[t], cnt(t))
                for t in ['kws-p', 'kws-s', 'mtn', 'mara', 'cons', 'priv'])
regopts = ''.join('<option value="%s">%s (%d)</option>' % (k, esc(sh), sum(1 for s in BYREG[k] if s['t'] != 'kmc')) for k, _, sh in REGIONS)
mapsec = '''<section class="kcm__sec kcm__sec--plan" id="map" aria-labelledby="kcm-h-map"><div class="kcm__in" style="max-width:var(--maxw)">
<p class="kcm__kicker">Interactive map</p>
<h2 id="kcm-h-map">Kenya campsites map with <em>park and conservancy boundaries</em></h2>
<p class="kcm__sub">Filter by who runs the site, region and access. Select a pin for the essentials and a link to its full profile.</p>
<div class="kcm__mapwrap">
<p class="kcm__nojs" id="kcm-nojs">The interactive map needs JavaScript. Every campsite is profiled region by region in the <a href="#regions">campsite directory</a>, and each region has its own static map.</p>
<div id="kcm-mapui" hidden>
<div class="kcm__filters" role="group" aria-label="Map filters">
<div class="kcm__frow"><span class="kcm__flabel">Run by</span>%(chips)s</div>
<div class="kcm__frow"><span class="kcm__flabel">Where</span>
<label class="kcm__sr" for="kcm-region">Region</label><select id="kcm-region"><option value="all">All 16 regions (%(n)d)</option>%(regopts)s</select>
<label class="kcm__sr" for="kcm-veh">Vehicle</label><select id="kcm-veh"><option value="all">Any vehicle</option><option value="2wd">Reachable without 4WD</option><option value="4wd">4WD recommended or required</option><option value="other">Boat or on foot</option></select>
<label class="kcm__sr" for="kcm-q">Search campsites</label><input type="search" id="kcm-q" placeholder="Search a campsite, park or county" autocomplete="off"></div>
<div class="kcm__frow"><span class="kcm__flabel">Show</span>
<label class="kcm__check"><input type="checkbox" id="kcm-f-priced"> Only with a published cost</label>
<label class="kcm__check"><input type="checkbox" id="kcm-f-inactive"> Include unconfirmed and closed (%(inact)d)</label>
<label class="kcm__check"><input type="checkbox" id="kcm-f-bounds" checked> Protected-area boundaries</label>
<button type="button" class="kcm__chip" id="kcm-reset" style="--c:#4C554B">Reset</button></div>
<p class="kcm__count" id="kcm-count" aria-live="polite"></p>
</div>
<div class="kcm__mapgrid">
<div class="kcm__map" id="kcm-map" role="region" aria-label="Interactive map of Kenya campsites" data-mbstyle="mapbox/outdoors-v12" data-mbtoken="%(tok)s"></div>
<div class="kcm__side"><div class="kcm__side-h"><b style="color:var(--forest);font-size:.86rem">Campsites in view</b></div><ul class="kcm__results" id="kcm-results" aria-label="Campsites matching the filters"></ul></div>
</div>
<ul class="kcm__legend" aria-label="Map key">%(legend)s<li><span class="kcm__t" style="--c:#3E7B4F">Park or reserve boundary</span></li><li><span class="kcm__t" style="--c:#B67A18">Conservancy boundary</span></li></ul>
</div>
<p class="kcm__note">Boundaries are simplified from UNEP-WCMC WDPA and OpenStreetMap and are not legal boundaries. Many conservancies are not mapped. Base map &copy; Mapbox &copy; OpenStreetMap contributors.</p>
</div>
</div></section>
''' % dict(chips=chips, regopts=regopts, n=N, inact=N_TBC + N_CLOSED, tok=TOK,
           legend=''.join('<li><span class="kcm__t kcm__t--%s">%s</span></li>' % (t, TSHORT[t]) for t in ['kws-p', 'kws-s', 'mtn', 'mara', 'cons', 'priv', 'kmc']))

# ------------------------------------------------------------------ types
types = '''<section class="kcm__sec kcm__sec--commerce" id="types" aria-labelledby="kcm-h-types"><div class="kcm__in">
<p class="kcm__kicker">Booking and facilities</p>
<h2 id="kcm-h-types">Who runs the campsite <em>decides how you book</em></h2>
<p class="kcm__sub">Kenya's campsites fall under five authorities and one private market. Each sets its own rules for booking, exclusivity and fees.</p>
<div class="kcm__split" style="align-items:start">
<figure class="kcm__fig kcm__own-svg"><div class="kcm__scroll" tabindex="0" role="region" aria-label="Map of all campsites and protected areas">%(nsvg)s</div>
<figcaption><b>Note how the operators split the country.</b> KWS sites follow the national parks: the mountains, the Rift lakes and Tsavo. Conservancy sites fill Laikipia and the northern rangelands, where there are few parks. Private camps cluster where people start and end road trips, around Nairobi and Naivasha.</figcaption></figure>
<div>
<div class="kcm__tw kcm__tw--fit" style="margin-top:0"><table>
<caption>Basis: KWS park pages and LN 160 of 2025; Mara Conservancy booking system; Ol Pejeta 2026 tariff; The Big North; Kenya Forest Service fees page. Read 11 Oct 2026.</caption>
<thead><tr><th scope="col">Run by</th><th scope="col">Profiles</th><th scope="col">Booking</th></tr></thead><tbody>
<tr><th scope="row"><span class="kcm__t kcm__t--kws-p">KWS public</span></th><td class="kcm__num">%(kp)d</td><td>No booking; shared; pay KWS fees online on eCitizen (KWSPay)</td></tr>
<tr><th scope="row"><span class="kcm__t kcm__t--kws-s">KWS special</span></th><td class="kcm__num">%(ks)d</td><td>Book ahead with the warden or reservations@kws.go.ke; exclusive; no facilities</td></tr>
<tr><th scope="row"><span class="kcm__t kcm__t--mtn">Mount Kenya hut camps</span></th><td class="kcm__num">%(km)d</td><td>Private hut operators inside the park; usually booked with a guide outfit</td></tr>
<tr><th scope="row"><span class="kcm__t kcm__t--mara">Masai Mara reserve</span></th><td class="kcm__num">%(mm)d</td><td>Mara Triangle: online through the Mara Conservancy; Narok side: direct</td></tr>
<tr><th scope="row"><span class="kcm__t kcm__t--cons">Conservancy or ranch</span></th><td class="kcm__num">%(cc)d</td><td>With the conservancy: Ol Pejeta online, NRT sites through The Big North</td></tr>
<tr><th scope="row"><span class="kcm__t kcm__t--priv">Private</span></th><td class="kcm__num">%(pp)d</td><td>Direct with the owner; prices and facilities vary most</td></tr>
</tbody></table></div>
<div class="kcm__callout"><p><b>Forest reserves are a sixth system.</b> Gazetted forests are run by the Kenya Forest Service, which charges KES 650 per adult per night for camping, whatever your residency. Ngare Ndare Forest is managed with a trust and books through The Big North at its own rate.</p></div>
<div class="kcm__callout"><p><b>Mount Kenya's high camps are not KWS campsites.</b> KWS lists Old Moses, Shipton's, Mackinder's and Met Station as privately run. You pay their hut or camping fee on top of KWS park entry, and you must climb with a licensed guide.</p></div>
</div></div>
</div></section>
''' % dict(nsvg=national_svg(SITES, D['bounds'], KEN), kp=cnt('kws-p'), ks=cnt('kws-s'), km=cnt('mtn'), mm=cnt('mara'), cc=cnt('cons'), pp=cnt('priv'))

# ------------------------------------------------------------------ costs
def fee_rows(tbl):
    return ''.join('<td class="kcm__num">%s %s / %s</td>' % (CUR[i], fmt(tbl[i][0]), fmt(tbl[i][1])) for i in range(4))
PARKS_BY_CAT = {}
for s in CAMPS:
    if s.get('kcat'): PARKS_BY_CAT.setdefault(s['kcat'][1], set()).add(s['kcat'][0])
entry_rows = ''.join('<tr><th scope="row">%s<br><span style="font-weight:400;font-size:.78rem;color:#5F655D">%s</span></th>%s</tr>' % (CATNAME[c], esc(', '.join(sorted(PARKS_BY_CAT.get(c, [])))), fee_rows(ENTRY[c]))
                     for c in ['premium', 'wildA', 'wildB', 'mountain', 'scenic', 'special', 'sanct', 'marine'] if c in PARKS_BY_CAT)
calc_opts = ''
for k, name, short in REGIONS:
    ks = [s for s in BYREG[k] if s['t'] in ('kws-p', 'kws-s', 'mtn') and s.get('kcat') and s['s'] != 'closed']
    if ks: calc_opts += '<optgroup label="%s">%s</optgroup>' % (esc(short), ''.join('<option value="%s">%s</option>' % (s['sid'], esc(s['n'])) for s in ks))
costs = '''<section class="kcm__sec kcm__sec--plan" id="costs" aria-labelledby="kcm-h-costs"><div class="kcm__in">
<p class="kcm__kicker">Camping costs</p>
<h2 id="kcm-h-costs">How much camping costs in Kenya, <em>authority by authority</em></h2>
<p class="kcm__sub">At a KWS campsite you pay two KWS fees: camping per night and park entry per 24 hours. Mara, conservancy and forest campsites set their own fees, shown separately below.</p>
<div class="kcm__answer"><p><b>A night at a KWS public campsite costs a non-resident adult USD 20 camping plus USD 25 to 90 park entry, depending on the park's fee band. Amboseli and Lake Nakuru are dearest at USD 120 for one adult night.</b> Kenyan citizens pay KES 200 to 500 camping plus KES 300 to 1,500 entry. Children pay less, under-fives are free, and vehicles cost KES 600 a day for under six seats.</p></div>
<div class="kcm__tw"><table><caption>KWS camping fees per person per night (adult / child). Wildlife Conservation and Management (Access, Entry and Conservation) (Fees) Regulations 2025, Legal Notice 160, effective 1 October 2025; matches the KWS October 2025 tariff sheet.</caption>
<thead><tr><th scope="col">Campsite and band</th><th scope="col">East African citizen</th><th scope="col">Kenya resident</th><th scope="col">Non-resident</th><th scope="col">African citizen</th></tr></thead><tbody>
<tr><th scope="row">Public, Amboseli and Lake Nakuru</th>%(p1)s</tr><tr><th scope="row">Public, all other parks</th>%(p2)s</tr>
<tr><th scope="row">Special, Amboseli and Lake Nakuru</th>%(s1)s</tr><tr><th scope="row">Special, all other parks</th>%(s2)s</tr>
<tr><th scope="row">Special campsite reservation</th><td colspan="4">KES 10,000 per week, non-refundable</td></tr></tbody></table></div>
<div class="kcm__tw"><table><caption>KWS park entry (conservation fee) per person per 24 hours (adult / child), LN 160 of 2025, for the fee bands of parks on this map. Vehicles: KES 600 (under 6 seats), 1,500 (6 to 12 seats), 3,000 (13 to 24 seats) per day; vehicle recovery inside a park KES 10,500.</caption>
<thead><tr><th scope="col">Fee band and parks</th><th scope="col">East African citizen</th><th scope="col">Kenya resident</th><th scope="col">Non-resident</th><th scope="col">African citizen</th></tr></thead><tbody>%(entry)s</tbody></table></div>
<div class="kcm__calc" id="kcm-calc">
<div><h3>KWS camping cost calculator</h3><p>Pick a KWS campsite and your group. It adds the camping fee, park entry for each 24 hours, the special-site reservation and your vehicle, using LN 160 rates.</p>
<label for="kcm-c-site">Campsite</label><select id="kcm-c-site">%(opts)s</select>
<label for="kcm-c-vis">Visitor category</label><select id="kcm-c-vis"><option value="2">Non-resident (USD)</option><option value="0">East African citizen (KES)</option><option value="1">Kenya resident (KES)</option><option value="3">African citizen (USD)</option></select>
<div class="kcm__crow"><div><label for="kcm-c-ad">Adults</label><input id="kcm-c-ad" type="number" min="1" max="30" value="2"></div><div><label for="kcm-c-ch">Children 5&ndash;17</label><input id="kcm-c-ch" type="number" min="0" max="30" value="0"></div><div><label for="kcm-c-n">Nights</label><input id="kcm-c-n" type="number" min="1" max="21" value="2"></div><div><label for="kcm-c-v">Vehicles (&lt;6 seats)</label><input id="kcm-c-v" type="number" min="0" max="6" value="1"></div></div>
<noscript><p>The calculator needs JavaScript; use the two tables above instead.</p></noscript>
</div>
<div class="kcm__cout" aria-live="polite"><p style="margin:0;color:#B9C6BC;font-size:.8rem" id="kcm-c-label">Estimated KWS fees</p><p class="kcm__ctotal" id="kcm-c-total">&ndash;</p><table><tbody id="kcm-c-rows"></tbody></table>
<p class="kcm__cnote">Assumes one 24-hour park entry per night camped. KWS adds a gateway fee on some payments. Vehicle fees are charged in KES whatever your category. Hut fees on Mount Kenya and guide costs are not included. Confirm on KWSPay when you book.</p></div>
</div>
<div class="kcm__callout"><p><b>The 2025 KWS fees are still in court.</b> On 1 to 2 October 2025 the High Court suspended the new fees on a Kenya Tourism Federation petition. KWS park pages updated in 2026 still show the LN 160 rates, and in March 2026 the Federation took the dispute to Parliament. We found no final judgment as of October 2026. Pay what KWSPay charges and keep your receipt.</p></div>
<h3 style="margin-top:34px">Fees set by other authorities</h3>
<div class="kcm__feegrid">
<div class="kcm__feecard" style="--c:var(--t-mara)"><p class="kcm__who">Mara Conservancy</p><h3>Mara Triangle campsites</h3><p>The Conservancy's booking system lists <b>USD 40 per non-resident adult per night</b> (child USD 20) at both public and private sites, 2026. A 2026 secondary guide gives USD 30 for public sites. We follow the operator. Campers must hire two rangers for the night, and private sites carry a booking fee. Park tickets run 06:00 to 18:00, are cashless and are sold through KAPS.</p></div>
<div class="kcm__feecard" style="--c:var(--t-mara)"><p class="kcm__who">Narok County</p><h3>Masai Mara, east side</h3><p>Several 2026 secondary sources agree on <b>USD 100 per non-resident adult (January to June) and USD 200 (July to December)</b> per 12-hour ticket; children 9 to 17 pay USD 50. Kenyan citizen rates conflict between sources (KES 1,500/3,000 or KES 2,500/5,000). We read no Narok County schedule; see the %(mfees)s.</p></div>
<div class="kcm__feecard" style="--c:var(--t-cons)"><p class="kcm__who">Ol Pejeta Conservancy, 2026 tariff</p><h3>Ol Pejeta camping</h3><p>Camping <b>KES 3,500 per adult and KES 1,750 per child per night</b>, plus an armed ranger at KES 5,000 per night. Conservancy entry is extra: USD 110 per non-resident adult, KES 3,500 per Kenya resident adult, KES 2,000 per citizen adult per 24 hours. Gates (Rongai and Serat) are cashless and open 07:00 to 19:00.</p></div>
<div class="kcm__feecard" style="--c:var(--t-cons)"><p class="kcm__who">The Big North (NRT conservancies)</p><h3>Northern community campsites</h3><p>Most sites charge <b>KES 2,000 per adult and KES 1,000 per child under 12</b> per night. Sera and Nesesia charge non-residents KES 5,000 for commercial camping, and Westgate HQ and Lorian KES 5,000 for private camping. Rangers cost KES 1,000 to 1,500 per day. Book by email with the conservancy or tourism@nrt-kenya.org.</p></div>
<div class="kcm__feecard" style="--c:#3E7B4F"><p class="kcm__who">Kenya Forest Service</p><h3>Forest reserve camping</h3><p><b>KES 650 per adult and KES 100 per child per night</b>, the same for citizens, residents and non-residents, plus daily access of KES 200, 400 or 600 per adult by category. Ngare Ndare is reported at KES 3,000 (resident) and KES 5,000 (non-resident) with a mandatory ranger.</p></div>
<div class="kcm__feecard" style="--c:var(--t-priv)"><p class="kcm__who">Community and private sites</p><h3>Private campsites</h3><p>Published rates on this map range from about <b>KES 500 to KES 2,500 per person per night</b>, such as Diani Backpackers KES 600 (2026), Roberts Camp KES 800 (2024), Aberdare Cottages KES 1,000 and Mount Suswa KES 1,000 (cash only). Many rates come from trip reports, so each profile shows the year we saw it.</p></div>
</div>
</div></section>
''' % dict(p1=fee_rows(CAMPFEE[('p', True)]), p2=fee_rows(CAMPFEE[('p', False)]), s1=fee_rows(CAMPFEE[('s', True)]), s2=fee_rows(CAMPFEE[('s', False)]),
           entry=entry_rows, opts=calc_opts, mfees=ilink('/ke/guides/masai-mara-entry-fees/', 'Masai Mara entry fees guide'))

# ------------------------------------------------------------------ regions
regions_intro = '''<section class="kcm__sec kcm__sec--commerce" id="regions" aria-labelledby="kcm-h-regions"><div class="kcm__in">
<p class="kcm__kicker">Campsite directory</p>
<h2 id="kcm-h-regions">Kenya campsites by region</h2>
<p class="kcm__sub">Sixteen regions, from the Masai Mara to Lake Turkana. Each has a boundary map and a profile for every campsite: where it is, the drive, access, cost and booking.</p>
<div class="kcm__rgrid">%s</div>
</div></section>
''' % rtiles.replace('kcm__rtile"', 'kcm__rtile" data-evt="region_jump"')
regs = ''.join(region_section(i + 1, k, n, sh) for i, (k, n, sh) in enumerate(REGIONS))

# ------------------------------------------------------------------ access & circuits
def leg_rows(c):
    return ''.join('<tr><td>%s</td><td>%s</td><td class="kcm__num">%s km</td><td class="kcm__num">%s</td></tr>' % (esc(a), esc(b), fmt(km) if km else '&ndash;', hm(m) if m else '&ndash;') for a, b, km, m in c['legs'])
circ = ''.join('<details%s><summary>%s <small>%s km in total</small></summary><div class="kcm__ans"><div class="kcm__tw"><table><thead><tr><th scope="col">From</th><th scope="col">To</th><th scope="col">Distance</th><th scope="col">Drive</th></tr></thead><tbody>%s</tbody></table></div></div></details>'
               % (' open' if i == 0 else '', esc(c['t']), fmt(sum(l[2] or 0 for l in c['legs'])), leg_rows(c)) for i, c in enumerate(D['circuits']))
access = '''<section class="kcm__sec kcm__sec--exp" id="access" aria-labelledby="kcm-h-access"><div class="kcm__in">
<p class="kcm__kicker">Getting there</p>
<h2 id="kcm-h-access">Roads, vehicles and <em>camping routes</em></h2>
<p class="kcm__sub">Most Kenyan campsites are a tarmac drive to a gate, then murram or dirt to the pitch. The vehicle you need depends on that last stretch and the season.</p>
<div class="kcm__answer"><p><b>Of the %(n)d campsites profiled, %(v2)d can be reached without four-wheel drive in dry weather, %(v4r)d are best in a 4WD and %(v4q)d need one.</b> %(vb)d are reached by boat or on foot, and the rest have no reliable access report. Mapbox road distances in each profile are routed, not measured, and murram sections usually take longer than shown.</p></div>
<div class="kcm__panels3">
<div class="kcm__pcard"><h3>Tarmac to the gate</h3><p>Naivasha's south shore, Hell's Gate, Nakuru, Nairobi's overland camps, Diani and the Mount Kenya gates are reached on tarmac or short murram links. A saloon or 2WD will do in dry weather.</p></div>
<div class="kcm__pcard"><h3>Murram and dirt inside parks</h3><p>Tsavo, Meru, the Mara Triangle, the Aberdares and the northern conservancies need high clearance, and usually 4WD. KWS bans off-road driving and sets a 40 km/h limit. Recovering a stuck vehicle inside a KWS park costs KES 10,500.</p></div>
<div class="kcm__pcard"><h3>Boat and foot access</h3><p>Central and South Island on Lake Turkana are reached by boat, and Mount Kenya's high camps on foot with a licensed guide. Where the nearest mapped road ends far from a pin, the profile says how far.</p></div>
</div>
<h3 style="margin-top:34px">Six camping circuits, routed from Nairobi</h3>
<p class="kcm__note" style="margin-bottom:14px">Drive times are Mapbox routing estimates between the named campsites, without stops.</p>
%(circ)s
<p class="kcm__note">For a guided version of these routes, see the %(cat)s. Itinerary lengths and prices are on the package pages.</p>
</div></section>
''' % dict(n=N, v2=VEH.get('2WD ok', 0), v4r=VEH.get('4WD recommended', 0), v4q=VEH.get('4WD required', 0), vb=VEH.get('boat', 0) + VEH.get('on foot', 0), circ=circ,
           cat=xlink(CATALOGUE, 'Kambu safari packages', 'catalogue_click'))

# ------------------------------------------------------------------ seasons
months = [('Jan', '', 'Dry'), ('Feb', '', 'Dry'), ('Mar', 'r1', 'Long rains'), ('Apr', 'r1', 'Long rains'), ('May', 'r1', 'Long rains'), ('Jun', 'r3', 'Coast, west'),
          ('Jul', 'r3', 'Coast, west'), ('Aug', 'r3', 'Coast, west'), ('Sep', '', 'Dry'), ('Oct', 'r2', 'Short rains'), ('Nov', 'r2', 'Short rains'), ('Dec', 'r2', 'Short rains')]
seasons = '''<section class="kcm__sec kcm__sec--plan" id="seasons" aria-labelledby="kcm-h-seasons"><div class="kcm__in">
<p class="kcm__kicker">Seasons and weather</p>
<h2 id="kcm-h-seasons">When to camp in Kenya, <em>and when the tracks close</em></h2>
<p class="kcm__sub">Kenya has two main rainy seasons, plus a third on the coast and in the west. Rain decides whether you reach a campsite at all.</p>
<div class="kcm__answer"><p><b>The driest camping months are January to February and June to September (except on the coast and in the west). The long rains fall from March to May and the short rains from October to December (Kenya Meteorological Department).</b> KWS calls April to June the low season and says most park roads may then need 4WD.</p></div>
<div class="kcm__months" role="list" aria-label="Rainfall seasons by month">%(m)s</div>
<p class="kcm__note">Blue: long rains. Teal: short rains. Light blue: third season on the coast, the western highlands and the Lake Victoria basin.</p>
<div class="kcm__panels3">
<div class="kcm__pcard"><h3>Floods have closed campsites</h3><p>The 2023&ndash;24 El Ni&ntilde;o rains flooded 46 of Kenya's 47 counties (IFRC). In May 2024 the Talek River swept through more than a dozen Masai Mara camps, and in March 2026 Mara and Talek floods cut bridges and access again (The Standard). Riverside pitches are the first to go.</p></div>
<div class="kcm__pcard"><h3>Short rains 2026: above average</h3><p>The Kenya Meteorological Service forecast above-average October&ndash;December 2026 rains for much of the country, with a strengthening El Ni&ntilde;o (The Star, 26 August 2026). If you are camping this season, confirm road status with the park or operator the day before.</p></div>
<div class="kcm__pcard"><h3>Altitude means cold</h3><p>Night temperature tracks altitude. At 3,000 m on Mount Kenya frosts are possible. Lake Michaelson camp (about 3,985 m) sees -2 to 1&deg;C at night, and Laikipia runs cooler than Tsavo. The Aberdares, Mount Elgon and Mount Kenya profiles all list their altitude.</p></div>
</div>
</div></section>
''' % dict(m=''.join('<div class="%s" role="listitem">%s<span>%s</span></div>' % (c, mo, l) for mo, c, l in months))

# ------------------------------------------------------------------ safety
safety = '''<section class="kcm__sec kcm__sec--exp" id="safety" aria-labelledby="kcm-h-safety"><div class="kcm__in">
<p class="kcm__kicker">Wildlife and safety</p>
<h2 id="kcm-h-safety">Camping safely among <em>wild animals</em></h2>
<p class="kcm__sub">Most Kenyan campsites are unfenced. The rules that keep campers safe are written by the authorities, and several require armed rangers.</p>
<div class="kcm__answer"><p><b>KWS says visitors enter parks at their own risk. Stay in your vehicle except in designated areas, keep at least 20 m from wildlife, never feed animals and never leave a campfire unattended.</b> In the Mara Triangle, on Ol Pejeta and on the northern conservancies you must hire rangers to camp.</p></div>
<div class="kcm__tw"><table><caption>Ranger requirements and charges where published, read 11 Oct 2026. Sources: Mara Conservancy, Ol Pejeta 2026 tariff, The Big North, KWS tariff sheet; Ngare Ndare from a secondary guide.</caption>
<thead><tr><th scope="col">Where</th><th scope="col">Requirement</th><th scope="col">Charge</th></tr></thead><tbody>
<tr><th scope="row">Mara Triangle</th><td>Two rangers for night-time security; transported to your site, no food or bed needed</td><td>Set by the Conservancy (tables not readable online)</td></tr>
<tr><th scope="row">Ol Pejeta</th><td>Armed guide or ranger for campers</td><td class="kcm__num">KES 5,000 per night</td></tr>
<tr><th scope="row">NRT conservancies</th><td>Rangers at community campsites</td><td class="kcm__num">KES 1,000&ndash;1,500 per day</td></tr>
<tr><th scope="row">Ngare Ndare Forest</th><td>Armed ranger for walks and camping</td><td class="kcm__num">KES 1,000 per day or night</td></tr>
<tr><th scope="row">KWS parks</th><td>Ranger-escorted tours on request (minimum two rangers)</td><td class="kcm__num">KES 2,000 per ranger up to 4 h</td></tr>
</tbody></table></div>
<div class="kcm__callout"><p><b>Hippos at Lake Naivasha.</b> In August 2018 a visitor was killed by a hippo while photographing it on the lakeshore near the Sopa resort. In July 2026 KWS warned that rising water had pushed hippos into lakeshore and residential areas. At the Naivasha camps, stay inside fenced areas after dark and never walk to the water at night. KWS's 24-hour wildlife line is 0800 597 000.</p></div>
</div></section>
'''

# ------------------------------------------------------------------ rules & responsible camping
rules = '''<section class="kcm__sec kcm__sec--plan" id="rules" aria-labelledby="kcm-h-rules"><div class="kcm__in">
<p class="kcm__kicker">Rules and responsible camping</p>
<h2 id="kcm-h-rules">Camping rules in Kenya's parks, <em>and how to leave no trace</em></h2>
<p class="kcm__sub">These rules are KWS's own published guidelines, plus each operator's rules where they differ.</p>
<div class="kcm__copy">
<ul class="kcm__list">
<li><b>Gate hours:</b> KWS gates open at 06:00 and close at 18:00 unless you are staying overnight. Mara Triangle tickets run 06:00 to 18:00 for 12 hours. Ol Pejeta's gates open 07:00 to 19:00.</li>
<li><b>Camp only at listed sites:</b> KWS publishes named public and special campsites for each park. We found no provision for camping elsewhere inside a park, so treat the listed sites as the only options.</li>
<li><b>Driving:</b> no off-road driving, 40 km/h speed limit, no hooting, and stay in the vehicle except at designated places. Night game drives are a paid special activity in selected parks only (KES 3,000 or USD 50 per person).</li>
<li><b>Plastic:</b> all KWS parks are single-use-plastic-free. On Mount Kenya, disposable water bottles are banned and you must declare consumables on entry and waste on exit.</li>
<li><b>Fire and firewood:</b> never leave a campfire unattended. The Mara Conservancy says firewood may not be collected in the Triangle, so bring your own. Mount Suswa sells it at KES 1,000 a night.</li>
<li><b>Drones:</b> you need a Kenya Civil Aviation Authority licence and a KWS drone permit for each park and day (KES 5,000, or USD 300 for non-residents).</li>
<li><b>Mount Kenya:</b> all climbers need a licensed guide. Porter loads are capped at 25 kg, and everyone signs in and out at the gate.</li>
<li><b>Payment:</b> KWS fees are paid on eCitizen (KWSPay) by M-Pesa or card, and the gates take no cash. The Mara Triangle and Ol Pejeta are cashless too. Mount Suswa is cash only.</li>
</ul>
<div class="kcm__callout"><p><b>Leave no trace, the practical version.</b> Carry every piece of rubbish out of special campsites, which have no bins. Use existing fire rings, and keep soap and washing water well away from rivers and lakeshores. Keep to the tracks that are already there: KWS's ban on off-road driving protects the grass around campsites as much as the wildlife.</p></div>
</div>
</div></section>
'''

# ------------------------------------------------------------------ gear & styles
CHECK = ['Water for every night at special sites (no supply)', 'Fuel for the round trip, as there is no fuel inside parks', 'Gas stove or charcoal, plus firewood where collecting is banned',
         'Warm sleeping bag for the Aberdares, Mount Kenya and Mount Elgon', 'Shade and sun protection for the north and Tsavo', 'Recovery kit: tow strap, shovel and a working jack',
         'Rubbish bags to carry everything out', 'Water treatment for streams on the mountains', 'Headtorch and spare batteries', 'Offline maps with the GPS points from this guide',
         'Proof of KWSPay and conservancy payments (no cash at gates)', 'First-aid kit and the KWS 24-hour line, 0800 597 000']
gear = '''<section class="kcm__sec kcm__sec--exp" id="gear" aria-labelledby="kcm-h-gear"><div class="kcm__in">
<p class="kcm__kicker">Camping styles, vehicles and gear</p>
<h2 id="kcm-h-gear">Ground tent, rooftop tent or guided: <em>what each style needs</em></h2>
<p class="kcm__sub">How you camp decides which campsites suit you, what you pay at the gate and what you carry.</p>
<div class="kcm__tw"><table><caption>KWS vehicle charges per day from LN 160 of 2025. Conservancies charge separately (Ol Pejeta: KES 1,000 for up to 6 seats).</caption>
<thead><tr><th scope="col">Style</th><th scope="col">Works best at</th><th scope="col">Watch out for</th><th scope="col">KWS vehicle fee</th></tr></thead><tbody>
<tr><th scope="row">Ground tent from a 2WD car</th><td>Private camps near towns, Hell's Gate, Naivasha, Nairobi, Diani</td><td>Murram in the rains; most park campsites need clearance</td><td class="kcm__num">KES 600 (under 6 seats)</td></tr>
<tr><th scope="row">Rooftop tent on a 4x4</th><td>KWS public and special sites, Mara Triangle, conservancies</td><td>Special sites have no water or toilets</td><td class="kcm__num">KES 600</td></tr>
<tr><th scope="row">Campervan</th><td>Private camps with power and showers; KWS public sites on good roads</td><td>Low clearance on park tracks; check each profile's access line</td><td class="kcm__num">KES 600 to 1,500</td></tr>
<tr><th scope="row">Overland truck</th><td>Nairobi overland camps, Naivasha, larger public sites</td><td>Group-size limits (Mara Triangle sites hold 10 to 40 people)</td><td class="kcm__num">KES 3,000 (13&ndash;24 seats)</td></tr>
<tr><th scope="row">Trekking camps</th><td>Mount Kenya routes, with a licensed guide and porters</td><td>Altitude and cold; hut fees on top of park entry</td><td class="kcm__num">None on foot</td></tr>
<tr><th scope="row">Guided camping safari</th><td>Any of the above, with tents, cook and vehicle provided</td><td>Check which campsite each night uses</td><td class="kcm__num">Included by the operator</td></tr>
</tbody></table></div>
<h3 style="margin-top:30px">Camping checklist</h3>
<p class="kcm__note" style="margin-bottom:12px">Tick as you pack. Nothing is saved.</p>
<ul class="kcm__checklist">%(check)s</ul>
</div></section>
''' % dict(check=''.join('<li><label><input type="checkbox"> %s</label></li>' % esc(c) for c in CHECK))

# ------------------------------------------------------------------ best-for picks (computed)
def pick_list(ss, n=6):
    return ', '.join('<a href="#%s">%s</a>' % (s['sid'], esc(s['n'])) for s in ss[:n])
OPEN = [s for s in CAMPS if s['s'] == 'open']
near = sorted([s for s in OPEN if s.get('drv') and s['drv'][1] and s['drv'][1] <= 150], key=lambda s: s['drv'][1])
high = sorted([s for s in OPEN if (s.get('alt') or s.get('elev') or 0) > 0], key=lambda s: -(s.get('alt') or s.get('elev')))
showers = [s for s in OPEN if any('shower' in x.lower() or 'bathroom' in x.lower() for x in (s.get('fac') or [])) or 'shower' in (s.get('f') or [])]
twowd = [s for s in OPEN if s.get('veh') == '2WD ok' and s['t'] in ('kws-p', 'kws-s')]
excl = [s for s in OPEN if s['t'] == 'kws-s' or 'Ol Pejeta' in (s.get('a') or '') or ('Private' in s['n'] and s['t'] == 'mara')]
island = [s for s in CAMPS if s.get('veh') == 'boat']
def kes_amount(s):
    p = s.get('price') or {}
    m = re.search(r'KES\s*([\d,]+)', p.get('amount', ''))
    return int(m.group(1).replace(',', '')) if m and 'per' in p.get('basis', '') else None
cheap = sorted([s for s in OPEN if s['t'] in ('priv', 'cons') and kes_amount(s)], key=kes_amount)
picks = '''<section class="kcm__sec kcm__sec--commerce" id="choose" aria-labelledby="kcm-h-choose"><div class="kcm__in">
<p class="kcm__kicker">Choose by what matters</p>
<h2 id="kcm-h-choose">Best campsites in Kenya <em>for what you want</em></h2>
<p class="kcm__sub">These shortlists come straight from the profiles: drive times, listed facilities, altitude and published prices, operating sites only. They are a filter, not a ranking.</p>
<div class="kcm__feegrid">
<div class="kcm__feecard" style="--c:var(--k-teal)"><p class="kcm__who">Within 2.5 hours of Nairobi</p><h3>Weekend camping</h3><p>%(near)s</p></div>
<div class="kcm__feecard" style="--c:var(--t-mtn)"><p class="kcm__who">Highest campsites</p><h3>Cold, clear nights</h3><p>%(high)s</p></div>
<div class="kcm__feecard" style="--c:var(--k-blue)"><p class="kcm__who">Showers or a bathroom listed</p><h3>Comfort camping</h3><p>%(showers)s</p></div>
<div class="kcm__feecard" style="--c:var(--t-kwsp)"><p class="kcm__who">KWS sites reachable without 4WD</p><h3>Saloon-car friendly parks</h3><p>%(twowd)s</p></div>
<div class="kcm__feecard" style="--c:var(--t-kwss)"><p class="kcm__who">Exclusive use</p><h3>A campsite to yourselves</h3><p>%(nexcl)d profiles are exclusive-use, including %(excl)s.</p></div>
<div class="kcm__feecard" style="--c:var(--t-priv)"><p class="kcm__who">Lowest published per-person rates</p><h3>Cheapest campsites</h3><p>%(cheap)s. Check each profile for the year the rate was seen.</p></div>
</div>
<div class="kcm__suit" style="margin-top:26px">
<div class="kcm__suit--yes"><h3>Camping suits you if</h3><ul><li>You travel self-sufficient in a 4x4, rooftop-tent vehicle or campervan, or with a camping crew</li><li>You want to wake inside a park rather than drive in from outside the gate</li><li>You are happy with shared ablutions, or none at special sites</li></ul></div>
<div class="kcm__suit--no"><h3>Choose a lodge or tented camp if</h3><ul><li>You need hot showers and cooked meals every night. Compare options in the %(acc)s</li><li>You want one fixed base in the Mara without arranging night rangers. %(kmc)s is ~9 km before Sekenani Gate</li><li>You need step-free access. Few campsites publish accessibility, so ask each operator</li></ul></div>
</div>
</div></section>
''' % dict(near=pick_list(near, 8), high=pick_list(high, 6), showers=pick_list(showers, 8), twowd=pick_list(twowd, 8), nexcl=len(excl), excl=pick_list(excl, 5), cheap=pick_list(cheap, 6),
           acc=ilink('/ke/guides/kenya-safari-accommodation/', 'Kenya safari accommodation guide'), kmc=ilink('/ke/kambu-mara-camp/', 'Kambu Mara Camp'))

# ------------------------------------------------------------------ booking
book = '''<section class="kcm__sec kcm__sec--plan" id="book" aria-labelledby="kcm-h-book"><div class="kcm__in">
<p class="kcm__kicker">How to book</p>
<h2 id="kcm-h-book">How to book a campsite in Kenya, <em>step by step</em></h2>
<p class="kcm__sub">Booking runs through a different system for each operator. Match the colour of the pin to the steps below.</p>
<ol class="kcm__steps">
<li><b>KWS public campsites:</b> no booking. Pay park entry, camping and vehicle fees in advance on eCitizen (KWSPay) by M-Pesa or card, and arrive before 18:00.</li>
<li><b>KWS special campsites:</b> email reservations@kws.go.ke or the park warden with your dates, then pay the KES 10,000 weekly reservation (non-refundable) plus nightly fees. KWS gives exact positions for some sites only on booking.</li>
<li><b>Mara Triangle:</b> reserve through the Mara Conservancy's booking system, where unpaid holds are released after 48 hours. Buy park tickets through KAPS and arrange two night rangers.</li>
<li><b>Ol Pejeta:</b> book through the conservancy's online booking system. Gates are cashless.</li>
<li><b>NRT conservancies:</b> email the conservancy (for example westgate@nrt-kenya.org) or tourism@nrt-kenya.org via The Big North.</li>
<li><b>Mount Kenya hut camps:</b> book through a licensed guide or trekking operator, who handles hut fees and porters.</li>
<li><b>Private campsites:</b> book direct, and ask whether the rate is per person, per tent or per vehicle. Rates here are dated because they change.</li>
</ol>
<div class="kcm__callout"><p><b>Before you pay anywhere,</b> confirm three things in writing: that the site is open, its exact location, and what water is there. Our profiles flag %(tbc)d campsites we could not confirm as operating in October 2026.</p></div>
</div></section>
''' % dict(tbc=N_TBC)

# ------------------------------------------------------------------ audit
moved = [s for s in CAMPS if s.get('coord') == 'moved']
checked = '''<section class="kcm__sec kcm__sec--exp" id="checked" aria-labelledby="kcm-h-checked"><div class="kcm__in">
<p class="kcm__kicker">What we checked</p>
<h2 id="kcm-h-checked">How this map was verified, <em>and what it still can't tell you</em></h2>
<p class="kcm__sub">Every pin started on a community campsite map. We checked each one against KWS's 2026 park pages, operator sites, OpenStreetMap and recent trip reports.</p>
<div class="kcm__cards">
<div class="kcm__card" style="--dot:var(--k-teal)"><b class="kcm__big">%(open)d</b><h3>Confirmed operating</h3><p>Listed by KWS or the operator, or reported in 2023&ndash;2026.</p></div>
<div class="kcm__card" style="--dot:var(--k-gold-safe)"><b class="kcm__big">%(tbc)d</b><h3>Unconfirmed</h3><p>No current listing found. Faded on the maps; call before you go.</p></div>
<div class="kcm__card" style="--dot:var(--k-coral)"><b class="kcm__big">%(closed)d</b><h3>Closed</h3><p>Elerai, Olchani and the Mombasa Marine site, which KWS says has no camping.</p></div>
<div class="kcm__card" style="--dot:var(--k-blue)"><b class="kcm__big">%(moved)d</b><h3>Pins moved</h3><p>Corrected to OpenStreetMap or operator positions, by up to 19 km.</p></div>
</div>
<div class="kcm__copy" style="margin-top:26px">
<h3>Corrections that change a trip</h3>
<ul class="kcm__list">
<li><b>Ten northern conservancy pins</b> shared coordinates or sat on headquarters. They are now on OpenStreetMap campsite points 5 to 19 km away (Westgate HQ, Lorian, Kisima Hamsini, Tumot, Lbaa, Lgweita, Loisaba Acacia, Mugie, Sabache, Kitich).</li>
<li><b>Chlobus</b> is KWS's Kisite campsite at Shimoni headquarters, about 5 km from the old pin. Komboyo in Tsavo West moved 2 km, and Mango Tree 4 km.</li>
<li><b>Category changes on KWS's 2026 pages:</b> Bongo (Aberdare), South Island (Turkana) and Ruma's Nyati are special campsites, not public. Satellite in the Chyulu Hills is a KWS public site. Shipton's, Mackinder's, Met Station and Old Moses are privately run hut camps.</li>
<li><b>No longer on KWS lists:</b> Honi, Shamata public and Bill Woodley (Aberdare), Rock Hyrax (Ol Donyo Sabuk), Kenge and Professional (Tsavo West), Kanderi (Tsavo East), three Shimba Hills sites and Mpunguti. We show them as unconfirmed rather than deleting them.</li>
<li><b>Removed:</b> Kisiwa, whose pin sits in a residential part of Kiambu with no campsite of that name. <b>Not yet pinned:</b> Ruma's Fig Tree public campsite and nine NRT sites listed by The Big North without coordinates.</li>
</ul>
<p><b>Test it yourself.</b> Each profile lists its sources, each with an evidence grade. If something here is out of date, %(wa)s and we will correct it.</p>
</div>
</div></section>
''' % dict(open=N_OPEN, tbc=N_TBC, closed=N_CLOSED, moved=N_MOVED, wa=xlink(WA, 'tell us on WhatsApp', 'feedback_whatsapp'))

# ------------------------------------------------------------------ gallery (placeholders, not watermarked)
GAL = [("File:Mt kenya shiptons camp with sendeyo.jpg", "Shipton's Camp, Sirimon route", "Shipton's Camp on Mount Kenya's Sirimon route, at about 4,200 m, with Terere and Sendeyo behind.", "Stone huts and a campsite among giant groundsels below the jagged peaks of Terere and Sendeyo on Mount Kenya"),
       ("File:Approaching Mackinders Camp.jpg", "Mackinder's Camp, Teleki Valley", "The approach to Mackinder's Camp on the Naro Moru route.", "A signpost for Mackinder's Camp on a stony path in the Teleki Valley, with Mount Kenya's snow-streaked peaks ahead"),
       ("File:Trail signs at Hell's Gate National Park, Kenya.jpg", "Hell's Gate trail signs", "Signs on the Hell's Gate floor point to the gates and to a campsite.", "Wooden trail signs on a stone plinth in Hell's Gate National Park pointing to gates and a campsite"),
       ("File:Hell's Gate Gorge (2294202692).jpg", "Hell's Gate gorge", "The Ol Njorowa gorge, a short drive from the park's three campsites.", "Sunlight falling between the steep rock walls of the gorge in Hell's Gate National Park"),
       ("File:Lake bogoria view.jpg", "Lake Bogoria", "Lake Bogoria from the escarpment above the Maji Moto camps.", "View over acacia bush to Lake Bogoria below a long escarpment under scattered cloud"),
       ("File:Rainbow over Samburu National Reserve landscape, Kenya.jpg", "Samburu storm", "An afternoon storm over Samburu. Northern tracks turn slippery fast.", "A rainbow over acacia scrub and a red dirt track as a storm approaches in Samburu National Reserve")]
slides = ''.join('<figure class="kcm__slide" data-own="false"><img src="%s" alt="%s" loading="lazy" width="960" height="640" data-placeholder="true"><figcaption><b>%s</b>%s <span class="kcm__cred">Photo: %s.</span></figcaption></figure>' % (img_url(t), esc(a), esc(h), esc(c), credit(t)) for t, h, c, a in GAL)
gallery = '''<section class="kcm__sec kcm__sec--plan" id="gallery" aria-labelledby="kcm-h-gal"><div class="kcm__in">
<p class="kcm__kicker">On the ground</p>
<h2 id="kcm-h-gal">What Kenya's campsite country <em>looks like</em></h2>
<p class="kcm__sub">Mountain camps, gorge country, Rift Valley lakes and northern bush.</p>
<div class="kcm__gal" data-gal>
<div class="kcm__gal-head"><p>Placeholder photographs credited to their authors; Kambu photography and watermark replace them.</p>
<div class="kcm__gal-nav" hidden><button type="button" class="kcm__arrow" data-dir="-1" aria-label="Previous photo">&lsaquo;</button><span class="kcm__gal-count" aria-live="polite">1 / %d</span><button type="button" class="kcm__arrow" data-dir="1" aria-label="Next photo">&rsaquo;</button></div></div>
<div class="kcm__track" tabindex="0" role="region" aria-label="Photo gallery, use arrow keys to move">%s</div></div>
</div></section>
''' % (len(GAL), slides)

# ------------------------------------------------------------------ FAQ
FAQ = [
 ("Can you camp in Kenya's national parks?", "Yes. KWS runs public and special campsites in %d parks and reserves on this map, including Hell's Gate, Lake Nakuru, Tsavo West, Meru, Mount Kenya and Mount Elgon. Public sites are shared and need no booking; special sites are exclusive and booked ahead." % len(KWS_PARKS)),
 ("How much does camping cost in Kenya?", "At KWS sites a non-resident adult pays USD 20 to 50 a night camping plus USD 25 to 90 park entry per 24 hours; Kenyan citizens pay KES 200 to 500 plus KES 300 to 1,500. Mara Triangle sites charge USD 40, northern conservancy sites about KES 2,000, and private campsites about KES 500 to 2,500 per person."),
 ("What is the difference between a public and a special campsite?", "A KWS public campsite is shared, needs no booking and usually has basic water and toilets. A special campsite is exclusive to your group, must be booked with the warden or KWS headquarters, carries a KES 10,000 weekly reservation fee and has no facilities."),
 ("Do you pay park entry fees separately from camping fees?", "Yes. At KWS sites you pay a camping fee per night and a park entry fee for each 24 hours, plus a vehicle fee. Conservancies and the Masai Mara also charge entry on top of their camping fees."),
 ("Can you camp inside the Masai Mara?", "Yes. Eleven campsites in the Mara Triangle are booked through the Mara Conservancy at USD 40 per non-resident adult per night, and campers must hire two night rangers. On the Narok County side, Olakira is listed and Tor's now runs mainly as a tented camp."),
 ("Is wild camping legal in Kenya?", "Inside parks and reserves, camp only at the named campsites the authority publishes. We found no provision for camping elsewhere inside a KWS park. Outside protected areas, camp on private or community land only with the landowner's permission."),
 ("Can you camp without a guide?", "At most KWS, conservancy and private campsites, yes. Mount Kenya is the exception: KWS requires every climber to go with a licensed guide. In the Mara Triangle and on several conservancies you must also hire rangers."),
 ("Can a 2WD car reach Kenyan campsites?", "Some can. %d of the %d campsites profiled are reachable without four-wheel drive in dry weather, mostly private camps near towns and sites like Hell's Gate. Most park and conservancy campsites need high clearance or 4WD, especially in the rains." % (VEH.get('2WD ok', 0), N)),
 ("Are campsites open during the rainy season?", "Most stay open, but access can fail. KWS says most park roads may need 4WD in the April to June long rains, and floods cut Mara camps in May 2024 and March 2026. Riverside and lakeshore pitches are the first to flood."),
 ("Are Kenya campsites safe from wild animals?", "Most campsites are unfenced, so animals pass through. Follow KWS's rules: stay in your vehicle except in designated areas, keep 20 m from wildlife, don't feed animals and stay in camp after dark. Where rangers are required, as in the Mara Triangle and on Ol Pejeta, hire them."),
 ("How do I pay KWS camping fees?", "Online through KWSPay on eCitizen, by M-Pesa or card, before you reach the gate. KWS gates take no cash. Keep your receipt, because the 2025 fee schedule is still being challenged in court."),
 ("Are the GPS points on this map exact?", "Most are within a few hundred metres, and %d were corrected this month. Some KWS special sites are given out only on booking, and a few positions remain unconfirmed; each profile says which." % N_MOVED),
]
faq = '''<section class="kcm__sec kcm__sec--commerce" id="faq" aria-labelledby="kcm-h-faq"><div class="kcm__in">
<p class="kcm__kicker">Questions</p>
<h2 id="kcm-h-faq">Camping in Kenya: <em>common questions</em></h2>
<p class="kcm__sub">Short answers; the sections above have the detail.</p>
%s
</div></section>
''' % ''.join('<details id="kcm-faq-%d"%s><summary>%s</summary><div class="kcm__ans"><p>%s</p></div></details>' % (i + 1, ' open' if i == 0 else '', esc(q), esc(a)) for i, (q, a) in enumerate(FAQ))

related = '''<section class="kcm__sec kcm__sec--plan" id="related" aria-labelledby="kcm-h-rel"><div class="kcm__in">
<p class="kcm__kicker">Keep planning</p><h2 id="kcm-h-rel">Related guides</h2>
<div class="kcm__cards">
<a class="kcm__relcard" href="/ke/guides/kenya-safari-accommodation/"%(p)s style="--dot:var(--brass)"><s>Parent guide</s><strong>Kenya safari accommodation</strong><span>Lodges, tented camps and campsites compared</span></a>
<a class="kcm__relcard" href="/ke/guides/kws-park-entry-fees/"%(p)s style="--dot:var(--k-teal)"><s>Fees</s><strong>KWS park entry fees</strong><span>Every park and visitor category</span></a>
<a class="kcm__relcard" href="/ke/guides/lake-naivasha-guide/"%(p)s style="--dot:var(--k-magenta)"><s>Destination</s><strong>Lake Naivasha guide</strong><span>The lake, Hell's Gate and Crescent Island</span></a>
<a class="kcm__relcard" href="/ke/kambu-mara-camp/"%(p)s style="--dot:var(--k-gold-safe)"><s>Our camp</s><strong>Kambu Mara Camp</strong><span>Our base ~9 km before Sekenani Gate</span></a>
</div></div></section>
''' % dict(p=PEND)

SRC = [('A', 'Legal Notice 160 of 2025, Wildlife Conservation and Management (Access, Entry and Conservation) (Fees) Regulations', 'https://www.sarovahotels.com/lionhill-nakuru/assets/images/The-Wildlife-Conservation-and-Management-Regulations-2025.pdf'),
       ('B', 'Kenya Wildlife Service park pages (campsites, safety guidelines, rates), 2026', 'https://kws.go.ke/park/hells-gate-national-park/'),
       ('B', 'KWS camping and picnicking (public and special campsite definitions)', 'https://kws.go.ke/node/10'),
       ('B', 'KWS FAQs (seasons and road conditions)', 'https://kws.go.ke/faqs/'),
       ('B', 'Kenya Forest Service, fees and charges', 'https://www.kenyaforestservice.org/fees-charges'),
       ('B', 'Kenya Meteorological Department, State of the Climate 2023', 'https://meteo.go.ke/documents/802/SoC_Kenya_2023_1.pdf'),
       ('C', 'Mara Conservancy conservation fees and rules', 'https://www.maratriangle.org/conservation-fees-1'),
       ('C', 'Mara Bookings, Mara Triangle campsite system', 'https://marabookings.co.ke/'),
       ('C', 'Ol Pejeta Conservancy tariff guide 2026', 'https://www.olpejetaconservancy.org/wp-content/uploads/2025/11/OPC-Tariff-Guide-2026.pdf'),
       ('C', 'The Big North, NRT conservancy campsites', 'https://thebignorth.travel/campsites/'),
       ('D', 'UNEP-WCMC World Database on Protected Areas (boundaries)', 'https://www.protectedplanet.net/country/KEN'),
       ('D', 'OpenStreetMap (conservancy boundaries, campsite positions)', 'https://www.openstreetmap.org/copyright'),
       ('D', 'Business Daily: court halts higher park fees, 2 Oct 2025', 'https://www.businessdailyafrica.com/bd/economy/kws-revenue-blow-as-court-halts-higher-park-entry-fees-5214790'),
       ('D', 'Business Daily: tourism players take KWS fees to Parliament, 24 Mar 2026', 'https://www.businessdailyafrica.com/bd/economy/tourism-players-take-battle-against-kws-payment-to-parliament-5401966'),
       ('D', 'IFRC final report, Kenya El Nino floods 2023-24', 'https://reliefweb.int/report/kenya/kenya-africa-el-nino-floods-2023-24-final-report-mdrke058'),
       ('D', 'The Standard: helicopter rescue as Mara floods disrupt camps, 7 Mar 2026', 'https://www.standardmedia.co.ke/business/national/article/2001542539/helicopter-rescue-as-flooded-rivers-damage-bridges-and-disrupt-camps-in-maasai-mara'),
       ('D', 'The Star: above-average October-December 2026 rains', 'https://www.the-star.co.ke/news/2026-08-26-kenya-set-for-above-average-october-december-rains'),
       ('D', 'Mara Triangle 2026 camping fees (secondary)', 'https://www.beyondforest.org/post/maasai-mara-entrance-fees-2026-2027-full-cost-breakdown-for-residents-kenyans-foreign-tourists'),
       ('K', 'Kambu Campers: 200+ Campsites in Kenya (2024 list) and the Kenya - Campsites en Route map layer', 'https://thatch.co/guide/13w8fv9xkrb6a/view')]
sources = '''<section class="kcm__sec kcm__sec--exp" id="sources" aria-labelledby="kcm-h-src"><div class="kcm__in">
<p class="kcm__kicker">Sources</p><h2 id="kcm-h-src">Where these facts come from</h2>
<p class="kcm__sub">Grades: A official instrument, B government or authority, C the operator itself, D expert secondary, K Kambu's own records. Every campsite profile also lists its own sources. Read 11 October 2026.</p>
<ul class="kcm__src">%s</ul>
<p class="kcm__reviewed">Last reviewed 11 October 2026 by Kambu Campers. Road distances and drive times are routed by Mapbox; altitudes not given by a source come from the Mapbox terrain model.</p>
</div></section>
''' % ''.join('<li><span>%s</span>%s</li>' % (g, xlink(u, esc(t))) for g, t, u in SRC)

final = '''<section class="kcm__final" aria-labelledby="kcm-h-final">
<div class="kcm__final-bg" style="background-image:url('%(bg)s')" data-placeholder="true" aria-hidden="true"></div><div class="kcm__final-tint"></div>
<div class="kcm__final-in"><p class="kcm__kicker">Plan it with us</p>
<h2 id="kcm-h-final">Want a route built around <em>the right campsites</em>?</h2>
<p>Tell us which parks you want, how you are travelling and how many nights you have. We'll sequence the campsites, gates and drive times, and tell you plainly where a lodge or our own camp near Sekenani Gate would work better.</p>
<div class="kcm__final-btns"><a class="kcm__btn kcm__btn--brass" href="%(wa)s" target="_blank" rel="noopener" data-evt="enquiry_start">Message us on WhatsApp</a><a class="kcm__btn kcm__btn--ghost" href="%(cat)s" target="_blank" rel="noopener" data-evt="catalogue_click">Browse safari packages</a></div>
<p class="kcm__final-contact">Or email <a href="mailto:bookings@kambucampers.com">bookings@kambucampers.com</a>. Park, reserve and conservancy fees are always quoted separately from our service.</p>
</div></section>
''' % dict(bg=img_url("File:Lake bogoria view.jpg", 1280), wa=WA, cat=CATALOGUE)

# ------------------------------------------------------------------ data for JS
mapdata = dict(
    types={t: dict(l=TYPES[t], c=COL[t]) for t in TYPES}, regions={k: sh for k, _, sh in REGIONS},
    sites=[dict(i=s['sid'], n=s['n'], la=s['la'], lo=s['lo'], t=s['t'], a=s.get('a') or '', g=s['g'], s=s['s'], v=s.get('veh', 'unknown'),
                c=s.get('county', ''), p=1 if (s.get('price') or s['t'] in ('kws-p', 'kws-s', 'mtn')) else 0) for s in SITES],
    bounds=[dict(n=b['n'], d=b['d'], r=b['r']) for b in D['bounds']],
    ov={s['sid']: dict(n=s['n'], t=TYPES[s['t']], r=RSHORT[s['g']], co=(s.get('county') or '').replace(' County', ''),
                       st={'tbc': 'Status unconfirmed: call before you go', 'closed': 'Closed'}.get(s['s'], ''), c=short_cost(s),
                       d=('%s km, about %s from Nairobi' % (fmt(s['drv'][0]), hm(s['drv'][1]))) if s.get('drv') and s['drv'][0] else '',
                       v=VEHL.get(s.get('veh', 'unknown'), '') if s.get('veh') not in (None, 'unknown') else '', rv=review_line(s)) for s in SITES},
    fees=dict(entry=ENTRY, camp={'p1': CAMPFEE[('p', True)], 'p0': CAMPFEE[('p', False)], 's1': CAMPFEE[('s', True)], 's0': CAMPFEE[('s', False)]}),
    kws={s['sid']: [s['kcat'][1], {'kws-p': 'p', 'kws-s': 's', 'mtn': 'm'}[s['t']], s['n'], s['kcat'][0]] for s in SITES if s['t'] in ('kws-p', 'kws-s', 'mtn') and s.get('kcat')})
data_js = '<script type="application/json" id="kcm-data">%s</script>' % json.dumps(mapdata, ensure_ascii=True, separators=(',', ':')).replace('</', '<\\/')

ORG = {'@type': ['Organization', 'TravelAgency'], '@id': 'https://kambucampers.com/#org', 'name': 'Kambu Campers', 'url': 'https://kambucampers.com/',
       'logo': 'https://kambucampers.com/wp-content/uploads/2023/10/Kambu-Campers-Logo.png', 'email': 'bookings@kambucampers.com'}
items = []
for i, s in enumerate(sorted([s for s in CAMPS if s['s'] == 'open'], key=lambda s: s['n'])):
    it = {'@type': 'Campground', 'name': s['n'], 'url': URL + '#' + s['sid'], 'geo': {'@type': 'GeoCoordinates', 'latitude': s['la'], 'longitude': s['lo']},
          }
    if s.get('a'): it['containedInPlace'] = {'@type': 'Place', 'name': s['a']}
    items.append({'@type': 'ListItem', 'position': i + 1, 'item': it})
graph = {'@context': 'https://schema.org', '@graph': [ORG,
    {'@type': 'Article', '@id': URL + '#article', 'headline': 'Kenya campsites map: every campsite, what it costs and how to get there',
     'description': 'Interactive map and profiles of %d Kenya campsites in 16 regions: KWS public and special sites, Masai Mara, conservancy, mountain and private campsites, with protected-area boundaries, access, KWS fees and booking.' % N,
     'url': URL, 'mainEntityOfPage': URL, 'inLanguage': 'en-GB', 'dateModified': '2026-10-11', 'datePublished': '2026-10-11',
     'author': {'@id': 'https://kambucampers.com/#org'}, 'publisher': {'@id': 'https://kambucampers.com/#org'}, 'image': img_url(HERO, 1280),
     'about': {'@type': 'Place', 'name': 'Kenya'}, 'hasPart': [{'@type': 'WebPageElement', 'name': n, 'url': URL + '#' + k} for k, n, _ in REGIONS]},
    {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://kambucampers.com/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Kenya safari accommodation', 'item': 'https://kambucampers.com/ke/guides/kenya-safari-accommodation/'},
        {'@type': 'ListItem', 'position': 3, 'name': 'Kenya campsites map', 'item': URL}]},
    {'@type': 'ItemList', '@id': URL + '#campsites', 'name': 'Campsites in Kenya confirmed operating, October 2026', 'numberOfItems': len(items), 'itemListElement': items},
    {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}]}
ld = '<script type="application/ld+json">%s</script>' % json.dumps(graph, ensure_ascii=True, separators=(',', ':'))

head = '''<!-- wp:html -->
<!--
KAMBU CAMPERS | Kenya campsites map v2 (supporting guide to Kenya safari accommodation)
URL (proposed): https://kambucampers.com/ke/guides/kenya-campsites-map/   Namespace .kcm (Executive Elegant)
H2 anchors: one per region, e.g. #masai-mara-campsites, #mount-kenya-campsites, #tsavo-campsites (16 in total)
SEO title: Kenya Campsites Map: %(n)d Campsites, Costs & Access | Kambu Campers
Meta: Every Kenya campsite on one map: %(n)d profiles in 16 regions with park boundaries, KWS camping fees, drive times, access and booking. Checked October 2026.
Data: campsite register (Google My Maps layer) audited 11 Oct 2026; per-site research (KWS 2026 park pages, operators, OSM); boundaries UNEP-WCMC WDPA + OSM;
      elevation Mapbox terrain-rgb; drive routes Mapbox Directions from Nairobi CBD (-1.28638, 36.81720). KWS fees: LN 160 of 2025.
Mapbox: the pk token in data-mbtoken is public by design; restrict it to kambucampers.com and staging9 in the Mapbox account.
Watermark: Kambu logo + @kambucampers.com on Kambu-made maps only; placeholder photos carry data-own="false" (add class kcm__own when swapped for Kambu photos).
Keyword data: none (Ahrefs plan lacks Keywords Explorer; SE Ranking key not supplied this session).
Last reviewed: 11 October 2026
-->
''' % dict(n=N)
fonts = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="">
'''
scripts = ('<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin="" data-cfasync="false" data-no-optimize="1" data-no-defer="1"></script>\n'
           '<script data-cfasync="false" data-no-optimize="1" data-no-defer="1">%s</script>' % JS)
body = hero + answer + mapsec + types + costs + regions_intro + regs + access + seasons + safety + rules + gear + picks + book + checked + gallery + faq + related + sources + final
body = body.encode('ascii', 'xmlcharrefreplace').decode()
block = (head + fonts + '<style>%s</style>\n' % CSS.encode('ascii', 'xmlcharrefreplace').decode() + '<div class="kcm">\n' + body + data_js + '\n' + ld + '\n' + scripts + '\n</div>\n<!-- /wp:html -->\n')
block = re.sub(r'\n\s*\n', '\n', block)
out = os.path.join(HERE, 'out'); os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'kenya-campsites-map-block.html'), 'w').write(block)
open(os.path.join(out, 'kenya-campsites-map-preview.html'), 'w').write('<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kenya Campsites Map | Kambu Campers (preview)</title><style>body{margin:0;background:#F1E9DB}</style></head><body>\n' + block + '</body></html>')
print('bytes', len(block), 'profiles', N, 'open', N_OPEN, 'tbc', N_TBC, 'closed', N_CLOSED, 'moved', N_MOVED, 'priced', N_PRICED, 'veh', VEH)
