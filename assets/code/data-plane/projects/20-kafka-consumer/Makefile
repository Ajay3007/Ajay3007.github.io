# Module 20 — Kafka Consumer (Policy Sync)
#
# Build:   make
# Run:     ./kafka_consumer --demo          (standalone, no Kafka)
#          ./kafka_consumer localhost:9092   (with real broker)
# Clean:   make clean

CC      = gcc
CFLAGS  = -Wall -Wextra -O2 -g -std=c11
LDFLAGS = -lrdkafka -lpthread

RDK_CFLAGS  := $(shell pkg-config --cflags rdkafka 2>/dev/null)
RDK_LDFLAGS := $(shell pkg-config --libs   rdkafka 2>/dev/null)

ifneq ($(RDK_CFLAGS),)
    CFLAGS  += $(RDK_CFLAGS)
    LDFLAGS  = $(RDK_LDFLAGS) -lpthread
endif

TARGET  = kafka_consumer
SRC     = kafka_consumer.c

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(TARGET)

.PHONY: clean
