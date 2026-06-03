# Module 18 — DNS Sinkhole
#
# Pure C — no DPDK, no Hyperscan required.
#
# Build:   make
# Run:     ./dns_sinkhole
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -I../05-packet-structs
TARGET  = dns_sinkhole
SRC     = dns_sinkhole.c

$(TARGET): $(SRC) ../05-packet-structs/packet_structs.h
	$(CC) $(CFLAGS) -o $@ $(SRC)

clean:
	rm -f $(TARGET)

.PHONY: clean
