/**
 * assets/js/ai-ml-roadmap.js
 * AI & ML Roadmap — interactivity
 *
 * Combines:
 * A. Original module/week/career/checklist tracking (localStorage)
 * B. New inline script from AIML_Roadmap.html: scroll progress, part nav,
 *    path selector, mc2 module toggle, new checklist toggle, scroll-to-top
 */

(function () {
  'use strict';

  /* ─── Helpers ─────────────────────────────────────────────────── */
  const LS_PREFIX = 'aiml-';
  function lsGet(key) { return localStorage.getItem(LS_PREFIX + key); }
  function lsSet(key, val) { localStorage.setItem(LS_PREFIX + key, val); }

  /* ─── Scroll progress bar + scroll-to-top visibility ──────────── */
  window.addEventListener('scroll', function () {
    var s = document.documentElement;
    var b = document.body;
    var scrolled = (s.scrollTop || b.scrollTop);
    var total = (s.scrollHeight || b.scrollHeight) - s.clientHeight;
    var pct = total > 0 ? (scrolled / total) * 100 : 0;
    var pb = document.getElementById('pb');
    if (pb) pb.style.width = pct + '%';
    var sct = document.getElementById('sct');
    if (sct) {
      if (scrolled > 300) {
        sct.classList.add('vis');
      } else {
        sct.classList.remove('vis');
      }
    }
  });

  /* ─── Part navigation ──────────────────────────────────────────── */
  window.showP = function (id, btn) {
    document.querySelectorAll('.psec').forEach(function (s) {
      s.classList.remove('active');
    });
    document.querySelectorAll('.pnb').forEach(function (b) {
      b.classList.remove('active');
    });
    var target = document.getElementById(id);
    if (target) target.classList.add('active');
    if (btn) btn.classList.add('active');
    var nav = document.querySelector('.pnav');
    if (nav) {
      window.scrollTo({ top: nav.offsetTop - 12, behavior: 'smooth' });
    }
  };

  /* ─── Path selector ────────────────────────────────────────────── */
  window.selPath = function (btn, id) {
    document.querySelectorAll('.ptb').forEach(function (b) {
      b.classList.remove('active');
    });
    document.querySelectorAll('.pc').forEach(function (p) {
      p.classList.remove('active');
    });
    if (btn) btn.classList.add('active');
    var panel = document.getElementById(id);
    if (panel) panel.classList.add('active');
  };

  /* ─── mc2 module toggle (new-style cards) + localStorage ──────── */
  window.togM = function (hdr) {
    var card = hdr.parentElement;
    card.classList.toggle('open');
    // persist open state using card id if present
    var cardId = card.id;
    if (cardId) {
      lsSet('mc2-open-' + cardId, card.classList.contains('open') ? '1' : '0');
    }
  };

  /* ─── New-style checklist toggle (Part 9 .ck lists) ───────────── */
  window.togCk = function (li) {
    li.classList.toggle('chk');
    var key = li.dataset.key;
    if (key) {
      lsSet(key, li.classList.contains('chk') ? '1' : '0');
      updateOverallProgress();
    }
  };

  /* ─── Scroll to top ────────────────────────────────────────────── */
  window.sctop = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  /* ─── Restore mc2 open states from localStorage ────────────────── */
  document.querySelectorAll('.mc2[id]').forEach(function (card) {
    if (lsGet('mc2-open-' + card.id) === '1') {
      card.classList.add('open');
    }
  });

  /* ─── Prerequisites accordion (old-style) ──────────────────────── */
  var prereqAcc = document.querySelector('.prereq-accordion');
  if (prereqAcc) {
    var prereqHeader = prereqAcc.querySelector('.prereq-header');
    if (prereqHeader) {
      prereqHeader.addEventListener('click', function () {
        prereqAcc.classList.toggle('open');
      });
    }
  }

  /* ─── Old-style module-card collapse / expand ──────────────────── */
  document.querySelectorAll('.module-card').forEach(function (card) {
    var header = card.querySelector('.module-header');
    if (!header) return;
    var id = card.dataset.module;
    if (lsGet('open-' + id) === '1') card.classList.add('open');
    header.addEventListener('click', function () {
      card.classList.toggle('open');
      lsSet('open-' + id, card.classList.contains('open') ? '1' : '0');
    });
  });

  /* ─── Week checkboxes + module progress ────────────────────────── */
  function updateModuleProgress(moduleId) {
    var card = document.querySelector('.module-card[data-module="' + moduleId + '"]');
    if (!card) return;
    var all = card.querySelectorAll('.week-item');
    var done = card.querySelectorAll('.week-item.checked').length;
    var total = all.length;
    var pct = total ? Math.round((done / total) * 100) : 0;
    var bar = card.querySelector('.mod-prog-bar');
    var txt = card.querySelector('.mod-prog-text');
    var pctEl = card.querySelector('.mod-prog-pct');
    if (bar) bar.style.width = pct + '%';
    if (txt) txt.textContent = done + '/' + total + ' weeks';
    if (pctEl) pctEl.textContent = pct + '%';
  }

  function updateOverallProgress() {
    var allCk = document.querySelectorAll('.ck li[data-key]');
    var allWeeks = document.querySelectorAll('.week-item');
    var total, done, label;
    if (allCk.length) {
      done = document.querySelectorAll('.ck li[data-key].chk').length;
      total = allCk.length;
      label = ' items completed';
    } else {
      done = document.querySelectorAll('.week-item.checked').length;
      total = allWeeks.length;
      label = ' weeks completed';
    }
    var pct = total ? Math.round((done / total) * 100) : 0;
    var bar = document.querySelector('.aiml-op-bar');
    var pctEl = document.querySelector('.aiml-op-pct');
    var countEl = document.querySelector('.aiml-op-count');
    if (bar) bar.style.width = pct + '%';
    if (pctEl) pctEl.textContent = pct + '%';
    if (countEl) countEl.textContent = done + ' of ' + total + label;
  }

  document.querySelectorAll('.week-item').forEach(function (item) {
    var key = item.dataset.key;
    if (!key) return;
    if (lsGet(key) === '1') item.classList.add('checked');
    item.addEventListener('click', function () {
      item.classList.toggle('checked');
      lsSet(key, item.classList.contains('checked') ? '1' : '0');
      var moduleCard = item.closest('.module-card');
      if (moduleCard) updateModuleProgress(moduleCard.dataset.module);
      updateOverallProgress();
    });
  });

  // Initialise all progress bars
  document.querySelectorAll('.module-card').forEach(function (card) {
    updateModuleProgress(card.dataset.module);
  });

  // Restore new-style checklist state from localStorage
  document.querySelectorAll('.ck li[data-key]').forEach(function (li) {
    if (lsGet(li.dataset.key) === '1') li.classList.add('chk');
  });

  updateOverallProgress();

  /* ─── Career path filter ────────────────────────────────────────── */
  var activeRole = null;

  document.querySelectorAll('.career-card').forEach(function (card) {
    card.addEventListener('click', function () {
      var role = card.dataset.role;
      if (activeRole === role) {
        activeRole = null;
        card.classList.remove('active');
        document.querySelectorAll('.module-card').forEach(function (m) {
          m.classList.remove('career-highlighted', 'career-dimmed');
        });
        return;
      }
      activeRole = role;
      document.querySelectorAll('.career-card').forEach(function (c) {
        c.classList.remove('active');
      });
      card.classList.add('active');
      document.querySelectorAll('.module-card').forEach(function (m) {
        var roles = (m.dataset.roles || '').split(',');
        m.classList.remove('career-highlighted', 'career-dimmed');
        if (roles.includes(role)) {
          m.classList.add('career-highlighted');
        } else {
          m.classList.add('career-dimmed');
        }
      });
    });
  });

  /* ─── Old-style portfolio / job-readiness checklists ───────────── */
  document.querySelectorAll('.check-item').forEach(function (item) {
    var key = item.dataset.key;
    if (!key) return;
    if (lsGet(key) === '1') item.classList.add('checked');
    item.addEventListener('click', function () {
      item.classList.toggle('checked');
      lsSet(key, item.classList.contains('checked') ? '1' : '0');
    });
  });

})();
