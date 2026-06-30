(function () {
  const STORAGE_KEY = 'huginn-promo-seen';
  if (sessionStorage.getItem(STORAGE_KEY)) return;

  const modal = document.createElement('div');
  modal.className = 'promo-modal';
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  modal.setAttribute('aria-labelledby', 'promo-title');
  modal.innerHTML = `
    <div class="promo-backdrop" data-promo-close></div>
    <div class="promo-dialog">
      <button type="button" class="promo-close" data-promo-close aria-label="Close promotion">&times;</button>
      <span class="promo-label mono">Limited time offer</span>
      <h2 id="promo-title">Pay the domain fee. Get a website.</h2>
      <p>Limited-time offer — pay just the domain registration fee and we'll build your tier 1 Starter site. Up to 5 pages, mobile-first design, lead capture, and SEO setup. Domain and going live included — you own the site.</p>
      <div class="promo-price">
        <span class="was">$499</span>
        <span class="now">$20</span>
        <span class="note">Deposit · domain + going live · ~20-30 business days</span>
      </div>
      <div class="promo-actions">
        <a class="btn-primary" href="/api/checkout?tier=starter">Reserve my build</a>
        <a class="btn-ghost" href="/#packages">View packages</a>
      </div>
    </div>
  `;

  document.body.appendChild(modal);
  document.body.classList.add('promo-open');

  function closePromo() {
    sessionStorage.setItem(STORAGE_KEY, '1');
    modal.classList.remove('open');
    document.body.classList.remove('promo-open');
    window.setTimeout(() => modal.remove(), 300);
  }

  modal.querySelectorAll('[data-promo-close]').forEach(el => {
    el.addEventListener('click', closePromo);
  });

  modal.querySelectorAll('.promo-actions a').forEach(link => {
    link.addEventListener('click', closePromo);
  });

  document.addEventListener('keydown', function onKeydown(event) {
    if (event.key === 'Escape' && document.body.contains(modal)) {
      closePromo();
      document.removeEventListener('keydown', onKeydown);
    }
  });

  window.requestAnimationFrame(() => {
    window.setTimeout(() => modal.classList.add('open'), 120);
  });
})();
