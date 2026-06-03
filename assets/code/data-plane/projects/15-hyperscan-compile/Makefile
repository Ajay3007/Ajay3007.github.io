# Module 15 — Hyperscan Pattern Compilation
#
# Requires: Hyperscan (libhs) installed.
#   RedHat/Rocky:  dnf install hyperscan hyperscan-devel
#   Ubuntu:        apt-get install libhyperscan-dev
#   From source:   https://github.com/intel/hyperscan (cmake + ninja)
#
# Build:   make
# Run:     ./hs_compile
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -march=native
LDFLAGS = -lhs
TARGET  = hs_compile
SRC     = hs_compile.c

# Check if Hyperscan is available via pkg-config
HS_CFLAGS  := $(shell pkg-config --cflags libhs 2>/dev/null)
HS_LDFLAGS := $(shell pkg-config --libs   libhs 2>/dev/null)

ifneq ($(HS_CFLAGS),)
    CFLAGS  += $(HS_CFLAGS)
    LDFLAGS  = $(HS_LDFLAGS)
endif

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(TARGET)

# Show Hyperscan version
version:
	@pkg-config --modversion libhs 2>/dev/null || echo "libhs not found via pkg-config"

.PHONY: clean version
