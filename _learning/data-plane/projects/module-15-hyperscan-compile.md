---
layout: learning
title: "Module 15 — Hyperscan: Pattern Compilation"
permalink: /learning/data-plane/projects/module-15-hyperscan-compile/
---

# Module 15 — Hyperscan: Pattern Compilation

> Requires **Hyperscan (libhs)** installed. See setup instructions below.

## What you learn

How to compile Hyperscan pattern databases — both regex (`hs_compile_multi`)
and literal (`hs_compile_lit_multi`) — including the exact `parseFlags()`,
`parseFile()`, and `hs_create_db()` implementations from `domain_scan.c`
in the DP application. Also covers DB info query, serialization for persistence, and
compile error handling.

---

## Hyperscan's role in the DP application

```text
Two databases, two purposes:

1. domainsPatternDB (global, regex):
   Compiled once at startup from patterns.txt + patterns2.txt.
   Patterns match the structure of TLS ClientHello (SNI extension header),
   HTTP Host headers, and IP addresses in URLs.
   IDs: TLS=1, HTTP_IPV4=2, HTTP_DOMAIN=3, HTTP_IPV6=4

2. group->database (per-group, literal):
   Compiled once per enterprise group when policy syncs from Kafka.
   Contains exact domain names: "google.com", "malware.ru", etc.
   Used as the Hyperscan fallback when rte_hash exact lookup misses.
```

---

## Setup

```bash
# RedHat 8 / Rocky Linux 8
dnf install hyperscan hyperscan-devel

# Ubuntu 22.04+
apt-get install libhyperscan-dev

# From source (latest version):
git clone https://github.com/intel/hyperscan
cd hyperscan && mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
ninja && sudo ninja install
```

---

## Build and run

```bash
make
./hs_compile
```

---

## Files

| File | Purpose |
|---|---|
| `hs_compile.c` | `parseFlags`, `parseFile`, `hs_create_db`, 6 demos |
| `sample_patterns.txt` | Example patterns.txt in the real format (ID:/pattern/flags) |
| `Makefile` | Links with `-lhs` (pkg-config aware) |

---

## Key concepts

### 1. `hs_compile_multi` vs `hs_compile_lit_multi`

```c
/* REGEX mode — for patterns.txt (TLS/HTTP patterns) */
hs_compile_multi(
    patterns,    /* char *[] of regex strings */
    flags,       /* unsigned[] of HS_FLAG_* per pattern */
    ids,         /* unsigned[] of IDs per pattern */
    count,
    HS_MODE_BLOCK,
    NULL,        /* platform: NULL = current CPU */
    &db, &err
);

/* LITERAL mode — for domain policy (no regex engine) */
hs_compile_lit_multi(
    patterns,          /* char *[] of byte strings */
    flags,
    ids,
    lens,              /* size_t[] — length of each literal */
    count,
    HS_MODE_BLOCK,
    NULL,
    &db, &err
);
```

**When to use literal:** domain names are exact strings, not patterns.
Literal mode is significantly faster to compile AND scan because Hyperscan
uses SIMD byte-comparison algorithms instead of building a full NFA/DFA.
For 10000 domain literals, literal compile takes ~50ms vs ~2s for regex.

### 2. `HS_FLAG_SINGLEMATCH` — the most important performance flag

```c
flags[i] = HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH;
```

Without `SINGLEMATCH`: Hyperscan fires a match callback for **every**
position in the data where the pattern matches.

With `SINGLEMATCH`: Hyperscan fires exactly **once** per scan per pattern.
Since the DP application only needs to know IF a pattern matched, `SINGLEMATCH`
eliminates redundant callbacks and is always used.

### 3. Pattern IDs — the callback dispatch mechanism

```c
/* In the on_hs_match callback (domain_scan.c): */
int on_hs_match(unsigned int id, unsigned long long from,
              unsigned long long to, unsigned int flags, void *ctx)
{
    switch (id) {
    case HS_PATTERN_ID_TLS:         /* 4 */
        /* read SNI at from+7 / from+9 (Module 07 pattern) */
        break;
    case HS_PATTERN_ID_HTTP_DOMAIN: /* 3 */
        /* extract Host: header domain */
        break;
    }
    return 0;  /* 0 = continue scanning, non-zero = stop */
}
```

### 4. `parseFile` — pattern file format

```text
# Comment
ID:/regex_or_literal/flags

Example:
4:/\x00\x00\x00\x00\x00/H
6:/Host: [a-zA-Z0-9._-]+/iH
```

### 5. Serialization for fast restart

```c
/* After compilation — save to disk: */
size_t sz;
hs_serialized_database_size(db, &sz);
char *buf = malloc(sz);
hs_serialize_database(db, buf, sz);
fwrite(buf, 1, sz, fp);

/* On restart — load instead of recompile: */
fread(buf, 1, sz, fp);
hs_deserialize_database(buf, sz, &db);
```

For the global DB with 100+ patterns, compilation takes ~500ms.
With serialization, restart takes ~5ms (just a memory copy).

### 6. Compile error handling

```c
hs_compile_error_t *err = NULL;
hs_error_t r = hs_compile_multi(..., &db, &err);

if (r != HS_SUCCESS) {
    if (err) {
        LOG_ERROR("Pattern %d failed: %s", err->expression, err->message);
        hs_free_compile_error(err);  /* MANDATORY: free the error struct */
    }
    return -1;
}
```

### 7. `HS_MODE_BLOCK` — always use this in the DP application

```text
HS_MODE_BLOCK:    Scan a complete buffer at once.
                  Most efficient for fixed-size packet payloads.

HS_MODE_STREAM:   Data arrives in chunks (e.g., TCP stream reassembly).
                  Would be needed if scanning fragmented DNS over TCP.

HS_MODE_VECTORED: Scan multiple non-contiguous buffers in one call.
                  Not used in the DP application.
```

---

## Next module

**Module 16 — Hyperscan: Scratch + Scan**: Allocate scratch space
(`hs_alloc_scratch`), clone per-lcore scratch (`hs_clone_scratch`), and
call `hs_scan()` with the `onMatch` callback.

---

## Source files

| File | Download |
|---|---|
| `hs_compile.c` | [hs_compile.c](https://github.com/Ajay3007/dataplane-learning/blob/main/15-hyperscan-compile/hs_compile.c){:target="_blank" rel="noopener noreferrer"} |
| `sample_patterns.txt` | [sample_patterns.txt](https://github.com/Ajay3007/dataplane-learning/blob/main/15-hyperscan-compile/sample_patterns.txt){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/15-hyperscan-compile/Makefile){:target="_blank" rel="noopener noreferrer"} |
