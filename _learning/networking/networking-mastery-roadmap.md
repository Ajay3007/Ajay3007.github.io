---
layout: learning
title: "Networking Mastery Roadmap"
permalink: /learning/networking-mastery/
---
<style>
/* ── Hero ─────────────────────────────────────────── */
.rmap-hero{
  background:linear-gradient(135deg,#0a1628 0%,#1a3a5c 40%,#0f6e56 75%,#8c2020 100%);
  border-radius:12px;padding:2.2rem 2rem 1.8rem;color:#fff;margin-bottom:2rem;
  position:relative;overflow:hidden;
}
.rmap-hero::before{
  content:'';position:absolute;top:-60px;right:-60px;width:220px;height:220px;
  border-radius:50%;background:rgba(255,255,255,.04);
}
.rmap-hero::after{
  content:'';position:absolute;bottom:-40px;left:30%;width:300px;height:300px;
  border-radius:50%;background:rgba(26,122,110,.08);
}
.rmap-hero-eye{
  font-size:.7rem;font-family:monospace;letter-spacing:.14em;
  color:#7ab8d8;text-transform:uppercase;margin-bottom:.5rem;
}
.rmap-hero h1{
  font-size:2rem;font-weight:800;color:#fff;border:none;
  margin:.3rem 0 .6rem;letter-spacing:-.02em;position:relative;z-index:1;
}
.rmap-hero p{color:#a8cce0;font-size:.92rem;margin:0 0 1rem;line-height:1.6;position:relative;z-index:1;}
.rmap-hero-tags{display:flex;flex-wrap:wrap;gap:.5rem;position:relative;z-index:1;}
.rmap-tag{
  background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);
  border-radius:20px;padding:3px 12px;font-size:.72rem;
  font-family:monospace;color:#c8e4f4;
}

/* ── Summary cards ────────────────────────────────── */
.summary-grid{
  display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));
  gap:.8rem;margin:1.5rem 0;
}
.sg-card{
  background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);
  border-radius:8px;padding:.8rem 1rem;text-align:center;
}
.sg-num{font-size:1.8rem;font-weight:800;display:block;line-height:1;}
.sg-lbl{
  font-size:.72rem;color:var(--light-text,#666);text-transform:uppercase;
  letter-spacing:.06em;font-family:monospace;display:block;margin-top:.2rem;
}

/* ── Phase timeline ───────────────────────────────── */
.phase-timeline{position:relative;margin:2rem 0;}
.phase-timeline::before{
  content:'';position:absolute;left:27px;top:10px;bottom:10px;width:3px;
  background:linear-gradient(180deg,#1a3a5c 0%,#0f6e56 25%,#c05e1b 50%,#5b3a8c 75%,#8c2020 100%);
  border-radius:2px;
}

.pt-phase{display:flex;gap:1.2rem;margin-bottom:2rem;position:relative;}
.pt-dot{
  width:56px;height:56px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-size:1.1rem;font-weight:800;color:#fff;flex-shrink:0;
  z-index:1;border:3px solid #fff;box-shadow:0 2px 10px rgba(0,0,0,.18);
}
.pt-body{
  flex:1;background:var(--card-bg,#fff);
  border:1.5px solid var(--border-color,#e4e4e4);
  border-radius:10px;padding:1rem 1.2rem;margin-top:.2rem;
}
.pt-header{display:flex;align-items:flex-start;gap:.8rem;flex-wrap:wrap;margin-bottom:.5rem;}
.pt-title{font-size:1.05rem;font-weight:700;color:var(--text-color,#111);margin:0;}
.pt-weeks{
  font-size:.72rem;font-family:monospace;padding:3px 10px;
  border-radius:12px;font-weight:700;white-space:nowrap;margin-top:.1rem;
}
.pt-desc{font-size:.87rem;color:var(--text-color,#444);line-height:1.65;margin-bottom:.8rem;}

/* Module link chips */
.pt-modules{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:.8rem;}
.pt-mod{
  display:inline-flex;align-items:center;gap:.35rem;
  padding:.28rem .75rem;border-radius:6px;font-size:.79rem;
  font-family:monospace;font-weight:600;
  text-decoration:none !important;border:1.5px solid;
  transition:opacity .15s,transform .1s;
  color:var(--text-color,#222);
}
.pt-mod:hover{opacity:.75;transform:translateY(-1px);}
.pt-mod-coming{
  display:inline-flex;align-items:center;gap:.35rem;
  padding:.28rem .75rem;border-radius:6px;font-size:.79rem;
  font-family:monospace;font-weight:600;border:1.5px dashed;
  opacity:.55;color:var(--light-text,#888);
}

/* Skill tags */
.pt-skills{display:flex;flex-wrap:wrap;gap:.35rem;margin-bottom:.5rem;}
.skill-tag{
  font-size:.72rem;background:var(--bg-color,#f0f0f0);
  color:var(--light-text,#555);border-radius:4px;
  padding:2px 8px;font-family:monospace;
}

/* Project chips */
.proj-chip{
  display:inline-flex;align-items:center;gap:.35rem;
  font-size:.78rem;font-family:monospace;padding:3px 10px;
  border-radius:6px;font-weight:600;margin-top:.4rem;margin-right:.3rem;
}

/* Dependency note */
.dep-note{
  font-size:.8rem;color:var(--light-text,#666);
  background:var(--bg-color,#f5f5f5);
  border-radius:6px;padding:.4rem .7rem;margin-top:.6rem;
  border-left:3px solid #1a7a6e;line-height:1.55;
}
[data-theme=dark] .dep-note{background:#0d2020;border-left-color:#2a9a8e;}

/* Advanced badge */
.adv-banner{
  background:linear-gradient(90deg,#1e0a0a,#3a1010);
  border:1.5px solid #8c2020;border-radius:8px;
  padding:.6rem 1rem;margin:1.5rem 0 .5rem;
  display:flex;align-items:center;gap:.8rem;
}
.adv-banner-icon{font-size:1.2rem;}
.adv-banner-text{font-size:.82rem;color:#f0c0c0;line-height:1.5;}
.adv-banner-text strong{color:#ffaaaa;}
[data-theme=dark] .adv-banner{background:#2a0808;border-color:#a03030;}

/* Full module table */
.mod-full-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem;}
.mod-full-table th{
  background:#1a3a5c;color:#fff;padding:.5rem .9rem;
  text-align:left;font-size:.77rem;font-weight:700;
  font-family:monospace;letter-spacing:.04em;
}
.mod-full-table td{
  padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);
  color:var(--text-color,#222);vertical-align:top;
}
.mod-full-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8);}
.mod-full-table code{
  font-size:.79rem;background:rgba(0,0,0,.06);
  padding:1px 5px;border-radius:3px;color:#1a7a6e;
}
.phase-badge{
  font-size:.7rem;font-family:monospace;font-weight:700;
  padding:2px 8px;border-radius:4px;
}

/* Section divider */
.sep{
  font-size:.7rem;font-family:monospace;font-weight:700;
  letter-spacing:.1em;text-transform:uppercase;
  color:var(--light-text,#888);margin:2rem 0 .8rem;
  padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee);
}

/* Nav */
.mod-nav{
  display:flex;justify-content:space-between;align-items:center;
  flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;
  padding-top:1.2rem;border-top:1px solid var(--border-color,#eee);
}
.mod-nav a{
  display:inline-flex;align-items:center;gap:.4rem;
  padding:.5rem 1rem;border-radius:7px;
  background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);
  font-size:.85rem;font-weight:600;
  color:var(--text-color,#333) !important;text-decoration:none !important;
  transition:background .15s;
}
.mod-nav a:hover{background:var(--bg-color,#ebebeb);}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c;}
.mod-nav .nb:hover{background:#245280;}
</style>

<!-- ═══════════════════════════ HERO ═══════════════════════════ -->
<div class="rmap-hero">
  <div class="rmap-hero-eye">NETWORKING MASTERY · FULL ROADMAP · 6 PHASES · 26 MODULES</div>
  <h1>🌐 Networking Mastery</h1>
  <p>A structured 6-month curriculum — from absolute networking basics through routing internals, Linux kernel networking, security protocols, and full NGFW application development. Built for engineers working on data-plane, router, and Next-Generation Firewall systems.</p>
  <div class="rmap-hero-tags">
    <span class="rmap-tag">Beginner → Advanced</span>
    <span class="rmap-tag">C / C++ / Python</span>
    <span class="rmap-tag">Linux Networking</span>
    <span class="rmap-tag">Socket Programming</span>
    <span class="rmap-tag">TLS / IPsec</span>
    <span class="rmap-tag">DPI / IDS / IPS</span>
    <span class="rmap-tag">NGFW Development</span>
    <span class="rmap-tag">26 weeks · 20+ Projects</span>
  </div>
</div>

<!-- ═════════════════════════ SUMMARY ═════════════════════════ -->
<div class="summary-grid">
  <div class="sg-card"><span class="sg-num" style="color:#1a3a5c">6</span><span class="sg-lbl">Phases</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#0f6e56">26</span><span class="sg-lbl">Modules</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#c05e1b">20+</span><span class="sg-lbl">Projects</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#5b3a8c">26</span><span class="sg-lbl">Weeks</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#8c2020">NGFW</span><span class="sg-lbl">Capstone</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#1a7a6e">0→1</span><span class="sg-lbl">Beginner OK</span></div>
</div>

<p class="sep">PHASE TIMELINE</p>

<!-- ═════════════════════════ TIMELINE ════════════════════════ -->
<div class="phase-timeline">

  <!-- ── PHASE 1 ── -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#1a3a5c;">1</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Networking Foundations</div>
        <span class="pt-weeks" style="background:#e8f1f9;color:#1a3a5c;">Weeks 1–3</span>
      </div>
      <div class="pt-desc">
        Start from zero. Understand how data moves through a network — from the physical wire all the way to your application. Covers the OSI and TCP/IP models, Ethernet framing, IP addressing and subnetting, ARP, ICMP, VLANs, and IPv6. Every subsequent phase builds directly on this foundation.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m01-osi-tcpip/' | relative_url }}"
           style="background:#eaf2fc;border-color:#b0ccec;color:#1a3a5c;">📡 M01 - OSI and TCP/IP Model</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m02-ethernet-l2/' | relative_url }}"
           style="background:#eaf2fc;border-color:#b0ccec;color:#1a3a5c;">🔌 M02 - Ethernet and L2</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m03-ipv4/' | relative_url }}"
           style="background:#eaf2fc;border-color:#b0ccec;color:#1a3a5c;">🌐 M03 - IPv4 Deep Dive</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m04-ipv6/' | relative_url }}"
           style="background:#eaf2fc;border-color:#b0ccec;color:#1a3a5c;">🔵 M04 - IPv6</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">OSI layers</span>
        <span class="skill-tag">Ethernet frames</span>
        <span class="skill-tag">MAC addressing</span>
        <span class="skill-tag">ARP / NDP</span>
        <span class="skill-tag">IPv4 subnetting</span>
        <span class="skill-tag">CIDR</span>
        <span class="skill-tag">ICMP</span>
        <span class="skill-tag">VLANs / 802.1Q</span>
        <span class="skill-tag">IPv6 addressing</span>
        <span class="skill-tag">dual-stack</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#e8f1f9;color:#1a3a5c;">🔬 Lab: Wireshark packet dissection</span>
        <span class="proj-chip" style="background:#e8f1f9;color:#1a3a5c;">🔬 Lab: Subnet a /20 by hand</span>
      </div>
    </div>
  </div>

  <!-- ── PHASE 2 ── -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#0f6e56;">2</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Transport and Application Protocols</div>
        <span class="pt-weeks" style="background:#e0f0ee;color:#0a3a30;">Weeks 4–7</span>
      </div>
      <div class="pt-desc">
        Go deep into how data is reliably delivered and how the most important application protocols work at the byte level. TCP state machine, flow control, congestion control, and timers. UDP, DNS, HTTP/1.1 through HTTP/3 with QUIC, and the protocols a firewall must inspect — SMTP, FTP, DHCP. This is where NGFW L7 visibility starts.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m05-tcp/' | relative_url }}"
           style="background:#e0f6f0;border-color:#90c8b8;color:#0a3a30;">⚡ M05 - TCP Internals</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m06-udp-icmp/' | relative_url }}"
           style="background:#e0f6f0;border-color:#90c8b8;color:#0a3a30;">📦 M06 - UDP and ICMP</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m07-dns/' | relative_url }}"
           style="background:#e0f6f0;border-color:#90c8b8;color:#0a3a30;">🔍 M07 - DNS</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m08-http/' | relative_url }}"
           style="background:#e0f6f0;border-color:#90c8b8;color:#0a3a30;">🌍 M08 - HTTP/1.1, HTTP/2, HTTP/3 and QUIC</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m09-app-protocols/' | relative_url }}"
           style="background:#e0f6f0;border-color:#90c8b8;color:#0a3a30;">📨 M09 - SMTP, FTP, DHCP</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">TCP state machine</span>
        <span class="skill-tag">3-way handshake</span>
        <span class="skill-tag">flow control</span>
        <span class="skill-tag">congestion control</span>
        <span class="skill-tag">NewReno / CUBIC</span>
        <span class="skill-tag">SACK</span>
        <span class="skill-tag">DNS resolution</span>
        <span class="skill-tag">DNSSEC</span>
        <span class="skill-tag">HTTP/2 streams</span>
        <span class="skill-tag">QUIC / IETF</span>
        <span class="skill-tag">SMTP envelope</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#e0f6f0;color:#0a3a30;">🔬 Lab: Trace a TCP handshake in tcpdump</span>
        <span class="proj-chip" style="background:#e0f6f0;color:#0a3a30;">🔬 Lab: Build a DNS resolver in Python</span>
        <span class="proj-chip" style="background:#e0f6f0;color:#0a3a30;">🔬 Lab: Capture and decode HTTP/2 frames</span>
      </div>
      <div class="dep-note">📌 Prerequisite: Phase 1 complete. TCP builds directly on IPv4 packet structure.</div>
    </div>
  </div>

  <!-- ── PHASE 3 ── -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#c05e1b;">3</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Routing and Forwarding</div>
        <span class="pt-weeks" style="background:#faeee4;color:#6a2800;">Weeks 8–11</span>
      </div>
      <div class="pt-desc">
        How packets find their path across networks. Covers the FIB/RIB split, longest prefix match algorithms, ECMP, OSPF link-state routing internals, BGP path selection and policy, MPLS label switching, and overlay tunneling (VxLAN, GRE). Essential for data-plane engineers and anyone building router software or firewall routing tables.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m10-routing-fundamentals/' | relative_url }}"
           style="background:#faeee4;border-color:#e8b890;color:#6a2800;">🗺️ M10 - Routing Fundamentals and FIB</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m11-ospf/' | relative_url }}"
           style="background:#faeee4;border-color:#e8b890;color:#6a2800;">🔄 M11 - OSPF Internals</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m12-bgp/' | relative_url }}"
           style="background:#faeee4;border-color:#e8b890;color:#6a2800;">🌍 M12 - BGP Internals</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m13-tunneling/' | relative_url }}"
           style="background:#faeee4;border-color:#e8b890;color:#6a2800;">🔗 M13 - MPLS, VxLAN, GRE and Tunneling</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">FIB / RIB</span>
        <span class="skill-tag">LPM</span>
        <span class="skill-tag">ECMP</span>
        <span class="skill-tag">OSPF LSA types</span>
        <span class="skill-tag">SPF algorithm</span>
        <span class="skill-tag">BGP attributes</span>
        <span class="skill-tag">AS path</span>
        <span class="skill-tag">route policy</span>
        <span class="skill-tag">MPLS labels</span>
        <span class="skill-tag">VxLAN VTEP</span>
        <span class="skill-tag">GRE tunnels</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#faeee4;color:#6a2800;">🔬 Lab: Implement LPM in C using a trie</span>
        <span class="proj-chip" style="background:#faeee4;color:#6a2800;">🔬 Lab: Simulate OSPF convergence with GNS3</span>
        <span class="proj-chip" style="background:#faeee4;color:#6a2800;">🔬 Lab: BGP peering between two Linux routers</span>
      </div>
      <div class="dep-note">📌 Prerequisite: IPv4 (M03) and TCP (M05). Routing builds on L3 fundamentals.</div>
    </div>
  </div>

  <!-- ── PHASE 4 ── -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#5b3a8c;">4</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Linux Networking and Socket Programming</div>
        <span class="pt-weeks" style="background:#ede8f5;color:#3a1a6c;">Weeks 12–16</span>
      </div>
      <div class="pt-desc">
        The implementation layer — where your C code actually runs. Covers the Linux kernel network stack (sk_buff, netdev, Netfilter, tc), POSIX socket programming from scratch (TCP servers, UDP, non-blocking I/O, epoll), raw and packet sockets, eBPF/XDP for kernel bypass, and high-performance techniques: NUMA-aware design, RSS, CPU affinity, io_uring, AF_XDP. This phase bridges theory and production code.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m14-linux-stack/' | relative_url }}"
           style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c;">🐧 M14 - Linux Network Stack</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m15-sockets/' | relative_url }}"
           style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c;">🔌 M15 - Socket Programming in C</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m16-ebpf-xdp/' | relative_url }}"
           style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c;">🔬 M16 - Raw Sockets, pcap and eBPF</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m17-dpdk/' | relative_url }}"
           style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c;">🚀 M17 - Kernel Bypass and XDP</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m18-vpp/' | relative_url }}"
           style="background:#ede8f5;border-color:#c0a8e8;color:#3a1a6c;">⚡ M18 - High-Performance Techniques</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">sk_buff</span>
        <span class="skill-tag">netfilter hooks</span>
        <span class="skill-tag">iptables internals</span>
        <span class="skill-tag">tc / qdisc</span>
        <span class="skill-tag">POSIX sockets</span>
        <span class="skill-tag">epoll</span>
        <span class="skill-tag">non-blocking I/O</span>
        <span class="skill-tag">raw sockets</span>
        <span class="skill-tag">eBPF / XDP</span>
        <span class="skill-tag">AF_XDP</span>
        <span class="skill-tag">io_uring</span>
        <span class="skill-tag">RSS / RPS</span>
        <span class="skill-tag">NUMA</span>
        <span class="skill-tag">CPU affinity</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#ede8f5;color:#3a1a6c;">🔨 Project: TCP echo server with epoll (C)</span>
        <span class="proj-chip" style="background:#ede8f5;color:#3a1a6c;">🔨 Project: Raw socket packet sniffer</span>
        <span class="proj-chip" style="background:#ede8f5;color:#3a1a6c;">🔨 Project: eBPF packet counter and dropper</span>
        <span class="proj-chip" style="background:#ede8f5;color:#3a1a6c;">🔨 Project: AF_XDP zero-copy forwarder</span>
      </div>
      <div class="dep-note">📌 Prerequisite: Phases 1–3. Socket programming requires solid TCP/IP knowledge. C programming basics assumed.</div>
    </div>
  </div>

  <!-- ── ADVANCED BANNER ── -->
  <div class="adv-banner">
    <span class="adv-banner-icon">🔐</span>
    <div class="adv-banner-text">
      <strong>Advanced territory begins here.</strong>
      Phases 5 and 6 require a solid foundation in all of the above. Phase 5 covers security protocol internals at the implementation level. Phase 6 is NGFW application development — bringing everything together into a production system.
    </div>
  </div>

  <!-- ── PHASE 5 ── -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#8c4a00;">5</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Security Protocols and Cryptography</div>
        <span class="pt-weeks" style="background:#fdf0e0;color:#5a2800;">Weeks 17–21</span>
      </div>
      <div class="pt-desc">
        The cryptographic and protocol foundation of every NGFW feature. Covers symmetric and asymmetric cryptography, PKI, X.509 certificate chains, TLS 1.2 and TLS 1.3 handshake internals (cipher suites, ALPN, session resumption), IPsec (ESP, AH, IKEv2, tunnel vs transport mode), DTLS, mutual TLS, and SSL inspection techniques used by NGFWs to decrypt and re-encrypt traffic for inspection.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m19-cryptography/' | relative_url }}"
           style="background:#fdf0e0;border-color:#e8c080;color:#5a2800;">🔑 M19 - Cryptography Essentials</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m20-tls/' | relative_url }}"
           style="background:#fdf0e0;border-color:#e8c080;color:#5a2800;">🔒 M20 - TLS 1.2 and TLS 1.3 Internals</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m21-ipsec/' | relative_url }}"
           style="background:#fdf0e0;border-color:#e8c080;color:#5a2800;">🛡️ M21 - IPsec and IKEv2</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m22-ssl-inspection/' | relative_url }}"
           style="background:#fdf0e0;border-color:#e8c080;color:#5a2800;">🔍 M22 - DTLS, mTLS and SSL Inspection</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">AES / ChaCha20</span>
        <span class="skill-tag">RSA / ECDSA</span>
        <span class="skill-tag">ECDH key exchange</span>
        <span class="skill-tag">PKI / X.509</span>
        <span class="skill-tag">certificate chains</span>
        <span class="skill-tag">TLS handshake</span>
        <span class="skill-tag">cipher suites</span>
        <span class="skill-tag">ALPN / SNI</span>
        <span class="skill-tag">session tickets</span>
        <span class="skill-tag">ESP / AH</span>
        <span class="skill-tag">IKEv2</span>
        <span class="skill-tag">VPN tunnels</span>
        <span class="skill-tag">SSL bump</span>
        <span class="skill-tag">certificate pinning</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#fdf0e0;color:#5a2800;">🔨 Project: TLS 1.3 handshake step-by-step with OpenSSL</span>
        <span class="proj-chip" style="background:#fdf0e0;color:#5a2800;">🔨 Project: Build a simple IKEv2 client in Python</span>
        <span class="proj-chip" style="background:#fdf0e0;color:#5a2800;">🔨 Project: SSL inspection proxy (mitmproxy internals)</span>
      </div>
      <div class="dep-note">📌 Prerequisite: TCP (M05), HTTP (M08). TLS runs over TCP and wraps HTTP — you need both to understand the full picture.</div>
    </div>
  </div>

  <!-- ── PHASE 6 ── -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#8c2020;">6</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">NGFW Development</div>
        <span class="pt-weeks" style="background:#faeaea;color:#5a0a0a;">Weeks 22–26</span>
      </div>
      <div class="pt-desc">
        Everything comes together. Build a Next-Generation Firewall from the ground up. Stateful connection tracking, NAT44/NAT64, ALGs for FTP/SIP. Deep Packet Inspection (DPI) using Hyperscan and nDPI for L7 application classification. IDS/IPS with Snort/Suricata rule engine and signature matching. URL and DNS-based filtering with threat intelligence feeds. SSL inspection pipeline. Policy engine tying it all together. Capstone: a working NGFW prototype.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m23-conntrack-nat/' | relative_url }}"
           style="background:#faeaea;border-color:#e8b0b0;color:#5a0a0a;">🔄 M23 - Connection Tracking and NAT</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m24-dpi/' | relative_url }}"
           style="background:#faeaea;border-color:#e8b0b0;color:#5a0a0a;">🔬 M24 - Deep Packet Inspection</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m25-ids-ips/' | relative_url }}"
           style="background:#faeaea;border-color:#e8b0b0;color:#5a0a0a;">🚨 M25 - IDS and IPS</a>
        <a class="pt-mod" href="{{ '/learning/networking-mastery/m26-policy-capstone/' | relative_url }}"
           style="background:#faeaea;border-color:#e8b0b0;color:#5a0a0a;">🛡️ M26 - NGFW Policy Engine and Capstone</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">conntrack</span>
        <span class="skill-tag">NAT44 / NAT64</span>
        <span class="skill-tag">ALG (FTP / SIP)</span>
        <span class="skill-tag">L7 classification</span>
        <span class="skill-tag">Hyperscan</span>
        <span class="skill-tag">nDPI</span>
        <span class="skill-tag">regex engine</span>
        <span class="skill-tag">Snort rules</span>
        <span class="skill-tag">Suricata</span>
        <span class="skill-tag">signature matching</span>
        <span class="skill-tag">URL filtering</span>
        <span class="skill-tag">DNS sinkhole</span>
        <span class="skill-tag">threat intel</span>
        <span class="skill-tag">SSL inspection</span>
        <span class="skill-tag">policy engine</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#faeaea;color:#5a0a0a;">🔨 Project: Stateful conntrack in C using bihash</span>
        <span class="proj-chip" style="background:#faeaea;color:#5a0a0a;">🔨 Project: L7 classifier with nDPI</span>
        <span class="proj-chip" style="background:#faeaea;color:#5a0a0a;">🔨 Project: Write 10 custom Snort rules</span>
        <span class="proj-chip" style="background:#faeaea;color:#5a0a0a;">🏆 Capstone: NGFW prototype — conntrack + DPI + policy + SSL inspection</span>
      </div>
      <div class="dep-note">📌 Prerequisite: All of Phases 1–5. This phase is the integration layer — every component you build uses knowledge from every prior module.</div>
    </div>
  </div>

</div><!-- end timeline -->

<!-- ═════════════════════ ALL MODULES TABLE ════════════════════ -->
<p class="sep">ALL 26 MODULES AT A GLANCE</p>

<div style="overflow-x:auto;">
<table class="mod-full-table">
  <thead>
    <tr>
      <th>Module</th>
      <th>Title</th>
      <th>Phase</th>
      <th>Key Topics</th>
      <th>Weeks</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>M01</code></td><td>OSI and TCP/IP Model</td><td><span class="phase-badge" style="background:#e8f1f9;color:#1a3a5c;">P1</span></td><td>OSI layers, encapsulation, PDUs, TCP/IP vs OSI</td><td>1</td></tr>
    <tr><td><code>M02</code></td><td>Ethernet and L2</td><td><span class="phase-badge" style="background:#e8f1f9;color:#1a3a5c;">P1</span></td><td>Ethernet frame, MAC, ARP, VLANs, 802.1Q, STP, RSTP</td><td>1–2</td></tr>
    <tr><td><code>M03</code></td><td>IPv4 Deep Dive</td><td><span class="phase-badge" style="background:#e8f1f9;color:#1a3a5c;">P1</span></td><td>Header fields, subnetting, CIDR, fragmentation, ICMP</td><td>2</td></tr>
    <tr><td><code>M04</code></td><td>IPv6</td><td><span class="phase-badge" style="background:#e8f1f9;color:#1a3a5c;">P1</span></td><td>Addressing, NDP, ICMPv6, SLAAC, dual-stack, transition</td><td>3</td></tr>
    <tr><td><code>M05</code></td><td>TCP Internals</td><td><span class="phase-badge" style="background:#e0f0ee;color:#0a3a30;">P2</span></td><td>State machine, handshake, flow control, congestion, SACK</td><td>4–5</td></tr>
    <tr><td><code>M06</code></td><td>UDP and ICMP</td><td><span class="phase-badge" style="background:#e0f0ee;color:#0a3a30;">P2</span></td><td>UDP header, IGMP, multicast, ICMP types, traceroute</td><td>5</td></tr>
    <tr><td><code>M07</code></td><td>DNS</td><td><span class="phase-badge" style="background:#e0f0ee;color:#0a3a30;">P2</span></td><td>Resolution, record types, DNSSEC, DoH, DoT, DNS attacks</td><td>5–6</td></tr>
    <tr><td><code>M08</code></td><td>HTTP/1.1, HTTP/2, HTTP/3 and QUIC</td><td><span class="phase-badge" style="background:#e0f0ee;color:#0a3a30;">P2</span></td><td>HTTP methods, headers, streams, multiplexing, QUIC frames</td><td>6</td></tr>
    <tr><td><code>M09</code></td><td>SMTP, FTP, DHCP</td><td><span class="phase-badge" style="background:#e0f0ee;color:#0a3a30;">P2</span></td><td>SMTP envelope, MIME, FTP active/passive, DHCP DORA</td><td>7</td></tr>
    <tr><td><code>M10</code></td><td>Routing Fundamentals and FIB</td><td><span class="phase-badge" style="background:#faeee4;color:#6a2800;">P3</span></td><td>FIB/RIB, LPM, trie, ECMP, policy routing</td><td>8</td></tr>
    <tr><td><code>M11</code></td><td>OSPF Internals</td><td><span class="phase-badge" style="background:#faeee4;color:#6a2800;">P3</span></td><td>LSA types, SPF, areas, DR/BDR, OSPF v3</td><td>9</td></tr>
    <tr><td><code>M12</code></td><td>BGP Internals</td><td><span class="phase-badge" style="background:#faeee4;color:#6a2800;">P3</span></td><td>eBGP/iBGP, path selection, attributes, communities, policy</td><td>10</td></tr>
    <tr><td><code>M13</code></td><td>MPLS, VxLAN, GRE and Tunneling</td><td><span class="phase-badge" style="background:#faeee4;color:#6a2800;">P3</span></td><td>Label switching, VTEP, overlay networks, encap/decap</td><td>11</td></tr>
    <tr><td><code>M14</code></td><td>Linux Network Stack</td><td><span class="phase-badge" style="background:#ede8f5;color:#3a1a6c;">P4</span></td><td>sk_buff, netdev, Netfilter, iptables, tc, nftables</td><td>12–13</td></tr>
    <tr><td><code>M15</code></td><td>Socket Programming in C</td><td><span class="phase-badge" style="background:#ede8f5;color:#3a1a6c;">P4</span></td><td>TCP server/client, UDP, non-blocking, select/poll/epoll</td><td>13–14</td></tr>
    <tr><td><code>M16</code></td><td>Raw Sockets, pcap and eBPF</td><td><span class="phase-badge" style="background:#ede8f5;color:#3a1a6c;">P4</span></td><td>SOCK_RAW, AF_PACKET, libpcap, BPF bytecode, eBPF maps</td><td>14–15</td></tr>
    <tr><td><code>M17</code></td><td>Kernel Bypass and XDP</td><td><span class="phase-badge" style="background:#ede8f5;color:#3a1a6c;">P4</span></td><td>XDP hook, AF_XDP, UMEM, io_uring, DPDK comparison</td><td>15</td></tr>
    <tr><td><code>M18</code></td><td>High-Performance Techniques</td><td><span class="phase-badge" style="background:#ede8f5;color:#3a1a6c;">P4</span></td><td>RSS/RPS/RFS, NUMA, hugepages, CPU pinning, lock-free</td><td>16</td></tr>
    <tr><td><code>M19</code></td><td>Cryptography Essentials</td><td><span class="phase-badge" style="background:#fdf0e0;color:#5a2800;">P5</span></td><td>Symmetric, asymmetric, hashing, PKI, X.509, CRL/OCSP</td><td>17–18</td></tr>
    <tr><td><code>M20</code></td><td>TLS 1.2 and TLS 1.3 Internals</td><td><span class="phase-badge" style="background:#fdf0e0;color:#5a2800;">P5</span></td><td>Handshake, cipher suites, ALPN, SNI, session resumption</td><td>18–19</td></tr>
    <tr><td><code>M21</code></td><td>IPsec and IKEv2</td><td><span class="phase-badge" style="background:#fdf0e0;color:#5a2800;">P5</span></td><td>ESP/AH headers, IKEv2 exchange, SA negotiation, VPN modes</td><td>19–20</td></tr>
    <tr><td><code>M22</code></td><td>DTLS, mTLS and SSL Inspection</td><td><span class="phase-badge" style="background:#fdf0e0;color:#5a2800;">P5</span></td><td>DTLS over UDP, certificate pinning, SSL bump, re-encryption</td><td>20–21</td></tr>
    <tr><td><code>M23</code></td><td>Connection Tracking and NAT</td><td><span class="phase-badge" style="background:#faeaea;color:#5a0a0a;">P6</span></td><td>conntrack table, NAT44/64, PAT, ALG for FTP/SIP/H.323</td><td>22–23</td></tr>
    <tr><td><code>M24</code></td><td>Deep Packet Inspection</td><td><span class="phase-badge" style="background:#faeaea;color:#5a0a0a;">P6</span></td><td>L7 classification, Hyperscan, nDPI, regex, protocol fingerprinting</td><td>23–24</td></tr>
    <tr><td><code>M25</code></td><td>IDS and IPS</td><td><span class="phase-badge" style="background:#faeaea;color:#5a0a0a;">P6</span></td><td>Snort/Suricata rule syntax, signature matching, anomaly detection</td><td>24–25</td></tr>
    <tr><td><code>M26</code></td><td>NGFW Policy Engine and Capstone</td><td><span class="phase-badge" style="background:#faeaea;color:#5a0a0a;">P6</span></td><td>URL filtering, DNS sinkhole, threat intel, policy engine, capstone</td><td>25–26</td></tr>
  </tbody>
</table>
</div>

<!-- ═══════════════════ LEARNING PATH NOTE ════════════════════ -->
<p class="sep">RECOMMENDED LEARNING PATH</p>

<div style="background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;padding:1.2rem 1.4rem;margin-bottom:1.5rem;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
    <div>
      <div style="font-size:.78rem;font-family:monospace;font-weight:700;color:#1a3a5c;margin-bottom:.5rem;text-transform:uppercase;letter-spacing:.06em;">For Beginners</div>
      <div style="font-size:.85rem;color:var(--text-color,#333);line-height:1.7;">Follow phases strictly in order 1 → 2 → 3 → 4 → 5 → 6. Do not skip M01–M04 even if they seem basic — M05 (TCP) and M14 (Linux stack) assume byte-level IP knowledge. Complete every lab before moving to the next module.</div>
    </div>
    <div>
      <div style="font-size:.78rem;font-family:monospace;font-weight:700;color:#8c2020;margin-bottom:.5rem;text-transform:uppercase;letter-spacing:.06em;">For Experienced Engineers</div>
      <div style="font-size:.85rem;color:var(--text-color,#333);line-height:1.7;">If you have solid L2/L3 foundations, start at M05 (TCP) or M14 (Linux stack) and use M01–M04 as reference. Phase 4 (Linux + sockets) is worth reading fully regardless of experience — eBPF and AF_XDP content is non-trivial even for senior engineers.</div>
    </div>
  </div>
</div>

<!-- ═══════════════════ REFERENCES ═══════════════════════════ -->
<p class="sep">KEY REFERENCES</p>

- [RFC 791 — IPv4](https://datatracker.ietf.org/doc/html/rfc791){:target="_blank" rel="noopener"}
- [RFC 793 — TCP](https://datatracker.ietf.org/doc/html/rfc793){:target="_blank" rel="noopener"}
- [RFC 8446 — TLS 1.3](https://datatracker.ietf.org/doc/html/rfc8446){:target="_blank" rel="noopener"}
- [RFC 7296 — IKEv2](https://datatracker.ietf.org/doc/html/rfc7296){:target="_blank" rel="noopener"}
- [Linux Kernel Networking — Rami Rosen (book)](https://www.oreilly.com/library/view/linux-kernel-networking/9781430261964/){:target="_blank" rel="noopener"}
- [The Linux man-pages — socket(7), ip(7), tcp(7)](https://man7.org/linux/man-pages/){:target="_blank" rel="noopener"}
- [nDPI — Open Source DPI Library](https://github.com/ntop/nDPI){:target="_blank" rel="noopener"}
- [Suricata IDPS](https://suricata.io/){:target="_blank" rel="noopener"}

<div class="mod-nav">
  <a href="{{ '/learning/' | relative_url }}">← Learning Hub</a>
  <a class="nb" href="{{ '/learning/networking-mastery/m01-osi-tcpip/' | relative_url }}">Start: M01 - OSI and TCP/IP →</a>
</div>
