import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const outDir = path.join(root, 'promo-screenshots');
const port = 8766;

const mime = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
};

const server = createServer(async (req, res) => {
  const urlPath = decodeURIComponent((req.url || '/').split('?')[0]);
  const filePath = path.join(root, urlPath === '/' ? 'index.html' : urlPath.replace(/^\//, ''));

  try {
    const data = await readFile(filePath);
    const ext = path.extname(filePath);
    res.writeHead(200, { 'Content-Type': mime[ext] || 'application/octet-stream' });
    res.end(data);
  } catch {
    res.writeHead(404).end('Not found');
  }
});

async function preparePage(page) {
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => {
    document.querySelectorAll('.reveal').forEach((el) => el.classList.add('visible'));
    document.querySelector('.promo-modal')?.remove();
    document.body.classList.remove('promo-open');
  });
  await page.waitForTimeout(400);
}

await mkdir(outDir, { recursive: true });
await new Promise((resolve) => server.listen(port, resolve));

const browser = await chromium.launch();
const viewport = { width: 1440, height: 900 };
const base = `http://127.0.0.1:${port}`;

const noPopupContext = await browser.newContext({ viewport });
await noPopupContext.addInitScript(() => {
  sessionStorage.setItem('huginn-promo-seen', '1');
});

const page = await noPopupContext.newPage();

try {
  await page.goto(`${base}/index.html`, { waitUntil: 'networkidle' });
  await preparePage(page);

  await page.screenshot({
    path: path.join(outDir, '01-homepage-hero.png'),
    clip: { x: 0, y: 0, width: 1440, height: 900 },
  });

  await page.locator('section.hero').screenshot({
    path: path.join(outDir, '02-hero-section.png'),
  });

  await page.locator('#packages').screenshot({
    path: path.join(outDir, '03-build-packages.png'),
  });

  await page.locator('#care').screenshot({
    path: path.join(outDir, '04-care-plans.png'),
  });

  await page.locator('#work').screenshot({
    path: path.join(outDir, '05-case-studies.png'),
  });

  await page.locator('#contact').screenshot({
    path: path.join(outDir, '06-contact-form.png'),
  });

  await page.goto(`${base}/blog/index.html`, { waitUntil: 'networkidle' });
  await preparePage(page);
  await page.screenshot({
    path: path.join(outDir, '08-blog.png'),
    fullPage: true,
  });

  const popupPage = await browser.newPage({ viewport });
  await popupPage.goto(`${base}/index.html`, { waitUntil: 'networkidle' });
  await popupPage.evaluate(() => document.fonts.ready);
  await popupPage.evaluate(() => {
    document.querySelectorAll('.reveal').forEach((el) => el.classList.add('visible'));
  });
  await popupPage.waitForSelector('.promo-modal.open', { timeout: 5000 });
  await popupPage.waitForTimeout(300);
  await popupPage.screenshot({
    path: path.join(outDir, '07-limited-offer-popup.png'),
  });
  await popupPage.close();

  console.log(`Saved 8 screenshots to ${outDir}`);
} finally {
  await noPopupContext.close();
  await browser.close();
  server.close();
}
