SITES = {
    "hacker_news": {"url": "https://news.ycombinator.com", "name": "Hacker News"},
    "bing": {"url": "https://www.bing.com", "name": "Bing"},
}

VIEWPORTS = {
    "desktop": {"width": 1280, "height": 720},
    "tablet": {"width": 768, "height": 1024},
    "mobile": {"width": 390, "height": 844},
}

HN_DYNAMIC_SELECTORS = [
    ".comhead a",
    ".age",
    ".score",
    ".titleline",
    ".subtext",
    ".rank",
]
