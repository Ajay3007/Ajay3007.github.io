---
layout: default
title: "Module 02 — Logger"
permalink: /learning/data-plane/projects/module-02-logger/
---

# Module 02 — Logger

## What you learn

How to write a thread-safe, level-filtered logger in C that outputs
timestamped lines to both console and file — the pattern used throughout
the DP codebase.

In a multi-lcore DPDK application, multiple CPU cores log concurrently.
Without a thread-safe logger you get interleaved, unreadable output.
The logger is initialized once at startup and then every subsystem — EAL,
ports, Hyperscan, Kafka, workers — uses the same `LOG_*` macros.

---

## Where this fits in the real application

```text
main()
  │
  ├─► config_load()             (Module 01)
  │
  ├─► logger_init(level, file)  ← THIS MODULE
  │     reads level from config: "DEBUG" / "INFO" / "WARN" / "ERROR"
  │     opens log file from config: /var/log/dp_app/dp_app.log
  │
  ├─► LOG_INFO("EAL initializing...")
  ├─► rte_eal_init()            (Module 11)
  │
  ├─► LOG_INFO("Port 0 configuring...")
  ├─► port_init()               (Module 13)
  │
  ├─► LOG_INFO("Hyperscan compiling...")
  ├─► hs_init_global_scratch()  (Module 19-21)
  │
  └─► LOG_INFO("Startup complete, packet processing active")
```

Every module from 03 onwards includes `logger.h` and uses `LOG_*` macros.

---

## Files

| File | Purpose |
|---|---|
| `logger.h` | Struct, enum, macros, function declarations — included by every module |
| `logger.c` | Implementation + demo startup sequence |
| `Makefile` | Build rules (`-lpthread` required) |

---

## Build and run

```bash
make
./logger
```

Expected output (with ANSI colours in terminal):

```
[2024-06-02 14:32:01.123] [INFO ] [logger.c:180] === DP Application starting ===
[2024-06-02 14:32:01.124] [INFO ] [logger.c:181] Logger initialized: level=DEBUG
[2024-06-02 14:32:01.124] [DEBUG] [logger.c:184] Config: eal.cores=0-7, socket_mem=2048
...
[2024-06-02 14:32:01.130] [WARN ] [logger.c:210] Port 0: RX ring 80% full on queue 2
[2024-06-02 14:32:01.131] [ERROR] [logger.c:212] Hyperscan scratch alloc failed...
...
[2024-06-02 14:32:01.135] [WARN ] [logger.c:221] This WARN line IS printed
```

---

## Key concepts in the code

### 1. Log format
```
[TIMESTAMP ms] [LEVEL] [file.c:line] message
```
Millisecond timestamps let operators correlate log events with packet
captures (tcpdump/Wireshark) down to the millisecond.

### 2. Dual output
- **stderr** (console): ANSI colour per level. For real-time watching.
- **Log file**: no colour codes (ANSI escape sequences break `grep`).
  File is `fflush()`-ed after every write so crash logs are not lost.

### 3. Level filtering
```c
if (level < g_logger.level)
    return;    /* fast path — no lock, no I/O */
```
In production the level is `INFO`. Switching to `DEBUG` via `log_set_level()`
at runtime (triggered by SIGUSR1) floods the log with per-packet detail —
useful for diagnosing a live issue without restarting the application.

### 4. Thread safety
```c
pthread_mutex_lock(&g_logger.lock);
/* write to stderr / file */
pthread_mutex_unlock(&g_logger.lock);
```
In DPDK, `rte_log()` uses a similar internal lock. The mutex is only
held during the actual I/O — the `vsnprintf()` into `message[]` happens
outside the lock so formatting time doesn't block other lcores.

### 5. `__attribute__((format(printf, 4, 5)))`
Tells GCC to type-check the format string and variadic arguments of
`log_write()` exactly like `printf`. Without this, a bug like
`LOG_INFO("count=%s", 42)` compiles silently and corrupts output.

### 6. FATAL calls abort()
```c
if (level == LOG_LEVEL_FATAL)
    abort();
```
`abort()` generates a SIGABRT which triggers a core dump (if
`ulimit -c unlimited` is set). GDB can then load the core and show
exactly which line triggered the fatal log.

---

## Log level guide

| Level | When to use |
|---|---|
| `LOG_DEBUG` | Per-packet detail, internal state. Off in production. |
| `LOG_INFO` | Normal startup progress, config values, connections established. |
| `LOG_WARN` | Recoverable issues: retry, fallback, near-limit conditions. |
| `LOG_ERROR` | Failure in one subsystem but app continues (e.g., one lcore failed). |
| `LOG_FATAL` | Unrecoverable: cannot allocate mempool, config missing. Calls `abort()`. |

---

## Next module

**Module 03 — Ring Buffer**: A fixed-size, lock-free (SPSC) ring buffer —
the manual equivalent of DPDK's `rte_ring`. Understanding it first makes
`rte_ring` immediately intuitive when you see it in Module 15.

---

## Source files

| File | Download |
|---|---|
| `logger.h` | [logger.h]({{ '/assets/code/data-plane/projects/02-logger/logger.h' | relative_url }}) |
| `logger.c` | [logger.c]({{ '/assets/code/data-plane/projects/02-logger/logger.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/02-logger/Makefile' | relative_url }}) |
