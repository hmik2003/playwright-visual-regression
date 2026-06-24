from fixtures.test_data import SITES
from pages.base_page import BasePage


class HackerNewsPage(BasePage):
    def open(self) -> None:
        self.goto(SITES["hacker_news"]["url"])
        self.wait_for_stable_layout(1500)

    @property
    def main_content(self):
        return self.page.locator("table.itemlist, #hnmain")

    @property
    def header(self):
        return self.page.locator("#hnmain .pagetop, #hnmain table:first-of-type tbody tr").first
