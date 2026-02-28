document.addEventListener('DOMContentLoaded', function() {
  var scrollTopBtn = document.getElementById('scroll-to-top');

  window.addEventListener('scroll', function() {
    // Scroll-to-top button visibility
    if (scrollTopBtn) {
      if (window.scrollY > 300) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    }
  });

  // Scroll-to-top click handler
  if (scrollTopBtn) {
    scrollTopBtn.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  var btn = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (!btn || !nav) return;

  btn.addEventListener('click', function() {
    nav.classList.toggle('open');
    btn.classList.toggle('open');
  });

  // Close nav when clicking outside on small screens
  document.addEventListener('click', function(e) {
    if (window.innerWidth <= 1024) {
      if (!nav.contains(e.target) && !btn.contains(e.target)) {
        nav.classList.remove('open');
        btn.classList.remove('open');
      }
    }
  });

  // Close nav when a link inside it is clicked (mobile)
  nav.addEventListener('click', function(e) {
    var target = e.target;
    if (target && target.tagName === 'A' && window.innerWidth <= 1024) {
      nav.classList.remove('open');
      btn.classList.remove('open');
    }
  });
});
