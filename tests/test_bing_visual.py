import pytest

from utils.screenshot_helpers import assert_screenshot


@pytest.mark.live_site
class TestBingVisualRegression:
    @pytest.fixture(autouse=True)
    def setup(self, bing_page):
        bing_page.open()
        bing_page.dismiss_cookie_banner()

    def test_homepage_viewport_screenshot(self, page, bing_page, request):
        assert_screenshot(
            page,
            "bing-homepage.png",
            request,
            full_page=False,
            clip={"x": 0, "y": 0, "width": 1280, "height": 720},
            mask=[bing_page.search_box, bing_page.logo],
            max_diff_pixel_ratio=0.15,
        )

    def test_search_box_component_screenshot(self, bing_page, request):
        assert_screenshot(
            bing_page.search_box,
            "bing-search-box.png",
            request,
            max_diff_pixel_ratio=0.12,
            timeout=15_000,
        )

    def test_logo_screenshot(self, bing_page, request):
        assert_screenshot(
            bing_page.logo,
            "bing-logo.png",
            request,
            max_diff_pixel_ratio=0.08,
            timeout=15_000,
        )
