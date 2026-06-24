import { Page } from '@playwright/test';

export class BasePage {
  constructor(protected readonly page: Page) {}

  async goto(url: string) {
    await this.page.goto(url, { waitUntil: 'domcontentloaded' });
  }

  async waitForStableLayout(timeoutMs = 1000) {
    await this.page.waitForLoadState('load').catch(() => {});
    await this.page.waitForTimeout(timeoutMs);
  }
}
