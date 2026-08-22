---
title: "Module B8: YouTube"
description: "SYSTEM DESIGN MASTERY · TRACK B · MODULE B8 · WEEK 18 VIDEO PLATFORM · TRANSCODING · CDN · PETABYTE STORAGE Case Study No."
domain: system-design
track: system-design-hld
order: 116
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-b8-youtube/
---

<link rel="stylesheet" href="/assets/css/sd-module-b8.css">
<div class="sd-module-b8">
<header>
  <div class="hdr-stripe"></div>
  <div class="hdr-top">
    <span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B8 · WEEK 18</span>
    <span>VIDEO PLATFORM · TRANSCODING · CDN · PETABYTE STORAGE</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-pill">Case Study No. 4 · Video Upload Pipeline · HLS Streaming</div>
      <h1>DESIGN<br><span class="acc">YOU</span>TUBE</h1>
      <div class="hdr-sub">TRANSCODING · HLS ADAPTIVE BITRATE · 3-TIER CDN<br>VIEW COUNTER · OBJECT STORAGE · ELASTICSEARCH</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">500hrs</div><div class="hs-l">UPLOAD/MIN</div></div>
      <div class="hs"><div class="hs-v">1B hrs</div><div class="hs-l">WATCHED/DAY</div></div>
      <div class="hs"><div class="hs-v">58Tbps</div><div class="hs-l">CDN BANDWIDTH</div></div>
      <div class="hs"><div class="hs-v">B8</div><div class="hs-l">MODULE</div></div>
    </div>
  </div>
  <div class="tag-row">
    <div class="tg" style="color:var(--red)">Chunked Upload</div>
    <div class="tg" style="color:var(--ora)">Transcoding</div>
    <div class="tg" style="color:var(--yel)">HLS / ABR</div>
    <div class="tg" style="color:var(--grn)">3-Tier CDN</div>
    <div class="tg" style="color:var(--blu)">View Counter</div>
    <div class="tg" style="color:var(--red)">Elasticsearch</div>
    <div class="tg" style="color:var(--ora)">Object Storage</div>
  </div>
</header>
<nav class="nav">
  <div class="nt active" onclick="mb8_show('req',this)">Requirements</div>
  <div class="nt" onclick="mb8_show('est',this)">Estimation</div>
  <div class="nt" onclick="mb8_show('arch',this)">Architecture</div>
  <div class="nt" onclick="mb8_show('upload',this)">Upload Pipeline</div>
  <div class="nt" onclick="mb8_show('transcode',this)">Transcoding</div>
  <div class="nt" onclick="mb8_show('hls',this)">HLS Streaming</div>
  <div class="nt" onclick="mb8_show('cdn',this)">CDN</div>
  <div class="nt" onclick="mb8_show('views',this)">View Counter</div>
  <div class="nt" onclick="mb8_show('storage',this)">Storage &amp; Search</div>
  <div class="nt" onclick="mb8_show('tasks',this)">Tasks</div>
  <div class="nt" onclick="mb8_show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- REQUIREMENTS -->
<div class="view active" id="view-req">
  <div class="sh">Requirements</div>
  <div class="sr">Scope the system — what we build, what we don't</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0">
    <div style="background:var(--panel);border:1px solid var(--bord2);border-left:2px solid var(--red);padding:16px">
      <div style="font-family:'Anton',sans-serif;font-size:16px;letter-spacing:0.5px;color:var(--white);margin-bottom:10px">Functional</div>
      <div style="font-family:'DM Mono',monospace;font-size:10px;color:var(--muted);line-height:2.2">
        Upload video (raw file → processed variants)<br>
        Stream video (adaptive bitrate, no buffering)<br>
        Search by title, description, tags<br>
        View count (real-time approximate)<br>
        Like / dislike / comment<br>
        Subscribe + notifications on new uploads<br><br>
        <span style="color:var(--aged)">OUT OF SCOPE: live streaming, ads, ML recommendations</span>
      </div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-left:2px solid var(--ora);padding:16px">
      <div style="font-family:'Anton',sans-serif;font-size:16px;letter-spacing:0.5px;color:var(--white);margin-bottom:10px">Non-Functional</div>
      <div style="font-family:'DM Mono',monospace;font-size:10px;color:var(--muted);line-height:2.2">
        2B users/month, 800M DAU<br>
        500 hrs video uploaded every minute<br>
        1 billion hours watched daily<br>
        Video start: p99 &lt; 2 seconds<br>
        Upload processing: &lt; 5 min for 10-min video<br>
        Read:write ≈ 200:1<br>
        Durability: videos never lost (multi-replica)
      </div>
    </div>
  </div>
  <div class="al red"><em>The key constraint:</em> Read:write is 200:1. Every architecture decision optimises for low-latency video delivery, not upload speed. The entire CDN and HLS strategy exists to serve this ratio.</div>
</div>
<!-- ESTIMATION -->
<div class="view" id="view-est">
  <div class="sh">Capacity Estimation</div>
  <div class="sr">Numbers that anchor every infrastructure decision</div>
  <table class="est-t">
    <thead><tr><th>METRIC</th><th>VALUE</th><th>CALCULATION</th></tr></thead>
    <tbody>
      <tr><td>Upload rate</td><td>8.3 hrs/sec</td><td>500 hrs/min ÷ 60</td></tr>
      <tr><td>Raw upload bandwidth</td><td>~16.6 GB/sec</td><td>8.3 hrs/sec × 2 GB/hr (1080p raw)</td></tr>
      <tr><td>Processed variants per video</td><td>6 resolutions</td><td>360p, 480p, 720p, 1080p, 1440p, 4K</td></tr>
      <tr><td>Processed storage per uploaded hr</td><td>~3 GB</td><td>6 × 500 MB avg per variant per hour</td></tr>
      <tr><td>New video storage/day</td><td>90 TB/day</td><td>500 hrs/min × 60 min × 3 GB</td></tr>
      <tr><td>New video storage/year</td><td>~33 PB/year</td><td>90 TB × 365</td></tr>
      <tr><td>Total YouTube storage</td><td>~1 exabyte</td><td>15+ years of uploads accumulated</td></tr>
      <tr><td>Watch throughput</td><td>11.6M hrs/sec</td><td>1B hrs/day ÷ 86,400</td></tr>
      <tr><td>CDN bandwidth required</td><td>~58 Tbps</td><td>11.6M hrs/sec × 5 Mbps (1080p)</td></tr>
    </tbody>
  </table>
  <div class="al yel"><em>Say aloud:</em> "58 Tbps of CDN bandwidth. This is why YouTube has 1,000+ edge PoPs globally — no single datacenter could serve this. The CDN IS the product."</div>
</div>
<!-- ARCHITECTURE -->
<div class="view" id="view-arch">
  <div class="sh">High-Level Architecture</div>
  <div class="sr">Upload path (write-heavy) vs Stream path (read-heavy)</div>
  <div class="pipeline">
    <div class="pl-label">// UPLOAD PATH</div>
    <div class="pl-step"><div class="pl-n">1.</div><div class="pl-node">[Client]</div><div class="pl-body">chunked upload → <span style="color:var(--white)">[Upload Service]</span> → raw file in <span style="color:var(--white)">[GCS/S3]</span></div></div>
    <div class="pl-step"><div class="pl-n">2.</div><div class="pl-node">[Upload Service]</div><div class="pl-body">publishes "video-uploaded" to <span style="color:var(--white)">[Kafka]</span></div></div>
    <div class="pl-step"><div class="pl-n">3.</div><div class="pl-node">[Kafka]</div><div class="pl-body">consumed by <span style="color:var(--white)">[Transcoding Workers]</span> — K8s autoscaled pool</div></div>
    <div class="pl-step"><div class="pl-n">4.</div><div class="pl-node">[Transcoding]</div><div class="pl-body">parallel workers per resolution + temporal segmentation → <span style="color:var(--yel)">.ts segments + .m3u8 manifest</span></div></div>
    <div class="pl-step"><div class="pl-n">5.</div><div class="pl-node">[Processed Files]</div><div class="pl-body">pushed to <span style="color:var(--white)">[GCS/S3]</span>, pre-warmed to <span style="color:var(--white)">[CDN edge nodes]</span></div></div>
    <div class="pl-step"><div class="pl-n">6.</div><div class="pl-node">[Metadata DB]</div><div class="pl-body">status updated: "processing" → "published"</div></div>
  </div>
  <div class="pipeline" style="margin-top:8px">
    <div class="pl-label">// STREAM PATH (p99 &lt; 2s start time)</div>
    <div class="pl-step"><div class="pl-n">1.</div><div class="pl-node">[Client]</div><div class="pl-body">GET /watch?v=abc123 → <span style="color:var(--white)">[Video Service]</span> returns master .m3u8 URL</div></div>
    <div class="pl-step"><div class="pl-n">2.</div><div class="pl-node">[Client]</div><div class="pl-body">fetches master.m3u8 from <span style="color:var(--white)">[CDN Edge PoP]</span> nearest to user (~5ms)</div></div>
    <div class="pl-step"><div class="pl-n">3.</div><div class="pl-node">[Player]</div><div class="pl-body">measures bandwidth → selects quality → fetches quality variant .m3u8</div></div>
    <div class="pl-step"><div class="pl-n">4.</div><div class="pl-node">[Player]</div><div class="pl-body">fetches first 3 segments (.ts files) from CDN → starts playback</div></div>
    <div class="pl-step"><div class="pl-n">5.</div><div class="pl-node">[Player]</div><div class="pl-body">continuously fetches next segments; switches quality as bandwidth changes</div></div>
  </div>
</div>
<!-- UPLOAD PIPELINE -->
<div class="view" id="view-upload">
  <div class="sh">Upload Pipeline</div>
  <div class="sr">Chunked resumable upload — resilient to network failures</div>
  <div class="cb"><div class="cb-top">Resumable upload protocol<span class="cb-l">HTTP</span></div>
<pre class="c"><span class="cm">// Step 1: Client initiates upload session</span>
POST /upload/initiate
Body: <span class="str">{"filename": "video.mp4", "size": 2147483648, "sha256": "abc123..."}</span>
Response: <span class="str">{"uploadId": "up_xyz", "chunkSize": 5242880}</span>  <span class="cm">← 5 MB chunks</span>
<span class="cm">// Step 2: Client checks for dedup (same SHA-256 already exists)</span>
POST /upload/check?hash=abc123
Response: <span class="str">{"exists": false}</span>  <span class="cm">← proceed with upload</span>
<span class="cm">// If exists: {"exists": true, "videoId": "abc123"} → DONE, no upload needed!</span>
<span class="cm">// Step 3: Upload chunks (can be parallelised)</span>
PUT /upload/up_xyz/chunk/0  Body: [bytes 0–5MB]       → <span class="ok">200 OK</span>
PUT /upload/up_xyz/chunk/1  Body: [bytes 5MB–10MB]    → <span class="ok">200 OK</span>
PUT /upload/up_xyz/chunk/2  Body: [bytes 10MB–15MB]   → <span class="er">500 (network drop)</span>
<span class="cm">// Step 4: Resume from last successful chunk</span>
GET /upload/up_xyz/status   → <span class="str">{"lastChunk": 1}</span>
PUT /upload/up_xyz/chunk/2  Body: [bytes 10MB–15MB]   → <span class="ok">200 OK</span>  <span class="cm">← retry</span>
<span class="cm">// Step 5: Finalize — triggers transcoding pipeline</span>
POST /upload/up_xyz/complete → <span class="str">{"videoId": "abc456", "status": "processing"}</span></pre>
  </div>
  <div class="al grn"><em>Deduplication win:</em> By checking SHA-256 before upload, re-uploaded content (same video uploaded twice by different users) is caught immediately. Saves both upload bandwidth and transcoding compute. YouTube uses this for copyright detection too.</div>
</div>
<!-- TRANSCODING -->
<div class="view" id="view-transcode">
  <div class="sh">Transcoding Pipeline</div>
  <div class="sr">Converting raw upload to streamable HLS segments — the most compute-intensive step</div>
  <div class="sh" style="font-size:16px;margin-top:14px">Parallelism Strategy</div>
  <div class="cb"><div class="cb-top">Temporal parallelism — split video into 1-min segments, transcode in parallel<span class="cb-l">ARCHITECTURE</span></div>
<pre class="c"><span class="cm">// Naive: one worker transcodes full 60-minute video</span>
<span class="cm">// 60-min video at 1x realtime = 60 min transcoding time ← too slow</span>
<span class="cm">// YouTube's approach: temporal parallelism</span>
<span class="cm">// 1. Split raw video into 1-minute segments</span>
60-minute video → <span class="or">60 × 1-minute segments</span>
<span class="cm">// 2. Dispatch each segment to a separate worker (60 workers)</span>
<span class="hl">Worker 01:</span> segment_01 → transcode to all 6 quality levels
<span class="hl">Worker 02:</span> segment_02 → transcode to all 6 quality levels
<span class="hl">Worker 03:</span> segment_03 → transcode to all 6 quality levels
...
<span class="hl">Worker 60:</span> segment_60 → transcode to all 6 quality levels
 
<span class="cm">// 3. All workers run simultaneously → done in ~1 minute (60× speedup)</span>
<span class="cm">// 4. Concatenate segments → complete HLS playlist per quality level</span>
<span class="cm">// Per-resolution breakdown (for each segment):</span>
Worker A: 360p  (fast — ~5 sec/segment)   ← first available, serve to poor connections immediately
Worker B: 480p  (~8 sec/segment)
Worker C: 720p  (~15 sec/segment)
Worker D: 1080p (~25 sec/segment)
Worker E: 1440p (~40 sec/segment)
Worker F: 4K    (~60 sec/segment)</pre>
  </div>
  <div class="sh" style="font-size:16px;margin-top:14px">Codec Trade-offs</div>
  <div class="codec-grid">
    <div class="cdc" style="border-top-color:var(--yel)">
      <div class="cdc-name" style="color:var(--yel)">H.264 (AVC)</div>
      <div class="cdc-sub">UNIVERSAL COMPAT</div>
      <div class="cdc-body">Every browser, device, smart TV supports it. Higher file size than VP9/AV1.</div>
      <div class="cdc-use" style="color:var(--yel)">Use: default fallback<br>All non-Chrome clients<br>Smart TVs, older devices</div>
    </div>
    <div class="cdc" style="border-top-color:var(--red)">
      <div class="cdc-name" style="color:var(--red)">VP9</div>
      <div class="cdc-sub">30-50% SMALLER THAN H.264</div>
      <div class="cdc-body">Google's codec. Excellent quality at lower bitrate. Native Chrome support (YouTube's primary client).</div>
      <div class="cdc-use" style="color:var(--red)">Use: Chrome browsers<br>YouTube default on web<br>Android devices</div>
    </div>
    <div class="cdc" style="border-top-color:var(--grn)">
      <div class="cdc-name" style="color:var(--grn)">AV1</div>
      <div class="cdc-sub">NEXT-GEN — 50% SMALLER</div>
      <div class="cdc-body">Best quality:size ratio. CPU-intensive to decode (hardware accel needed). Future default.</div>
      <div class="cdc-use" style="color:var(--grn)">Use: flagship devices<br>4K/8K content<br>Low-bandwidth markets</div>
    </div>
  </div>
  <div class="al yel"><em>In practice:</em> YouTube encodes both H.264 AND VP9 for every video. Client sends Accept-Encoding header → server delivers VP9 to Chrome, H.264 to everything else. Doubles storage cost but dramatically reduces CDN bandwidth (VP9 saves 30-50% per stream).</div>
</div>
<!-- HLS STREAMING -->
<div class="view" id="view-hls">
  <div class="sh">HLS Adaptive Bitrate Streaming</div>
  <div class="sr">How the player automatically adjusts quality without buffering</div>
  <div class="hls-box">
    <div class="hls-label">// HLS FILE STRUCTURE — one video, multiple quality levels</div>
    <div class="hls-row">
      <div class="hls-quality" style="border-color:var(--red);color:var(--red)">master.m3u8</div>
      <div class="hls-arrow">→</div>
      <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--muted)">lists all quality variants with bandwidth info</div>
    </div>
    <div class="hls-row">
      <div style="width:90px"></div>
      <div class="hls-quality" style="border-color:var(--muted)">360p.m3u8</div>
      <div class="hls-arrow">→</div>
      <div class="hls-seg">seg_001.ts</div>
      <div class="hls-seg">seg_002.ts</div>
      <div class="hls-seg">seg_003.ts</div>
      <div class="hls-seg">... (2s each)</div>
    </div>
    <div class="hls-row">
      <div style="width:90px"></div>
      <div class="hls-quality" style="border-color:var(--ora)">720p.m3u8</div>
      <div class="hls-arrow">→</div>
      <div class="hls-seg">seg_001.ts</div>
      <div class="hls-seg">seg_002.ts</div>
      <div class="hls-seg">seg_003.ts</div>
      <div class="hls-seg">...</div>
    </div>
    <div class="hls-row">
      <div style="width:90px"></div>
      <div class="hls-quality" style="border-color:var(--yel)">1080p.m3u8</div>
      <div class="hls-arrow">→</div>
      <div class="hls-seg">seg_001.ts</div>
      <div class="hls-seg">seg_002.ts</div>
      <div class="hls-seg">seg_003.ts</div>
      <div class="hls-seg">...</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">master.m3u8 — what the player downloads first<span class="cb-l">HLS MANIFEST</span></div>
<pre class="c">#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=640x360
<span class="str">https://cdn.youtube.com/v/abc123/360p.m3u8</span>
 
#EXT-X-STREAM-INF:BANDWIDTH=2500000,RESOLUTION=1280x720
<span class="str">https://cdn.youtube.com/v/abc123/720p.m3u8</span>
 
#EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080
<span class="str">https://cdn.youtube.com/v/abc123/1080p.m3u8</span>
<span class="cm"># Player logic (every 2 seconds):</span>
<span class="cm"># measured bandwidth > 5 Mbps  → switch to 1080p</span>
<span class="cm"># measured bandwidth 2.5–5 Mbps → switch to 720p</span>
<span class="cm"># measured bandwidth < 500 Kbps  → switch to 360p</span>
<span class="cm"># Switches happen at segment boundaries → no buffering</span></pre>
  </div>
  <div class="al grn"><em>Why segments?</em> Each .ts file is 2–10 seconds of independent video. The player can switch quality between segments — it doesn't need to re-buffer the current segment. This is what enables seamless quality switching as your network changes.</div>
</div>
<!-- CDN -->
<div class="view" id="view-cdn">
  <div class="sh">3-Tier CDN Architecture</div>
  <div class="sr">58 Tbps served globally — the CDN IS the product</div>
  <div class="cdn-tiers">
    <div class="cdn-tier" style="border-left-color:var(--red)">
      <div class="ct-name">Edge PoPs</div>
      <div class="ct-desc">1,000+ nodes globally. Within 20ms of every major city. Hot content only (top 10% of videos = 90% of views). 10–100 TB storage each.</div>
      <div class="ct-lat" style="color:var(--red)">~5–20ms</div>
      <div class="ct-hit">~80% hit</div>
    </div>
    <div class="cdn-tier" style="border-left-color:var(--ora)">
      <div class="ct-name">Regional Cache</div>
      <div class="ct-desc">~100 nodes. Inter-regional. Warm content missed at edge. ~1 PB storage per node. Backed by higher-capacity hardware.</div>
      <div class="ct-lat" style="color:var(--ora)">~30–60ms</div>
      <div class="ct-hit">~15% hit</div>
    </div>
    <div class="cdn-tier" style="border-left-color:var(--muted)">
      <div class="ct-name">Origin (GCS/S3)</div>
      <div class="ct-desc">Source of truth. Only ~5% of traffic reaches here. Multi-region replication. Exabyte-scale object storage.</div>
      <div class="ct-lat" style="color:var(--muted)">~100–200ms</div>
      <div class="ct-hit">~5% miss</div>
    </div>
  </div>
  <div class="sh" style="font-size:16px;margin-top:18px">CDN Pre-Warming Strategy</div>
  <div class="cb"><div class="cb-top">Push popular content to edges before users request it<span class="cb-l">STRATEGY</span></div>
<pre class="c"><span class="cm">// New video uploaded by channel with 10M subscribers:</span>
<span class="cm">// Don't wait for cache misses — proactively push to edges</span>
<span class="cm">// Tier 1: Subscriber count-based pre-warm</span>
<span class="kw">if</span> (channel.subscriberCount > <span class="or">1_000_000</span>) {
    cdn.<span class="fn">prefetch</span>(videoUrl, tier: <span class="str">"edge"</span>, regions: <span class="str">"all"</span>);   <span class="cm">// push to all edges</span>
} <span class="kw">else if</span> (channel.subscriberCount > <span class="or">100_000</span>) {
    cdn.<span class="fn">prefetch</span>(videoUrl, tier: <span class="str">"regional"</span>);              <span class="cm">// push to regional only</span>
}
 
<span class="cm">// Tier 2: Virality-based dynamic warm (triggered by view velocity)</span>
<span class="kw">if</span> (viewVelocity > <span class="or">10_000</span> <span class="cm">// views/minute</span>) {
    cdn.<span class="fn">prefetch</span>(videoUrl, tier: <span class="str">"edge"</span>, regions: <span class="str">"all"</span>);
}
 
<span class="cm">// Pre-warm only first 5 segments (first 10–30 seconds)</span>
<span class="cm">// Reason: most users watch the start; remaining segments warmed on demand</span>
<span class="cm">// "Seek-ahead": when user is at segment N, pre-fetch N+1 to N+5</span></pre>
  </div>
</div>
<!-- VIEW COUNTER -->
<div class="view" id="view-views">
  <div class="sh">View Counter Design</div>
  <div class="sr">11,600 views/sec globally — naive DB update doesn't scale</div>
  <div class="vc-grid">
    <div class="vc" style="border-top-color:var(--ora)">
      <div class="vc-name" style="color:var(--ora)">Redis INCR</div>
      <div class="vc-sub">FAST, APPROXIMATE</div>
      <div class="vc-body">Atomic counter per video. Background job syncs to MySQL every 30s. Loses up to 30s of counts on Redis crash.</div>
      <div class="vc-cmd" style="color:var(--ora)">
        INCR view_count:{videoId}<br>
        Background: every 30s sync to DB<br>
        ✓ Fast &nbsp;&nbsp; ✗ 30s loss risk
      </div>
    </div>
    <div class="vc" style="border-top-color:var(--yel)">
      <div class="vc-name" style="color:var(--yel)">Kafka + ClickHouse</div>
      <div class="vc-sub">ACCURATE, SCALABLE</div>
      <div class="vc-body">Each view → Kafka event. ClickHouse consumer aggregates. Accurate, scalable, ~30-60s latency. Foundation for analytics.</div>
      <div class="vc-cmd" style="color:var(--yel)">
        Kafka: view_events (videoId, userId, ts)<br>
        ClickHouse: COUNT(*) per videoId<br>
        ✓ Accurate &nbsp;&nbsp; ✗ 30-60s lag
      </div>
    </div>
    <div class="vc" style="border-top-color:var(--red)">
      <div class="vc-name" style="color:var(--red)">Sharded Counters</div>
      <div class="vc-sub">FOR VIRAL VIDEOS</div>
      <div class="vc-body">Shard count across N Redis keys. INCR random shard. Read = SUM all shards. Removes hot key problem for viral content.</div>
      <div class="vc-cmd" style="color:var(--red)">
        INCR view:{videoId}:shard_{rand(N)}<br>
        READ: SUM view:{videoId}:shard_0..N<br>
        ✓ No hotkey &nbsp;&nbsp; ✗ N reads per count
      </div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Production view counter — combining all three approaches<span class="cb-l">ARCHITECTURE</span></div>
<pre class="c"><span class="cm">// On every view event:</span>
<span class="cm">// 1. INCR random Redis shard (instant, non-blocking)</span>
INCR view:<span class="str">{videoId}</span>:shard_<span class="or">{random(10)}</span>
<span class="cm">// 2. Publish to Kafka (async, doesn't block response)</span>
kafka.<span class="fn">publish</span>(<span class="str">"view-events"</span>, <span class="str">{videoId, userId, ip, timestamp, country}</span>)
 
<span class="cm">// View count displayed to user:</span>
GET /api/views/{videoId}
  → SUM MGET view:{videoId}:shard_0 ... view:{videoId}:shard_9  <span class="cm">← Redis (fast)</span>
<span class="cm">// Analytics dashboard (historical, per-country, per-hour):</span>
SELECT COUNT(*) FROM view_events WHERE video_id = X AND timestamp > T
  → ClickHouse query  <span class="cm">← accurate, supports complex aggregations</span>
<span class="cm">// Spam prevention:</span>
<span class="cm">// Check: SETNX view_dedup:{videoId}:{ip}:{hour} 1  EX 3600</span>
<span class="cm">// If key already exists → don't count this view (same IP, same hour)</span></pre>
  </div>
</div>
<!-- STORAGE & SEARCH -->
<div class="view" id="view-storage">
  <div class="sh">Storage Strategy &amp; Search</div>
  <div class="sr">Petabyte object storage + Elasticsearch for discovery</div>
  <div class="cb"><div class="cb-top">GCS/S3 object structure + lifecycle policies<span class="cb-l">OBJECT STORAGE</span></div>
<pre class="c"><span class="cm">// Storage layout:</span>
raw/<span class="str">{videoId}</span>/original.mp4                   <span class="cm">← deleted after transcoding (save cost)</span>
processed/<span class="str">{videoId}</span>/master.m3u8               <span class="cm">← HLS master playlist</span>
processed/<span class="str">{videoId}</span>/360p/seg_001.ts           <span class="cm">← 2s video segments</span>
processed/<span class="str">{videoId}</span>/1080p/seg_001.ts
thumbnails/<span class="str">{videoId}</span>/thumb_1.jpg             <span class="cm">← multiple choices for uploader</span>
<span class="cm">// Lifecycle policies (automated tiering by popularity):</span>
Hot   (&gt;100 views/month):  Standard storage + CDN — fast and expensive
Warm  (10–100 views/month): Nearline — slightly slower, 50% cheaper
Cold  (&lt;10 views/month):   Coldline — retrieval delay, 80% cheaper
Archive (&lt;1 view/month):   Archive — hours to retrieve, 95% cheaper
 
<span class="cm">// ~80% of all YouTube videos have fewer than 1K total views ever</span>
<span class="cm">// Tiering long-tail to cold storage saves enormous cost</span>
<span class="cm">// Replication:</span>
<span class="cm">// GCS multi-region: automatic 3x replication across AZs</span>
<span class="cm">// Cross-region: popular videos replicated to US, EU, APAC buckets</span></pre>
  </div>
  <div class="sh" style="font-size:16px;margin-top:18px">Search Architecture</div>
  <div class="cb"><div class="cb-top">Elasticsearch for video discovery<span class="cb-l">SEARCH</span></div>
<pre class="c"><span class="cm">// Elasticsearch index: "videos"</span>
{
  <span class="str">"videoId"</span>: <span class="str">"abc123"</span>,
  <span class="str">"title"</span>: <span class="str">"How to make pasta"</span>,            <span class="cm">← full-text search</span>
  <span class="str">"description"</span>: <span class="str">"Step by step guide..."</span>,    <span class="cm">← full-text search</span>
  <span class="str">"tags"</span>: [<span class="str">"cooking"</span>, <span class="str">"pasta"</span>, <span class="str">"recipe"</span>],  <span class="cm">← exact match</span>
  <span class="str">"transcript"</span>: <span class="str">"Today we're making..."</span>,     <span class="cm">← auto-generated captions</span>
  <span class="str">"viewCount"</span>: 1500000,                      <span class="cm">← boost popular results</span>
  <span class="str">"uploadDate"</span>: <span class="str">"2024-01-15"</span>,               <span class="cm">← recency signal</span>
  <span class="str">"channelSubscribers"</span>: 5000000             <span class="cm">← authority signal</span>
}
 
<span class="cm">// Keep ES in sync with MySQL:</span>
<span class="cm">// MySQL change → Debezium CDC → Kafka topic "db-changes" → ES consumer</span>
<span class="cm">// Async — ES may lag MySQL by seconds, acceptable for search freshness</span>
<span class="cm">// Autocomplete: ES "search_as_you_type" field type on title</span>
<span class="cm">// Returns suggestions after 2 characters</span></pre>
  </div>
</div>
<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="mb8_tt(this)"><div class="t-num">01</div><div class="t-lbl">Transcoding Pipeline Design</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>How many transcoding workers are needed for 8.3 hrs/sec input at 1× realtime? Show the math.</li>
          <li>Design the Kafka topic + partition key for the transcoding job queue (ordering? parallelism?)</li>
          <li>A 4-hour video is uploaded. Temporal parallelism splits it into 240 segments. How do you coordinate the concatenation step?</li>
          <li>A transcoding worker crashes halfway through segment 42 of 240. How do you resume without re-processing completed segments?</li>
          <li>Priority queue: paid YouTube Premium creators should process before free-tier. Design the priority mechanism.</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="mb8_tt(this)"><div class="t-num">02</div><div class="t-lbl">CDN Caching Strategy</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <ol>
          <li>New video from Mr. Beast (230M subscribers) — what happens in the first 10 minutes?</li>
          <li>Steady popular video: 500K views/day for 5 years. Where is it cached and what tier?</li>
          <li>Long-tail video: 2 views/month for 5 years. Should it even be on CDN?</li>
          <li>50M people watch a live music event simultaneously. How does CDN handle the thundering herd?</li>
          <li>Cache invalidation: creator updates thumbnail after 1M views. How do you purge it from 1,000+ edge nodes?</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="mb8_tt(this)"><div class="t-num">03</div><div class="t-lbl">View Counter at Scale</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Design a view counter with these exact constraints:</p>
        <ul>
          <li>Viral video: 10M views in 1 hour (2,778 views/sec on a single video)</li>
          <li>Display count with &lt;30 second lag</li>
          <li>Durability: must not lose counts (Redis crash shouldn't lose 30s of views)</li>
          <li>Spam prevention: same IP in same hour should only count once</li>
          <li>Analytics: views-per-hour breakdown for the last 30 days (for creator analytics)</li>
        </ul>
        <p style="margin-top:8px">For the viral video case: how many Redis nodes are needed? What's the sharding strategy?</p>
      </div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--red)">
      <div class="task-hd" onclick="mb8_tt(this)"><div class="t-num" style="color:var(--red)">★</div><div class="t-lbl">Full YouTube Design — 45-min Simulation</div><div class="t-meta">~3 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Apply the 7-step framework. Time yourself to 45 minutes. Cover:</p>
        <ol>
          <li>Requirements + estimations: upload rate, storage growth, CDN bandwidth, transcoding throughput</li>
          <li>Full architecture diagram: upload path + stream path</li>
          <li>Chunked upload protocol + deduplication</li>
          <li>Transcoding: temporal parallelism math, codec choices</li>
          <li>HLS: manifest structure, adaptive bitrate switching</li>
          <li>CDN: 3-tier strategy + pre-warming</li>
          <li>View counter: sharded Redis + Kafka + ClickHouse</li>
          <li>Failure modes: transcoding worker crash, CDN node failure, GCS region outage</li>
        </ol>
      </div>
    </div>
  </div>
</div>
<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 16 completed</span><span style="font-family:'DM Mono',monospace">MODULE B8 · YOUTUBE</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Requirements: upload, stream, search, view count, subscribe</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Estimation: 90 TB/day new video, 58 Tbps CDN bandwidth</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Chunked resumable upload: uploadId, 5 MB chunks, resume from last ACK</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Pre-upload SHA-256 deduplication</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Transcoding: temporal parallelism (1-min segments × N workers = 60× speedup)</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">HLS: master.m3u8 → quality variant .m3u8 → 2s .ts segments</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Adaptive bitrate: player measures bandwidth every 2s, switches at segment boundaries</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Codec trade-offs: H.264 (universal), VP9 (30-50% smaller, Chrome), AV1 (future)</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">3-tier CDN: edge PoPs (80% hit) → regional (15%) → GCS origin (5%)</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">CDN pre-warming: subscriber count + view velocity triggers edge prefetch</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">View counter: sharded Redis INCR + Kafka events + ClickHouse analytics</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Spam prevention: SETNX dedup key per IP per hour</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Storage lifecycle: hot → nearline → coldline → archive by view velocity</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Search: Elasticsearch with title/description/transcript + CDC sync from MySQL</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Tasks 1–3: transcoding pipeline, CDN strategy, view counter</div></div>
    <div class="chk" onclick="mb8_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4 (capstone): full YouTube — 45-min interview simulation</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--red)">
    <div style="font-family:'DM Mono',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
    <div style="font-family:'Anton',sans-serif;font-size:28px;letter-spacing:0.5px;color:var(--white);margin-bottom:6px">B9 — Design a Rate Limiter</div>
    <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--muted);line-height:2">
      Token bucket · Leaky bucket · Fixed window · Sliding window log<br>
      Sliding window counter · Distributed rate limiting · Redis Lua scripts<br>
      Where to apply limits · API gateway integration · Edge rate limiting
    </div>
  </div>
</div>
</div>
<!-- Bottom Navigation -->
<div class="mb8-bottom-nav">
  <a href="/learning/system-design/hld/module-b7-whatsapp/" class="mb8-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb8-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
    PREVIOUS: B7
  </a>
  <a href="/learning/system-design/hld/module-b8-notes/" class="mb8-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb8-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    READ STUDY NOTES
  </a>
  <a href="/learning/system-design/system-design-roadmap/" class="mb8-nav-footer-btn" style="border-right: 1px solid var(--bord2);">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb8-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
    ROADMAP
  </a>
  <a href="/learning/system-design/hld/module-b9-rate-limiter/" class="mb8-nav-footer-btn">
    NEXT: B9
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" class="mb8-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </a>
</div>
</div>
<script src="/assets/js/sd-module-b8.js"></script>
