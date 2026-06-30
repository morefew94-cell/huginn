import { chromium } from 'playwright';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const assetsDir = path.join(path.resolve(__dirname, '..'), 'assets', 'clients');

async function dismissOverlays(page) {
  const closeSelectors = [
    '[aria-label="Close"]',
    '[aria-label="Close modal"]',
    'button.close',
    '.modal-close',
    '[data-dismiss="modal"]',
    'button:has-text("×")',
    'button:has-text("Close")',
  ];

  for (const selector of closeSelectors) {
    const btn = page.locator(selector).first();
    if (await btn.count()) {
      try {
        await btn.click({ timeout: 2000 });
        await page.waitForTimeout(500);
        break;
      } catch {
        // try next selector
      }
    }
  }

  await page.evaluate(() => {
    const selectors = [
      '[role="dialog"]',
      '[aria-modal="true"]',
      '.modal',
      '.popup',
      '[class*="Modal"]',
      '[class*="modal"]',
      '[class*="popup"]',
      '[class*="overlay"]',
    ];
    selectors.forEach((sel) => {
      document.querySelectorAll(sel).forEach((el) => el.remove());
    });
    document.body.classList.remove('modal-open', 'overflow-hidden', 'no-scroll');
    document.body.style.overflow = '';
    document.documentElement.style.overflow = '';
  });
}

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

try {
  await page.goto('https://veridianims.com', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2500);
  await dismissOverlays(page);
  await page.waitForTimeout(800);
  await page.screenshot({
    path: path.join(assetsDir, 'veridian-ims-screenshot.png'),
    type: 'png',
  });
  console.log('Saved veridian-ims-screenshot.png');
} catch (error) {
  console.error('Capture failed:', error.message);
  process.exitCode = 1;
} finally {
  await browser.close();
}
