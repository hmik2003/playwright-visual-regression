import { BasePage } from './base.page';
import { SITES } from '../fixtures/test-data';

export class BingPage extends BasePage {
  async open() {
    await this.goto(SITES.bing.url);
    await this.waitForStableLayout(2000);
  }

  async dismissCookieBanner() {
    const acceptButton = this.page.locator('#bnp_btn_accept, button[id*="accept"]');
    if (await acceptButton.isVisible({ timeout: 3000 }).catch(() => false)) {
      await acceptButton.click();
      await this.page.waitForTimeout(500);
    }
  }

  get searchBox() {
    return this.page.locator('#sb_form_q, input[name="q"]');
  }

  get logo() {
    return this.page.locator('#b_logo, .b_logo');
  }

  get homepageContent() {
    return this.page.locator('#b_content, body');
  }
}
