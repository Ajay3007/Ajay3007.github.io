/**
 * tls_sni.h — Module 07: TLS SNI Extractor
 *
 * For HTTPS traffic, the DP application cannot decrypt the payload. However, the
 * TLS ClientHello — sent in plaintext at the start of every TLS connection —
 * contains the Server Name Indication (SNI) extension. The SNI tells the
 * server which hostname the client wants, and it is the only L7 signal
 * available for policy enforcement on HTTPS.
 *
 * In the real the DP application project:
 *   1. Hyperscan scans the TCP payload with HS_PATTERN_ID_TLS = 1
 *      (a pattern that matches the TLS SNI extension header bytes)
 *   2. The on_hs_match callback fires with a 'from' offset pointing to the
 *      start of the server_name extension (type 0x0000)
 *   3. The callback reads the SNI name length at from+7 and copies
 *      the name starting at from+9
 *
 * This module implements:
 *   a) A full TLS ClientHello walker (no Hyperscan, pure C)
 *   b) The Hyperscan-style extractor (given 'from', extract SNI)
 *      — mirrors exactly what on_hs_match does in domain_scan.c
 *
 * TLS 1.2 and TLS 1.3 both carry the SNI in the ClientHello extensions
 * before encryption begins, so this technique works for both.
 */

#ifndef TLS_SNI_H
#define TLS_SNI_H

#include <stdint.h>
#include "packet_structs.h"    /* for read_u16_be, read_u32_be */

/* ───────────────────────────────────────────────────────────
 * TLS Content Types
 * Defined as an enum in pkt_proc.h in the real project.
 * ─────────────────────────────────────────────────────────── */
typedef enum {
    TLS_CONTENT_CHANGE_CIPHER = 0x14,
    TLS_CONTENT_ALERT         = 0x15,
    TLS_CONTENT_HANDSHAKE     = 0x16,   /* ClientHello lives here */
    TLS_CONTENT_APP_DATA      = 0x17,   /* encrypted after handshake */
} tls_content_type_t;

/* ───────────────────────────────────────────────────────────
 * TLS Handshake Types
 * ─────────────────────────────────────────────────────────── */
#define TLS_HANDSHAKE_CLIENT_HELLO  0x01
#define TLS_HANDSHAKE_SERVER_HELLO  0x02
#define TLS_HANDSHAKE_CERTIFICATE   0x0B
#define TLS_HANDSHAKE_SERVER_DONE   0x0E
#define TLS_HANDSHAKE_FINISHED      0x14

/* ───────────────────────────────────────────────────────────
 * TLS Version values
 * ─────────────────────────────────────────────────────────── */
#define TLS_VERSION_1_0  0x0301
#define TLS_VERSION_1_1  0x0302
#define TLS_VERSION_1_2  0x0303
#define TLS_VERSION_1_3  0x0304

/* ───────────────────────────────────────────────────────────
 * TLS Extension Types (relevant ones)
 * ─────────────────────────────────────────────────────────── */
#define TLS_EXT_SERVER_NAME         0x0000   /* SNI — what we extract */
#define TLS_EXT_ALPN                0x0010   /* protocol: h2, http/1.1 */
#define TLS_EXT_SUPPORTED_VERSIONS  0x002B   /* TLS 1.3 negotiation */
#define TLS_EXT_EC_POINT_FORMATS    0x000B
#define TLS_EXT_ELLIPTIC_CURVES     0x000A
#define TLS_EXT_SESSION_TICKET      0x0023

/* ───────────────────────────────────────────────────────────
 * TLS Record Header — 5 bytes
 *
 * Every TLS message on the wire starts with this.
 * The ClientHello is in a Handshake record (content_type = 0x16).
 *
 * Note: version in the record layer is often TLS 1.0 (0x0301)
 * even for TLS 1.2/1.3 connections — for compatibility reasons.
 * The true negotiated version is in the supported_versions extension.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint8_t  content_type;   /* tls_content_type_t */
    uint16_t legacy_version; /* big-endian; usually 0x0301 regardless of TLS ver */
    uint16_t length;         /* big-endian; length of payload following this header */
} __attribute__((packed)) tls_record_hdr_t;

/* ───────────────────────────────────────────────────────────
 * TLS Handshake Header — 4 bytes
 *
 * Follows the TLS record header for Handshake records.
 * The length field is 24 bits (3 bytes), NOT 32 bits.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint8_t type;       /* TLS_HANDSHAKE_CLIENT_HELLO = 0x01 */
    uint8_t len[3];     /* 24-bit big-endian length of the handshake body */
} __attribute__((packed)) tls_handshake_hdr_t;

/* ───────────────────────────────────────────────────────────
 * SNI extraction result
 * ─────────────────────────────────────────────────────────── */
#define MAX_SNI_LEN  256

typedef struct {
    char     hostname[MAX_SNI_LEN];  /* extracted SNI, null-terminated */
    uint16_t length;                 /* SNI length without null terminator */
    uint16_t tls_version;            /* TLS version from ClientHello body */
    int      sni_found;              /* 1 if SNI extension was present */
} tls_sni_result_t;

/* ─── Public API ─────────────────────────────────────────── */

/**
 * tls_extract_sni — walk a TLS ClientHello and extract the SNI.
 *
 * @payload     : pointer to TCP payload (starts at TLS record header)
 * @payload_len : number of bytes available
 * @result      : output struct
 *
 * Returns 0 if a valid ClientHello was found (SNI may still be absent
 * if the client didn't send one). Returns -1 if not a ClientHello.
 *
 * In the real app this is called from pkt_proc.h after detecting
 * that the TCP packet's payload begins with a TLS Handshake record.
 * The Hyperscan approach (below) is faster but requires a prior scan.
 */
int tls_extract_sni(const uint8_t *payload, int payload_len,
                    tls_sni_result_t *result);

/**
 * tls_extract_sni_from_match — extract SNI given a Hyperscan match offset.
 *
 * In the real the DP application project, Hyperscan fires on_hs_match with:
 *   id   = HS_PATTERN_ID_TLS (1)
 *   from = byte offset of the server_name extension type (0x00 0x00)
 *
 * The SNI layout starting at 'from':
 *   from+0  from+1 : extension type  = 0x00 0x00
 *   from+2  from+3 : extension length
 *   from+4  from+5 : server name list length
 *   from+6         : server name type = 0x00 (host_name)
 *   from+7  from+8 : SERVER NAME LENGTH   ← read_u16_be(payload + from + 7)
 *   from+9  ...    : SERVER NAME BYTES    ← payload + from + 9
 *
 * This function mirrors the exact logic in domain_scan.c on_hs_match.
 */
int tls_extract_sni_from_match(const uint8_t *payload, int payload_len,
                                int from,
                                char *sni_out, int sni_out_len,
                                uint16_t *sni_len_out);

/**
 * tls_get_version_str — version number to human-readable string.
 */
const char *tls_get_version_str(uint16_t version);

#endif /* TLS_SNI_H */
