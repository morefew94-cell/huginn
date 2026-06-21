#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FONT_LINK = (
    '  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700'
    '&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400'
    '&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />'
)

OLD_FONT = (
    '  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700'
    '&family=DM+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />'
)

OLD_HEADER = """<header>
  <div class="wrap-wide nav">
    <a class="brand" href="../index.html" aria-label="Huginn home"><img src="../huginn-logo.png" alt="Huginn" /></a>
    <a class="nav-cta" href="../index.html#contact">Request a site plan</a>
  </div>
</header>"""

BLOG_HEADER = """<div class="bg-glow" aria-hidden="true"></div>
<div class="grain" aria-hidden="true"></div>

<header>
  <div class="wrap-wide">
    <div class="nav">
      <a class="brand" href="../index.html" aria-label="Huginn home">
        <img src="../huginn-logo.png" alt="Huginn — web design and development" />
      </a>
      <nav class="nav-links" aria-label="Primary">
        <a href="../index.html#work">Work</a>
        <a href="../index.html#packages">Build packages</a>
        <a href="../index.html#care">Care plans</a>
        <a href="../index.html#process">Process</a>
        <a href="index.html">Blog</a>
      </nav>
      <a class="nav-cta" href="../index.html#contact">Request a site plan</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-nav">Menu</button>
    </div>
    <nav id="mobile-nav" class="mobile-nav" aria-label="Mobile">
      <a href="../index.html#work">Work</a>
      <a href="../index.html#packages">Build packages</a>
      <a href="../index.html#care">Care plans</a>
      <a href="../index.html#process">Process</a>
      <a href="index.html">Blog</a>
      <a href="../index.html#contact">Request a site plan</a>
    </nav>
  </div>
</header>"""

CASE_HEADER = BLOG_HEADER.replace('href="index.html">Blog', 'href="../blog/index.html">Blog')

OLD_FOOTER = """<footer>
  <div class="wrap"><p class="mono">Huginn — web design &amp; development, sharpened. · <a href="../privacy.html">Privacy</a></p></div>
</footer>

</body>"""

NEW_FOOTER = """<footer>
  <div class="wrap-wide">
    <div class="brand-footer">
      <img src="../huginn-logo.png" alt="Huginn" />
    </div>
    <p class="mono">Web design &amp; development, sharpened.</p>
    <p class="mono footer-links">
      <a href="../web-design-australia.html">Australia</a> ·
      <a href="../web-development-usa.html">USA</a> ·
      <a href="../saas-website-design.html">SaaS</a> ·
      <a href="../blog/index.html">Blog</a> ·
      <a href="../privacy.html">Privacy</a> ·
      <a href="../index.html#faq">FAQ</a>
    </p>
  </div>
</footer>

<script src="../site-nav.js"></script>
</body>"""


def patch_file(path: Path, header: str) -> None:
    text = path.read_text()
    if OLD_FONT in text:
        text = text.replace(OLD_FONT, FONT_LINK)
    if 'name="theme-color"' not in text:
        text = text.replace(
            '<meta name="robots" content="index, follow" />',
            '<meta name="robots" content="index, follow" />\n  <meta name="theme-color" content="#08090c" />',
            1,
        )
    if '../subpage.css' not in text:
        text = text.replace(FONT_LINK, FONT_LINK + '\n  <link rel="stylesheet" href="../subpage.css" />')
    if 'application/ld+json' in text and '\n  </script>\n  <!-- Google tag' not in text:
        text = text.replace('\n  <!-- Google tag (gtag.js) -->', '\n  </script>\n  <!-- Google tag (gtag.js) -->', 1)
    if OLD_HEADER in text:
        text = text.replace('<body>\n\n' + OLD_HEADER, '<body>\n\n' + header)
    text = text.replace('<h2 class="mono" style="color:var(--accent);">Related</h2>', '<h2>Related</h2>')
    text = text.replace(OLD_FOOTER, NEW_FOOTER)
    path.write_text(text)
    print(f'Updated {path.relative_to(ROOT)}')


for blog_file in sorted((ROOT / 'blog').glob('*.html')):
    if blog_file.name == 'index.html':
        continue
    patch_file(blog_file, BLOG_HEADER)

for case_file in sorted((ROOT / 'case-studies').glob('*.html')):
    patch_file(case_file, CASE_HEADER)
