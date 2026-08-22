---
title: "DevToolBox"
description: "Web suite for network packet analysis, editing, generation, and hex viewing. No local tool setup required — runs entirely in the browser."
year: 2024
tech: ["Python", "Flask", "Vue.js 3", "Scapy", "Docker", "Vercel"]
github: https://github.com/Ajay3007/devtoolbox
demo: https://devtoolbox-sandy.vercel.app/
url: /projects/devtoolbox/
---

## The Problem

Network engineers and security professionals constantly juggle multiple local tools for PCAP work: Wireshark for inspection, Scapy scripts for editing, custom tooling for generation. DevToolBox collapses this into a single browser-based app — upload a PCAP, do the work, download the result.

## Features

<div class="c-feat-grid">
  <div class="c-feat-card">
    <div class="c-feat-title">PCAP Editor</div>
    <div class="c-feat-desc">Upload PCAP/PCAPNG files. Modify MAC addresses, IPs, ports, VLAN IDs, TLS SNI fields, and HTTP Host headers. Automatic checksum recalculation on every edit.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">PCAP Generator</div>
    <div class="c-feat-desc">Generate synthetic packet flows with full TCP 3-way handshakes. Supports HTTP, DNS (UDP/TCP), TLS Client Hello, VLAN tagging, and incremental destination IPs for unique flows.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">PCAP Merger</div>
    <div class="c-feat-desc">Combine two or more PCAP/PCAPNG files into a single chronologically-ordered capture. Preserves millisecond timing and packet sequencing across all input files.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Hex Viewer</div>
    <div class="c-feat-desc">Inspect any binary file as a hex dump with auto-detected encoding (UTF-8, ASCII, Latin-1, UTF-16, UTF-32). Search by hex pattern or ASCII text. Pagination for large files.</div>
  </div>
</div>

## Stack

<div class="c-stack-grid">
  <div><div class="c-stack-key">backend</div><div class="c-stack-val">Python 3 / Flask</div></div>
  <div><div class="c-stack-key">frontend</div><div class="c-stack-val">Vue.js 3 / Vite</div></div>
  <div><div class="c-stack-key">packet engine</div><div class="c-stack-val">Scapy</div></div>
  <div><div class="c-stack-key">http client</div><div class="c-stack-val">Axios</div></div>
  <div><div class="c-stack-key">container</div><div class="c-stack-val">Docker</div></div>
  <div><div class="c-stack-key">hosting</div><div class="c-stack-val">Vercel (frontend)</div></div>
</div>

## Quick Start

```bash
git clone https://github.com/Ajay3007/devtoolbox.git
cd devtoolbox

# Backend
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/app.py          # → localhost:5000

# Frontend
cd frontend && npm install && npm run dev  # → localhost:8080
```
