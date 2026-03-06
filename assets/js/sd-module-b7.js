function mb7_show(tab,el){
  document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
  document.querySelectorAll('.nt').forEach(t=>t.classList.remove('active'));
  document.getElementById('view-'+tab).classList.add('active');
  el.classList.add('active');
}
function mb7_tt(hd){
  const bd=hd.nextElementSibling,arr=hd.querySelector('.t-arr');
  bd.classList.toggle('open',!bd.classList.contains('open'));
  arr.classList.toggle('open',!arr.classList.contains('open'));
}
function mb7_tick(el){
  el.classList.toggle('done');
  el.querySelector('.chk-box').textContent=el.classList.contains('done')?'✓':'';
  const total=document.querySelectorAll('.chk').length;
  const done=document.querySelectorAll('.chk.done').length;
  document.getElementById('prog-lbl').textContent=`${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width=`${(done/total)*100}%`;
}