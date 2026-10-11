"""SVG maps with protected-area boundaries, Kambu logo watermark and @kambucampers.com (Kambu-made graphics)."""
import math, html
LOGO = 'https://kambucampers.com/wp-content/uploads/2023/10/Kambu-Campers-Logo.png'
COL = {'kws-p': '#159C97', 'kws-s': '#2B47A8', 'mara': '#D2532D', 'cons': '#B67A18', 'priv': '#C0448E', 'kmc': '#233A31', 'mtn': '#6A4C93'}
def pa_style(d):
    d = d.lower()
    if 'marine' in d: return '#D6E8F2', '#2B6FA8'
    if 'conservancy' in d or 'sanctuary' in d and 'national' not in d or 'sector' in d: return '#F6E7C8', '#B67A18'
    return '#DCEBD3', '#3E7B4F'

class Proj:
    def __init__(self, lon0, lon1, lat0, lat1, W, H, pad=14):
        self.k = math.cos(math.radians((lat0 + lat1) / 2))
        sx = (W - 2 * pad) / ((lon1 - lon0) * self.k); sy = (H - 2 * pad) / (lat1 - lat0)
        self.s = min(sx, sy)
        self.ox = (W - (lon1 - lon0) * self.k * self.s) / 2; self.oy = (H - (lat1 - lat0) * self.s) / 2
        self.lon0, self.lat1 = lon0, lat1
    def __call__(self, lo, la):
        return (self.ox + (lo - self.lon0) * self.k * self.s, self.oy + (self.lat1 - la) * self.s)

def ring_path(P, ring, tol=1.2):
    pts = []
    for p in ring:
        x, y = P(p[0], p[1])
        if pts and abs(x - pts[-1][0]) + abs(y - pts[-1][1]) < tol: continue
        pts.append((x, y))
    if len(pts) < 3: return ''
    return 'M' + 'L'.join('%d,%d' % (round(x), round(y)) for x, y in pts) + 'Z'

def poly_centroid(ring):
    xs = [p[0] for p in ring]; ys = [p[1] for p in ring]
    return sum(xs) / len(xs), sum(ys) / len(ys)

def nice_km(span_km):
    for v in [1, 2, 5, 10, 20, 25, 50, 100, 200]:
        if v >= span_km / 5: return v
    return 200

import json as _j, os as _o
LAKES = _j.load(open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'lakes.json')))
def lakes_svg(P, vb=None):
    o = []
    for l in LAKES:
        pts = [p for r in l['r'] for p in r]
        if vb and (max(p[0] for p in pts) < vb[0] or min(p[0] for p in pts) > vb[1] or max(p[1] for p in pts) < vb[2] or min(p[1] for p in pts) > vb[3]): continue
        d = ''.join(ring_path(P, r, 0.6) for r in l['r'])
        if d: o.append('<path d="%s" fill="#BFDDEA" stroke="#6FA6C2" stroke-width=".8"/>' % d)
    return o

def region_svg(sites, bounds, title, uid, W=760, H=560):
    las = [s['la'] for s in sites]; los = [s['lo'] for s in sites]
    la0, la1, lo0, lo1 = min(las), max(las), min(los), max(los)
    cx, cy = (lo0 + lo1) / 2, (la0 + la1) / 2
    k = math.cos(math.radians(cy))
    hl = max(la1 - la0, (lo1 - lo0) * k * H / W, 0.16) * 0.6
    wl = hl / k * W / H
    P = Proj(cx - wl, cx + wl, cy - hl, cy + hl, W, H, pad=0)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="%st %sd">' % (W, H, uid, uid),
           '<title id="%st">%s: campsite map with protected-area boundaries</title>' % (uid, html.escape(title)),
           '<desc id="%sd">Numbered pins match the campsite profiles below. Shaded areas are protected-area boundaries (simplified).</desc>' % uid,
           '<defs><clipPath id="%sc"><rect width="%d" height="%d"/></clipPath></defs>' % (uid, W, H),
           '<rect width="%d" height="%d" fill="#F4EFE4"/>' % (W, H), '<g clip-path="url(#%sc)">' % uid]
    labels = []
    vb = (cx - wl - .3, cx + wl + .3, cy - hl - .3, cy + hl + .3)
    for b in bounds:
        pts = [p for r in b['r'] for p in r]
        if not pts: continue
        if max(p[0] for p in pts) < vb[0] or min(p[0] for p in pts) > vb[1] or max(p[1] for p in pts) < vb[2] or min(p[1] for p in pts) > vb[3]: continue
        fill, stroke = pa_style(b['d'])
        d = ''.join(ring_path(P, r) for r in b['r'])
        out.append('<path d="%s" fill="%s" fill-opacity=".85" stroke="%s" stroke-width="1.6" stroke-dasharray="%s"/>' % (d, fill, stroke, '5 3' if 'onservancy' in b['d'] or 'sector' in b['d'] else 'none'))
        big = max(b['r'], key=len); x, y = P(*poly_centroid(big))
        if 20 < x < W - 20 and 20 < y < H - 20:
            labels.append((x, y, b['n'], stroke))
    out.extend(lakes_svg(P, vb))
    out.append('</g>')
    # labels with crude collision
    placed = []
    for x, y, n, c in labels:
        w = len(n) * 6.4
        box = (x - w / 2, y - 9, x + w / 2, y + 5)
        if any(not (box[2] < q[0] or box[0] > q[2] or box[3] < q[1] or box[1] > q[3]) for q in placed): continue
        placed.append(box)
        out.append('<text x="%.1f" y="%.1f" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11.5" font-weight="700" fill="%s" stroke="#F4EFE4" stroke-width="3.5" paint-order="stroke" letter-spacing=".4">%s</text>' % (x, y, c, html.escape(n.upper())))
    # watermark logo (Kambu-made map)
    out.append('<image href="%s" x="%d" y="%d" width="%d" height="%d" opacity=".14" preserveAspectRatio="xMidYMid meet" pointer-events="none"/>' % (LOGO, W * .15, H * .33, W * .7, H * .34))
    # pins
    for s in sites:
        x, y = P(s['lo'], s['la'])
        c = COL[s['t']]; op = '1' if s['s'] == 'open' else '.55'
        out.append('<g class="kcm__mpin" data-sid="%s" tabindex="0" role="button" aria-label="%d. %s: show overview" opacity="%s"><circle cx="%.1f" cy="%.1f" r="13" fill="transparent"/><circle class="kcm__mdot" cx="%.1f" cy="%.1f" r="11" fill="%s" stroke="#fff" stroke-width="2.2"/><text x="%.1f" y="%.1f" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="10.5" font-weight="700" fill="#fff" pointer-events="none">%d</text></g>' % (s['sid'], s['num'], html.escape(s['n'], quote=True), op, x, y, x, y, c, x, y + 3.7, s['num']))
    # scale bar
    kmpx = P.s / 111.32
    v = nice_km((W / kmpx) * 0.35)
    L = v * kmpx
    out.append('<g transform="translate(%d,%d)"><rect x="-6" y="-16" width="%.0f" height="26" rx="5" fill="#fff" fill-opacity=".85"/><rect x="0" y="0" width="%.1f" height="4" fill="#233A31"/><text x="%.1f" y="-4" text-anchor="end" font-family="Inter,Arial,sans-serif" font-size="11" fill="#233A31">%d km</text></g>' % (W - L - 24, H - 22, L + 12, L, L, v))
    out.append('<text x="14" y="%d" font-family="Inter,Arial,sans-serif" font-size="13" font-style="italic" font-weight="600" fill="#233A31" stroke="#F4EFE4" stroke-width="3" paint-order="stroke">@kambucampers.com</text>' % (H - 12))
    out.append('<text x="%d" y="16" text-anchor="end" font-family="Inter,Arial,sans-serif" font-size="9.5" fill="#4C554B" stroke="#F4EFE4" stroke-width="3" paint-order="stroke">Boundaries: UNEP-WCMC WDPA, OpenStreetMap (simplified)</text>' % (W - 10))
    out.append('</svg>')
    return '\n'.join(out)

def national_svg(sites, bounds, kenya, W=900, H=1000):
    lon0, lon1, lat0, lat1 = 33.6, 42.2, -4.95, 5.25
    P = Proj(lon0, lon1, lat0, lat1, W, H, pad=20)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" role="img" aria-labelledby="kcmnt kcmnd">' % (W, H),
           '<title id="kcmnt">Kenya campsites and protected areas</title>',
           '<desc id="kcmnd">Every campsite pin in this guide over Kenya\'s national parks, reserves and mapped conservancies.</desc>',
           '<rect width="%d" height="%d" fill="#F8F4EC"/>' % (W, H)]
    d = ''.join(ring_path(P, ring) for poly in kenya['coordinates'] for ring in poly)
    out.append('<path d="%s" fill="#FFFFFF" stroke="#233A31" stroke-width="1.6"/>' % d)
    for b in bounds:
        fill, stroke = pa_style(b['d'])
        out.append('<path d="%s" fill="%s" stroke="%s" stroke-width=".9"/>' % (''.join(ring_path(P, r) for r in b['r']), fill, stroke))
    out.extend(lakes_svg(P))
    out.append('<image href="%s" x="%d" y="%d" width="%d" height="%d" opacity=".12" preserveAspectRatio="xMidYMid meet" pointer-events="none"/>' % (LOGO, 120, 380, 660, 240))
    for name, la, lo, dx, anc in [('Nairobi', -1.286, 36.817, 10, 'start'), ('Mombasa', -4.043, 39.668, -10, 'end'), ('Kisumu', -0.092, 34.768, -10, 'end'),
                                  ('Nanyuki', 0.017, 37.074, -10, 'end'), ('Lodwar', 3.119, 35.597, 10, 'start'), ('Garissa', -0.453, 39.646, 10, 'start')]:
        x, y = P(lo, la)
        out.append('<rect x="%.1f" y="%.1f" width="7" height="7" fill="#191B18"/>' % (x - 3.5, y - 3.5))
        out.append('<text x="%.1f" y="%.1f" font-family="Inter,Arial,sans-serif" font-size="15" font-weight="600" fill="#191B18" text-anchor="%s" stroke="#fff" stroke-width="4" paint-order="stroke">%s</text>' % (x + dx, y + 5, anc, name))
    for t in ['cons', 'priv', 'kws-p', 'mtn', 'kws-s', 'mara', 'kmc']:
        for s in sites:
            if s['t'] != t or s['s'] == 'closed': continue
            x, y = P(s['lo'], s['la'])
            if t == 'kmc':
                out.append('<g class="kcm__mpin" data-sid="%s" tabindex="-1" aria-label="%s"><circle cx="%.1f" cy="%.1f" r="14" fill="transparent"/><circle class="kcm__mdot" cx="%.1f" cy="%.1f" r="9" fill="#233A31" stroke="#C7A874" stroke-width="3"/></g>' % (s['sid'], html.escape(s['n'], quote=True), x, y, x, y))
            else:
                out.append('<g class="kcm__mpin" data-sid="%s" tabindex="-1" aria-label="%s"><circle cx="%.1f" cy="%.1f" r="11" fill="transparent"/><circle class="kcm__mdot" cx="%.1f" cy="%.1f" r="5.4" fill="%s" fill-opacity="%s" stroke="#fff" stroke-width="1.5"/></g>' % (s['sid'], html.escape(s['n'], quote=True), x, y, x, y, COL[t], '.95' if s['s'] == 'open' else '.5'))
    lx, ly = 566, 24
    LAB = [('kws-p', 'KWS public campsite'), ('kws-s', 'KWS special campsite'), ('mtn', 'Mount Kenya hut camp'), ('mara', 'Masai Mara reserve'),
           ('cons', 'Conservancy or ranch'), ('priv', 'Private campsite'), ('kmc', 'Kambu Mara Camp')]
    out.append('<rect x="%d" y="%d" width="318" height="%d" rx="12" fill="#FFFFFF" stroke="#E4DBCA"/>' % (lx, ly, 70 + 25 * len(LAB) + 52))
    out.append('<text x="%d" y="%d" font-family="Inter,Arial,sans-serif" font-size="13" font-weight="700" letter-spacing="1.5" fill="#233A31">WHO RUNS THE CAMPSITE</text>' % (lx + 18, ly + 30))
    for i, (t, l) in enumerate(LAB):
        y = ly + 58 + i * 25
        n = sum(1 for s in sites if s['t'] == t and s['s'] != 'closed')
        out.append('<circle cx="%d" cy="%d" r="7" fill="%s" stroke="%s" stroke-width="%s"/>' % (lx + 28, y - 5, COL[t], '#C7A874' if t == 'kmc' else '#fff', 3 if t == 'kmc' else 1.6))
        out.append('<text x="%d" y="%d" font-family="Inter,Arial,sans-serif" font-size="14" fill="#191B18">%s%s</text>' % (lx + 46, y, l, '' if t == 'kmc' else ' (%d)' % n))
    y = ly + 58 + len(LAB) * 25 + 6
    out.append('<rect x="%d" y="%d" width="16" height="12" fill="#DCEBD3" stroke="#3E7B4F"/><text x="%d" y="%d" font-family="Inter,Arial,sans-serif" font-size="13" fill="#191B18">National park or reserve</text>' % (lx + 20, y - 10, lx + 46, y))
    out.append('<rect x="%d" y="%d" width="16" height="12" fill="#F6E7C8" stroke="#B67A18"/><text x="%d" y="%d" font-family="Inter,Arial,sans-serif" font-size="13" fill="#191B18">Conservancy (where mapped)</text>' % (lx + 20, y + 12, lx + 46, y + 22))
    out.append('<text x="20" y="%d" font-family="Inter,Arial,sans-serif" font-size="15" font-style="italic" font-weight="600" fill="#233A31">@kambucampers.com</text>' % (H - 34))
    out.append('<text x="20" y="%d" font-family="Inter,Arial,sans-serif" font-size="11" fill="#4C554B">Outline: Natural Earth. Boundaries: UNEP-WCMC WDPA and OpenStreetMap, simplified. Pins audited by Kambu Campers, Oct 2026.</text>' % (H - 14))
    out.append('</svg>')
    return '\n'.join(out)
