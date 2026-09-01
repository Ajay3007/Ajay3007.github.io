// Interactive Logic for Module A3 (Structural Patterns)

const m3Colours = ['var(--c1)','var(--c2)','var(--c3)','var(--c4)','var(--c5)','var(--c6)','var(--c7)'];
const CHK_STORAGE_KEY_A3 = 'ajdevhub_m3_checklist';

function m3Show(tab, el) {
  document.querySelectorAll('.m3-view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.m3-nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('m3-view-' + tab).classList.add('active');
  if (el) {
    el.classList.add('active');
  }
}

function m3SelPat(i) {
  document.querySelectorAll('.m3-ps-btn').forEach((b,j) => {
    b.classList.toggle('active', i===j);
    if (i===j) {
        b.style.background = 'var(--ink)';
        b.style.color = 'var(--paper)';
    } else {
        b.style.background = 'var(--paper)';
        b.style.color = 'var(--muted)';
    }
  });
  document.querySelectorAll('.m3-pat-panel').forEach((p,j) => p.classList.toggle('active', i===j));
}

function m3GoToPattern(i) {
  m3Show('patterns', document.querySelectorAll('.m3-nav-tab')[1]);
  m3SelPat(i);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function m3ToggleTask(hd) {
  const bd = hd.nextElementSibling;
  const arr = hd.querySelector('.m3-t-arr');
  const open = bd.classList.contains('open');
  bd.classList.toggle('open', !open);
  arr.classList.toggle('open', !open);
}

function m3Tick(el) {
  el.classList.toggle('done');
  el.querySelector('.m3-chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  m3UpdateProgress();
  m3SaveChecklist();
}

function m3UpdateProgress() {
  const chks = document.querySelectorAll('.m3-chk');
  if (chks.length === 0) return;
  
  const total = chks.length;
  const done = document.querySelectorAll('.m3-chk.done').length;
  
  const lbl = document.getElementById('m3-prog-lbl');
  if(lbl) lbl.textContent = `${done} / ${total} completed`;
  
  const fill = document.getElementById('m3-prog-fill');
  if(fill) fill.style.width = `${(done/total)*100}%`;
}

function m3SaveChecklist() {
  const chks = document.querySelectorAll('.m3-chk');
  const state = Array.from(chks).map(c => c.classList.contains('done'));
  localStorage.setItem(CHK_STORAGE_KEY_A3, JSON.stringify(state));
}

function m3LoadChecklist() {
  const saved = localStorage.getItem(CHK_STORAGE_KEY_A3);
  if (saved) {
    const state = JSON.parse(saved);
    const chks = document.querySelectorAll('.m3-chk');
    chks.forEach((c, i) => {
      if (state[i]) {
        c.classList.add('done');
        const box = c.querySelector('.m3-chk-box');
        if(box) box.textContent = '✓';
      }
    });
    m3UpdateProgress();
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  m3LoadChecklist();
  m3UpdateProgress();
});
