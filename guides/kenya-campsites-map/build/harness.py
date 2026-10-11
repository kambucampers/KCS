import re,json,os
src=open('out/kenya-campsites-map-preview.html').read()
ch=json.load(open('../img/chosen.json'))
km={o['thumb'].split('?')[0].rsplit('/',2)[-2]:os.path.abspath(f'../img/t{i}.jpg') for i,o in enumerate(ch)}
open('render/preview-local.html','w').write(re.sub(r'https://upload\.wikimedia\.org/[^\'"\s)]+',lambda m:'file://'+km[m.group(0).rsplit('/',2)[-2]],src))
