---
layout: default
title: "Module 06 — DNS Parser"
permalink: /learning/data-plane/projects/module-06-dns-parser/
---

# Module 06 — DNS Parser

## What you learn

How to parse a complete DNS message from raw wire bytes — queries and
responses, over UDP and TCP, including pointer compression and CNAME chains.

After this module you have everything needed to extract the domain name
and query type from any DNS packet entering the pipeline, which is the
prerequisite for both policy lookup (Module 17) and DNS sinkholing (Module 18).

---

## Where this fits in the real application

```text
UDP payload (or TCP payload after stripping 2-byte length prefix)
  │
  ├─► dns_parse_message(wire, wire_len, &msg)
  │
  │   msg.qname   = "blocked-malware.example.com"
  │   msg.qtype   = DNS_TYPE_A  (or DNS_TYPE_AAAA)
  │   msg.id      = 0xcafe
  │   msg.question_wire_end = offset after question section
  │
  ├─► dns_normalize_name(msg.qname)   → lowercase
  │
  ├─► rte_hash_lookup_data(domain_details_table, msg.qname, &fd)
  │     hit  → apply filter_details (Module 17)
  │     miss → hs_scan_dp_process_group(msg.qname, ...) (Module 17)
  │
  └─► if blocked:
        qtype A    → inject A    answer (walled-garden IPv4)  (Module 18)
        qtype AAAA → inject AAAA answer (walled-garden IPv6)  (Module 18)
```

---

## Files

| File | Purpose |
|---|---|
| `dns_parser.h` | `dns_message_t`, `dns_answer_t`, API declarations |
| `dns_parser.c` | Parser + 5 tests (A query, AAAA with normalization, A response, CNAME+AAAA chain, DNS over TCP) |
| `Makefile` | Build rules (includes `../05-packet-structs` for `packet_structs.h`) |

---

## Build and run

```bash
make
./dns_parser
```

Expected output:
```
=== Module 06: DNS Parser ===

--- Test 1: A query for blocked-malware.example.com ---
  ID      : 0xcafe
  Type    : QUERY
  [Question]
    qname : blocked-malware.example.com
    qtype : A (1)
  → policy engine would look up: "blocked-malware.example.com" (type A)
  PASS

--- Test 2: AAAA query — uppercase normalization ---
  'GOOGLE.COM' normalized to 'google.com'
  PASS

--- Test 3: A response with pointer compression ---
  Pointer compression decoded correctly: www.example.com → 93.184.216.34
  PASS

--- Test 4: CNAME + AAAA chain response ---
  CNAME decoded: cdn.example.com → origin.example.com
  PASS

--- Test 5: DNS over TCP ---
  TCP length prefix: 38 bytes
  Extracted domain: "ads.tracker.io"
  PASS
```

---

## Key concepts in the code

### 1. DNS qname wire format — label encoding

DNS names are **not** null-terminated strings in the wire format. They
use length-prefixed labels:

```text
"www.example.com" on the wire:

  Offset  Value   Meaning
  ------  -----   -------
  0       0x03    length = 3
  1-3     "www"
  4       0x07    length = 7
  5-11    "example"
  12      0x03    length = 3
  13-15   "com"
  16      0x00    root label = end of name
```

### 2. Pointer compression (RFC 1035 §4.1.4)

In DNS responses, names are often back-referenced to save space.
If the top 2 bits of a length byte are `11`, it's a pointer:

```text
0xC0 0x0C = 1100_0000 0000_1100
             ^^                 top 2 bits set → pointer
               ^^^^^^^^^^^^^^   14-bit offset = 12
```

So `0xC0 0x0C` means "the name is at offset 12 in this DNS message".
Without handling this, answer section parsing breaks for virtually all real responses.

### 3. DNS over TCP — 2-byte length prefix

```text
TCP stream (DNS):  +-----+-----+---DNS message---+
                   | len (2B)  |  DNS header + qname + ... |
                   +-----+-----+---DNS message---+
```

```c
uint16_t dns_len = read_u16_be(tcp_payload);
uint8_t *dns_msg = tcp_payload + 2;
dns_parse_message(dns_msg, dns_len, &msg);
```

### 4. qtype matters for sinkholing

The query type drives what kind of fake DNS answer to inject:

```text
Client sends:  www.blocked.com  A    query
SASE DP injects: A answer with 10.0.0.1 (walled-garden IPv4)

Client sends:  www.blocked.com  AAAA query
SASE DP injects: AAAA answer with fd00::1 (walled-garden IPv6)
```

### 5. Name normalisation

DNS names are case-insensitive (RFC 1034 §3.1). A client may send
`GOOGLE.COM`, `Google.Com`, or `google.com` — all mean the same thing.

`dns_normalize_name()` lowercases the qname **before** any hash table
lookup, so the policy table only needs to store lowercase entries.

### 6. `question_wire_end` offset

After parsing, `msg.question_wire_end` holds the byte offset where the
question section ends. Module 18 (DNS sinkhole) uses this to know where
to write the injected answer section in the in-place mbuf rewrite:

```text
[DNS header 12B][question section][  ← inject answer here]
                                  ^
                              question_wire_end
```

---

## DNS record types reference

| Type | Value | rdata | Used for |
|---|---|---|---|
| A | 1 | 4-byte IPv4 | Most queries, sinkhole target |
| AAAA | 28 | 16-byte IPv6 | IPv6 queries, sinkhole target |
| CNAME | 5 | label-encoded name | CDN aliases — follow the chain |
| MX | 15 | priority + name | Email — not filtered in SASE DP |
| NS | 2 | label-encoded name | Nameserver delegation |

---

## Next module

**Module 07 — TLS SNI Extractor**: Parse a TLS ClientHello from a TCP
payload to extract the Server Name Indication (SNI) field — the domain
name for HTTPS connections.

---

## Source files

| File | Download |
|---|---|
| `dns_parser.h` | [dns_parser.h]({{ '/assets/code/data-plane/projects/06-dns-parser/dns_parser.h' | relative_url }}) |
| `dns_parser.c` | [dns_parser.c]({{ '/assets/code/data-plane/projects/06-dns-parser/dns_parser.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/06-dns-parser/Makefile' | relative_url }}) |
