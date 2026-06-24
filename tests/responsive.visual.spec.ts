import { test, expect } from '../fixtures/test-fixtures';
import { VIEWPORTS } from '../fixtures/test-data';

test.describe('Responsive Visual Regression', () => {
  for (const [label, viewport] of Object.entries(VIEWPORTS)) {
    test(`Hacker News at ${label} viewport (${viewport.width}x${viewport.height})`, async ({
      page,
      hackerNewsPage,
    }) => {
      await page.setViewportSize(viewport);
      await hackerNewsPage.open();
      await expect(page).toHaveScreenshot(`hn-responsive-${label}.png`, {
        fullPage: false,
        clip: { x: 0, y: 0, width: viewport.width, height: Math.min(viewport.height, 900) },
        maxDiffPixelRatio: 0.04,
        animations: 'disabled',
      });
    });
  }

  for (const [label, viewport] of Object.entries(VIEWPORTS)) {
    test(`Bing at ${label} viewport (${viewport.width}x${viewport.height})`, async ({
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
        maxDiffPixelRatio: 0.05,
        animations: 'disabled',
      });
    });
  }
});
