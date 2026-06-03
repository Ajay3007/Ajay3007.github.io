# Module 05 — Packet Structs
#
# Build:   make
# Run:     ./packet_parser
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11
TARGET  = packet_parser
SRC     = packet_parser.c

$(TARGET): $(SRC) packet_structs.h
	$(CC) $(CFLAGS) -o $@ $(SRC)

clean:
	rm -f $(TARGET)

.PHONY: clean
