---
title: "ftp-analyzer"
description: "C++ utility that reconstructs FTP-transferred files from raw PCAP captures via TCP reassembly and FTP protocol parsing. Works entirely offline."
year: 2024
tech: ["C++", "libpcap", "TCP/IP", "FTP", "CMake"]
github: https://github.com/Ajay3007/ftp-analyzer
url: /projects/ftp-analyzer/
---

## The Problem

Given a PCAP file captured during an FTP session, reconstruct the files that were transferred — without access to the original server and without running the FTP protocol again. The PCAP may contain unrelated noise (ARP, ICMP, DHCP, mDNS) and the FTP session may span multiple connections.

## How It Works

The pipeline runs in four modular stages:

1. **PCAP Reader** — reads raw frames using libpcap, strips link-layer headers
2. **TCP Reassembly** — tracks TCP streams by 4-tuple, reorders segments, handles duplicates and retransmits
3. **FTP Parser** — tracks the FTP control channel (port 21) to find PASV/EPSV passive-mode data ports and extract filenames from STOR/RETR commands
4. **Session Manager** — correlates control and data channels, writes reconstructed bytes to output files

## Features

<div class="c-feat-grid">
  <div class="c-feat-card">
    <div class="c-feat-title">Offline Analysis</div>
    <div class="c-feat-desc">No FTP server or network access required. Reconstructs files from a static PCAP capture using libpcap for frame reading.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">TCP Reassembly</div>
    <div class="c-feat-desc">Full segment reordering with duplicate packet handling. Correctly reconstructs streams that arrive out-of-order or contain retransmissions.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Passive & Active FTP</div>
    <div class="c-feat-desc">Supports PASV/EPSV passive mode and PORT/EPRT active mode. Handles both IPv4 and IPv6 data connections.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Noisy PCAPs</div>
    <div class="c-feat-desc">Silently skips non-TCP frames and unrelated protocols. Multi-session support — reconstructs all FTP transfers present in a single capture.</div>
  </div>
</div>

## Stack

<div class="c-stack-grid">
  <div><div class="c-stack-key">language</div><div class="c-stack-val">C++17</div></div>
  <div><div class="c-stack-key">packet I/O</div><div class="c-stack-val">libpcap</div></div>
  <div><div class="c-stack-key">build</div><div class="c-stack-val">CMake</div></div>
  <div><div class="c-stack-key">protocols</div><div class="c-stack-val">FTP, TCP, IPv4/IPv6</div></div>
</div>

## Quick Start

```bash
git clone https://github.com/Ajay3007/ftp-analyzer.git
cd ftp-analyzer
mkdir build && cd build
cmake .. && make

./ftp-analyzer ../captures/ftp_2file.pcap
# Reconstructed files written to ./output/
```
