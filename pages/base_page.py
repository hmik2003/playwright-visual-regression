from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_for_stable_layout(self, timeout_ms: int = 1000) -> None:
        try:
            self.page.wait_for_load_state("load")
        except Exception:
            pass
        self.page.wait_for_timeout(timeout_ms)
