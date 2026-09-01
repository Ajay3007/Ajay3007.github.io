/**
 * assets/js/backend-roadmap.js
 * Backend Engineering Roadmap — Interactivity
 *
 * Features:
 * - Phase collapse/expand (localStorage state)
 * - Per-concept checklist checkboxes (localStorage)
 * - Phase + global progress bars
 * - Code block toggles (collapsed by default)
 * - Sticky phase pill nav with IntersectionObserver active-highlight
 */
(function () {
  'use strict';

  const LS = 'be-';
  const lsGet = k => localStorage.getItem(LS + k);
  const lsSet = (k, v) => localStorage.setItem(LS + k, v);

  /* ── Phase collapse/expand ─────────────────────────────────── */
  document.querySelectorAll('.ch-card').forEach(card => {
    const id = card.dataset.ch;
    if (!id) return;
    const header = card.querySelector('.ch-header');
    if (!header) return;
    if (lsGet('open-' + id) === '1') card.classList.add('open');
    header.addEventListener('click', () => {
      card.classList.toggle('open');
      lsSet('open-' + id, card.classList.contains('open') ? '1' : '0');
    });
  });

  /* ── Per-concept checkbox + phase progress ─────────────────── */
  function updatePhaseProgress(chId) {
    const card = document.querySelector(`.ch-card[data-ch="${chId}"]`);
    if (!card) return;
    const allRows = card.querySelectorAll('tr[data-key]');
    const doneRows = card.querySelectorAll('tr[data-key].solved').length;
    const total = allRows.length;
    const pct = total ? Math.round((doneRows / total) * 100) : 0;
    const bar = card.querySelector('.ch-prog-bar');
    const txt = card.querySelector('.ch-prog-text');
    const pctEl = card.querySelector('.ch-prog-pct');
    if (bar) bar.style.width = pct + '%';
    if (txt) txt.textContent = `${doneRows}/${total} checked`;
    if (pctEl) pctEl.textContent = pct + '%';
    const pill = document.querySelector(`.ch-pill[href="#${chId}"] .pill-count`);
    if (pill) pill.textContent = `${doneRows}/${total}`;
  }

  function updateGlobalProgress() {
    const allRows = document.querySelectorAll('tr[data-key]');
    const doneRows = document.querySelectorAll('tr[data-key].solved').length;
    const total = allRows.length;
    const pct = total ? Math.round((doneRows / total) * 100) : 0;
    const bar = document.querySelector('.be-op-bar');
    const pctEl = document.querySelector('.be-op-pct');
    const countEl = document.querySelector('.be-op-count');
    if (bar) bar.style.width = pct + '%';
    if (pctEl) pctEl.textContent = pct + '%';
    if (countEl) countEl.textContent = `${doneRows} of ${total} concepts checked`;
  }

  document.querySelectorAll('tr[data-key]').forEach(row => {
    const key = row.dataset.key;
    if (!key) return;
    if (lsGet(key) === '1') row.classList.add('solved');
    const checkEl = row.querySelector('.solved-check');
    if (!checkEl) return;
    checkEl.addEventListener('click', e => {
      e.stopPropagation();
      row.classList.toggle('solved');
      lsSet(key, row.classList.contains('solved') ? '1' : '0');
      const card = row.closest('.ch-card');
      if (card) updatePhaseProgress(card.dataset.ch);
      updateGlobalProgress();
    });
  });

  document.querySelectorAll('.ch-card').forEach(card => updatePhaseProgress(card.dataset.ch));
  updateGlobalProgress();

  /* ── Code block toggles ────────────────────────────────────── */
  document.querySelectorAll('.code-toggle-btn').forEach(btn => {
    const wrap = btn.nextElementSibling;
    if (!wrap || !wrap.classList.contains('code-block-wrap')) return;
    btn.addEventListener('click', () => {
      btn.classList.toggle('open');
      wrap.classList.toggle('open');
      const caret = btn.querySelector('.caret');
      if (caret) caret.textContent = wrap.classList.contains('open') ? '▾' : '▸';
    });
  });

  /* ── Sticky nav — IntersectionObserver ─────────────────────── */
  const pills = document.querySelectorAll('.ch-pill[href]');
  if (pills.length) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          pills.forEach(p => {
            p.classList.toggle('active', p.getAttribute('href') === '#' + id);
          });
          const activePill = document.querySelector(`.ch-pill[href="#${id}"]`);
          if (activePill) {
            activePill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
          }
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px', threshold: 0 });

    document.querySelectorAll('.ch-card[data-ch]').forEach(card => {
      const id = card.getAttribute('id');
      if (id) observer.observe(card);
    });
  }

})();
