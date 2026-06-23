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
      <span class="promo-label mono">Limited special</span>
      <h2 id="promo-title">Starter website for domain cost only</h2>
      <p>Tier 1 build — up to 5 pages, mobile-first design, lead capture, SEO and analytics setup. Pay domain registration cost and we handle the rest.</p>
      <div class="promo-price">
        <span class="was">$499</span>
        <span class="now">$20</span>
        <span class="note">1st-year domain included · limited availability</span>
      </div>
      <div class="promo-actions">
        <a class="btn-primary" href="/#contact">Claim the special</a>
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
