import { test, expect } from '../fixtures/test-fixtures';

test.describe('Bing Visual Regression @live-site', () => {
  test.beforeEach(async ({ bingPage }) => {
    await bingPage.open();
    await bingPage.dismissCookieBanner();
  });

  test('homepage viewport screenshot', async ({ page, bingPage }) => {
    await expect(page).toHaveScreenshot('bing-homepage.png', {
      fullPage: false,
      clip: { x: 0, y: 0, width: 1280, height: 720 },
      mask: [bingPage.searchBox, bingPage.logo],
      maxDiffPixelRatio: 0.15,
      animations: 'disabled',
    });
  });

  test('search box component screenshot', async ({ bingPage }) => {
    await expect(bingPage.searchBox).toHaveScreenshot('bing-search-box.png', {
      maxDiffPixelRatio: 0.12,
      animations: 'disabled',
      timeout: 15_000,
    });
  });

  test('logo screenshot', async ({ bingPage }) => {
    await expect(bingPage.logo).toHaveScreenshot('bing-logo.png', {
      maxDiffPixelRatio: 0.08,
      animations: 'disabled',
      timeout: 15_000,
    });
  });
});
