# Module 21 — Full Pipeline
#
# Build (simulate, no deps):  make
# Run:                         ./full_pipeline
# Clean:                       make clean
#
# Production build (all deps):
#   make production  (requires DPDK + Hyperscan + rdkafka)

PKGCONF ?= pkg-config
CC       = gcc
CFLAGS   = -Wall -Wextra -O2 -g -std=c11 \
           -I../03-ring-buffer \
           -I../05-packet-structs

LDFLAGS  = -lpthread

TARGET   = full_pipeline
SRCS     = full_pipeline.c \
           ../03-ring-buffer/ring.c

$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -o $@ $(SRCS) $(LDFLAGS)

# ── Production build: all dependencies ──────────────────────
DPDK_CFLAGS  := $(shell $(PKGCONF) --cflags libdpdk    2>/dev/null)
DPDK_LDFLAGS := $(shell $(PKGCONF) --libs   libdpdk    2>/dev/null)
HS_CFLAGS    := $(shell $(PKGCONF) --cflags libhs      2>/dev/null)
HS_LDFLAGS   := $(shell $(PKGCONF) --libs   libhs      2>/dev/null)
RDK_CFLAGS   := $(shell $(PKGCONF) --cflags rdkafka    2>/dev/null)
RDK_LDFLAGS  := $(shell $(PKGCONF) --libs   rdkafka    2>/dev/null)

production:
ifneq ($(DPDK_CFLAGS),)
	$(CC) $(CFLAGS) \
	    -DWITH_DPDK -DWITH_HYPERSCAN -DWITH_KAFKA \
	    $(DPDK_CFLAGS) $(HS_CFLAGS) $(RDK_CFLAGS) \
	    -o full_pipeline_prod full_pipeline.c \
	    $(DPDK_LDFLAGS) $(HS_LDFLAGS) $(RDK_LDFLAGS) -lpthread
	@echo "Built full_pipeline_prod"
else
	@echo "DPDK not found — simulate-only build available via 'make'"
endif

clean:
	rm -f $(TARGET) full_pipeline_prod

.PHONY: production clean
