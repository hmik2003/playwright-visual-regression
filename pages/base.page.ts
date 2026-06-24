import { Page } from '@playwright/test';

export class BasePage {
  constructor(protected readonly page: Page) {}

  async goto(url: string) {
    await this.page.goto(url, { waitUntil: 'domcontentloaded' });
  }

  async waitForStableLayout(timeoutMs = 2000) {
    await this.page.waitForLoadState('networkidle').catch(() => {});
    await this.page.waitForTimeout(timeoutMs);
  }
}
