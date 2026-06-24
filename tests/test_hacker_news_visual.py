import pytest

from utils.screenshot_helpers import assert_screenshot, hide_hacker_news_dynamic_content


@pytest.mark.ci
class TestHackerNewsVisual:
    def test_homepage_layout(self, page, hacker_news_page, request):
        hacker_news_page.open()
        hide_hacker_news_dynamic_content(page)
        assert_screenshot(
            page,
            "hn-homepage.png",
            request,
            full_page=False,
            clip={"x": 0, "y": 0, "width": 1280, "height": 720},
            max_diff_pixel_ratio=0.08,
        )

    def test_main_content(self, page, hacker_news_page, request):
        hacker_news_page.open()
        hide_hacker_news_dynamic_content(page)
        assert_screenshot(
            hacker_news_page.main_content,
            "hn-main-content.png",
            request,
            max_diff_pixel_ratio=0.08,
        )

    def test_header(self, hacker_news_page, request):
        hacker_news_page.open()
        assert_screenshot(
            hacker_news_page.header,
            "hn-header.png",
            request,
            max_diff_pixel_ratio=0.06,
        )
