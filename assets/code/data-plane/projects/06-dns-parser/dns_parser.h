/**
 * dns_parser.h — Module 06: DNS Parser
 *
 * A complete DNS message parser covering query and response parsing,
 * DNS over UDP, and DNS over TCP.
 *
 * In the real DP project (pkt_proc.h), four functions handle
 * DNS parsing depending on transport and IP version:
 *
 *   parse_dns_ipv4_request_packet_over_udp()
 *   parse_dns_ipv6_request_packet_over_udp()
 *   parse_dns_ipv4_request_packet_over_tcp()
 *   parse_dns_ipv6_request_packet_over_tcp()
 *
 * Each of these extracts the query domain name and type (A or AAAA),
 * then calls url_policy_for_dns() which runs the
 * hash table lookup + Hyperscan policy scan.
 *
 * The qtype (A vs AAAA) matters for the DNS sinkhole response (Module 23):
 * - A query blocked  → inject answer with walled-garden IPv4
 * - AAAA query blocked → inject answer with walled-garden IPv6
 *
 * DNS over TCP note:
 *   RFC 1035 §4.2.2: DNS messages over TCP are prefixed with a 2-byte
 *   big-endian length field. The real app reads this length first, then
 *   reads exactly that many bytes as the DNS message.
 *
 *   +--------+--------+---------- - - -----------+
 *   |  length (2B)    |   DNS message             |
 *   +--------+--------+---------- - - -----------+
 */

#ifndef DNS_PARSER_H
#define DNS_PARSER_H

#include <stdint.h>
#include <stddef.h>
#include "packet_structs.h"

/* ───────────────────────────────────────────────────────────
 * Limits
 * ─────────────────────────────────────────────────────────── */
#define MAX_DNS_NAME_LEN   256    /* RFC 1035: max 253 usable + nul */
#define MAX_DNS_ANSWERS     16    /* max answers we bother parsing   */
#define DNS_TCP_LEN_PREFIX   2    /* 2-byte length prefix for TCP    */

/* ───────────────────────────────────────────────────────────
 * dns_answer_t — one parsed resource record from the answer section
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    char     name[MAX_DNS_NAME_LEN];
    uint16_t type;               /* DNS_TYPE_A, DNS_TYPE_AAAA, DNS_TYPE_CNAME */
    uint16_t cls;
    uint32_t ttl;
    uint16_t rdlength;
    uint8_t  rdata[16];          /* raw rdata (4 bytes for A, 16 for AAAA)    */
    char     cname[MAX_DNS_NAME_LEN]; /* decoded name if type == CNAME        */
} dns_answer_t;

/* ───────────────────────────────────────────────────────────
 * dns_message_t — a fully parsed DNS message
 *
 * This is the struct that the policy engine works with.
 * In the real app, the equivalent state is passed as function
 * arguments (qname, qtype, id) rather than a single struct,
 * but the data is identical.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    /* --- Header fields --- */
    uint16_t id;
    int      is_response;       /* 0 = query, 1 = response     */
    int      recursion_desired; /* RD bit set by client        */
    int      recursion_avail;   /* RA bit set by server        */
    int      authoritative;     /* AA bit                      */
    uint16_t rcode;             /* 0=OK, 3=NXDOMAIN, 5=REFUSED */
    uint16_t qdcount;
    uint16_t ancount;

    /* --- Parsed question section --- */
    char     qname[MAX_DNS_NAME_LEN];   /* domain name, dot-separated */
    uint16_t qtype;                     /* DNS_TYPE_A or DNS_TYPE_AAAA */
    uint16_t qclass;

    /*
     * question_wire_end: byte offset in the raw DNS message where the
     * question section ends. Used by Module 23 (DNS sinkhole) to know
     * where to append the injected answer section.
     */
    int      question_wire_end;

    /* --- Parsed answer section (filled for responses) --- */
    dns_answer_t answers[MAX_DNS_ANSWERS];
    int          num_answers;
} dns_message_t;

/* ─── Public API ─────────────────────────────────────────── */

/**
 * dns_parse_message — parse a DNS message from raw bytes.
 *
 * @wire     : pointer to start of DNS message (after UDP header,
 *             or after the 2-byte TCP length prefix)
 * @wire_len : length of the DNS message in bytes
 * @msg      : output struct to fill
 *
 * Returns 0 on success, -1 on malformed message.
 *
 * In the real app, this is called as part of:
 *   parse_dns_ipv4_request_packet_over_udp(mbuf, worker_info, ...)
 * which first locates the UDP payload pointer, then parses the DNS.
 */
int dns_parse_message(const uint8_t *wire, int wire_len, dns_message_t *msg);

/**
 * dns_parse_qname — decode a DNS wire-format label-encoded name.
 *
 * Handles pointer compression (RFC 1035 §4.1.4).
 *
 * @wire      : start of the full DNS message (needed for pointer resolution)
 * @wire_len  : length of the full DNS message
 * @offset    : byte offset within wire where the name starts
 * @out       : output buffer for the decoded dot-separated name
 * @out_len   : size of output buffer
 *
 * Returns number of bytes consumed at offset (not counting pointer jumps),
 * or -1 on error.
 */
int dns_parse_qname(const uint8_t *wire, int wire_len,
                    int offset, char *out, int out_len);

/**
 * dns_normalize_name — lowercase a domain name in place.
 *
 * DNS names are case-insensitive. The real app normalises to lowercase
 * before hash table lookup and Hyperscan scanning to ensure
 * "Google.COM" matches the same policy as "google.com".
 */
void dns_normalize_name(char *name);

/**
 * dns_dump — pretty-print a parsed dns_message_t.
 */
void dns_dump(const dns_message_t *msg);

/* Convenience: type/rcode number to human-readable string */
const char *dns_type_str(uint16_t type);
const char *dns_rcode_str(uint16_t rcode);

#endif /* DNS_PARSER_H */
