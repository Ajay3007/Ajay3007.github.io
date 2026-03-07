function mb13_show(tab,el){
  document.querySelectorAll('.sd-module-b13 .view').forEach(v=>v.classList.remove('active'));
  document.querySelectorAll('.sd-module-b13 .nt').forEach(t=>t.classList.remove('active'));
  document.getElementById('view-'+tab).classList.add('active');
  el.classList.add('active');
}
function mb13_qa(hd){
  const bd=hd.nextElementSibling,arr=hd.querySelector('.qa-arr');
  bd.classList.toggle('open',!bd.classList.contains('open'));
  arr.classList.toggle('open',!arr.classList.contains('open'));
}
function mb13_tick(el){
  el.classList.toggle('done');
  el.querySelector('.chk-box').textContent=el.classList.contains('done')?'✓':'';
  const total=document.querySelectorAll('.sd-module-b13 .chk').length;
  const done=document.querySelectorAll('.sd-module-b13 .chk.done').length;
  document.getElementById('prog-lbl').textContent=`${done} / ${total} completed`;
  document.getElementById('prog-fill').style.width=`${(done/total)*100}%`;
}
