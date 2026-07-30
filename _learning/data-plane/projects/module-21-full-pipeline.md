---
layout: learning
title: "Module 21 — Full Pipeline (Annotated Assembly)"
permalink: /learning/data-plane/projects/module-21-full-pipeline/
---

# Module 21 — Full Pipeline (Annotated Assembly)

> Runs standalone with `make && ./full_pipeline` (no DPDK/HS/Kafka needed).  
> Every production API call is annotated with its module number.

## What this module is

A single annotated C file that assembles all 20 prior modules into one
complete dataplane application. Read it top-to-bottom to see exactly
how a production DPDK URL filtering engine is structured — from `main()`
startup through the packet hot path to graceful shutdown.

---

## Build and run

```bash
make
./full_pipeline
```

Expected output:
```
=== Module 21: Full Pipeline ===
Simulating 1000 packets across 2 workers

[1] Config loaded
[2] Logger initialized
[3] EAL initialized (simulation: using pthreads)
...
[11] Policy tables seeded: 3 domains, 2 malicious
[12] Inter-lcore rings created
[13] Launching lcores...

[Final Statistics]
  rx=1000  tx=762  drop=238
  dns=800  tls=200  sinkholes=238
  cdr_records=1000
```

---

## Full system architecture

```text
┌─────────────────────────────────────────────────────────────────┐
│                     the DP application Process                             │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  lcore 0: MAIN CONTROL LOOP                             │    │
│  │                                                          │    │
│  │  rd_kafka_consumer_poll()     ← Module 20               │    │
│  │    apply_policy_message()                                │    │
│  │      SYNC_COMPLETE → atomic_swap + RCU synchronize       │    │
│  │                                                          │    │
│  │  rd_kafka_poll(cdr_producer)  ← Module 19                │    │
│  │  print_stats()                ← Module 13                │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌──────────────┐  rings  ┌──────────────────┐  ring  ┌──────┐  │
│  │ lcore 1: RX  │ ──────► │ lcores 3-6:      │ ──────►│ TX   │  │
│  │              │         │ WORKERS           │        │      │  │
│  │ rte_eth_     │         │                   │        │rte_  │  │
│  │ rx_burst()   │         │ parse ETH/IP/UDP  │        │eth_  │  │
│  │ Module 10    │         │ Module 05         │        │tx_   │  │
│  │              │         │                   │        │burst │  │
│  │ distribute   │         │ DNS: dns_parse()  │        │Mod10 │  │
│  │ Module 11    │         │ Module 06         │        └──────┘  │
│  └──────────────┘         │                   │                  │
│                            │ TLS: hs_scan()    │                  │
│                            │ Module 16         │                  │
│                            │                   │                  │
│                            │ policy_lookup()   │                  │
│                            │ Module 17         │                  │
│                            │                   │                  │
│                            │ if SINKHOLE:      │                  │
│                            │  dns_sinkhole()   │                  │
│                            │  Module 18        │                  │
│                            └──────────────────┘                  │
└─────────────────────────────────────────────────────────────────┘
        │ CDR (Module 19)              ▲ Policy updates (Module 20)
        ▼                              │
   ┌──────────┐                 ┌──────────────────┐
   │  Kafka   │                 │  PM              │
   │  Broker  │                 │ (Provisioning    │
   └──────────┘                 └──────────────────┘
```

---

## Startup sequence (exact order, production)

```text
Step  What                          Module  Why order matters
----  ---                           ------  -----------------
 1    config_load()                  01     Everything reads from config
 2    logger_init()                  02     All following steps log errors
 3    rte_eal_init()                 08     Hugepages, CPU affinity, NIC probe
 4    rte_pktmbuf_pool_create()      09     NIC needs pool for RX descriptors
 5    port_init()                    10     Needs pool from step 4
 6    NUMA alloc: hash tables        12/14  Must know socket from step 3
 7    hs_create_db()          15     Patterns loaded, DB compiled
 8    hs_init_global_scratch()    16     Needs DB from step 7
 9    kafka_producer_init()          19     CDR topic ready before workers
10    kafka_consumer_init()          20     Read initial policy before workers
11    Seed policy tables             12/20  Workers need policies from day 1
12    rte_ring_create()              03/11  Workers need rings before launch
13    rte_eal_remote_launch()        08/11  TX first, then workers, then RX
14    main control loop              19/20  Poll Kafka, flush CDR, print stats
```

**Step 13 launch order (TX → workers → RX) is critical:**
- If RX launches before workers: packets pile up in rings until workers start
- If TX launches after workers: workers can't enqueue (tx_ring is NULL)
- Correct order ensures pipeline is ready before packets flow

---

## Shutdown sequence (exact order, production)

```text
SIGTERM received → g_shutdown = 1

1. Stop RX lcore first  → stops generating packets
2. Wait for RX lcore
3. Stop worker lcores   → workers finish in-flight packets + flush CDR batches
4. Wait for workers
5. Stop TX lcore LAST   → TX drains remaining packets from tx_ring
6. Wait for TX
7. Kafka flush (Module 19): rd_kafka_flush(rk_producer, 5000)
8. Hyperscan cleanup: hs_free_scratch() + hs_free_database()
9. rte_eth_dev_stop() + rte_eth_dev_close()
10. rte_eal_cleanup()
```

**Step 5 (TX last) is critical:** workers may have enqueued a final burst
after getting the stop signal. If TX stops first, those sinkhole responses
never reach the client.

---

## Complete module dependency map

```text
Module 21 (Full Pipeline)
  │
  ├── Module 01  config_load()
  ├── Module 02  logger_init()
  │
  ├── Module 08  rte_eal_init() + lcore launch
  │    └── Module 14  NUMA socket allocation
  │
  ├── Module 09  rte_pktmbuf_pool_create()
  ├── Module 10  port_init()
  │
  ├── Module 03  ring_create()
  ├── Module 12  rte_hash CRUD (domain_details_table)
  │
  ├── Module 15  hs_create_db()
  ├── Module 16  hs_init_global_scratch()
  │
  ├── Module 19  kafka_producer_init()
  ├── Module 20  kafka_consumer_init()
  │
  └── PER-PACKET HOT PATH (worker lcore):
       ├── Module 05  ETH/IP/UDP-TCP header parse
       ├── Module 06  dns_parse_message()
       ├── Module 07  tls_extract_sni_from_match()
       ├── Module 13  atomic counter increments
       ├── Module 16  hs_scan_payload()
       ├── Module 17  url_policy_for_dns()
       ├── Module 18  dns_build_sinkhole_v4/6()
       └── Module 19  cdr_batch_add()
```

---

## Learning path recap

| Module | Topic | Dependencies |
|---|---|---|
| 01 | Config parser | none |
| 02 | Logger | none |
| 03 | Ring buffer | none |
| 04 | Hash map | none |
| 05 | Packet structs | none |
| 06 | DNS parser | 05 |
| 07 | TLS SNI extractor | 05 |
| 08 | DPDK EAL init | 01, 02 |
| 09 | Mempool + mbuf | 08 |
| 10 | Port init | 08, 09 |
| 11 | Multi-lcore pipeline | 08, 09, 10, 03 |
| 12 | rte_hash CRUD | 08 |
| 13 | Atomic stats | none |
| 14 | NUMA alloc | 08 |
| 15 | Hyperscan compile | none |
| 16 | Hyperscan scan | 15 |
| 17 | Two-tier policy | 12, 16 |
| 18 | DNS sinkhole | 05, 06 |
| 19 | Kafka producer | none |
| 20 | Kafka consumer | 19, 17 |
| **21** | **Full pipeline** | **all** |

---

## Source files

| File | Download |
|---|---|
| `full_pipeline.c` | [full_pipeline.c](https://github.com/Ajay3007/dataplane-learning/blob/main/21-full-pipeline/full_pipeline.c){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/21-full-pipeline/Makefile){:target="_blank" rel="noopener noreferrer"} |
