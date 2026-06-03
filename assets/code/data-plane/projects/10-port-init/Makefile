# Module 10 — NIC Port Init
#
# Build:   make
# Run:     sudo ./port_init
#          sudo ./port_init  (with null PMD: add --vdev net_null0 to eal_args)
# Clean:   make clean

PKGCONF  ?= pkg-config
CC        = gcc

DPDK_CFLAGS  := $(shell $(PKGCONF) --cflags libdpdk 2>/dev/null)
DPDK_LDFLAGS := $(shell $(PKGCONF) --libs   libdpdk 2>/dev/null)

ifeq ($(DPDK_CFLAGS),)
$(error "libdpdk not found. Is DPDK installed?")
endif

CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -march=native $(DPDK_CFLAGS)
LDFLAGS = $(DPDK_LDFLAGS)

TARGET  = port_init
SRC     = port_init.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $(SRC) $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
