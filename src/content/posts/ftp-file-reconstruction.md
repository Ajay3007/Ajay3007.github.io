---
title: "Reconstructing Files from FTP Network Traffic: Understanding FTP, PCAP, and TCP Reassembly"
description: "During a recent interview assignment, I was asked to design a system that could reconstruct a file transferred using FTP by analyzing raw network traffic."
date: 2026-02-01
tags: [data-plane, system-design]
url: /blog/2026/02/01/ftp-file-reconstruction/
---

During a recent interview assignment, I was asked to design a system that could reconstruct a file transferred using FTP by analyzing raw network traffic. This task helped me understand how real-world file transfers work at the protocol level.

In this post, I’ll explain the core concepts behind FTP, Active and Passive modes, and how I used PCAP analysis and TCP reassembly to solve the problem.

---

## What is FTP?

FTP (File Transfer Protocol) is one of the oldest protocols used to transfer files over a network.

It works on top of TCP and is mainly used to:

- Upload files to servers
- Download files from servers
- Manage remote directories

FTP is simple, reliable, and still used in many legacy and internal systems.

However, traditional FTP does **not encrypt data**, which makes it useful for learning and traffic analysis.

---

## Why is FTP Used?

FTP is used because:

- It is easy to implement
- It supports large file transfers
- It works well over TCP
- It is supported by almost all operating systems

In many internal networks and testing environments, FTP is still widely used.

For my assignment, FTP was chosen because it allows capturing raw file data from the network.

---

## Two Connections in FTP

Unlike most protocols, FTP uses **two TCP connections**:

| Connection Type | Purpose | Default Port |
|-----------------|----------|--------------|
| Control Channel | Commands and responses | 21 |
| Data Channel | File transfer | Dynamic |

- The **control channel** handles login and commands.
- The **data channel** carries actual file bytes.

Understanding this separation is critical for packet analysis.

---

## Passive FTP (PASV / EPSV Mode)

In Passive mode, the **server opens a data port** and tells the client where to connect.

### Flow:

```java
Client → Server (21)
Server → Client (PASV / EPSV response)
Client → Server (Data Port)
```


### Examples

IPv4:

```bash
227 (192,168,1,5,32,144)
```

IPv6:

```bash
229 (|||49210|)
```


### Why Passive Mode Exists

Passive FTP is widely used because:

- It works behind firewalls
- It works with NAT
- It avoids incoming connections to clients

Most modern FTP clients use passive mode by default.

---

## Active FTP (PORT / EPRT Mode)

In Active mode, the **client opens a port** and asks the server to connect.

### Flow:

```bash
Client → Server (21)
Client → Server (PORT / EPRT)
Server → Client (Data Port)
```


### Examples

IPv4:

```bash
PORT 192,168,1,5,32,144
```

IPv6:

```bash
EPRT |2|::1|8336|
```


### Limitations of Active Mode

Active FTP often fails because:

- Firewalls block incoming connections
- NAT breaks address mapping

This is why Active mode is rarely used today.

---

## Problem Statement of My Assignment

The assignment required me to:

1. Transfer a file using FTP
2. Capture traffic using tcpdump
3. Analyze the PCAP file
4. Extract raw bytes
5. Reconstruct the original file

The main challenge was handling multiple TCP packets and rebuilding the file correctly.

---

## Understanding PCAP Files

A PCAP file stores raw network packets captured from an interface.

Each packet contains:

- Link Layer Header
- IP Header (IPv4 / IPv6)
- TCP Header
- Application Data

My program reads PCAP files using `libpcap` and extracts TCP payloads.

---

## TCP Reassembly

TCP splits large data into small segments.

Packets may arrive:

- Out of order
- Duplicated
- Delayed

So reconstruction requires:

1. Collecting all segments
2. Sorting by sequence number
3. Removing duplicates
4. Writing in correct order

This process is called **TCP reassembly**.

---

## Handling IPv4 and IPv6

Originally, my implementation only supported IPv4.

Later, I upgraded it to support IPv6 by:

- Detecting IP version
- Parsing IPv6 headers
- Supporting EPSV mode
- Using unified IP address structures

This made the tool dual-stack compatible.

---

## Tools and Technologies Used

| Tool | Purpose |
|------|----------|
| C++ | Core implementation |
| libpcap | Packet parsing |
| tcpdump | Packet capture |
| Pure-FTPd | FTP server |
| CMake | Build system |
| Wireshark | Debugging |

---

## Key Learnings

Through this project, I learned:

- How FTP works internally
- Difference between Active and Passive modes
- How TCP ensures reliability
- How packet captures are structured
- How to reconstruct application data from network traffic
- How to design modular C++ systems

---

## Conclusion

This assignment helped me move from using networking tools to understanding how they work internally.

Reconstructing a file from raw packets gave me hands-on experience with real-world networking and systems programming.

In future, I plan to extend this project with:

- Active FTP support
- Multi-session handling
- Advanced retransmission recovery
- Better CLI filters

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="/blogs" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← All Blogs</a>
  <a href="/" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Home 🏠</a>
</div>
