/* ================================================================
   assets/js/sd-module-a1.js
   JavaScript for LLD Module A1 — SOLID + OOP + UML
   ================================================================ */

// ── Tab switching (main 7-tab nav) ─────────────────────────────
function m1Show(tab, el) {
  document.querySelectorAll('.m1-view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.m1-nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('m1-view-' + tab).classList.add('active');
  el.classList.add('active');
}

// ── SOLID principle panel switcher ─────────────────────────────
function m1SelectSolid(letter, el) {
  document.querySelectorAll('.m1-solid-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.m1-solid-panel').forEach(p => p.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('m1-solid-' + letter).classList.add('active');
}

// ── Task accordion ─────────────────────────────────────────────
function m1ToggleTask(head) {
  const body = head.nextElementSibling;
  const chev = head.querySelector('.m1-task-chevron');
  const open = body.classList.contains('open');
  body.classList.toggle('open', !open);
  chev.classList.toggle('open', !open);
}

// ── Checklist with localStorage persistence ────────────────────
const M1_STORAGE_KEY = 'sd-module-a1-checklist';

function m1Toggle(el) {
  el.classList.toggle('done');
  el.querySelector('.m1-chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  m1UpdateProgress();
  m1SaveChecklist();
}

function m1UpdateProgress() {
  const total = document.querySelectorAll('.m1-chk').length;
  const done  = document.querySelectorAll('.m1-chk.done').length;
  const label = document.getElementById('m1-prog-label');
  const fill  = document.getElementById('m1-prog-fill');
  if (label) label.textContent = `${done} / ${total} completed`;
  if (fill)  fill.style.width   = total > 0 ? `${(done / total) * 100}%` : '0%';
}

function m1SaveChecklist() {
  const states = [];
  document.querySelectorAll('.m1-chk').forEach(el => states.push(el.classList.contains('done')));
  try { localStorage.setItem(M1_STORAGE_KEY, JSON.stringify(states)); } catch (e) {}
}

function m1LoadChecklist() {
  let states = [];
  try { states = JSON.parse(localStorage.getItem(M1_STORAGE_KEY) || '[]'); } catch (e) {}
  const items = document.querySelectorAll('.m1-chk');
  items.forEach((el, i) => {
    if (states[i]) {
      el.classList.add('done');
      el.querySelector('.m1-chk-box').textContent = '✓';
    }
  });
  m1UpdateProgress();
}

// ── Init ────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  m1LoadChecklist();
});
