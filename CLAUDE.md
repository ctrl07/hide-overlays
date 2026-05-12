# overlay-css — project notes

## What this is

A PyPI package that provides curated CSS selectors to hide cookie consent
banners, live chat widgets, and accessibility overlays before web capture
(screenshots, PDFs). Spun out from the TARS scraper project.

## Status

Scaffolded, not yet published. All files are ready except the two manual
edits listed below.

## Structure

```
overlay-css/
├── overlay_css/
│   ├── __init__.py       # Public API: get_css(), get_selectors()
│   └── selectors.yaml    # All CSS selectors organised by group
├── pyproject.toml        # Package metadata — needs author + URLs filled in
├── README.md
├── LICENSE               # Needs real name filled in
└── CLAUDE.md             # This file
```

## Before publishing — two manual edits required

### 1. pyproject.toml
- `authors` — replace `Your Name` and `you@example.com`
- `[project.urls]` — replace `ctrl07/overlay-css` with the real GitHub repo
  slug once you create it

### 2. LICENSE
- Replace `Your Name` on line 3 with your real name

## Publishing steps (no TestPyPI)

```bash
# 1. Install build tools
uv add --dev hatchling

# 2. Build the wheel and sdist
uv build

# 3. Publish to PyPI (needs PYPI_TOKEN or interactive login)
uv publish
```

You will be prompted for a PyPI API token on first publish.
Get one at: https://pypi.org/manage/account/token/

## API

```python
from overlay_css import get_css, get_selectors

# All groups
css = get_css()

# Specific groups only
css = get_css(groups=["cookies", "chat"])

# Raw selector dict
d = get_selectors(groups=["accessibility"])
```

## Selector groups

| Group | Covers |
|---|---|
| `cookies` | OneTrust, Cookiebot, Termly, cc-window, dealer-specific |
| `chat` | Drift, Intercom, Zopim, HubSpot, generic patterns |
| `accessibility` | accessiBe, UserWay, AudioEye, ADA widget buttons |

## Adding selectors

Edit `overlay_css/selectors.yaml` — add a selector string under the
appropriate group. Group names are cosmetic (used as CSS comments only).

## Future ideas

- GitHub Actions workflow: publish to PyPI on `v*` tag (same pattern as TARS)
- Dependabot for the actions workflow
- Community PR guide for adding new selectors
- `.gitignore` (copy from TARS: venv, pycache, dist/)

## Related

- TARS scraper (parent project): `c:\Users\suyog.kurlekar\Downloads\tools\bs4`
- TARS uses `_build_css(cfg)` which does the same thing — overlay-css is the
  standalone, installable version of that function
