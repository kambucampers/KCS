#!/usr/bin/env python3
"""Bundle a Kambu guide into one self-contained HTML file.

Usage:
    python3 design-system/kambu-guide/tools/build_standalone.py guides/<slug>/index.html [-o dist/<slug>.html] [--embed-images]

Inlines every local stylesheet and script the page links, so the result opens
anywhere (email attachment, a preview, a CMS that takes one HTML file). Google
Fonts stay as an @import. With --embed-images, local images become data: URIs
(the 800 px file for each <img>, the largest file for gallery links); expect
the file to grow by roughly a third of the image weight.
"""
import argparse
import base64
import mimetypes
import os
import re
import sys


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or ("image/webp" if path.endswith(".webp") else "application/octet-stream")
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"


def is_local(ref):
    return ref and not re.match(r"^(https?:|data:|//|mailto:|#)", ref)


def build(src_path, embed_images=False):
    base = os.path.dirname(os.path.abspath(src_path))
    html = read(src_path)
    missing = []

    def inline_css(m):
        href = m.group(1)
        p = os.path.join(base, href)
        if not is_local(href) or not os.path.exists(p):
            return m.group(0)
        css = read(p)
        # @import must stay the first rule inside the <style> block
        imports = re.findall(r"@import[^;]+;", css)
        css = re.sub(r"@import[^;]+;", "", css)
        return "<style>/* " + os.path.basename(href) + " */\n" + "\n".join(imports) + "\n" + css.strip() + "\n</style>"

    html = re.sub(r'<link rel="stylesheet" href="([^"]+)">', inline_css, html)

    def inline_js(m):
        src = m.group(1)
        p = os.path.join(base, src)
        if not is_local(src) or not os.path.exists(p):
            return m.group(0)
        return "<script>/* " + os.path.basename(src) + " */\n" + read(p).replace("</script", "<\\/script") + "\n</script>"

    html = re.sub(r'<script src="([^"]+)"(?: defer)?></script>', inline_js, html)

    if embed_images:
        def embed_attr(m):
            attr, ref = m.group(1), m.group(2)
            p = os.path.join(base, ref)
            if not is_local(ref):
                return m.group(0)
            if not os.path.exists(p):
                missing.append(ref)
                return m.group(0)
            return f'{attr}="{data_uri(p)}"'
        html = re.sub(r'\s(?:srcset|imagesrcset|imagesizes)="[^"]*"', "", html)
        html = re.sub(r'<link rel="preload" as="image"[^>]*>', "", html)
        html = re.sub(r'\b(src)="([^"]+\.(?:webp|jpe?g|png|avif|gif|svg))"', embed_attr, html)
        html = re.sub(r'(?<=<a class="kg-gallery__open" )(href)="([^"]+)"', embed_attr, html)
    return html, missing


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page")
    ap.add_argument("-o", "--out")
    ap.add_argument("--embed-images", action="store_true")
    a = ap.parse_args()
    slug = os.path.basename(os.path.dirname(os.path.abspath(a.page)))
    out = a.out or os.path.join("dist", f"{slug}.html")
    html, missing = build(a.page, a.embed_images)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {out} ({len(html.encode()) / 1024:.0f} KB)")
    if missing:
        print("missing local images (left as links): " + ", ".join(sorted(set(missing))), file=sys.stderr)
    if not a.embed_images:
        print("images still load from the page's assets/ folder; use --embed-images for a single portable file")


if __name__ == "__main__":
    main()
