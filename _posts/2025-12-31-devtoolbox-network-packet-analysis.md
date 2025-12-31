---
layout: post
title: "DevToolBox: A Comprehensive Network Packet Analysis Suite"
date: 2025-12-31
categories: [data-plane, system-design, general]
excerpt: "Building a hybrid web application for PCAP editing, generation, merging, and hex viewing using Flask and Vue.js. A developer's toolkit for network forensics and packet manipulation."
---

## Introduction

As a developer working with network protocols and data plane technologies, I found myself repeatedly needing tools to analyze packet captures, generate test data, and inspect binary files. Rather than switching between multiple tools, I built **DevToolBox** — a unified web-based suite that brings together four essential utilities in one place.

🔗 **[GitHub Repository](https://github.com/Ajay3007/devtoolbox){:target="_blank" rel="noopener noreferrer"}**

---

## 🎯 The Problem Space

Network engineers and developers often face these challenges:

- **PCAP Analysis** — Need to read, modify, and understand network packet captures
- **Test Data Generation** — Creating realistic PCAP files for testing network protocols
- **Binary Inspection** — Analyzing firmware, protocol payloads, and unknown binary files
- **Capture Management** — Merging multiple PCAP files from different sources

Existing tools are either:
- Command-line based (steep learning curve)
- Desktop applications (platform-specific)
- Limited to single functionality
- Expensive commercial software

**DevToolBox** addresses this gap with a modern, web-based interface that's accessible, intuitive, and completely free.

---

## 🛠️ The Four Core Tools

### 1. PCAP Editor

The **PCAP Editor** lets you upload and analyze PCAP/PCAPNG files with detailed packet information:

- **Protocol Breakdown** — View TCP, UDP, ICMP, DNS, HTTP, TLS packets
- **Field Modification** — Edit MAC addresses, IP addresses, ports, VLAN IDs
- **Application Layer Editing** — Modify HTTP Host headers, TLS SNI fields, DNS queries
- **Automatic Checksums** — Recalculates IP and TCP checksums automatically
- **Download Modified Captures** — Export your changes as new PCAP files

**Use Cases:**
- Protocol testing and debugging
- Security research and forensics
- Network simulation
- Anonymizing packet captures

### 2. PCAP Generator

Create synthetic PCAP files with **complete TCP 3-way handshake flows**:

- **Multiple Protocols** — TCP, HTTP, UDP, DNS (UDP/TCP), TLS
- **Realistic Flows** — Full TCP lifecycle: SYN → SYN-ACK → ACK → Data → FIN-ACK
- **Incremental IPs** — Generates unique flows with auto-incrementing destination IPs
- **VLAN Support** — Add VLAN tagging for enterprise network simulation
- **Custom Configuration** — Configure MAC addresses, IPs, ports, packet counts

**Use Cases:**
- Creating test datasets
- Load testing network equipment
- Protocol implementation testing
- Network simulation scenarios

### 3. PCAP Merger

Combine multiple PCAP/PCAPNG files into a single capture:

- **Preserve Timing** — Maintains original packet timestamps
- **Maintain Order** — Keeps chronological packet sequence
- **Multi-Format Support** — Works with PCAP and PCAPNG formats
- **Automatic Statistics** — Shows packet counts from merged files

**Use Cases:**
- Consolidating forensics data
- Merging test captures
- Combining multi-interface captures
- Creating comprehensive datasets

### 4. Hex Viewer

Upload any binary file and view it with dual modes:

- **Text View** — Human-readable text with auto-detected encoding (UTF-8, ASCII, Latin-1, UTF-16, UTF-32)
- **Hex View** — Traditional hex dump with ASCII representation
- **Format Detection** — Automatically identifies JSON, XML, Plain Text, Binary
- **Pattern Search** — Search by hex pattern or ASCII text
- **Pagination** — Handle large files efficiently
- **Export Options** — Copy to clipboard or export as hex dump

**Use Cases:**
- Firmware analysis
- Protocol reverse engineering
- File forensics
- Unknown file format inspection

---

## 🏗️ Technical Architecture

### Backend: Python + Flask + Scapy

The backend is built with:
- **Flask** — Lightweight REST API server
- **Scapy** — Powerful Python library for packet manipulation
- **File Handling** — Secure upload/download with size limits

Key modules:
- `app.py` — Flask API endpoints
- `pcap_handler.py` — PCAP processing logic
- `utils.py` — Helper functions for encoding/checksums

### Frontend: Vue.js 3 + Vite

The frontend features:
- **Vue.js 3** — Modern reactive framework
- **Vite** — Fast development and build tool
- **Axios** — HTTP client for API calls
- **Component Architecture** — Separate views for each tool

Key components:
- `Home.vue` — Landing page with tool navigation
- `PCAPEditor.vue` — Editor interface
- `PCAPGenerator.vue` — Generator form
- `PCAPMerger.vue` — Merger interface
- `HexViewer.vue` — Hex/text viewer

### Communication Flow

```
User → Vue.js Frontend → Axios HTTP → Flask Backend → Scapy Processing → Response → Display
```

---

## 🚀 Key Features & Implementation

### Automatic Checksum Recalculation

When modifying packet fields (IPs, ports), checksums must be updated:

```python
# Delete old checksums
del packet[IP].chksum
del packet[TCP].chksum

# Scapy automatically recalculates on packet serialization
```

### Complete TCP Flow Generation

Generating realistic TCP flows requires proper state handling:

1. **SYN** — Client initiates connection
2. **SYN-ACK** — Server responds
3. **ACK** — Client acknowledges
4. **PSH-ACK** — Data transmission
5. **FIN-ACK** — Connection termination

Each packet has proper sequence and acknowledgment numbers.

### Multi-Format PCAP Support

Using Scapy's `rdpcap()` and `wrpcap()` functions:
- Automatically detects PCAP vs PCAPNG
- Preserves timestamp precision
- Handles both formats seamlessly

### Hex Viewer Encoding Detection

The hex viewer tries multiple encodings:
```python
encodings = ['utf-8', 'ascii', 'latin-1', 'utf-16', 'utf-32']
for encoding in encodings:
    try:
        text = data.decode(encoding)
        return text, encoding
    except UnicodeDecodeError:
        continue
```

---

## 📊 Performance Considerations

- **File Size Limits** — Default 100MB, configurable up to 500MB
- **Pagination** — Large files displayed in chunks
- **Incremental Processing** — Packets processed one at a time
- **Client-Side Rendering** — Vue.js handles DOM updates efficiently

---

## 🔧 Quick Start

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

Visit **http://localhost:8080** and start analyzing!

---

## 🎓 Real-World Use Cases

### Network Forensics
Analyze suspicious traffic captures from IDS/IPS systems, modify timestamps for timeline analysis, and extract specific protocols for detailed inspection.

### Protocol Testing
Generate synthetic traffic to test protocol implementations, verify state machine handling, and stress-test network equipment.

### Security Research
Modify packet fields to test security controls, create proof-of-concept exploits in controlled environments, and analyze malware network behavior.

### Education
Learn about network protocols by inspecting real packet captures, understand TCP 3-way handshake with visual flows, and practice protocol analysis.

---

## 🔮 Future Enhancements

- **Packet Filtering** — Filter by protocol, IP, port, or custom expressions
- **Statistics Dashboard** — Visual graphs for protocol distribution, bandwidth usage
- **Batch Operations** — Modify multiple packets simultaneously
- **Protocol Dissectors** — Deep inspection for more application protocols
- **Live Capture** — Real-time packet capture from network interfaces
- **Export Formats** — Support for CSV, JSON exports of packet data

---

## 📝 Lessons Learned

### 1. Scapy is Powerful but Complex
Scapy's flexibility comes with a learning curve. Understanding packet layers and field manipulation required extensive documentation reading.

### 2. Checksum Handling
Automatic checksum recalculation works well, but edge cases (like tunneled packets) need special handling.

### 3. File Upload Security
Always validate file types, limit file sizes, and sanitize filenames to prevent security issues.

### 4. Frontend-Backend Separation
Using Vue.js + Flask allows independent development and easier testing of both layers.

---

## 🎯 Conclusion

**DevToolBox** started as a personal need and evolved into a comprehensive toolkit for network analysis. By combining multiple utilities in a single web interface, it simplifies workflows for network engineers, security researchers, and developers.

The project demonstrates:
- Practical application of **data plane** concepts
- **System design** for web-based tools
- Integration of Python packet processing with modern JavaScript frameworks

Whether you're debugging network issues, generating test data, or learning about protocols, DevToolBox provides an accessible, powerful solution.

**Try it out:** [GitHub - Ajay3007/devtoolbox](https://github.com/Ajay3007/devtoolbox){:target="_blank" rel="noopener noreferrer"}

---

## 🔗 Related Topics

- [Data Plane Technologies]({{ '/learning/data-plane/' | relative_url }})
- [Networking Fundamentals]({{ '/learning/networking/' | relative_url }})
- [System Design Concepts]({{ '/learning/system-design/' | relative_url }})

---

*Built with 💻 by Ajay — Exploring the intersection of networking, data plane, and software engineering.*
