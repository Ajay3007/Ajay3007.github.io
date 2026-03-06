document.addEventListener('DOMContentLoaded', () => {
    // Initialise checklist from localStorage
    m2LoadChecklist();
});

function m2Show(tab, el) {
  document.querySelectorAll('.m2-view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.m2-nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('m2-view-' + tab).classList.add('active');
  el.classList.add('active');
}

function m2SelPat(p, el) {
  document.querySelectorAll('.m2-pat-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.m2-pat-panel').forEach(pan => pan.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('m2-pat-' + p).classList.add('active');
}

function m2GoToPattern(p) {
  m2Show('patterns', document.querySelectorAll('.m2-nav-tab')[1]);
  m2SelPat(p, document.querySelector('.m2-pat-btn.' + p));
}

function m2ToggleTask(hd) {
  const bd = hd.nextElementSibling;
  const arr = hd.querySelector('.m2-t-arr');
  const open = bd.classList.contains('open');
  bd.classList.toggle('open', !open);
  arr.classList.toggle('open', !open);
}

function m2Tick(el) {
  el.classList.toggle('done');
  el.querySelector('.m2-chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  m2UpdateProgress();
  m2SaveChecklist();
}

function m2UpdateProgress() {
    const total = document.querySelectorAll('.m2-chk').length;
    const done  = document.querySelectorAll('.m2-chk.done').length;
    
    const progLbl = document.getElementById('m2-prog-lbl');
    const progFill = document.getElementById('m2-prog-fill');
    
    if (progLbl) progLbl.textContent = `${done} / ${total} completed`;
    if (progFill) progFill.style.width = `${(done/total)*100}%`;
}

function m2SaveChecklist() {
    const items = document.querySelectorAll('.m2-chk');
    const state = Array.from(items).map(item => item.classList.contains('done'));
    localStorage.setItem('ajdev_m2_checklist', JSON.stringify(state));
}

function m2LoadChecklist() {
    const saved = localStorage.getItem('ajdev_m2_checklist');
    if (saved) {
        const state = JSON.parse(saved);
        const items = document.querySelectorAll('.m2-chk');
        
        items.forEach((item, index) => {
            if (state[index]) {
                item.classList.add('done');
                item.querySelector('.m2-chk-box').textContent = '✓';
            }
        });
    }
    m2UpdateProgress();
}
