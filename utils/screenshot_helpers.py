import io
from pathlib import Path
from typing import Union

import pytest
from playwright.sync_api import Locator, Page

try:
    from PIL import Image

    _HAS_PIL = True
except ImportError:
    _HAS_PIL = False


HN_DYNAMIC_SELECTORS = [
    ".comhead a",
    ".age",
    ".score",
    ".titleline",
    ".subtext",
    ".rank",
]


def hide_dynamic_elements(page: Page, selectors: list[str]) -> None:
    page.evaluate(
        """(sels) => {
            sels.forEach((sel) => {
                document.querySelectorAll(sel).forEach((el) => {
                    el.style.visibility = 'hidden';
                });
            });
        }""",
        selectors,
    )


def hide_hacker_news_dynamic_content(page: Page) -> None:
    hide_dynamic_elements(page, HN_DYNAMIC_SELECTORS)


def get_viewport_label(width: int) -> str:
    if width >= 1024:
        return "desktop"
    if width >= 768:
        return "tablet"
    return "mobile"


def _images_match(
    expected_bytes: bytes,
    actual_bytes: bytes,
    max_diff_pixel_ratio: float,
) -> tuple[bool, float]:
    if expected_bytes == actual_bytes:
        return True, 0.0

    if not _HAS_PIL:
        return False, 1.0

    expected = Image.open(io.BytesIO(expected_bytes)).convert("RGB")
    actual = Image.open(io.BytesIO(actual_bytes)).convert("RGB")
    if expected.size != actual.size:
        actual = actual.resize(expected.size)
    diff_pixels = 0
    total = expected.size[0] * expected.size[1]
    exp_data = expected.load()
    act_data = actual.load()
    for y in range(expected.size[1]):
        for x in range(expected.size[0]):
            if exp_data[x, y] != act_data[x, y]:
                diff_pixels += 1
    ratio = diff_pixels / total if total else 0
    return ratio <= max_diff_pixel_ratio, ratio


def assert_screenshot(
    target: Union[Page, Locator],
    name: str,
    request: pytest.FixtureRequest,
    *,
    max_diff_pixel_ratio: float = 0.05,
    **screenshot_kwargs,
) -> None:
    test_path = Path(str(request.node.fspath))
    snapshot_dir = test_path.parent / f"{test_path.stem}-snapshots"
    snapshot_path = snapshot_dir / name
    update = request.config.getoption("--update-snapshots", default=False)

    screenshot_kwargs.setdefault("animations", "disabled")
    actual = target.screenshot(**screenshot_kwargs)

    if update or not snapshot_path.exists():
        snapshot_dir.mkdir(parents=True, exist_ok=True)
        snapshot_path.write_bytes(actual)
        return

    expected = snapshot_path.read_bytes()
    matched, ratio = _images_match(expected, actual, max_diff_pixel_ratio)
    if not matched:
        diff_path = snapshot_dir / name.replace(".png", "-actual.png")
        diff_path.write_bytes(actual)
        pytest.fail(
            f"Screenshot '{name}' mismatch: diff pixel ratio {ratio:.4f} "
            f"exceeds threshold {max_diff_pixel_ratio}. Actual saved to {diff_path}"
        )
