# Module 17 — Two-tier Policy Lookup
#
# Requires Hyperscan. No DPDK needed.
#
# Build:   make
# Run:     ./policy_lookup
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -march=native
LDFLAGS = -lhs

HS_CFLAGS  := $(shell pkg-config --cflags libhs 2>/dev/null)
HS_LDFLAGS := $(shell pkg-config --libs   libhs 2>/dev/null)

ifneq ($(HS_CFLAGS),)
    CFLAGS  += $(HS_CFLAGS)
    LDFLAGS  = $(HS_LDFLAGS)
endif

TARGET  = policy_lookup
SRC     = policy_lookup.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
