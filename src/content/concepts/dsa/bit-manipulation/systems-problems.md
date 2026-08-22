---
title: "Bit Manipulation — Systems Problems"
description: "DSA MASTERY · CH 11 · BIT MANIPULATION · CHAPTER 9 & 9881;& 65039; Systems Bit Manipulation Problems Fully-worked problems from real systems engineering — IPv4 · Subnets ·…"
domain: dsa
order: 99
ownHeader: true
url: /learning/dsa/bit-manipulation/systems-problems/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0c29 0%,#1a1060 55%,#24243e 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#a78bfa;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c4b5fd;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(167,139,250,.15);border:1px solid rgba(167,139,250,.3);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ddd6fe}
.p-violet{background:#f5f3ff;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-blue{background:#eaf2fc;border-left:4px solid #2e6da4;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-teal{background:#e8f6f4;border-left:4px solid #0f766e;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-orange{background:#fff7ed;border-left:4px solid #ea580c;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-slate{background:#f4f6f8;border-left:4px solid #64748b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-violet h4,.p-blue h4,.p-teal h4,.p-orange h4,.p-slate h4{margin:0 0 .5rem;font-size:.9rem;font-weight:700}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3;white-space:pre-wrap}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
.badge{display:inline-block;font-size:.7rem;font-family:monospace;font-weight:700;padding:2px 8px;border-radius:4px;margin-left:.5rem;vertical-align:middle}
.easy{background:#d1fae5;color:#065f46}.medium{background:#fef3c7;color:#92400e}.hard{background:#fee2e2;color:#991b1b}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a1060;color:#fff !important;border-color:#1a1060}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">DSA MASTERY · CH 11 · BIT MANIPULATION · CHAPTER 9</div>
  <div class="mod-title">&#9881;&#65039; Systems Bit Manipulation Problems</div>
  <div class="mod-subtitle">Fully-worked problems from real systems engineering — IPv4 · Subnets · Packet Headers · MAC · Memory Alignment</div>
  <div class="mod-pills">
<span class="mod-pill">IPv4 Encoding</span>
<span class="mod-pill">Subnet / CIDR</span>
<span class="mod-pill">VLAN / TCP / DSCP</span>
<span class="mod-pill">MAC Address</span>
<span class="mod-pill">Aligned Allocator</span>
<span class="mod-pill">Ring Buffer</span>
  </div>
</div>
<div style="background:#1a1060;border-radius:0 0 8px 8px;padding:.7rem 1.5rem;color:#a78bfa;font-size:.82rem;font-family:monospace;margin-bottom:2rem;">
  Each problem: bit layout &rarr; approach &rarr; complete C code &rarr; dry run &rarr; edge cases
</div>
<p class="sep">PROBLEM SET 1 &mdash; IPv4 ENCODING &amp; DECODING</p>
<div class="p-blue">
<h4>P1.1 &mdash; <code>ipv4_to_uint32(char* ip)</code> <span class="badge medium">Medium</span></h4>
Convert <code>"192.168.10.5"</code> into a single <code>uint32_t</code> without library functions.
</div>
<div class="diagram-box">IPv4 "192.168.10.5" layout:
Bit: 31..24  23..16  15..8   7..0
     [ 192 ][ 168  ][  10  ][  5  ]
result = (192&lt;&lt;24)|(168&lt;&lt;16)|(10&lt;&lt;8)|5 = 0xC0A80A05</div>
<div class="cb"><span class="co">uint32_t</span> <span class="cf">ipv4_to_uint32</span>(<span class="ck">const</span> <span class="ck">char</span>* ip) {
<span class="co">uint32_t</span> result = <span class="cn">0</span>;
<span class="ck">int</span> octet = <span class="cn">0</span>, shift = <span class="cn">24</span>;
<span class="ck">while</span> (*ip) {
<span class="ck">if</span> (*ip == <span class="cs">'.'</span>) { result |= (<span class="co">uint32_t</span>)octet &lt;&lt; shift; shift -= <span class="cn">8</span>; octet = <span class="cn">0</span>; }
<span class="ck">else</span> { octet = octet * <span class="cn">10</span> + (*ip - <span class="cs">'0'</span>); }
        ip++;
    }
<span class="ck">return</span> result | (<span class="co">uint32_t</span>)octet;
}

<span class="ck">void</span> <span class="cf">uint32_to_ipv4</span>(<span class="co">uint32_t</span> ip, <span class="ck">char</span>* buf) {
<span class="cf">sprintf</span>(buf, <span class="cs">"%u.%u.%u.%u"</span>,
        (ip &gt;&gt; <span class="cn">24</span>) &amp; <span class="cn">0xFF</span>, (ip &gt;&gt; <span class="cn">16</span>) &amp; <span class="cn">0xFF</span>,
        (ip &gt;&gt;  <span class="cn">8</span>) &amp; <span class="cn">0xFF</span>,  ip &amp; <span class="cn">0xFF</span>);
}</div>
<p class="sep">PROBLEM SET 2 &mdash; SUBNET &amp; CIDR OPERATIONS</p>
<div class="p-teal">
<h4>P2.1 &mdash; <code>isValidIP(char* ip, char* netId, int prefix)</code> <span class="badge hard">Hard</span></h4>
Does IP belong to the given subnet? E.g. <code>isValidIP("192.168.10.5","192.168.10.0",28)</code> &rarr; true.
</div>
<div class="diagram-box">192.168.10.5 &amp; mask(/28=0xFFFFFFF0) = 0xC0A80A00
192.168.10.0 &amp; mask(/28=0xFFFFFFF0) = 0xC0A80A00  &rarr; match &#10003;</div>
<div class="cb"><span class="ck">bool</span> <span class="cf">isValidIP</span>(<span class="ck">char</span>* ip, <span class="ck">char</span>* netId, <span class="ck">int</span> prefix) {
<span class="co">uint32_t</span> a = <span class="cf">ipv4_to_uint32</span>(ip),  b = <span class="cf">ipv4_to_uint32</span>(netId);
<span class="co">uint32_t</span> mask = (prefix == <span class="cn">0</span>) ? <span class="cn">0</span> : ~((<span class="cn">1U</span> &lt;&lt; (<span class="cn">32</span>-prefix)) - <span class="cn">1</span>);
<span class="ck">return</span> (a &amp; mask) == (b &amp; mask);
}

<span class="co">uint32_t</span> <span class="cf">networkAddr</span> (<span class="co">uint32_t</span> ip, <span class="ck">int</span> p) { <span class="ck">return</span> ip &amp; ~((<span class="cn">1U</span>&lt;&lt;(<span class="cn">32</span>-p))-<span class="cn">1</span>); }
<span class="co">uint32_t</span> <span class="cf">broadcastAddr</span>(<span class="co">uint32_t</span> ip, <span class="ck">int</span> p) { <span class="ck">return</span> <span class="cf">networkAddr</span>(ip,p) | ((<span class="cn">1U</span>&lt;&lt;(<span class="cn">32</span>-p))-<span class="cn">1</span>); }
<span class="co">uint32_t</span> <span class="cf">hostCount</span>    (<span class="ck">int</span> p)           { <span class="ck">return</span> (<span class="cn">1U</span> &lt;&lt; (<span class="cn">32</span>-p)) - <span class="cn">2</span>; }</div>
<p class="sep">PROBLEM SET 3 &mdash; PACKET HEADER FIELD EXTRACTION</p>
<div class="p-violet">
<h4>P3.1 &mdash; Parse VLAN 802.1Q Tag <span class="badge medium">Medium</span></h4>
Extract PCP (3-bit), DEI (1-bit), VID (12-bit) from a 16-bit tag.
</div>
<div class="cb"><span class="co">uint16_t</span> tag = <span class="cf">ntohs</span>(raw);
<span class="co">uint8_t</span>  pcp = (tag &gt;&gt; <span class="cn">13</span>) &amp; <span class="cn">0x07</span>;
<span class="co">uint8_t</span>  dei = (tag &gt;&gt; <span class="cn">12</span>) &amp; <span class="cn">0x01</span>;
<span class="co">uint16_t</span> vid = tag &amp; <span class="cn">0x0FFF</span>;
<span class="cm">// Rebuild: htons((pcp&lt;&lt;13)|(dei&lt;&lt;12)|(vid&amp;0xFFF))</span></div>
<div class="p-violet">
<h4>P3.2 &mdash; Extract DSCP and ECN from IPv4 TOS byte <span class="badge easy">Easy</span></h4>
</div>
<div class="diagram-box">TOS byte:  [DSCP: 6 bits][ECN: 2 bits]
DSCP = (tos &gt;&gt; 2) &amp; 0x3F
ECN  =  tos &amp; 0x03</div>
<div class="cb"><span class="co">uint8_t</span> dscp = (tos &gt;&gt; <span class="cn">2</span>) &amp; <span class="cn">0x3F</span>;
<span class="co">uint8_t</span> ecn  = tos &amp; <span class="cn">0x03</span>;
<span class="cm">// Rebuild: tos = (dscp &lt;&lt; 2) | (ecn &amp; 3)</span></div>
<div class="p-violet">
<h4>P3.3 &mdash; Inspect TCP Flags <span class="badge medium">Medium</span></h4>
</div>
<div class="cb"><span class="cv">#define TCP_FIN 0x01</span>
<span class="cv">#define TCP_SYN 0x02</span>
<span class="cv">#define TCP_RST 0x04</span>
<span class="cv">#define TCP_PSH 0x08</span>
<span class="cv">#define TCP_ACK 0x10</span>
<span class="ck">const</span> <span class="ck">char</span>* <span class="cf">tcpState</span>(<span class="co">uint8_t</span> f) {
<span class="ck">if</span> ((f &amp; <span class="cn">0x12</span>) == <span class="cn">0x02</span>) <span class="ck">return</span> <span class="cs">"SYN"</span>;
<span class="ck">if</span> ((f &amp; <span class="cn">0x12</span>) == <span class="cn">0x12</span>) <span class="ck">return</span> <span class="cs">"SYN+ACK"</span>;
<span class="ck">if</span>  (f &amp; <span class="cn">0x04</span>)            <span class="ck">return</span> <span class="cs">"RST"</span>;
<span class="ck">if</span>  (f &amp; <span class="cn">0x01</span>)            <span class="ck">return</span> <span class="cs">"FIN"</span>;
<span class="ck">return</span> <span class="cs">"ACK/data"</span>;
}</div>
<p class="sep">PROBLEM SET 4 &mdash; MAC ADDRESS OPERATIONS</p>
<div class="p-orange">
<h4>P4.1 &mdash; mac_to_uint64 / uint64_to_mac <span class="badge medium">Medium</span></h4>
Pack/unpack 6-byte MAC into uint64_t. Detect multicast, broadcast, extract OUI.
</div>
<div class="diagram-box">AA:BB:CC:DD:EE:FF &rarr; 0x0000AABBCCDDEEFF
I/G bit (bit 0 of byte[0]) = 1 means multicast
Broadcast = 0x0000FFFFFFFFFFFFULL</div>
<div class="cb"><span class="co">uint64_t</span> <span class="cf">mac_to_uint64</span>(<span class="ck">const</span> <span class="co">uint8_t</span> m[<span class="cn">6</span>]) {
<span class="co">uint64_t</span> r=<span class="cn">0</span>; <span class="ck">for</span>(<span class="ck">int</span> i=<span class="cn">0</span>;i&lt;<span class="cn">6</span>;i++) r=(r&lt;&lt;<span class="cn">8</span>)|m[i]; <span class="ck">return</span> r; }
<span class="ck">void</span> <span class="cf">uint64_to_mac</span>(<span class="co">uint64_t</span> v, <span class="co">uint8_t</span> m[<span class="cn">6</span>]) {
<span class="ck">for</span>(<span class="ck">int</span> i=<span class="cn">5</span>;i&gt;=<span class="cn">0</span>;i--){m[i]=v&amp;<span class="cn">0xFF</span>;v&gt;&gt;=<span class="cn">8</span>;} }
<span class="ck">bool</span> <span class="cf">isMulticast</span>(<span class="ck">const</span> <span class="co">uint8_t</span> m[<span class="cn">6</span>]) { <span class="ck">return</span> (m[<span class="cn">0</span>]&amp;<span class="cn">1</span>)!=<span class="cn">0</span>; }
<span class="co">uint32_t</span> <span class="cf">getOUI</span>(<span class="ck">const</span> <span class="co">uint8_t</span> m[<span class="cn">6</span>]) {
<span class="ck">return</span> ((<span class="co">uint32_t</span>)m[<span class="cn">0</span>]&lt;&lt;<span class="cn">16</span>)|((<span class="co">uint32_t</span>)m[<span class="cn">1</span>]&lt;&lt;<span class="cn">8</span>)|m[<span class="cn">2</span>]; }</div>
<p class="sep">PROBLEM SET 5 &mdash; GENERAL &amp; INTERVIEW PROBLEMS</p>
<div class="p-slate">
<h4>P5.1 &mdash; Binary Palindrome <span class="badge medium">Medium</span> &nbsp; P5.2 &mdash; Generate All Subsets <span class="badge medium">Medium</span></h4>
</div>
<div class="cb"><span class="cm">// P5.1: Is 32-bit integer a binary palindrome?</span>
<span class="ck">bool</span> <span class="cf">isBinPalindrome</span>(<span class="co">uint32_t</span> x) {
<span class="co">uint32_t</span> r=x;
    r=((r&amp;<span class="cn">0xFFFF0000</span>)&gt;&gt;<span class="cn">16</span>)|((r&amp;<span class="cn">0x0000FFFF</span>)&lt;&lt;<span class="cn">16</span>);
    r=((r&amp;<span class="cn">0xFF00FF00</span>)&gt;&gt; <span class="cn">8</span>)|((r&amp;<span class="cn">0x00FF00FF</span>)&lt;&lt; <span class="cn">8</span>);
    r=((r&amp;<span class="cn">0xF0F0F0F0</span>)&gt;&gt; <span class="cn">4</span>)|((r&amp;<span class="cn">0x0F0F0F0F</span>)&lt;&lt; <span class="cn">4</span>);
    r=((r&amp;<span class="cn">0xCCCCCCCC</span>)&gt;&gt; <span class="cn">2</span>)|((r&amp;<span class="cn">0x33333333</span>)&lt;&lt; <span class="cn">2</span>);
    r=((r&amp;<span class="cn">0xAAAAAAAA</span>)&gt;&gt; <span class="cn">1</span>)|((r&amp;<span class="cn">0x55555555</span>)&lt;&lt; <span class="cn">1</span>);
<span class="ck">return</span> x==r;
}

<span class="cm">// P5.2: All subsets using bitmask enumeration</span>
<span class="ck">void</span> <span class="cf">allSubsets</span>(<span class="ck">int</span>* a, <span class="ck">int</span> n) {
<span class="ck">for</span>(<span class="ck">int</span> mask=<span class="cn">0</span>; mask&lt;(<span class="cn">1</span>&lt;&lt;n); mask++) {
<span class="ck">for</span>(<span class="ck">int</span> i=<span class="cn">0</span>; i&lt;n; i++) <span class="ck">if</span>(mask&amp;(<span class="cn">1</span>&lt;&lt;i)) <span class="cf">printf</span>(<span class="cs">"%d "</span>,a[i]);
<span class="cf">printf</span>(<span class="cs">"\n"</span>);
    }
}</div>
<div class="p-slate">
<h4>P5.3 &mdash; Count Subarrays with XOR = k <span class="badge hard">Hard</span></h4>
Key insight: <code>XOR(i..j) = prefixXOR[j] ^ prefixXOR[i-1]</code>. Use prefix XOR + hash map.
</div>
<div class="cb"><span class="ck">int</span> <span class="cf">countXOR</span>(<span class="ck">int</span>* nums, <span class="ck">int</span> n, <span class="ck">int</span> k) {
<span class="ck">int</span> freq[<span class="cn">1024</span>]={<span class="cn">0</span>}; freq[<span class="cn">0</span>]=<span class="cn">1</span>;
<span class="ck">int</span> pre=<span class="cn">0</span>, cnt=<span class="cn">0</span>;
<span class="ck">for</span>(<span class="ck">int</span> i=<span class="cn">0</span>;i&lt;n;i++) { pre^=nums[i]; cnt+=freq[pre^k]; freq[pre]++; }
<span class="ck">return</span> cnt;
}</div>
<p class="sep">PROBLEM SET 6 &mdash; MEMORY ALIGNMENT &amp; ALLOCATOR TRICKS</p>
<div class="p-blue">
<h4>P6.1 &mdash; Aligned Memory Allocator <span class="badge hard">Hard</span></h4>
Over-allocate, adjust pointer forward to alignment boundary, store original pointer just before user block.
</div>
<div class="diagram-box">Strategy: malloc extra bytes &rarr; find aligned addr &rarr; store orig ptr before it
aligned_malloc(100, 64): raw=malloc(172) &rarr; aligned=alignUp(raw+8,64) &rarr; store raw &rarr; return aligned
aligned_free(ptr): raw = ((void**)ptr)[-1]; free(raw);</div>
<div class="cb"><span class="ck">void</span>* <span class="cf">aligned_malloc</span>(<span class="ck">size_t</span> sz, <span class="ck">size_t</span> al) {
<span class="ck">if</span>(!al||(al&amp;(al-<span class="cn">1</span>))) <span class="ck">return</span> <span class="cn">NULL</span>;
<span class="ck">void</span>* raw = <span class="cf">malloc</span>(sz + al + <span class="ck">sizeof</span>(<span class="ck">void</span>*));
<span class="ck">if</span>(!raw) <span class="ck">return</span> <span class="cn">NULL</span>;
<span class="co">uintptr_t</span> adj = (<span class="co">uintptr_t</span>)raw + <span class="ck">sizeof</span>(<span class="ck">void</span>*);
<span class="co">uintptr_t</span> aln = (adj + al - <span class="cn">1</span>) &amp; ~(al - <span class="cn">1</span>);
    ((<span class="ck">void</span>**)aln)[-<span class="cn">1</span>] = raw;
<span class="ck">return</span> (<span class="ck">void</span>*)aln;
}
<span class="ck">void</span> <span class="cf">aligned_free</span>(<span class="ck">void</span>* p) { <span class="ck">if</span>(p) <span class="cf">free</span>(((<span class="ck">void</span>**)p)[-<span class="cn">1</span>]); }</div>
<div class="p-blue">
<h4>P6.2 &mdash; Ring Buffer with Power-of-2 Sizing <span class="badge medium">Medium</span></h4>
Use <code>(idx+1) &amp; mask</code> instead of <code>% size</code> for index wrapping &mdash; valid only when size is power of 2.
</div>
<div class="cb"><span class="ck">typedef</span> <span class="ck">struct</span> { <span class="co">uint32_t</span>* data; <span class="co">uint32_t</span> mask,head,tail; } ring_t;

<span class="ck">bool</span> <span class="cf">push</span>(ring_t* r, <span class="co">uint32_t</span> v) {
<span class="co">uint32_t</span> n=(r-&gt;head+<span class="cn">1</span>)&amp;r-&gt;mask;
<span class="ck">if</span>(n==r-&gt;tail) <span class="ck">return</span> <span class="cn">false</span>;
    r-&gt;data[r-&gt;head]=v; r-&gt;head=n; <span class="ck">return</span> <span class="cn">true</span>;
}
<span class="ck">bool</span> <span class="cf">pop</span>(ring_t* r, <span class="co">uint32_t</span>* v) {
<span class="ck">if</span>(r-&gt;head==r-&gt;tail) <span class="ck">return</span> <span class="cn">false</span>;
    *v=r-&gt;data[r-&gt;tail]; r-&gt;tail=(r-&gt;tail+<span class="cn">1</span>)&amp;r-&gt;mask; <span class="ck">return</span> <span class="cn">true</span>;
}
<span class="cm">// DPDK rte_ring uses exactly this pattern.</span></div>
<div class="mod-nav">
  <a href="/learning/dsa/bit-manipulation/">&#8592; Bit Manipulation</a>
  <a href="/learning/dsa/bit-manipulation/debugging/">&#128027; Debugging Guide</a>
  <a class="nb" href="/learning/dsa/bit-manipulation/bit-manipulation-problems/">Practice Problems &#8594;</a>
</div>
