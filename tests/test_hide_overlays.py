"""Tests for hide-overlays."""

import pytest
from overlay_css import get_css, get_selectors


KNOWN_GROUPS = {"cookies", "chat", "accessibility"}


# ── get_selectors ────────────────────────────────────────────────────────────

class TestGetSelectors:
    def test_returns_all_groups_by_default(self):
        data = get_selectors()
        assert set(data.keys()) == KNOWN_GROUPS

    def test_returns_lists_of_strings(self):
        data = get_selectors()
        for group, selectors in data.items():
            assert isinstance(selectors, list), f"{group} should be a list"
            assert all(isinstance(s, str) for s in selectors), \
                f"{group} selectors should all be strings"

    def test_filter_single_group(self):
        data = get_selectors(groups=["cookies"])
        assert list(data.keys()) == ["cookies"]

    def test_filter_multiple_groups(self):
        data = get_selectors(groups=["cookies", "chat"])
        assert set(data.keys()) == {"cookies", "chat"}

    def test_unknown_group_silently_omitted(self):
        data = get_selectors(groups=["cookies", "nonexistent"])
        assert list(data.keys()) == ["cookies"]

    def test_empty_groups_list_returns_empty(self):
        data = get_selectors(groups=[])
        assert data == {}

    def test_none_groups_returns_all(self):
        assert get_selectors(None) == get_selectors()

    def test_known_cookie_selectors_present(self):
        cookies = get_selectors(groups=["cookies"])["cookies"]
        assert "#onetrust-consent-sdk" in cookies
        assert "#CybotCookiebotDialog" in cookies

    def test_known_chat_selectors_present(self):
        chat = get_selectors(groups=["chat"])["chat"]
        assert "#drift-frame-chat" in chat
        assert "#intercom-container" in chat

    def test_known_accessibility_selectors_present(self):
        acc = get_selectors(groups=["accessibility"])["accessibility"]
        assert "#userway-widget" in acc
        assert "#ada-button-frame" in acc

    def test_no_empty_selector_strings(self):
        for group, selectors in get_selectors().items():
            assert all(s.strip() for s in selectors), \
                f"{group} contains empty/whitespace selector"


# ── get_css ──────────────────────────────────────────────────────────────────

class TestGetCss:
    def test_returns_string(self):
        assert isinstance(get_css(), str)

    def test_non_empty(self):
        assert get_css().strip()

    def test_contains_display_none(self):
        assert "display: none !important" in get_css()

    def test_contains_visibility_hidden(self):
        assert "visibility: hidden !important" in get_css()

    def test_contains_group_comments(self):
        css = get_css()
        for group in KNOWN_GROUPS:
            assert f"/* {group} */" in css

    def test_filter_group_excludes_others(self):
        css = get_css(groups=["cookies"])
        assert "/* cookies */" in css
        assert "/* chat */" not in css
        assert "/* accessibility */" not in css

    def test_filter_multiple_groups(self):
        css = get_css(groups=["cookies", "chat"])
        assert "/* cookies */" in css
        assert "/* chat */" in css
        assert "/* accessibility */" not in css

    def test_empty_groups_returns_empty_string(self):
        assert get_css(groups=[]) == ""

    def test_selectors_appear_in_css(self):
        css = get_css(groups=["cookies"])
        assert "#onetrust-consent-sdk" in css

    def test_css_is_valid_block_structure(self):
        """Each group block must contain a { ... } rule."""
        css = get_css()
        assert "{" in css and "}" in css

    def test_none_groups_equals_all_groups(self):
        assert get_css(None) == get_css()