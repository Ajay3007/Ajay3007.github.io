---
title: "Data Plane Projects"
tagline: "Twenty-one build-it-yourself modules, config parser to full pipeline."
description: "🚀 Dataplane Engineer Roadmap (0 → Production Ready) Overview This comprehensive roadmap is designed for: - Freshers entering systems programming - Backend developers…"
domain: data-plane
order: 4
status: active
url: /learning/data-plane/roadmap/
---

# 🚀 Dataplane Engineer Roadmap (0 → Production Ready)

## Overview

This comprehensive roadmap is designed for:
- Freshers entering systems programming
- Backend developers transitioning to systems and networking
- New joiners in SASE / Telecom / Networking teams

**Total Duration:** 6–9 months

---

## 🟢 PHASE 0 — Foundation (1 Month)

**Goal:** Make them "system-aware programmers"

### Topics
- ✅ Linux basics
- ✅ C fundamentals
- ✅ Memory model
- ✅ Debugging

### Task 0.1: Linux Survival

Master essential Linux tools:
- `ps`, `top`, `htop` — process monitoring
- `strace` — system call tracing
- `tcpdump` — packet capture
- `netstat` — network statistics
- `perf` — performance analysis

**Mini Project:** Analyze CPU/memory usage of a process

### Task 0.2: C Memory Lab

Write programs demonstrating:
- `malloc`/`free` mechanics
- Memory leak patterns and detection
- Buffer overflow vulnerabilities
- Segmentation fault debugging

**Mini Project:** Write custom malloc tracker

### Task 0.3: Debugging Tools

Learn industry-standard tools:
- `gdb` — GNU debugger
- `valgrind` — memory analysis
- sanitizers (ASan, MSan, UBSan)

**Mini Project:** Debug crashing server

---

## 🟡 PHASE 1 — Networking Basics (1–1.5 Months)

**Goal:** Understand packets, protocols, and flows

### Topics
- ✅ OSI / TCP-IP model
- ✅ Ethernet / IP / TCP / UDP / DNS
- ✅ Wireshark
- ✅ PCAP file format

### Task 1.1: Packet Analyzer

**Mini Project:** Write C program to parse PCAP files

Features:
- Parse and print IP/TCP/UDP/DNS headers
- Count flows by 5-tuple
- Extract domains from DNS queries

*(Matches your FTP/PCAP work)*

### Task 1.2: Socket Server

**Mini Project:** Build TCP proxy

Features:
- Accept incoming client connections
- Forward traffic to backend server
- Log packet details and statistics

---

## 🟠 PHASE 2 — Multithreading & Performance (1 Month)

**Goal:** Think in cores, not functions

### Topics
- ✅ pthread / std::thread
- ✅ mutex / atomic operations
- ✅ CPU cache behavior
- ✅ NUMA architecture

### Task 2.1: Worker Pool

**Mini Project:** Build packet processor with worker threads

Architecture:
```
RX Thread → Queue → Worker Pool → TX Thread
```

### Task 2.2: Lock-Free Counter

**Mini Project:** Compare synchronization primitives

Test and measure:
- mutex-based counter
- atomic operations
- per-core counters

Benchmark performance across approaches.

---

## 🔵 PHASE 3 — DPDK Fundamentals (1.5–2 Months)

📄 **[DPDK Mastery Roadmap &rarr;](/learning/data-plane/dpdk/dpdk-roadmap/)** — Full 3-phase deep-dive (18 chapters, 6 modules, 7 projects)

**Goal:** Become a real dataplane developer

### Topics
- ✅ Hugepages and memory allocation
- ✅ mbuf (memory buffers)
- ✅ RX/TX queues
- ✅ mempool management
- ✅ lcores (logical cores)
- ✅ Poll-mode drivers (PMD)

### Task 3.1: Hello DPDK

**Mini Project:** Run DPDK examples (l2fwd / helloworld)

Deliverables:
- Understand EAL (Environment Abstraction Layer)
- Explain lcore binding
- Master mempool allocation

### Task 3.2: Packet Forwarder

**Mini Project:** Write L2 forwarder in DPDK

Features:
- Receive packets from NIC queue
- Modify MAC addresses
- Transmit to output port

### Task 3.3: Packet Filter

**Mini Project:** Build IP/Port filter

Features:
- Block port 80 traffic
- Allow port 443 (HTTPS)
- Dynamic drop rules

*(Mini firewall implementation)*

---

## 🟣 PHASE 4 — Dataplane Architecture (2 Months)

**Goal:** Teach real system design (inspired by SASEDP)

### Topics
- ✅ Distributor-worker patterns
- ✅ Hash table implementations
- ✅ Flow cache design
- ✅ Policy engine
- ✅ Deep Packet Inspection (DPI)
- ✅ Pattern matching (Hyperscan)

### Task 4.1: Flow Tracker

**Mini Project:** Build 5-tuple flow engine

Features:
- Hash-based flow lookup
- Flow timeout management
- Per-flow statistics collection

### Task 4.2: Domain Filter (Your Signature)

**Mini Project:** DNS/SNI extractor + filter engine

Features:
- Extract domain from DNS queries and TLS SNI
- Pattern matching with Hyperscan
- Dynamic allow/block rules

*(Exactly mirrors your SASEDP dataplane flow)*

### Task 4.3: Policy Engine

**Mini Project:** Group-based rule evaluation

Data flow:
```
User → Group Mapping → Policy Rules → Action
```

---

## 🔴 PHASE 5 — Distributed Systems (1–1.5 Months)

**Goal:** Connect dataplane to control plane

### Topics
- ✅ Kafka message streaming
- ✅ Redis / Aerospike caching
- ✅ Microservices communication
- ✅ REST APIs

### Task 5.1: Policy Sync

**Mini Project:** Dynamic rule delivery via Kafka

Flow:
```
Java/Python Service → Kafka → DPDK Dataplane
```

### Task 5.2: Runtime Update

**Mini Project:** Hot reload rules (QSBR style)

Requirements:
- Zero-downtime policy updates
- Quiescent State Based Reclamation (QSBR) pattern
- Graceful in-flight packet handling

---

## 🟤 PHASE 6 — VPP & Advanced Networking (1 Month)

**Goal:** Make them platform engineers

### Topics
- ✅ VPP (Vector Packet Processing) graph architecture
- ✅ VPP plugins
- ✅ ACL (Access Control Lists)
- ✅ NAT (Network Address Translation)
- ✅ IPSec encryption

### Task 6.1: VPP Plugin

**Mini Project:** Write custom VPP plugin

Features:
- Custom packet processing node
- Packet filtering logic
- Integration with VPP graph

### Task 6.2: VPP + DPDK Bridge

**Mini Project:** Connect VPP → DPDK → Application

Architecture:
```
NIC → VPP Dataplane ↔ DPDK App → Control
```

---

## ⭐ PHASE 7 — Production Engineering (Ongoing)

**Goal:** Make them production-grade engineers

### Topics
- ✅ Observability (metrics, logs, traces)
- ✅ Structured logging
- ✅ Crash dump analysis
- ✅ SLA monitoring
- ✅ High Availability (HA)

### Task 7.1: Telemetry

**Mini Project:** Add Prometheus metrics

Export:
- Packet counts (RX/TX/drops)
- Latency histograms
- Resource utilization

### Task 7.2: Failure Simulation

**Mini Project:** Chaos engineering practice

Scenarios:
- Kill worker threads → observe recovery
- Break network link → test failover
- Simulate DDoS → monitor behavior

---

## 📊 Final Capstone Project (3 Months)

### 🌟 Mini Secure Gateway

This is the "mini SASE" integration project combining all phases.

#### Architecture
```
NIC → DPDK RX → Filter → DPI → Policy → Kafka → Dashboard
```

#### Core Features
- ✅ Packet RX/TX via DPDK
- ✅ Domain filtering (DNS/SNI)
- ✅ Application detection (basic)
- ✅ User identity mapping
- ✅ Policy updates from control plane
- ✅ Prometheus metrics dashboard

**Outcome:** Industry-ready dataplane engineer

---

## 🧠 Mentorship Model

### Your Training Approach

| Period | Role | Activities |
|--------|------|-----------|
| **Month 1–2** | Mentor | Pair programming on all tasks |
| **Month 3–4** | Lead | Trainee owns small modules independently |
| **Month 5+** | Debug Rotations | Assign production bugs from live systems |

### Weekly Structure

| Day | Activity |
|-----|----------|
| **Monday** | Theory review + architecture discussion |
| **Tuesday** | Hands-on coding |
| **Wednesday** | Debugging & optimization |
| **Thursday** | Performance tuning & benchmarking |
| **Friday** | Design review & knowledge sharing |
| **Saturday** | Mini project milestone checkpoint |

---

## 🔥 Interview-Ready Outcome

After completing this roadmap, your trainees will be able to:

- ✔️ Write production DPDK applications
- ✔️ Design dataplane pipelines from scratch
- ✔️ Debug packet drops in complex systems
- ✔️ Optimize latency and throughput
- ✔️ Build packet filters and firewalls
- ✔️ Integrate Kafka for policy delivery
- ✔️ Contribute to VPP projects
- ✔️ Design and implement HA systems

**Result:** Top 5% tier engineers ready for senior roles

---

## 💡 Why This Roadmap Matters for You

### Career Impact

Implementing this roadmap positions you as:
- ✅ Technical Leader
- ✅ System Architect
- ✅ Effective Mentor
- ✅ Technical Builder

### Growth Opportunities

This accelerates progression toward:
- Senior/Staff Engineer roles
- Architecture positions
- Hiring manager responsibilities
- Principal Engineer path

Your mentees become your force multiplier.

