from playwright.sync_api import Page

from fixtures.test_data import HN_DYNAMIC_SELECTORS


def hide_hacker_news_dynamic_content(page: Page) -> None:
    page.evaluate(
        """(sels) => {
            sels.forEach(sel => {
                document.querySelectorAll(sel).forEach(el => {
                    el.style.visibility = 'hidden';
                });
            });
        }""",
        HN_DYNAMIC_SELECTORS,
    )
