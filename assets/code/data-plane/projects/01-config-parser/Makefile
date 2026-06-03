# Module 01 — Config Parser
#
# Build:   make
# Run:     ./config_parser
#          ./config_parser /path/to/other.conf
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11
TARGET  = config_parser
SRC     = config_parser.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(TARGET)

.PHONY: clean
