# Kenya campsites map guide

Proposed URL: `/ke/guides/kenya-campsites-map/`

- `block.html`: the WordPress Custom HTML block. Before pasting it, replace `__MAPBOX_PUBLIC_TOKEN__` with the Mapbox public (pk) token. The token is kept out of this public repo, and it should be URL-restricted to kambucampers.com and staging9.
- `kenya-campsites-database.csv`: all 187 campsites with their researched fields, Google review stats, pros and cons, and photo URLs still to be licensed.
- `RESEARCH.md`: method, coverage, sources and open items.
- `VERIFY.txt`: test results for this build.
- `build/`: generator and test sources. The input data stays in the build workspace and isn't committed.
