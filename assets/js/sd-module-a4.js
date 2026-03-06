// Interactive Logic for Module A4 (Behavioral Patterns)

const CHK_STORAGE_KEY_A4 = 'ajdevhub_m4_checklist';

function m4Show(tab, el) {
  document.querySelectorAll('.m4-view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.m4-nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('m4-view-' + tab).classList.add('active');
  if(el) el.classList.add('active');
}

function m4SelPat(i) {
  document.querySelectorAll('.m4-pt-btn').forEach((b, j) => {
    b.classList.toggle('active', i === j);
    if(i === j) {
       b.style.borderColor = `var(--p${i+1})`;
       b.style.color = `var(--p${i+1})`;
    } else {
       b.style.borderColor = 'var(--border)';
       b.style.color = 'var(--muted)';
    }
  });
  document.querySelectorAll('.m4-pat-panel').forEach((p, j) => {
    p.classList.toggle('active', i === j);
  });
}

function m4GoToPattern(i) {
  m4Show('patterns', document.querySelectorAll('.m4-nav-tab')[1]);
  m4SelPat(i);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function m4ToggleTask(hd) {
  const bd = hd.nextElementSibling;
  const arr = hd.querySelector('.m4-t-arr');
  const open = bd.classList.contains('open');
  bd.classList.toggle('open', !open);
  arr.classList.toggle('open', !open);
}

function m4Tick(el) {
  el.classList.toggle('done');
  m4UpdateProgress();
  m4SaveChecklist();
}

function m4UpdateProgress() {
  const chks = document.querySelectorAll('.m4-chk');
  if (chks.length === 0) return;
  
  const total = chks.length;
  const done = document.querySelectorAll('.m4-chk.done').length;
  
  const lbl = document.getElementById('m4-prog-lbl');
  if(lbl) lbl.textContent = `${done} / ${total} completed`;
  
  const fill = document.getElementById('m4-prog-fill');
  if(fill) fill.style.width = `${(done/total)*100}%`;
}

function m4SaveChecklist() {
  const chks = document.querySelectorAll('.m4-chk');
  const state = Array.from(chks).map(c => c.classList.contains('done'));
  localStorage.setItem(CHK_STORAGE_KEY_A4, JSON.stringify(state));
}

function m4LoadChecklist() {
  const saved = localStorage.getItem(CHK_STORAGE_KEY_A4);
  if (saved) {
    const state = JSON.parse(saved);
    const chks = document.querySelectorAll('.m4-chk');
    chks.forEach((c, i) => {
      if (state[i]) {
        c.classList.add('done');
      }
    });
    m4UpdateProgress();
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  m4LoadChecklist();
  m4UpdateProgress();
});
