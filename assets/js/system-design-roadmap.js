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

  { section: 'TRACK B — HLD (Weeks 3–16)' },
  { label: 'B1 · System Requirements', start: 3, end: 3, color: '#00d4aa', tip: 'Availability, Scalability, Durability, Consistency, Performance' },
  { label: 'B2 · Networking + Protocols', start: 4, end: 4, color: '#00d4aa', tip: 'TCP, UDP, HTTP/2/3, WebSocket, gRPC, Push/Pull, SSE' },
  { label: 'B3 · Hardware + Infra', start: 5, end: 5, color: '#00d4aa', tip: 'Regions, AZs, VMs, Containers, Serverless, CDN, API Gateway' },
  { label: 'B4 · Caching', start: 6, end: 6, color: '#00d4aa', tip: 'LRU/LFU, Cache-aside, Write-through, Redis. Task: Twitter feed cache' },
  { label: 'B5 · Data Store Internals', start: 7, end: 7, color: '#00d4aa', tip: 'LSM-tree, B-tree, RocksDB, Page Cache. Project: Build Key-Value Store' },
  { label: 'B6 · Databases at Scale', start: 8, end: 8, color: '#00d4aa', tip: 'SQL vs NoSQL, Sharding, Replication, Leader Election. Task: Instagram DB' },
  { label: 'B7 · Queues + Kafka', start: 9, end: 9, color: '#00d4aa', tip: 'Producer-Consumer, Kafka, Consumer offsets, Delivery guarantees' },
  { label: 'B8 · Distributed Concepts', start: 10, end: 10, color: '#00d4aa', tip: 'CAP, Consistent Hashing, Bloom Filter, Merkle Tree, Gossip' },
  { label: 'B9 · Scalability Patterns', start: 11, end: 11, color: '#00d4aa', tip: '0-to-million, Load Balancing, Autoscaling, Microservices, SAGA' },
  { label: 'B10 · Reliability + Fault Tol.', start: 12, end: 12, color: '#00d4aa', tip: 'Circuit Breaker, Bulkhead, Shuffle Sharding, Retries' },
  { label: 'B11 · Storage Systems', start: 13, end: 13, color: '#00d4aa', tip: 'Block/File/Object, RAID, GFS, HDFS. Task: Dropbox storage' },
  { label: 'B12 · Special Topics', start: 14, end: 14, color: '#00d4aa', tip: 'Typeahead, Web Crawler, News Feed, Geospatial (Yelp)' },
  { label: 'B13 · ML Systems Design', start: 15, end: 15, color: '#00d4aa', tip: 'Feature Store, Model Serving, A/B Testing, Recommendation Systems' },
  { label: 'B14 · Kubernetes + Containers', start: 16, end: 16, color: '#00d4aa', tip: 'Pods, Services, HPA, StatefulSets, Service Mesh (Istio)' },

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
