import pytest

from pages.bing_page import BingPage
from pages.hacker_news_page import HackerNewsPage


def pytest_addoption(parser):
    parser.addoption(
        "--update-snapshots",
        action="store_true",
        default=False,
        help="Update visual snapshot baselines",
    )


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture
def hacker_news_page(page):
    return HackerNewsPage(page)


@pytest.fixture
def bing_page(page):
    return BingPage(page)
