const menuBtn = document.querySelector('.menu-btn');
const mobileNav = document.getElementById('mobile-nav');

if (menuBtn && mobileNav) {
  menuBtn.addEventListener('click', () => {
    const open = mobileNav.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', open);
    menuBtn.textContent = open ? 'Close' : 'Menu';
  });

  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      menuBtn.setAttribute('aria-expanded', 'false');
      menuBtn.textContent = 'Menu';
    });
  });
}

(function initNavDropdowns() {
  const dropdowns = document.querySelectorAll('.nav-links .nav-dropdown');
  if (!dropdowns.length) return;

  const desktopQuery = window.matchMedia('(min-width: 769px)');

  function closeAll(except) {
    dropdowns.forEach(dropdown => {
      if (dropdown === except) return;
      dropdown.classList.remove('open');
      const trigger = dropdown.querySelector('.nav-dropdown-trigger');
      if (trigger) trigger.setAttribute('aria-expanded', 'false');
    });
  }

  dropdowns.forEach(dropdown => {
    const trigger = dropdown.querySelector('.nav-dropdown-trigger');
    if (!trigger) return;

    let closeTimer;

    dropdown.addEventListener('mouseenter', () => {
      if (!desktopQuery.matches) return;
      window.clearTimeout(closeTimer);
      closeAll(dropdown);
      dropdown.classList.add('open');
      trigger.setAttribute('aria-expanded', 'true');
    });

    dropdown.addEventListener('mouseleave', () => {
      if (!desktopQuery.matches) return;
      closeTimer = window.setTimeout(() => {
        dropdown.classList.remove('open');
        trigger.setAttribute('aria-expanded', 'false');
      }, 120);
    });

    trigger.addEventListener('click', event => {
      event.preventDefault();
      event.stopPropagation();
      const open = dropdown.classList.toggle('open');
      trigger.setAttribute('aria-expanded', open);
      if (open) closeAll(dropdown);
    });
  });

  document.addEventListener('click', event => {
    if (event.target.closest('.nav-dropdown')) return;
    closeAll();
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') closeAll();
  });
})();

(function initSubpagePromo() {
  if (document.body.dataset.page === 'home') return;

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
