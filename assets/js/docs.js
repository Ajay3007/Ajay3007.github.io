/* Docs enhancements (redesign Phase 5).
   Currently: copy-to-clipboard buttons on code blocks in the docs content.
   Progressive enhancement — if anything is unsupported the page is unaffected. */
(function () {
  'use strict';

  function addCopyButtons() {
    if (!navigator.clipboard) return; // needs a secure context (GitHub Pages is https)
    var pres = document.querySelectorAll('.learning-content pre');
    for (var i = 0; i < pres.length; i++) {
      var pre = pres[i];
      // Attach to the Rouge .highlight wrapper when present, else the <pre>.
      var container = pre.closest ? (pre.closest('.highlight') || pre) : pre;
      if (container.getAttribute('data-copy-ready')) continue;
      container.setAttribute('data-copy-ready', '1');

      var btn = document.createElement('button');
      btn.className = 'copy-code-btn';
      btn.type = 'button';
      btn.textContent = 'Copy';
      btn.setAttribute('aria-label', 'Copy code to clipboard');

      (function (btnRef, preRef) {
        btnRef.addEventListener('click', function () {
          var codeEl = preRef.querySelector('code') || preRef;
          var text = codeEl.innerText;
          navigator.clipboard.writeText(text).then(function () {
            btnRef.textContent = 'Copied!';
            setTimeout(function () { btnRef.textContent = 'Copy'; }, 1500);
          }, function () {
            btnRef.textContent = 'Failed';
            setTimeout(function () { btnRef.textContent = 'Copy'; }, 1500);
          });
        });
      })(btn, pre);

      container.appendChild(btn);
    }
  }

  function buildTOC() {
    var toc = document.getElementById('doc-toc');
    var content = document.querySelector('.learning-content');
    if (!toc || !content) return;
    var headings = content.querySelectorAll('h2, h3');
    if (headings.length < 2) return; // not worth a table of contents

    var nav = toc.querySelector('.toc-nav');
    var links = [];
    for (var i = 0; i < headings.length; i++) {
      var h = headings[i];
      if (!h.id) {
        h.id = 'sec-' + i + '-' + h.textContent.trim().toLowerCase()
          .replace(/[^\w]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 40);
      }
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent;
      a.className = 'toc-link toc-' + h.tagName.toLowerCase();
      nav.appendChild(a);
      links.push({ a: a, h: h });
    }
    toc.hidden = false;

    // Scroll-spy: highlight the last heading scrolled past.
    var ticking = false;
    function spy() {
      ticking = false;
      var current = null;
      for (var j = 0; j < links.length; j++) {
        if (links[j].h.getBoundingClientRect().top <= 140) current = links[j];
      }
      for (var k = 0; k < links.length; k++) {
        links[k].a.classList.toggle('active', links[k] === current);
      }
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(spy); }
    }, { passive: true });
    spy();
  }

  function init() { addCopyButtons(); buildTOC(); }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
