# Kambu Campers content system

Strategy, design system and guide pages for kambucampers.com.

| Folder | What it holds |
|---|---|
| [`strategy/`](strategy/) | Source-context charter, topical map (250-page cap), conservation vector, production tracker |
| [`design-system/kambu-guide/`](design-system/kambu-guide/) | The Kambu Guide design system: CSS, interactive components, writing framework, checker and bundler |
| [`guides/`](guides/) | Guide pages, one folder each. Start from [`guides/_template/`](guides/_template/); the worked example is [`guides/10-day-kenya-safari-itinerary/`](guides/10-day-kenya-safari-itinerary/) |
| [`.claude/skills/kambu-safari-guide/`](.claude/skills/kambu-safari-guide/SKILL.md) | The Claude skill that writes and builds a guide with this system |

Preview locally with `python3 -m http.server` from the repo root, then open
`http://localhost:8000/guides/<slug>/`. Check a page with
`python3 design-system/kambu-guide/tools/check_guide.py guides/<slug>/index.html`.
