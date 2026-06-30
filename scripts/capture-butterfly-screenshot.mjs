import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const previewPath = path.join(root, 'assets', 'clients', 'butterfly-beauty-preview.html');
const outPath = path.join(root, 'assets', 'clients', 'butterfly-beauty-screenshot.png');
const port = 8778;

const server = createServer(async (req, res) => {
  const url = req.url?.split('?')[0] ?? '/';
  if (url === '/' || url === '/preview') {
    const html = await readFile(previewPath, 'utf8');
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(html);
    return;
  }
  const clientFile = url.replace(/^\//, '');
  if (clientFile === 'butterfly-beauty-logo.png' || clientFile.startsWith('butterfly/')) {
    const filePath = path.join(root, 'assets', 'clients', clientFile);
    try {
      const data = await readFile(filePath);
      const ext = path.extname(filePath).toLowerCase();
      const type = ext === '.jpg' ? 'image/jpeg' : ext === '.png' ? 'image/png' : 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': type });
      res.end(data);
      return;
    } catch {
      res.writeHead(404);
      res.end();
      return;
    }
  }
  res.writeHead(404);
  res.end();
});

await new Promise((resolve) => server.listen(port, resolve));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

try {
  await page.goto(`http://127.0.0.1:${port}/preview`, { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForTimeout(2000);
  await page.screenshot({ path: outPath, type: 'png' });
  console.log(`Saved ${outPath}`);
} finally {
  await browser.close();
  server.close();
}
