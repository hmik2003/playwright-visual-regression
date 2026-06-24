# Playwright Visual Regression

[![Visual Regression Tests](https://github.com/hmik2003/playwright-visual-regression/actions/workflows/playwright.yml/badge.svg)](https://github.com/hmik2003/playwright-visual-regression/actions/workflows/playwright.yml)
[![Tests](https://img.shields.io/badge/CI%20tests-6%20passing-brightgreen)](https://github.com/hmik2003/playwright-visual-regression/actions/workflows/playwright.yml)
[![Local suite](https://img.shields.io/badge/local%20suite-12%20tests-blue)](https://github.com/hmik2003/playwright-visual-regression)
[![Playwright](https://img.shields.io/badge/Playwright-1.49-blue?logo=playwright)](https://playwright.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue?logo=typescript)](https://www.typescriptlang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Screenshot-based visual regression testing using Playwright's built-in `toHaveScreenshot` comparison. Tests real-world UIs — **Hacker News** and **Bing** — across desktop, tablet, and mobile viewports.

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
├── fixtures/              # Viewport configs & site URLs
├── pages/                 # Page objects for target sites
├── tests/                 # Visual test specs + baseline snapshots
├── utils/                 # Screenshot helper utilities
├── playwright.config.ts
└── package.json
```

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) 18+
- npm 9+

### Installation

```bash
git clone https://github.com/hmik2003/playwright-visual-regression.git
cd playwright-visual-regression
npm install
npx playwright install
```

### Run Tests

```bash
# CI-stable suite (Hacker News only — same as GitHub Actions)
npx playwright test --grep @ci

# Full suite including Bing live-site tests (local)
npm test

# Update baseline snapshots after intentional UI changes
npm run test:update

# Headed mode for debugging
npm run test:headed
```

### CI vs local

| Tag | Tests | Runs in CI? | Why |
|-----|-------|-------------|-----|
| `@ci` | 6 | Yes | Hacker News — stable layout, dynamic content masked |
| `@live-site` | 6 | No (local only) | Bing — backgrounds/news change between runs; too flaky for CI gates |

GitHub Actions runs **desktop-chrome** only, syncs Linux baselines, then verifies `@ci` tests.
Use the **Update Visual Snapshots** workflow (manual dispatch) to refresh baselines after intentional UI changes.

### View Report

```bash
npm run report
```

## Test Coverage

| Suite              | Tests | Tag         | CI | Targets                          |
|--------------------|-------|-------------|----|----------------------------------|
| Hacker News        | 3     | `@ci`       | ✅ | Full page, main content, header  |
| Responsive (HN)    | 3     | `@ci`       | ✅ | HN × desktop / tablet / mobile   |
| Bing               | 3     | `@live-site`| ❌ | Homepage, search box, logo       |
| Responsive (Bing)  | 3     | `@live-site`| ❌ | Bing × 3 viewports               |

## Visual Thresholds

| Setting            | Value  | Purpose                          |
|--------------------|--------|----------------------------------|
| maxDiffPixelRatio  | 0.02   | Default pixel tolerance          |
| Dynamic sites      | 0.03–0.05 | Higher tolerance for live UIs |

## Updating Baselines

When a site legitimately changes appearance:

```bash
npm run test:update
git add tests/**/*-snapshots/
git commit -m "chore: update visual baselines"
```

## Tech Stack

- [Playwright](https://playwright.dev/) — visual comparison engine
- [TypeScript](https://www.typescriptlang.org/) — type-safe tests
- [GitHub Actions](https://github.com/features/actions) — CI with diff artifacts

## License

MIT
