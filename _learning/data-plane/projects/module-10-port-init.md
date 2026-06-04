---
layout: default
title: "Module 10 — NIC Port Initialization"
permalink: /learning/data-plane/projects/module-10-port-init/
---

# Module 10 — NIC Port Initialization

> **Reference code** — requires DPDK and a DPDK-bound NIC (or `--vdev net_null0`).

## What you learn

How to configure a DPDK NIC port end-to-end: detect capabilities, set up
RX/TX queues and descriptor rings, enable RSS for multi-queue distribution,
configure hardware offloads (checksum, VLAN), start the port, and verify
link state. This is the last setup step before worker lcores can call
`rte_eth_rx_burst()` / `rte_eth_tx_burst()`.

---

## Port init sequence

```text
rte_eth_dev_count_avail()            → how many NICs available
rte_eth_dev_info_get(port, &info)    → query NIC capabilities
  │
  ├─ mask requested offloads against info.rx_offload_capa
  ├─ mask RSS hash types against info.flow_type_rss_offloads
  │
rte_eth_dev_configure(port, nb_rx_q, nb_tx_q, &port_conf)
  │
rte_eth_dev_adjust_nb_rx_tx_desc()   → align descriptor counts to NIC limits
  │
rte_eth_rx_queue_setup() × nb_rx_q   → each queue gets a slice of mbuf pool
rte_eth_tx_queue_setup() × nb_tx_q
  │
rte_eth_dev_start()                  → NIC starts link negotiation + DMA
rte_eth_promiscuous_enable()         → accept all frames (not just own MAC)
  │
check_port_link_status()             → poll until UP (timeout = 9 sec)
```

---

## Files

| File | Purpose |
|---|---|
| `port_init.c` | Full port init: capability check, configure, queues, start, link poll, stats |
| `Makefile` | DPDK pkg-config build |

---

## Key concepts in the code

### 1. Capability intersection — the most common bug

```c
/* WRONG: request offloads blindly */
port_conf.rxmode.offloads = RTE_ETH_RX_OFFLOAD_CHECKSUM;

/* CORRECT: mask against what the NIC actually supports */
port_conf.rxmode.offloads &= dev_info.rx_offload_capa;
```

If you request `CHECKSUM` on a NIC that doesn't support it,
`rte_eth_dev_configure()` returns `-EINVAL`. Always intersect against
`dev_info` capabilities.

The same applies to RSS hash types:
```c
port_conf.rx_adv_conf.rss_conf.rss_hf &= dev_info.flow_type_rss_offloads;
```

### 2. RSS — why it's critical for multi-lcore scaling

Without RSS (single RX queue):
```text
All packets → queue 0 → RX lcore → ring → single worker lcore
                                            ↑ bottleneck
```

With RSS (4 RX queues, one per worker lcore):
```text
DNS from 198.51.100.x → hash=0xA3 % 4 = 3 → queue 3 → worker lcore 6
DNS from 10.0.0.x    → hash=0x51 % 4 = 1 → queue 1 → worker lcore 4
```

RSS hash is computed by the NIC hardware (Toeplitz algorithm on src/dst
IP + port). Each worker lcore polls its own dedicated queue — no contention.

### 3. Descriptor ring depth and mbuf pool sizing

```text
RX ring (1024 descriptors):
  NIC pre-fills these with mbuf pointers from the pool.
  If the software is slow and all 1024 descriptors are full:
    → new packets are dropped → stats.imissed increments

Pool must always have more mbufs than (sum of all RX descriptor rings):
  4 queues × 1024 desc × 1 port × 2 = 8192 → pool of 8191 is just enough
```

### 4. `rte_eth_dev_adjust_nb_rx_tx_desc`

Different NICs have different constraints on descriptor counts.
Always call this after `rte_eth_dev_configure()`:

```c
uint16_t nb_rxd = 1024, nb_txd = 1024;
rte_eth_dev_adjust_nb_rx_tx_desc(port, &nb_rxd, &nb_txd);
/* nb_rxd / nb_txd are now adjusted to valid values for this NIC */
```

### 5. Promiscuous mode — why it's necessary

the DP application sits inline between clients and the internet — packets are addressed
to the router, not to the appliance. Promiscuous mode makes the NIC accept
everything regardless of dst MAC.

### 6. TX hardware checksum offload

After DNS sinkhole response is built in Module 18:
```c
m->ol_flags |= RTE_MBUF_F_TX_IPV4 | RTE_MBUF_F_TX_IP_CKSUM
             | RTE_MBUF_F_TX_UDP_CKSUM;
ip4->checksum = 0;
udp->checksum = rte_ipv4_phdr_cksum(ip4, m->ol_flags);
```

For this to work, the TX queue must have been set up with the same offloads
in `port_conf.txmode`. If either is missing, `rte_eth_tx_burst()` silently
ignores the flags and transmits with checksum=0 — every receiver drops the packet.

### 7. `stats.imissed` — the first metric to check

```c
struct rte_eth_stats stats;
rte_eth_stats_get(port, &stats);
if (stats.imissed > 0)
    LOG_WARN("Port %u: %lu packets dropped (NIC ring full)", port, stats.imissed);
```

`imissed` increments when a packet arrives but there's no free mbuf or no
free descriptor. In the DP application, `imissed` was the first indicator when the
product went live at 50 Gbps and revealed that one lcore was occasionally
taking too long in the Hyperscan path.

---

## Testing without a physical NIC

```c
/* Add to eal_args in main(): */
"--vdev", "net_null0,copy=1",
```

`net_null` is a virtual NIC PMD that accepts TX packets and returns empty
RX bursts. The entire `port_init()` code runs identically — useful for CI/CD.

---

## Next module

**Module 11 — Multi-lcore RX/TX Pipeline**: Wire together everything from
Modules 08–10 into a complete multi-lcore packet processing pipeline skeleton.

---

## Source files

| File | Download |
|---|---|
| `port_init.c` | [port_init.c]({{ '/assets/code/data-plane/projects/10-port-init/port_init.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/10-port-init/Makefile' | relative_url }}) |
