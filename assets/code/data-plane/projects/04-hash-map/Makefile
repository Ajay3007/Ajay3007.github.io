# Module 04 — Hash Map
#
# Build:   make
# Run:     ./hashmap
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11
TARGET  = hashmap
SRC     = hashmap.c

$(TARGET): $(SRC) hashmap.h
	$(CC) $(CFLAGS) -o $@ $(SRC)

clean:
	rm -f $(TARGET)

.PHONY: clean
