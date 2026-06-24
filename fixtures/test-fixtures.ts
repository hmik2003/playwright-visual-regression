import { test as base } from '@playwright/test';
import { HackerNewsPage } from '../pages/hacker-news.page';
import { BingPage } from '../pages/bing.page';

type VisualFixtures = {
  hackerNewsPage: HackerNewsPage;
  bingPage: BingPage;
};

export const test = base.extend<VisualFixtures>({
  hackerNewsPage: async ({ page }, use) => {
    await use(new HackerNewsPage(page));
  },

  bingPage: async ({ page }, use) => {
    await use(new BingPage(page));
  },
});

export { expect } from '@playwright/test';
