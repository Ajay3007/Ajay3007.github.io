(function () {
  var phrases = [
    'networking & data plane.',
    'backend architecture.',
    'real-time threat detection.',
    'scalable system design.',
    'DPDK & VPP performance.',
    'DSA & competitive programming.',
  ];

  var el = document.getElementById('hero-typed');
  if (!el) return;

  var phraseIndex = 0;
  var charIndex = 0;
  var isDeleting = false;
  var TYPING_SPEED = 60;
  var DELETING_SPEED = 35;
  var PAUSE_AFTER_TYPE = 1800;
  var PAUSE_AFTER_DELETE = 400;

  function tick() {
    var current = phrases[phraseIndex];

    if (isDeleting) {
      charIndex--;
    } else {
      charIndex++;
    }

    el.textContent = current.slice(0, charIndex);

    var delay = isDeleting ? DELETING_SPEED : TYPING_SPEED;

    if (!isDeleting && charIndex === current.length) {
      // Finished typing — pause then start deleting
      delay = PAUSE_AFTER_TYPE;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      // Finished deleting — move to next phrase
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      delay = PAUSE_AFTER_DELETE;
    }

    setTimeout(tick, delay);
  }

  // Small initial delay so page has settled
  setTimeout(tick, 600);
})();
