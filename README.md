# Playwright Visual Regression (Python)

[![Visual Regression Tests](https://github.com/hmik2003/playwright-visual-regression/actions/workflows/playwright.yml/badge.svg)](https://github.com/hmik2003/playwright-visual-regression/actions/workflows/playwright.yml)
[![Tests](https://img.shields.io/badge/CI%20tests-6%20passing-brightgreen)](https://github.com/hmik2003/playwright-visual-regression/actions/workflows/playwright.yml)
[![Local suite](https://img.shields.io/badge/local%20suite-12%20tests-blue)](https://github.com/hmik2003/playwright-visual-regression)
[![Playwright](https://img.shields.io/badge/Playwright-Python-blue?logo=playwright)](https://playwright.dev/python/)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Screenshot-based visual regression testing using Playwright's built-in `to_have_screenshot` comparison. Tests real-world UIs — **Hacker News** and **Bing** — across desktop, tablet, and mobile viewports.

> **Portfolio highlight:** Demonstrates visual QA skills — pixel-diff gates, responsive testing, and CI-enforced screenshot baselines.

## Features

- **Built-in screenshot diffing** — Playwright native visual comparison
- **Multi-viewport** — desktop (1280×720), tablet (768×1024), mobile (390×844)
- **Real UIs** — Hacker News & Bing homepage components
- **CI gates** — pipeline fails on visual drift beyond threshold
- **Masking** — dynamic elements masked to reduce flakiness

## Project Structure

```
playwright-visual-regression/
├── .github/workflows/     # CI pipeline with visual diff artifacts
├── conftest.py            # pytest fixtures
├── fixtures/              # Viewport configs & site URLs
├── pages/                 # Page objects for target sites
├── tests/                 # Visual test modules + baseline snapshots
├── utils/                 # Screenshot helper utilities
├── pytest.ini
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
git clone https://github.com/hmik2003/playwright-visual-regression.git
cd playwright-visual-regression
pip install -r requirements.txt
playwright install
```

### Run Tests

```bash
# CI-stable suite (Hacker News only — same as GitHub Actions)
pytest -m ci

# Full suite including Bing live-site tests (local)
pytest

# Update baseline snapshots after intentional UI changes
pytest --update-snapshots

# Headed mode for debugging
pytest --headed
```

### CI vs local

| Tag | Tests | Runs in CI? | Why |
|-----|-------|-------------|-----|
| `@ci` | 6 | Yes | Hacker News — stable layout, dynamic content masked |
| `@live_site` | 6 | No (local only) | Bing — backgrounds/news change between runs; too flaky for CI gates |

GitHub Actions syncs Linux baselines, then verifies `@ci` tests only.
Use the **Update Visual Snapshots** workflow (manual dispatch) to refresh baselines after intentional UI changes.

## Test Coverage

| Suite              | Tests | Tag          | CI | Targets                          |
|--------------------|-------|--------------|----|----------------------------------|
| Hacker News        | 3     | `@ci`        | ✅ | Full page, main content, header  |
| Responsive (HN)    | 3     | `@ci`        | ✅ | HN × desktop / tablet / mobile   |
| Bing               | 3     | `@live_site` | ❌ | Homepage, search box, logo       |
| Responsive (Bing)  | 3     | `@live_site` | ❌ | Bing × 3 viewports               |

## Visual Thresholds

| Setting            | Value  | Purpose                          |
|--------------------|--------|----------------------------------|
| maxDiffPixelRatio  | 0.02   | Default pixel tolerance          |
| Dynamic sites      | 0.03–0.05 | Higher tolerance for live UIs |

## Updating Baselines

When a site legitimately changes appearance:

```bash
pytest --update-snapshots
git add tests/**/*-snapshots/
git commit -m "chore: update visual baselines"
```

## Tech Stack

- [Playwright for Python](https://playwright.dev/python/) — visual comparison engine
- [pytest](https://docs.pytest.org/) — test runner
- [pytest-playwright](https://github.com/microsoft/playwright-pytest) — browser fixtures
- [GitHub Actions](https://github.com/features/actions) — CI with diff artifacts

## License

MIT
