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

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addCopyButtons);
  } else {
    addCopyButtons();
  }
})();
