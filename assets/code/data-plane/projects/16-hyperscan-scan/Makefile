# Module 16 — Hyperscan Scratch + Scan
#
# Build:   make
# Run:     ./hs_scan
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -march=native
LDFLAGS = -lhs -lpthread

HS_CFLAGS  := $(shell pkg-config --cflags libhs 2>/dev/null)
HS_LDFLAGS := $(shell pkg-config --libs   libhs 2>/dev/null)

ifneq ($(HS_CFLAGS),)
    CFLAGS  += $(HS_CFLAGS)
    LDFLAGS  = $(HS_LDFLAGS) -lpthread
endif

TARGET  = hs_scan
SRC     = hs_scan.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
