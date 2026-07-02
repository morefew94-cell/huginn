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
