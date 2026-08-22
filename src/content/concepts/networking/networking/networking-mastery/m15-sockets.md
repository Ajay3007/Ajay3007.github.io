---
title: "M15 - Socket Programming"
description: "NETWORKING MASTERY · PHASE 4 · MODULE 15 · WEEK 13 🔌 Socket Programming POSIX sockets · TCP/UDP patterns · Non-blocking I/O · epoll · SO REUSEPORT · Raw sockets · Socket…"
domain: networking
track: networking-mastery
order: 15
ownHeader: true
url: /learning/networking-mastery/m15-sockets/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 40%,#1a5a8c 75%,#0a3a6c 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#90c8f0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c0dff8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d8ecff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#90c8f0;border-bottom-color:#90c8f0}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul,.cp-body ol{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.cp-body h4{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin:.9rem 0 .3rem}
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a5a8c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c0dff8;white-space:pre}
.cm{color:#4a6a88}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#e8f4ff;border:1.5px solid #1a5a8c;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0d2038;border-color:#2a6aac}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#1a3a6c}[data-theme=dark] .ins strong{color:#90c8f0}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#1a3a6c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a5a8c}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #1a5a8c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1a5a8c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1a5a8c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a5a8c;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 4 · MODULE 15 · WEEK 13</div>
  <div class="mod-title">🔌 Socket Programming</div>
  <div class="mod-subtitle">POSIX sockets · TCP/UDP patterns · Non-blocking I/O · epoll · SO_REUSEPORT · Raw sockets · Socket options</div>
  <div class="mod-pills">
    <span class="mod-pill">Intermediate → Advanced</span>
    <span class="mod-pill">Prerequisite: M14 Linux Stack</span>
    <span class="mod-pill">POSIX.1-2017</span>
    <span class="mod-pill">C / Systems Programming</span>
    <span class="mod-pill">3 Labs</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Socket API</button>
  <button class="tab-btn" onclick="vt(event,'t1')">TCP Server Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t2')">UDP Programming</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Non-blocking and epoll</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Socket Options</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Raw Sockets</button>
  <button class="tab-btn" onclick="vt(event,'t6')">AF_PACKET</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>
<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<p class="sep">THE POSIX SOCKET API — THE GATEWAY TO THE NETWORK</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>Socket Fundamentals</h3><span class="tag tag-blue">BASICS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* socket() — create a socket */</span>
<span class="ck">int</span> fd = socket(domain, type, protocol);
 
domain:   AF_INET (IPv4), AF_INET6 (IPv6), AF_UNIX (local), AF_PACKET (raw L2)
type:     SOCK_STREAM (TCP), SOCK_DGRAM (UDP), SOCK_RAW (raw IP/L2)
protocol: Usually 0 (auto-select). IPPROTO_TCP, IPPROTO_UDP, IPPROTO_ICMP
 
<span class="cm">/* Address structures */</span>
<span class="ck">struct</span> sockaddr_in {               <span class="cm">/* IPv4 */</span>
    sa_family_t    sin_family;      <span class="cm">/* AF_INET */</span>
    in_port_t      sin_port;        <span class="cm">/* htons(port) — network byte order! */</span>
    struct in_addr sin_addr;        <span class="cm">/* .s_addr = htonl(INADDR_ANY) or inet_addr("1.2.3.4") */</span>
};
 
<span class="ck">struct</span> sockaddr_in6 {              <span class="cm">/* IPv6 */</span>
    sa_family_t     sin6_family;    <span class="cm">/* AF_INET6 */</span>
    in_port_t       sin6_port;      <span class="cm">/* htons(port) */</span>
    uint32_t        sin6_flowinfo;
    struct in6_addr sin6_addr;      <span class="cm">/* IPv6 address (16 bytes) */</span>
    uint32_t        sin6_scope_id;
};
 
<span class="cm">/* Byte order — critical! */</span>
htons(x):  host-to-network short (16-bit port numbers)
htonl(x):  host-to-network long  (32-bit IP addresses)
ntohs(x):  network-to-host short
ntohl(x):  network-to-host long
<span class="cm"># Network byte order = big-endian</span>
<span class="cm"># x86 is little-endian → ALWAYS use htons/htonl for ports/IPs in structs</span>
<span class="cm">/* Dual-stack (IPv4+IPv6) */</span>
<span class="ck">int</span> fd = socket(AF_INET6, SOCK_STREAM, 0);
<span class="ck">int</span> v6only = 0;
setsockopt(fd, IPPROTO_IPV6, IPV6_V6ONLY, &v6only, sizeof(v6only));
<span class="cm">/* Binding :: (IPv6 any) now accepts IPv4-mapped IPv6 addresses (::ffff:x.x.x.x) */</span></pre></div>
  </div>
</div>
</div>
<!-- TAB 1 -->
<div id="t1" class="tab-pane">
<p class="sep">TCP SERVER PATTERNS</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🖥️</span><h3>Complete TCP Server Template</h3><span class="tag tag-green">TCP SERVER</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cs">#include &lt;sys/socket.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;</span>
<span class="ck">int</span> tcp_server(<span class="ck">uint16_t</span> port) {
    <span class="ck">int</span> lfd = socket(AF_INET6, SOCK_STREAM, 0);
 
    <span class="cm">/* SO_REUSEADDR: allow bind to port even if in TIME_WAIT */</span>
    <span class="ck">int</span> opt = 1;
    setsockopt(lfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    <span class="cm">/* SO_REUSEPORT: multiple processes can bind same port (load balance) */</span>
    setsockopt(lfd, SOL_SOCKET, SO_REUSEPORT, &opt, sizeof(opt));
 
    <span class="ck">struct</span> sockaddr_in6 addr = {0};
    addr.sin6_family = AF_INET6;
    addr.sin6_port   = htons(port);
    addr.sin6_addr   = in6addr_any;   <span class="cm">/* :: = any interface */</span>
 
    bind(lfd, (<span class="ck">struct</span> sockaddr *)&addr, sizeof(addr));
    listen(lfd, 128);  <span class="cm">/* backlog: max pending connections in accept queue */</span>
    <span class="ck">while</span> (1) {
        <span class="ck">struct</span> sockaddr_in6 client;
        socklen_t clen = sizeof(client);
        <span class="ck">int</span> cfd = accept(lfd, (<span class="ck">struct</span> sockaddr *)&client, &clen);
        <span class="cm">/* cfd is a NEW socket for this connection; lfd still listens */</span>
        <span class="cm">/* Handle client — in production: fork() or thread */</span>
        handle_client(cfd);
        close(cfd);
    }
}
 
<span class="ck">void</span> handle_client(<span class="ck">int</span> fd) {
    <span class="ck">char</span> buf[4096];
    ssize_t n;
    <span class="cm">/* CRITICAL: recv may return LESS than requested — MUST loop */</span>
    <span class="ck">while</span> ((n = recv(fd, buf, sizeof(buf), 0)) > 0) {
        <span class="cm">/* n bytes received; process buf[0..n-1] */</span>
        send(fd, buf, n, 0);  <span class="cm">/* echo back */</span>
        <span class="cm">/* send may also return less than n → must loop send too */</span>
    }
    <span class="cm">/* n == 0: peer closed connection (FIN received) */</span>
    <span class="cm">/* n == -1: error (check errno: EAGAIN, ECONNRESET, etc.) */</span>
}
 
<span class="cm">/* TCP client */</span>
<span class="ck">int</span> tcp_connect(<span class="ck">const char</span> *host, <span class="ck">uint16_t</span> port) {
    <span class="ck">struct</span> addrinfo hints = {0}, *res;
    hints.ai_family   = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    <span class="ck">char</span> portstr[8]; snprintf(portstr, sizeof(portstr), <span class="cs">"%u"</span>, port);
    getaddrinfo(host, portstr, &hints, &res);
 
    <span class="ck">int</span> fd = socket(res->ai_family, res->ai_socktype, 0);
    connect(fd, res->ai_addr, res->ai_addrlen);
    freeaddrinfo(res);
    <span class="ck">return</span> fd;
}</pre></div>
  </div>
</div>
</div>
<!-- TAB 2 -->
<div id="t2" class="tab-pane">
<p class="sep">UDP PROGRAMMING</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📡</span><h3>UDP Socket — sendto/recvfrom</h3><span class="tag tag-teal">UDP</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* UDP server — connectionless, per-datagram source address */</span>
<span class="ck">int</span> udp_server(<span class="ck">uint16_t</span> port) {
    <span class="ck">int</span> fd = socket(AF_INET, SOCK_DGRAM, 0);
    <span class="ck">struct</span> sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port   = htons(port);
    addr.sin_addr.s_addr = INADDR_ANY;
    bind(fd, (<span class="ck">struct</span> sockaddr *)&addr, sizeof(addr));
 
    <span class="ck">char</span> buf[65536];  <span class="cm">/* max UDP payload */</span>
    <span class="ck">while</span> (1) {
        <span class="ck">struct</span> sockaddr_in client;
        socklen_t clen = sizeof(client);
        ssize_t n = recvfrom(fd, buf, sizeof(buf), 0,
                            (<span class="ck">struct</span> sockaddr *)&client, &clen);
        <span class="cm">/* n == complete datagram size — UDP preserves message boundaries */</span>
        <span class="cm">/* client contains source IP+port for this packet */</span>
        sendto(fd, buf, n, 0, (<span class="ck">struct</span> sockaddr *)&client, clen);
    }
}
 
<span class="cm">/* UDP multicast sender */</span>
<span class="ck">int</span> udp_multicast_send(<span class="cs">const char</span> *group, <span class="ck">uint16_t</span> port) {
    <span class="ck">int</span> fd = socket(AF_INET, SOCK_DGRAM, 0);
    <span class="ck">struct</span> ip_mreq mreq;
    inet_aton(group, &mreq.imr_multiaddr);
    mreq.imr_interface.s_addr = INADDR_ANY;
    setsockopt(fd, IPPROTO_IP, IP_ADD_MEMBERSHIP, &mreq, sizeof(mreq));
    <span class="cm">/* TTL for multicast (default 1 = link-local) */</span>
    <span class="ck">unsigned char</span> ttl = 32;
    setsockopt(fd, IPPROTO_IP, IP_MULTICAST_TTL, &ttl, sizeof(ttl));
    <span class="ck">struct</span> sockaddr_in dst = {0};
    dst.sin_family = AF_INET;
    dst.sin_port   = htons(port);
    inet_aton(group, &dst.sin_addr);
    sendto(fd, <span class="cs">"hello multicast"</span>, 15, 0,
           (<span class="ck">struct</span> sockaddr *)&dst, sizeof(dst));
    <span class="ck">return</span> fd;
}</pre></div>
  </div>
</div>
</div>
<!-- TAB 3 -->
<div id="t3" class="tab-pane">
<p class="sep">NON-BLOCKING I/O AND epoll</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>epoll — Scalable I/O Multiplexing</h3><span class="tag tag-purple">EPOLL</span></div>
  <div class="cp-body">
    <p>The classic <code>select()</code> and <code>poll()</code> have O(n) scan overhead — with 10,000 fds, every call scans all 10,000 even if only 1 is ready. <code>epoll</code> maintains a kernel-side data structure and returns only the fds that are actually ready — O(1) per event, O(k) where k is ready events.</p>
<div class="cb"><pre><span class="cs">#include &lt;sys/epoll.h&gt;
#include &lt;fcntl.h&gt;</span>
<span class="cm">/* Set fd to non-blocking */</span>
<span class="ck">void</span> set_nonblocking(<span class="ck">int</span> fd) {
    <span class="ck">int</span> flags = fcntl(fd, F_GETFL, 0);
    fcntl(fd, F_SETFL, flags | O_NONBLOCK);
}
 
<span class="cm">/* Create epoll instance and event loop */</span>
<span class="ck">int</span> epoll_server(<span class="ck">int</span> lfd) {
    <span class="ck">int</span> epfd = epoll_create1(0);
 
    <span class="cm">/* Add listener to epoll */</span>
    <span class="ck">struct</span> epoll_event ev = { .events = EPOLLIN, .data.fd = lfd };
    epoll_ctl(epfd, EPOLL_CTL_ADD, lfd, &ev);
 
    <span class="ck">struct</span> epoll_event events[1024];
    <span class="ck">while</span> (1) {
        <span class="ck">int</span> n = epoll_wait(epfd, events, 1024, -1);  <span class="cm">/* -1 = block forever */</span>
        <span class="ck">for</span> (<span class="ck">int</span> i = 0; i < n; i++) {
            <span class="ck">if</span> (events[i].data.fd == lfd) {
                <span class="cm">/* New connection */</span>
                <span class="ck">int</span> cfd = accept(lfd, NULL, NULL);
                set_nonblocking(cfd);
                <span class="ck">struct</span> epoll_event cev = {
                    .events = EPOLLIN | EPOLLET,  <span class="cm">/* edge-triggered */</span>
                    .data.fd = cfd
                };
                epoll_ctl(epfd, EPOLL_CTL_ADD, cfd, &cev);
            } <span class="ck">else</span> {
                <span class="cm">/* Data ready on existing connection */</span>
                <span class="ck">char</span> buf[4096];
                ssize_t nr;
                <span class="cm">/* Edge-triggered: MUST read until EAGAIN */</span>
                <span class="ck">while</span> ((nr = recv(events[i].data.fd, buf, sizeof(buf), 0)) > 0)
                    process(buf, nr);
                <span class="ck">if</span> (nr == 0) {  <span class="cm">/* connection closed */</span>
                    epoll_ctl(epfd, EPOLL_CTL_DEL, events[i].data.fd, NULL);
                    close(events[i].data.fd);
                }
                <span class="cm">/* nr == -1 && errno == EAGAIN: no more data right now */</span>
            }
        }
    }
}
 
<span class="cm">/* Edge-triggered vs Level-triggered */</span>
<span class="cm"># EPOLLET (edge): notify ONCE when state changes (unread→readable)</span>
<span class="cm">#   Must read ALL data immediately or it won't be reported again</span>
<span class="cm">#   Higher performance (fewer epoll_wait wakeups)</span>
<span class="cm"># Level (default): notify every time data is available</span>
<span class="cm">#   Easier to code correctly; acceptable for most applications</span></pre></div>
  </div>
</div>
</div>
<!-- TAB 4 -->
<div id="t4" class="tab-pane">
<p class="sep">SOCKET OPTIONS — TUNING FOR PERFORMANCE</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>Critical Socket Options</h3><span class="tag tag-amber">SOCKOPTS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Option</th><th>Level</th><th>Effect</th><th>When to Use</th></tr></thead>
      <tbody>
        <tr><td><code>SO_REUSEADDR</code></td><td>SOL_SOCKET</td><td>Allow bind to port in TIME_WAIT state</td><td>Always on servers — prevents "address already in use" after restart</td></tr>
        <tr><td><code>SO_REUSEPORT</code></td><td>SOL_SOCKET</td><td>Multiple sockets bind same IP:port; kernel load-balances</td><td>Multi-process/thread servers (Nginx, high-performance servers)</td></tr>
        <tr><td><code>SO_KEEPALIVE</code></td><td>SOL_SOCKET</td><td>Send TCP keepalive probes; detect dead connections</td><td>Long-lived connections; detect peer disappear without data</td></tr>
        <tr><td><code>SO_RCVBUF</code></td><td>SOL_SOCKET</td><td>Set receive buffer size (kernel doubles the value)</td><td>High-bandwidth connections; increase for long fat networks</td></tr>
        <tr><td><code>SO_SNDBUF</code></td><td>SOL_SOCKET</td><td>Set send buffer size</td><td>High-throughput senders; typically let autotuning manage</td></tr>
        <tr><td><code>TCP_NODELAY</code></td><td>IPPROTO_TCP</td><td>Disable Nagle's algorithm — send immediately</td><td>Low-latency protocols (RPC, gaming, trading); penalises small writes</td></tr>
        <tr><td><code>TCP_CORK</code></td><td>IPPROTO_TCP</td><td>Buffer all data until cork removed or MSS reached</td><td>HTTP/file transfers — batch headers+body into one segment</td></tr>
        <tr><td><code>TCP_QUICKACK</code></td><td>IPPROTO_TCP</td><td>Disable delayed ACK</td><td>Latency-sensitive request-response protocols</td></tr>
        <tr><td><code>IP_TOS</code></td><td>IPPROTO_IP</td><td>Set DSCP/TOS field in outgoing IP packets</td><td>QoS marking for VoIP, streaming, or traffic shaping</td></tr>
        <tr><td><code>SO_TIMESTAMP</code></td><td>SOL_SOCKET</td><td>Receive hardware/kernel timestamp with each packet via cmsg</td><td>Latency measurement, PTP, network monitoring</td></tr>
      </tbody>
    </table>
<div class="cb"><pre><span class="cm">/* Setting socket options */</span>
<span class="ck">int</span> opt = 1;
setsockopt(fd, SOL_SOCKET,   SO_REUSEADDR, &opt, sizeof(opt));
setsockopt(fd, SOL_SOCKET,   SO_REUSEPORT, &opt, sizeof(opt));
setsockopt(fd, IPPROTO_TCP,  TCP_NODELAY,  &opt, sizeof(opt));
 
<span class="ck">int</span> bufsize = 4 * 1024 * 1024;  <span class="cm">/* 4MB */</span>
setsockopt(fd, SOL_SOCKET, SO_RCVBUF, &bufsize, sizeof(bufsize));
setsockopt(fd, SOL_SOCKET, SO_SNDBUF, &bufsize, sizeof(bufsize));
 
<span class="cm">/* TCP keepalive tuning */</span>
<span class="ck">int</span> idle = 60, interval = 10, count = 3;
setsockopt(fd, IPPROTO_TCP, TCP_KEEPIDLE,  &idle,     sizeof(idle));
setsockopt(fd, IPPROTO_TCP, TCP_KEEPINTVL, &interval, sizeof(interval));
setsockopt(fd, IPPROTO_TCP, TCP_KEEPCNT,   &count,    sizeof(count));
<span class="cm">/* After 60s idle: send probe every 10s, 3 times → declare dead after 30s */</span>
<span class="cm">/* Read back effective buffer size */</span>
<span class="ck">int</span> actual; socklen_t alen = sizeof(actual);
getsockopt(fd, SOL_SOCKET, SO_RCVBUF, &actual, &alen);
<span class="cm">/* actual may be 2× requested (kernel doubles for overhead) */</span></pre></div>
  </div>
</div>
</div>
<!-- TAB 5 -->
<div id="t5" class="tab-pane">
<p class="sep">RAW SOCKETS — CRAFTING ARBITRARY IP PACKETS</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Raw IP Sockets</h3><span class="tag tag-red">RAW SOCKETS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Raw socket — receive ALL IP packets of a given protocol */</span>
<span class="cm">/* Requires CAP_NET_RAW or root */</span>
<span class="ck">int</span> fd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);  <span class="cm">/* all ICMP */</span>
<span class="ck">int</span> fd = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);   <span class="cm">/* all TCP (also received by TCP stack) */</span>
<span class="ck">int</span> fd = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);   <span class="cm">/* send-only; craft own IP header */</span>
<span class="cm">/* Send a custom ICMP echo request */</span>
<span class="ck">struct</span> {
    <span class="ck">struct</span> icmphdr hdr;
    <span class="ck">char</span>           data[56];
} pkt;
pkt.hdr.type     = ICMP_ECHO;
pkt.hdr.code     = 0;
pkt.hdr.un.echo.id  = htons(getpid());
pkt.hdr.un.echo.sequence = htons(1);
pkt.hdr.checksum = 0;
pkt.hdr.checksum = checksum(&pkt, sizeof(pkt));
 
<span class="ck">struct</span> sockaddr_in dst;
dst.sin_family = AF_INET;
inet_aton(<span class="cs">"8.8.8.8"</span>, &dst.sin_addr);
 
<span class="ck">int</span> raw = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
sendto(raw, &pkt, sizeof(pkt), 0, (<span class="ck">struct</span> sockaddr *)&dst, sizeof(dst));
 
<span class="cm">/* Receive: kernel prepends IP header on recvfrom */</span>
<span class="ck">char</span> rbuf[1024];
recv(raw, rbuf, sizeof(rbuf), 0);
<span class="ck">struct</span> iphdr   *ip   = (<span class="ck">struct</span> iphdr *)rbuf;
<span class="ck">struct</span> icmphdr *icmp = (<span class="ck">struct</span> icmphdr *)(rbuf + ip->ihl * 4);
 
<span class="cm">/* IP_HDRINCL — you supply your own IP header */</span>
<span class="ck">int</span> opt = 1;
setsockopt(raw, IPPROTO_IP, IP_HDRINCL, &opt, sizeof(opt));
<span class="cm">/* Now sendto() includes your crafted IP header in the buffer */</span></pre></div>
  </div>
</div>
</div>
<!-- TAB 6 -->
<div id="t6" class="tab-pane">
<p class="sep">AF_PACKET — RAW LAYER 2 SOCKET</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>AF_PACKET — Capture and Inject Raw Frames</h3><span class="tag tag-blue">AF_PACKET</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* AF_PACKET — access raw Ethernet frames */</span>
<span class="cm">/* Foundation of tcpdump, Wireshark, and custom packet generators */</span>
<span class="cs">#include &lt;linux/if_packet.h&gt;
#include &lt;net/ethernet.h&gt;
#include &lt;net/if.h&gt;</span>
<span class="cm">/* Open raw L2 socket — receives ALL Ethernet frames */</span>
<span class="ck">int</span> fd = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
 
<span class="cm">/* Bind to specific interface */</span>
<span class="ck">struct</span> sockaddr_ll sll = {0};
sll.sll_family   = AF_PACKET;
sll.sll_ifindex  = if_nametoindex(<span class="cs">"eth0"</span>);
sll.sll_protocol = htons(ETH_P_ALL);
bind(fd, (<span class="ck">struct</span> sockaddr *)&sll, sizeof(sll));
 
<span class="cm">/* Set promiscuous mode (receive frames not destined for us) */</span>
<span class="ck">struct</span> packet_mreq mreq = {0};
mreq.mr_ifindex = sll.sll_ifindex;
mreq.mr_type    = PACKET_MR_PROMISC;
setsockopt(fd, SOL_PACKET, PACKET_ADD_MEMBERSHIP, &mreq, sizeof(mreq));
 
<span class="cm">/* Receive raw Ethernet frame */</span>
<span class="ck">unsigned char</span> frame[2048];
ssize_t n = recv(fd, frame, sizeof(frame), 0);
<span class="ck">struct</span> ethhdr *eth = (<span class="ck">struct</span> ethhdr *)frame;
<span class="cm">/* eth->h_dest, eth->h_source, eth->h_proto */</span>
<span class="cm">/* PACKET_MMAP — zero-copy ring buffer for high-speed capture */</span>
<span class="cm">/* Maps NIC DMA buffers directly into process address space */</span>
<span class="cm">/* Used by tcpdump/libpcap for high-performance capture */</span>
<span class="ck">struct</span> tpacket_req req = {
    .tp_block_size = 4096,
    .tp_block_nr   = 64,
    .tp_frame_size = 2048,
    .tp_frame_nr   = 128
};
setsockopt(fd, SOL_PACKET, PACKET_RX_RING, &req, sizeof(req));
<span class="ck">void</span> *ring = mmap(NULL, req.tp_block_size * req.tp_block_nr,
                  PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);
<span class="cm">/* Poll ring directly — no syscall per packet */</span></pre></div>
    <div class="ins"><p>💡 <strong>AF_PACKET is how tcpdump/libpcap work.</strong> Every packet you've ever captured with Wireshark passed through an AF_PACKET socket. The PACKET_MMAP extension maps the NIC's DMA ring into userspace for zero-copy capture — this is how Wireshark achieves high capture rates. Your DPDK knowledge directly informs why this is still slower than full kernel bypass.</p></div>
  </div>
</div>
</div>
<!-- TAB 7 -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Multi-Connection TCP Server with epoll</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a fully functional non-blocking TCP echo server using epoll that handles 1000+ simultaneous connections without threads.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement the epoll event loop from the code in Tab 3. Use EPOLLET (edge-triggered) mode. Handle: new connections (accept), incoming data (read loop until EAGAIN), connection close (EPOLLHUP/recv returns 0), errors (EPOLLERR).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Set all accepted sockets to non-blocking with <code>fcntl(fd, F_SETFL, O_NONBLOCK)</code>. Set <code>TCP_NODELAY</code> and <code>SO_REUSEPORT</code>. Add a per-connection state structure (track bytes received, connection ID).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Load test with <code>ab -n 100000 -c 1000 http://localhost:8080/</code> or a custom C client. Measure: connections/second, max concurrent connections, memory per connection. Compare with a fork-per-connection server under the same load.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add SO_REUSEPORT: run 4 instances of your server on the same port (set different process IDs). Verify with <code>ss -tlnp | grep 8080</code> that all 4 are bound. Use <code>ab</code> to send 40,000 requests and verify even distribution across processes.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Raw Packet Craft and AF_PACKET Capture</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Write a minimal packet sniffer using AF_PACKET, then craft custom ICMP packets with raw sockets.</p>
    <div class="lab-step"><div class="sn">1</div><div>Write a packet sniffer: AF_PACKET socket, promiscuous mode, read loop. For each received frame: print timestamp, Ethernet src/dst MACs, EtherType. If EtherType=0x0800 (IPv4), also parse the IP header (src/dst IP, protocol, TTL). If protocol=ICMP, print type/code.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Run your sniffer and generate traffic: ping, curl a website, start a TCP connection. Verify your sniffer correctly identifies all frame types. Compare output with tcpdump running in parallel on the same interface.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Write an ICMP ping with raw sockets (SOCK_RAW, IPPROTO_ICMP). Calculate the ICMP checksum. Send to 8.8.8.8 and receive the reply. Parse the reply to extract RTT (measure time between send and receive). Implement 5 pings and show min/avg/max RTT.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Socket Performance Benchmarking</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Measure the impact of socket options on latency and throughput.</p>
    <div class="lab-step"><div class="sn">1</div><div>Write a benchmark that sends 1-byte request, receives 1-byte response, measures RTT. Test with TCP_NODELAY on vs off. Expected: TCP_NODELAY on = ~0.2ms; off = up to 40ms (Nagle delay). The 200× difference illustrates why TCP_NODELAY matters for latency-sensitive code.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Measure SO_RCVBUF impact on throughput: send 1GB over TCP with recv buffer at 4KB vs 256KB vs 4MB. Use iperf3 as reference. Explain why buffer size affects throughput on a high-latency link (BDP = bandwidth × delay).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Compare select vs poll vs epoll with 1000 file descriptors: open 1000 socket-pairs, use each API to wait for activity on all 1000. Measure time per call. Document the O(n) vs O(1) difference empirically.</div></div>
  </div>
</div>
</div>
<!-- TAB 8 -->
<div id="t8" class="tab-pane">
<p class="sep">M15 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know socket() parameters: AF_INET/INET6/UNIX/PACKET, SOCK_STREAM/DGRAM/RAW, protocol values</li>
  <li>Know byte order: network = big-endian; always use htons/htonl for ports/IPs in structs</li>
  <li>Know sockaddr_in fields: sin_family, sin_port (htons), sin_addr.s_addr</li>
  <li>Know TCP server sequence: socket → setsockopt(REUSEADDR) → bind → listen → accept loop</li>
  <li>Know that recv may return less than requested — always loop recv for stream sockets</li>
  <li>Know TCP client sequence: socket → getaddrinfo → connect → send/recv</li>
  <li>Know recv returns 0 on EOF (peer closed), -1 on error (check errno)</li>
  <li>Know UDP differences: sendto/recvfrom, message boundaries preserved, no connect needed</li>
  <li>Know why epoll outperforms select/poll at scale: O(1) per ready event vs O(n) scan</li>
  <li>Know epoll API: epoll_create1, epoll_ctl (ADD/MOD/DEL), epoll_wait</li>
  <li>Know edge-triggered vs level-triggered: ET fires once on state change (must read to EAGAIN), LT fires while data present</li>
  <li>Know SO_REUSEADDR: allow bind in TIME_WAIT — always set on servers</li>
  <li>Know SO_REUSEPORT: multiple processes bind same port, kernel load-balances</li>
  <li>Know TCP_NODELAY: disables Nagle's algorithm, reduces latency for small writes</li>
  <li>Know TCP keepalive options: TCP_KEEPIDLE, TCP_KEEPINTVL, TCP_KEEPCNT</li>
  <li>Know raw sockets require CAP_NET_RAW; receive all packets of specified IP protocol</li>
  <li>Know IP_HDRINCL: allows crafting custom IP header in SOCK_RAW</li>
  <li>Know AF_PACKET: raw Ethernet frame access; foundation of tcpdump/libpcap/Wireshark</li>
  <li>Know PACKET_MMAP: zero-copy ring buffer for high-speed capture in AF_PACKET</li>
  <li>Completed Lab 1: built epoll-based non-blocking server, benchmarked under 1000 concurrent connections</li>
  <li>Completed Lab 2: wrote packet sniffer with AF_PACKET, crafted ICMP with raw sockets</li>
  <li>Completed Lab 3: benchmarked TCP_NODELAY, buffer size, and select/poll/epoll performance</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M16 - eBPF and XDP</strong> — the most exciting recent addition to the Linux networking toolkit, enabling programmable packet processing without kernel modifications.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/networking-mastery/m14-linux-stack/">← M14 Linux Stack</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m16-ebpf-xdp/">Next: M16 - eBPF/XDP →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
