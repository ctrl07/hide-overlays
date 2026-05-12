# hide-overlays

Curated CSS selectors that hide cookie consent banners, live chat widgets, and accessibility overlays before web capture.

Works with any browser automation tool — Playwright, Selenium, Puppeteer.

## Install

```
pip install hide-overlays
```

## Usage

### Playwright

```python
from overlay_css import get_css

page.add_style_tag(content=get_css())
```

### Selenium

```python
from overlay_css import get_css

css = get_css()
driver.execute_script(
    f"const s=document.createElement('style');s.innerHTML=`{css}`;document.head.appendChild(s);"
)
```

### Filter to specific groups

```python
from overlay_css import get_css, get_selectors

# Only hide cookie banners
page.add_style_tag(content=get_css(groups=["cookies"]))

# Inspect the raw selectors
print(get_selectors(groups=["chat", "accessibility"]))
```

## Selector groups

| Group | Covers |
|---|---|
| `cookies` | OneTrust, Cookiebot, Termly, cc-window, dealer-specific banners |
| `chat` | Drift, Intercom, Zopim, HubSpot, generic chat widget patterns |
| `accessibility` | accessiBe, UserWay, AudioEye, ADA widget buttons |

## Adding selectors

The selectors live in `overlay_css/selectors.yaml`. Open a pull request to add new ones.

## License

MIT
