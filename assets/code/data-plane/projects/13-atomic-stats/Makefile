# Module 13 — Atomic Counters + Per-lcore Stats
#
# Pure C — no DPDK required.
#
# Build:   make
# Run:     ./atomic_stats
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -march=native
LDFLAGS = -lpthread
TARGET  = atomic_stats
SRC     = atomic_stats.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $(SRC) $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
