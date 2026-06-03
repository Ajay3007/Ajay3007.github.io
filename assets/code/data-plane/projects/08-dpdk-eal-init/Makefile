# Module 08 — DPDK EAL Init
#
# DPDK must be installed. On RedHat/Rocky:
#   dnf install dpdk dpdk-devel
# Or built from source with meson/ninja.
#
# Build:   make
# Run:     sudo ./eal_init
#          (root needed for hugepage access / vfio-pci NIC binding)
# Clean:   make clean
#
# Troubleshooting:
#   "No hugepages available": allocate with
#     echo 512 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages
#   "EAL: No probed ethernet devices": normal if no NIC bound via vfio-pci;
#     add --vdev net_null0 to EAL args for a null device in testing.

PKGCONF  ?= pkg-config
CC        = gcc

# DPDK flags via pkg-config (works for both source-built and system DPDK)
DPDK_CFLAGS  := $(shell $(PKGCONF) --cflags libdpdk 2>/dev/null)
DPDK_LDFLAGS := $(shell $(PKGCONF) --libs   libdpdk 2>/dev/null)

ifeq ($(DPDK_CFLAGS),)
$(error "libdpdk not found via pkg-config. Is DPDK installed?")
endif

CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -march=native $(DPDK_CFLAGS)
LDFLAGS = $(DPDK_LDFLAGS)

TARGET  = eal_init
SRC     = eal_init.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $(SRC) $(LDFLAGS)

clean:
	rm -f $(TARGET)

# Show the full compile command (useful when debugging include path issues)
show-flags:
	@echo "CFLAGS  = $(CFLAGS)"
	@echo "LDFLAGS = $(LDFLAGS)"

.PHONY: clean show-flags
