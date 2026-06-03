# Module 09 — Mempool + mbuf
#
# Build:   make
# Run:     sudo ./mempool_mbuf
# Clean:   make clean

PKGCONF  ?= pkg-config
CC        = gcc

DPDK_CFLAGS  := $(shell $(PKGCONF) --cflags libdpdk 2>/dev/null)
DPDK_LDFLAGS := $(shell $(PKGCONF) --libs   libdpdk 2>/dev/null)

ifeq ($(DPDK_CFLAGS),)
$(error "libdpdk not found. Is DPDK installed?")
endif

CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -march=native \
          -I../05-packet-structs \
          $(DPDK_CFLAGS)
LDFLAGS = $(DPDK_LDFLAGS)

TARGET  = mempool_mbuf
SRC     = mempool_mbuf.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $(SRC) $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
