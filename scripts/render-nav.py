#!/usr/bin/env python3
"""Generate site header nav HTML for home, root, and nested page depths."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def nav_html(base: str, wide: bool = True) -> str:
    """base: '' for homepage, '../' for blog/ and case-studies/."""
    is_home = base == "" and not wide
    ix = "" if is_home else f"{base}index.html"
    hash_ = (lambda frag: f"#{frag}") if is_home else (lambda frag: f"{ix}#{frag}")
    cs = f"{base}case-studies"
    blog = f"{base}blog"
    wrap = "wrap-wide" if wide else "wrap"

    desktop = f"""      <nav class="nav-links" aria-label="Primary">
        <div class="nav-dropdown">
          <button type="button" class="nav-dropdown-trigger" aria-expanded="false" aria-haspopup="true">Work</button>
          <div class="nav-dropdown-menu" role="menu">
            <span class="nav-dropdown-label mono">Case studies</span>
            <a href="{cs}/butterfly-beauty.html" role="menuitem"><strong>Butterfly Beauty</strong><span class="nav-dropdown-desc">Starter tier · beauty &amp; wellness website</span></a>
            <a href="{cs}/ibuild-pm.html" role="menuitem"><strong>iBuild PM</strong><span class="nav-dropdown-desc">Pro · industrial services &amp; portals</span></a>
            <a href="{cs}/veridian-ims.html" role="menuitem"><strong>Veridian IMS</strong><span class="nav-dropdown-desc">Pro · SaaS product &amp; Stripe checkout</span></a>
            <div class="nav-dropdown-divider"></div>
            <a href="{hash_('work')}" role="menuitem"><strong>View all work</strong><span class="nav-dropdown-desc">Portfolio &amp; client screenshots</span></a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button type="button" class="nav-dropdown-trigger" aria-expanded="false" aria-haspopup="true">Packages</button>
          <div class="nav-dropdown-menu" role="menu">
            <span class="nav-dropdown-label mono">Build packages</span>
            <a href="{hash_('plan-starter')}" role="menuitem"><strong>Starter · Tier 1</strong><span class="nav-dropdown-desc">From $20 deposit · up to 5 pages · domain included</span></a>
            <a href="{hash_('plan-growth')}" role="menuitem"><strong>Growth</strong><span class="nav-dropdown-desc">$2,999 · custom design, CMS &amp; lead flows</span></a>
            <a href="{hash_('plan-pro')}" role="menuitem"><strong>Pro</strong><span class="nav-dropdown-desc">$9,999 · Next.js, portals &amp; integrations</span></a>
            <div class="nav-dropdown-divider"></div>
            <a href="{hash_('extras')}" role="menuitem"><strong>Extras &amp; add-ons</strong><span class="nav-dropdown-desc">Logo design, copywriting, SEO setup &amp; more</span></a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button type="button" class="nav-dropdown-trigger" aria-expanded="false" aria-haspopup="true">Services</button>
          <div class="nav-dropdown-menu" role="menu">
            <span class="nav-dropdown-label mono">By market &amp; industry</span>
            <a href="{base}web-design-australia.html" role="menuitem"><strong>Web design Australia</strong><span class="nav-dropdown-desc">Custom sites for Australian businesses · AUD pricing</span></a>
            <a href="{base}web-development-usa.html" role="menuitem"><strong>Web development USA</strong><span class="nav-dropdown-desc">Marketing sites &amp; web apps for US clients</span></a>
            <a href="{base}saas-website-design.html" role="menuitem"><strong>SaaS website design</strong><span class="nav-dropdown-desc">Product sites, pricing pages &amp; trial signup</span></a>
            <div class="nav-dropdown-divider"></div>
            <a href="{hash_('care')}" role="menuitem"><strong>Website care plans</strong><span class="nav-dropdown-desc">Hosting, updates &amp; ongoing support</span></a>
            <a href="{hash_('process')}" role="menuitem"><strong>Our process</strong><span class="nav-dropdown-desc">Survey, plan, build &amp; handover</span></a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button type="button" class="nav-dropdown-trigger" aria-expanded="false" aria-haspopup="true">Resources</button>
          <div class="nav-dropdown-menu" role="menu">
            <span class="nav-dropdown-label mono">Guides &amp; blog</span>
            <a href="{blog}/index.html" role="menuitem"><strong>Blog</strong><span class="nav-dropdown-desc">Website cost, care plans &amp; SaaS tips</span></a>
            <a href="{blog}/website-cost-australia.html" role="menuitem"><strong>Website cost in Australia</strong><span class="nav-dropdown-desc">What to budget for a custom site</span></a>
            <a href="{blog}/care-plan-vs-diy.html" role="menuitem"><strong>Care plan vs DIY</strong><span class="nav-dropdown-desc">When to pay for hosting &amp; updates</span></a>
            <a href="{blog}/saas-landing-page-checklist.html" role="menuitem"><strong>SaaS landing page checklist</strong><span class="nav-dropdown-desc">Convert trials into revenue</span></a>
            <div class="nav-dropdown-divider"></div>
            <a href="{hash_('faq')}" role="menuitem"><strong>FAQ</strong><span class="nav-dropdown-desc">Pricing, deposits, ownership &amp; timelines</span></a>
          </div>
        </div>
        <a class="nav-link-direct" href="{hash_('contact')}">Contact</a>
      </nav>"""

    mobile = f"""    <nav id="mobile-nav" class="mobile-nav" aria-label="Mobile">
      <details class="mobile-nav-group">
        <summary>Work</summary>
        <a href="{cs}/butterfly-beauty.html"><strong>Butterfly Beauty</strong><span class="nav-dropdown-desc">Starter tier case study</span></a>
        <a href="{cs}/ibuild-pm.html"><strong>iBuild PM</strong><span class="nav-dropdown-desc">Industrial services case study</span></a>
        <a href="{cs}/veridian-ims.html"><strong>Veridian IMS</strong><span class="nav-dropdown-desc">SaaS product case study</span></a>
        <a href="{hash_('work')}"><strong>View all work</strong></a>
      </details>
      <details class="mobile-nav-group">
        <summary>Packages</summary>
        <a href="{hash_('plan-starter')}"><strong>Starter · Tier 1</strong><span class="nav-dropdown-desc">From $20 deposit</span></a>
        <a href="{hash_('plan-growth')}"><strong>Growth</strong><span class="nav-dropdown-desc">$2,999 custom design</span></a>
        <a href="{hash_('plan-pro')}"><strong>Pro</strong><span class="nav-dropdown-desc">$9,999 bespoke build</span></a>
        <a href="{hash_('extras')}"><strong>Extras &amp; add-ons</strong></a>
      </details>
      <details class="mobile-nav-group">
        <summary>Services</summary>
        <a href="{base}web-design-australia.html"><strong>Web design Australia</strong></a>
        <a href="{base}web-development-usa.html"><strong>Web development USA</strong></a>
        <a href="{base}saas-website-design.html"><strong>SaaS website design</strong></a>
        <a href="{hash_('care')}"><strong>Care plans</strong></a>
        <a href="{hash_('process')}"><strong>Process</strong></a>
      </details>
      <details class="mobile-nav-group">
        <summary>Resources</summary>
        <a href="{blog}/index.html"><strong>Blog</strong></a>
        <a href="{blog}/website-cost-australia.html"><strong>Website cost Australia</strong></a>
        <a href="{blog}/care-plan-vs-diy.html"><strong>Care plan vs DIY</strong></a>
        <a href="{blog}/saas-landing-page-checklist.html"><strong>SaaS landing page checklist</strong></a>
        <a href="{hash_('faq')}"><strong>FAQ</strong></a>
      </details>
      <a href="{hash_('contact')}">Contact</a>
      <a class="mobile-nav-cta" href="{hash_('packages')}">Make a deposit</a>
    </nav>"""

    brand_href = "/" if is_home else f"{base}index.html"
    cta_href = hash_("packages") if is_home else f"{ix}#packages"
    logo_src = f"{base}huginn-logo.png"

    return f"""<header>
  <div class="{wrap}">
    <div class="nav">
      <a class="brand" href="{brand_href}" aria-label="Huginn home">
        <img src="{logo_src}" alt="Huginn — web design and development" />
      </a>
{desktop}
      <a class="nav-cta" href="{cta_href}">Make a deposit</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-nav">Menu</button>
    </div>
{mobile}
  </div>
</header>"""


if __name__ == "__main__":
    for name, base, wide in [
        ("home", "", False),
        ("root", "", True),
        ("nested", "../", True),
    ]:
        out = ROOT / "partials" / f"nav-{name}.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(nav_html(base, wide=wide), encoding="utf-8")
        print("wrote", out)
