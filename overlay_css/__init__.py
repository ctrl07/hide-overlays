"""
hide-overlays: curated CSS to hide cookie banners, chat widgets,
and accessibility overlays.
"""

from importlib.resources import files
from typing import Iterable
import yaml

_SELECTORS_FILE = files("overlay_css") / "selectors.yaml"


def _load() -> dict[str, list[str]]:
    return yaml.safe_load(_SELECTORS_FILE.read_text(encoding="utf-8"))


def get_selectors(groups: Iterable[str] | None = None) -> dict[str, list[str]]:
    """Return the selector dict, optionally filtered to specific groups.

    Args:
        groups: iterable of group names to include, e.g. ``["cookies", "chat"]``.
                If None, all groups are returned.

    Returns:
        Dict mapping group name → list of CSS selectors.
    """
    data = _load()
    if groups is None:
        return data
    return {g: data[g] for g in groups if g in data}


def get_css(groups: Iterable[str] | None = None) -> str:
    """Return a CSS string that hides all matched elements.

    Args:
        groups: iterable of group names to include.
                If None, all groups are included.

    Returns:
        CSS string ready to inject via ``page.add_style_tag`` or
        ``driver.execute_script``.

    Example::

        from overlay_css import get_css

        # Playwright
        page.add_style_tag(content=get_css())

        # Selenium
        driver.execute_script(
            f"const s=document.createElement('style');"
            f"s.innerHTML=`{get_css()}`;"
            f"document.head.appendChild(s);"
        )
    """
    selectors = get_selectors(groups)
    rules = []
    for group, sel_list in selectors.items():
        if sel_list:
            joined = ",\n".join(sel_list)
            rules.append(
                f"/* {group} */\n"
                f"{joined} {{\n"
                f"  display: none !important;\n"
                f"  visibility: hidden !important;\n"
                f"}}"
            )
    return "\n\n".join(rules)


__all__ = ["get_css", "get_selectors"]