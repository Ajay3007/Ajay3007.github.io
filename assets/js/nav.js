document.addEventListener('DOMContentLoaded', function() {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (!btn || !nav) return;

  btn.addEventListener('click', function() {
    nav.classList.toggle('open');
    btn.classList.toggle('open');
  });

  // Close nav when clicking outside on small screens
  document.addEventListener('click', function(e) {
    if (window.innerWidth <= 768) {
      if (!nav.contains(e.target) && !btn.contains(e.target)) {
        nav.classList.remove('open');
        btn.classList.remove('open');
      }
    }
  });

  // Close nav when a link inside it is clicked (mobile)
  nav.addEventListener('click', function(e) {
    var target = e.target;
    if (target && target.tagName === 'A' && window.innerWidth <= 768) {
      nav.classList.remove('open');
      btn.classList.remove('open');
    }
  });
});


// nav.js (append to your existing script)
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (!btn || !nav) return;

  // === Active link highlight ===
  var current = location.pathname.replace(/\/$/, '');
  nav.querySelectorAll('a[href]').forEach(function (a) {
    var href = a.getAttribute('href');
    if (!href) return;
    var path = href.replace(location.origin, '').replace(/\/$/, '');

    // Mark active if exact match or section root match
    if (path && (current === path || (path !== '/' && current.startsWith(path)))) {
      a.classList.add('active');
    }
  });

  // === Dropdowns ===
  var dropdowns = nav.querySelectorAll('.has-dropdown');
  dropdowns.forEach(function (dd) {
    var trigger = dd.querySelector('a, button');
    var menu = dd.querySelector('.dropdown-menu');
    if (!trigger || !menu) return;

    // Accessibility
    trigger.setAttribute('aria-haspopup', 'true');
    trigger.setAttribute('aria-expanded', 'false');

    // Desktop: open on hover
    dd.addEventListener('mouseenter', function () {
      if (window.innerWidth > 768) {
        dd.classList.add('open');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });
    dd.addEventListener('mouseleave', function () {
      if (window.innerWidth > 768) {
        dd.classList.remove('open');
        trigger.setAttribute('aria-expanded', 'false');
      }
    });

    // Mobile: toggle on click
    trigger.addEventListener('click', function (e) {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        dd.classList.toggle('open');
        trigger.setAttribute('aria-expanded', dd.classList.contains('open') ? 'true' : 'false');
      }
    });
  });
});
