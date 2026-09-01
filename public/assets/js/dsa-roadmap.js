/**
 * assets/js/dsa-roadmap.js
 * DSA Mastery Roadmap — Interactivity
 *
 * Features:
 * - Chapter collapse/expand (localStorage state)
 * - Per-problem solved checkboxes (localStorage, independent)
 * - Chapter + global progress bars
 * - Difficulty filter (Easy / Medium / Hard)
 * - Sticky chapter pill nav with IntersectionObserver active-highlight
 * - Code block toggles (collapsed by default)
 */
(function () {
  'use strict';

  const LS = 'dsa-';
  const lsGet = k => localStorage.getItem(LS + k);
  const lsSet = (k, v) => localStorage.setItem(LS + k, v);

  /* ── Chapter collapse/expand ───────────────────────────────── */
  document.querySelectorAll('.ch-card').forEach(card => {
    const id = card.dataset.ch;
    if (!id) return;
    const header = card.querySelector('.ch-header');
    if (!header) return;
    // restore
    if (lsGet('open-' + id) === '1') card.classList.add('open');
    header.addEventListener('click', () => {
      card.classList.toggle('open');
      lsSet('open-' + id, card.classList.contains('open') ? '1' : '0');
    });
  });

  /* ── Per-problem checkbox + chapter progress ──────────────── */
  function updateChapterProgress(chId) {
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
    if (txt) txt.textContent = `${doneRows}/${total} solved`;
    if (pctEl) pctEl.textContent = pct + '%';

    // update pill
    const pill = document.querySelector(`.ch-pill[href="#${chId}"] .pill-count`);
    if (pill) pill.textContent = `${doneRows}/${total}`;
  }

  function updateGlobalProgress() {
    const allRows = document.querySelectorAll('tr[data-key]');
    const doneRows = document.querySelectorAll('tr[data-key].solved').length;
    const total = allRows.length;
    const pct = total ? Math.round((doneRows / total) * 100) : 0;
    const bar = document.querySelector('.dsa-op-bar');
    const pctEl = document.querySelector('.dsa-op-pct');
    const countEl = document.querySelector('.dsa-op-count');
    if (bar) bar.style.width = pct + '%';
    if (pctEl) pctEl.textContent = pct + '%';
    if (countEl) countEl.textContent = `${doneRows} of ${total} problems solved`;
  }

  document.querySelectorAll('tr[data-key]').forEach(row => {
    const key = row.dataset.key;
    if (!key) return;
    // restore
    if (lsGet(key) === '1') row.classList.add('solved');

    const checkEl = row.querySelector('.solved-check');
    if (!checkEl) return;
    checkEl.addEventListener('click', e => {
      e.stopPropagation(); // don't bubble to chapter header
      row.classList.toggle('solved');
      lsSet(key, row.classList.contains('solved') ? '1' : '0');
      const card = row.closest('.ch-card');
      if (card) updateChapterProgress(card.dataset.ch);
      updateGlobalProgress();
    });
  });

  // Init all progress bars
  document.querySelectorAll('.ch-card').forEach(card => updateChapterProgress(card.dataset.ch));
  updateGlobalProgress();

  /* ── Difficulty filter ─────────────────────────────────────── */
  let activeDiff = lsGet('diff-filter') || 'all';

  function applyFilter(diff) {
    activeDiff = diff;
    lsSet('diff-filter', diff);
    document.querySelectorAll('tr[data-diff]').forEach(row => {
      if (diff === 'all' || row.dataset.diff === diff) {
        row.classList.remove('diff-hidden');
      } else {
        row.classList.add('diff-hidden');
      }
    });
    document.querySelectorAll('.diff-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.diff === diff);
    });
  }

  document.querySelectorAll('.diff-btn').forEach(btn => {
    btn.addEventListener('click', () => applyFilter(btn.dataset.diff));
  });
  applyFilter(activeDiff); // restore on load

  /* ── Code block toggles ───────────────────────────────────── */
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
          // scroll active pill into view
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

  /* ── Cheatsheet toggle ─────────────────────────────────────── */
  const cs = document.querySelector('.dsa-cheatsheet-toggle');
  if (cs) {
    cs.querySelector('.dsa-cheatsheet-header').addEventListener('click', () => {
      cs.classList.toggle('open');
    });
  }

})();
