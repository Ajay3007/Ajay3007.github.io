document.addEventListener('DOMContentLoaded', () => {
    // Attach checklist to local storage if desired, but for now just initializing UI state
    const tot = document.querySelectorAll("#cl li").length;
    const done = document.querySelectorAll("#cl li.done").length;
    if (document.getElementById("pfill")) {
        const p = Math.round(done/tot*100);
        document.getElementById("pfill").style.width = p + "%";
        document.getElementById("ptxt").textContent = done + " / " + tot + " complete";
    }
});

function show(id, el) {
  document.querySelectorAll(".sec").forEach(s => s.classList.remove("active"));
  document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
  document.getElementById("s-"+id).classList.add("active");
  el.classList.add("active");
}

function chk(li) {
  li.classList.toggle("done");
  li.querySelector(".chk").innerHTML = li.classList.contains("done") ? "&#10003;" : "";
  const tot = document.querySelectorAll("#cl li").length;
  const done = document.querySelectorAll("#cl li.done").length;
  const p = Math.round(done/tot*100);
  document.getElementById("pfill").style.width = p + "%";
  document.getElementById("ptxt").textContent = done + " / " + tot + " complete";
}

function fmt(n) {
  if(n>=1e15) return (n/1e15).toFixed(1)+" PB";
  if(n>=1e12) return (n/1e12).toFixed(1)+" TB";
  if(n>=1e9) return (n/1e9).toFixed(1)+" GB";
  if(n>=1e6) return (n/1e6).toFixed(1)+" MB";
  if(n>=1e3) return (n/1e3).toFixed(1)+" KB";
  return n.toFixed(0)+" B";
}

function fmtq(n) {
  if(n>=1e6) return (n/1e6).toFixed(1)+"M QPS";
  if(n>=1e3) return (n/1e3).toFixed(0)+"K QPS";
  return n.toFixed(0)+" QPS";
}

function calc() {
  const dau=parseFloat(document.getElementById("dau").value)||0;
  const wpd=parseFloat(document.getElementById("wpd").value)||0;
  const rpd=parseFloat(document.getElementById("rpd").value)||0;
  const ws=parseFloat(document.getElementById("ws").value)||0;
  const rs=parseFloat(document.getElementById("rs").value)||0;
  const yr=parseFloat(document.getElementById("yr").value)||5;
  
  const wqps=dau*wpd/86400, rqps=dau*rpd/86400;
  const pqps=(wqps+rqps)*3;
  const sd=dau*wpd*ws, sy=sd*365*yr;
  const bwi=sd/86400, bwo=rqps*rs;
  
  document.getElementById("rgrid").innerHTML=[
    ["WRITE QPS",fmtq(wqps)],["READ QPS",fmtq(rqps)],["PEAK QPS",fmtq(pqps)],
    ["STORAGE/DAY",fmt(sd)],["STORAGE/"+yr+"YR",fmt(sy)],
    ["BANDWIDTH IN",fmt(bwi)+"/s"],["BANDWIDTH OUT",fmt(bwo)+"/s"]
  ].map(([l,v])=>`<div class="res-card"><div class="res-lbl">${l}</div><div class="res-val">${v}</div></div>`).join("");
  
  const tips=[];
  if(sy>1e15) tips.push("&#128230; "+fmt(sy)+" storage &rarr; Object store (S3) mandatory.");
  if(rqps>50000) tips.push("&#9889; "+fmtq(rqps)+" read QPS &rarr; Multi-layer caching required.");
  if(bwo>1e9) tips.push("&#127760; "+fmt(bwo)+"/s outgoing &rarr; CDN is mandatory.");
  if(wqps>10000) tips.push("&#9999; "+fmtq(wqps)+" write QPS &rarr; Queue-based async ingestion needed.");
  if(rqps/wqps>10) tips.push("&#128214; Read:Write "+Math.round(rqps/wqps)+":1 &rarr; Read-optimized architecture needed.");
  if(!tips.length) tips.push("&#9989; Modest scale &mdash; single region, single DB, simple cache sufficient.");
  
  document.getElementById("impl").innerHTML="<div class='card-label' style='margin-bottom:12px'>Design Implications</div>"+tips.map(t=>`<div class="tip" style="margin-bottom:8px"><span class="tip-n">&rarr;</span>${t}</div>`).join("");
  document.getElementById("cres").style.display="block";
}
