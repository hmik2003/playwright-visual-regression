import pytest

from pages.bing_page import BingPage
from pages.hacker_news_page import HackerNewsPage


@pytest.fixture
def hacker_news_page(page):
    return HackerNewsPage(page)


@pytest.fixture
def bing_page(page):
    return BingPage(page)
