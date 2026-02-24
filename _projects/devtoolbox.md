---
layout: project
title: DevToolBox - Network Packet Analysis Suite
description: "Hybrid web application for PCAP analysis, generation, merging, and hex viewing. Built with Flask and Vue.js for network forensics and packet manipulation."
permalink: /projects/devtoolbox/
---

<!-- Hero Section -->
<section class="hero-section" style="background: linear-gradient(135deg, rgba(255, 107, 107, 0.05), rgba(72, 219, 251, 0.05)); border: 1px solid rgba(255, 107, 107, 0.1);">
    <h1 class="hero-title">DevToolBox 🛠️</h1>
    <p class="hero-subtitle">
        Comprehensive web suite for <strong>Network Packet Processing</strong>, PCAP generation, flow merging, and advanced hex binary analysis.
    </p>
    <div class="hero-actions">
        <a href="https://devtoolbox-sandy.vercel.app/" target="_blank" rel="noopener noreferrer" class="btn-primary" style="background: linear-gradient(135deg, #FF6B6B, #EE5253); box-shadow: 0 4px 15px rgba(238, 82, 83, 0.4);">
            🌐 Live Demo (Vercel)
        </a>
        <a href="https://github.com/Ajay3007/devtoolbox" target="_blank" rel="noopener noreferrer" class="btn-secondary">
            📦 View on GitHub
        </a>
    </div>
</section>

<!-- What Problem it Solves -->
<section class="modern-section" style="max-width: 800px; margin: 0 auto 4.5rem auto;">
    <h2 class="section-title">🎯 The Challenge</h2>
    <p style="font-size: 1.1rem; color: var(--text-color); line-height: 1.8; margin-bottom: 2rem;">
        DevToolBox addresses critical needs for network engineers, security professionals, and backend developers. It completely eliminates the friction of configuring local multi-tool environments for:
    </p>
    <ul style="margin: 0; padding-left: 1.5rem; color: var(--text-color); font-size: 1.05rem; line-height: 1.7;">
        <li><strong style="color: var(--primary-color);">PCAP Interpretation</strong> — Rapidly modifying massive packet captures with protocol breakdowns.</li>
        <li><strong style="color: var(--primary-color);">Simulated Traffic</strong> — Generating fully synthetic PCAP sequences mimicking real 3-way TCP handshakes.</li>
        <li><strong style="color: var(--primary-color);">File Forensics</strong> — Instantaneous browser-based binary inspection mapping hex blocks.</li>
    </ul>
</section>

<!-- Key Features Array -->
<section class="modern-section">
    <h2 class="section-title">✨ Key Features</h2>
    <div class="nav-grid">
        <div class="nav-card" style="border-left-color: #3b82f6;">
            <div class="nav-card-title">📊 PCAP Editor</div>
            <div class="nav-card-desc">Upload and analyze PCAP/PCAPNG streams. Effortlessly modify field MACs, IP headers, TCP/UDP ports, TLS SNI, and instantly recalculate layer checksums.</div>
        </div>
        <div class="nav-card" style="border-left-color: #fca5a5;">
            <div class="nav-card-title">🔄 PCAP Synthetic Gen.</div>
            <div class="nav-card-desc">Build realistic network flow architectures. Capable of generating HTTP, DNS, UDP, TLS data spanning complete TCP lifecycle handshakes and teardowns.</div>
        </div>
        <div class="nav-card" style="border-left-color: #c084fc;">
            <div class="nav-card-title">🔗 Intelligent Merger</div>
            <div class="nav-card-desc">Lossless chronological combinations of massive PCAP chunks, preserving millisecond-precision timing accuracy and packet sequencing.</div>
        </div>
        <div class="nav-card" style="border-left-color: #34d399;">
            <div class="nav-card-title">🔍 Advanced Hex Viewer</div>
            <div class="nav-card-desc">Zero-install binary reading logic inside the browser. Maps raw format encoding schemas (UTF-8, ASCII, UTF-32) against raw hex dumps immediately.</div>
        </div>
    </div>
</section>

<!-- Architecture / Tech Stack Breakdown -->
<section class="modern-section">
    <h2 class="section-title">🏗️ Architecture & Stack</h2>
    <div style="display: flex; gap: 2rem; flex-wrap: wrap;">
        
        <!-- Architecture List -->
        <div class="featured-project-card" style="flex: 1; min-width: 300px; border-top-color: #FF6B6B;">
            <div class="featured-project-title">Project Structure</div>
            <ul style="margin: 0; padding-left: 1.2rem; color: var(--text-color); line-height: 1.8;">
                <li><code>backend/</code> — Flask python API server managing complex Scapy packet mutation logic. (Dockerized)</li>
                <li><code>frontend/</code> — Interactive Vue.js SPA managing the PCAP Editor layout constraints via Vite. (Edge Vercel networks)</li>
                <li><code>docs/</code> — GH Pages implementation workflows.</li>
            </ul>
        </div>
        
        <!-- Tech Stack Highlight -->
        <div class="featured-project-card" style="flex: 1; min-width: 300px; border-top-color: #2d3748; background: #f8fafc;">
            <div class="featured-project-title">Technology Topology</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Backend</span><strong style="color: #1a1f36;">Python 3.8 / Flask</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Frontend</span><strong style="color: #1a1f36;">Vue 3 / Vite</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Network Intel</span><strong style="color: #1a1f36;">Scapy Library</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">API Binding</span><strong style="color: #1a1f36;">Axios</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Containerization</span><strong style="color: #1a1f36;">Docker</strong></div>
                <div><span style="color: #64748b; font-size: 0.85rem; display: block;">Deployment Node</span><strong style="color: #1a1f36;">Vercel</strong></div>
            </div>
        </div>
        
    </div>
</section>

<!-- Quick Start Section -->
<section class="modern-section">
    <h2 class="section-title">🚀 Deployment Boot-Up</h2>
    <div style="background: linear-gradient(135deg, #1e293b, #0f172a); padding: 2rem; border-radius: 12px; border-left: 4px solid #fca5a5; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
<pre style="margin: 0; background: transparent; padding: 0; border: none; box-shadow: none;"><code style="color: #e2e8f0; font-family: 'Fira Code', 'Courier New', monospace; font-size: 0.95rem;">> git clone https://github.com/Ajay3007/devtoolbox.git
> cd devtoolbox

# Initialize Backend Instance
> python -m venv .venv
> pip install -r backend/requirements.txt
> python backend/app.py 
[Running: port 5000 / Scapy logic active]

# Boot Frontend Client 
> cd frontend && npm install && npm run dev
[Vite v3 bound to localhost:8080]</code></pre>
    </div>
</section>

<!-- Extra Docs Links -->
<section class="modern-section">
    <div style="background: linear-gradient(135deg, rgba(33, 150, 243, 0.04) 0%, rgba(33, 150, 243, 0.01) 100%); padding: 1.5rem; border-radius: 8px; border-left: 4px solid #2196F3;">
        <p style="margin: 0 0 0.8rem 0; font-size: 1.25rem;"><strong>📚 Application Resources</strong></p>
        <ul style="margin: 0; padding-left: 1.5rem; color: var(--text-color); font-size: 1.05rem; line-height: 1.6;">
            <li><strong>Quick Start Guide</strong> — <a href="https://github.com/Ajay3007/devtoolbox/blob/main/QUICKSTART.md" style="color: #2196F3;">5-minute rapid deployment</a></li>
            <li><strong>Rest API Docs</strong> — <a href="https://github.com/Ajay3007/devtoolbox/blob/main/API_REFERENCE.md" style="color: #2196F3;">Endpoint logic paths</a></li>
            <li><strong>Troubleshooting</strong> — <a href="https://github.com/Ajay3007/devtoolbox/blob/main/TROUBLESHOOTING.md" style="color: #2196F3;">Logging trace maps</a></li>
        </ul>
    </div>
</section>

<div style="text-align: center; margin: 4rem 0 2rem 0; border-top: 1px solid var(--border-color); padding-top: 3rem;">
  <a href="{{ '/projects/' | relative_url }}" class="btn-secondary">
    <span style="margin-right: 0.5rem;">🎒</span> Back to Projects
  </a>
</div>
