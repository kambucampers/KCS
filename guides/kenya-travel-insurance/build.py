#!/usr/bin/env python3
"""Assemble the deliverable block, a standalone preview and a render harness
from src/page.html. Refuses to write if seam checks fail."""
import re, pathlib, sys
root = pathlib.Path(__file__).parent
src = (root / 'src' / 'page.html').read_text(encoding='utf-8')

# seam checks
for donor in ('kbh__', 'kgh__', 'kms__', 'kcs__', 'kph__', 'xx__', '.ns ', 'ns__'):
    assert donor not in src, 'stray namespace: ' + donor
left = re.findall(r'__[A-Z][A-Z0-9_]*__', src)
assert not left, 'unreplaced tokens: %r' % left
assert src.count('<h1') == 1, 'exactly one h1'

block = '<!-- wp:html -->\n' + src.strip() + '\n<!-- /wp:html -->\n'
(root / 'out' / 'kenya-travel-insurance-block.html').write_text(block, encoding='utf-8')

head = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Kenya Travel Insurance for Safari: The Mandatory USD 44 Cover, Step by Step | Kambu Campers</title>'
        '<style>html,body{margin:0;padding:0;background:#F1E9DB}</style></head><body>\n')
tail = '\n</body></html>\n'

# preview: images resolve to the repo copies next to the preview
preview = src.replace('/wp-content/uploads/2026/10/', 'img/')
(root / 'out' / 'kenya-travel-insurance-preview.html').write_text(head + preview + tail, encoding='utf-8')

# render harness: same as preview but images absolute to repo dir
harness = src.replace('/wp-content/uploads/2026/10/', '../img/')
(root / 'render' / 'index.html').write_text(head + harness + tail, encoding='utf-8')
print('built: block %d bytes, preview %d bytes' % (len(block), len(head + preview + tail)))
