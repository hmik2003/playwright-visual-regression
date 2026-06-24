import { test, expect } from '../fixtures/test-fixtures';
import { hideDynamicElements } from '../utils/screenshot.helpers';

test.describe('Hacker News Visual Regression', () => {
  test.beforeEach(async ({ hackerNewsPage }) => {
    await hackerNewsPage.open();
  });

  test('homepage full page screenshot', async ({ page }) => {
    await hideDynamicElements(page, ['.comhead a', '.age']);
    await expect(page).toHaveScreenshot('hn-homepage.png', {
      fullPage: true,
      maxDiffPixelRatio: 0.03,
      animations: 'disabled',
    });
  });

  test('main content area screenshot', async ({ hackerNewsPage }) => {
    await expect(hackerNewsPage.mainContent).toHaveScreenshot('hn-main-content.png', {
      maxDiffPixelRatio: 0.03,
      animations: 'disabled',
    });
  });

  test('header navigation screenshot', async ({ hackerNewsPage }) => {
    await expect(hackerNewsPage.header).toHaveScreenshot('hn-header.png', {
      maxDiffPixelRatio: 0.02,
      animations: 'disabled',
    });
  });
});
