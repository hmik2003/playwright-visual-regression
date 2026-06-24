import { Page } from '@playwright/test';
import { BasePage } from './base.page';
import { SITES } from '../fixtures/test-data';

export class HackerNewsPage extends BasePage {
  async open() {
    await this.goto(SITES.hackerNews.url);
    await this.waitForStableLayout(1500);
  }

  get mainContent() {
    return this.page.locator('table.itemlist, #hnmain');
  }

  get header() {
    return this.page.locator('tr:first-child');
  }
}
