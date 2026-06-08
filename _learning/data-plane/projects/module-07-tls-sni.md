---
layout: default
title: "Module 07 — TLS SNI Extractor"
permalink: /learning/data-plane/projects/module-07-tls-sni/
---

# Module 07 — TLS SNI Extractor

## What you learn

How to extract the Server Name Indication (SNI) from a TLS ClientHello —
the only domain-name signal available for policy enforcement on HTTPS traffic.

Two approaches are implemented:
1. **Full ClientHello walker** — walks every field, robust for standalone use
2. **Hyperscan-match extractor** — uses fixed offsets from a Hyperscan match,
   mirrors exactly what `on_hs_match` does in `domain_scan.c`

---

## Why SNI matters for a URL filtering engine

For DNS packets you can read the domain name in plaintext (Module 06).
For HTTPS the payload is encrypted — but the TLS ClientHello is sent before
encryption begins, and it contains the SNI extension with the target hostname.

```text
Client → Server:  TLS ClientHello (PLAINTEXT)
                  includes extensions:
                    server_name: "www.blocked-site.com"   ← the DP application reads this
                    supported_versions: TLS 1.3
                    ...
Client ← Server:  TLS ServerHello (PLAINTEXT headers, encrypted body from here)
Client → Server:  [Encrypted Application Data]
```

the DP application extracts the SNI and runs the same policy lookup as for DNS.
If blocked → TCP RST injected to terminate the connection.

---

## Where this fits in the real application

```text
TCP packet, dst_port = 443
  │
  ├─► TCP payload stored in tls_session_table
  │   (state machine waits for ClientHello across possibly fragmented pkts)
  │
  ├─► hs_scan_payload(payload, len, worker_info, &matchCtx)
  │     Hyperscan scans for HS_PATTERN_ID_TLS = 1
  │     Pattern matches the SNI extension type bytes (0x00 0x00)
  │     at some offset 'from' within the payload
  │
  ├─► on_hs_match callback fires: id=1, from=<SNI_ext_offset>
  │
  │   /* Exact code from domain_scan.c: */
  │   uint16_t sni_len = read_u16_be(payload + from + 7);
  │   memcpy(matchCtx->extractedDomain, payload + from + 9, sni_len);
  │   matchCtx->extractedDomainLength = sni_len;
  │
  └─► url_policy_for_tls(sni, worker_info, ...)
        → hash table lookup + Hyperscan fallback (Module 17)
        → DROP → TCP RST injection
        → ALLOW → forward
```

---

## Files

| File | Purpose |
|---|---|
| `tls_sni.h` | Structs, enums, constants, API |
| `tls_sni.c` | Full walker + Hyperscan-style extractor + 4 tests |
| `Makefile` | Build rules |

---

## Build and run

```bash
make
./tls_sni
```

Expected output:
```
=== Module 07: TLS SNI Extractor ===

--- Struct sizes ---
  tls_record_hdr_t    : 5 bytes (expected 5)
  tls_handshake_hdr_t : 4 bytes (expected 4)

--- Test 1: Full ClientHello walker ---
  SNI found       : "www.secure-corp.example"
  SNI length      : 23
  Client version  : TLS 1.2 (0x0303)
  PASS

--- Test 2: Hyperscan-style extraction ---
  Extension type at offset 54: 0x0000 (server_name=yes)
  from+7 bytes: 0x00 0x17 → length=23
  Extracted SNI   : "www.secure-corp.example" (23 bytes)
  PASS

--- Test 3: C2 domain extraction ---
  SNI extracted   : "malicious.c2-server.io"
  → policy lookup → found in malicious_domain_table → BLOCK
  PASS

--- Test 4: non-Handshake record rejected ---
  Application Data record correctly rejected (ret=-1)
  PASS
```

---

## Key concepts in the code

### 1. TLS record hierarchy

```text
TLS Record (5 bytes)
  └─ Handshake record
       └─ ClientHello body
            ├─ version (2)
            ├─ random  (32)
            ├─ session_id (variable)
            ├─ cipher_suites (variable)
            ├─ compression (variable)
            └─ Extensions list
                 ├─ server_name (0x0000)  ← SNI here
                 ├─ supported_versions (0x002B)
                 └─ ALPN (0x0010)
```

### 2. The 3-byte handshake length — a common bug

```c
/* WRONG: treats length as 4 bytes */
uint32_t hs_len = *(uint32_t *)(payload + 5);   // reads type + 3 len bytes

/* CORRECT: read 3 bytes manually */
uint32_t hs_len = ((uint32_t)hs->len[0] << 16) |
                  ((uint32_t)hs->len[1] <<  8) |
                   (uint32_t)hs->len[2];
```

The TLS Handshake header type field (1 byte) is followed by a 24-bit length,
not a 32-bit one. Treating it as 4 bytes reads the type into the high byte
of the length — silently producing a wrong length value.

### 3. Hyperscan match offsets (the real domain_scan.c logic)

```text
SNI extension layout (starting at Hyperscan 'from'):

  from+0  from+1  : type     = 0x00 0x00  (server_name)
  from+2  from+3  : ext_len
  from+4  from+5  : list_len
  from+6          : name_type = 0x00       (host_name)
  from+7  from+8  : NAME LENGTH            ← read_u16_be(payload + from + 7)
  from+9  ...     : NAME BYTES             ← payload + from + 9
```

### 4. TLS 1.3 — SNI still in plaintext

TLS 1.3 encrypts more of the handshake than TLS 1.2, but the ClientHello
(including SNI) remains in plaintext. The record-layer version field will
still show `0x0301` for compatibility.

### 5. When SNI is absent

Some clients (old browsers, embedded devices, curl without SNI) send
no `server_name` extension. In that case `result->sni_found == 0` and
the hostname is empty. The real app falls back to IP-based policy.

---

## TLS struct mapping to DPDK / real app

| This module | real DP application |
|---|---|
| `tls_record_hdr_t` | Inline struct in `pkt_proc.h` |
| `TLS_CONTENT_HANDSHAKE = 0x16` | `tls_content_type` enum in `pkt_proc.h` |
| `from+7` name_len | `read_u16_be(payload + from + 7)` in `domain_scan.c` `on_hs_match` |
| `from+9` name bytes | `payload + from + 9` in `domain_scan.c` `on_hs_match` |
| `HS_PATTERN_ID_TLS = 1` | Defined in `domain_scan.h` |

---

## Next module

**Layer 0 complete.** Modules 01–07 cover pure-C foundations.

**Module 08 — DPDK EAL Init**: The first DPDK module. Initialize the
Environment Abstraction Layer, hand CPU cores to DPDK, set up hugepages,
and launch the first lcore function. (Reference code — requires DPDK.)

---

## Source files

| File | Download |
|---|---|
| `tls_sni.h` | [tls_sni.h](https://github.com/Ajay3007/dataplane-learning/blob/main/07-tls-sni/tls_sni.h){:target="_blank" rel="noopener noreferrer"} |
| `tls_sni.c` | [tls_sni.c](https://github.com/Ajay3007/dataplane-learning/blob/main/07-tls-sni/tls_sni.c){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/07-tls-sni/Makefile){:target="_blank" rel="noopener noreferrer"} |
