import pytest
from playwright.sync_api import expect

from utils.screenshot_helpers import hide_hacker_news_dynamic_content


@pytest.mark.ci
class TestHackerNewsVisual:
    def test_homepage_layout(self, page, hacker_news_page):
        hacker_news_page.open()
        hide_hacker_news_dynamic_content(page)
        expect(page).to_have_screenshot(
            "hn-homepage.png",
            full_page=False,
            clip={"x": 0, "y": 0, "width": 1280, "height": 720},
            max_diff_pixel_ratio=0.08,
            animations="disabled",
        )

    def test_main_content(self, page, hacker_news_page):
        hacker_news_page.open()
        hide_hacker_news_dynamic_content(page)
        expect(hacker_news_page.main_content).to_have_screenshot(
            "hn-main-content.png",
            max_diff_pixel_ratio=0.08,
            animations="disabled",
        )

    def test_header(self, hacker_news_page):
        hacker_news_page.open()
        expect(hacker_news_page.header).to_have_screenshot(
            "hn-header.png",
            max_diff_pixel_ratio=0.06,
            animations="disabled",
        )
