---
title: "VPP P4 - Plugin Development"
description: "VPP MASTERY · PHASE 4 · WEEKS 14–18 🔨 Plugin Development Scaffold · Binary API (.api) · CLI · bihash classifier · Stateful tracker · Test framework VLIB REGISTER NODE .api…"
domain: data-plane
track: vpp
order: 4
ownHeader: true
url: /learning/data-plane/vpp/module-p4-plugin-dev/
---

<style>
.mod-header{background:linear-gradient(135deg,#0d1b2a 0%,#3a1a6c 60%,#5b3a8c 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c0a8e8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#d8c8f4;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ecdcff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0d1b2a;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}.tab-btn.active{color:#b090e8;border-bottom-color:#b090e8}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-green{background:#c8e8d4;color:#0e4a28}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.cb{background:#0d1b2a;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #5b3a8c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#dcd0f8;white-space:pre}
.cm{color:#6a5a80}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#e8f5f0;border:1.5px solid #1a7a6e;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#2a9a8e}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0e5248}[data-theme=dark] .ins strong{color:#5dd6c8}
.api-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.86rem}
.api-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.api-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.api-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.api-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a7a6e}
.proj-box{border:2px solid #5b3a8c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.proj-hdr{background:#5b3a8c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.proj-hdr .pn{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.proj-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.proj-body{padding:1.1rem 1.2rem}
.proj-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.ps{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.ps:last-of-type{border-bottom:none}
.ps .sn{background:#5b3a8c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a7a6e;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">VPP MASTERY · PHASE 4 · WEEKS 14–18</div>
  <div class="mod-title">🔨 Plugin Development</div>
  <div class="mod-subtitle">Scaffold · Binary API (.api) · CLI · bihash classifier · Stateful tracker · Test framework</div>
  <div class="mod-pills">
    <span class="mod-pill">VLIB_REGISTER_NODE</span>
    <span class="mod-pill">.api files</span>
    <span class="mod-pill">VLIB_CLI_COMMAND</span>
    <span class="mod-pill">vpptest</span>
    <span class="mod-pill">Projects 6 &amp; 7</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'ta')">Plugin Scaffold</button>
  <button class="tab-btn" onclick="vt(event,'tb')">Binary API (.api)</button>
  <button class="tab-btn" onclick="vt(event,'tc')">CLI Commands</button>
  <button class="tab-btn" onclick="vt(event,'td')">Classifier Plugin</button>
  <button class="tab-btn" onclick="vt(event,'te')">Stateful Tracker</button>
  <button class="tab-btn" onclick="vt(event,'tf')">Test Framework</button>
  <button class="tab-btn" onclick="vt(event,'tg')">Checklist</button>
</div>
<!-- SCAFFOLD -->
<div id="ta" class="tab-pane active">
<p class="sep">PLUGIN SCAFFOLD AND FILE LAYOUT</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>Generating and Understanding a Plugin</h3><span class="tag tag-purple">SCAFFOLD</span></div>
  <div class="cp-body">
    <p>VPP ships an Emacs/shell plugin generator that creates all boilerplate files. Always start here, then modify.</p>
<div class="cb"><pre><span class="cm"># Generate plugin scaffold</span>
cd vpp
extras/emacs/make-plugin.sh
<span class="cm"># Prompts for: plugin name (e.g. "classify")</span>
<span class="cm"># Generates: src/plugins/classify/</span>
<span class="cm"># Generated file layout:</span>
src/plugins/classify/
├── CMakeLists.txt        <span class="cm"># cmake build rules</span>
├── classify.h            <span class="cm"># main_t struct, per-worker data, extern declarations</span>
├── classify.c            <span class="cm"># plugin init, API message handlers</span>
├── node.c                <span class="cm"># the graph node function</span>
├── classify.api          <span class="cm"># binary API message definitions</span>
├── classify_all_api_h.h  <span class="cm"># generated: #include of .api.h files</span>
├── classify_msg_enum.h   <span class="cm"># generated: enum of message IDs</span>
├── setup.pg              <span class="cm"># packet generator script for testing</span>
└── test/
    └── test_classify.py  <span class="cm"># Python test using VppTestCase</span></pre></div>
    <p><strong>Key structures in classify.h:</strong></p>
<div class="cb"><pre><span class="cm">/* Plugin main struct - singleton, holds all plugin state */</span>
<span class="ck">typedef struct</span> {
    <span class="cm">/* Per-worker data - allocated as a vec, indexed by thread_index */</span>
    classify_per_worker_t *per_worker;
 
    <span class="cm">/* Global state (bihash tables, pool of rules, config) */</span>
    clib_bihash_8_8_t flow_table;
    classify_rule_t *rules;           <span class="cm">/* pool */</span>
    <span class="ck">u32</span>  rule_count;
 
    <span class="cm">/* vlib / vnet handles cached for fast access */</span>
    vlib_main_t    *vlib_main;
    vnet_main_t    *vnet_main;
} classify_main_t;
 
<span class="ck">extern</span> classify_main_t classify_main;
 
<span class="cm">/* Per-worker struct - thread-local, no locking needed */</span>
<span class="ck">typedef struct</span> {
    <span class="ck">u64</span>  n_classified;
    <span class="ck">u64</span>  n_passed;
    <span class="ck">u64</span>  n_dropped;
} classify_per_worker_t;</pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>Plugin Init and Registration</h3><span class="tag tag-teal">LIFECYCLE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Plugin registration - VPP loads this .so at startup */</span>
VLIB_PLUGIN_REGISTER () = {
    .version = VPP_BUILD_VER,
    .description = "Packet classifier plugin",
};
 
<span class="cm">/* Init function - runs once after all plugins are loaded */</span>
<span class="ck">static</span> clib_error_t *
classify_init (vlib_main_t *vm)
{
    classify_main_t *cm = &classify_main;
    cm->vlib_main  = vm;
    cm->vnet_main  = vnet_get_main();
 
    <span class="cm">/* Allocate per-worker structs */</span>
    vec_validate_init_empty(cm->per_worker,
        vlib_num_workers(), (classify_per_worker_t){0});
 
    <span class="cm">/* Init bihash - 64K buckets, 128MB backing */</span>
    clib_bihash_init_8_8(&cm->flow_table, "classify-flow",
                         64 * 1024, 128 << 20);
 
    <span class="cm">/* Register API message handlers */</span>
    classify_api_hookup(vm);
 
    <span class="ck">return</span> 0;
}
VLIB_INIT_FUNCTION (classify_init);
 
<span class="cm">/* Config function - parses startup.conf stanza if any */</span>
VLIB_CONFIG_FUNCTION (classify_config, "classify");
</pre></div>
  </div>
</div>
</div>
<!-- BINARY API -->
<div id="tb" class="tab-pane">
<p class="sep">BINARY API - .api FILES</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📡</span><h3>Defining Messages in .api Files</h3><span class="tag tag-blue">BINARY API</span></div>
  <div class="cp-body">
    <p>VPP's binary API is the programmatic control-plane interface - used by vppctl, GoVPP, vpp_papi, and any management agent. API messages are defined in <code>.api</code> files and compiled into C, Go, and Python stubs automatically.</p>
<div class="cb"><pre><span class="cm">/* classify.api - message definitions */</span>
<span class="cm">/* Option: API version */</span>
option version = "1.0.0";
import "vnet/interface_types.api";
 
<span class="cm">/* ── Add a classifier rule ── */</span>
autoreply define classify_add_rule {
    u32  client_index;
    u32  context;
    vl_api_interface_index_t sw_if_index;  <span class="cm">/* interface to apply rule on */</span>
    u32  src_ip;                            <span class="cm">/* host byte order */</span>
    u32  dst_ip;
    u16  src_port;
    u16  dst_port;
    u8   protocol;
    u8   action;                            <span class="cm">/* 0=pass, 1=drop, 2=redirect */</span>
    u32  redirect_sw_if_index;
};
 
<span class="cm">/* autoreply generates a _reply message automatically */</span>
<span class="cm">/* VPP sends: typedef classify_add_rule_reply_t { i32 retval; } */</span>
<span class="cm">/* ── Dump all rules (uses dump+details pattern) ── */</span>
define classify_rule_dump {
    u32 client_index;
    u32 context;
};
define classify_rule_details {
    u32 context;
    u32 rule_index;
    vl_api_interface_index_t sw_if_index;
    u32 src_ip;
    u32 dst_ip;
    u16 src_port;
    u16 dst_port;
    u8  protocol;
    u8  action;
    u64 packet_count;
    u64 byte_count;
};</pre></div>
    <p><strong>Implementing the handler in classify.c:</strong></p>
<div class="cb"><pre><span class="cm">/* API message handler - called from the main thread */</span>
<span class="ck">static</span> <span class="ck">void</span>
vl_api_classify_add_rule_t_handler (vl_api_classify_add_rule_t *mp)
{
    classify_main_t *cm = &classify_main;
    vl_api_classify_add_rule_reply_t *rmp;
    <span class="ck">int</span> rv = 0;
 
    <span class="cm">/* Validate input */</span>
    <span class="ck">u32</span> sw_if_index = ntohl(mp->sw_if_index);
    <span class="ck">if</span> (!vnet_sw_interface_is_valid(vnet_get_main(), sw_if_index)) {
        rv = VNET_API_ERROR_INVALID_SW_IF_INDEX;
        <span class="ck">goto</span> done;
    }
 
    <span class="cm">/* Add rule - hold a vlib barrier since we're modifying global state */</span>
    vlib_worker_thread_barrier_sync(cm->vlib_main);
    rv = classify_add_rule_internal(cm, mp);
    vlib_worker_thread_barrier_release(cm->vlib_main);
 
done:
    <span class="cm">/* Send reply */</span>
    REPLY_MACRO(VL_API_CLASSIFY_ADD_RULE_REPLY);
}
 
<span class="cm">/* Registration glue */</span>
<span class="ck">static</span> <span class="ck">void</span>
classify_api_hookup (vlib_main_t *vm)
{
<span class="cs">#define _(N,n) vl_msg_api_set_handlers(VL_API_##N, #n,</span>
<span class="cs">    vl_api_##n##_t_handler, /* ... */)</span>
    foreach_classify_api_msg;
<span class="cs">#undef _</span>
}</pre></div>
  </div>
</div>
</div>
<!-- CLI -->
<div id="tc" class="tab-pane">
<p class="sep">CLI COMMANDS - VLIB_CLI_COMMAND</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">💻</span><h3>Registering and Implementing CLI Commands</h3><span class="tag tag-green">CLI</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* ── Registration ── */</span>
VLIB_CLI_COMMAND (classify_add_rule_command, <span class="ck">static</span>) = {
    .path = <span class="cs">"classify add rule"</span>,
    .short_help = <span class="cs">"classify add rule &lt;if&gt; src &lt;ip&gt; dst &lt;ip&gt; [proto &lt;N&gt;] [drop|pass]"</span>,
    .function = classify_add_rule_command_fn,
};
 
VLIB_CLI_COMMAND (classify_show_command, <span class="ck">static</span>) = {
    .path = <span class="cs">"show classify"</span>,
    .short_help = <span class="cs">"show classify [interface &lt;if&gt;]"</span>,
    .function = classify_show_command_fn,
};
 
<span class="cm">/* ── Implementation ── */</span>
<span class="ck">static</span> clib_error_t *
classify_add_rule_command_fn (vlib_main_t *vm,
    unformat_input_t *input, vlib_cli_command_t *cmd)
{
    classify_main_t *cm = &classify_main;
    <span class="ck">u32</span> sw_if_index = ~0;
    ip4_address_t src = {0}, dst = {0};
    <span class="ck">u8</span>  protocol = 0;
    <span class="ck">int</span> drop = 0;
    clib_error_t *error = 0;
 
    <span class="cm">/* Parse arguments */</span>
    <span class="ck">while</span> (unformat_check_input(input) != UNFORMAT_END_OF_INPUT) {
        <span class="ck">if</span> (unformat(input, <span class="cs">"%U"</span>, unformat_vnet_sw_interface,
                      vnet_get_main(), &sw_if_index))
            ;
        <span class="ck">else if</span> (unformat(input, <span class="cs">"src %U"</span>, unformat_ip4_address, &src))
            ;
        <span class="ck">else if</span> (unformat(input, <span class="cs">"dst %U"</span>, unformat_ip4_address, &dst))
            ;
        <span class="ck">else if</span> (unformat(input, <span class="cs">"proto %d"</span>, &protocol))
            ;
        <span class="ck">else if</span> (unformat(input, <span class="cs">"drop"</span>))
            drop = 1;
        <span class="ck">else</span> {
            error = clib_error_return(0, <span class="cs">"Unknown argument: '%U'"</span>,
                                      format_unformat_error, input);
            <span class="ck">goto</span> done;
        }
    }
 
    <span class="ck">if</span> (sw_if_index == ~0) {
        error = clib_error_return(0, <span class="cs">"Interface required"</span>);
        <span class="ck">goto</span> done;
    }
 
    classify_add_rule_internal(cm, sw_if_index, &src, &dst, protocol, drop);
    vlib_cli_output(vm, <span class="cs">"Rule added (sw_if_index %d)\n"</span>, sw_if_index);
 
done:
    <span class="ck">return</span> error;
}
 
<span class="cm">/* ── Show command ── */</span>
<span class="ck">static</span> clib_error_t *
classify_show_command_fn (vlib_main_t *vm,
    unformat_input_t *input, vlib_cli_command_t *cmd)
{
    classify_main_t *cm = &classify_main;
    classify_rule_t *rule;
    <span class="ck">u32</span> sw_if_index = ~0;
 
    <span class="ck">if</span> (unformat(input, <span class="cs">"%U"</span>, unformat_vnet_sw_interface,
                  vnet_get_main(), &sw_if_index))
        ;
 
    <span class="cm">/* Print header */</span>
    vlib_cli_output(vm, <span class="cs">"%-5s %-16s %-16s %-6s %-6s %-10s %-10s\n"</span>,
                    <span class="cs">"ID"</span>, <span class="cs">"SRC"</span>, <span class="cs">"DST"</span>, <span class="cs">"PROTO"</span>, <span class="cs">"ACTION"</span>, <span class="cs">"PACKETS"</span>, <span class="cs">"BYTES"</span>);
 
    pool_foreach(rule, cm->rules) {
        <span class="ck">if</span> (sw_if_index != ~0 && rule->sw_if_index != sw_if_index)
            continue;
        vlib_cli_output(vm, <span class="cs">"%-5d %-16U %-16U %-6d %-6s %-10llu %-10llu\n"</span>,
                        rule - cm->rules,
                        format_ip4_address, &rule->src,
                        format_ip4_address, &rule->dst,
                        rule->protocol,
                        rule->action == CLASSIFY_ACTION_DROP ? <span class="cs">"DROP"</span> : <span class="cs">"PASS"</span>,
                        rule->n_packets, rule->n_bytes);
    }
    <span class="ck">return</span> 0;
}</pre></div>
  </div>
</div>
</div>
<!-- CLASSIFIER PLUGIN -->
<div id="td" class="tab-pane">
<p class="sep">COMPLETE CLASSIFIER NODE - BIHASH FAST PATH</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔎</span><h3>5-Tuple Classifier Node Implementation</h3><span class="tag tag-orange">PROJECT 6</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Error strings */</span>
<span class="ck">static</span> <span class="ck">char</span> *classify_error_strings[] = {
<span class="cs">#define _(n,s) s,</span>
    foreach_classify_error
<span class="cs">#undef _</span>
};
 
VLIB_REGISTER_NODE (classify_node) = {
    .name = <span class="cs">"pkt-classify"</span>,
    .vector_size = <span class="ck">sizeof</span>(u32),
    .type = VLIB_NODE_TYPE_INTERNAL,
    .n_errors = CLASSIFY_N_ERROR,
    .error_strings = classify_error_strings,
    .n_next_nodes = CLASSIFY_N_NEXT,
    .next_nodes = {
        [CLASSIFY_NEXT_DROP]   = <span class="cs">"error-drop"</span>,
        [CLASSIFY_NEXT_PASS]   = <span class="cs">"ip4-lookup"</span>,
    },
    .format_trace = format_classify_trace,
};
 
VLIB_NODE_FN (classify_node) (vlib_main_t *vm,
    vlib_node_runtime_t *node, vlib_frame_t *frame)
{
    classify_main_t *cm = &classify_main;
    <span class="ck">u32</span> thread_index = vm->thread_index;
    classify_per_worker_t *pw = &cm->per_worker[thread_index];
 
    <span class="ck">u32</span> n_left_from, *from;
    from = vlib_frame_vector_args(frame);
    n_left_from = frame->n_vectors;
 
    <span class="ck">u16</span> nexts[VLIB_FRAME_SIZE];
    <span class="ck">u16</span> *next = nexts;
 
    <span class="cm">/* Quad loop */</span>
    <span class="ck">while</span> (n_left_from >= 8) {
        vlib_buffer_t *b0, *b1, *b2, *b3;
        ip4_header_t *ip0, *ip1, *ip2, *ip3;
        clib_bihash_kv_8_8_t kv;
 
        vlib_prefetch_buffer_with_index(vm, from[4], LOAD);
        vlib_prefetch_buffer_with_index(vm, from[5], LOAD);
        vlib_prefetch_buffer_with_index(vm, from[6], LOAD);
        vlib_prefetch_buffer_with_index(vm, from[7], LOAD);
 
        vlib_get_buffers(vm, from, &b0, 4);
 
        ip0 = vlib_buffer_get_current(b0);
        ip1 = vlib_buffer_get_current(b1);
        ip2 = vlib_buffer_get_current(b2);
        ip3 = vlib_buffer_get_current(b3);
 
        <span class="cm">/* Macro: pack 5-tuple into u64 key for bihash_8_8 lookup */</span>
<span class="cs">#define CLASSIFY_KEY(ip) \</span>
        ((((u64)(ip)->src_address.as_u32) << 32) | (ip)->dst_address.as_u32)
 
        kv.key = CLASSIFY_KEY(ip0);
        next[0] = (clib_bihash_search_8_8(&cm->flow_table, &kv, &kv) == 0)
                  ? (u16)kv.value : CLASSIFY_NEXT_PASS;
 
        kv.key = CLASSIFY_KEY(ip1);
        next[1] = (clib_bihash_search_8_8(&cm->flow_table, &kv, &kv) == 0)
                  ? (u16)kv.value : CLASSIFY_NEXT_PASS;
 
        kv.key = CLASSIFY_KEY(ip2);
        next[2] = (clib_bihash_search_8_8(&cm->flow_table, &kv, &kv) == 0)
                  ? (u16)kv.value : CLASSIFY_NEXT_PASS;
 
        kv.key = CLASSIFY_KEY(ip3);
        next[3] = (clib_bihash_search_8_8(&cm->flow_table, &kv, &kv) == 0)
                  ? (u16)kv.value : CLASSIFY_NEXT_PASS;
 
        pw->n_classified += 4;
        from += 4; next += 4; n_left_from -= 4;
    }
 
    <span class="cm">/* Dual and single drain loops omitted for brevity - same pattern */</span>
 
    vlib_buffer_enqueue_to_next(vm, node,
        vlib_frame_vector_args(frame), nexts, frame->n_vectors);
    <span class="ck">return</span> frame->n_vectors;
}</pre></div>
  </div>
</div>
</div>
<!-- STATEFUL TRACKER -->
<div id="te" class="tab-pane">
<p class="sep">STATEFUL CONNECTION TRACKER - PROJECT 7</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Per-Flow State + Timeout Sweep</h3><span class="tag tag-purple">ADVANCED</span></div>
  <div class="cp-body">
    <p>A stateful tracker extends the classifier to maintain per-flow connection state (NEW, ESTABLISHED, FIN_WAIT, CLOSED), byte/packet counters per flow, and a timeout sweep to expire idle flows. This is the foundation of NAT, firewalls, and connection tracking.</p>
<div class="cb"><pre><span class="cm">/* Flow state machine */</span>
<span class="ck">typedef enum</span> {
    FLOW_STATE_NEW = 0,
    FLOW_STATE_ESTABLISHED,
    FLOW_STATE_FIN_WAIT,
    FLOW_STATE_CLOSED,
} flow_state_t;
 
<span class="cm">/* Flow entry - stored in a pool */</span>
<span class="ck">typedef struct</span> {
    <span class="cm">/* Key (also used as bihash lookup) */</span>
    ip4_address_t src, dst;
    <span class="ck">u16</span>  src_port, dst_port;
    <span class="ck">u8</span>   protocol;
 
    <span class="cm">/* State */</span>
    flow_state_t state;
    f64  last_seen;          <span class="cm">/* vlib_time_now() */</span>
    <span class="ck">u64</span>  n_packets, n_bytes;
 
    <span class="cm">/* Timer wheel handle */</span>
    <span class="ck">u32</span>  timer_handle;
} flow_entry_t;
 
<span class="cm">/* Fast path: per-packet state update */</span>
VLIB_NODE_FN(flow_track_node)(vlib_main_t *vm, ...) {
    <span class="cm">/* ... dual loop ... */</span>
    f64 now = vlib_time_now(vm);
 
    <span class="cm">/* Lookup flow */</span>
    clib_bihash_kv_16_8_t kv;
    pack_5tuple(&kv.key, ip0, tcp0);
 
    <span class="ck">if</span> (PREDICT_TRUE(clib_bihash_search_16_8(&fm->flow_table, &kv, &kv) == 0)) {
        <span class="cm">/* Existing flow */</span>
        flow_entry_t *f = pool_elt_at_index(fm->flows, kv.value);
        f->last_seen = now;
        f->n_packets++;
        f->n_bytes += b0->current_length;
 
        <span class="cm">/* State transition on TCP flags */</span>
        <span class="ck">if</span> (tcp0->flags & TCP_FLAG_FIN)
            f->state = FLOW_STATE_FIN_WAIT;
        <span class="ck">else if</span> (f->state == FLOW_STATE_NEW)
            f->state = FLOW_STATE_ESTABLISHED;
    } <span class="ck">else</span> {
        <span class="cm">/* New flow - send to slow path for allocation */</span>
        next0 = FLOW_NEXT_SLOW_PATH;
    }
}
 
<span class="cm">/* Timeout sweep - runs in a PROCESS node once per second */</span>
VLIB_NODE_FN(flow_timeout_process)(vlib_main_t *vm, ...) {
    <span class="ck">while</span> (1) {
        vlib_process_suspend(vm, 1.0);  <span class="cm">/* yield for 1 second */</span>
        f64 now = vlib_time_now(vm);
        flow_entry_t *f;
        pool_foreach(f, fm->flows) {
            <span class="ck">if</span> (now - f->last_seen > FLOW_TIMEOUT_SEC) {
                <span class="cm">/* Remove from bihash + free pool slot */</span>
                flow_delete(fm, f);
            }
        }
    }
}</pre></div>
    <div class="ins">
      <p>💡 <strong>Thread safety in the tracker:</strong> The fast path (flow lookup + counter update) runs on worker threads. The timeout sweep (pool_foreach + flow_delete) runs on the main thread. To safely delete flows from a worker-accessed bihash, use <code>vlib_worker_thread_barrier_sync</code> in the sweep, or use atomic operations / a lock-free delete queue. The barrier approach is simpler and correct for low-frequency deletions.</p>
    </div>
  </div>
</div>
</div>
<!-- TEST FRAMEWORK -->
<div id="tf" class="tab-pane">
<p class="sep">VPP TEST FRAMEWORK</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🧪</span><h3>Writing Python Tests with VppTestCase</h3><span class="tag tag-teal">TESTING</span></div>
  <div class="cp-body">
    <p>VPP's test framework (<code>test/</code>) provides <code>VppTestCase</code>, a Python unittest subclass that spins up a real VPP instance, sends packets via the packet generator or raw sockets, and makes assertions on counters and captured packets.</p>
<div class="cb"><pre><span class="cm">## test/test_classify.py</span>
from framework import VppTestCase
from scapy.layers.inet import IP, TCP, UDP, Ether
from vpp_papi import VppEnum
 
class TestClassify(VppTestCase):
    """Packet Classifier Plugin Tests"""
 
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
 
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
 
    def setUp(self):
        super().setUp()
        <span class="cm"># Create two loopback interfaces for testing</span>
        self.create_loopback_interfaces(2)
        self.lo0, self.lo1 = self.lo_interfaces
 
        for i in self.lo_interfaces:
            i.admin_up()
            i.config_ip4()
            i.resolve_arp()
 
        <span class="cm"># Enable classify feature on lo0</span>
        self.vapi.classify_enable_disable(
            sw_if_index=self.lo0.sw_if_index,
            enable=1
        )
 
    def tearDown(self):
        for i in self.lo_interfaces:
            i.unconfig_ip4()
            i.admin_down()
        super().tearDown()
 
    def test_drop_rule(self):
        """Verify DROP rule drops matching packets"""
        <span class="cm"># Add DROP rule for src 10.0.0.100 → dst 10.0.0.200</span>
        self.vapi.classify_add_rule(
            sw_if_index=self.lo0.sw_if_index,
            src_ip=socket.inet_aton("10.0.0.100"),
            dst_ip=socket.inet_aton("10.0.0.200"),
            action=1  <span class="cm"># DROP</span>
        )
 
        <span class="cm"># Craft and send matching packet</span>
        pkts = [Ether() / IP(src="10.0.0.100", dst="10.0.0.200") / TCP()]
        self.send_and_assert_no_replies(self.lo0, pkts)
 
        <span class="cm"># Verify drop counter incremented</span>
        stats = self.vapi.classify_stats_get()
        self.assertEqual(stats.n_dropped, 1)
 
    def test_pass_rule(self):
        """Verify non-matching packets pass through"""
        pkts = [Ether() / IP(src="10.0.1.1", dst="10.0.1.2") / UDP()]
        self.send_and_expect(self.lo0, pkts, self.lo1)</pre></div>
    <p>Run your test: <code>make test TEST=test_classify</code></p>
  </div>
</div>
</div>
<!-- CHECKLIST -->
<div id="tg" class="tab-pane">
<p class="sep">P4 COMPLETION CHECKLIST</p>
<ul class="cl">
  <li>Can generate a plugin scaffold and explain the purpose of each generated file</li>
  <li>Can write classify_main_t, classify_per_worker_t correctly - global vs per-worker data</li>
  <li>Know the VLIB_PLUGIN_REGISTER + VLIB_INIT_FUNCTION lifecycle</li>
  <li>Understand how to use vlib_worker_thread_barrier_sync when modifying global state from API handlers</li>
  <li>Can write a complete .api file with autoreply define and dump/details pair</li>
  <li>Can implement an API message handler: parse, validate, REPLY_MACRO</li>
  <li>Can write VLIB_CLI_COMMAND with unformat_input_t parsing and vlib_cli_output printing</li>
  <li>Can implement a bihash-based classifier node using the dual-loop pattern</li>
  <li>Understand the stateful tracker design: pool for flow entries, bihash for fast lookup, PROCESS node for timeout sweep</li>
  <li>Can write a VppTestCase Python test: setUp with loopbacks, send_and_assert_no_replies, counter assertions</li>
  <li>Know how to run a specific test: make test TEST=test_mytest</li>
  <li>Completed Project 6 (bihash classifier) and Project 7 (stateful tracker)</li>
</ul>
<div class="ins" style="margin-top:1.2rem;">
  <p>✅ Phase 4 complete. You can now build production VPP plugins end-to-end. Move to <strong>Phase 5 - Control Plane &amp; GoVPP</strong> to learn how to drive VPP programmatically from Go.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/data-plane/vpp/module-p3-tap-afxdp/">← TAP · AF_XDP</a>
  <a href="/learning/data-plane/vpp/vpp-roadmap/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/data-plane/vpp/module-p5-controlplane/">Next: Control Plane →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active');}
</script>
