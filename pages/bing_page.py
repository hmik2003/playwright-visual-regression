from fixtures.test_data import SITES
from pages.base_page import BasePage


class BingPage(BasePage):
    def open(self) -> None:
        self.goto(SITES["bing"]["url"])
        self.wait_for_stable_layout(1000)

    def dismiss_cookie_banner(self) -> None:
        accept = self.page.locator('#bnp_btn_accept, button[id*="accept"]')
        if accept.is_visible(timeout=3000):
            accept.click()
            self.page.wait_for_timeout(500)

    @property
    def search_box(self):
        return self.page.locator('#sb_form_q, input[name="q"]')

    @property
    def logo(self):
        return self.page.locator(
            '#b_logo, .b_logo, a[aria-label="Bing"], header a[href*="bing"]'
        ).first
