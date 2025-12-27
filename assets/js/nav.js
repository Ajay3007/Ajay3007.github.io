
document.addEventListener('DOMContentLoaded', () => {
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.site-nav');
  if (!btn || !nav) return;

  const mq = window.matchMedia('(max-width: 768px)');

  const closeNav = () => {
    nav.classList.remove('open');
    btn.classList.remove('open');
  };

  // --- Mobile off-canvas toggle ---
  btn.addEventListener('click', () => {
    nav.classList.toggle('open');
    btn.classList.toggle('open');
  });

  // Close nav when clicking outside (mobile)
  document.addEventListener('click', (e) => {
    if (mq.matches && !nav.contains(e.target) && !btn.contains(e.target)) {
      closeNav();
    }
  });

  // Close nav after link click (mobile)
  nav.addEventListener('click', (e) => {
    const t = e.target;
    if (mq.matches && t && t.tagName === 'A') {
      closeNav();
    }
  });

  // --- Active link highlight ---
  const baseurl = nav.dataset.baseurl || ''; // set via data-baseurl="{{ site.baseurl }}"
  const strip = (url) => {
    // Normalize a URL or path to a comparable pathname without trailing slash or baseurl
    try {
      const u = new URL(url, location.origin);
      let p = u.pathname;
      if (baseurl && p.startsWith(baseurl)) p = p.slice(baseurl.length);
      return p.replace(/\/$/, '');
    } catch {
      // Fallback for relative paths
      let p = url.replace(/\/$/, '');
      if (baseurl && p.startsWith(baseurl)) p = p.slice(baseurl.length);
      return p;
    }
  };

  const current = strip(location.pathname);

  nav.querySelectorAll('a[href]').forEach((a) => {
    const href = a.getAttribute('href');
    if (!href || /^https?:\/\//i.test(href)) return; // ignore external links
    const path = strip(href);
    if (path && (current === path || current.startsWith(path))) {
      a.classList.add('active');
      a.setAttribute('aria-current', 'page');
    }
  });

  // --- Dropdowns ---
  nav.querySelectorAll('.has-dropdown').forEach((dd) => {
    const trigger = dd.querySelector('a, button');
    const menu = dd.querySelector('.dropdown-menu');
    if (!trigger || !menu) return;

    trigger.setAttribute('aria-haspopup', 'true');
    trigger.setAttribute('aria-expanded', 'false');

    const openDesktop = () => {
      dd.classList.add('open');
      trigger.setAttribute('aria-expanded', 'true');
    };
    const closeDesktop = () => {
      dd.classList.remove('open');
      trigger.setAttribute('aria-expanded', 'false');
    };

    // Desktop: open/close on hover
    dd.addEventListener('mouseenter', () => { if (!mq.matches) openDesktop(); });
    dd.addEventListener('mouseleave', () => { if (!mq.matches) closeDesktop(); });

    // Mobile: toggle on click
    trigger.addEventListener('click', (e) => {
      if (mq.matches) {
        e.preventDefault();
        dd.classList.toggle('open');
        trigger.setAttribute('aria-expanded', dd.classList.contains('open') ? 'true' : 'false');
      }
    });

    // Keyboard: Escape closes (desktop)
    dd.addEventListener('keyup', (e) => {
      if (e.key === 'Escape' && !mq.matches) closeDesktop();
    });
  });

  // Close nav when breakpoint changes or on resize
  mq.addEventListener?.('change', closeNav);
  window.addEventListener('resize', () => {
    if (!mq.matches) closeNav();
  });
});
