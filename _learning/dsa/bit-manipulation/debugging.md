---
layout: learning
title: "Bit Manipulation — Debugging Guide"
permalink: /learning/dsa/bit-manipulation/debugging/
---
<style>
.mod-header{background:linear-gradient(135deg,#0f0c29 0%,#1a1060 55%,#24243e 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#a78bfa;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c4b5fd;font-size:.95rem;margin-bottom:1rem}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#1a1060;color:#a78bfa;font-family:monospace;font-size:.75rem;font-weight:700;padding:.5rem .7rem;text-align:left;border-bottom:2px solid #2d1b80}
.t-table td{padding:.45rem .7rem;border-bottom:1px solid var(--border-color,#e8e8e8);vertical-align:top;font-family:monospace;font-size:.83rem}
.t-table tr:last-child td{border-bottom:none}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3;white-space:pre-wrap}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
.p-violet{background:#f5f3ff;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-violet h4{margin:0 0 .5rem;font-size:.9rem;font-weight:700}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.ins{background:#e8f5e9;border:1px solid #66bb6a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.3rem 0;font-size:.87rem;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐ ";font-size:1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a1060;color:#fff !important;border-color:#1a1060}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">DSA MASTERY · CH 11 · BIT MANIPULATION · APPENDIX A</div>
  <div class="mod-title">&#128027; Debugging Bit Operations</div>
  <div class="mod-subtitle">Print binary &middot; Common bug checklist &middot; Operator precedence quick reference</div>
</div>
<div style="background:#1a1060;border-radius:0 0 8px 8px;padding:.7rem 1.5rem;color:#a78bfa;font-size:.82rem;font-family:monospace;margin-bottom:2rem;">
  Appendix A &mdash; practical tools and checklists for when your bit operations misbehave
</div>

<p class="sep">A.1 &mdash; PRINT BINARY IN C AND JAVA</p>

<div class="p-violet">
<h4>First step of debugging any bit bug: print what you actually have</h4>
Never guess at bit patterns in your head. Print them. Compare visually.
</div>

<div class="cb"><span class="cm">// C — print binary for any unsigned integer, grouped by nibble</span>
<span class="ck">void</span> <span class="cf">printBits</span>(<span class="co">uint64_t</span> x, <span class="ck">int</span> bits) {
    <span class="ck">for</span> (<span class="ck">int</span> i = bits-<span class="cn">1</span>; i &gt;= <span class="cn">0</span>; i--) {
        <span class="cf">putchar</span>((x &gt;&gt; i) &amp; <span class="cn">1</span> ? <span class="cs">'1'</span> : <span class="cs">'0'</span>);
        <span class="ck">if</span> (i &gt; <span class="cn">0</span> &amp;&amp; i % <span class="cn">4</span> == <span class="cn">0</span>) <span class="cf">putchar</span>(<span class="cs">' '</span>);  <span class="cm">// group by nibble</span>
    }
    <span class="cf">putchar</span>(<span class="cs">'\n'</span>);
}
<span class="cm">// printBits(0xC0A80A05, 32):</span>
<span class="cm">// 1100 0000 1010 1000 0000 1010 0000 0101</span>

<span class="cm">// Alternative: use printf with format string</span>
<span class="cf">printf</span>(<span class="cs">"x = 0x%08X = %u\n"</span>, x, x);  <span class="cm">// hex + decimal</span></div>

<div class="cb"><span class="cm">// Java — print binary</span>
<span class="cf">System.out.println</span>(<span class="cf">Integer.toBinaryString</span>(x));         <span class="cm">// no leading zeros</span>
<span class="cf">System.out.printf</span>(<span class="cs">"%32s%n"</span>, <span class="cf">Integer.toBinaryString</span>(x))
    .replace(<span class="cs">' '</span>, <span class="cs">'0'</span>);                                   <span class="cm">// with leading zeros</span>
<span class="cf">System.out.println</span>(<span class="cf">Integer.toHexString</span>(x));              <span class="cm">// hex</span>
<span class="cf">System.out.println</span>(<span class="cf">Long.toBinaryString</span>(x));              <span class="cm">// 64-bit</span></div>

<div class="ins">&#10003; <strong>Debug workflow:</strong> Print both the mask and the value before ANDing. Print the result. Compare all three side-by-side in binary. The bug is usually immediately obvious visually.</div>

<p class="sep">A.2 &mdash; COMMON BUG CHECKLIST</p>

<table class="t-table">
<thead><tr><th>Bug</th><th>Example of the mistake</th><th>Fix</th></tr></thead>
<tbody>
<tr>
  <td><strong>Missing parentheses</strong></td>
  <td><code>x &amp; mask == 0</code> &mdash; parsed as <code>x &amp; (mask==0)</code></td>
  <td><code>(x &amp; mask) == 0</code></td>
</tr>
<tr>
  <td><strong>Sign extension on ~</strong></td>
  <td><code>~(uint8_t)x</code> gives 32-bit result 0xFFFFFF00</td>
  <td><code>(uint8_t)(~x)</code> &mdash; cast after NOT</td>
</tr>
<tr>
  <td><strong>Shift by &ge; type width</strong></td>
  <td><code>1 &lt;&lt; 32</code> on int &mdash; undefined behaviour</td>
  <td><code>1ULL &lt;&lt; 32</code> or use 64-bit type</td>
</tr>
<tr>
  <td><strong>Signed right shift</strong></td>
  <td><code>signed x &gt;&gt; n</code> fills sign bit (arithmetic)</td>
  <td>Cast to unsigned, or use <code>&gt;&gt;&gt;</code> in Java</td>
</tr>
<tr>
  <td><strong>No ntohs() before mask</strong></td>
  <td>Masking network-order bytes gives wrong fields on x86</td>
  <td>Always <code>ntohs()</code> / <code>ntohl()</code> before masking</td>
</tr>
<tr>
  <td><strong>Align not power of 2</strong></td>
  <td><code>&amp; (align-1)</code> gives garbage if align=7</td>
  <td><code>assert((align &amp; (align-1)) == 0)</code> at init</td>
</tr>
<tr>
  <td><strong>Ring size not pow2</strong></td>
  <td><code>&amp; mask</code> wraps incorrectly</td>
  <td>Enforce <code>nextPow2()</code> at ring creation</td>
</tr>
<tr>
  <td><strong>Bit check vs exact match</strong></td>
  <td><code>if (x &amp; mask)</code> where mask has multiple bits &mdash; checks any, not all</td>
  <td><code>if ((x &amp; mask) == mask)</code> to require all bits set</td>
</tr>
</tbody>
</table>

<div class="warn">&#9888;&#65039; <strong>Most frequent source of bit bugs:</strong> Missing parentheses around bitwise sub-expressions that are compared or combined with logical operators. When in doubt, add parentheses &mdash; they are free.</div>

<p class="sep">A.3 &mdash; OPERATOR PRECEDENCE QUICK REFERENCE (BITWISE CONTEXT)</p>

<div class="diagram-box">Precedence (highest to lowest) &mdash; bitwise operators highlighted:

Priority   | Operator(s)          | Notes
-----------+----------------------+---------------------------------------
Highest    |  ~                   | Bitwise NOT (unary) &mdash; applies first
           |  &lt;&lt;  &gt;&gt;              | Shifts
           |  &amp;                   | Bitwise AND
           |  ^                   | Bitwise XOR
           |  |                   | Bitwise OR
-----------+----------------------+---------------------------------------
 !!! TRAP  |  == != &lt; &gt; &lt;= &gt;=    | Comparisons &mdash; ABOVE &amp; ^ |  &larr; GOTCHA!
-----------+----------------------+---------------------------------------
           |  &amp;&amp;                  | Logical AND
           |  ||                  | Logical OR
Lowest     |  = |= &amp;= ^= &lt;&lt;= &gt;&gt;= | Assignment operators</div>

<table class="t-table">
<thead><tr><th>Expression</th><th>How it parses</th><th>What you meant</th></tr></thead>
<tbody>
<tr><td><code>x &amp; 0xFF == 0</code></td><td><code>x &amp; (0xFF == 0)</code> &mdash; always <code>x &amp; 0</code></td><td><code>(x &amp; 0xFF) == 0</code></td></tr>
<tr><td><code>a | b &gt; 0</code></td><td><code>a | (b &gt; 0)</code> &mdash; adds 0 or 1</td><td><code>(a | b) &gt; 0</code></td></tr>
<tr><td><code>flags &amp; FLAG != 0</code></td><td><code>flags &amp; (FLAG != 0)</code> &mdash; flags &amp; 1</td><td><code>(flags &amp; FLAG) != 0</code></td></tr>
<tr><td><code>a ^ b == c</code></td><td><code>a ^ (b == c)</code> &mdash; XOR with bool</td><td><code>(a ^ b) == c</code></td></tr>
<tr><td><code>~x &amp; mask</code></td><td>OK &mdash; <code>~</code> is highest bitwise</td><td>Fine as-is</td></tr>
<tr><td><code>x &lt;&lt; 2 &amp; mask</code></td><td>OK &mdash; shifts before AND</td><td>Fine as-is</td></tr>
</tbody>
</table>

<div class="ins">&#10003; <strong>Golden rule:</strong> Wrap every bitwise sub-expression in parentheses when the result is used in a comparison or logical expression. The compiler will not warn you; the bug will be silent.</div>

<p class="sep">MASTERY CHECKLIST &mdash; BEFORE YOU SHIP BIT CODE</p>

<ul class="cl">
  <li>All bitwise expressions mixed with comparisons have explicit parentheses</li>
  <li>NOT (~) on sub-int types is followed by an explicit cast back to the target type</li>
  <li>Shift amounts are &lt; the width of the type (use ULL literals for 64-bit shifts)</li>
  <li>Signed types use &gt;&gt;&gt; (Java) or explicit cast to unsigned (C) where logical shift needed</li>
  <li>All multi-byte network fields are converted with ntohs()/ntohl() before masking</li>
  <li>Alignment values are validated to be powers of 2 at initialisation</li>
  <li>Ring/hash table sizes are enforced to be powers of 2 before using &amp;mask trick</li>
  <li>Printed binary representation validates every intermediate mask value</li>
</ul>

<div class="mod-nav">
  <a href="{{ '/learning/dsa/bit-manipulation/' | relative_url }}">&#8592; Bit Manipulation</a>
  <a href="{{ '/learning/dsa/bit-manipulation/systems-problems/' | relative_url }}">&#9881;&#65039; Systems Problems</a>
  <a class="nb" href="{{ '/learning/dsa/bit-manipulation/bit-manipulation-problems/' | relative_url }}">Practice Problems &#8594;</a>
</div>
