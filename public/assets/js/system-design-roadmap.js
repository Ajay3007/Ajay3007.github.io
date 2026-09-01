function switchTab(view, el) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById('view-' + view).classList.add('active');
  el.classList.add('active');
}

// GANTT data
const ganttRows = [
  { section: 'PHASE 0 — FOUNDATION', link: '/learning/system-design/foundation/phase0-foundation/' },
  { label: 'Networking + OS + DB Basics', start: 1, end: 2, color: '#ffa94d', tip: 'TCP/IP, HTTP, Threads, Memory, ACID, Indexing' },
  { label: 'SD Interview Framework', start: 1, end: 2, color: '#ffa94d', tip: 'Req → Estimation → HLD → Deep Dive → Trade-offs' },
  { label: 'Back-of-Envelope Estimation', start: 1, end: 2, color: '#ffa94d', tip: 'QPS, Storage, Bandwidth calculation as a skill' },

  { section: 'TRACK A — LLD (Weeks 3–10)' },
  { label: 'A1 · SOLID + OOP + UML', start: 3, end: 3, color: '#7c6fff', tip: 'SOLID principles, UML Class/Sequence diagrams. Task: Refactor Parking Lot' },
  { label: 'A2 · Creational Patterns', start: 4, end: 4, color: '#7c6fff', tip: 'Singleton, Factory, Abstract Factory, Builder, Prototype. Project: ATM System' },
  { link: '/learning/system-design/lld/module-a3-structural/', label: 'A3 · Structural Patterns', start: 5, end: 5, color: '#7c6fff', tip: 'Adapter, Decorator, Proxy, Composite, Facade, Bridge, Flyweight. Project: Splitwise' },
  { link: '/learning/system-design/lld/module-a4-behavioral/', label: 'A4 · Behavioral Patterns', start: 6, end: 7, color: '#7c6fff', tip: '12 patterns: Strategy, Observer, CoR, State, Command... Project: BookMyShow' },
  { label: 'A5 · Concurrency in LLD', start: 8, end: 8, color: '#7c6fff', tip: 'Threads, Locks, Semaphores, Thread Pool, Deadlock prevention' },
  { label: 'A6 · Advanced LLD Systems', start: 9, end: 10, color: '#7c6fff', tip: 'LinkedIn, Amazon, Uber, Hotel, Voting, Cache, Rate Limiter. Project: Uber LLD' },

  { section: 'TRACK B — HLD (Weeks 11–22)' },
  { link: '/learning/system-design/hld/module-b1-hld-fundamentals/', label: 'B1 · HLD Fundamentals', start: 11, end: 11, color: '#00d4aa', tip: 'Scalability, CAP Theorem, Consistency Models, Availability Patterns, Load Balancing, Back-of-Envelope Estimation' },
  { link: '/learning/system-design/hld/module-b2-databases-at-scale/', label: 'B2 · Databases at Scale', start: 12, end: 12, color: '#00d4aa', tip: 'Indexing (B-Tree, Hash, Composite), ACID vs BASE, SQL vs NoSQL, Replication, Sharding, DB Selection Guide' },
  { link: '/learning/system-design/hld/module-b3-caching/', label: 'B3 · Caching', start: 13, end: 13, color: '#00d4aa', tip: 'Cache-Aside, Write-Through, Write-Back, LRU/LFU eviction, Stampede prevention, Redis data structures, CDN' },
  { link: '/learning/system-design/hld/module-b4-message-queues/', label: 'B4 · Message Queues & Kafka', start: 14, end: 14, color: '#00d4aa', tip: 'Kafka partitions/offsets/consumer groups, at-least-once vs exactly-once, async patterns, backpressure' },
  { link: '/learning/system-design/hld/module-b5-url-shortener/', label: 'B5 · URL Shortener', start: 15, end: 15, color: '#00d4aa', tip: 'Base62 encoding, Snowflake ID generation, 301 vs 302 redirects, caching topology, read-heavy scaling' },
  { link: '/learning/system-design/hld/module-b6-twitter-feed/', label: 'B6 · Design Twitter Feed', start: 16, end: 16, color: '#00d4aa', tip: 'Fan-out on write vs read, hybrid timeline, Redis cache pre-computation, async count updates' },
  { link: '/learning/system-design/hld/module-b7-whatsapp/', label: 'B7 · Design WhatsApp', start: 17, end: 17, color: '#00d4aa', tip: 'Persistent WebSockets, Cassandra, delivery receipts, presence system, group messaging fan-out' },
  { link: '/learning/system-design/hld/module-b8-youtube/', label: 'B8 · Design YouTube', start: 18, end: 18, color: '#00d4aa', tip: 'Chunked upload, temporal parallelism transcoding, HLS adaptive streaming, 3-tier CDN, sharded view counter' },
  { link: '/learning/system-design/hld/module-b9-rate-limiter/', label: 'B9 · Rate Limiter', start: 19, end: 19, color: '#00d4aa', tip: 'Fixed/Sliding Window, Token Bucket, Leaky Bucket, Redis Lua atomicity, multi-tier architecture, HTTP 429' },
  { link: '/learning/system-design/hld/module-b10-consistent-hashing/', label: 'B10 · Consistent Hashing', start: 20, end: 20, color: '#00d4aa', tip: 'Hash ring, virtual nodes (150/node), clockwise key lookup, heterogeneous weighting, Consul, ZooKeeper, Raft' },
  { link: '/learning/system-design/hld/module-b11-distributed-tx/', label: 'B11 · Distributed Transactions', start: 21, end: 21, color: '#00d4aa', tip: '2PC (blocking, SPOF), Saga pattern, choreography vs orchestration, Outbox pattern, idempotency keys' },
  { link: '/learning/system-design/hld/module-b12-interview-framework/', label: 'B12 · Interview Framework', start: 22, end: 22, color: '#00d4aa', tip: '7-step 45-min framework, capacity estimation cheat sheet, 6 mock problems, 7 common mistakes' },

  { section: 'PHASE 2 — CONVERGENCE (Weeks 17–20)' },
  { label: 'URL Shortener · Pastebin', start: 17, end: 17, color: '#ff6b9d', tip: 'Full design: Req → Est → HLD → Deep dive → Trade-offs' },
  { label: 'WhatsApp · Notification Sys', start: 17, end: 18, color: '#ff6b9d', tip: 'Real-time messaging, push notifications, fan-out' },
  { label: 'Instagram · Twitter · NewsFeed', start: 18, end: 19, color: '#ff6b9d', tip: 'Feed generation, ranking, media storage, CDN' },
  { label: 'YouTube · Dropbox · Drive', start: 19, end: 20, color: '#ff6b9d', tip: 'Video transcoding, chunked upload, file sync' },
  { label: 'Ticket Master · Web Crawler', start: 20, end: 20, color: '#ff6b9d', tip: 'Seat reservation, concurrency, crawl scheduling' },

  { section: 'PHASE 3 — ADVANCED (Weeks 21–22)' },
  { label: 'Maintainability + Security', start: 21, end: 21, color: '#e879f9', tip: 'SLOs, Observability, AuthN/AuthZ, mTLS, Zero Trust' },
  { label: 'Cost Optimization + Projects', start: 22, end: 22, color: '#e879f9', tip: 'Spot instances, tiered storage. Projects: Fraud Detection, Auth+Monitoring' },

  { section: 'PHASE 4 — MOCK + CAPSTONE (Weeks 23–24)' },
  { label: 'Mock Interview Bank (20 Qs)', start: 23, end: 23, color: '#38bdf8', tip: '20 timed problems with evaluation rubric' },
  { label: 'Capstone Project', start: 24, end: 24, color: '#38bdf8', tip: 'Uber / YouTube / BookMyShow end-to-end LLD+HLD' },
];

const root = document.getElementById('gantt-root');
const tooltip = document.getElementById('tooltip');
const WEEKS = 24;

document.addEventListener('DOMContentLoaded', () => {
    const root = document.getElementById('gantt-root');
    if (!root) return;

// Header
const headerRow = document.createElement('div');
headerRow.className = 'gantt-header-row';
headerRow.innerHTML = '<div></div>';
for (let w = 1; w <= WEEKS; w++) {
  const cell = document.createElement('div');
  cell.className = 'gantt-week-label';
  cell.textContent = `W${w}`;
  headerRow.appendChild(cell);
}
root.appendChild(headerRow);

ganttRows.forEach(row => {
  if (row.section) {
    const sRow = document.createElement('div');
    sRow.className = 'gantt-row';
    const label = document.createElement('div');
    label.className = 'gantt-section-title';
    if (row.link) {
      label.innerHTML = `<a href="${row.link}" style="color: inherit; text-decoration: none;">${row.section}</a>`;
    } else {
      label.textContent = row.section;
    }
    sRow.appendChild(label);
    root.appendChild(sRow);
    return;
  }

  const gRow = document.createElement('div');
  gRow.className = 'gantt-row';

  const label = document.createElement('div');
  label.className = 'gantt-label';
  if (row.link) {
    label.innerHTML = `<a href="${row.link}" style="color: inherit; text-decoration: none;">${row.label}</a>`;
  } else {
    label.textContent = row.label;
  }
  gRow.appendChild(label);

  for (let w = 1; w <= WEEKS; w++) {
    const cell = document.createElement('div');
    cell.className = 'gantt-cell';
    if (w >= row.start && w <= row.end) {
      cell.className = 'gantt-cell filled';
      cell.style.background = row.color;
      cell.style.opacity = '0.85';
      if (w === row.start) cell.style.borderRadius = '4px 0 0 4px';
      if (w === row.end) cell.style.borderRadius = (row.start === row.end ? '4px' : '0 4px 4px 0');
      if (w > row.start && w < row.end) cell.style.borderRadius = '0';

      cell.addEventListener('mouseenter', (e) => {
        document.getElementById('tt-title').textContent = row.label;
        document.getElementById('tt-body').textContent = row.tip;
        tooltip.classList.add('show');
      });
      cell.addEventListener('mousemove', (e) => {
        tooltip.style.left = (e.clientX + 16) + 'px';
        tooltip.style.top = (e.clientY - 10) + 'px';
      });
      cell.addEventListener('mouseleave', () => tooltip.classList.remove('show'));
    }
    gRow.appendChild(cell);
  }

  root.appendChild(gRow);
});
});
