# Contributing to hide-overlays

Thanks for helping grow the selector list. The bar is low — if you found an overlay that slips through, a PR is the right fix.

## What belongs here

- Cookie / GDPR consent banners
- Live chat widgets
- Accessibility overlay widgets (accessiBe, UserWay, AudioEye, etc.)

If the element you want to hide is page-specific content rather than a third-party widget injected across many sites, it probably doesn't belong here.

## Adding a selector

1. Fork the repo and create a branch: `git checkout -b add/<vendor-name>`
2. Open `overlay_css/selectors.yaml`
3. Add your selector under the correct group (`cookies`, `chat`, or `accessibility`)
4. Keep one selector per line; use the most specific selector that reliably targets the element

```yaml
cookies:
  - "#your-new-selector"   # VendorName consent banner
```

5. Open a pull request with:
   - The vendor / product name in the PR title, e.g. `Add: CookieYes banner`
   - A brief note on what site or widget the selector targets

## Running tests locally

```bash
uv run --with pytest pytest tests/ -v
```

All 22 existing tests must stay green. No new tests are required for selector additions, but feel free to add one that asserts your selector string is present.

## Proposing a new group

If you have selectors that don't fit `cookies`, `chat`, or `accessibility`, open an issue first to discuss the new group name before submitting a PR.

## License

By contributing you agree that your additions are released under the project's MIT license.
