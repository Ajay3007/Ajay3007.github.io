# Module 06 — DNS Parser
#
# Depends on packet_structs.h from Module 05.
# Copy it here or adjust the include path.
#
# Build:   make
# Run:     ./dns_parser
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -I../05-packet-structs
TARGET  = dns_parser
SRC     = dns_parser.c

$(TARGET): $(SRC) dns_parser.h ../05-packet-structs/packet_structs.h
	$(CC) $(CFLAGS) -o $@ $(SRC)

clean:
	rm -f $(TARGET)

.PHONY: clean
