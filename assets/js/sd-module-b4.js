/* JS for System Design Module B4 (Message Queues) */
function mb4Show(tab, el) {
  document.querySelectorAll('.mb4-view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.mb4-nt').forEach(t => t.classList.remove('active'));
  document.getElementById('view-' + tab).classList.add('active');
  el.classList.add('active');
}

function mb4ToggleTask(hd) {
  const bd = hd.nextElementSibling;
  const arr = hd.querySelector('.mb4-t-arr');
  bd.classList.toggle('open');
  arr.classList.toggle('open');
}

function mb4Tick(el) {
  el.classList.toggle('done');
  el.querySelector('.mb4-chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  const total = document.querySelectorAll('.mb4-chk').length;
  const done = document.querySelectorAll('.mb4-chk.done').length;
  document.getElementById('prog-lbl').textContent = `${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width = `${(done / total) * 100}%`;
}
