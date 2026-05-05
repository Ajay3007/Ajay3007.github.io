// Animated packet flowing across the data-plane pipeline.
// Resolution-independent; respects prefers-reduced-motion.
(function () {
  const canvas = document.getElementById('packet-pipeline');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let dpr = window.devicePixelRatio || 1;
  let cssW = 0, cssH = 0;

  function resize() {
    const rect = canvas.getBoundingClientRect();
    cssW = rect.width; cssH = rect.height;
    canvas.width  = Math.floor(cssW * dpr);
    canvas.height = Math.floor(cssH * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  const ACCENT = '#22d3ee';
  const FAINT  = '#2a3142';

  let t0 = performance.now();
  const PERIOD = 3600; // ms per traverse
  const TRAIL  = 6;

  function frame(now) {
    const w = cssW, h = cssH;
    if (!w || !h) { requestAnimationFrame(frame); return; }
    const cy = h / 2;
    const x0 = w * 0.06, x1 = w * 0.94;

    ctx.clearRect(0, 0, w, h);

    // Track (dashed)
    ctx.strokeStyle = FAINT;
    ctx.lineWidth = 1;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(x0, cy);
    ctx.lineTo(x1, cy);
    ctx.stroke();
    ctx.setLineDash([]);

    // Packet position (eased ping-pong)
    const phase = ((now - t0) % PERIOD) / PERIOD;
    const tri = phase < 0.5 ? phase * 2 : (1 - phase) * 2; // 0..1..0
    const eased = tri * tri * (3 - 2 * tri); // smoothstep
    const px = x0 + (x1 - x0) * eased;

    // Trail
    for (let i = TRAIL; i >= 1; i--) {
      const back = px - (i * 8);
      if (back < x0) continue;
      ctx.fillStyle = ACCENT;
      ctx.globalAlpha = (TRAIL - i + 1) / (TRAIL * 3);
      ctx.beginPath();
      ctx.arc(back, cy, 3, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;

    // Glow
    ctx.fillStyle = ACCENT;
    ctx.shadowColor = ACCENT;
    ctx.shadowBlur = 10;
    ctx.beginPath();
    ctx.arc(px, cy, 4.5, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    if (!reduce) requestAnimationFrame(frame);
  }

  resize();
  window.addEventListener('resize', resize);
  if (reduce) {
    // Draw a single static frame mid-pipeline.
    t0 = performance.now() - PERIOD / 4;
    frame(performance.now());
  } else {
    requestAnimationFrame(frame);
  }
})();
