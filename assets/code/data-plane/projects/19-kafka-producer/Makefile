# Module 19 — Kafka Producer (CDR Export)
#
# Requires: librdkafka
#   RedHat/Rocky:  dnf install librdkafka librdkafka-devel
#   Ubuntu:        apt-get install librdkafka-dev
#   From source:   https://github.com/confluentinc/librdkafka
#
# Build:   make
# Run:     ./kafka_producer [broker] [topic]
#          ./kafka_producer localhost:9092 dp_cdr
#
# Test broker (Docker):
#   docker run -p 9092:9092 apache/kafka:3.7.0
#
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11
LDFLAGS = -lrdkafka -lpthread

# Try pkg-config first, fall back to system paths
RDK_CFLAGS  := $(shell pkg-config --cflags rdkafka 2>/dev/null)
RDK_LDFLAGS := $(shell pkg-config --libs   rdkafka 2>/dev/null)

ifneq ($(RDK_CFLAGS),)
    CFLAGS  += $(RDK_CFLAGS)
    LDFLAGS  = $(RDK_LDFLAGS) -lpthread
endif

TARGET  = kafka_producer
SRC     = kafka_producer.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
