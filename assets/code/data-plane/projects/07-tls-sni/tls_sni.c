/**
 * tls_sni.c — Module 07: TLS SNI Extractor
 *
 * Two approaches:
 *
 *  A) Full ClientHello walker (tls_extract_sni)
 *     Walks the TLS record → handshake → ClientHello → extensions
 *     until it finds type 0x0000 (server_name). More robust, used
 *     when you want to be certain you're parsing correctly.
 *
 *  B) Hyperscan-match extractor (tls_extract_sni_from_match)
 *     Hyperscan fires a match at the SNI extension start. The callback
 *     uses fixed offsets (+7 for length, +9 for name) to extract the SNI
 *     without walking the full handshake. Faster, used in the real app.
 *
 * In the real DP application pipeline:
 *   - TCP packet with dst_port=443 arrives
 *   - Packet stored in tls_session_table (across fragmented pkts)
 *   - When enough bytes arrive, hs_scan_payload() runs
 *   - Hyperscan matches HS_PATTERN_ID_TLS=1 at the SNI extension offset
 *   - on_hs_match extracts SNI via approach (B)
 *   - SNI passed to url_policy_for_tls() for policy decision
 */

#include "tls_sni.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define TLS_RECORD_HDR_LEN    5
#define TLS_HANDSHAKE_HDR_LEN 4
#define TLS_CLIENTHELLO_VER_LEN 2
#define TLS_RANDOM_LEN       32

/* ───────────────────────────────────────────────────────────
 * tls_get_version_str
 * ─────────────────────────────────────────────────────────── */
const char *tls_get_version_str(uint16_t version)
{
    switch (version) {
    case TLS_VERSION_1_0: return "TLS 1.0";
    case TLS_VERSION_1_1: return "TLS 1.1";
    case TLS_VERSION_1_2: return "TLS 1.2";
    case TLS_VERSION_1_3: return "TLS 1.3";
    default:              return "unknown";
    }
}

/* ───────────────────────────────────────────────────────────
 * tls_extract_sni_from_match — approach (B), reimplements from domain_scan.c
 *
 * This is the exact logic from on_hs_match in the real project.
 * 'from' is the byte offset of the SNI extension type field (0x00 0x00)
 * within the TCP payload.
 *
 * Layout at 'from':
 *
 *  Offset  Size  Field
 *  ------  ----  -----
 *  from+0   2    Extension type       = 0x00 0x00 (server_name)
 *  from+2   2    Extension data len
 *  from+4   2    Server Name List len
 *  from+6   1    Server Name Type     = 0x00 (host_name)
 *  from+7   2    Server Name Length   ← read_u16_be HERE
 *  from+9   N    Server Name          ← copy from HERE
 * ─────────────────────────────────────────────────────────── */
int tls_extract_sni_from_match(const uint8_t *payload, int payload_len,
                                int from,
                                char *sni_out, int sni_out_len,
                                uint16_t *sni_len_out)
{
    /* minimum needed: from + 9 bytes + at least 1 byte of name */
    if (from + 10 > payload_len)
        return -1;

    /* sanity: verify extension type is server_name (0x0000) */
    uint16_t ext_type = read_u16_be(payload + from);
    if (ext_type != TLS_EXT_SERVER_NAME)
        return -1;

    /* read SNI length at from+7 */
    uint16_t name_len = read_u16_be(payload + from + 7);

    if (name_len == 0 || name_len >= (uint16_t)sni_out_len)
        return -1;

    if (from + 9 + name_len > payload_len)
        return -1;

    /* copy SNI name starting at from+9 */
    memcpy(sni_out, payload + from + 9, name_len);
    sni_out[name_len] = '\0';

    if (sni_len_out)
        *sni_len_out = name_len;

    return 0;
}

/* ───────────────────────────────────────────────────────────
 * tls_extract_sni — approach (A), full ClientHello walker
 *
 * Walks the full TLS record → handshake → ClientHello → extensions.
 * Finds the server_name extension (type 0x0000) and extracts the SNI.
 * ─────────────────────────────────────────────────────────── */
int tls_extract_sni(const uint8_t *payload, int payload_len,
                    tls_sni_result_t *result)
{
    int offset = 0;

    if (!payload || !result || payload_len < TLS_RECORD_HDR_LEN)
        return -1;

    memset(result, 0, sizeof(*result));

    /* ── Step 1: TLS Record Header (5 bytes) ── */
    const tls_record_hdr_t *rec = (const tls_record_hdr_t *)payload;

    if (rec->content_type != TLS_CONTENT_HANDSHAKE)
        return -1;   /* not a handshake record — could be app data */

    uint16_t rec_len = ntohs(rec->length);
    offset = TLS_RECORD_HDR_LEN;

    if (offset + rec_len > payload_len)
        return -1;   /* truncated record */

    /* ── Step 2: TLS Handshake Header (4 bytes) ── */
    if (offset + TLS_HANDSHAKE_HDR_LEN > payload_len)
        return -1;

    const tls_handshake_hdr_t *hs = (const tls_handshake_hdr_t *)(payload + offset);

    if (hs->type != TLS_HANDSHAKE_CLIENT_HELLO)
        return -1;   /* not a ClientHello */

    /*
     * Handshake length is 3 bytes (24-bit), not a standard uint32_t.
     * This is a common parsing mistake — always read 3 bytes manually.
     */
    uint32_t hs_len = ((uint32_t)hs->len[0] << 16) |
                      ((uint32_t)hs->len[1] <<  8) |
                       (uint32_t)hs->len[2];

    offset += TLS_HANDSHAKE_HDR_LEN;

    int body_start = offset;
    int body_end   = body_start + (int)hs_len;

    if (body_end > payload_len)
        return -1;

    /* ── Step 3: ClientHello body ── */

    /* client_version: 2 bytes */
    if (offset + 2 > body_end) return -1;
    result->tls_version = read_u16_be(payload + offset);
    offset += 2;

    /* random: 32 bytes */
    if (offset + TLS_RANDOM_LEN > body_end) return -1;
    offset += TLS_RANDOM_LEN;

    /* session_id: 1-byte length + data */
    if (offset + 1 > body_end) return -1;
    uint8_t session_id_len = payload[offset++];
    if (offset + session_id_len > body_end) return -1;
    offset += session_id_len;

    /* cipher_suites: 2-byte length + data */
    if (offset + 2 > body_end) return -1;
    uint16_t cs_len = read_u16_be(payload + offset);
    offset += 2;
    if (offset + cs_len > body_end) return -1;
    offset += cs_len;

    /* compression_methods: 1-byte length + data */
    if (offset + 1 > body_end) return -1;
    uint8_t comp_len = payload[offset++];
    if (offset + comp_len > body_end) return -1;
    offset += comp_len;

    /* ── Step 4: Extensions ── */
    if (offset + 2 > body_end) return -1;  /* no extensions present */

    uint16_t ext_total_len = read_u16_be(payload + offset);
    offset += 2;

    int ext_end = offset + ext_total_len;
    if (ext_end > body_end) return -1;

    /*
     * Walk each extension looking for type 0x0000 (server_name).
     * Each extension:
     *   2 bytes: type
     *   2 bytes: data length
     *   N bytes: data
     */
    while (offset + 4 <= ext_end) {
        uint16_t ext_type = read_u16_be(payload + offset);
        uint16_t ext_len  = read_u16_be(payload + offset + 2);
        offset += 4;

        if (offset + ext_len > ext_end) break;

        if (ext_type == TLS_EXT_SERVER_NAME) {
            /*
             * server_name extension data layout:
             *   2 bytes: server name list length
             *   (for each entry):
             *     1 byte:  server name type (0x00 = host_name)
             *     2 bytes: server name length
             *     N bytes: server name
             *
             * Use tls_extract_sni_from_match() which reads from
             * offset-4 (the extension type field) — i.e., 'from' = offset-4
             *
             * Or equivalently, read directly:
             */
            int sni_offset = offset;  /* start of extension data */

            if (sni_offset + 5 > ext_end) break;

            /* skip list_len (2) and name_type (1): that's from+4,+5,+6 */
            /* name_len is at sni_offset + 2 + 1 = sni_offset + 3 ... */

            /*
             * Recall from+7 in the Hyperscan approach = ext_type(2) + ext_len(2)
             * + list_len(2) + name_type(1) = 7 bytes before name_len.
             * Here we skipped the first 4 (ext_type + ext_len), so:
             * name_len is at sni_offset + 3.
             */
            if (sni_offset + 5 > ext_end) break;

            uint16_t name_len = read_u16_be(payload + sni_offset + 3);

            if (name_len == 0 || name_len >= MAX_SNI_LEN) break;
            if (sni_offset + 5 + name_len > ext_end) break;

            memcpy(result->hostname, payload + sni_offset + 5, name_len);
            result->hostname[name_len] = '\0';
            result->length    = name_len;
            result->sni_found = 1;
            return 0;
        }

        offset += ext_len;
    }

    /* ClientHello parsed successfully but no SNI extension found */
    return 0;
}

/* ═══════════════════════════════════════════════════════════
 * Sample TLS ClientHello packets
 * ═══════════════════════════════════════════════════════════ */

/*
 * TLS 1.3 ClientHello for "www.secure-corp.example"
 * Contains: server_name, supported_versions (TLS 1.3), ALPN (h2, http/1.1)
 *
 * Byte layout (hand-crafted, real-world structure):
 *
 *   [0-4]   TLS record header (5 bytes)
 *   [5-8]   Handshake header (4 bytes)
 *   [9-10]  ClientHello version (TLS 1.2 in body, as per spec)
 *   [11-42] Random (32 bytes)
 *   [43]    Session ID length = 0
 *   [44-45] Cipher suites length = 4
 *   [46-49] Cipher suites: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384
 *   [50]    Compression length = 1
 *   [51]    Compression: null
 *   [52-53] Extensions total length = 57
 *   [54-85] SNI extension (32 bytes)   ← Hyperscan matches type at offset 54
 *   [86-92] supported_versions ext (7 bytes)
 *   [93-110] ALPN extension (18 bytes)
 */
static const uint8_t sample_client_hello[] = {
    /* TLS Record Header */
    0x16,              /* content_type: Handshake */
    0x03, 0x01,        /* legacy version: TLS 1.0 (compat) */
    0x00, 0x6a,        /* record length: 106 */

    /* TLS Handshake Header */
    0x01,              /* type: ClientHello */
    0x00, 0x00, 0x66,  /* handshake body length: 102 */

    /* ClientHello body */
    0x03, 0x03,        /* client_version: TLS 1.2 (body; actual version in ext) */

    /* Random: 32 bytes */
    0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00, 0x11,
    0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99,
    0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00, 0x11,
    0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99,

    0x00,              /* session_id_len: 0 */

    0x00, 0x04,        /* cipher_suites_len: 4 */
    0x13, 0x01,        /* TLS_AES_128_GCM_SHA256 */
    0x13, 0x02,        /* TLS_AES_256_GCM_SHA384 */

    0x01,              /* compression_methods_len: 1 */
    0x00,              /* null compression */

    0x00, 0x39,        /* extensions total length: 57 */

    /* ─── Extension 1: server_name (SNI) ─── */
    0x00, 0x00,        /* type: server_name        ← Hyperscan from=54 */
    0x00, 0x1c,        /* ext data length: 28 */
    0x00, 0x1a,        /* server name list length: 26 */
    0x00,              /* server name type: host_name */
    0x00, 0x17,        /* server name length: 23   ← from+7 = 61 */
    /* server name: "www.secure-corp.example" (23 bytes) ← from+9 = 63 */
    0x77, 0x77, 0x77, 0x2e,                   /* www. */
    0x73, 0x65, 0x63, 0x75, 0x72, 0x65, 0x2d, /* secure- */
    0x63, 0x6f, 0x72, 0x70, 0x2e,             /* corp. */
    0x65, 0x78, 0x61, 0x6d, 0x70, 0x6c, 0x65, /* example */

    /* ─── Extension 2: supported_versions ─── */
    0x00, 0x2b,        /* type: supported_versions */
    0x00, 0x03,        /* ext data length: 3 */
    0x02,              /* versions list length: 2 */
    0x03, 0x04,        /* TLS 1.3 */

    /* ─── Extension 3: ALPN ─── */
    0x00, 0x10,        /* type: application_layer_protocol_negotiation */
    0x00, 0x0e,        /* ext data length: 14 */
    0x00, 0x0c,        /* ALPN list length: 12 */
    0x02,              /* protocol length: 2 */
    0x68, 0x32,        /* "h2" */
    0x08,              /* protocol length: 8 */
    0x68, 0x74, 0x74, 0x70, 0x2f, 0x31, 0x2e, 0x31, /* "http/1.1" */
};

/*
 * TLS ClientHello for a C2 domain: "malicious.c2-server.io"
 * Simulates traffic a compromised host might generate —
 * the DP application would block this after extracting the SNI.
 */
static const uint8_t sample_c2_hello[] = {
    0x16, 0x03, 0x01,
    0x00, 0x5a,        /* record length: 90 */

    0x01,
    0x00, 0x00, 0x56,  /* handshake length: 86 */

    0x03, 0x03,

    /* Random */
    0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88,
    0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00,
    0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88,
    0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff, 0x00,

    0x00,              /* session_id_len: 0 */

    0x00, 0x02,        /* cipher_suites_len: 2 */
    0xc0, 0x2b,        /* TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 */

    0x01, 0x00,        /* compression: null */

    0x00, 0x27,        /* extensions total length: 39 */

    /* SNI: "malicious.c2-server.io" = 22 bytes */
    0x00, 0x00,        /* type: server_name */
    0x00, 0x1b,        /* ext data length: 27 */
    0x00, 0x19,        /* server name list length: 25 */
    0x00,              /* host_name type */
    0x00, 0x16,        /* name length: 22 */
    0x6d, 0x61, 0x6c, 0x69, 0x63, 0x69, 0x6f, 0x75, /* maliciou */
    0x73, 0x2e, 0x63, 0x32, 0x2d,                   /* s.c2-    */
    0x73, 0x65, 0x72, 0x76, 0x65, 0x72, 0x2e,       /* server.  */
    0x69, 0x6f,                                       /* io       */

    /* supported_versions: TLS 1.2 only */
    0x00, 0x2b,
    0x00, 0x03,
    0x02,
    0x03, 0x03,        /* TLS 1.2 */
};

/* ─── Tests ──────────────────────────────────────────────── */

static void test_full_walker(void)
{
    tls_sni_result_t result;

    printf("\n--- Test 1: Full ClientHello walker ---\n");
    int ret = tls_extract_sni(sample_client_hello,
                               sizeof(sample_client_hello), &result);
    assert(ret == 0);
    assert(result.sni_found == 1);
    assert(strcmp(result.hostname, "www.secure-corp.example") == 0);

    printf("  SNI found       : \"%s\"\n", result.hostname);
    printf("  SNI length      : %u\n", result.length);
    printf("  Client version  : %s (0x%04x)\n",
           tls_get_version_str(result.tls_version), result.tls_version);
    printf("  PASS\n");
}

static void test_hyperscan_style(void)
{
    char     sni[MAX_SNI_LEN];
    uint16_t sni_len;

    printf("\n--- Test 2: Hyperscan-style extraction (from offset) ---\n");

    /*
     * Hyperscan matches the SNI extension type 0x00 0x00 at offset 54.
     * The on_hs_match callback receives:
     *   id   = HS_PATTERN_ID_TLS = 1
     *   from = 54
     * and calls tls_extract_sni_from_match(payload, len, from=54, ...)
     */
    int from = 54;  /* offset of SNI extension type in sample_client_hello */

    /* Verify the extension type is 0x0000 at this offset */
    uint16_t ext_type = read_u16_be(sample_client_hello + from);
    printf("  Extension type at offset %d: 0x%04x (server_name=%s)\n",
           from, ext_type, ext_type == TLS_EXT_SERVER_NAME ? "yes" : "no");

    printf("  from+7 (name_len) bytes: 0x%02x 0x%02x → length=%u\n",
           sample_client_hello[from + 7],
           sample_client_hello[from + 8],
           read_u16_be(sample_client_hello + from + 7));

    int ret = tls_extract_sni_from_match(sample_client_hello,
                                          sizeof(sample_client_hello),
                                          from, sni, sizeof(sni), &sni_len);
    assert(ret == 0);
    assert(strcmp(sni, "www.secure-corp.example") == 0);

    printf("  Extracted SNI   : \"%s\" (%u bytes)\n", sni, sni_len);
    printf("  PASS\n");
}

static void test_c2_domain(void)
{
    tls_sni_result_t result;

    printf("\n--- Test 3: C2 domain extraction ---\n");
    int ret = tls_extract_sni(sample_c2_hello,
                               sizeof(sample_c2_hello), &result);
    assert(ret == 0);
    assert(result.sni_found == 1);
    assert(strcmp(result.hostname, "malicious.c2-server.io") == 0);

    printf("  SNI extracted   : \"%s\"\n", result.hostname);
    printf("  TLS version     : %s\n", tls_get_version_str(result.tls_version));
    printf("  → policy lookup for \"%s\"\n", result.hostname);
    printf("  → found in malicious_domain_table → BLOCK\n");
    printf("  PASS\n");
}

static void test_not_handshake(void)
{
    printf("\n--- Test 4: non-Handshake record rejected ---\n");

    /* TLS Application Data record — encrypted, no SNI */
    uint8_t app_data[] = {
        0x17, 0x03, 0x03,  /* content_type = Application Data */
        0x00, 0x10,        /* length: 16 */
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,  /* encrypted payload */
        0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
    };

    tls_sni_result_t result;
    int ret = tls_extract_sni(app_data, sizeof(app_data), &result);
    assert(ret == -1);   /* not a handshake record */

    printf("  Application Data record correctly rejected (ret=%d)\n", ret);
    printf("  → real app: skip non-handshake records in TLS state machine\n");
    printf("  PASS\n");
}

static void test_struct_sizes(void)
{
    printf("\n--- Struct sizes ---\n");
    printf("  tls_record_hdr_t    : %zu bytes (expected 5)\n",
           sizeof(tls_record_hdr_t));
    printf("  tls_handshake_hdr_t : %zu bytes (expected 4)\n",
           sizeof(tls_handshake_hdr_t));
    assert(sizeof(tls_record_hdr_t)    == 5);
    assert(sizeof(tls_handshake_hdr_t) == 4);
    printf("  All sizes correct.\n");
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 07: TLS SNI Extractor ===\n");

    test_struct_sizes();
    test_full_walker();
    test_hyperscan_style();
    test_c2_domain();
    test_not_handshake();

    printf("\nAll tests passed.\n");

    printf("\n--- TLS SNI → policy flow in the DP application ---\n");
    printf("  1. TCP dst_port == 443 detected\n");
    printf("  2. TCP payload stored in tls_session_table\n");
    printf("  3. hs_scan_payload(payload, len, ...) called\n");
    printf("  4. Hyperscan matches HS_PATTERN_ID_TLS=1 at SNI ext offset\n");
    printf("  5. on_hs_match: sni_len = read_u16_be(payload + from + 7)\n");
    printf("  6.            memcpy(domain, payload + from + 9, sni_len)\n");
    printf("  7. url_policy_for_tls(domain, worker_info, ...)\n");
    printf("  8. Hash table exact match OR Hyperscan regex fallback\n");
    printf("  9. DROP → TCP RST injection; ALLOW → forward packet\n");

    return 0;
}
