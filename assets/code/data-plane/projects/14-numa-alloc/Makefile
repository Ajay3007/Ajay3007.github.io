# Module 14 — NUMA-aware Memory Allocation
#
# Two build targets:
#
#   make        → Part A only (pure C, NUMA topology reader, no DPDK)
#                 Run: ./numa_alloc
#
#   make dpdk   → Part A + Part B (DPDK allocation demos)
#                 Run: sudo ./numa_alloc_dpdk
#
#   make clean  → remove binaries

PKGCONF  ?= pkg-config
CC        = gcc

# ── Part A: pure C, always builds ──
CFLAGS_A  = -Wall -Wextra -O2 -g -std=c11
TARGET_A  = numa_alloc

$(TARGET_A): numa_alloc.c
	$(CC) $(CFLAGS_A) -o $@ $<

# ── Part B: DPDK, builds if libdpdk is available ──
DPDK_CFLAGS  := $(shell $(PKGCONF) --cflags libdpdk 2>/dev/null)
DPDK_LDFLAGS := $(shell $(PKGCONF) --libs   libdpdk 2>/dev/null)
TARGET_B  = numa_alloc_dpdk

dpdk: numa_alloc.c
ifneq ($(DPDK_CFLAGS),)
	$(CC) -Wall -Wextra -O2 -g -std=c11 -march=native \
	    -DWITH_DPDK $(DPDK_CFLAGS) -o $(TARGET_B) $< $(DPDK_LDFLAGS)
	@echo "Built $(TARGET_B). Run: sudo ./$(TARGET_B)"
else
	@echo "libdpdk not found via pkg-config — Part B not built."
endif

clean:
	rm -f $(TARGET_A) $(TARGET_B)

.PHONY: dpdk clean
