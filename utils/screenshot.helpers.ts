import { expect, Page, Locator } from '@playwright/test';

export interface ScreenshotOptions {
  fullPage?: boolean;
  mask?: Locator[];
  maxDiffPixelRatio?: number;
}

export async function hideDynamicElements(page: Page, selectors: string[]) {
  await page.evaluate((sels) => {
    sels.forEach((sel) => {
      document.querySelectorAll(sel).forEach((el) => {
        (el as HTMLElement).style.visibility = 'hidden';
      });
    });
  }, selectors);
}

export function getViewportLabel(width: number): string {
  if (width >= 1024) return 'desktop';
  if (width >= 768) return 'tablet';
  return 'mobile';
}

export async function assertVisualMatch(
  locator: Locator,
  snapshotName: string,
  maxDiffPixelRatio = 0.02,
) {
  await expect(locator).toHaveScreenshot(snapshotName, {
    maxDiffPixelRatio,
    animations: 'disabled',
  });
}
