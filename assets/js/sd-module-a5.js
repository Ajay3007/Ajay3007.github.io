function show(tab, el) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('view-' + tab).classList.add('active');
  el.classList.add('active');
}

function tt(hd) {
  const bd  = hd.nextElementSibling;
  const arr = hd.querySelector('.t-arr');
  const open = bd.classList.contains('open');
  bd.classList.toggle('open', !open);
  arr.classList.toggle('open', !open);
}

function tick(el) {
  el.classList.toggle('done');
  el.querySelector('.chk-box').textContent = el.classList.contains('done') ? '✓' : '';
  const total = document.querySelectorAll('.chk').length;
  const done  = document.querySelectorAll('.chk.done').length;
  document.getElementById('prog-lbl').textContent = `${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width = `${(done/total)*100}%`;
}

// Animated thread counter
let counts = [0, 0, 0];
function animateCounts() {
  counts = counts.map((c, i) => {
    const delta = Math.floor(Math.random() * 3);
    return Math.min(1000, c + delta);
  });
  document.getElementById('tv1').textContent = counts[0];
  document.getElementById('tv2').textContent = counts[1];
  document.getElementById('tv3').textContent = counts[2];
}
setInterval(animateCounts, 400);