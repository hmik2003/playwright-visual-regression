import { test, expect } from '../fixtures/test-fixtures';
import { hideHackerNewsDynamicContent } from '../utils/screenshot.helpers';

test.describe('Hacker News Visual Regression @ci', () => {
  test.beforeEach(async ({ hackerNewsPage }) => {
    await hackerNewsPage.open();
  });

  test('homepage layout screenshot', async ({ page }) => {
    await hideHackerNewsDynamicContent(page);
    await expect(page).toHaveScreenshot('hn-homepage.png', {
      fullPage: false,
      clip: { x: 0, y: 0, width: 1280, height: 720 },
      maxDiffPixelRatio: 0.08,
      animations: 'disabled',
    });
  });

  test('main content area screenshot', async ({ page, hackerNewsPage }) => {
    await hideHackerNewsDynamicContent(page);
    await expect(hackerNewsPage.mainContent).toHaveScreenshot('hn-main-content.png', {
      maxDiffPixelRatio: 0.08,
      animations: 'disabled',
    });
  });

  test('header navigation screenshot', async ({ hackerNewsPage }) => {
    await expect(hackerNewsPage.header).toHaveScreenshot('hn-header.png', {
      maxDiffPixelRatio: 0.06,
      animations: 'disabled',
    });
  });
});
