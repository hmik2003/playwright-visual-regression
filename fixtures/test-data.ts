export const VIEWPORTS = {
  desktop: { width: 1280, height: 720 },
  tablet: { width: 768, height: 1024 },
  mobile: { width: 390, height: 844 },
} as const;

export const SITES = {
  hackerNews: {
    url: 'https://news.ycombinator.com',
    name: 'Hacker News',
  },
  bing: {
    url: 'https://www.bing.com',
    name: 'Bing',
  },
} as const;

export const VISUAL_THRESHOLDS = {
  maxDiffPixelRatio: 0.02,
  fullPage: true,
} as const;
