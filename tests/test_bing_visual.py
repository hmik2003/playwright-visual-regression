import pytest
from playwright.sync_api import Page, expect


@pytest.mark.live_site
class TestBingVisualRegression:
    @pytest.fixture(autouse=True)
    def setup(self, bing_page):
        bing_page.open()
        bing_page.dismiss_cookie_banner()

    def test_homepage_viewport_screenshot(self, page: Page, bing_page):
        expect(page).to_have_screenshot(
            "bing-homepage.png",
            full_page=False,
            clip={"x": 0, "y": 0, "width": 1280, "height": 720},
            mask=[bing_page.search_box, bing_page.logo],
            max_diff_pixel_ratio=0.15,
            animations="disabled",
        )

    def test_search_box_component_screenshot(self, bing_page):
        expect(bing_page.search_box).to_have_screenshot(
            "bing-search-box.png",
            max_diff_pixel_ratio=0.12,
            animations="disabled",
            timeout=15_000,
        )

    def test_logo_screenshot(self, bing_page):
        expect(bing_page.logo).to_have_screenshot(
            "bing-logo.png",
            max_diff_pixel_ratio=0.08,
            animations="disabled",
            timeout=15_000,
        )
