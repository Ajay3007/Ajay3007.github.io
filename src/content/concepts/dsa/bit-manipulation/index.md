---
title: "Bit Manipulation — First-Principles Deep Dive"
description: "DSA MASTERY · CH 11 · BIT MANIPULATION & 9881;& 65039; Bit Manipulation Masking Binary representation · 6 operators · masking patterns · classic tricks · interview problems ·…"
domain: dsa
order: 0
url: /learning/dsa/bit-manipulation/
---

<style>
.mod-header{background:linear-gradient(135deg,#0f0c29 0%,#1a1060 55%,#24243e 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#a78bfa;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c4b5fd;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(167,139,250,.15);border:1px solid rgba(167,139,250,.3);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ddd6fe}
.tab-bar{display:flex;flex-wrap:wrap;gap:0;background:#1a1060;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#a78bfa;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#c4b5fd;border-bottom-color:#c4b5fd}
.tab-pane{display:none}
.tab-pane.active{display:block}
.p-violet{background:#f5f3ff;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-blue{background:#eaf2fc;border-left:4px solid #2e6da4;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-teal{background:#e8f6f4;border-left:4px solid #0f766e;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-slate{background:#f4f6f8;border-left:4px solid #64748b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-orange{background:#fff7ed;border-left:4px solid #ea580c;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
[data-theme=dark] .p-violet{background:#1a0d30;border-color:#9d6bf0}
[data-theme=dark] .p-blue{background:#0d1e34;border-color:#4a90d9}
[data-theme=dark] .p-teal{background:#0d2020;border-color:#2a9a8e}
[data-theme=dark] .p-slate{background:#1a1e24;border-color:#8898aa}
[data-theme=dark] .p-orange{background:#1e0d00;border-color:#e07830}
.p-violet h4,.p-blue h4,.p-teal h4,.p-slate h4,.p-orange h4{margin:0 0 .5rem;font-size:.9rem;font-weight:700}
.ins{background:#e8f5e9;border:1px solid #66bb6a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
[data-theme=dark] .ins{background:#0d2010;border-color:#388e3c}
[data-theme=dark] .warn{background:#1e1800;border-color:#f9a825}
[data-theme=dark] .note{background:#0d1e2e;border-color:#1976d2}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3;white-space:pre-wrap}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}.cb .cg{color:#3fb950}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#1a1060;color:#a78bfa;font-family:monospace;font-size:.75rem;font-weight:700;padding:.5rem .7rem;text-align:left;border-bottom:2px solid #2d1b80}
.t-table td{padding:.45rem .7rem;border-bottom:1px solid var(--border-color,#e8e8e8);vertical-align:top;font-family:monospace;font-size:.83rem}
.t-table tr:last-child td{border-bottom:none}
.t-table tr:hover td{background:var(--bg-color,#f8f9fa)}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:.8rem 0}
@media(max-width:640px){.two-col{grid-template-columns:1fr}}
.pattern-card{background:var(--card-bg,#fff);border:1.5px solid #7c3aed;border-radius:8px;padding:.8rem 1rem;margin:.5rem 0}
.pattern-card h4{margin:0 0 .4rem;font-size:.88rem;color:#6d28d9}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.3rem 0;font-size:.87rem;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐ ";font-size:1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a1060;color:#fff !important;border-color:#1a1060}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">DSA MASTERY · CH 11 · BIT MANIPULATION</div>
  <div class="mod-title">&#9881;&#65039; Bit Manipulation &amp; Masking</div>
  <div class="mod-subtitle">Binary representation · 6 operators · masking patterns · classic tricks · interview problems · systems flags</div>
  <div class="mod-pills">
    <span class="mod-pill">Binary / Two's Complement</span>
    <span class="mod-pill">AND · OR · XOR · NOT · Shifts</span>
    <span class="mod-pill">Masking · Bitfields</span>
    <span class="mod-pill">FAANG Patterns</span>
    <span class="mod-pill">C / Java / C++</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t-binary')">Binary &amp; Number Repr</button>
  <button class="tab-btn" onclick="vt(event,'t-ops')">6 Operators</button>
  <button class="tab-btn" onclick="vt(event,'t-mask')">Bit Masking</button>
  <button class="tab-btn" onclick="vt(event,'t-tricks')">Classic Tricks</button>
  <button class="tab-btn" onclick="vt(event,'t-range')">Ranges &amp; Bitfields</button>
  <button class="tab-btn" onclick="vt(event,'t-systems')">Systems &amp; Flags</button>
  <button class="tab-btn" onclick="vt(event,'t-patterns')">Interview Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t-ref')">Quick Reference</button>
  <button class="tab-btn" onclick="vt(event,'t-arith')">Arithmetic &amp; Memory</button>
  <button class="tab-btn" onclick="vt(event,'t-advanced')">Advanced</button>
</div>

<!-- TAB: Binary & Number Repr -->
<div id="t-binary" class="tab-pane active">

<p class="sep">WHAT IS A BIT?</p>

<div class="p-violet">
<h4>Memory Layout — Value 45 in 8 bits</h4>
Each bit position <em>n</em> carries weight 2<sup>n</sup>. Bit 0 = LSB (Least Significant Bit). Bit 7 = MSB (Most Significant Bit).
</div>

<div class="diagram-box">Bit position:  7    6    5    4    3    2    1    0
               ┌────┬────┬────┬────┬────┬────┬────┬────┐
Value = 45:    │ 0  │ 0  │ 1  │ 0  │ 1  │ 1  │ 0  │ 1  │
               └────┴────┴────┴────┴────┴────┴────┴────┘
Bit weight:    128   64   32   16    8    4    2    1

Value = 0×128 + 0×64 + 1×32 + 0×16 + 1×8 + 1×4 + 0×2 + 1×1 = 45</div>

<p class="sep">DATA SIZES</p>

<table class="t-table">
<thead><tr><th>C Type</th><th>Java Type</th><th>Size</th><th>Bit Width</th><th>Unsigned Range</th></tr></thead>
<tbody>
<tr><td><code>uint8_t</code></td><td><code>byte</code></td><td>1 byte</td><td>8 bits</td><td>0 – 255</td></tr>
<tr><td><code>uint16_t</code></td><td><code>short</code></td><td>2 bytes</td><td>16 bits</td><td>0 – 65,535</td></tr>
<tr><td><code>uint32_t</code></td><td><code>int</code></td><td>4 bytes</td><td>32 bits</td><td>0 – 4,294,967,295</td></tr>
<tr><td><code>uint64_t</code></td><td><code>long</code></td><td>8 bytes</td><td>64 bits</td><td>0 – 18,446,744,073,709,551,615</td></tr>
</tbody>
</table>

<p class="sep">TWO'S COMPLEMENT — SIGNED INTEGERS</p>

<div class="p-teal">
<h4>Why Two's Complement?</h4>
Negate a number by flipping all bits then adding 1. This means addition hardware works <em>identically</em> for positive and negative numbers — no special case needed. The MSB is the <strong>sign bit</strong>: 0 = positive, 1 = negative. Range for N-bit signed: −2<sup>N−1</sup> to 2<sup>N−1</sup>−1.
</div>

<div class="diagram-box">Represent -45 in 8-bit two's complement:

Step 1 — Start with +45:   0 0 1 0 1 1 0 1
Step 2 — Flip all bits:    1 1 0 1 0 0 1 0
Step 3 — Add 1:            1 1 0 1 0 0 1 1   ← -45 = 0xD3

Verify: 128+64+16+2+1 = 211.  211 - 256 = -45 ✓</div>

<p class="sep">HEX ↔ BINARY QUICK REFERENCE</p>

<div class="two-col">
<div class="diagram-box">Hex │ Binary    Hex │ Binary
────┼────────   ────┼────────
 0  │ 0000       8  │ 1000
 1  │ 0001       9  │ 1001
 2  │ 0010       A  │ 1010
 3  │ 0011       B  │ 1011
 4  │ 0100       C  │ 1100
 5  │ 0101       D  │ 1101
 6  │ 0110       E  │ 1110
 7  │ 0111       F  │ 1111</div>
<div>
<div class="p-slate">
<h4>Conversion Examples</h4>
<code>0xB5</code> = <code>1011 0101</code> = 181<br><br>
<code>0xDEAD</code> = <code>1101 1110 1010 1101</code><br><br>
<strong>Java:</strong> use <code>L</code> suffix for long literals: <code>0xFFFFFFFFL</code><br><br>
<strong>C:</strong> always use <code>0x</code> prefix — <code>0xFFFF</code> is 65535.
</div>
</div>
</div>

<p class="sep">INTEGER PROMOTION RULES (C)</p>

<div class="p-orange">
<h4>Silent widening — the source of many bitmasking bugs</h4>
When you use a value smaller than <code>int</code> in a bitwise expression, C <em>automatically promotes it to <code>int</code></em> before the operation. Bitwise NOT on a <code>uint8_t</code> produces a 32-bit result — not an 8-bit one.
</div>

<div class="diagram-box">uint8_t x = 0x01;
uint8_t result = ~x;   // Danger: C promotes to int first!

// Step 1 — x promoted to int:   0x00000001
// Step 2 — ~(0x00000001)      = 0xFFFFFFFE  (32-bit result)
// Step 3 — truncated to u8    = 0xFE        (OK by accident here)

// In a mask expression this silently bleeds through:
uint8_t mask = 0x0F;
if (~mask & 0xFF00FF00) { }  // ~mask = 0xFFFFFFF0 — upper bits live!

// Safe fix: cast explicitly back
uint8_t safe = (uint8_t)(~x);  // Forces back to 8 bits</div>

<table class="t-table">
<thead><tr><th>Expression</th><th>What C actually does</th><th>Safe?</th></tr></thead>
<tbody>
<tr><td><code>~(uint8_t)x</code></td><td>Promote to int, flip 32 bits → 0xFFFFFFFE</td><td>⚠️ Depends on use</td></tr>
<tr><td><code>(uint8_t)(~x)</code></td><td>Same, but truncates result → 0xFE</td><td>✅ Safe</td></tr>
<tr><td><code>1 &lt;&lt; 31</code></td><td>Signed int shift — UB if overflow</td><td>❌ UB! Use <code>1U &lt;&lt; 31</code></td></tr>
<tr><td><code>1ULL &lt;&lt; 40</code></td><td>64-bit unsigned shift — safe</td><td>✅ Safe</td></tr>
</tbody>
</table>

<p class="sep">ENDIANNESS — NETWORK CODE GOTCHA</p>

<div class="p-blue">
<h4>Big-Endian vs Little-Endian</h4>
<strong>Little-endian</strong> (x86, ARM default): LSB stored at lowest address.<br>
<strong>Big-endian</strong> (network byte order): MSB stored at lowest address.<br><br>
Network protocols always use <strong>big-endian</strong>. Masking a multi-byte field without calling <code>ntohs()</code>/<code>ntohl()</code> first will produce wrong results on x86.
</div>

<div class="diagram-box">Value 0x1234 in memory:

Little-endian (x86):  [0x34][0x12]  ← LSB at lower address
Big-endian (network): [0x12][0x34]  ← MSB at lower address

Reading IPv4 total_length on x86 without conversion:
  uint16_t len = *(uint16_t*)ptr;  // gives 0x3412 instead of 0x1234!

Correct:
  uint16_t len = ntohs(*(uint16_t*)ptr);  // always right</div>

<div class="cb"><span class="cm">// Rule: convert BEFORE masking, convert back AFTER building</span>
<span class="co">uint16_t</span> raw   = *(<span class="co">uint16_t</span>*)ptr;
<span class="co">uint16_t</span> host  = <span class="cf">ntohs</span>(raw);        <span class="cm">// host byte order</span>
<span class="co">uint16_t</span> offset = host &amp; <span class="cn">0x1FFF</span>;     <span class="cm">// NOW safe to mask fragment offset</span>
<span class="co">uint16_t</span> df     = host &amp; <span class="cn">0x4000</span>;     <span class="cm">// Don't Fragment bit</span>

<span class="cm">// Writing back: convert to network order</span>
pkt->frag_off = <span class="cf">htons</span>(host);</div>

<p class="sep">OVERFLOW AND WRAPAROUND</p>

<div class="two-col">
<div class="p-teal">
<h4>Unsigned Overflow — Well-Defined Wraparound</h4>
Unsigned integer overflow wraps modulo 2<sup>N</sup>. Exploited intentionally in checksums, ring buffers, and TCP sequence number arithmetic.
</div>
<div class="p-orange">
<h4>Signed Overflow — Undefined Behaviour (C)</h4>
Signed integer overflow is UB in C. The compiler may assume it never happens and optimise away your overflow guards. Always use unsigned types for bit manipulation.
</div>
</div>

<div class="diagram-box">uint8_t x = 255;  x++;  // wraps to 0 — defined for unsigned ✓
int8_t  y = 127;  y++;  // UB in C — may silently corrupt logic ✗

// Safe patterns:
uint32_t a = UINT32_MAX;
uint32_t sum = a + 1;       // wraps to 0 — defined ✓
// To detect: check BEFORE adding
if (a > UINT32_MAX - b) { /* overflow */ }

// Shift safety:
int x = 1 &lt;&lt; 31;            // UB on signed int!
uint32_t x = 1U &lt;&lt; 31;     // Fine — unsigned ✓</div>

</div><!-- /t-binary -->

<!-- TAB: 6 Operators -->
<div id="t-ops" class="tab-pane">

<p class="sep">THE 6 BITWISE OPERATORS</p>

<table class="t-table">
<thead><tr><th>Operator</th><th>Symbol</th><th>Rule</th><th>Key Use</th></tr></thead>
<tbody>
<tr><td><strong>AND</strong></td><td><code>&amp;</code></td><td>1 only when BOTH bits are 1</td><td>Filter/mask — forces bits to 0</td></tr>
<tr><td><strong>OR</strong></td><td><code>|</code></td><td>1 when AT LEAST ONE bit is 1</td><td>Set (force to 1) specific bits</td></tr>
<tr><td><strong>XOR</strong></td><td><code>^</code></td><td>1 when bits are DIFFERENT</td><td>Toggle bits; self-cancellation tricks</td></tr>
<tr><td><strong>NOT</strong></td><td><code>~</code></td><td>Flips ALL bits (unary)</td><td>Create inverse masks to CLEAR bits</td></tr>
<tr><td><strong>Left Shift</strong></td><td><code>&lt;&lt;</code></td><td>Move bits toward MSB; fill 0s from right</td><td>Multiply by 2ⁿ; build masks with <code>1 &lt;&lt; n</code></td></tr>
<tr><td><strong>Right Shift</strong></td><td><code>&gt;&gt;</code></td><td>Move bits toward LSB</td><td>Divide by 2ⁿ; extract upper fields</td></tr>
</tbody>
</table>

<div class="two-col">
<div>
<div class="p-violet"><h4>AND — Extract lower nibble</h4></div>
<div class="diagram-box">x    = 0xB7 = 1011 0111
mask = 0x0F = 0000 1111
            ─────────────
result       = 0x07 = 0000 0111
↑ lower 4 bits preserved, upper 4 zeroed</div>
</div>
<div>
<div class="p-violet"><h4>OR — Set bit 5</h4></div>
<div class="diagram-box">x    = 0x43 = 0100 0011
mask = 0x20 = 0010 0000  ← (1 &lt;&lt; 5)
            ─────────────
result       = 0x63 = 0110 0011
↑ bit 5 is now 1, rest unchanged</div>
</div>
</div>

<div class="two-col">
<div>
<div class="p-violet"><h4>XOR — Toggle bit 3</h4></div>
<div class="diagram-box">x    = 1011 0101
mask = 0000 1000  ← (1 &lt;&lt; 3)
     ─────────────
     = 1011 1101  ← bit 3 flipped

Properties:  x ^ x = 0  (self-cancel)
             x ^ 0 = x  (identity)
             x ^ y ^ y = x  (self-inverse)</div>
</div>
<div>
<div class="p-violet"><h4>NOT — Inverse mask</h4></div>
<div class="diagram-box">mask  = (1 &lt;&lt; 5) = 0000 0000 0010 0000
~mask             = 1111 1111 1101 1111
x &amp;= ~mask  ← clears bit 5, rest unchanged

In C:  ~0  on signed int = -1 (all bits set)
In Java: ~0  is also -1 (int always 32-bit)</div>
</div>
</div>

<p class="sep">SHIFTS — LOGICAL vs ARITHMETIC</p>

<div class="diagram-box">Left Shift  (&lt;&lt;):  zeros fill from right — always same behavior
  0b00000001 &lt;&lt; 3  =  0b00001000  (1 × 8 = 8)
  1 &lt;&lt; n  builds a mask with exactly bit n set.

Right Shift (&gt;&gt;):  LOGICAL (unsigned) fills 0; ARITHMETIC (signed) fills sign bit
  LOGICAL:     0b10110100 &gt;&gt; 2  →  0b00101101  (fills 0)
  ARITHMETIC:  0b10110100 &gt;&gt; 2  →  0b11101101  (fills sign bit)

C:   &gt;&gt; on unsigned = logical.  &gt;&gt; on signed = implementation-defined (usually arithmetic)
Java: &gt;&gt; = arithmetic,  &gt;&gt;&gt; = logical (unsigned right shift)</div>

<div class="warn">&#9888;&#65039; <strong>Java gotcha:</strong> There is no unsigned right shift in C — you must cast to unsigned first. In Java, always use <code>&gt;&gt;&gt;</code> when you want logical (zero-fill) shift on potentially-negative values.</div>

<p class="sep">OPERATOR PRECEDENCE — THE HIDDEN BUG</p>

<div class="warn">⚠️ <strong>Critical gotcha:</strong> Bitwise operators have <em>lower</em> precedence than comparison operators (<code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>). The expression <code>x &amp; mask == 0</code> is parsed as <code>x &amp; (mask == 0)</code> — almost certainly not what you want.</div>

<div class="diagram-box">WRONG — == binds tighter than &:
  if (x &amp; mask == 0) { ... }   // parsed as: x &amp; (mask == 0)  ← always 0

CORRECT — add parentheses:
  if ((x &amp; mask) == 0) { ... } // what you actually mean

Precedence (high → low):
  ~           NOT  (unary — highest bitwise)
  &lt;&lt; &gt;&gt;       Shifts
  &amp;           AND
  ^           XOR
  |           OR
  == != &lt; &gt;   Comparisons  ← sit ABOVE &, ^, | ← GOTCHA!
  &amp;&amp; ||       Logical AND/OR
  = |= &amp;= ^=  Assignment (lowest)</div>

<table class="t-table">
<thead><tr><th>Expression</th><th>Parsed as</th><th>Correct form</th></tr></thead>
<tbody>
<tr><td><code>x &amp; 0xFF == 0</code></td><td><code>x &amp; (0xFF == 0)</code> = <code>x &amp; 0</code> = always 0</td><td><code>(x &amp; 0xFF) == 0</code></td></tr>
<tr><td><code>x | y &gt; 0</code></td><td><code>x | (y &gt; 0)</code> — adds 0 or 1 to x</td><td><code>(x | y) &gt; 0</code></td></tr>
<tr><td><code>a ^ b == c</code></td><td><code>a ^ (b == c)</code> — XORs with boolean</td><td><code>(a ^ b) == c</code></td></tr>
<tr><td><code>flags &amp; FLAG_A != 0</code></td><td><code>flags &amp; (FLAG_A != 0)</code> = <code>flags &amp; 1</code></td><td><code>(flags &amp; FLAG_A) != 0</code></td></tr>
</tbody>
</table>

<div class="ins">✅ <strong>Rule:</strong> Always wrap every bitwise sub-expression in its own parentheses when mixing with comparisons or logical operators.</div>

</div><!-- /t-ops -->

<!-- TAB: Bit Masking -->
<div id="t-mask" class="tab-pane">

<p class="sep">THE 4 CORE MASK OPERATIONS</p>

<table class="t-table">
<thead><tr><th>Operation</th><th>Formula</th><th>Effect</th></tr></thead>
<tbody>
<tr><td><strong>SET</strong></td><td><code>x |= (1 &lt;&lt; n)</code></td><td>Force bit n to 1</td></tr>
<tr><td><strong>CLEAR</strong></td><td><code>x &amp;= ~(1 &lt;&lt; n)</code></td><td>Force bit n to 0</td></tr>
<tr><td><strong>TOGGLE</strong></td><td><code>x ^= (1 &lt;&lt; n)</code></td><td>Flip bit n</td></tr>
<tr><td><strong>CHECK</strong></td><td><code>(x &gt;&gt; n) &amp; 1</code></td><td>Read bit n — returns 0 or 1</td></tr>
</tbody>
</table>

<div class="cb"><span class="co">uint16_t</span> x = <span class="cn">0b0000010011010010</span>;  <span class="cm">// = 1234</span>

x |= (<span class="cn">1</span> &lt;&lt; <span class="cn">7</span>);        <span class="cm">// SET   bit 7</span>
x &amp;= ~(<span class="cn">1</span> &lt;&lt; <span class="cn">6</span>);       <span class="cm">// CLEAR bit 6</span>
x ^= (<span class="cn">1</span> &lt;&lt; <span class="cn">4</span>);        <span class="cm">// TOGGLE bit 4</span>
<span class="ck">int</span> b3 = (x &gt;&gt; <span class="cn">3</span>) &amp; <span class="cn">1</span>; <span class="cm">// CHECK bit 3 → 0 or 1</span></div>

<p class="sep">MULTI-BIT MASK CONSTRUCTION</p>

<div class="p-teal">
<h4>Formula: mask for <em>width</em> bits starting at <em>pos</em></h4>
<code>mask = ((1 &lt;&lt; width) - 1) &lt;&lt; pos</code>
</div>

<div class="diagram-box">Goal: Build mask for bits 13, 14, 15 (3 bits wide, starting at bit 13)

Step 1 — (1 &lt;&lt; 3) = 0b1000
Step 2 — subtract 1 = 0b0111  ← 3 consecutive ones
Step 3 — shift to pos 13:

Bit:  15  14  13  12  11 ... 0
mask:  1   1   1   0   0 ... 0  = 0xE000

mask = ((1 &lt;&lt; 3) - 1) &lt;&lt; 13 = 0xE000</div>

<p class="sep">PATTERN INSERTION — READ/WRITE A BITFIELD</p>

<div class="p-violet">
<h4>3-Step: Clear target bits → OR in new pattern</h4>
Goal: Replace bits 15–13 with pattern <code>0b110</code>
</div>

<div class="diagram-box">x = 1234 = 0000 0100 1101 0010   (bits 15,14,13 = 000)

STEP 1 — Build mask:    mask = ((1&lt;&lt;3)-1) &lt;&lt; 13 = 0xE000
STEP 2 — Clear target:  x &amp; ~mask = 0000 0100 1101 0010
STEP 3 — OR in pattern: pattern = 0b110 &lt;&lt; 13 = 0xC000
                        result  = 1100 0100 1101 0010
                        bits 15,14,13 = 1,1,0 ✓</div>

<div class="cb"><span class="co">uint16_t</span> x = <span class="cn">1234</span>;
<span class="co">uint16_t</span> mask    = ((<span class="cn">1</span> &lt;&lt; <span class="cn">3</span>) - <span class="cn">1</span>) &lt;&lt; <span class="cn">13</span>;   <span class="cm">// 0xE000 — covers bits 13,14,15</span>
<span class="co">uint16_t</span> pattern = <span class="cn">0b110</span> &lt;&lt; <span class="cn">13</span>;              <span class="cm">// 0xC000</span>
x = (x &amp; ~mask) | pattern;                  <span class="cm">// Result = 0xC4D2</span></div>

<p class="sep">EXTRACT A BITFIELD</p>

<div class="cb"><span class="cm">// Extract width bits starting at position start</span>
<span class="cm">// Formula: (x &gt;&gt; start) &amp; ((1 &lt;&lt; width) - 1)</span>

<span class="ck">int</span> start = <span class="cn">13</span>, width = <span class="cn">3</span>;
<span class="co">uint16_t</span> field = (x &gt;&gt; start) &amp; ((<span class="cn">1</span> &lt;&lt; width) - <span class="cn">1</span>);
<span class="cm">// Extracts bits 13–15 as a standalone 0–7 value</span></div>

<div class="warn">&#9888;&#65039; <strong>C gotcha:</strong> <code>~mask</code> on a 16-bit value may sign-extend to 32-bit. Cast explicitly: <code>(uint16_t)(~mask)</code> to be safe in mixed-width expressions.</div>

<p class="sep">BITMASK AS A SET — UNION, INTERSECTION, DIFFERENCE</p>

<div class="p-violet">
<h4>A bitmask of N bits represents a subset of N elements</h4>
Bit <em>i</em> = 1 means element <em>i</em> is <em>in</em> the set. Bit <em>i</em> = 0 means it is absent. This abstraction drives subset-sum DP, scheduling, permutation states, and flag systems.
</div>

<table class="t-table">
<thead><tr><th>Set Operation</th><th>Formula</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td><strong>Union</strong></td><td><code>A | B</code></td><td>Elements in A or B (or both)</td></tr>
<tr><td><strong>Intersection</strong></td><td><code>A &amp; B</code></td><td>Elements in both A and B</td></tr>
<tr><td><strong>Difference A − B</strong></td><td><code>A &amp; ~B</code></td><td>Elements in A but not in B</td></tr>
<tr><td><strong>Complement</strong></td><td><code>~A &amp; FULL</code></td><td>All elements NOT in A (where FULL = (1&lt;&lt;N)−1)</td></tr>
<tr><td><strong>Is subset?</strong></td><td><code>(A &amp; B) == A</code></td><td>Every element of A is also in B</td></tr>
<tr><td><strong>Is empty?</strong></td><td><code>A == 0</code></td><td>Set has no elements</td></tr>
<tr><td><strong>Full set (N bits)</strong></td><td><code>(1 &lt;&lt; N) - 1</code></td><td>All N elements present</td></tr>
<tr><td><strong>Add element i</strong></td><td><code>A | (1 &lt;&lt; i)</code></td><td>Include element i in A</td></tr>
<tr><td><strong>Remove element i</strong></td><td><code>A &amp; ~(1 &lt;&lt; i)</code></td><td>Exclude element i from A</td></tr>
</tbody>
</table>

<div class="cb"><span class="cm">// 4 tasks {T0, T1, T2, T3} mapped to bits 0–3</span>
<span class="ck">int</span> A = <span class="cn">0b0101</span>;   <span class="cm">// {T0, T2} selected</span>
<span class="ck">int</span> B = <span class="cn">0b0110</span>;   <span class="cm">// {T1, T2} selected</span>

<span class="ck">int</span> u   = A | B;          <span class="cm">// 0b0111 = {T0,T1,T2} — union</span>
<span class="ck">int</span> i   = A &amp; B;          <span class="cm">// 0b0100 = {T2}       — intersection</span>
<span class="ck">int</span> d   = A &amp; ~B;         <span class="cm">// 0b0001 = {T0}       — A minus B</span>
<span class="ck">int</span> all = (<span class="cn">1</span> &lt;&lt; <span class="cn">4</span>) - <span class="cn">1</span>; <span class="cm">// 0b1111 = {T0,T1,T2,T3} — full set</span>

<span class="cm">// Iterate all non-empty subsets of set S (classic DP trick):</span>
<span class="ck">for</span> (<span class="ck">int</span> sub = S; sub &gt; <span class="cn">0</span>; sub = (sub - <span class="cn">1</span>) &amp; S) {
    <span class="cm">// process subset 'sub' — covers all 2^|S| non-empty subsets</span>
}</div>

<div class="note">📌 <strong>Subset enumeration:</strong> <code>sub = (sub−1) &amp; S</code> iterates all non-empty subsets of S efficiently. This is the cornerstone of bitmask DP for problems like TSP, task scheduling, and subset-sum variants.</div>

</div><!-- /t-mask -->

<!-- TAB: Classic Tricks -->
<div id="t-tricks" class="tab-pane">

<p class="sep">THE CANONICAL BIT TRICKS</p>

<div class="two-col">
<div class="pattern-card">
<h4>&#128994; Is Power of Two?</h4>
<div class="diagram-box">x     = 16 = 0001 0000
x-1   = 15 = 0000 1111
x&(x-1)   = 0000 0000 ← zero!

Non-power (20): 0001 0100
          19:   0001 0011
          AND:  0001 0000 ← non-zero</div>
<div class="cb"><span class="ck">bool</span> <span class="cf">isPow2</span>(<span class="ck">int</span> x) {
    <span class="ck">return</span> x &gt; <span class="cn">0</span> &amp;&amp; (x &amp; (x-<span class="cn">1</span>)) == <span class="cn">0</span>;
}</div>
</div>
<div class="pattern-card">
<h4>&#128308; Clear Lowest Set Bit</h4>
<div class="diagram-box">x     = 1011 0100
x-1   = 1011 0011  (borrow cascades up)
x&(x-1)= 1011 0000  ← lowest set bit gone</div>
<div class="cb"><span class="cm">// Brian Kernighan bit count</span>
<span class="ck">int</span> <span class="cf">countBits</span>(<span class="ck">int</span> x) {
    <span class="ck">int</span> c = <span class="cn">0</span>;
    <span class="ck">while</span> (x) { x &amp;= (x-<span class="cn">1</span>); c++; }
    <span class="ck">return</span> c;  <span class="cm">// O(set bits) not O(32)</span>
}</div>
</div>
</div>

<div class="two-col">
<div class="pattern-card">
<h4>&#128309; Isolate Lowest Set Bit</h4>
<div class="diagram-box">x     = 1011 0100
-x    = 0100 1100  (two's complement: ~x+1)
x&(-x)= 0000 0100  ← only lowest bit remains

Why: -x flips all bits above the lowest 1,
     leaves the 1 intact; AND zeros the rest.</div>
<div class="cb"><span class="ck">int</span> lowest = x &amp; (-x);</div>
</div>
<div class="pattern-card">
<h4>&#128310; Find MSB Position</h4>
<div class="cb"><span class="cm">// GCC built-in (fastest)</span>
<span class="ck">int</span> msb = <span class="cn">31</span> - <span class="cf">__builtin_clz</span>(x);
<span class="cm">// clz = count leading zeros</span>

<span class="cm">// Portable — bit-smearing</span>
<span class="co">uint32_t</span> <span class="cf">smear</span>(<span class="co">uint32_t</span> x) {
    x |= x &gt;&gt; <span class="cn">1</span>; x |= x &gt;&gt; <span class="cn">2</span>;
    x |= x &gt;&gt; <span class="cn">4</span>; x |= x &gt;&gt; <span class="cn">8</span>;
    x |= x &gt;&gt; <span class="cn">16</span>;
    <span class="ck">return</span> x - (x &gt;&gt; <span class="cn">1</span>);
}</div>
</div>
</div>

<p class="sep">MORE CLASSIC ONE-LINERS</p>

<div class="cb"><span class="cm">// XOR swap — no temp variable (AVOID in production)</span>
a ^= b;  b ^= a;  a ^= b;  <span class="cm">// Fails if a and b are same memory location!</span>

<span class="cm">// Branchless sign detection (signed 32-bit)</span>
<span class="ck">int</span> sign = x &gt;&gt; <span class="cn">31</span>;  <span class="cm">// 0 if positive, -1 (0xFFFFFFFF) if negative</span>

<span class="cm">// Branchless absolute value</span>
<span class="ck">int</span> mask = x &gt;&gt; <span class="cn">31</span>;     <span class="cm">// all-zeros or all-ones</span>
<span class="ck">int</span> abs  = (x + mask) ^ mask;  <span class="cm">// For x=-5: (-5-1)^0xFFFFFFFF = 5</span>

<span class="cm">// Rotate left k bits (32-bit)</span>
<span class="co">uint32_t</span> <span class="cf">rotl</span>(<span class="co">uint32_t</span> x, <span class="ck">int</span> k) { <span class="ck">return</span> (x &lt;&lt; k) | (x &gt;&gt; (<span class="cn">32</span>-k)); }
<span class="co">uint32_t</span> <span class="cf">rotr</span>(<span class="co">uint32_t</span> x, <span class="ck">int</span> k) { <span class="ck">return</span> (x &gt;&gt; k) | (x &lt;&lt; (<span class="cn">32</span>-k)); }</div>

<div class="note">&#128204; <strong>Rotations</strong> wrap bits around instead of discarding them — unlike shifts. Essential in cryptography (AES, SHA) and networking checksums. The formula <code>(x &lt;&lt; k) | (x &gt;&gt; (32-k))</code> is what most compilers recognize and compile to a single <code>ROL</code> / <code>ROR</code> instruction.</div>

<div class="two-col">
<div class="pattern-card">
<h4>🟣 Find Position of Lowest Set Bit</h4>
<div class="diagram-box">x        = 1011 0100
x &amp; (-x) = 0000 0100  ← isolates bit 2

__builtin_ctz(x) = count trailing zeros = bit position
ctz(0b10110100) = 2  ← position of lowest '1'</div>
<div class="cb"><span class="cm">// GCC/Clang — compiles to single BSF/TZCNT on x86</span>
<span class="ck">int</span> pos = <span class="cf">__builtin_ctz</span>(x);   <span class="cm">// count trailing zeros (C)</span>

<span class="cm">// Java equivalent</span>
<span class="ck">int</span> pos = <span class="cf">Integer.numberOfTrailingZeros</span>(x);

<span class="cm">// Portable C (no builtins) — use isolate-then-popcount:</span>
<span class="ck">int</span> pos = <span class="cf">__builtin_popcount</span>((x &amp; -x) - <span class="cn">1</span>);</div>
</div>
<div class="pattern-card">
<h4>🯤 Next Power of Two</h4>
<div class="diagram-box">Goal: round x UP to nearest power of 2.
Key: smear all bits below MSB, then add 1.

x = 0b0101 1100  (92)
After smearing: 0b0111 1111  (127)
Add 1:          0b1000 0000  (128) ✓</div>
<div class="cb"><span class="co">uint32_t</span> <span class="cf">nextPow2</span>(<span class="co">uint32_t</span> x) {
    <span class="ck">if</span> (x == <span class="cn">0</span>) <span class="ck">return</span> <span class="cn">1</span>;
    x--;               <span class="cm">// handle exact powers of 2</span>
    x |= x &gt;&gt; <span class="cn">1</span>;  x |= x &gt;&gt; <span class="cn">2</span>;
    x |= x &gt;&gt; <span class="cn">4</span>;  x |= x &gt;&gt; <span class="cn">8</span>;
    x |= x &gt;&gt; <span class="cn">16</span>;
    <span class="ck">return</span> x + <span class="cn">1</span>;
}
<span class="cm">// nextPow2(100)=128  nextPow2(128)=128  nextPow2(0)=1</span></div>
</div>
</div>

</div><!-- /t-tricks -->

<!-- TAB: Ranges & Bitfields -->
<div id="t-range" class="tab-pane">

<p class="sep">UNIVERSAL BITFIELD FORMULA REFERENCE</p>

<div class="diagram-box">EXTRACT a bitfield (read bits [start .. start+width-1]):
  field = (value &gt;&gt; start) &amp; ((1 &lt;&lt; width) - 1)

INSERT a bitfield (write pattern into bits [start .. start+width-1]):
  mask  = ((1 &lt;&lt; width) - 1) &lt;&lt; start
  value = (value &amp; ~mask) | ((pattern &amp; ((1 &lt;&lt; width)-1)) &lt;&lt; start)

CHECK if any bit in range is set:
  (value &amp; mask) != 0

COUNT set bits in range:
  popcount((value &gt;&gt; start) &amp; ((1 &lt;&lt; width) - 1))</div>

<p class="sep">REVERSE BITS — DIVIDE AND CONQUER</p>

<div class="cb"><span class="co">uint32_t</span> <span class="cf">reverseBits</span>(<span class="co">uint32_t</span> n) {
    n = ((n &amp; <span class="cn">0xFFFF0000</span>) &gt;&gt; <span class="cn">16</span>) | ((n &amp; <span class="cn">0x0000FFFF</span>) &lt;&lt; <span class="cn">16</span>); <span class="cm">// swap halves</span>
    n = ((n &amp; <span class="cn">0xFF00FF00</span>) &gt;&gt;  <span class="cn">8</span>) | ((n &amp; <span class="cn">0x00FF00FF</span>) &lt;&lt;  <span class="cn">8</span>); <span class="cm">// swap bytes</span>
    n = ((n &amp; <span class="cn">0xF0F0F0F0</span>) &gt;&gt;  <span class="cn">4</span>) | ((n &amp; <span class="cn">0x0F0F0F0F</span>) &lt;&lt;  <span class="cn">4</span>); <span class="cm">// swap nibbles</span>
    n = ((n &amp; <span class="cn">0xCCCCCCCC</span>) &gt;&gt;  <span class="cn">2</span>) | ((n &amp; <span class="cn">0x33333333</span>) &lt;&lt;  <span class="cn">2</span>); <span class="cm">// swap pairs</span>
    n = ((n &amp; <span class="cn">0xAAAAAAAA</span>) &gt;&gt;  <span class="cn">1</span>) | ((n &amp; <span class="x55555555</span>) &lt;&lt;  <span class="cn">1</span>); <span class="cm">// swap bits</span>
    <span class="ck">return</span> n;
}</div>

<div class="p-teal">
<h4>Strategy: Divide-and-Conquer Swap</h4>
Each level swaps progressively smaller chunks: 16-bit halves → 8-bit bytes → 4-bit nibbles → 2-bit pairs → individual bits. Five passes, no loops. The masks are alternating patterns: <code>0xAAAAAAAA</code> = <code>1010...1010</code>, <code>0x55555555</code> = <code>0101...0101</code>.
</div>

<p class="sep">GRAY CODE</p>

<div class="cb"><span class="cm">// Binary → Gray code (consecutive values differ by exactly 1 bit)</span>
<span class="ck">int</span> <span class="cf">toGray</span>(<span class="ck">int</span> n) { <span class="ck">return</span> n ^ (n &gt;&gt; <span class="cn">1</span>); }

<span class="cm">// Gray code → Binary</span>
<span class="ck">int</span> <span class="cf">fromGray</span>(<span class="ck">int</span> g) {
    <span class="ck">int</span> n = <span class="cn">0</span>;
    <span class="ck">for</span> (; g &gt; <span class="cn">0</span>; g &gt;&gt;= <span class="cn">1</span>) n ^= g;
    <span class="ck">return</span> n;
}</div>

<div class="diagram-box">Gray Code — consecutive values differ by exactly 1 bit:
Dec │ Binary │ Gray
────┼────────┼──────
 0  │  000   │  000
 1  │  001   │  001  ← 1 bit different
 2  │  010   │  011  ← 1 bit different
 3  │  011   │  010  ← 1 bit different
 4  │  100   │  110  ← 1 bit different
 5  │  101   │  111
 6  │  110   │  101
 7  │  111   │  100</div>

</div><!-- /t-range -->

<!-- TAB: Systems & Flags -->
<div id="t-systems" class="tab-pane">

<div class="p-orange">
<h4>&#9889; Real-World Context: DPDK rte_mbuf.ol_flags</h4>
<code>ol_flags</code> is a 64-bit integer on every DPDK packet with 30+ defined flag bits controlling TX/RX offloads, tunneling, timestamps, and security metadata. Every packet in a SASE dataplane engine uses exactly this pattern.
</div>

<div class="cb"><span class="cm">// Define flag constants — each is a power-of-2 bit position</span>
<span class="cv">#define PKT_RX_VLAN</span>         (<span class="cn">1</span> &lt;&lt; <span class="cn">0</span>)   <span class="cm">// bit 0 — VLAN stripped</span>
<span class="cv">#define PKT_RX_RSS_HASH</span>     (<span class="cn">1</span> &lt;&lt; <span class="cn">1</span>)   <span class="cm">// bit 1 — RSS hash valid</span>
<span class="cv">#define PKT_TX_OFFLOAD_IP</span>   (<span class="cn">1</span> &lt;&lt; <span class="cn">2</span>)   <span class="cm">// bit 2 — IP checksum offload</span>
<span class="cv">#define PKT_TX_TCP_SEG</span>      (<span class="cn">1</span> &lt;&lt; <span class="cn">3</span>)   <span class="cm">// bit 3 — TCP segmentation</span>

<span class="co">uint64_t</span> ol_flags = <span class="cn">0</span>;

ol_flags |= PKT_RX_VLAN | PKT_RX_RSS_HASH;  <span class="cm">// Set multiple flags</span>

<span class="ck">if</span> (ol_flags &amp; PKT_TX_TCP_SEG) { <span class="cm">/* TSO path */</span> }   <span class="cm">// Check one flag</span>

ol_flags &amp;= ~PKT_RX_VLAN;                          <span class="cm">// Clear a flag</span>

<span class="co">uint64_t</span> both = PKT_RX_VLAN | PKT_RX_RSS_HASH;
<span class="ck">if</span> ((ol_flags &amp; both) == both) { <span class="cm">/* both set */</span> }  <span class="cm">// Check if BOTH set</span></div>

<p class="sep">IPv4 HEADER BITFIELDS</p>

<div class="diagram-box">IPv4 Flags + Fragment Offset (16-bit word at header offset 6):

Bit: 15  14  13  12 11 10 9 8 7 6 5 4 3 2 1 0
     ┌───┬───┬───┬────────────────────────────┐
     │ 0 │DF │MF │  Fragment Offset (13 bits) │
     └───┴───┴───┴────────────────────────────┘
       Reserved   More Frags
              Don't Fragment

Extract Fragment Offset:  offset = ntohs(ip-&gt;frag_off) &amp; 0x1FFF
Check Don't Fragment bit: df     = ntohs(ip-&gt;frag_off) &amp; 0x4000</div>

<p class="sep">C BITFIELD STRUCTS vs EXPLICIT MASKS</p>

<div class="cb"><span class="cm">// C bitfield struct — concise but NOT portable for network protocols</span>
<span class="ck">struct</span> ipv4_hdr_bits {
    <span class="co">uint32_t</span> ihl       : <span class="cn">4</span>;   <span class="cm">// bits 0-3</span>
    <span class="co">uint32_t</span> version   : <span class="cn">4</span>;   <span class="cm">// bits 4-7</span>
    <span class="co">uint32_t</span> ecn       : <span class="cn">2</span>;   <span class="cm">// bits 8-9</span>
    <span class="co">uint32_t</span> dscp      : <span class="cn">6</span>;   <span class="cm">// bits 10-15</span>
    <span class="co">uint32_t</span> total_len : <span class="cn">16</span>;  <span class="cm">// bits 16-31</span>
};</div>

<div class="warn">&#9888;&#65039; <strong>Portability trap:</strong> Bit ordering within bytes in C structs is compiler and architecture-dependent. For network protocol parsing, always prefer <strong>explicit bit manipulation with masks and shifts</strong> over bitfield structs. The struct version above is readable for documentation but unsafe for cross-platform packet parsing.</div>

<p class="sep">TCP FLAGS FIELD</p>

<div class="diagram-box">TCP Flags — 9 bits at TCP header offset byte 13:

Bit:  8    7    6    5    4    3    2    1    0
      ┌────┬────┬────┬────┬────┬────┬────┬────┬────┐
      │ NS │CWR │ECE │URG │ACK │PSH │RST │SYN │FIN │
      └────┴────┴────┴────┴────┴────┴────┴────┴────┘

Common patterns:
  SYN         = 0x002  ← connection initiation
  SYN+ACK     = 0x012  ← server handshake reply
  ACK         = 0x010  ← data acknowledgement
  FIN+ACK     = 0x011  ← graceful connection close
  RST         = 0x004  ← abrupt reset / port closed</div>

<div class="cb"><span class="cv">#define TCP_FIN  0x01</span>
<span class="cv">#define TCP_SYN  0x02</span>
<span class="cv">#define TCP_RST  0x04</span>
<span class="cv">#define TCP_PSH  0x08</span>
<span class="cv">#define TCP_ACK  0x10</span>
<span class="cv">#define TCP_URG  0x20</span>
<span class="cv">#define TCP_ECE  0x40</span>
<span class="cv">#define TCP_CWR  0x80</span>

<span class="co">uint8_t</span> flags = tcp_hdr-&gt;th_flags;

<span class="ck">if</span> (flags &amp; TCP_SYN) {                             <span class="cm">// new connection</span> }
<span class="ck">if</span> ((flags &amp; (TCP_SYN | TCP_ACK)) == (TCP_SYN | TCP_ACK)) { <span class="cm">// handshake</span> }
<span class="ck">if</span> (flags &amp; TCP_RST) {                             <span class="cm">// reset — drop state</span> }
<span class="ck">if</span> (flags &amp; TCP_FIN) {                             <span class="cm">// graceful close</span> }</div>

<p class="sep">VLAN 802.1Q TAG — COMPLETE EXTRACTION</p>

<div class="diagram-box">802.1Q VLAN Tag — 16 bits (follows EtherType 0x8100):

Bit: 15  14  13  12  11  10   9   8   7   6   5   4   3   2   1   0
     ┌──────────┬───┬──────────────────────────────────────┐
     │  PCP (3)   │DEI│            VID (12 bits)              │
     └──────────┴───┴──────────────────────────────────────┘
     Priority     Drop  VLAN ID (0–4095)
     Code Point   Elig.

PCP = bits [15:13] — 3-bit 802.1p QoS priority (0–7, 7 = highest)
DEI = bit  [12]    — Drop Eligible Indicator
VID = bits [11:0]  — VLAN ID (VID 0=untagged, 4095=reserved)</div>

<div class="cb"><span class="co">uint16_t</span> tag = <span class="cf">ntohs</span>(*(<span class="co">uint16_t</span>*)(pkt + <span class="cn">14</span>)); <span class="cm">// after 14-byte Ethernet hdr</span>

<span class="co">uint8_t</span>  pcp = (tag &gt;&gt; <span class="cn">13</span>) &amp; <span class="cn">0x07</span>;  <span class="cm">// bits 15–13: priority 0–7</span>
<span class="co">uint8_t</span>  dei = (tag &gt;&gt; <span class="cn">12</span>) &amp; <span class="cn">0x01</span>;  <span class="cm">// bit  12:    drop eligible</span>
<span class="co">uint16_t</span> vid = tag &amp; <span class="cn">0x0FFF</span>;        <span class="cm">// bits 11–0:  VLAN ID 0–4095</span>

<span class="cm">// Rebuild tag from fields:</span>
tag = ((<span class="co">uint16_t</span>)pcp &lt;&lt; <span class="cn">13</span>) | ((<span class="co">uint16_t</span>)dei &lt;&lt; <span class="cn">12</span>) | (vid &amp; <span class="cn">0x0FFF</span>);</div>

<div class="note">📌 <strong>VID 0</strong> = priority-tagged (no VLAN). <strong>VID 4095</strong> = reserved. Valid user VLANs: 1–4094. Always call <code>ntohs()</code> before extracting fields from a live packet.</div>

</div><!-- /t-systems -->

<!-- TAB: Interview Patterns -->
<div id="t-patterns" class="tab-pane">

<p class="sep">PATTERN RECOGNITION CHEAT SHEET</p>

<table class="t-table">
<thead><tr><th>When You See...</th><th>Think...</th><th>Key Formula</th></tr></thead>
<tbody>
<tr><td>Find unique / missing element</td><td>XOR pair cancellation</td><td><code>result ^= each element</code></td></tr>
<tr><td>No extra space, O(n)</td><td>XOR trick</td><td><code>x ^ x = 0, x ^ 0 = x</code></td></tr>
<tr><td>Is power of two?</td><td>Clear lowest set bit</td><td><code>x &gt; 0 &amp;&amp; (x &amp; (x-1)) == 0</code></td></tr>
<tr><td>Count set bits</td><td>Brian Kernighan</td><td><code>x &amp;= x-1</code> in loop</td></tr>
<tr><td>Set/clear/toggle one bit</td><td>OR / AND~mask / XOR</td><td><code>1 &lt;&lt; n</code> as mask</td></tr>
<tr><td>Extract N bits from position P</td><td>Shift + mask</td><td><code>(x &gt;&gt; P) &amp; ((1&lt;&lt;N)-1)</code></td></tr>
<tr><td>Insert pattern at position P</td><td>Clear-then-OR</td><td><code>(x &amp; ~mask) | (pat &lt;&lt; P)</code></td></tr>
<tr><td>Consecutive elements differ by 1 bit</td><td>Gray code</td><td><code>n ^ (n &gt;&gt; 1)</code></td></tr>
<tr><td>Hamming distance</td><td>popcount of XOR</td><td><code>__builtin_popcount(x^y)</code></td></tr>
</tbody>
</table>

<p class="sep">CORE INTERVIEW SOLUTIONS</p>

<div class="pattern-card">
<h4>&#129504; Find Single Number — LeetCode 136</h4>
Every element appears twice except one. XOR cancels pairs: <code>x^x=0</code>.
</div>
<div class="cb"><span class="ck">int</span> <span class="cf">singleNumber</span>(<span class="ck">int</span>[] nums) {
    <span class="ck">int</span> result = <span class="cn">0</span>;
    <span class="ck">for</span> (<span class="ck">int</span> n : nums) result ^= n;
    <span class="ck">return</span> result;  <span class="cm">// O(n) time · O(1) space</span>
}</div>

<div class="pattern-card">
<h4>&#129504; Find Missing Number</h4>
Array contains 0..n with one missing. XOR all indices with all values.
</div>
<div class="cb"><span class="ck">int</span> <span class="cf">missingNumber</span>(<span class="ck">int</span>[] nums) {
    <span class="ck">int</span> xor = nums.length;  <span class="cm">// start with n</span>
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">0</span>; i &lt; nums.length; i++)
        xor ^= i ^ nums[i];  <span class="cm">// paired indices and values cancel</span>
    <span class="ck">return</span> xor;
}</div>

<div class="pattern-card">
<h4>&#129504; Two Elements Appearing Once (others twice)</h4>
XOR all → get x^y. Use rightmost differing bit to partition array into two groups.
</div>
<div class="cb"><span class="ck">int</span>[] <span class="cf">twoSingleNumbers</span>(<span class="ck">int</span>[] nums) {
    <span class="ck">int</span> xorAll = <span class="cn">0</span>;
    <span class="ck">for</span> (<span class="ck">int</span> n : nums) xorAll ^= n;       <span class="cm">// xorAll = x ^ y</span>
    <span class="ck">int</span> diffBit = xorAll &amp; (-xorAll);     <span class="cm">// rightmost bit where x≠y</span>
    <span class="ck">int</span> a = <span class="cn">0</span>, b = <span class="cn">0</span>;
    <span class="ck">for</span> (<span class="ck">int</span> n : nums) {
        <span class="ck">if</span> ((n &amp; diffBit) != <span class="cn">0</span>) a ^= n;  <span class="cm">// group with that bit set</span>
        <span class="ck">else</span>                    b ^= n;  <span class="cm">// group without</span>
    }
    <span class="ck">return</span> <span class="ck">new</span> <span class="ck">int</span>[]{a, b};
}</div>

<div class="pattern-card">
<h4>&#129504; Count Bits for 0..n — LeetCode 338</h4>
DP: <code>dp[i] = dp[i &gt;&gt; 1] + (i &amp; 1)</code>. Removes LSB and adds it back.
</div>
<div class="cb"><span class="ck">int</span>[] <span class="cf">countBits</span>(<span class="ck">int</span> n) {
    <span class="ck">int</span>[] dp = <span class="ck">new</span> <span class="ck">int</span>[n + <span class="cn">1</span>];
    <span class="ck">for</span> (<span class="ck">int</span> i = <span class="cn">1</span>; i &lt;= n; i++)
        dp[i] = dp[i &gt;&gt; <span class="cn">1</span>] + (i &amp; <span class="cn">1</span>);  <span class="cm">// O(n)</span>
    <span class="ck">return</span> dp;
}</div>

<p class="sep">MORE INTERVIEW PATTERNS</p>

<div class="pattern-card">
<h4>🧠 Single Number II — LeetCode 137 (each element appears 3 times)</h4>
XOR cancels pairs but not triplets. Use two variables (<code>ones</code>, <code>twos</code>) to track per-bit modulo-3 count. The single number accumulates in <code>ones</code>.
</div>
<div class="cb"><span class="ck">int</span> <span class="cf">singleNumberII</span>(<span class="ck">int</span>[] nums) {
    <span class="ck">int</span> ones = <span class="cn">0</span>, twos = <span class="cn">0</span>;
    <span class="ck">for</span> (<span class="ck">int</span> n : nums) {
        ones = (ones ^ n) &amp; ~twos;  <span class="cm">// add to ‘seen once’ if not in ‘seen twice’</span>
        twos = (twos ^ n) &amp; ~ones;  <span class="cm">// add to ‘seen twice’ if not in ‘seen once’</span>
    }
    <span class="ck">return</span> ones;  <span class="cm">// bits that appeared exactly 1 time (mod 3)</span>
}</div>

<div class="pattern-card">
<h4>🧠 Hamming Distance — LeetCode 461 &amp; Total Hamming Distance LC 477</h4>
Number of positions where two values differ = popcount of their XOR.
</div>
<div class="cb"><span class="cm">// Single pair — O(1)</span>
<span class="ck">int</span> <span class="cf">hammingDistance</span>(<span class="ck">int</span> x, <span class="ck">int</span> y) {
    <span class="ck">return</span> <span class="cf">Integer.bitCount</span>(x ^ y);  <span class="cm">// Java; C: __builtin_popcount(x^y)</span>
}

<span class="cm">// Total Hamming distance across all pairs in array — O(32n)</span>
<span class="ck">int</span> <span class="cf">totalHammingDistance</span>(<span class="ck">int</span>[] nums) {
    <span class="ck">int</span> total = <span class="cn">0</span>;
    <span class="ck">for</span> (<span class="ck">int</span> bit = <span class="cn">0</span>; bit &lt; <span class="cn">32</span>; bit++) {
        <span class="ck">int</span> ones = <span class="cn">0</span>;
        <span class="ck">for</span> (<span class="ck">int</span> n : nums) ones += (n &gt;&gt; bit) &amp; <span class="cn">1</span>;
        total += ones * (nums.length - ones); <span class="cm">// pairs that differ at this bit</span>
    }
    <span class="ck">return</span> total;
}</div>

<div class="pattern-card">
<h4>🧠 Bitwise AND of Range [m, n] — LeetCode 201</h4>
AND of all numbers in [m, n]. Any bit that flips across the range becomes 0. Only the common prefix of m and n survives.
</div>
<div class="cb"><span class="ck">int</span> <span class="cf">rangeBitwiseAnd</span>(<span class="ck">int</span> m, <span class="ck">int</span> n) {
    <span class="ck">int</span> shift = <span class="cn">0</span>;
    <span class="ck">while</span> (m != n) {   <span class="cm">// right-shift until equal = find common prefix</span>
        m &gt;&gt;= <span class="cn">1</span>;
        n &gt;&gt;= <span class="cn">1</span>;
        shift++;
    }
    <span class="ck">return</span> m &lt;&lt; shift;  <span class="cm">// restore prefix to original bit position</span>
}
<span class="cm">// Example: [5,7] = 101 &amp; 110 &amp; 111 = 100  → common prefix = 1, shift=2 → 4</span></div>

</div><!-- /t-patterns -->

<!-- TAB: Quick Reference -->
<div id="t-ref" class="tab-pane">

<p class="sep">OPERATOR SUMMARY</p>

<table class="t-table">
<thead><tr><th>Operator</th><th>Symbol</th><th>Effect</th><th>Example</th></tr></thead>
<tbody>
<tr><td>AND</td><td><code>&amp;</code></td><td>1 only if both 1 — masks/filters</td><td><code>0b1100 &amp; 0b1010 = 0b1000</code></td></tr>
<tr><td>OR</td><td><code>|</code></td><td>1 if at least one 1 — sets bits</td><td><code>0b1100 | 0b0011 = 0b1111</code></td></tr>
<tr><td>XOR</td><td><code>^</code></td><td>1 if bits differ — toggles/compares</td><td><code>0b1100 ^ 0b1010 = 0b0110</code></td></tr>
<tr><td>NOT</td><td><code>~</code></td><td>Flips all bits</td><td><code>~0b00001111 = 0b11110000</code></td></tr>
<tr><td>Left Shift</td><td><code>&lt;&lt;</code></td><td>Shift left, fill 0 from right</td><td><code>0b0001 &lt;&lt; 3 = 0b1000</code></td></tr>
<tr><td>Right Shift</td><td><code>&gt;&gt;</code></td><td>Shift right (logical/arithmetic)</td><td><code>0b1000 &gt;&gt; 2 = 0b0010</code></td></tr>
</tbody>
</table>

<p class="sep">CORE PATTERNS CHEATSHEET</p>

<table class="t-table">
<thead><tr><th>Goal</th><th>Code</th></tr></thead>
<tbody>
<tr><td>Set bit n</td><td><code>x |= (1 &lt;&lt; n)</code></td></tr>
<tr><td>Clear bit n</td><td><code>x &amp;= ~(1 &lt;&lt; n)</code></td></tr>
<tr><td>Toggle bit n</td><td><code>x ^= (1 &lt;&lt; n)</code></td></tr>
<tr><td>Check bit n</td><td><code>(x &gt;&gt; n) &amp; 1</code></td></tr>
<tr><td>Is power of two?</td><td><code>x &gt; 0 &amp;&amp; (x &amp; (x-1)) == 0</code></td></tr>
<tr><td>Clear lowest set bit</td><td><code>x &amp; (x - 1)</code></td></tr>
<tr><td>Isolate lowest set bit</td><td><code>x &amp; (-x)</code></td></tr>
<tr><td>Count set bits</td><td><code>while(x) { x &amp;= x-1; count++; }</code></td></tr>
<tr><td>Extract field [p, p+w)</td><td><code>(x &gt;&gt; p) &amp; ((1&lt;&lt;w)-1)</code></td></tr>
<tr><td>Insert pattern at p</td><td><code>(x &amp; ~mask) | (pat &lt;&lt; p)</code></td></tr>
<tr><td>Rotate left k</td><td><code>(x &lt;&lt; k) | (x &gt;&gt; (32-k))</code></td></tr>
<tr><td>XOR unique element</td><td><code>result=0; for n: result ^= n</code></td></tr>
</tbody>
</table>

<p class="sep">COMMON MASKS</p>

<table class="t-table">
<thead><tr><th>Mask</th><th>Hex</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>Lower 4 bits (nibble)</td><td><code>0x0F</code></td><td>Extract low nibble</td></tr>
<tr><td>Upper 4 bits</td><td><code>0xF0</code></td><td>Extract high nibble</td></tr>
<tr><td>Lower byte</td><td><code>0x00FF</code></td><td>Byte 0</td></tr>
<tr><td>Upper byte (16-bit)</td><td><code>0xFF00</code></td><td>Byte 1</td></tr>
<tr><td>Lower 16 bits</td><td><code>0x0000FFFF</code></td><td>Low word</td></tr>
<tr><td>Upper 16 bits</td><td><code>0xFFFF0000</code></td><td>High word</td></tr>
<tr><td>All ones (32-bit)</td><td><code>0xFFFFFFFF</code></td><td>Full mask / -1 (signed)</td></tr>
<tr><td>Alternating 01...</td><td><code>0x55555555</code></td><td>Even bits</td></tr>
<tr><td>Alternating 10...</td><td><code>0xAAAAAAAA</code></td><td>Odd bits</td></tr>
</tbody>
</table>

<p class="sep">MASTERY CHECKLIST</p>
<ul class="cl">
<li>Can convert between binary, hex, and decimal in both directions</li>
<li>Can represent negative numbers using two's complement (flip + add 1)</li>
<li>Can apply all 4 core mask operations: SET, CLEAR, TOGGLE, CHECK</li>
<li>Can build a multi-bit mask for any width/position using <code>((1&lt;&lt;w)-1)&lt;&lt;p</code></li>
<li>Can insert a bit pattern using 3-step clear-then-OR</li>
<li>Can extract a bitfield using shift-then-mask</li>
<li>Can explain why <code>x &amp; (x-1)</code> detects powers of two</li>
<li>Can explain why <code>x &amp; (-x)</code> isolates the lowest set bit</li>
<li>Can solve Single Number (LeetCode 136) using XOR in one pass</li>
<li>Can solve Count Bits (LeetCode 338) using DP in O(n)</li>
<li>Can write rotate-left / rotate-right for 32-bit unsigned</li>
<li>Can explain the difference between arithmetic and logical right shift and when each applies</li>
</ul>

</div><!-- /t-ref -->

<!-- TAB: Arithmetic & Memory -->
<div id="t-arith" class="tab-pane">

<p class="sep">SHIFT-BASED MULTIPLY AND DIVIDE</p>

<div class="p-violet">
<h4>Shifts are cheaper than multiply/divide on many architectures</h4>
Left shift by n = multiply by 2<sup>n</sup>. Right shift by n = divide by 2<sup>n</sup> (integer, rounds toward zero for unsigned). Compilers do this automatically, but recognising the pattern matters for bitfield arithmetic.
</div>

<div class="cb"><span class="cm">// Multiply by powers of 2</span>
<span class="ck">int</span> x8  = n &lt;&lt; <span class="cn">3</span>;   <span class="cm">// n * 8</span>
<span class="ck">int</span> x12 = (n &lt;&lt; <span class="cn">3</span>) + (n &lt;&lt; <span class="cn">2</span>);  <span class="cm">// n*8 + n*4 = n*12</span>

<span class="cm">// Divide by powers of 2 (unsigned — logical shift)</span>
<span class="co">uint32_t</span> d4  = x &gt;&gt; <span class="cn">2</span>;   <span class="cm">// x / 4  (exact if divisible, floors otherwise)</span>

<span class="cm">// Signed division: arithmetic right shift rounds toward -inf, not zero!</span>
<span class="cm">// For correct signed floor-divide by power of 2 use:</span>
<span class="ck">int</span> div4 = (x + <span class="cn">3</span>) &gt;&gt; <span class="cn">2</span>;  <span class="cm">// round toward zero for positive x</span></div>

<p class="sep">MEMORY ALIGNMENT — THE MOST IMPORTANT TRICK IN SYSTEMS</p>

<div class="p-orange">
<h4>Why alignment matters</h4>
Cache lines (64 bytes), DPDK buffers (128 bytes), DMA descriptors, SIMD vectors — all require naturally aligned addresses. Mis-aligned access causes bus errors on strict architectures and performance penalties everywhere else.
</div>

<div class="diagram-box">A pointer p is aligned to A bytes when: (p &amp; (A-1)) == 0
  (Works only when A is a power of 2 — then A-1 is an all-ones mask)

Round DOWN to alignment A:  aligned = ptr &amp; ~(A-1)
Round UP   to alignment A:  aligned = (ptr + A - 1) &amp; ~(A-1)

Example: A=64, ptr=0x1003
  Round down: 0x1003 &amp; ~63 = 0x1003 &amp; 0xFFFFFFC0 = 0x10C0
  Round up:  (0x1003 + 63) &amp; ~63 = 0x1042 &amp; 0xFFFFFFC0 = 0x1040</div>

<div class="cb"><span class="cm">// Check if ptr is aligned to A (A must be power of 2)</span>
<span class="ck">bool</span> isAligned(<span class="co">uintptr_t</span> ptr, <span class="ck">size_t</span> A) {
    <span class="ck">return</span> (ptr &amp; (A - <span class="cn">1</span>)) == <span class="cn">0</span>;
}

<span class="cm">// Round address up to next multiple of A</span>
<span class="co">uintptr_t</span> alignUp(<span class="co">uintptr_t</span> ptr, <span class="ck">size_t</span> A) {
    <span class="ck">return</span> (ptr + A - <span class="cn">1</span>) &amp; ~(A - <span class="cn">1</span>);
}

<span class="cm">// Round address down</span>
<span class="co">uintptr_t</span> alignDown(<span class="co">uintptr_t</span> ptr, <span class="ck">size_t</span> A) {
    <span class="ck">return</span> ptr &amp; ~(A - <span class="cn">1</span>);
}

<span class="cm">// Verify at runtime:</span>
assert(((uintptr_t)buf &amp; <span class="cn">63</span>) == <span class="cn">0</span>);  <span class="cm">// must be 64-byte aligned</span></div>

<p class="sep">MODULO BY POWER OF TWO</p>

<div class="p-teal">
<h4>x % (2^n) == x &amp; (2^n - 1) — when x is unsigned</h4>
This is why ring buffers, hash tables, and DPDK use power-of-2 sizes: the wrapping step becomes a single AND instead of a costly division.
</div>

<div class="cb"><span class="cm">// Expensive: requires integer divide instruction</span>
<span class="ck">int</span> idx = pos % capacity;   <span class="cm">// UB if capacity is 0, slow in any case</span>

<span class="cm">// Cheap: single AND — valid ONLY when capacity is a power of 2</span>
<span class="ck">int</span> idx = pos &amp; (capacity - <span class="cn">1</span>);

<span class="cm">// Ring buffer wrap (DPDK-style):</span>
<span class="ck">uint32_t</span> mask = size - <span class="cn">1</span>;       <span class="cm">// pre-computed once at init</span>
head = (head + <span class="cn">1</span>) &amp; mask;       <span class="cm">// wrap head cheaply</span>
tail = (tail + <span class="cn">1</span>) &amp; mask;       <span class="cm">// wrap tail cheaply</span>

<span class="cm">// HASH bucket index (power-of-2 table size):</span>
<span class="ck">uint32_t</span> bucket = hash(key) &amp; (TABLE_SIZE - <span class="cn">1</span>);</div>

<div class="warn">⚠️ <code>x &amp; (n-1)</code> gives wrong results if <code>n</code> is <em>not</em> a power of two. Always validate with <code>assert((n &amp; (n-1)) == 0)</code> at initialisation.</div>

<p class="sep">POPULATION COUNT (HAMMING WEIGHT)</p>

<div class="p-slate">
<h4>Count the number of 1-bits in an integer</h4>
Used in checksums, error correction, set cardinality checks, and cryptography. Hardware instruction on modern CPUs; software fallback uses the divide-and-conquer approach.
</div>

<div class="cb"><span class="cm">// Fastest — single hardware instruction on x86 (SSE4.2+)</span>
<span class="ck">int</span> cnt = <span class="cf">__builtin_popcount</span>(x);     <span class="cm">// C/GCC (32-bit)</span>
<span class="ck">int</span> cnt = <span class="cf">__builtin_popcountll</span>(x);   <span class="cm">// C/GCC (64-bit)</span>
<span class="ck">int</span> cnt = <span class="cf">Integer.bitCount</span>(x);       <span class="cm">// Java</span>

<span class="cm">// Brian Kernighan — O(set bits), no hardware needed</span>
<span class="ck">int</span> <span class="cf">popcount</span>(<span class="co">uint32_t</span> x) {
    <span class="ck">int</span> c = <span class="cn">0</span>;
    <span class="ck">while</span> (x) { x &amp;= x - <span class="cn">1</span>; c++; }    <span class="cm">// clear lowest set bit each iteration</span>
    <span class="ck">return</span> c;
}

<span class="cm">// Parallel popcount — O(log bits), no loop</span>
<span class="co">uint32_t</span> <span class="cf">popcount32</span>(<span class="co">uint32_t</span> x) {
    x = x - ((x &gt;&gt; <span class="cn">1</span>) &amp; <span class="cn">0x55555555</span>);           <span class="cm">// count pairs</span>
    x = (x &amp; <span class="cn">0x33333333</span>) + ((x &gt;&gt; <span class="cn">2</span>) &amp; <span class="cn">0x33333333</span>); <span class="cm">// count nibbles</span>
    x = (x + (x &gt;&gt; <span class="cn">4</span>)) &amp; <span class="cn">0x0F0F0F0F</span>;             <span class="cm">// count bytes</span>
    <span class="ck">return</span> (x * <span class="cn">0x01010101</span>) &gt;&gt; <span class="cn">24</span>;              <span class="cm">// sum all byte counts</span>
}</div>

</div><!-- /t-arith -->

<!-- TAB: Advanced -->
<div id="t-advanced" class="tab-pane">

<p class="sep">BITMASK DP — SUBSETS AND STATE COMPRESSION</p>

<div class="p-violet">
<h4>When to use Bitmask DP</h4>
Bitmask DP represents state as a bitmask where each bit = one element in-or-out. Applicable when N ≤ 20 (so 2<sup>N</sup> states fit in memory). Common problems: TSP, assignment, task scheduling, game states.
</div>

<div class="diagram-box">Pattern:
  dp[mask] = optimal cost/result considering exactly the elements in mask

Transitions:
  For each mask, try adding element i (not yet in mask):
    newmask = mask | (1 &lt;&lt; i)
    dp[newmask] = min/max(dp[newmask], dp[mask] + cost(i))

Base case:  dp[0] = 0
Answer:     dp[(1&lt;&lt;N)-1]  (full set)</div>

<div class="cb"><span class="cm">// Minimum cost to visit all N nodes (TSP-style DP)</span>
<span class="cm">// dp[mask][i] = min cost to visit nodes in mask, ending at node i</span>
<span class="ck">int</span>[][] dp = <span class="ck">new</span> <span class="ck">int</span>[<span class="cn">1</span> &lt;&lt; N][N];
<span class="cm">// Fill with INF:</span>
<span class="ck">for</span> (<span class="ck">int</span>[] row : dp) <span class="cf">Arrays.fill</span>(row, <span class="cn">Integer.MAX_VALUE</span> / <span class="cn">2</span>);
dp[<span class="cn">1</span>][<span class="cn">0</span>] = <span class="cn">0</span>;  <span class="cm">// start at node 0, mask = 0b0001</span>

<span class="ck">for</span> (<span class="ck">int</span> mask = <span class="cn">1</span>; mask &lt; (<span class="cn">1</span> &lt;&lt; N); mask++) {
    <span class="ck">for</span> (<span class="ck">int</span> u = <span class="cn">0</span>; u &lt; N; u++) {
        <span class="ck">if</span> ((mask &amp; (<span class="cn">1</span> &lt;&lt; u)) == <span class="cn">0</span>) <span class="ck">continue</span>;  <span class="cm">// u not in mask</span>
        <span class="ck">for</span> (<span class="ck">int</span> v = <span class="cn">0</span>; v &lt; N; v++) {
            <span class="ck">if</span> ((mask &amp; (<span class="cn">1</span> &lt;&lt; v)) != <span class="cn">0</span>) <span class="ck">continue</span>; <span class="cm">// v already visited</span>
            <span class="ck">int</span> newmask = mask | (<span class="cn">1</span> &lt;&lt; v);
            dp[newmask][v] = <span class="cf">Math.min</span>(dp[newmask][v], dp[mask][u] + dist[u][v]);
        }
    }
}
<span class="cm">// Enumerate subsets of mask in O(3^N) total:</span>
<span class="ck">for</span> (<span class="ck">int</span> sub = mask; sub &gt; <span class="cn">0</span>; sub = (sub - <span class="cn">1</span>) &amp; mask) { <span class="cm">/*..*/</span> }</div>

<p class="sep">SWAR — SIMD WITHIN A REGISTER</p>

<div class="p-blue">
<h4>Process multiple values simultaneously with integer arithmetic</h4>
SWAR packs multiple sub-word values into a single 64-bit register and uses carefully chosen masks to prevent carry-propagation between adjacent logical fields. Enables 8 parallel byte operations with a single integer add.
</div>

<div class="diagram-box">Example: add 1 to each of 8 bytes packed in a uint64_t

64-bit word:  [B7][B6][B5][B4][B3][B2][B1][B0]  (8 bytes)

Naive: requires 8 separate additions
SWAR: use overflow-guard mask to prevent carry from byte N into byte N+1

Mask 0x7F7F7F7F7F7F7F7F:
  Clear the MSB of every byte (guard bit)
  Allows carry within each byte but blocks inter-byte carry propagation</div>

<div class="cb"><span class="co">uint64_t</span> <span class="cf">swar_add1_to_each_byte</span>(<span class="co">uint64_t</span> v) {
    <span class="cm">// Add 1 to each byte field without inter-byte carry</span>
    <span class="co">uint64_t</span> lo = v &amp; <span class="cn">0x7F7F7F7F7F7F7F7FULL</span>;  <span class="cm">// clear MSB of each byte</span>
    lo = lo + <span class="cn">0x0101010101010101ULL</span>;           <span class="cm">// add 1 to each byte (no overflow into guard)</span>
    <span class="co">uint64_t</span> hi = (v ^ lo) &amp; <span class="cn">0x8080808080808080ULL</span>; <span class="cm">// recover original MSBs</span>
    <span class="ck">return</span> lo | hi;
}

<span class="cm">// Population count via SWAR (classic Hacker's Delight)</span>
<span class="co">uint64_t</span> <span class="cf">popcount64_swar</span>(<span class="co">uint64_t</span> x) {
    x = x - ((x &gt;&gt; <span class="cn">1</span>) &amp; <span class="cn">0x5555555555555555ULL</span>);
    x = (x &amp; <span class="cn">0x3333333333333333ULL</span>) + ((x &gt;&gt; <span class="cn">2</span>) &amp; <span class="cn">0x3333333333333333ULL</span>);
    x = (x + (x &gt;&gt; <span class="cn">4</span>)) &amp; <span class="cn">0x0F0F0F0F0F0F0F0FULL</span>;
    <span class="ck">return</span> (x * <span class="cn">0x0101010101010101ULL</span>) &gt;&gt; <span class="cn">56</span>;
}</div>

<div class="note">📌 SWAR is used in high-performance parsers, DPDK, network classification engines, and wherever vectorized operations are needed without SIMD intrinsics. The key discipline: choose masks so the "guard bit" pattern prevents fields from bleeding into each other.</div>

</div><!-- /t-advanced -->

<div class="mod-nav">
  <a href="/learning/dsa/">&#8592; DSA Hub</a>
  <a href="/learning/dsa/dsa-roadmap/">&#8593; DSA Roadmap</a>
  <a href="/learning/dsa/bit-manipulation/systems-problems/">&#9881;&#65039; Systems Problems</a>
  <a href="/learning/dsa/bit-manipulation/debugging/">&#128027; Debugging Guide</a>
  <a class="nb" href="/learning/dsa/bit-manipulation/bit-manipulation-problems/">Practice Problems &#8594;</a>
</div>

<script>
function vt(e,id){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  e.target.classList.add('active');
}
</script>
