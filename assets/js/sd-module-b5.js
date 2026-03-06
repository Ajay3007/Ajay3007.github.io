function show(tab, el){
  document.querySelectorAll('.mb5-wrap .view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.mb5-wrap .nt').forEach(t => t.classList.remove('active'));
  document.getElementById('view-' + tab).classList.add('active');
  if (el) el.classList.add('active');
}

function tt(hd){
  const bd = hd.nextElementSibling;
  const arr = hd.querySelector('.t-arr');
  bd.classList.toggle('open', !bd.classList.contains('open'));
  arr.classList.toggle('open', !arr.classList.contains('open'));
}

function tick(el){
  el.classList.toggle('done');
  el.querySelector('.chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  const total = document.querySelectorAll('.mb5-wrap .chk').length;
  const done = document.querySelectorAll('.mb5-wrap .chk.done').length;
  document.getElementById('prog-lbl').textContent = `${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width = `${(done / total) * 100}%`;
}
