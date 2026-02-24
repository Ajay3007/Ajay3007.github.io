---
layout: default
title: C Basics
permalink: /learning/programming-language/c/c-basics/
---

# C Basics — Notes + Enhanced Documentation

This documentation is based on my handwritten notes (C basics) and converted into GitHub Pages friendly Markdown.
I have **kept the original depth** and additionally **enhanced each topic** with missing important points,
debugging tips, and interview-friendly clarifications.



---

## Topics

> Tip: Read in order like a short book. Run the examples. Add your own experiments.


<div style="display: grid; gap: 1rem; margin: 2rem 0;">

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/c-compilation-process' | relative_url }}" style="color:#1976d2;text-decoration:none;">C Compilation Process</a></h3>
  <p>The full life of a C program. Preprocessing, Compiler, Assembler, Linker.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/memory-layout' | relative_url }}" style="color:#1976d2;text-decoration:none;">Memory Layout in C</a></h3>
  <p>C program memory segments (text/data/bss/heap/stack), how they grow, and how OS maps memory at runtime.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/pointers' | relative_url }}" style="color:#1976d2;text-decoration:none;">Pointers in C</a></h3>
  <p>Pointer fundamentals, dereferencing, pointer arithmetic, void/NULL pointers, pointer-to-pointer, and common bugs.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/stack-frame' | relative_url }}" style="color:#1976d2;text-decoration:none;">Stack Frame & Call Stack</a></h3>
  <p>Stack frames, call stack execution flow (LIFO), what gets stored per call, and stack overflow causes.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/arrays-and-pointers' | relative_url }}" style="color:#1976d2;text-decoration:none;">Arrays & Pointers</a></h3>
  <p>Array-pointer relation, `[]` equivalence, array decay, `sizeof` behavior, strings, and pointer-to-array.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/multidimensional-arrays' | relative_url }}" style="color:#1976d2;text-decoration:none;">Multidimensional Arrays & Pointers</a></h3>
  <p>2D/3D array memory model (row-major), correct pointer types, address math, and passing arrays to functions.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/pointers-const' | relative_url }}" style="color:#1976d2;text-decoration:none;">Pointers and `const`</a></h3>
  <p>All const combinations (`const int*`, `int* const`, `const int* const`) with rule-based understanding and examples.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/function-pointers' | relative_url }}" style="color:#1976d2;text-decoration:none;">Function Pointers</a></h3>
  <p>Function pointer syntax, callbacks, array of function pointers, and function pointers inside structures.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/dynamic-memory' | relative_url }}" style="color:#1976d2;text-decoration:none;">Dynamic Memory Allocation</a></h3>
  <p>`malloc/calloc/realloc/free`, safe realloc pattern, dynamic arrays, and dynamic 2D allocation methods.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/structures' | relative_url }}" style="color:#1976d2;text-decoration:none;">Structures in C</a></h3>
  <p>Struct usage, dot vs arrow, initialization styles, typedef, passing structs, shallow vs deep copy, self-referential structs.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/padding-packing' | relative_url }}" style="color:#1976d2;text-decoration:none;">Padding, Alignment & Packing</a></h3>
  <p>Structure padding/alignment, minimizing wasted bytes, and packing using GCC attributes / `#pragma pack`.</p>
</div>

<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3><a href="{{ '/learning/programming-language/c/c-basics/pointer-practice' | relative_url }}" style="color:#1976d2;text-decoration:none;">C Pointer Practice</a></h3>
  <p>This document explains pointer, memory, and data structure concepts
using practical C examples.</p>
</div>

</div>

---

<div style="text-align:center;margin-top:2.5rem;">
  <a href="{{ '/learning/programming-language/c' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#1976d2;color:white;text-decoration:none;border-radius:8px;font-weight:600;margin-right:1rem;">← Back to C</a>
  <a href="{{ '/' | relative_url }}" style="display:inline-block;padding:0.75rem 1.5rem;background:#2d3748;color:white;text-decoration:none;border-radius:8px;font-weight:600;">🏠 Home</a>
</div>
