# Module 03 — Ring Buffer
#
# Build:   make
# Run:     ./ring
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11
LDFLAGS = -lpthread
TARGET  = ring
SRC     = ring.c

$(TARGET): $(SRC) ring.h
	$(CC) $(CFLAGS) -o $@ $(SRC) $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
