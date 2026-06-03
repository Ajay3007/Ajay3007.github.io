# Module 11 — Multi-lcore RX/TX Pipeline
#
# Build:   make
# Run:     sudo ./pipeline
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

TARGET  = pipeline
SRC     = pipeline.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $(SRC) $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
