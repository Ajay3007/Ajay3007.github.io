# Module 07 — TLS SNI Extractor
#
# Depends on packet_structs.h from Module 05.
#
# Build:   make
# Run:     ./tls_sni
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11 -I../05-packet-structs
TARGET  = tls_sni
SRC     = tls_sni.c

$(TARGET): $(SRC) tls_sni.h ../05-packet-structs/packet_structs.h
	$(CC) $(CFLAGS) -o $@ $(SRC)

clean:
	rm -f $(TARGET)

.PHONY: clean
