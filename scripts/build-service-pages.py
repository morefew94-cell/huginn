#!/usr/bin/env python3
"""Generate care plans and process detail pages at site root."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAV = (ROOT / "partials" / "nav-root.html").read_text(encoding="utf-8")

FOOTER = """<footer>
  <div class="wrap-wide">
    <div class="brand-footer">
      <img src="huginn-logo.png" alt="Huginn" />
    </div>
    <p class="mono">Web design &amp; development, sharpened.</p>
    <p class="mono footer-links">
      <a href="web-design-australia.html">Australia</a> ·
      <a href="web-development-usa.html">USA</a> ·
      <a href="saas-website-design.html">SaaS</a> ·
      <a href="blog/index.html">Blog</a> ·
      <a href="privacy.html">Privacy</a> ·
      <a href="index.html#faq">FAQ</a>
    </p>
  </div>
</footer>

<script src="site-nav.js"></script>
</body>
</html>"""


def shell(title, description, canonical_slug, body, extra_scripts=""):
    breadcrumb_label = title.replace(" | Huginn", "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow" />
  <meta name="theme-color" content="#08090c" />
  <meta name="google-site-verification" content="r3BlNP4yPdbvOc2dqCGIzokBrElt6f1NIe89Prdp2Hs" />
  <title>{title}</title>
  <link rel="canonical" href="https://www.huginnweb.com/{canonical_slug}" />
  <link rel="icon" href="favicon.ico" sizes="any" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="subpage.css" />
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
    <p class="breadcrumb"><a href="index.html">Home</a> / {breadcrumb_label}</p>

{body}
  </div>
</main>

{FOOTER}
{extra_scripts}"""


CARE_PLANS = shell(
    "Website Care Plans | Huginn",
    "Website care plans from $99/mo — hosting, security updates, backups, content updates, and SEO reporting. Optional after your build is finalised.",
    "care-plans",
    """    <div class="page-hero">
      <span class="mono label">Care plans · USD · Optional</span>
      <h1>The site keeps working after launch</h1>
      <p class="lead">Care plans are optional. After your site is finalised, no further changes are included in the build fee — subscribe for ongoing hosting and updates, or use a one-off $99 change window if you only need occasional edits.</p>
    </div>

    <nav class="package-nav-links mono" aria-label="Care plan tiers">
      <a href="#essentials">Essentials</a>
      <a href="#growth">Growth</a>
      <a href="#partner">Partner</a>
      <a href="#change-window">Change window</a>
    </nav>

    <div class="billing-toggle" role="group" aria-label="Care plan billing period">
      <button type="button" class="active" data-billing="monthly" aria-pressed="true">Monthly</button>
      <button type="button" data-billing="6" aria-pressed="false">6 months</button>
      <button type="button" data-billing="12" aria-pressed="false">12 months <small style="opacity:0.85">· save 20%</small></button>
    </div>

    <div class="extra-detail" id="essentials">
      <h3>Essentials — keep it running</h3>
      <p class="care-tier-price" data-care-price="99"><span class="care-amount">$99</span><small class="care-suffix">/mo</small></p>
      <p>The basics covered so you can focus on your business — hosting, security, and backups handled on Huginn infrastructure.</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>What's included</h3>
          <ul class="scope-list">
            <li>Hosting with Huginn (huginnweb.com)</li>
            <li>Security updates for your site stack</li>
            <li>Daily backups</li>
            <li>Uptime monitoring</li>
            <li>SSL certificate maintenance</li>
            <li>Basic technical support for hosting issues</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>What's not included</h3>
          <ul class="scope-list">
            <li>Content or design changes</li>
            <li>SEO reporting or performance reviews</li>
            <li>New pages or feature development</li>
            <li>Domain renewal fees (paid to your registrar)</li>
            <li>Third-party tool subscriptions</li>
            <li>Email mailbox hosting fees</li>
          </ul>
        </div>
      </div>
      <a class="btn-primary" href="index.html#contact">Get Essentials</a>
    </div>

    <div class="extra-detail" id="growth">
      <span class="care-tier-badge">Most chosen</span>
      <h3>Growth — keep it current</h3>
      <p class="care-tier-price" data-care-price="299"><span class="care-amount">$299</span><small class="care-suffix">/mo</small></p>
      <p>Regular updates and insight so the site keeps performing — everything in Essentials plus monthly content work and reporting.</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>What's included</h3>
          <ul class="scope-list">
            <li>Everything in Essentials</li>
            <li>Monthly content updates (scoped each month)</li>
            <li>SEO performance reporting</li>
            <li>Conversion and performance review</li>
            <li>Minor layout and copy tweaks within scope</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>What's not included</h3>
          <ul class="scope-list">
            <li>Major redesigns or new page builds</li>
            <li>Custom development or new integrations</li>
            <li>Unlimited same-day changes</li>
            <li>Paid advertising management</li>
            <li>Logo or brand kit work</li>
            <li>Work outside the agreed monthly scope</li>
          </ul>
        </div>
      </div>
      <a class="btn-primary" href="index.html#contact">Get Growth</a>
    </div>

    <div class="extra-detail" id="partner">
      <h3>Partner — outsourced digital team</h3>
      <p class="care-tier-price" data-care-price="1249"><span class="care-amount">$1,249</span><small class="care-suffix">/mo</small></p>
      <p>Ongoing optimisation and priority support when you need a partner, not just a host — for businesses that treat their site as a growth channel.</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>What's included</h3>
          <ul class="scope-list">
            <li>Everything in Growth</li>
            <li>Ongoing conversion optimisation</li>
            <li>Lead-generation campaign support</li>
            <li>Priority support and faster change turnaround</li>
            <li>Proactive recommendations each month</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>What's not included</h3>
          <ul class="scope-list">
            <li>Full platform rebuilds (new Pro-tier projects)</li>
            <li>Large-scale custom software development</li>
            <li>Dedicated full-time staff allocation</li>
            <li>Media buying budgets (ad spend)</li>
            <li>Legal, compliance, or industry certification consulting</li>
            <li>24/7 emergency on-call outside business hours</li>
          </ul>
        </div>
      </div>
      <a class="btn-primary" href="index.html#contact">Get Partner</a>
    </div>

    <div class="extra-detail" id="change-window">
      <h3>One-off change window — no subscription</h3>
      <p class="care-tier-price">$99 <small>· 10 business days</small></p>
      <p>If your site is already finalised and you don't need ongoing updates, a change window covers a short round of revisions without subscribing to a care plan.</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>What's included</h3>
          <ul class="scope-list">
            <li>10 business days to request and approve revisions</li>
            <li>Copy, image, and minor layout updates within scope</li>
            <li>One consolidated round of changes</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>What's not included</h3>
          <ul class="scope-list">
            <li>Hosting (must already be live or self-hosted)</li>
            <li>New pages or major feature development</li>
            <li>Ongoing monthly updates after the window closes</li>
            <li>Emergency or same-day turnaround</li>
          </ul>
        </div>
      </div>
      <a class="btn-primary" href="index.html#contact">Request a change window</a>
    </div>

    <div class="related">
      <h2>Related</h2>
      <ul>
        <li><a href="blog/care-plan-vs-diy.html">Care plan vs DIY</a></li>
        <li><a href="packages/starter.html">Build packages</a></li>
        <li><a href="our-process.html">Our process</a></li>
      </ul>
    </div>""",
    extra_scripts="""
<script>
(function () {
  const carePrices = document.querySelectorAll('[data-care-price]');
  const billingBtns = document.querySelectorAll('[data-billing]');
  if (!carePrices.length || !billingBtns.length) return;

  function formatCarePrice(amount) {
    return amount.toLocaleString('en-US');
  }

  function updateCarePrices(period) {
    carePrices.forEach(el => {
      const monthly = Number(el.dataset.carePrice);
      const amountEl = el.querySelector('.care-amount');
      const suffixEl = el.querySelector('.care-suffix');
      if (!amountEl || !suffixEl) return;

      if (period === 'monthly') {
        amountEl.textContent = '$' + formatCarePrice(monthly);
        suffixEl.textContent = '/mo';
      } else if (period === '6') {
        amountEl.textContent = '$' + formatCarePrice(monthly * 6);
        suffixEl.textContent = '/6 mo';
      } else {
        amountEl.textContent = '$' + formatCarePrice(Math.round(monthly * 12 * 0.8));
        suffixEl.textContent = '/yr';
      }
    });
  }

  billingBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      billingBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-pressed', 'true');
      updateCarePrices(btn.dataset.billing);
    });
  });
})();
</script>""",
)

OUR_PROCESS = shell(
    "Our Process | Huginn Web Design",
    "How Huginn builds websites — four stages from survey to handover. Survey, plan, build, and launch with domain and hosting included.",
    "our-process",
    """    <div class="page-hero">
      <span class="mono label">How it works</span>
      <h1>Four stages. Start to finish.</h1>
      <p class="lead">Same logic as a build program — survey the site, plan the works, build it, hand it over ready to use. No surprises at launch because structure and scope are signed off before design starts.</p>
    </div>

    <nav class="package-nav-links mono" aria-label="Build process">
      <a href="#survey">Survey</a>
      <a href="#plan">Plan</a>
      <a href="#build">Build</a>
      <a href="#handover">Handover</a>
    </nav>

    <div class="process-detail" id="survey">
      <div class="process-detail-header">
        <span class="process-step-num">1</span>
        <h3>Survey</h3>
      </div>
      <p class="step-timing">Kickoff · ~30–60 minutes</p>
      <p>A short call to understand your business, how you win work today, and where the gaps are. We capture goals, audience, competitors, and any must-have features before quoting.</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>What's included</h3>
          <ul class="scope-list">
            <li>Discovery call (video or phone)</li>
            <li>Business goals and target audience review</li>
            <li>Review of existing site or brand assets if you have them</li>
            <li>Initial package and extras recommendation</li>
            <li>Deposit link to secure your build slot</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>Your responsibilities</h3>
          <ul class="scope-list">
            <li>Share access to any existing domain or hosting if relevant</li>
            <li>Provide rough content or direction where you have it</li>
            <li>Confirm decision-makers for sign-off</li>
            <li>Pay deposit via Stripe to start the plan phase</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="process-detail" id="plan">
      <div class="process-detail-header">
        <span class="process-step-num">2</span>
        <h3>Plan</h3>
      </div>
      <p class="step-timing">Before design starts</p>
      <p>Page list, structure, and copy direction — signed off before any design work. Growth and Pro projects receive a detailed site plan with timeline; Starter projects follow the tier 1 scope.</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>What's included</h3>
          <ul class="scope-list">
            <li>Sitemap and page structure</li>
            <li>Wireframe or layout direction for key pages</li>
            <li>Content outline and copy direction</li>
            <li>Confirmed timeline and revision schedule</li>
            <li>Quoted extras added to your build invoice</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>What's not included yet</h3>
          <ul class="scope-list">
            <li>Final visual design (that's the Build stage)</li>
            <li>Development or going live</li>
            <li>Full written copy unless copywriting extra is added</li>
            <li>Scope beyond what was agreed in the signed plan</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="process-detail" id="build">
      <div class="process-detail-header">
        <span class="process-step-num">3</span>
        <h3>Build</h3>
      </div>
      <p class="step-timing">~20-30 business days depending on package</p>
      <p>Design and development in check-ins so there are no surprises at handover. Starter typically ~20 days; Growth ~20-25 days; Pro ~25-30 days. Starter runs 10 days working draft, then 10 days unlimited revisions. Growth and Pro follow the timeline in your signed site plan.</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>What's included</h3>
          <ul class="scope-list">
            <li>Visual design and front-end build</li>
            <li>Mobile-first responsive layouts</li>
            <li>Forms, SEO setup, and structured data as per package</li>
            <li>Regular progress updates and revision rounds</li>
            <li>Staging review before launch</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>What's not included</h3>
          <ul class="scope-list">
            <li>Changes outside signed scope without a change order</li>
            <li>Content you haven't supplied by agreed deadlines</li>
            <li>Third-party account setup you prefer to manage yourself</li>
            <li>Ongoing updates after final sign-off (care plan or change window)</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="process-detail" id="handover">
      <div class="process-detail-header">
        <span class="process-step-num">4</span>
        <h3>Handover</h3>
      </div>
      <p class="step-timing">Launch · balance due before go-live</p>
      <p>Live on the internet with domain and hosting in place. You own the site outright once the build is paid in full. Need changes later? Care plan, or a $99 change window for occasional edits.</p>
      <div class="scope-grid">
        <div class="scope-card included">
          <h3>What's included</h3>
          <ul class="scope-list">
            <li>Domain registration (1st year on Starter) and DNS setup</li>
            <li>Site live on the internet — hosted through Huginn or self-host handover</li>
            <li>Final balance invoiced and paid before launch</li>
            <li>Ownership transferred to you — Huginn retains no rights</li>
            <li>Basic launch checklist (search console, forms tested)</li>
          </ul>
        </div>
        <div class="scope-card not-included">
          <h3>After handover</h3>
          <ul class="scope-list">
            <li>Further edits without a care plan or change window</li>
            <li>Domain renewal after year one</li>
            <li>Google Analytics setup (your responsibility if wanted)</li>
            <li>Training on CMS unless scoped in Growth/Pro plan</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="btn-row">
      <a class="btn-primary" href="index.html#packages">Reserve my build</a>
      <a class="btn-ghost" href="blog/whats-in-a-site-plan.html">What's in a site plan?</a>
    </div>

    <div class="related">
      <h2>Related</h2>
      <ul>
        <li><a href="packages/starter.html">Starter package</a></li>
        <li><a href="care-plans.html">Website care plans</a></li>
        <li><a href="index.html#faq">FAQ</a></li>
      </ul>
    </div>""",
)

PAGES = {
    "care-plans.html": CARE_PLANS,
    "our-process.html": OUR_PROCESS,
}

if __name__ == "__main__":
    if not (ROOT / "partials" / "nav-root.html").exists():
        raise SystemExit("Run scripts/render-nav.py first")
    for name, html in PAGES.items():
        path = ROOT / name
        path.write_text(html, encoding="utf-8")
        print("wrote", path)
