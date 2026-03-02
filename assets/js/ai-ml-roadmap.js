/**
 * assets/js/ai-ml-roadmap.js
 * AI & ML Roadmap — interactivity
 * - Career path filter (highlight/dim modules)
 * - Per-week checkbox progress tracking (localStorage)
 * - Module-level & overall progress bars
 * - Collapsible modules & prerequisites
 * - Portfolio & job-readiness checklists (localStorage)
 */

(function () {
  'use strict';

  const LS_PREFIX = 'aiml-';

  /* ─── Helpers ─────────────────────────────────────────────── */
  function lsGet(key) { return localStorage.getItem(LS_PREFIX + key); }
  function lsSet(key, val) { localStorage.setItem(LS_PREFIX + key, val); }

  /* ─── Prerequisites accordion ─────────────────────────────── */
  const prereqAcc = document.querySelector('.prereq-accordion');
  if (prereqAcc) {
    const header = prereqAcc.querySelector('.prereq-header');
    header.addEventListener('click', () => prereqAcc.classList.toggle('open'));
  }

  /* ─── Module collapse / expand ────────────────────────────── */
  document.querySelectorAll('.module-card').forEach(card => {
    const header = card.querySelector('.module-header');
    if (!header) return;
    const id = card.dataset.module;
    // restore open state
    if (lsGet('open-' + id) === '1') card.classList.add('open');
    header.addEventListener('click', () => {
      card.classList.toggle('open');
      lsSet('open-' + id, card.classList.contains('open') ? '1' : '0');
    });
  });

  /* ─── Week checkboxes + module progress ───────────────────── */
  function updateModuleProgress(moduleId) {
    const card = document.querySelector(`.module-card[data-module="${moduleId}"]`);
    if (!card) return;
    const all = card.querySelectorAll('.week-item');
    const done = card.querySelectorAll('.week-item.checked').length;
    const total = all.length;
    const pct = total ? Math.round((done / total) * 100) : 0;
    const bar = card.querySelector('.mod-prog-bar');
    const txt = card.querySelector('.mod-prog-text');
    const pctEl = card.querySelector('.mod-prog-pct');
    if (bar) bar.style.width = pct + '%';
    if (txt) txt.textContent = `${done}/${total} weeks`;
    if (pctEl) pctEl.textContent = pct + '%';
  }

  function updateOverallProgress() {
    const allWeeks = document.querySelectorAll('.week-item');
    const doneWeeks = document.querySelectorAll('.week-item.checked').length;
    const total = allWeeks.length;
    const pct = total ? Math.round((doneWeeks / total) * 100) : 0;
    const bar = document.querySelector('.aiml-op-bar');
    const pctEl = document.querySelector('.aiml-op-pct');
    const countEl = document.querySelector('.aiml-op-count');
    if (bar) bar.style.width = pct + '%';
    if (pctEl) pctEl.textContent = pct + '%';
    if (countEl) countEl.textContent = `${doneWeeks} of ${total} weeks completed`;
  }

  document.querySelectorAll('.week-item').forEach(item => {
    const key = item.dataset.key;
    if (!key) return;
    // restore
    if (lsGet(key) === '1') item.classList.add('checked');
    item.addEventListener('click', () => {
      item.classList.toggle('checked');
      lsSet(key, item.classList.contains('checked') ? '1' : '0');
      const moduleCard = item.closest('.module-card');
      if (moduleCard) updateModuleProgress(moduleCard.dataset.module);
      updateOverallProgress();
    });
  });

  // initialise all bars
  document.querySelectorAll('.module-card').forEach(card => {
    updateModuleProgress(card.dataset.module);
  });
  updateOverallProgress();

  /* ─── Career path filter ───────────────────────────────────── */
  let activeRole = null;

  document.querySelectorAll('.career-card').forEach(card => {
    card.addEventListener('click', () => {
      const role = card.dataset.role;
      if (activeRole === role) {
        // deactivate — show all
        activeRole = null;
        card.classList.remove('active');
        document.querySelectorAll('.module-card').forEach(m => {
          m.classList.remove('career-highlighted', 'career-dimmed');
        });
        return;
      }
      activeRole = role;
      document.querySelectorAll('.career-card').forEach(c => c.classList.remove('active'));
      card.classList.add('active');

      document.querySelectorAll('.module-card').forEach(m => {
        const roles = (m.dataset.roles || '').split(',');
        m.classList.remove('career-highlighted', 'career-dimmed');
        if (roles.includes(role)) {
          m.classList.add('career-highlighted');
        } else {
          m.classList.add('career-dimmed');
        }
      });
    });
  });

  /* ─── Portfolio / job-readiness checklists ─────────────────── */
  document.querySelectorAll('.check-item').forEach(item => {
    const key = item.dataset.key;
    if (!key) return;
    if (lsGet(key) === '1') item.classList.add('checked');
    item.addEventListener('click', () => {
      item.classList.toggle('checked');
      lsSet(key, item.classList.contains('checked') ? '1' : '0');
    });
  });

})();
