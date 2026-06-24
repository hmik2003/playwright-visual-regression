import pytest

from fixtures.test_data import VIEWPORTS
from utils.screenshot_helpers import assert_screenshot, hide_hacker_news_dynamic_content


@pytest.mark.ci
@pytest.mark.parametrize("label,viewport", list(VIEWPORTS.items()))
class TestResponsiveHackerNewsVisual:
    def test_hacker_news_at_viewport(
        self, page, hacker_news_page, label, viewport, request
    ):
        page.set_viewport_size(viewport)
        hacker_news_page.open()
        hide_hacker_news_dynamic_content(page)
        height = min(viewport["height"], 900)
        assert_screenshot(
            page,
            f"hn-responsive-{label}.png",
            request,
            full_page=False,
            clip={
                "x": 0,
                "y": 0,
                "width": viewport["width"],
                "height": height,
            },
            max_diff_pixel_ratio=0.08,
        )


@pytest.mark.live_site
@pytest.mark.parametrize("label,viewport", list(VIEWPORTS.items()))
class TestResponsiveBingVisual:
    def test_bing_at_viewport(self, page, bing_page, label, viewport, request):
        page.set_viewport_size(viewport)
        bing_page.open()
        bing_page.dismiss_cookie_banner()
        height = min(viewport["height"], 900)
        assert_screenshot(
            page,
            f"bing-responsive-{label}.png",
            request,
            full_page=False,
            clip={
                "x": 0,
                "y": 0,
                "width": viewport["width"],
                "height": height,
            },
            mask=[bing_page.search_box],
            max_diff_pixel_ratio=0.22,
        )
