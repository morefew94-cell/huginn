import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const assetsDir = path.join(root, 'assets', 'clients');
const port = 8777;

await mkdir(assetsDir, { recursive: true });

const browser = await chromium.launch();

async function captureSite(url, screenshotName, logoSelector) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
    await page.waitForTimeout(1500);
    await page.screenshot({
      path: path.join(assetsDir, screenshotName),
      type: 'png',
    });
    console.log(`Saved ${screenshotName}`);

    if (logoSelector) {
      const logo = page.locator(logoSelector).first();
      if (await logo.count()) {
        await logo.screenshot({ path: path.join(assetsDir, screenshotName.replace('-screenshot', '-logo')) });
        console.log(`Saved logo for ${screenshotName}`);
      }
    }
  } catch (error) {
    console.error(`Failed ${url}:`, error.message);
  } finally {
    await page.close();
  }
}

try {
  await captureSite('https://ibuildpm.com.au', 'ibuild-pm-screenshot.png', 'img[alt*="iBuild"], .logo img, header img');
  await captureSite('https://veridianims.com', 'veridian-ims-screenshot.png', 'img[alt*="Veridian"], header img, .logo img');

  const butterflyUrls = [
    'https://butterflybeauty.com.au',
    'https://www.butterflybeauty.com.au',
  ];
  for (const url of butterflyUrls) {
    try {
      const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
      await page.goto(url, { waitUntil: 'networkidle', timeout: 15000 });
      await page.waitForTimeout(1000);
      await page.screenshot({ path: path.join(assetsDir, 'butterfly-beauty-screenshot.png'), type: 'png' });
      console.log(`Saved butterfly-beauty-screenshot.png from ${url}`);
      await page.close();
      break;
    } catch {
      continue;
    }
  }
} finally {
  await browser.close();
}
