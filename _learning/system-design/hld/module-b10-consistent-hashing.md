---
layout: default
title: "Module B10: Consistent Hashing"
permalink: /learning/system-design/hld/module-b10-consistent-hashing/
---

<link rel="stylesheet" href="{{ "/assets/css/sd-module-b10.css" | relative_url }}">

<div class="sd-module-b10">
<header>
  <div class="hdr-stripe"></div>
  <div class="hdr-top">
    <span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B10 · WEEK 20</span>
    <span>CONSISTENT HASHING · VIRTUAL NODES · SERVICE DISCOVERY</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">Distributed Systems Fundamentals · Hash Ring · Registry</div>
      <h1>CONSISTENT<br><span class="acc">HASHING</span></h1>
      <div class="hdr-sub">HASH RING · VIRTUAL NODES · CONSUL · ZOOKEEPER<br>CLIENT-SIDE vs SERVER-SIDE · GOSSIP · HEALTH CHECKS</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">1/N</div><div class="hs-l">KEYS REMAPPED</div></div>
      <div class="hs"><div class="hs-v">2³²</div><div class="hs-l">RING SIZE</div></div>
      <div class="hs"><div class="hs-v">150</div><div class="hs-l">VNODES/NODE</div></div>
      <div class="hs"><div class="hs-v">B10</div><div class="hs-l">MODULE</div></div>
    </div>
  </div>
  <div class="tag-row">
    <div class="tg" style="color:var(--bri)">Modulo Problem</div>
    <div class="tg" style="color:var(--cya)">Hash Ring</div>
    <div class="tg" style="color:var(--grn)">Virtual Nodes</div>
    <div class="tg" style="color:var(--yel)">Consul</div>
    <div class="tg" style="color:var(--pur)">ZooKeeper</div>
    <div class="tg" style="color:var(--bri)">Gossip Protocol</div>
    <div class="tg" style="color:var(--cya)">Health Checks</div>
  </div>
</header>

<nav class="nav">
  <div class="nt active" onclick="mb10_show('problem',this)">The Problem</div>
  <div class="nt" onclick="mb10_show('ring',this)">Hash Ring</div>
  <div class="nt" onclick="mb10_show('vnodes',this)">Virtual Nodes</div>
  <div class="nt" onclick="mb10_show('impl',this)">Implementation</div>
  <div class="nt" onclick="mb10_show('uses',this)">Use Cases</div>
  <div class="nt" onclick="mb10_show('discovery',this)">Service Discovery</div>
  <div class="nt" onclick="mb10_show('registries',this)">Consul &amp; ZooKeeper</div>
  <div class="nt" onclick="mb10_show('health',this)">Health Checks</div>
  <div class="nt" onclick="mb10_show('gossip',this)">Gossip Protocol</div>
  <div class="nt" onclick="mb10_show('tasks',this)">Tasks</div>
  <div class="nt" onclick="mb10_show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<div class="view active" id="view-problem">
  <div class="sh">The Modulo Hashing Problem</div>
  <div class="sr">Why hash(key) % N breaks when N changes</div>
  <div class="cmp">
    <div class="cmp-col" style="background:rgba(255,68,102,.03)">
      <div class="cmp-name" style="color:var(--red)">Modulo Hashing — BROKEN</div>
      <div class="cmp-body">
        3 nodes: shard = hash(key) % 3<br>
        "user:123" → hash=456 → 456%3 = <span style="color:var(--white)">Node 0</span><br>
        "user:456" → hash=789 → 789%3 = <span style="color:var(--white)">Node 2</span><br><br>
        <span style="color:var(--red)">Add 4th node (N=3 → N=4):</span><br>
        789 % 4 = <span style="color:var(--red)">1 → WRONG (was Node 2)</span><br>
        111 % 4 = <span style="color:var(--red)">3 → WRONG (was Node 0)</span><br><br>
        <span style="color:var(--red)">~75% of all keys remapped instantly.</span><br>
        75% cache miss rate → thundering herd.
      </div>
    </div>
    <div class="cmp-col" style="background:rgba(68,255,170,.02)">
      <div class="cmp-name" style="color:var(--grn)">Consistent Hashing — SOLVED</div>
      <div class="cmp-body">
        Ring: positions [0, 2³²)<br>
        Node A → pos 12 · Node B → pos 45 · Node C → pos 78<br><br>
        "user:123" → pos=20 → clockwise → <span style="color:var(--white)">Node B (45)</span><br>
        "user:456" → pos=60 → clockwise → <span style="color:var(--white)">Node C (78)</span><br><br>
        <span style="color:var(--grn)">Add Node D at position 55:</span><br>
        Only keys in range (45, 55] remapped → ~1/N ≈ 25%.<br><br>
        <span style="color:var(--grn)">25% vs 75% — 3× fewer cache misses</span>
      </div>
    </div>
  </div>
  <div class="al pur"><em>The key number:</em> Adding 1 node to an N-node cluster remaps ~1/(N+1) of all keys. For a 12-node cluster adding a 13th: only 7.7% of keys move. With modulo: 92.3% would move.</div>
</div>

<div class="view" id="view-ring">
  <div class="sh">The Hash Ring</div>
  <div class="sr">Nodes and keys share the same circular address space [0, 2³²)</div>
  <div class="ring-canvas">
    <div class="ring-wrap">
      <svg viewBox="0 0 320 320" width="320" height="320">
        <defs><radialGradient id="rg" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#1e1640"/><stop offset="100%" stop-color="#07050f"/></radialGradient></defs>
        <circle cx="160" cy="160" r="155" fill="url(#rg)" stroke="#2e2060" stroke-width="1"/>
        <circle cx="160" cy="160" r="120" fill="none" stroke="#3a2880" stroke-width="2"/>
        <g stroke="#2e2060" stroke-width="1"><line x1="160" y1="40" x2="160" y2="48"/><line x1="280" y1="160" x2="272" y2="160"/><line x1="160" y1="280" x2="160" y2="272"/><line x1="40" y1="160" x2="48" y2="160"/></g>
        <text x="160" y="32" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#3a2860">0</text>
        <text x="290" y="164" text-anchor="start" font-family="IBM Plex Mono" font-size="9" fill="#3a2860">2³¹</text>
        <text x="160" y="296" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#3a2860">2³²÷2</text>
        <circle cx="220" cy="100" r="10" fill="#441888" stroke="#8844ff" stroke-width="2"/>
        <text x="220" y="104" text-anchor="middle" font-family="Orbitron" font-size="8" font-weight="bold" fill="#aa66ff">A</text>
        <text x="236" y="90" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="#3a2860">pos:12</text>
        <circle cx="75" cy="100" r="10" fill="#441888" stroke="#8844ff" stroke-width="2"/>
        <text x="75" y="104" text-anchor="middle" font-family="Orbitron" font-size="8" font-weight="bold" fill="#aa66ff">B</text>
        <text x="56" y="90" text-anchor="middle" font-family="IBM Plex Mono" font-size="8" fill="#3a2860">pos:45</text>
        <circle cx="160" cy="282" r="10" fill="#441888" stroke="#8844ff" stroke-width="2"/>
        <text x="160" y="286" text-anchor="middle" font-family="Orbitron" font-size="8" font-weight="bold" fill="#aa66ff">C</text>
        <text x="185" y="288" font-family="IBM Plex Mono" font-size="8" fill="#3a2860">pos:78</text>
        <circle cx="210" cy="60" r="5" fill="#44ffaa" stroke="none"/>
        <text x="222" y="64" font-family="IBM Plex Mono" font-size="7" fill="#44ffaa">k:20→B</text>
        <circle cx="60" cy="175" r="5" fill="#44ddff" stroke="none"/>
        <text x="26" y="170" font-family="IBM Plex Mono" font-size="7" fill="#44ddff">k:60→C</text>
        <circle cx="250" cy="240" r="5" fill="#ffdd44" stroke="none"/>
        <text x="252" y="250" font-family="IBM Plex Mono" font-size="7" fill="#ffdd44">k:90→A↩</text>
        <circle cx="115" cy="58" r="8" fill="none" stroke="#ff8833" stroke-width="2" stroke-dasharray="3,2"/>
        <text x="115" y="62" text-anchor="middle" font-family="Orbitron" font-size="7" fill="#ff8833">D?</text>
        <text x="115" y="44" text-anchor="middle" font-family="IBM Plex Mono" font-size="7" fill="#ff8833">pos:55</text>
      </svg>
    </div>
    <div class="ring-legend">
      <div class="rl-title">// RING LEGEND</div>
      <div class="rl-item"><div class="rl-dot" style="background:#8844ff"></div><div class="rl-label">Physical nodes (A, B, C) placed by hash of node name</div></div>
      <div class="rl-item"><div class="rl-dot" style="background:#44ffaa"></div><div class="rl-label">k:20 → clockwise → node at 45 = Node B</div></div>
      <div class="rl-item"><div class="rl-dot" style="background:#44ddff"></div><div class="rl-label">k:60 → clockwise → node at 78 = Node C</div></div>
      <div class="rl-item"><div class="rl-dot" style="background:#ffdd44"></div><div class="rl-label">k:90 → clockwise → wraps to 12 = Node A</div></div>
      <div class="rl-item"><div class="rl-dot" style="background:#ff8833;border-radius:0"></div><div class="rl-label">New Node D at pos 55: only keys in (45, 55] move.</div></div>
      <div style="margin-top:14px;font-family:'IBM Plex Mono',monospace;font-size:9px;color:var(--text);line-height:1.9">
        Node A owns: (78, 12] (wraps around 0)<br>
        Node B owns: (12, 45]<br>
        Node C owns: (45, 78]
      </div>
    </div>
  </div>
</div>

<div class="view" id="view-vnodes">
  <div class="sh">Virtual Nodes</div>
  <div class="sr">K positions per physical node → uniform load distribution</div>
  <div class="vnode-grid">
    <div class="vn-card" style="border-top-color:var(--red)">
      <div class="vn-name" style="color:var(--red)">1 Vnode/Node</div>
      <div style="display:flex;gap:2px;height:40px;align-items:flex-end;margin:8px 0">
        <div style="background:var(--pur);width:33%;height:20%"></div>
        <div style="background:var(--pur);width:33%;height:80%"></div>
        <div style="background:var(--pur);width:33%;height:40%"></div>
      </div>
      <div class="vn-label">High variance — random positions lead to unequal arc sizes</div>
    </div>
    <div class="vn-card" style="border-top-color:var(--yel)">
      <div class="vn-name" style="color:var(--yel)">10 Vnodes/Node</div>
      <div style="display:flex;gap:2px;height:40px;align-items:flex-end;margin:8px 0">
        <div style="background:var(--pur);width:33%;height:50%"></div>
        <div style="background:var(--pur);width:33%;height:60%"></div>
        <div style="background:var(--pur);width:33%;height:55%"></div>
      </div>
      <div class="vn-label">Better — converging toward equal, still some variance</div>
    </div>
    <div class="vn-card" style="border-top-color:var(--grn)">
      <div class="vn-name" style="color:var(--grn)">150 Vnodes/Node ★</div>
      <div style="display:flex;gap:2px;height:40px;align-items:flex-end;margin:8px 0">
        <div style="background:var(--pur);width:33%;height:64%"></div>
        <div style="background:var(--pur);width:33%;height:66%"></div>
        <div style="background:var(--pur);width:33%;height:65%"></div>
      </div>
      <div class="vn-label">Near-uniform. Cassandra default. Std deviation &lt;5%</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Virtual node benefits beyond load balancing<span class="cb-l">KEY INSIGHT</span></div>
<pre class="c"><span class="cm">// BENEFIT 1: Even load (K=150 vnodes → each node ≈ 1/N share)</span>
<span class="cm">// BENEFIT 2: Adding node redistributes from ALL existing nodes evenly</span>
<span class="cm">// BENEFIT 3: Heterogeneous capacity</span>
PowerfulNode (32 cores): <span class="pu">300 vnodes</span>  → handles 2× data
StandardNode (16 cores): <span class="pu">150 vnodes</span>  → handles 1× data
WeakNode     ( 8 cores): <span class="pu"> 75 vnodes</span>  → handles 0.5× data
<span class="cm">// Cassandra: 256 vnodes default. Redis Cluster: 16,384 hash slots.</span></pre>
  </div>
</div>

<div class="view" id="view-impl">
  <div class="sh">Java Implementation</div>
  <div class="sr">TreeMap provides O(log N) clockwise walk via ceilingEntry()</div>
  <div class="cb"><div class="cb-top">ConsistentHashRing<span class="cb-l">JAVA</span></div>
<pre class="c"><span class="kw">public class</span> <span class="hl">ConsistentHashRing</span> {
    <span class="kw">private final</span> TreeMap&lt;Integer, String&gt; ring = <span class="kw">new</span> <span class="fn">TreeMap</span>&lt;&gt;();
    <span class="kw">private final int</span> VNODES = <span class="cy">150</span>;

    <span class="kw">private int</span> <span class="fn">hash</span>(String key) {
        <span class="kw">return</span> Hashing.murmur3_32().<span class="fn">hashString</span>(key, UTF_8).<span class="fn">asInt</span>();
    }

    <span class="kw">public void</span> <span class="fn">addNode</span>(String node) {
        <span class="kw">for</span> (<span class="kw">int</span> v = <span class="cy">0</span>; v &lt; VNODES; v++) ring.<span class="fn">put</span>(<span class="fn">hash</span>(node + <span class="str">"#"</span> + v), node);
    }

    <span class="kw">public void</span> <span class="fn">removeNode</span>(String node) {
        <span class="kw">for</span> (<span class="kw">int</span> v = <span class="cy">0</span>; v &lt; VNODES; v++) ring.<span class="fn">remove</span>(<span class="fn">hash</span>(node + <span class="str">"#"</span> + v));
    }

    <span class="kw">public</span> String <span class="fn">getNode</span>(String key) {
        <span class="kw">if</span> (ring.<span class="fn">isEmpty</span>()) <span class="kw">throw new</span> IllegalStateException(<span class="str">"No nodes"</span>);
        Map.Entry&lt;Integer, String&gt; e = ring.<span class="fn">ceilingEntry</span>(<span class="fn">hash</span>(key));
        <span class="kw">return</span> (e != <span class="kw">null</span> ? e : ring.<span class="fn">firstEntry</span>()).<span class="fn">getValue</span>();
    }
}</pre>
  </div>
</div>

<div class="view" id="view-uses">
  <div class="sh">Real-World Use Cases</div>
  <div class="sr">Where consistent hashing solves the node change problem</div>
  <table class="reg-table">
    <thead><tr><th>SYSTEM</th><th>HOW IT USES CONSISTENT HASHING</th><th>SPECIFICS</th></tr></thead>
    <tbody>
      <tr><td>Redis Cluster</td><td>16,384 hash slots across nodes. CRC16(key) % 16,384 → slot → node.</td><td>Hash tags: {user_id} forces related keys to same slot.</td></tr>
      <tr><td>Apache Cassandra</td><td>256 vnodes/node. Token range owns ring slice. Reads/writes to token owner + replicas.</td><td>RF=3 → 3 consecutive ring nodes own each key.</td></tr>
      <tr><td>Amazon DynamoDB</td><td>Consistent hashing for partition routing. Auto-scaling splits ranges.</td><td>Consistent hashing minimises rebalancing on partition add.</td></tr>
      <tr><td>CDN (Akamai)</td><td>Consistent hashing within PoP across cache servers.</td><td>Same URL → same cache server → higher hit rate.</td></tr>
      <tr><td>Sticky LB</td><td>Same user → same backend server → in-memory session cache works.</td><td>Server failure: only that server's users remapped.</td></tr>
    </tbody>
  </table>
</div>

<div class="view" id="view-discovery">
  <div class="sh">Service Discovery Patterns</div>
  <div class="sr">How Service A finds Service B in a dynamic microservices environment</div>
  <div class="disc-grid">
    <div class="dc" style="border-top-color:var(--bri)">
      <div class="dc-name" style="color:var(--bri)">Client-Side Discovery</div>
      <div class="dc-sub">CLIENT QUERIES REGISTRY DIRECTLY</div>
      <div class="dc-body">Client queries registry → gets instance list → load balances (round-robin/random) → connects directly.</div>
      <div class="dc-pro">✓ No extra network hop<br>✓ Client controls LB strategy</div>
      <div class="dc-con">✗ LB logic in every client<br>✗ Multiple language SDKs needed</div>
    </div>
    <div class="dc" style="border-top-color:var(--grn)">
      <div class="dc-name" style="color:var(--grn)">Server-Side Discovery ★</div>
      <div class="dc-sub">GATEWAY HANDLES ROUTING</div>
      <div class="dc-body">Client calls gateway → gateway queries registry → gateway routes to healthy instance. Clients need no discovery logic.</div>
      <div class="dc-pro">✓ Simple clients<br>✓ Central LB policy<br>✓ Works across languages</div>
      <div class="dc-con">✗ Extra hop through gateway<br>✗ Gateway is critical path</div>
    </div>
    <div class="dc" style="border-top-color:var(--cya)">
      <div class="dc-name" style="color:var(--cya)">DNS-Based Discovery</div>
      <div class="dc-sub">SERVICE = DNS A RECORD</div>
      <div class="dc-body">Registry publishes IPs as DNS A records. Kubernetes CoreDNS handles this automatically.</div>
      <div class="dc-pro">✓ Standard protocol<br>✓ Kubernetes native</div>
      <div class="dc-con">✗ DNS TTL caching = stale IPs<br>✗ No health awareness in DNS</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Kubernetes DNS discovery<span class="cb-l">KUBERNETES</span></div>
<pre class="c"><span class="cm"># Format: {service}.{namespace}.svc.cluster.local</span>
curl http://payment-service.default.svc.cluster.local:<span class="cy">8080</span>/charge
<span class="cm"># CoreDNS → ClusterIP → kube-proxy → healthy pod</span>
<span class="cm"># Pod fails → Endpoints controller removes it → no traffic routed</span></pre>
  </div>
</div>

<div class="view" id="view-registries">
  <div class="sh">Consul &amp; ZooKeeper</div>
  <div class="sr">Production service registries — choose by consistency needs</div>
  <div class="cb"><div class="cb-top">Consul — register + discover healthy instances<span class="cb-l">CONSUL HTTP API</span></div>
<pre class="c">PUT /v1/agent/service/register
{ <span class="str">"Name"</span>: <span class="str">"payment-service"</span>, <span class="str">"ID"</span>: <span class="str">"payment-1"</span>,
  <span class="str">"Address"</span>: <span class="str">"10.0.1.23"</span>, <span class="str">"Port"</span>: <span class="cy">8080</span>,
  <span class="str">"Check"</span>: { <span class="str">"HTTP"</span>: <span class="str">"http://10.0.1.23:8080/health"</span>, <span class="str">"Interval"</span>: <span class="str">"10s"</span> } }

GET /v1/health/service/payment-service?passing=<span class="kw">true</span>
<span class="cm">// → returns healthy instances only</span>

GET /v1/health/service/payment-service?passing=true&amp;index=<span class="cy">50</span>&amp;wait=<span class="cy">30s</span>
<span class="cm">// → long-poll: blocks until change or timeout → client auto-refreshes</span></pre>
  </div>
  <div class="cb"><div class="cb-top">ZooKeeper — ephemeral znodes<span class="cb-l">ZOOKEEPER</span></div>
<pre class="c">create /services/payment/instance-1  <span class="str">"10.0.1.23:8080"</span>  [EPHEMERAL]
<span class="cm">// Ephemeral = auto-deleted on session expire (service crash)</span>
getChildren /services/payment [WATCH]
<span class="cm">// → client notified when instance created/deleted</span></pre>
  </div>
  <table class="reg-table" style="margin-top:14px">
    <thead><tr><th>FEATURE</th><th>CONSUL</th><th>ZOOKEEPER</th><th>ETCD (k8s)</th></tr></thead>
    <tbody>
      <tr><td>Consistency</td><td>Raft (strong)</td><td>ZAB (strong)</td><td>Raft (strong)</td></tr>
      <tr><td>Use case</td><td>Service mesh, multi-DC</td><td>Locks, leader election</td><td>Kubernetes control plane</td></tr>
      <tr><td>Health checks</td><td>Built-in (HTTP/TCP)</td><td>Session timeout only</td><td>Leases (TTL keys)</td></tr>
    </tbody>
  </table>
</div>

<div class="view" id="view-health">
  <div class="sh">Health Checks</div>
  <div class="sr">Registry must know which instances are healthy</div>
  <div class="cb"><div class="cb-top">/health endpoint standard<span class="cb-l">HTTP</span></div>
<pre class="c"><span class="cm">// GET /health → 200 if healthy, 503 if not</span>
{ <span class="str">"status"</span>: <span class="str">"healthy"</span>, <span class="str">"checks"</span>: {
    <span class="str">"database"</span>: <span class="str">"connected"</span>,
    <span class="str">"redis"</span>:    <span class="str">"connected"</span>,
    <span class="str">"disk"</span>:     <span class="str">"98% free"</span>
  }, <span class="str">"version"</span>: <span class="str">"2.3.1"</span> }

<span class="cm">// Registry sees 503 → removes from routing pool</span>
<span class="cm">// Consul default: 2 consecutive failures → deregister</span>
<span class="cm">// Check interval 10s → failure detected within 20–30s</span></pre>
  </div>
  <div class="al pur"><em>Liveness vs Readiness (Kubernetes):</em> Liveness = process alive? (restart if not). Readiness = ready for traffic? (remove from LB if not). Only readiness affects service discovery routing.</div>
</div>

<div class="view" id="view-gossip">
  <div class="sh">Gossip Protocol</div>
  <div class="sr">Eventual consistency for cluster membership — O(log N) propagation</div>
  <div class="gossip-box">
    <div class="gb-label">// GOSSIP PROPAGATION — 16 nodes, K=3 neighbors per round</div>
    <div class="gb-round">
      <span style="width:60px;color:var(--muted)">Round 1:</span>
      <div class="gb-nodes">
        <div class="gb-node" style="border-color:var(--pur);color:var(--bri)">N1★</div>
        <div class="gb-node" style="border-color:var(--pur);color:var(--bri)">N5★</div>
        <div class="gb-node" style="border-color:var(--pur);color:var(--bri)">N11★</div>
        <div class="gb-node" style="border-color:var(--bord2);color:var(--muted)">N2</div>
        <div class="gb-node" style="border-color:var(--bord2);color:var(--muted)">N3</div>
        <div style="color:var(--muted);font-size:9px;margin-left:4px">3/16 nodes know</div>
      </div>
    </div>
    <div class="gb-round">
      <span style="width:60px;color:var(--muted)">Round 2:</span>
      <div class="gb-nodes">
        <div class="gb-node" style="border-color:var(--bri);color:var(--bri)">N1★</div>
        <div class="gb-node" style="border-color:var(--bri);color:var(--bri)">N5★</div>
        <div class="gb-node" style="border-color:var(--bri);color:var(--bri)">N11★</div>
        <div class="gb-node" style="border-color:var(--bri);color:var(--text)">N2★</div>
        <div class="gb-node" style="border-color:var(--bri);color:var(--text)">N7★</div>
        <div class="gb-node" style="border-color:var(--bri);color:var(--text)">N14★</div>
        <div class="gb-node" style="border-color:var(--bri);color:var(--text)">N9★</div>
        <div style="color:var(--muted);font-size:9px;margin-left:4px">9/16 nodes know</div>
      </div>
    </div>
    <div class="gb-round">
      <span style="width:60px;color:var(--muted)">Round 3:</span>
      <div class="gb-nodes">
        <div class="gb-node" style="border-color:var(--grn);color:var(--grn)">ALL 16★</div>
        <div style="color:var(--muted);font-size:9px;margin-left:8px">16/16 know · O(log₃ 16) ≈ 2.5 rounds</div>
      </div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Gossip vs Raft<span class="cb-l">COMPARISON</span></div>
<pre class="c"><span class="cm">// GOSSIP: eventually consistent, O(log N), no leader, scales to 1000s of nodes</span>
<span class="cm">// Use for: cluster membership, failure detection</span>

<span class="cm">// RAFT: strongly consistent, leader-based, quorum required, ~5-7 nodes practical</span>
<span class="cm">// Use for: config store, leader election, distributed locks</span>

<span class="cm">// Consul uses BOTH:</span>
<span class="cm">//   Gossip (SWIM) for membership + failure detection</span>
<span class="cm">//   Raft for KV store + service catalog consistency</span></pre>
  </div>
</div>

<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="mb10_tt(this)"><div class="t-num">01</div><div class="t-lbl">Consistent Hash Ring Implementation</div><div class="t-meta">~2 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd"><ol>
        <li>Implement <code>ConsistentHashRing</code> with <code>addNode</code>, <code>removeNode</code>, <code>getNode</code> using TreeMap</li>
        <li>Test with 3 nodes and 1,000 random keys. Verify ~33% per node.</li>
        <li>Add a 4th node. Verify ~25% of keys remapped (not 75%).</li>
        <li>Remove a node. Verify only that node's keys remapped.</li>
        <li>What if two nodes hash to the same ring position? Handle collisions.</li>
      </ol></div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="mb10_tt(this)"><div class="t-num">02</div><div class="t-lbl">Virtual Node Distribution Analysis</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd"><ol>
        <li>Simulate 3 nodes with 1, 10, 50, 150, 300 vnodes each.</li>
        <li>Hash 10,000 random keys in each configuration.</li>
        <li>Calculate std deviation across nodes for each vnode count.</li>
        <li>At what vnode count does std dev fall below 5%?</li>
        <li>At K=150, how does adding a 4th node compare to modulo hashing?</li>
      </ol></div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="mb10_tt(this)"><div class="t-num">03</div><div class="t-lbl">Service Discovery System Design</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd"><p>Design service discovery for 50 microservices, each with 3–10 instances:</p><ol>
        <li>Client-side vs server-side discovery — argue both, pick one, justify.</li>
        <li>Pod starts at 9:00:00. What happens step-by-step until first request?</li>
        <li>Pod dies without SIGTERM at 9:05:00. When do errors stop? What is the gap?</li>
        <li>Network partition: 2 of 5 Consul nodes can't reach the other 3. Who serves?</li>
        <li>What does /health check? What thresholds trigger unhealthy?</li>
      </ol></div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--pur)">
      <div class="task-hd" onclick="mb10_tt(this)"><div class="t-num" style="color:var(--pur)">★</div><div class="t-lbl">Add Consistent Hashing to URL Shortener</div><div class="t-meta">~2 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd"><p>URL shortener from B5 + B9 now has 5 Redis cache nodes:</p><ol>
        <li>How many vnodes per Redis node? Justify.</li>
        <li>Redis node 3 fails. Miss rate impact vs modulo hashing?</li>
        <li>Add Redis node 6. What % of cached URLs need to be reloaded from DB?</li>
        <li>What would modulo hashing do when node 3 fails?</li>
        <li>Design zero-downtime transition from modulo to consistent hashing.</li>
      </ol></div>
    </div>
  </div>
</div>

<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 19 completed</span><span style="font-family:'IBM Plex Mono',monospace">MODULE B10 · CONSISTENT HASHING</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Modulo flaw: adding 1 node remaps ~N/(N+1) ≈ all keys</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Hash ring: both nodes and keys mapped to [0, 2³²)</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Clockwise walk: ceilingEntry() or firstEntry() to wrap</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Adding node: only 1/(N+1) keys remapped</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Virtual nodes: K positions per physical node → uniform distribution</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Vnodes: 150 standard (Cassandra: 256, Redis: 16,384 slots)</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Heterogeneous nodes: weighted vnodes (2× hardware → 2× vnodes)</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">TreeMap: addNode, removeNode, getNode — O(log N)</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Use cases: Redis Cluster, Cassandra, CDN, sticky LB</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Service discovery registry pattern: register, query, health check</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Client-side vs server-side discovery trade-offs</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">DNS-based: Kubernetes CoreDNS, service.namespace.svc.cluster.local</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Consul: HTTP register + health check + passing=true + watch</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">ZooKeeper: ephemeral znodes auto-deleted on session expire</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Health check: 200 healthy / 503 unhealthy; 2-failure threshold</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Liveness vs readiness — different purposes, different consequences</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Gossip: O(log N) propagation, eventual consistency, no leader</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Tasks 1–3: ring impl, vnode analysis, service discovery</div></div>
    <div class="chk" onclick="mb10_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4 (capstone): consistent hashing added to URL shortener</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--pur)">
    <div style="font-family:'IBM Plex Mono',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
    <div style="font-family:'Orbitron',sans-serif;font-size:22px;font-weight:700;letter-spacing:1px;color:var(--white);margin-bottom:6px">B11 — ACID, Distributed Transactions &amp; Saga</div>
    <div style="font-family:'IBM Plex Mono',monospace;font-size:9px;color:var(--muted);line-height:2">
      ACID properties · 2-Phase Commit · Distributed transactions<br>
      Saga pattern (choreography vs orchestration) · Compensating transactions<br>
      Outbox pattern · Idempotency · BASE vs ACID trade-offs
    </div>
  </div>
</div>

</div>

<div class="mb10-bottom-nav">
  <a href="/learning/system-design/hld/module-b9-rate-limiter/" class="mb10-nav-footer-btn">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
    ← B9 RATE LIMITER
  </a>
  <a href="/learning/system-design/hld/module-b10-notes/" class="mb10-nav-footer-btn">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
    READ STUDY NOTES
  </a>
  <a href="/learning/system-design/hld/" class="mb10-nav-footer-btn">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    ↑ HLD TRACK
  </a>
  <a href="/learning/system-design/hld/module-b11-distributed-tx/" class="mb10-nav-footer-btn">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    NEXT: B11 →
  </a>
</div>
</div>
<script src="{{ "/assets/js/sd-module-b10.js" | relative_url }}"></script>
