#!/usr/bin/env python3
"""Kambu Guide pre-publication checks.

Usage:
    python3 design-system/kambu-guide/tools/check_guide.py guides/<slug>/index.html [...]

Runs the automatable gates from docs/writing-framework.md section 12:
structure, accessibility wiring, interaction wiring, never-claim terms,
banned phrasing, controlled vocabulary, evidence furniture and local assets.
FAIL blocks publication; WARN needs a human decision; INFO is for review.
Exit code is 1 when any FAIL is reported. Standard library only.
"""
import os
import re
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

# Domains that share a content lineage with kambucampers.com (kambu-page-build).
PUBLISHER_NETWORK = [
    "masaimara.ke", "masaimarasafari.travel", "tourwithpipi.com", "maramasai.com", "masaimara.or.ke",
    "marareserve.org", "masaimara.travel", "kenyatourism.in", "masai-mara.in", "masaimara.co.ke",
    "masaimarasafari.in", "masaimara.com",
]
BANNED_PHRASES = [
    "nestled", "boasts", "when it comes to", "look no further", "in today's world", "world-class",
    "unparalleled", "once-in-a-lifetime", "once in a lifetime", "breathtaking destination",
    "don't hesitate", "do not hesitate", "hope this email finds", "touching base", "kindly revert",
    "cheers", "haha", "whether you're a",
]
PAGE_TALK = [
    "this guide covers", "this page covers", "in this article", "in this guide we", "in this guide, we",
    "below we will", "this article will", "we will explore", "let's dive", "let us dive",
]
BAD_LINK_TEXT = {"click here", "read more", "learn more", "here", "this page", "link"}
BARE_LABELS = {"overview", "introduction", "information", "details", "about", "summary", "conclusion"}
US_SPELLINGS = {
    r"\bcolou?r\b": None, r"\bcolor": "colour", r"\bfavorite": "favourite", r"\borganiz": "organis",
    r"\btraveler": "traveller", r"\btraveling\b": "travelling", r"\bkilometer": "kilometre",
    r"\bprogram\b": "programme", r"\bcenter\b": "centre", r"\bcatalog\b": "catalogue",
    r"\bapologiz": "apologis", r"\bcanceled\b": "cancelled",
}
NEVER_CLAIM = [
    (r"\bKATO\b", "KATO membership is not held (kambu-brand-voice Never claim)"),
    (r"\bKPSGA\b", "KPSGA grading is not held (kambu-brand-voice Never claim)"),
]


class Node:
    __slots__ = ("tag", "attrs", "children", "parent", "text")

    def __init__(self, tag, attrs=None, parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs or {}), parent
        self.children, self.text = [], ""

    def cls(self):
        return self.attrs.get("class", "").split()

    def iter(self):
        yield self
        for c in self.children:
            if isinstance(c, Node):
                yield from c.iter()

    def find_all(self, pred):
        return [n for n in self.iter() if pred(n)]

    def ancestors(self):
        p = self.parent
        while p is not None:
            yield p
            p = p.parent

    def inside(self, pred):
        return any(pred(a) for a in self.ancestors())

    def get_text(self, skip=None):
        out = []
        for c in self.children:
            if isinstance(c, Node):
                if c.tag in ("script", "style") or (skip and skip(c)):
                    continue
                out.append(c.get_text(skip))
            else:
                out.append(c)
        return "".join(out)


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, [(k, v or "") for k, v in attrs], self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, [(k, v or "") for k, v in attrs], self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def has_class(name):
    return lambda n: name in n.cls()


def check(path):
    src = open(path, encoding="utf-8").read()
    tb = TreeBuilder()
    tb.feed(src)
    root = tb.root
    results = []

    def report(level, msg):
        results.append((level, msg))

    def drafts(n):
        return "editorial-notes" in n.cls()

    article = next(iter(root.find_all(lambda n: n.attrs.get("id") == "article")), root)
    body_text = article.get_text(skip=drafts)
    norm = re.sub(r"\s+", " ", body_text)
    low = norm.lower()

    # ---------- Structure ----------
    h1 = root.find_all(lambda n: n.tag == "h1")
    report("PASS" if len(h1) == 1 else "FAIL", f"one H1 (found {len(h1)})")

    ids = [n.attrs["id"] for n in root.iter() if "id" in n.attrs]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    report("PASS" if not dup else "FAIL", "unique ids" + (f": duplicates {dup}" if dup else ""))
    idset = set(ids)

    markers = re.findall(r"\[\[[^\]]*\]\]|\bTODO\b|\{\{[^}]*\}\}|lorem ipsum", src, flags=re.I)
    report("PASS" if not markers else "FAIL", "no template markers" + (f": {len(markers)} left, e.g. {markers[0][:40]}" if markers else ""))

    bad_lbl = [n for n in root.find_all(lambda n: n.tag in ("section", "nav", "aside", "figure") and "aria-labelledby" in n.attrs)
               if n.attrs["aria-labelledby"] not in idset]
    report("PASS" if not bad_lbl else "FAIL", "aria-labelledby targets exist" + (f": {[n.attrs['aria-labelledby'] for n in bad_lbl]}" if bad_lbl else ""))

    h2s = [n for n in article.find_all(lambda n: n.tag == "h2") if not n.inside(drafts)]
    bare = [n.get_text().strip() for n in h2s if n.get_text().strip().lower() in BARE_LABELS]
    report("PASS" if not bare else "FAIL", "H2s state something (no bare labels)" + (f": {bare}" if bare else ""))
    no_id = [n.get_text().strip()[:40] for n in h2s if "id" not in n.attrs]
    report("PASS" if not no_id else "WARN", "every H2 has an id for deep links" + (f": {no_id}" if no_id else ""))

    # heading order: no jump of more than one level
    jumps, last = [], 1
    for n in article.iter():
        if n.tag in ("h2", "h3", "h4") and not n.inside(drafts):
            lvl = int(n.tag[1])
            if lvl > last + 1:
                jumps.append(n.get_text().strip()[:40])
            last = lvl
    report("PASS" if not jumps else "WARN", "heading levels do not skip" + (f": {jumps}" if jumps else ""))

    # ---------- Evidence furniture ----------
    report("PASS" if root.find_all(has_class("kg-answer")) else "FAIL", "direct answer block (.kg-answer) present")
    report("PASS" if root.find_all(has_class("kg-reviewed")) else "FAIL", "last-reviewed line (.kg-reviewed) present")
    srcs = root.find_all(has_class("kg-sources"))
    graded = sum(len(s.find_all(has_class("kg-grade"))) for s in srcs)
    report("PASS" if srcs and graded else "FAIL", f"graded sources register (.kg-sources, {graded} graded rows)")
    if root.find_all(drafts):
        report("WARN", "editorial-notes drawer present: remove before publishing")

    # ---------- Never claim / accuracy traps ----------
    for pat, why in NEVER_CLAIM:
        hits = re.findall(pat, src)
        report("PASS" if not hits else "FAIL", f"never-claim {pat.strip(chr(92) + 'b')}" + (f": {why}" if hits else ""))
    eight = [m.group(0) for m in re.finditer(r"[^.]{0,120}\b(8|eight)\s*(km|kilomet\w+)[^.]{0,120}", norm, flags=re.I) if "sekenani" in m.group(0).lower()]
    eight += [m.group(0) for m in re.finditer(r"[^.]{0,120}\b14 minutes[^.]{0,120}", norm, flags=re.I)]
    report("PASS" if not eight else "FAIL", "Kambu Mara Camp distance (about 9.0 km before Sekenani, not 8 km / 14 min)" + (f": '{eight[0].strip()[:90]}'" if eight else ""))

    # ---------- Phrasing ----------
    found = [p for p in BANNED_PHRASES if re.search(r"\b" + re.escape(p) + r"\b", low)]
    report("PASS" if not found else "WARN", "no banned SEO or email phrases" + (f": {found}" if found else ""))
    talk = [p for p in PAGE_TALK if p in low]
    report("PASS" if not talk else "WARN", "no sentences about the page itself" + (f": {talk}" if talk else ""))
    us = []
    for pat, fix in US_SPELLINGS.items():
        if fix is None:
            continue
        for m in re.finditer(pat, norm, flags=re.I):
            ctx = norm[max(0, m.start() - 12):m.end() + 2]
            if "Giraffe Center" in ctx:
                continue
            us.append(f"{m.group(0)}→{fix}")
    report("PASS" if not us else "WARN", "British spelling" + (f": {sorted(set(us))}" if us else ""))
    vocab = []
    if re.search(r"\bsafari drives?\b", low):
        vocab.append("'safari drive' → game drive")
    if re.search(r"\bcustomers?\b", low):
        vocab.append("'customer' → guest")
    guide_alone = re.findall(r"(?:meet|with|ask|tell) (?:the|your) guides?\b(?!-)|\b(?:your|the|a) guides? (?:can|should|might|will|choose|plans?|explains?)\b", low)
    if guide_alone:
        vocab.append(f"'guide' alone where a driver-guide is meant: {guide_alone[:3]}")
    for m in re.finditer(r"[^.]{0,60}\b(budget|luxury)\b[^.]{0,60}", norm, flags=re.I):
        if "kambu" in m.group(0).lower():
            vocab.append(f"'{m.group(1)}' near Kambu: '{m.group(0).strip()[:70]}'")
    report("PASS" if not vocab else "WARN", "controlled vocabulary" + (f": {vocab}" if vocab else ""))

    # prices need a basis in the same sentence
    no_basis = []
    for sent in re.split(r"(?<=[.!?])\s+", norm):
        if re.search(r"(US\$|USD|KES|\$)\s?\d", sent) and not re.search(
                r"per (person|adult|tent|vehicle|day|night|group)|total|each|non-resident|resident|benchmark|per-person", sent, flags=re.I):
            no_basis.append(sent.strip()[:80])
    cells = [n for n in article.find_all(lambda n: n.tag == "td" and "numeric" in n.cls())]
    report("PASS" if not no_basis else "WARN", "every price sentence states its basis" + (f": {no_basis[:3]}" if no_basis else "")
           + (f" ({len(cells)} numeric table cells: check captions carry the basis)" if cells else ""))

    # ---------- Links ----------
    links = article.find_all(lambda n: n.tag == "a" and "href" in n.attrs)
    net = sorted({a.attrs["href"] for a in links if any(d in a.attrs["href"] for d in PUBLISHER_NETWORK)})
    report("PASS" if not net else "FAIL", "no citations to the publisher network" + (f": {net}" if net else ""))
    blank = [a.attrs["href"] for a in root.find_all(lambda n: n.tag == "a" and n.attrs.get("target") == "_blank")
             if "noopener" not in a.attrs.get("rel", "")]
    report("PASS" if not blank else "FAIL", "target=_blank links carry rel=noopener" + (f": {blank}" if blank else ""))
    weak = [a.get_text().strip() for a in links if a.get_text().strip().lower().rstrip(" →.") in BAD_LINK_TEXT]
    report("PASS" if not weak else "WARN", "descriptive link text" + (f": {weak}" if weak else ""))
    broken = [a.attrs["href"] for a in links if a.attrs["href"].startswith("#") and len(a.attrs["href"]) > 1 and a.attrs["href"][1:] not in idset]
    report("PASS" if not broken else "FAIL", "in-page links resolve" + (f": {broken}" if broken else ""))

    def furniture(n):
        return any(c in n.cls() for c in ("kg-daynav", "contents", "kg-sources", "editorial-notes", "breadcrumbs", "route-stops", "table-scroll"))
    prose_links = [a for a in links if not a.inside(furniture) and "kambucampers.com" in a.attrs["href"] and not a.attrs["href"].startswith("mailto:")]
    home = [a for a in prose_links if re.fullmatch(r"https?://(www\.)?kambucampers\.com/?", a.attrs["href"])]
    report("PASS" if len(home) == 1 else "WARN", f"entity-home link in prose once, from a credential (found {len(home)})")
    by_url, by_text = {}, {}
    for a in prose_links:
        by_url.setdefault(a.attrs["href"], set()).add(a.get_text().strip())
        t = a.get_text().strip().lower()
        by_text.setdefault(t, set()).add(a.attrs["href"])
    multi_anchor = {u: sorted(t) for u, t in by_url.items() if len(t) > 1}
    multi_url = {t: sorted(u) for t, u in by_text.items() if len(u) > 1}
    report("PASS" if not multi_anchor and not multi_url else "WARN",
           "anchor discipline (one phrase per URL)" + (f": {multi_anchor or multi_url}" if multi_anchor or multi_url else ""))
    report("INFO", f"{len({a.attrs['href'] for a in prose_links})} internal kambucampers.com URLs to verify as live: "
           + ", ".join(sorted({a.attrs['href'].replace('https://kambucampers.com', '') for a in prose_links})))

    # ---------- Images ----------
    imgs = root.find_all(lambda n: n.tag == "img")
    no_alt = [i.attrs.get("src") for i in imgs if not i.attrs.get("alt", "").strip()]
    report("PASS" if not no_alt else "FAIL", "every image has alt text" + (f": {no_alt}" if no_alt else ""))
    no_dims = [i.attrs.get("src") for i in imgs if not (i.attrs.get("width") and i.attrs.get("height"))]
    report("PASS" if not no_dims else "FAIL", "every image has width and height" + (f": {no_dims}" if no_dims else ""))
    eager = [i.attrs.get("src") for i in imgs if i.attrs.get("loading") != "lazy" and not i.inside(has_class("hero-figure"))]
    report("PASS" if not eager else "WARN", "below-the-fold images lazy-load" + (f": {eager}" if eager else ""))
    base = os.path.dirname(os.path.abspath(path))
    local = set()
    for i in imgs:
        local.add(i.attrs.get("src", ""))
        for part in i.attrs.get("srcset", "").split(","):
            if part.strip():
                local.add(part.strip().split()[0])
    for a in root.find_all(has_class("kg-gallery__open")):
        local.add(a.attrs.get("href", ""))
    missing = sorted(p for p in local if p and not re.match(r"^(https?:|data:|//)", p) and not os.path.exists(os.path.join(base, p)))
    report("PASS" if not missing else "FAIL", "local image files exist" + (f": {missing}" if missing else ""))
    galleries = root.find_all(has_class("kg-gallery"))
    uncredited = sum(1 for g in galleries for f in g.find_all(lambda n: n.tag == "figcaption") if not f.find_all(has_class("kg-credit")))
    report("PASS" if not uncredited else "WARN", f"gallery captions carry a credit ({uncredited} without)")

    # ---------- Interaction wiring ----------
    for ts in root.find_all(lambda n: "data-kg-tabs" in n.attrs):
        name = ts.attrs.get("data-kg-label", "(unnamed)")
        tabs = ts.find_all(lambda n: "data-kg-tab" in n.attrs)
        problems = []
        if not ts.attrs.get("data-kg-label"):
            problems.append("no data-kg-label")
        selected = [t for t in tabs if t.attrs.get("aria-selected") == "true" or "data-kg-default" in t.attrs]
        if len(selected) != 1:
            problems.append(f"{len(selected)} default tabs")
        for t in tabs:
            pid = t.attrs["data-kg-tab"]
            panel = next(iter(root.find_all(lambda n: n.attrs.get("id") == pid)), None)
            if panel is None:
                problems.append(f"missing panel #{pid}")
            elif not panel.find_all(lambda n: n.tag in ("h2", "h3", "h4")):
                problems.append(f"panel #{pid} has no heading")
            if t.tag != "button":
                problems.append(f"tab for #{pid} is not a <button>")
        lst = ts.find_all(has_class("kg-tabs__list"))
        if lst and "hidden" not in lst[0].attrs:
            problems.append("tab list should start hidden (JS reveals it)")
        report("PASS" if not problems else "FAIL", f"tabs '{name}' wiring ({len(tabs)} tabs)" + (f": {problems}" if problems else ""))
    for acc in root.find_all(has_class("kg-acc")):
        items = acc.find_all(lambda n: n.tag == "details")
        first_open = bool(items) and "open" in items[0].attrs
        lists = sum(1 for d in items if d.find_all(lambda n: n.tag in ("ul", "ol")))
        report("PASS" if first_open else "WARN", f"accordion: first of {len(items)} items open")
        if acc.inside(lambda n: n.attrs.get("aria-labelledby") == "faq" or n.attrs.get("id") == "faq"):
            report("PASS" if 6 <= len(items) <= 10 else "WARN", f"FAQ has about eight questions ({len(items)})")
            report("PASS" if not lists else "WARN", "FAQ answers are prose, not lists" + (f" ({lists} with lists)" if lists else ""))
    for g in galleries:
        n = len(g.find_all(has_class("kg-gallery__slide")))
        ok = g.find_all(lambda x: "data-kg-prev" in x.attrs) and g.find_all(lambda x: "data-kg-next" in x.attrs)
        report("PASS" if ok and n >= 2 else "WARN", f"gallery '{g.attrs.get('aria-label', '')}' has {n} slides and arrow controls")

    # ---------- Suitability and decision rules ----------
    report("PASS" if root.find_all(has_class("kg-suit")) else "WARN", "suitability split (suits / choose something else)")
    if root.find_all(lambda n: "kg-tabs--vertical" in n.cls()) or "compare" in low:
        report("PASS" if root.find_all(has_class("kg-choose")) else "WARN", "comparison ends with Choose A if / Choose B if")
    fieldnotes = root.find_all(has_class("kg-fieldnote"))
    report("PASS" if 1 <= len(fieldnotes) <= 3 else "WARN", f"field notes (first-party experience): {len(fieldnotes)} (aim 1-3)")

    return results


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    failed = False
    for path in argv[1:]:
        print(f"\n{path}")
        res = check(path)
        width = max(len(l) for l, _ in res)
        for level, msg in res:
            print(f"  {level:<{width}}  {msg}")
        counts = {k: sum(1 for l, _ in res if l == k) for k in ("PASS", "WARN", "FAIL", "INFO")}
        print(f"  -- {counts['PASS']} pass, {counts['WARN']} warn, {counts['FAIL']} fail")
        failed |= counts["FAIL"] > 0
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
