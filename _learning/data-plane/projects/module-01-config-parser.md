---
layout: learning
title: "Module 01 — Config Parser"
permalink: /learning/data-plane/projects/module-01-config-parser/
---

# Module 01 — Config Parser

## What you learn

How to write a config file parser in C and use it to drive all subsystem
initialization in a dataplane application.

In a real DPDK app **nothing can start without a config file**. The config
tells the application which CPU cores to hand to DPDK, how many NIC queues
to open, where Kafka is running, where the Hyperscan pattern files live, and
which lcore plays which role (RX / TX / worker). Every piece of the system
reads from this one parsed structure.

---

## Where this fits in the real application

```text
main()
  │
  ├─► config_load()          ← THIS MODULE
  │     parse dp_app.conf
  │     populate config_t
  │
  ├─► build eal_argv[]       (Module 11 — EAL Init)
  │     from config: cores, socket_mem, hugepage_sz
  │
  ├─► rte_eal_init()         (Module 11)
  │
  ├─► port_init()            (Module 13)
  │     from config: num_rx_queues, rx_desc, tx_desc
  │
  ├─► kafka_init()           (Module 25/26)
  │     from config: broker, topic_policy, topic_cdr
  │
  ├─► hs_init_global_scratch()   (Module 19/21)
  │     from config: pattern_file, pattern_file2
  │
  └─► launch worker lcores   (Module 15)
        from config: rx_lcore, tx_lcore, worker_lcores
```

In the production dataplane project this logic lives in `app_main.c`.

---

## Files

| File | Purpose |
|---|---|
| `config_parser.c` | Parser implementation + demo main() |
| `sample.conf` | Example config with all sections a real DP app uses |
| `Makefile` | Build rules |

---

## Build and run

```bash
make
./config_parser             # reads sample.conf
./config_parser my.conf     # reads a custom config file
```

Expected output:
```
=== Module 01: Config Parser ===

[config] Loaded 23 entries:
  [eal                ]  cores                    = 0-7
  [eal                ]  socket_mem               = 2048
  ...

--- Values a real dataplane app reads at startup ---

[EAL]
  cores         = 0-7
  socket_mem    = 2048 MB
  ...
```

---

## Key concepts in the code

### 1. Parse once, read many times
`config_load()` is called once. The resulting `config_t` is a global (or
passed by pointer). Every subsystem calls `config_get_*()` to read its
values — no one re-parses the file.

### 2. Section + key lookup
Values are identified by `[section] + key`, not just key. This prevents
name collisions across subsystems (`eal.log_level` vs `logging.level`).

### 3. Default values everywhere
`config_get_int(&cfg, "port", "num_rx_queues", 1)` — the third argument is
the default. Code never crashes on a missing key; it falls back gracefully.
This is critical in production where operators may omit optional settings.

### 4. Inline comments stripped
`broker.example.com:9092  # primary broker` is parsed as `broker.example.com:9092`.
Without this, the `#` would end up in the Kafka broker string and cause a
connection failure.

### 5. Type coercion at read time
The file stores everything as strings. `config_get_int()` and
`config_get_bool()` convert at read time with proper error handling —
same pattern used with every C config library.

---

## Config format reference

```ini
# Full-line comment (ignored)
; Also a comment

[section_name]
key = value
key = value   # inline comment (stripped)
```

Supported value types:

| Function | Accepts |
|---|---|
| `config_get_string()` | any string |
| `config_get_int()` | decimal integer |
| `config_get_bool()` | true/false, yes/no, 1/0 |

---

## Next module

**Module 02 — Logger**: Once config is parsed the first real subsystem to
initialize is the logger. Every subsequent module (EAL, ports, Kafka, policy
engine) uses it to report startup progress and errors.

---

## Source files

| File | Download |
|---|---|
| `config_parser.c` | [config_parser.c](https://github.com/Ajay3007/dataplane-learning/blob/main/01-config-parser/config_parser.c){:target="_blank" rel="noopener noreferrer"} |
| `sample.conf` | [sample.conf](https://github.com/Ajay3007/dataplane-learning/blob/main/01-config-parser/sample.conf){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/01-config-parser/Makefile){:target="_blank" rel="noopener noreferrer"} |
