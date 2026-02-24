---
layout: project
title: DevToolBox - Network Packet Analysis Suite
description: "Hybrid web application for PCAP analysis, generation, merging, and hex viewing. Built with Flask and Vue.js for network forensics and packet manipulation."
permalink: /projects/devtoolbox/
---

# 🛠️ DevToolBox — Network Packet Analysis Suite

> **Comprehensive developer tools for PCAP editing, generation, merging, and binary file inspection**

<div style="text-align: center; margin: 2rem 0; display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
  <a href="https://devtoolbox-sandy.vercel.app/" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; justify-content: center; padding: 0.85rem 1.75rem; background: linear-gradient(135deg, #FF6B6B 0%, #EE5253 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: 700; box-shadow: 0 4px 15px rgba(238, 82, 83, 0.4); transition: transform 0.2s, box-shadow 0.2s;">
    🌐 Live Demo (Vercel)
  </a>
  <a href="https://github.com/Ajay3007/devtoolbox" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; justify-content: center; padding: 0.85rem 1.75rem; background: #2d3748; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; box-shadow: 0 4px 15px rgba(45, 55, 72, 0.2); transition: transform 0.2s, box-shadow 0.2s;">
    📦 View on GitHub
  </a>
</div>

---

## 🎯 What Problem Does It Solve?

DevToolBox addresses critical needs for network engineers, security professionals, and developers:
- **PCAP Analysis** — Read and modify network packet captures with detailed protocol breakdown
- **Synthetic Testing** — Generate realistic PCAP files with complete TCP flows for testing and simulation
- **File Forensics** — Inspect binary files with hex/text dual view and pattern search
- **Packet Merging** — Combine multiple PCAP captures for comprehensive analysis

---

## ✨ Key Features

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3>📊 PCAP Editor</h3>
  <p>Upload and analyze PCAP/PCAPNG files with detailed packet information. View protocol breakdowns, modify network fields (MAC, IP, ports, DNS, HTTP Host, TLS SNI), and automatically recalculate checksums. Download modified captures instantly.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3>🔄 PCAP Generator</h3>
  <p>Generate synthetic PCAP files with complete TCP 3-way handshake flows. Support for multiple protocols (TCP, HTTP, UDP, DNS, TLS) with custom network configurations, VLAN tagging, and full TCP lifecycle simulation.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3>🔗 PCAP Merger</h3>
  <p>Combine 2+ PCAP/PCAPNG files into a single capture while preserving packet order and timing. Perfect for consolidating network forensics data and merging test datasets.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3>🔍 Hex Viewer</h3>
  <p>Upload any binary file and view with dual modes: human-readable text and hex dump. Auto-detects encoding (UTF-8, ASCII, Latin-1, UTF-16, UTF-32) and format (JSON, XML, Plain Text, Binary). Includes search by hex pattern or ASCII text.</p>
</div>

</div>

---

## 🏗️ Architecture

**Tech Stack:**
- **Backend:** Python 3.8+ with Flask & Scapy
- **Frontend:** Vue.js 3 with Vite & Axios (Live on **Vercel**)
- **PCAP Processing:** Scapy library for network packet manipulation
- **Deployment Strategy:** Frontend via Vercel Edge Networks, Backend via Docker containers.

**Project Structure:**
- `backend/` — Flask API server with PCAP processing logic
- `frontend/` — Vue.js SPA with tool components (Editor, Generator, Merger, HexViewer)
- `docs/` — GitHub Pages documentation
- Complete setup scripts and comprehensive guides

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/Ajay3007/devtoolbox.git
cd devtoolbox

# Backend setup (Terminal 1)
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r backend/requirements.txt
python backend/app.py

# Frontend setup (Terminal 2)
cd frontend
npm install
npm run dev
```

Visit **http://localhost:8080** to start analyzing packets!

---

## 📋 Requirements

- Python 3.8 or higher
- Node.js 14.0 or higher
- npm 6.0 or higher

---

## 📚 Documentation

- [Quick Start Guide](https://github.com/Ajay3007/devtoolbox/blob/main/QUICKSTART.md) — 5-minute setup
- [Running Instructions](https://github.com/Ajay3007/devtoolbox/blob/main/RUN.md) — Detailed guide
- [API Reference](https://github.com/Ajay3007/devtoolbox/blob/main/API_REFERENCE.md) — REST endpoints
- [Troubleshooting](https://github.com/Ajay3007/devtoolbox/blob/main/TROUBLESHOOTING.md) — Common issues

---

## 🎓 Use Cases

✅ **Network Forensics** — Analyze packet captures from security investigations  
✅ **Protocol Testing** — Generate synthetic traffic for testing network protocols  
✅ **Firmware Analysis** — Inspect binary files and extract hex patterns  
✅ **Test Data Creation** — Generate realistic PCAP files for QA and testing  
✅ **Traffic Simulation** — Merge and modify captures for network simulation  

---

## 📝 License

MIT License — See [LICENSE](https://github.com/Ajay3007/devtoolbox/blob/main/LICENSE) for details.
