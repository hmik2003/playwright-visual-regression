import { test, expect } from '../fixtures/test-fixtures';

test.describe('Bing Visual Regression', () => {
  test.beforeEach(async ({ bingPage }) => {
    await bingPage.open();
    await bingPage.dismissCookieBanner();
  });

  test('homepage full page screenshot', async ({ page, bingPage }) => {
    await expect(page).toHaveScreenshot('bing-homepage.png', {
      fullPage: true,
      mask: [bingPage.searchBox],
      maxDiffPixelRatio: 0.05,
      animations: 'disabled',
    });
  });

  test('search box component screenshot', async ({ bingPage }) => {
    await expect(bingPage.searchBox).toHaveScreenshot('bing-search-box.png', {
      maxDiffPixelRatio: 0.03,
      animations: 'disabled',
    });
  });

  test('logo screenshot', async ({ bingPage }) => {
    await expect(bingPage.logo).toHaveScreenshot('bing-logo.png', {
      maxDiffPixelRatio: 0.02,
      animations: 'disabled',
    });
  });
});
