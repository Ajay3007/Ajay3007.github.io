# Module 02 — Logger
#
# Build:   make
# Run:     ./logger
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11
LDFLAGS = -lpthread
TARGET  = logger
SRC     = logger.c

$(TARGET): $(SRC) logger.h
	$(CC) $(CFLAGS) -o $@ $(SRC) $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
