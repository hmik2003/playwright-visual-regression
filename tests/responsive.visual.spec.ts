import { test, expect } from '../fixtures/test-fixtures';
import { VIEWPORTS } from '../fixtures/test-data';
import { hideHackerNewsDynamicContent } from '../utils/screenshot.helpers';

test.describe('Responsive Visual Regression', () => {
  for (const [label, viewport] of Object.entries(VIEWPORTS)) {
    test(`Hacker News at ${label} viewport (${viewport.width}x${viewport.height}) @ci`, async ({
      page,
      hackerNewsPage,
    }) => {
      await page.setViewportSize(viewport);
      await hackerNewsPage.open();
      await hideHackerNewsDynamicContent(page);
      await expect(page).toHaveScreenshot(`hn-responsive-${label}.png`, {
        fullPage: false,
        clip: { x: 0, y: 0, width: viewport.width, height: Math.min(viewport.height, 900) },
        maxDiffPixelRatio: 0.08,
        animations: 'disabled',
      });
    });
  }

  for (const [label, viewport] of Object.entries(VIEWPORTS)) {
    test(`Bing at ${label} viewport (${viewport.width}x${viewport.height}) @live-site`, async ({
      page,
      bingPage,
    }) => {
      await page.setViewportSize(viewport);
      await bingPage.open();
      await bingPage.dismissCookieBanner();
      await expect(page).toHaveScreenshot(`bing-responsive-${label}.png`, {
        fullPage: false,
        clip: { x: 0, y: 0, width: viewport.width, height: Math.min(viewport.height, 900) },
        mask: [bingPage.searchBox],
        maxDiffPixelRatio: 0.22,
        animations: 'disabled',
      });
    });
  }
});
