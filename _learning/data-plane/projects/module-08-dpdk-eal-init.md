---
layout: default
title: "Module 08 — DPDK EAL Initialization"
permalink: /learning/data-plane/projects/module-08-dpdk-eal-init/
---

# Module 08 — DPDK EAL Initialization

> **Reference code** — requires DPDK installed. Read the code as a reference
> when building a real DPDK application. The concepts and API calls are
> production-accurate.

## What you learn

How to initialize the DPDK Environment Abstraction Layer (`rte_eal_init`),
build an EAL argument vector programmatically from config, assign CPU cores
to roles (RX / TX / WORKER), launch per-lcore functions, and shut down cleanly.

This is the first code that runs in every DPDK application after the
application-level setup (config, logger). Everything in subsequent modules —
mempools, ports, rings, Hyperscan — only works after `rte_eal_init` succeeds.

---

## What rte_eal_init actually does

```text
rte_eal_init(argc, argv)
  │
  ├─ Locks hugepages
  │    mmap() pre-allocated 2MB pages into the process address space.
  │    These are pinned in physical memory — the OS never pages them out.
  │    All rte_mbuf packet buffers live here (zero kernel allocation at runtime).
  │
  ├─ Sets CPU affinity
  │    Each lcore in the list is pinned to a physical CPU core via
  │    pthread_setaffinity_np(). From this point on, the OS never
  │    migrates these threads — they run on their assigned physical core only.
  │
  ├─ Initialises per-lcore memory
  │    rte_malloc zones per NUMA socket.
  │
  ├─ Probes PCI devices (NICs)
  │    Finds NIC devices bound with dpdk-devbind --bind=vfio-pci.
  │    DPDK takes exclusive ownership — the kernel network stack can no
  │    longer see this NIC.
  │
  └─ Returns: number of EAL args consumed
```

---

## Where this fits in the real application

```text
main()
  │
  ├─► config_load()           (Module 01)
  ├─► logger_init()           (Module 02)
  │
  ├─► build_eal_args()        ← reads cores, socket_mem from config
  ├─► rte_eal_init()          ← THIS MODULE
  │
  ├─► rte_pktmbuf_pool_create()   (Module 09)
  ├─► port_init()                 (Module 10)
  ├─► initialize_global_scratch() (Module 15/16)
  ├─► kafka_init()                (Module 19/20)
  ├─► rte_ring_create()           (Module 03 concept)
  │
  ├─► assign_lcore_roles()    ← THIS MODULE
  ├─► rte_eal_remote_launch() ← THIS MODULE (one call per worker lcore)
  │
  ├─► main lcore control loop (Kafka poll, stats, OAM)
  │
  └─► rte_eal_cleanup()       ← THIS MODULE
```

---

## Files

| File | Purpose |
|---|---|
| `eal_init.c` | Full EAL init, lcore topology, role assignment, launch, shutdown |
| `Makefile` | DPDK build via pkg-config (RedHat/Rocky compatible) |

---

## Setup (RedHat / Rocky Linux)

```bash
# Install DPDK
dnf install dpdk dpdk-devel

# Allocate hugepages (2MB pages, 512 = 1 GB)
echo 512 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

# Mount hugepage filesystem (if not auto-mounted)
mount -t hugetlbfs nodev /dev/hugepages

# For NIC binding (optional — needed for real packet IO)
dpdk-devbind --status
dpdk-devbind --bind=vfio-pci <PCI_addr>

# Build and run
make
sudo ./eal_init
```

---

## Key concepts in the code

### 1. EAL arg vector — built by the app, not the shell

```c
/* Instead of running: ./sase_dp -l 0-7 --socket-mem 2048 */
/* The app builds argv[] programmatically from config: */

eal_add_arg("sase_dp");
eal_add_arg("-l");
eal_add_arg(config_get_string(&cfg, "eal", "cores", "0-3"));
eal_add_arg("--socket-mem");
eal_add_arg(config_get_string(&cfg, "eal", "socket_mem", "1024"));
...
ret = rte_eal_init(eal_argc, eal_argv);
```

### 2. Lcore vs CPU core

A **lcore** is DPDK's abstraction for a logical CPU core. Lcore IDs are
DPDK's numbering, not the OS's.

```c
rte_lcore_count()              /* total lcores handed to DPDK */
rte_get_main_lcore()           /* main thread's lcore ID      */
rte_lcore_to_socket_id(id)     /* which NUMA socket this lcore is on */
RTE_LCORE_FOREACH_WORKER(id)   /* iterate all non-main lcores */
```

### 3. Role assignment — why it matters

```text
NIC port 0 queue 0 → RX lcore 1 → rte_ring → Worker lcores 3,4,5,6
                                                      ↓
                   TX lcore 2 ← rte_ring ←────────────┘
```

### 4. `rte_eal_remote_launch` vs `pthread_create`

```c
/* DPDK way — lcore already pinned to CPU core, just start the function */
rte_eal_remote_launch(lcore_worker_func, &lcore_info[id], id);

/* NOT used in DPDK for worker cores — would create an unpinned thread */
pthread_create(&tid, NULL, lcore_worker_func, &lcore_info[id]);
```

### 5. `rte_pause()` — the polling spin hint

```c
while (running) {
    nb_rx = rte_eth_rx_burst(port, queue, mbufs, BURST);
    if (nb_rx == 0) {
        rte_pause();   /* x86 PAUSE instruction — reduces power, improves HT */
        continue;
    }
    /* process mbufs */
}
```

**Never** use `sleep()` or `usleep()` in an lcore function. Sleeping yields
the core to the OS scheduler, potentially stalling for milliseconds — during
which time the NIC RX ring fills and packets are dropped.

### 6. Graceful shutdown sequence

```text
SIGTERM received
  → signal_handler sets force_quit = 1
  → main lcore exits control loop
  → sets lcore_info[id].running = 0 for each worker
  → worker lcores see running=0, exit their loops
  → rte_eal_wait_lcore(id) for each worker  ← must call before cleanup
  → flush CDR to Kafka
  → rte_eal_cleanup()
  → exit(0)
```

---

## Common errors

| Error | Cause | Fix |
|---|---|---|
| `No hugepages available` | Hugepages not allocated | `echo 512 > /sys/.../nr_hugepages` |
| `Cannot init EAL: invalid core list` | lcore range invalid | Check CPU count with `nproc` |
| `EAL: No probed ethernet devices` | NIC not bound to vfio-pci | `dpdk-devbind --bind=vfio-pci <addr>` |
| `rte_eal_init: Permission denied` | Not running as root | `sudo ./eal_init` or set capabilities |
| `Cannot create lock on hugepage file` | Another DPDK process running | Kill other DPDK processes first |

---

## Next module

**Module 09 — Mempool + mbuf**: Create an `rte_mempool` for packet buffers
(`rte_mbuf`), understand the mbuf lifecycle (alloc → fill → process → free),
and learn why mempools exist.

---

## Source files

| File | Download |
|---|---|
| `eal_init.c` | [eal_init.c]({{ '/assets/code/data-plane/projects/08-dpdk-eal-init/eal_init.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/08-dpdk-eal-init/Makefile' | relative_url }}) |
