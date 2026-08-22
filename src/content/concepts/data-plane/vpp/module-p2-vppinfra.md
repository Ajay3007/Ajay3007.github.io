---
title: "VPP P2A - vppinfra Core Library"
description: "VPP MASTERY · PHASE 2A · WEEKS 4–5 🧱 vppinfra - Core Library vec · pool · bihash · clib mem · format/unformat · ring buffers · timers src/vppinfra/ C macros pool.h bihash 8…"
domain: data-plane
track: vpp
order: 2
ownHeader: true
url: /learning/data-plane/vpp/module-p2-vppinfra/
---

<style>
.mod-header{background:linear-gradient(135deg,#0d1b2a 0%,#1e3a5c 60%,#1a7a6e 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#7ab8d8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8cce0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8e4f4}
.tab-bar{display:flex;flex-wrap:wrap;gap:0;background:#0d1b2a;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#5dd6c8;border-bottom-color:#5dd6c8}
.tab-pane{display:none}
.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.p-blue .cp-hdr{background:#e8f1f9}
.p-teal .cp-hdr{background:#e0f0ee}
.p-orange .cp-hdr{background:#faeee4}
.p-purple .cp-hdr{background:#ede8f5}
.p-green .cp-hdr{background:#e2f0e8}
.p-red .cp-hdr{background:#faeaea}
[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.tag-blue{background:#d0e8f8;color:#1a4a7c}
.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}
.tag-red{background:#f4d0d0;color:#6c1a1a}
.cb{background:#0d1b2a;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a7a6e}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c8e0d0;white-space:pre}
.cm{color:#4a7a5a}
.ck{color:#7ab8d8}
.cv{color:#f0c080}
.cs{color:#f0a060}
.ct{color:#b0e0b0}
.dpdk-box{background:#f0ecf8;border:1.5px solid #9b7bd0;border-left:4px solid #5b3a8c;border-radius:8px;padding:1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .dpdk-box{background:#1a1028;border-color:#7060a8;border-left-color:#9b7bd0}
.dpdk-box .dh{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.08em;color:#5b3a8c;margin-bottom:.5rem;text-transform:uppercase}
[data-theme=dark] .dpdk-box .dh{color:#b090e8}
.dpdk-box ul{margin:0;padding-left:1.2rem}
.dpdk-box li{font-size:.87rem;line-height:1.65;color:var(--text-color,#222);margin-bottom:.25rem}
.ins{background:#e8f5f0;border:1.5px solid #1a7a6e;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#2a9a8e}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0e5248}
[data-theme=dark] .ins strong{color:#5dd6c8}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ds-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1rem;margin:1rem 0}
.ds-card{border-radius:8px;border:1.5px solid var(--border-color,#ddd);background:var(--card-bg,#fff);overflow:hidden}
.ds-card-hdr{padding:.6rem 1rem;font-family:monospace;font-size:.82rem;font-weight:700;color:#fff;background:#1a3a5c}
.ds-card-body{padding:.8rem 1rem}
.ds-card-body p{font-size:.85rem;line-height:1.6;color:var(--text-color,#222);margin:.3rem 0}
.ds-card-body code{font-size:.8rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px}
.api-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.86rem}
.api-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.api-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.api-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.api-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a7a6e}
.proj-box{border:2px solid #c05e1b;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.proj-hdr{background:#c05e1b;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.proj-hdr .pn{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.proj-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.proj-body{padding:1.1rem 1.2rem}
.proj-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.ps{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.ps:last-of-type{border-bottom:none}
.ps .sn{background:#c05e1b;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;border-radius:6px;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
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
  <div class="mod-eyebrow">VPP MASTERY · PHASE 2A · WEEKS 4–5</div>
  <div class="mod-title">🧱 vppinfra - Core Library</div>
  <div class="mod-subtitle">vec · pool · bihash · clib_mem · format/unformat · ring buffers · timers</div>
  <div class="mod-pills">
    <span class="mod-pill">src/vppinfra/</span>
    <span class="mod-pill">C macros</span>
    <span class="mod-pill">pool.h</span>
    <span class="mod-pill">bihash_8_8.h</span>
    <span class="mod-pill">vec.h</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'ta')">Overview</button>
  <button class="tab-btn" onclick="vt(event,'tb')">vec - Dynamic Array</button>
  <button class="tab-btn" onclick="vt(event,'tc')">pool - Object Allocator</button>
  <button class="tab-btn" onclick="vt(event,'td')">bihash - Hash Table</button>
  <button class="tab-btn" onclick="vt(event,'te')">Memory &amp; Format</button>
  <button class="tab-btn" onclick="vt(event,'tf')">Checklist</button>
</div>
<!-- ── OVERVIEW ── -->
<div id="ta" class="tab-pane active">
<p class="sep">WHY VPPINFRA EXISTS</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📚</span><h3>vppinfra is VPP's Standard Library</h3><span class="tag tag-blue">FOUNDATION</span></div>
  <div class="cp-body">
    <p>vppinfra replaces the C standard library for VPP's dataplane. It provides memory management, data structures, I/O formatting, and timers that are specifically designed for the demands of high-performance packet processing: deterministic allocation, cache-line awareness, zero-copy design, and macro-heavy APIs for maximum inlining.</p>
    <p>Every plugin and node you write will use vppinfra primitives. Understanding these data structures deeply - not just their API but their memory layout - is what separates engineers who write correct VPP code from those who write fast, correct VPP code.</p>
  </div>
</div>
<div class="ds-grid">
  <div class="ds-card">
    <div class="ds-card-hdr">vec - Dynamic Array · vec.h</div>
    <div class="ds-card-body">
      <p>Heap-allocated array with a hidden header storing length and capacity. The pointer <em>points to element 0</em>, not the header - fully compatible with C array indexing. Use everywhere you'd use <code>std::vector</code> or <code>realloc</code>-based arrays.</p>
      <p><code>vec_add1</code> · <code>vec_add</code> · <code>vec_len</code> · <code>vec_free</code> · <code>vec_foreach</code></p>
    </div>
  </div>
  <div class="ds-card">
    <div class="ds-card-hdr">pool - Fixed-Size Object Allocator · pool.h</div>
    <div class="ds-card-body">
      <p>Pre-allocated array of fixed-size objects with a free-list bitmap. O(1) alloc/free. Objects are addressed by <em>index</em> - never store pointers to pool elements (pool can realloc). This is how sessions, interfaces, and FIB entries are stored.</p>
      <p><code>pool_get</code> · <code>pool_put</code> · <code>pool_elt_at_index</code> · <code>pool_foreach</code></p>
    </div>
  </div>
  <div class="ds-card">
    <div class="ds-card-hdr">bihash - Bounded-Index Hash · bihash_8_8.h</div>
    <div class="ds-card-body">
      <p>Two-level hash table with bounded worst-case lookup: a bucket array (L1) pointing to fixed-size pages (L2) of key-value pairs. Designed for concurrent read with a single writer. Used in NAT, ACL, FIB, session tables - essentially every fast-path lookup.</p>
      <p><code>BV(clib_bihash_add_del)</code> · <code>BV(clib_bihash_search)</code></p>
    </div>
  </div>
  <div class="ds-card">
    <div class="ds-card-hdr">clib_mem - Memory Management · mem.h</div>
    <div class="ds-card-body">
      <p>Wrapper around dlmalloc with NUMA awareness and heap introspection. Supports multiple heaps (main heap, per-NUMA heaps). <code>clib_mem_alloc_aligned</code> guarantees cache-line alignment. Never use <code>malloc</code>/<code>free</code> in VPP code.</p>
      <p><code>clib_mem_alloc</code> · <code>clib_mem_free</code> · <code>clib_mem_alloc_aligned</code></p>
    </div>
  </div>
  <div class="ds-card">
    <div class="ds-card-hdr">format/unformat · format.h</div>
    <div class="ds-card-body">
      <p>Extensible printf/scanf replacement. <code>format</code> returns a <code>u8 *</code> vec (not a fixed buffer). Custom format functions registered via <code>%U</code>. All VPP CLI output and packet trace use this - learn it to write readable trace functions.</p>
      <p><code>format(0, "%U", format_ip4_address, &addr)</code></p>
    </div>
  </div>
  <div class="ds-card">
    <div class="ds-card-hdr">clib_fifo / clib_ring · fifo.h</div>
    <div class="ds-card-body">
      <p>FIFO and ring-buffer primitives built on top of vec. Used for work queues, event rings, and inter-thread communication at the framework level. Power-of-2 sized for fast modulo via bitmask.</p>
      <p><code>clib_fifo_add1</code> · <code>clib_fifo_sub1</code> · <code>clib_ring_new</code></p>
    </div>
  </div>
</div>
<div class="dpdk-box">
  <div class="dh">⚙️ DPDK PARALLEL - Data Structure Mapping</div>
  <ul>
    <li><strong>vec</strong> ≈ <code>rte_malloc</code> + manual realloc tracking - but with automatic growth and a type-safe foreach macro</li>
    <li><strong>pool</strong> ≈ <code>rte_mempool</code> for fixed-size objects - but pool objects stay in-place (no dequeue/enqueue), addressed by index, not pointer. VPP sessions are stored in pools exactly like DPDK mbufs in a mempool</li>
    <li><strong>bihash</strong> ≈ a hash table you'd build over <code>rte_hash</code> - but bihash is specifically designed for read-mostly concurrent access without locking on the read path</li>
    <li><strong>clib_mem</strong> ≈ <code>rte_malloc</code> - both support NUMA-local allocation and cache-line alignment. VPP uses clib_mem everywhere; never mix with rte_malloc inside VPP</li>
  </ul>
</div>
</div>
<!-- ── VEC ── -->
<div id="tb" class="tab-pane">
<p class="sep">VEC - DYNAMIC ARRAY (src/vppinfra/vec.h)</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📐</span><h3>Memory Layout - The Hidden Header</h3><span class="tag tag-teal">INTERNALS</span></div>
  <div class="cp-body">
    <p>The key to understanding vec is its memory layout. The header lives <em>before</em> the data in memory, so the pointer you hold points directly to element[0]. This makes vec transparent to any C code expecting a plain array.</p>
<div class="cb"><pre><span class="cm">/* Memory layout of a vec_t */</span>
+──────────────────────────────────────────────────────+
|  vec_header_t   |  element[0]  |  element[1]  | ...  |
|  len   (u32)    |              |              |       |
|  dlmalloc_hdr   |              |              |       |
+──────────────────────────────────────────────────────+
                  ↑
            your pointer lives here
 
<span class="cm">/* The pointer IS the array - C-array compatible */</span>
<span class="ck">u32</span> *my_vec = 0;          <span class="cm">/* NULL == empty vec, NOT uninitialised */</span>
vec_add1(my_vec, 42);     <span class="cm">/* grows by 1, may realloc */</span>
vec_add1(my_vec, 99);
<span class="cm">/* my_vec[0] == 42, my_vec[1] == 99 - plain array access */</span>
<span class="ck">u32</span> len = vec_len(my_vec); <span class="cm">/* == 2 */</span></pre></div>
    <ul>
      <li><strong>NULL is a valid empty vec</strong> - always initialise to 0, never to an uninitialised pointer</li>
      <li><strong>Never hold pointers to vec elements</strong> - <code>vec_add1</code> may realloc, invalidating all element addresses. Hold indices instead</li>
      <li><strong>vec_free does not NULL the pointer</strong> - use <code>vec_free(v); v = 0;</code> to be safe</li>
    </ul>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🛠️</span><h3>Complete vec API Reference</h3><span class="tag tag-blue">API</span></div>
  <div class="cp-body">
<table class="api-table">
  <thead><tr><th>Function / Macro</th><th>Signature / Usage</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td><code>vec_add1(v, e)</code></td><td>Append single element <code>e</code> to vec <code>v</code></td><td>May realloc. v updated in-place (macro takes address)</td></tr>
    <tr><td><code>vec_add(v, p, n)</code></td><td>Append <code>n</code> elements from array <code>p</code></td><td>Bulk append - faster than N × vec_add1</td></tr>
    <tr><td><code>vec_add2(v, p, n)</code></td><td>Reserve space for <code>n</code> elements, return pointer to first</td><td>Use when you want to write directly into the vec</td></tr>
    <tr><td><code>vec_len(v)</code></td><td>Returns <code>u32</code> element count. Returns 0 for NULL vec</td><td>Safe to call on NULL - does not crash</td></tr>
    <tr><td><code>vec_bytes(v)</code></td><td>Returns total byte size of vec data region</td><td>vec_len(v) * sizeof(v[0])</td></tr>
    <tr><td><code>vec_free(v)</code></td><td>Free vec memory</td><td>Does NOT set v=0. Do that manually</td></tr>
    <tr><td><code>vec_reset_length(v)</code></td><td>Set length to 0 without freeing memory</td><td>Reuse allocation - faster than free+realloc</td></tr>
    <tr><td><code>vec_foreach(var,v)</code></td><td>Iterate: <code>vec_foreach(ep, entries) { ... }</code></td><td>var is a pointer to each element</td></tr>
    <tr><td><code>vec_foreach_index(i,v)</code></td><td>Iterate by index: <code>i</code> goes 0..vec_len(v)-1</td><td>When you need the index inside the loop</td></tr>
    <tr><td><code>vec_dup(v)</code></td><td>Return a copy of the vec</td><td>Heap-allocates a new vec with same content</td></tr>
    <tr><td><code>vec_validate(v, i)</code></td><td>Ensure vec is at least <code>i+1</code> elements, zero-filling new slots</td><td>Use to grow to a known index safely</td></tr>
    <tr><td><code>vec_validate_init_empty(v,i,val)</code></td><td>Like vec_validate but fills with <code>val</code> instead of 0</td><td>Useful for flag arrays initialised to ~0</td></tr>
    <tr><td><code>vec_insert(v,n,i)</code></td><td>Insert <code>n</code> zero elements at position <code>i</code></td><td>O(n) - shifts elements right</td></tr>
    <tr><td><code>vec_del1(v,i)</code></td><td>Delete element at <code>i</code>, replacing with last element</td><td>O(1) - order NOT preserved</td></tr>
    <tr><td><code>_vec_len(v)</code></td><td>Direct header field access - no NULL check</td><td>Use only when v is guaranteed non-NULL</td></tr>
    <tr><td><code>vec_set_len(v,n)</code></td><td>Force-set length field</td><td>Advanced: use after manual direct writes to vec memory</td></tr>
  </tbody>
</table>
<div class="cb"><pre><span class="cm">/* Typical plugin usage: building a list of sw_if_index values */</span>
<span class="ck">u32</span> *sw_if_indices = 0;   <span class="cm">/* NULL = empty vec */</span>
<span class="cm">/* Collect all interfaces matching a condition */</span>
pool_foreach(hw, im->hw_interfaces) {
    <span class="ck">if</span> (hw->flags & VNET_HW_INTERFACE_FLAG_LINK_UP)
        vec_add1(sw_if_indices, hw->sw_if_index);
}
 
<span class="cm">/* Process them */</span>
<span class="ck">u32</span> *si;
vec_foreach(si, sw_if_indices) {
    vnet_sw_interface_t *swif = vnet_get_sw_interface(vnm, *si);
    <span class="cm">/* ... do something with swif */</span>
}
 
<span class="cm">/* Reuse without realloc */</span>
vec_reset_length(sw_if_indices);
 
<span class="cm">/* Or free completely */</span>
vec_free(sw_if_indices);
sw_if_indices = 0;</pre></div>
  </div>
</div>
<div class="warn">
  <p>⚠️ <strong>Critical pitfall - storing pointers to vec elements:</strong> Any operation that can grow the vec (<code>vec_add1</code>, <code>vec_add</code>, <code>vec_validate</code>) <em>may call realloc</em>, which moves the entire array to a new address. Any pointer you saved to an element is now a dangling pointer. Always store the <strong>index</strong> into the vec, not a pointer to the element.</p>
</div>
</div>
<!-- ── POOL ── -->
<div id="tc" class="tab-pane">
<p class="sep">POOL - FIXED-SIZE OBJECT ALLOCATOR (src/vppinfra/pool.h)</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🏊</span><h3>Pool Memory Layout and Design</h3><span class="tag tag-teal">INTERNALS</span></div>
  <div class="cp-body">
    <p>A pool is a pre-allocated contiguous array of fixed-size objects. It maintains a free-list as a bitmap of free slots. Allocation (<code>pool_get</code>) finds the first free bit and marks it used - O(1). Free (<code>pool_put</code>) marks the slot free again - O(1). Crucially, <strong>object addresses are stable</strong> as long as the pool does not grow - the pool never moves existing elements on alloc.</p>
<div class="cb"><pre><span class="cm">/* Pool memory model */</span>
pool = [  obj[0]  |  obj[1]  |  obj[2]  |  obj[3]  | ... ]
         (in use)    (FREE)     (in use)    (FREE)
 
free_bitmap = 0b...1010   (bits set = free slots)
 
<span class="cm">/* pool_get: find lowest set bit, clear it, return pointer */</span>
<span class="cm">/* pool_put: set the bit at this index                     */</span>
<span class="cm">/* Declaration */</span>
<span class="ck">typedef struct</span> {
    <span class="ck">u32</span>  conn_id;
    <span class="ck">u32</span>  sw_if_index;
    <span class="ck">ip4_address_t</span> src, dst;
    <span class="ck">u8</span>   state;
} my_session_t;
 
my_session_t *session_pool = 0;   <span class="cm">/* NULL = empty pool */</span></pre></div>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🛠️</span><h3>Complete pool API</h3><span class="tag tag-blue">API</span></div>
  <div class="cp-body">
<table class="api-table">
  <thead><tr><th>Macro / Function</th><th>Usage</th><th>Returns / Effect</th></tr></thead>
  <tbody>
    <tr><td><code>pool_get(P, E)</code></td><td>Allocate one element from pool P, set pointer E</td><td>E points to newly allocated element (zero-filled)</td></tr>
    <tr><td><code>pool_get_aligned(P, E, align)</code></td><td>pool_get with alignment guarantee</td><td>Use for SIMD-aligned structs</td></tr>
    <tr><td><code>pool_put(P, E)</code></td><td>Return element pointed to by E back to pool</td><td>Marks slot free. E still points to valid memory until next pool_get</td></tr>
    <tr><td><code>pool_put_index(P, i)</code></td><td>Free by index rather than pointer</td><td>Equivalent to pool_put(P, pool_elt_at_index(P,i))</td></tr>
    <tr><td><code>pool_elt_at_index(P, i)</code></td><td>Return pointer to element at index i</td><td>No bounds check - undefined if i is free</td></tr>
    <tr><td><code>pool_is_free_index(P, i)</code></td><td>Return 1 if slot i is free</td><td>Always check before dereferencing by index</td></tr>
    <tr><td><code>pool_elts(P)</code></td><td>Count of currently in-use elements</td><td>Returns u32</td></tr>
    <tr><td><code>pool_len(P)</code></td><td>Capacity - total allocated slots (used + free)</td><td>Returns u32</td></tr>
    <tr><td><code>pool_foreach(E, P)</code></td><td>Iterate over all in-use elements</td><td>E is a pointer to each live element</td></tr>
    <tr><td><code>pool_foreach_index(i, P)</code></td><td>Iterate by index over all in-use elements</td><td>i is the index of each live element</td></tr>
    <tr><td><code>pool_free(P)</code></td><td>Free the entire pool memory</td><td>Frees backing store, does not set P=0</td></tr>
    <tr><td><code>pool_validate_index(P, i)</code></td><td>Assert that index i is valid (not free)</td><td>Debug helper - crashes on invalid access</td></tr>
    <tr><td><code>pool_alloc(P, n)</code></td><td>Pre-allocate pool capacity for n objects</td><td>Avoids repeated realloc during initial population</td></tr>
  </tbody>
</table>
<div class="cb"><pre><span class="cm">/* Complete example: per-flow session pool */</span>
my_session_t *sessions = 0;        <span class="cm">/* pool */</span>
<span class="ck">uword</span> *session_by_key = 0;         <span class="cm">/* hash: key → pool index */</span>
<span class="cm">/* Create a session */</span>
my_session_t *s;
pool_get_zero(sessions, s);        <span class="cm">/* allocate + zero-fill */</span>
<span class="ck">u32</span> session_index = s - sessions;  <span class="cm">/* derive index from pointer arithmetic */</span>
s->conn_id = next_conn_id++;
s->state = SESSION_STATE_INIT;
 
<span class="cm">/* Store in hash by key for fast lookup */</span>
hash_set(session_by_key, flow_key, session_index);
 
<span class="cm">/* Fast-path lookup: key → index → pointer */</span>
<span class="ck">uword</span> *val = hash_get(session_by_key, flow_key);
<span class="ck">if</span> (val) {
    s = pool_elt_at_index(sessions, *val);
    <span class="cm">/* s is now valid - use it */</span>
}
 
<span class="cm">/* Destroy a session */</span>
hash_unset(session_by_key, flow_key);
pool_put(sessions, s);            <span class="cm">/* marks slot free */</span>
<span class="cm">/* Walk all active sessions (e.g., for timeout sweep) */</span>
pool_foreach(s, sessions) {
    <span class="ck">if</span> (now - s->last_seen > SESSION_TIMEOUT)
        expire_session(sessions, session_by_key, s);
}</pre></div>
  </div>
</div>
<div class="ins">
  <p>💡 <strong>Deriving an index from a pointer:</strong> The idiom <code>index = element_ptr - pool_base_ptr</code> is idiomatic in VPP. It works because pool elements are contiguous. This index is stable even if the pool grows (existing elements don't move). Always <strong>store the index</strong> in inter-subsystem references (e.g., in a buffer's opaque field), never the pointer.</p>
</div>
</div>
<!-- ── BIHASH ── -->
<div id="td" class="tab-pane">
<p class="sep">BIHASH - BOUNDED-INDEX EXTENSIBLE HASHING (src/vppinfra/bihash_*.h)</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>Bihash Architecture - Two-Level Lookup</h3><span class="tag tag-orange">INTERNALS</span></div>
  <div class="cp-body">
    <p>Bihash is VPP's primary hash table for dataplane lookups. Its design is optimised for the read-heavy, write-rare workload of packet forwarding: millions of lookups per second with occasional control-plane insertions.</p>
<div class="cb"><pre><span class="cm">/* Two-level structure */</span>
 
Level 1 - Bucket Array (always in memory, fits in L2 cache):
  bucket[0]  → page pointer + lock bit
  bucket[1]  → page pointer + lock bit
  ...
  bucket[N-1]→ page pointer + lock bit
 
  hash(key) & (N-1) → selects bucket index
 
Level 2 - KV Pages (per-bucket, allocated on demand):
  page = [ kvp[0] | kvp[1] | kvp[2] | kvp[3] | ... ]
         (BIHASH_KVP_PER_PAGE entries, default 4 or 8)
 
Lookup:
  1. bucket_idx = hash(key) & (N-1)          O(1) - bitmask
  2. page = bucket[bucket_idx].page           O(1) - pointer deref
  3. linear scan page for matching key        O(1) - ≤8 compares</pre></div>
    <p>When a bucket fills (all KVP slots taken), it <em>overflows</em> to a chain of pages. The chain length is bounded by the load factor at init time. This gives <strong>worst-case O(chain_len)</strong> lookup - not O(n) like a chaining hash table.</p>
    <p>The lock bit in the bucket enables a <strong>single-writer, multi-reader</strong> protocol: readers spin on the lock bit; the writer sets it, modifies the page, clears it. Readers detect inconsistency via the version counter and retry.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📦</span><h3>Bihash Variants - Choosing the Right One</h3><span class="tag tag-blue">VARIANTS</span></div>
  <div class="cp-body">
    <p>Bihash is a template implemented via macros. The type name encodes <code>key_size_value_size</code> in bytes:</p>
<table class="api-table">
  <thead><tr><th>Type</th><th>Key</th><th>Value</th><th>Typical Use in VPP</th></tr></thead>
  <tbody>
    <tr><td><code>bihash_8_8</code></td><td>8 bytes (u64)</td><td>8 bytes (u64)</td><td>NAT4 simple lookup, sw_if_index tables, ARP cache</td></tr>
    <tr><td><code>bihash_16_8</code></td><td>16 bytes</td><td>8 bytes</td><td>NAT44 endpoint-dependent (src_ip+src_port+protocol+vrf)</td></tr>
    <tr><td><code>bihash_48_8</code></td><td>48 bytes</td><td>8 bytes</td><td>NAT66, IPv6 session tables, 5-tuple flow tables</td></tr>
    <tr><td><code>bihash_24_8</code></td><td>24 bytes</td><td>8 bytes</td><td>MPLS, L2 FIB with bridge domain</td></tr>
    <tr><td><code>bihash_40_8</code></td><td>40 bytes</td><td>8 bytes</td><td>VXLAN tunnel tables (src+dst+vni)</td></tr>
  </tbody>
</table>
<div class="cb"><pre><span class="cm">/* Include the specific variant you need */</span>
<span class="cs">#include "vppinfra/bihash_8_8.h"</span>
<span class="cs">#include "vppinfra/bihash_template.h"</span>  <span class="cm">/* defines BV() macro */</span>
<span class="cm">/* BV() prepends the type name: BV(clib_bihash_init) → clib_bihash_8_8_init */</span>
<span class="ck">typedef</span> clib_bihash_8_8_t my_hash_t;
 
<span class="cm">/* Key-value pair type */</span>
clib_bihash_kv_8_8_t kv;   <span class="cm">/* kv.key (u64), kv.value (u64) */</span>
<span class="cm">/* Initialise (call once, control plane) */</span>
clib_bihash_8_8_t h;
<span class="ck">u32</span> nbuckets = 64 * 1024;   <span class="cm">/* power of 2, tuned to expected entries */</span>
<span class="ck">u32</span> mem_bytes = 128 * 1024 * 1024;  <span class="cm">/* 128 MB backing store */</span>
clib_bihash_init_8_8(&h, <span class="cs">"my-flow-table"</span>, nbuckets, mem_bytes);</pre></div>
  </div>
</div>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Fast-Path Lookup and Insert Patterns</h3><span class="tag tag-teal">DATAPLANE</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* ── LOOKUP (fast path - called per packet) ── */</span>
clib_bihash_kv_8_8_t kv;
 
<span class="cm">/* Pack key: for 5-tuple flows you'd pack into 8 bytes */</span>
kv.key = ((<span class="ck">u64</span>)src_addr << 32) | dst_addr;   <span class="cm">/* example: src+dst IP */</span>
<span class="ck">if</span> (PREDICT_TRUE(
    clib_bihash_search_8_8(&h, &kv, &kv) == 0))
{
    <span class="cm">/* Hit - kv.value is the stored value (e.g. session pool index) */</span>
    <span class="ck">u32</span> session_idx = kv.value;
    my_session_t *s = pool_elt_at_index(sessions, session_idx);
    <span class="cm">/* ... process packet using s */</span>
}
<span class="ck">else</span> {
    <span class="cm">/* Miss - new flow, create session */</span>
    goto slow_path;
}
 
<span class="cm">/* ── INSERT (slow path / control plane) ── */</span>
clib_bihash_kv_8_8_t kv;
kv.key   = ((<span class="ck">u64</span>)src_addr << 32) | dst_addr;
kv.value = session_idx;                       <span class="cm">/* pool index */</span>
clib_bihash_add_del_8_8(&h, &kv, 1 <span class="cm">/* is_add */</span>);
 
<span class="cm">/* ── DELETE ── */</span>
kv.key = ((<span class="ck">u64</span>)src_addr << 32) | dst_addr;
kv.value = 0;                                 <span class="cm">/* value irrelevant for delete */</span>
clib_bihash_add_del_8_8(&h, &kv, 0 <span class="cm">/* is_add=0 means delete */</span>);</pre></div>
    <div class="dpdk-box">
      <div class="dh">⚙️ DPDK PARALLEL - rte_hash vs bihash</div>
      <ul>
        <li><strong>rte_hash</strong> uses Cuckoo hashing with SIMD key comparison - excellent for fixed-size lookups but requires explicit locking for concurrent writers</li>
        <li><strong>bihash</strong> uses a per-bucket lock bit so the <em>read path is lock-free</em> - readers never acquire a lock, they just check the version counter. This matters at 10 Mpps where lock contention would be catastrophic</li>
        <li>Both are pre-allocated with fixed backing memory. If bihash fills beyond capacity, lookups degrade (longer page chains) but do not crash - rte_hash returns -ENOSPC</li>
        <li>For your session table work: bihash_48_8 is the right choice for full 5-tuple IPv4 flows (src_ip 4B + dst_ip 4B + src_port 2B + dst_port 2B + proto 1B = 13B, padded to 48B for alignment)</li>
      </ul>
    </div>
  </div>
</div>
</div>
<!-- ── MEMORY & FORMAT ── -->
<div id="te" class="tab-pane">
<p class="sep">MEMORY, FORMAT/UNFORMAT, TIMERS</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🖨️</span><h3>format / unformat - Extensible I/O</h3><span class="tag tag-purple">FORMAT</span></div>
  <div class="cp-body">
    <p><code>format</code> is VPP's printf replacement. Instead of writing to a fixed buffer, it appends to a <code>u8 *</code> vec, growing as needed. The <code>%U</code> specifier allows any function with the right signature to be used as a format directive - this is how VPP achieves composable trace output.</p>
<div class="cb"><pre><span class="cm">/* format signature: u8 *format(u8 *s, const char *fmt, ...); */</span>
<span class="cm">/* Returns the u8-vec with formatted output appended */</span>
 
u8 *s = 0;   <span class="cm">/* start with empty vec */</span>
s = format(s, <span class="cs">"Interface %d IP: %U\n"</span>,
           sw_if_index,
           format_ip4_address, &my_addr);  <span class="cm">/* %U calls format_ip4_address */</span>
vlib_cli_output(vm, <span class="cs">"%v"</span>, s);             <span class="cm">/* %v = print u8-vec */</span>
vec_free(s);
 
<span class="cm">/* Writing your own format function */</span>
<span class="ck">static</span> u8 * format_my_flow(u8 *s, va_list *args) {
    my_flow_t *f = va_arg(*args, my_flow_t *);
    s = format(s, <span class="cs">"[%U:%d → %U:%d proto %d]"</span>,
               format_ip4_address, &f->src, f->src_port,
               format_ip4_address, &f->dst, f->dst_port,
               f->proto);
    <span class="ck">return</span> s;
}
 
<span class="cm">/* Use it anywhere */</span>
s = format(0, <span class="cs">"Flow: %U\n"</span>, format_my_flow, &my_flow);
 
<span class="cm">/* unformat - parsing */</span>
unformat_input_t input;
unformat_init_string(&input, "192.168.1.1");
ip4_address_t addr;
<span class="ck">if</span> (unformat(&input, <span class="cs">"%U"</span>, unformat_ip4_address, &addr))
    vlib_cli_output(vm, <span class="cs">"Parsed: %U\n"</span>, format_ip4_address, &addr);</pre></div>
    <ul>
      <li><code>format(0, ...)</code> allocates a new vec - caller must <code>vec_free</code> it</li>
      <li><code>format(existing_vec, ...)</code> appends to existing vec</li>
      <li><code>%v</code> - print a <code>u8 *</code> vec as a string</li>
      <li><code>%U</code> - call a custom format function</li>
      <li><strong>Every packet trace function uses format</strong> - learn this before writing your first plugin</li>
    </ul>
  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⏱️</span><h3>clib_time and Timing Primitives</h3><span class="tag tag-green">TIMERS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* High-resolution time - based on TSC (rdtsc) */</span>
clib_time_t ct;
clib_time_init(&ct);
 
f64 now = clib_time_now(&ct);        <span class="cm">/* seconds since init, f64 */</span>
u64 cycles = clib_cpu_time_now();    <span class="cm">/* raw TSC cycles */</span>
<span class="cm">/* In graph nodes: use vlib_time_now() which is pre-computed per dispatch */</span>
f64 now = vlib_time_now(vm);  <span class="cm">/* preferred in node functions */</span>
<span class="cm">/* Timer wheel (tw_timer_*.h) for protocol timeouts */</span>
<span class="cm">/* Used for TCP retransmit timers, NAT session expiry */</span>
<span class="cs">#include "vppinfra/tw_timer_2t_1w_2048sl.h"</span>
<span class="cm">/* Parameters: 2 timers/object, 1 wheel, 2048 slots */</span>
TWT(tw_timer_wheel) tw;
tw_timer_wheel_init_2t_1w_2048sl(&tw, expired_cb, 1.0, ~0);</pre></div>
    <p>For session timeouts in your Stateful Connection Tracker project (Mini-Project 7), use <code>tw_timer_*</code> - it handles expiry callbacks at O(1) per tick regardless of the number of active timers.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🧮</span><h3>clib_mem - Memory Allocation</h3><span class="tag tag-blue">MEMORY</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Always use clib_mem_*, never malloc/free in VPP code */</span>
<span class="cm">/* Basic allocation */</span>
void *p = clib_mem_alloc(size);
void *p = clib_mem_alloc_aligned(size, CLIB_CACHE_LINE_BYTES);  <span class="cm">/* 64-byte aligned */</span>
clib_mem_free(p);
 
<span class="cm">/* NUMA-aware allocation */</span>
clib_mem_set_numa_affinity(numa_node);  <span class="cm">/* set before alloc */</span>
void *p = clib_mem_alloc_aligned(size, CLIB_CACHE_LINE_BYTES);
clib_mem_set_default_numa_affinity();   <span class="cm">/* reset */</span>
<span class="cm">/* Heap introspection */</span>
clib_mem_usage_t usage;
clib_mem_get_heap_usage(clib_mem_get_heap(), &usage);
<span class="cm">/* usage.bytes_used, usage.bytes_free */</span>
<span class="cm">/* For per-worker allocations: use per-thread heaps */</span>
<span class="cm">/* vlib sets up per-thread heaps automatically */</span>
void *old_heap = clib_mem_set_heap(vm->thread_main->heap);
<span class="cm">/* allocate on worker-local heap */</span>
clib_mem_set_heap(old_heap);   <span class="cm">/* restore */</span></pre></div>
    <p><strong>CLIB_CACHE_LINE_BYTES</strong> is 64 on x86_64. Always align per-worker data structures to cache lines to avoid false sharing between worker threads - a common source of hidden performance problems in multi-threaded VPP plugins.</p>
  </div>
</div>
</div>
<!-- ── CHECKLIST ── -->
<div id="tf" class="tab-pane">
<p class="sep">P2A COMPLETION CHECKLIST</p>
<ul class="cl">
  <li>Understand vec memory layout: hidden header, pointer to element[0], NULL == empty</li>
  <li>Can write vec_add1, vec_foreach, vec_reset_length patterns from memory</li>
  <li>Know why you must never store pointers to vec elements (realloc risk)</li>
  <li>Understand pool memory model: contiguous array, bitmap free-list, stable indices</li>
  <li>Can implement the pool_get → store index → pool_elt_at_index pattern</li>
  <li>Know the difference between pool_foreach and pool_foreach_index</li>
  <li>Understand bihash two-level structure: bucket array → KV pages</li>
  <li>Can choose the right bihash variant (8_8, 16_8, 48_8) for a given key size</li>
  <li>Can implement bihash init, insert, lookup, and delete correctly</li>
  <li>Understand bihash single-writer/multi-reader protocol (lock bit + version)</li>
  <li>Can write a custom format function using the %U registration pattern</li>
  <li>Know when to use clib_mem_alloc_aligned vs plain clib_mem_alloc</li>
  <li>Can explain how timer wheels work and when to use tw_timer vs a simpler per-node sweep</li>
</ul>
<div class="ins" style="margin-top:1.2rem;">
  <p>✅ When complete: move to <strong>P2B - vlib</strong>. You now know the data structures. vlib is where you learn how those structures are used in the graph dispatcher - the engine that drives VPP.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/data-plane/vpp/module-p1-foundation/">← P1 Foundation</a>
  <a href="/learning/data-plane/vpp/vpp-roadmap/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/data-plane/vpp/module-p2-vlib/">Next: vlib →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active');}
</script>
