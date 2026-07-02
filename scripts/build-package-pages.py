#!/usr/bin/env python3
"""Generate package detail pages under packages/."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "packages"
OUT.mkdir(exist_ok=True)

NAV = (ROOT / "partials" / "nav-nested.html").read_text(encoding="utf-8")

FOOTER = """<footer>
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
<script src="../stripe-deposits.js"></script>
</body>
</html>"""

PACKAGE_NAV = """    <nav class="package-nav-links mono" aria-label="Build packages">
      <a href="starter.html"{starter_active}>Starter</a>
      <a href="growth.html"{growth_active}>Growth</a>
      <a href="pro.html"{pro_active}>Pro</a>
      <a href="extras.html"{extras_active}>Extras</a>
    </nav>"""


def shell(title, description, canonical_slug, body, active):
    nav_links = PACKAGE_NAV.format(
        starter_active=' class="active"' if active == "starter" else "",
        growth_active=' class="active"' if active == "growth" else "",
        pro_active=' class="active"' if active == "pro" else "",
        extras_active=' class="active"' if active == "extras" else "",
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow" />
  <meta name="theme-color" content="#08090c" />
  <meta name="google-site-verification" content="r3BlNP4yPdbvOc2dqCGIzokBrElt6f1NIe89Prdp2Hs" />
  <title>{title} | Huginn</title>
  <link rel="canonical" href="https://www.huginnweb.com/packages/{canonical_slug}" />
  <link rel="icon" href="../favicon.ico" sizes="any" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../subpage.css" />
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-24NZY2REEW"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-24NZY2REEW');
  </script>
</head>
<body>

<div class="bg-glow" aria-hidden="true"></div>
<div class="grain" aria-hidden="true"></div>

{NAV}

<main>
  <div class="wrap">
    <p class="breadcrumb"><a href="../index.html">Home</a> / <a href="../index.html#packages">Packages</a> / {title.split(' | ')[0] if ' | ' in title else title.replace(' | Huginn', '')}</p>

{nav_links}

{body}
  </div>
</main>

{FOOTER}"""


STARTER = shell(
    "Starter · Tier 1 Website Package",
    "Starter tier 1 website package — up to 5 pages, mobile-first design, lead capture, SEO setup, domain and going live included. $499 · $25 deposit (5%).",
    "starter",
    """    <div class="page-hero">
      <span class="mono label">Build package · Tier 1 · USD</span>
      <h1>Starter — get found, get contacted</h1>
      <p class="lead">A solid foundation for businesses ready to be discovered online. Up to 5 pages, mobile-first design, enquiry capture, and search setup — domain registration and going live included.</p>
    </div>

    <div class="package-price-banner">
      <span class="price-main">$499</span>
      <span class="price-deposit">· $25 deposit (5%)</span>
      <p class="price-note">Balance due before launch · domain (1st year) and hosting setup included · you own the site outright</p>
    </div>

    <p>Best for local service businesses, studios, trades, and professionals who need a credible online presence without complex integrations. Typical timeline: <strong>~20 business days</strong> (Starter tier — builds overall run ~20-30 business days depending on package).</p>

    <div class="scope-grid">
      <div class="scope-card included">
        <h3>What's included</h3>
        <ul class="scope-list">
          <li>Up to 5 pages (e.g. home, services, about, contact, one extra)</li>
          <li>Mobile-first responsive design</li>
          <li>Lead capture / contact forms wired to your inbox</li>
          <li>Google Search Console setup and on-page local SEO</li>
          <li>Domain registration — first year included</li>
          <li>Hosting setup and going live on the internet</li>
          <li>Hosted through Huginn or self-host handover at launch</li>
          <li>10 business days working draft, then 10 days unlimited revisions</li>
          <li>You own the site outright once paid in full</li>
        </ul>
      </div>
      <div class="scope-card not-included">
        <h3>What's not included</h3>
        <ul class="scope-list">
          <li>Pages beyond the 5-page allowance (available as an extra)</li>
          <li>Custom CMS or blog you can update yourself</li>
          <li>Booking, quote, or multi-step signup flows</li>
          <li>E-commerce, member portals, or customer logins</li>
          <li>Logo design, brand kit, or professional copywriting (extras)</li>
          <li>Google Analytics setup — that's your responsibility if wanted</li>
          <li>Ongoing updates after final sign-off (care plan or $99 change window)</li>
          <li>Domain renewal after year one (you renew directly or via care plan)</li>
        </ul>
      </div>
    </div>

    <h2>Good fit if you…</h2>
    <ul>
      <li>Need a professional site live quickly without a large upfront budget</li>
      <li>Want enquiries via contact form rather than online booking or checkout</li>
      <li>Are happy with a focused 5-page structure to start</li>
    </ul>

    <div class="btn-row">
      <a class="btn-primary" href="/api/checkout?tier=starter" data-stripe-deposit="starter">Reserve my build</a>
      <a class="btn-ghost" href="../case-studies/butterfly-beauty.html">See Starter example</a>
    </div>

    <div class="related">
      <h2>Compare packages</h2>
      <ul>
        <li><a href="growth.html">Growth — custom design &amp; CMS ($2,999)</a></li>
        <li><a href="pro.html">Pro — bespoke Next.js platform ($9,999)</a></li>
        <li><a href="extras.html">Extras &amp; add-ons</a></li>
      </ul>
    </div>""",
    "starter",
)

GROWTH = shell(
    "Growth Website Package",
    "Growth website package — $2,999 custom design, CMS, booking and signup flows, SEO and structured data. $150 deposit. Everything in Starter included.",
    "growth",
    """    <div class="page-hero">
      <span class="mono label">Build package · Most chosen · USD</span>
      <h1>Growth — built to convert</h1>
      <p class="lead">Custom design and flows that turn visitors into leads. No templates — a site shaped around your business with a content system you can update and conversion paths built in.</p>
    </div>

    <div class="package-price-banner">
      <span class="price-main">$2,999</span>
      <span class="price-deposit">· $150 deposit (5%)</span>
      <p class="price-note">Balance due before launch · domain, hosting setup, and going live included · you own the site outright</p>
    </div>

    <p>Best for established service businesses, professional firms, and growing brands that need custom design, a blog or CMS, and structured lead flows. Typical timeline: <strong>~20-25 business days</strong> — confirmed in your site plan before design starts.</p>

    <div class="scope-grid">
      <div class="scope-card included">
        <h3>What's included</h3>
        <ul class="scope-list">
          <li>Everything in Starter</li>
          <li>Custom design — no off-the-shelf templates</li>
          <li>Blog or content management system you can update</li>
          <li>Booking, quote request, or signup flows</li>
          <li>SEO optimisation and structured data (schema markup)</li>
          <li>Expanded page structure scoped in your site plan</li>
          <li>Domain registration, hosting setup, and launch</li>
          <li>Revision rounds as defined in your site plan</li>
        </ul>
      </div>
      <div class="scope-card not-included">
        <h3>What's not included</h3>
        <ul class="scope-list">
          <li>Bespoke Next.js application builds (see Pro)</li>
          <li>Customer or member portals with logins</li>
          <li>Full e-commerce catalogues, subscriptions, or complex payment flows</li>
          <li>Deep CRM, ERP, or custom API integrations</li>
          <li>Logo, brand kit, or copywriting unless added as extras</li>
          <li>Google Analytics setup</li>
          <li>Ongoing content updates after launch (care plan or $99 change window)</li>
          <li>Unlimited pages — scope is agreed upfront in the site plan</li>
        </ul>
      </div>
    </div>

    <h2>Good fit if you…</h2>
    <ul>
      <li>Outgrew a template or DIY site and need a distinctive brand presence</li>
      <li>Want to publish content and capture leads through structured flows</li>
      <li>Need more than 5 pages but not a full custom platform</li>
    </ul>

    <div class="btn-row">
      <a class="btn-primary" href="/api/checkout?tier=growth" data-stripe-deposit="growth">Reserve my build</a>
      <a class="btn-ghost" href="starter.html">Compare Starter</a>
    </div>

    <div class="related">
      <h2>Compare packages</h2>
      <ul>
        <li><a href="starter.html">Starter — tier 1 foundation ($499)</a></li>
        <li><a href="pro.html">Pro — bespoke Next.js platform ($9,999)</a></li>
        <li><a href="extras.html">Extras &amp; add-ons</a></li>
      </ul>
    </div>""",
    "growth",
)

PRO = shell(
    "Pro Website Package",
    "Pro website package — $9,999 bespoke Next.js build with portals, payments, CRM and SaaS integrations. $500 deposit. Everything in Growth included.",
    "pro",
    """    <div class="page-hero">
      <span class="mono label">Build package · Bespoke · USD</span>
      <h1>Pro — custom-built platform</h1>
      <p class="lead">For e-commerce, SaaS, membership sites, and businesses that need more than a marketing site — bespoke Next.js builds with portals, payments, and integrations.</p>
    </div>

    <div class="package-price-banner">
      <span class="price-main">$9,999</span>
      <span class="price-deposit">· $500 deposit (5%)</span>
      <p class="price-note">Balance due before launch · domain, hosting setup, and going live included · you own the site outright</p>
    </div>

    <p>Best for SaaS products, e-commerce brands, membership businesses, and industrial or professional services that need authenticated areas, databases, or third-party integrations. Typical timeline: <strong>~25-30 business days</strong> — scope and schedule defined in a detailed site plan before build starts.</p>

    <div class="scope-grid">
      <div class="scope-card included">
        <h3>What's included</h3>
        <ul class="scope-list">
          <li>Everything in Growth</li>
          <li>Bespoke build on Next.js</li>
          <li>Customer, member, or staff portals with authentication</li>
          <li>Payment processing (e.g. Stripe) where scoped</li>
          <li>CRM, SaaS, and third-party API integrations as agreed</li>
          <li>E-commerce, SaaS, or membership-ready architecture</li>
          <li>Database-backed features (job boards, dashboards, registers)</li>
          <li>Domain, hosting setup, launch, and handover documentation</li>
        </ul>
      </div>
      <div class="scope-card not-included">
        <h3>What's not included</h3>
        <ul class="scope-list">
          <li>Native iOS or Android apps</li>
          <li>Unlimited integrations or scope beyond the signed site plan</li>
          <li>Ongoing feature development after launch (care plan or change window)</li>
          <li>Third-party subscription fees (Stripe, hosting tiers, SaaS tools)</li>
          <li>Logo, brand, or copy unless added as extras</li>
          <li>Google Analytics setup</li>
          <li>Legal, compliance, or industry certification consulting</li>
          <li>24/7 support — post-launch support via care plans</li>
        </ul>
      </div>
    </div>

    <h2>Good fit if you…</h2>
    <ul>
      <li>Need logged-in areas, dashboards, or database-driven content</li>
      <li>Sell online, run subscriptions, or offer SaaS trials</li>
      <li>Require integrations with payments, CRM, or internal tools</li>
    </ul>

    <div class="btn-row">
      <a class="btn-primary" href="/api/checkout?tier=pro" data-stripe-deposit="pro">Reserve my build</a>
      <a class="btn-ghost" href="../case-studies/veridian-ims.html">See Pro example</a>
    </div>

    <div class="related">
      <h2>Compare packages</h2>
      <ul>
        <li><a href="starter.html">Starter — tier 1 foundation</a></li>
        <li><a href="growth.html">Growth — custom design &amp; CMS</a></li>
        <li><a href="extras.html">Extras &amp; add-ons</a></li>
        <li><a href="../case-studies/ibuild-pm.html">Case study: iBuild PM</a></li>
        <li><a href="../case-studies/veridian-ims.html">Case study: Veridian IMS</a></li>
      </ul>
    </div>""",
    "pro",
)

EXTRAS = shell(
    "Website Extras & Add-ons",
    "Optional website extras — logo design, brand kit, copywriting, extra pages, stock photography, business email, Google Business Profile, and booking integrations. Added to your build invoice.",
    "extras",
    """    <div class="page-hero">
      <span class="mono label">Add-ons · USD · Any package</span>
      <h1>Extras for your build</h1>
      <p class="lead">Optional add-ons bolted onto Starter, Growth, or Pro — quoted upfront and added to your build invoice. Reserve your package first; extras and balance are invoiced before work starts.</p>
    </div>

    <p>Extras are not separate checkout items. Tell us what you need via the <a href="../index.html#contact">contact form</a> or when you reserve your build — we'll include them in your quote before design starts.</p>

    <div class="extra-detail" id="logo">
      <h3>Logo design</h3>
      <p class="extra-price-tag">From $99</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>Included</h3>
          <ul class="scope-list">
            <li>Three initial concepts</li>
            <li>Two revision rounds</li>
            <li>Final vector files (SVG, PNG) for web and print</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Not included</h3>
          <ul class="scope-list">
            <li>Full brand strategy workshop</li>
            <li>Trademark or legal clearance</li>
            <li>Print stationery or signage design</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="extra-detail" id="brand-kit">
      <h3>Brand kit</h3>
      <p class="extra-price-tag">From $599</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>Included</h3>
          <ul class="scope-list">
            <li>Logo (or refinement of your existing mark)</li>
            <li>Colour palette and typography guidelines</li>
            <li>Social profile assets</li>
            <li>Consistent look for site and channels</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Not included</h3>
          <ul class="scope-list">
            <li>Print collateral (business cards, brochures)</li>
            <li>Brand naming or tagline development</li>
            <li>Ongoing brand management</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="extra-detail" id="copywriting">
      <h3>Copywriting</h3>
      <p class="extra-price-tag">From $99 / page</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>Included</h3>
          <ul class="scope-list">
            <li>Professional web copy per page scoped</li>
            <li>Homepage, services, about, and key landing pages</li>
            <li>One revision round per page</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Not included</h3>
          <ul class="scope-list">
            <li>Blog posts or ongoing content marketing</li>
            <li>SEO keyword research reports</li>
            <li>Legal, medical, or compliance-reviewed copy</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="extra-detail" id="extra-pages">
      <h3>Extra pages</h3>
      <p class="extra-price-tag">From $199 / page</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>Included</h3>
          <ul class="scope-list">
            <li>Additional pages beyond your package allowance</li>
            <li>Service areas, team bios, FAQs, or landing pages</li>
            <li>Design and build consistent with your site</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Not included</h3>
          <ul class="scope-list">
            <li>Complex interactive features per page</li>
            <li>Copywriting unless added separately</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="extra-detail" id="stock-photos">
      <h3>Stock photography</h3>
      <p class="extra-price-tag">From $149</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>Included</h3>
          <ul class="scope-list">
            <li>Licensed stock imagery curated for your brand</li>
            <li>Basic editing to match your site aesthetic</li>
            <li>No generic placeholder photos</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Not included</h3>
          <ul class="scope-list">
            <li>On-location or custom photo shoots</li>
            <li>Exclusive image buyouts beyond standard licence</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="extra-detail" id="business-email">
      <h3>Business email</h3>
      <p class="extra-price-tag">From $99</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>Included</h3>
          <ul class="scope-list">
            <li>Professional addresses on your domain (e.g. hello@yourbusiness.com)</li>
            <li>Setup and configuration</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Not included</h3>
          <ul class="scope-list">
            <li>Ongoing mailbox hosting fees (paid to your provider)</li>
            <li>Email migration from legacy systems at scale</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="extra-detail" id="google-business">
      <h3>Google Business Profile</h3>
      <p class="extra-price-tag">From $149</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>Included</h3>
          <ul class="scope-list">
            <li>Listing setup and verification support</li>
            <li>Local profile optimisation for Maps search</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Not included</h3>
          <ul class="scope-list">
            <li>Ongoing review management or posting</li>
            <li>Paid Google Ads campaigns</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="extra-detail" id="booking">
      <h3>Booking integration</h3>
      <p class="extra-price-tag">From $249</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>Included</h3>
          <ul class="scope-list">
            <li>Connect Calendly, Acuity, or similar</li>
            <li>Embedded booking flows on contact and service pages</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Not included</h3>
          <ul class="scope-list">
            <li>Subscription fees for the booking tool</li>
            <li>Custom-built scheduling from scratch (see Growth/Pro flows)</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="extra-detail" id="custom">
      <h3>Custom request</h3>
      <p class="extra-price-tag">Quote</p>
      <p>Photography direction, illustrations, multilingual pages, or something else — tell us what you need and we'll price it before adding to your invoice.</p>
    </div>

    <div class="btn-row">
      <a class="btn-primary" href="../index.html#contact">Request a quote</a>
      <a class="btn-ghost" href="../index.html#packages">View build packages</a>
    </div>

    <div class="related">
      <h2>Build packages</h2>
      <ul>
        <li><a href="starter.html">Starter · Tier 1</a></li>
        <li><a href="growth.html">Growth</a></li>
        <li><a href="pro.html">Pro</a></li>
      </ul>
    </div>""",
    "extras",
)

PAGES = {
    "starter.html": STARTER,
    "growth.html": GROWTH,
    "pro.html": PRO,
    "extras.html": EXTRAS,
}

if __name__ == "__main__":
    if not (ROOT / "partials" / "nav-nested.html").exists():
        raise SystemExit("Run scripts/render-nav.py first")
    for name, html in PAGES.items():
        path = OUT / name
        path.write_text(html, encoding="utf-8")
        print("wrote", path)
