---
title: "C Compilation Process (Deep Dive)"
description: "C Program Compilation Steps (Deep Dive) When we run a C program , we are not directly executing the .c file."
domain: languages
track: c-fundamentals
order: 11
url: /learning/programming-language/c/c-basics/c-compilation-process/
---

# C Program Compilation Steps (Deep Dive)

When we **run a C program**, we are not directly executing the `.c` file.
A **C source file** goes through multiple stages before it becomes an executable.

✅ **Preprocessing → Compilation → Assembling → Linking → Loading/Runtime**

---

## Overall Pipeline

```
main.c
  |
  |  (1) Preprocessor
  v
main.i
  |
  |  (2) Compiler
  v
main.s
  |
  |  (3) Assembler
  v
main.o
  |
  |  (4) Linker (+ libraries)
  v
main (executable)
  |
  |  (5) OS Loader
  v
Running Process (in memory)
```

---

### C Program Build + Run Pipeline Diagram

![C Program Build + Run Pipeline](/assets/diagrams/learning/programming-language/c/c-basics/diagrams/c-compilation-pipeline.svg){:class="diagram-img"}

*Detailed compilation pipeline diagram showing preprocessing, compilation, assembling, linking, static vs dynamic linking.*

---

## 0) Source Code (`.c`)

Example program:

```c
#include <stdio.h>

int x = 10;

int main() {
    printf("Hello %d\n", x);
    return 0;
}
```

---

## 1) Preprocessing (`.c → .i`)

Preprocessor performs **text-based transformations** before compilation.

### What happens?

- expands header files (`#include`)
- replaces macros (`#define`)
- applies conditional compilation (`#if`, `#ifdef`, ...)
- removes comments

### Command

```bash
gcc -E main.c -o main.i
```

### Why useful?

If you suspect macro/header related issues, inspect `main.i`.

---

## 2) Compilation (`.i → .s`)

Compilation converts preprocessed C code into **assembly**.

### Internal stages inside the compiler

1. **Lexical analysis (tokenization)**  
   Converts raw text to tokens like `int`, `main`, `{`, `}`

2. **Parsing**  
   Builds **AST (Abstract Syntax Tree)** using grammar rules

3. **Semantic analysis**  
   Type checking, prototype matching, conversions

4. **Optimization**  
   Examples:
   - constant folding
   - dead code elimination
   - common subexpression elimination
   - function inlining (optional)

5. **Code generation**  
   Converts intermediate representation (IR) to assembly

### Command

```bash
gcc -S main.i -o main.s
```

Output file:
- `main.s` = assembly code

---

## 3) Assembling (`.s → .o`)

Assembler converts assembly into machine code.

### Command

```bash
gcc -c main.s -o main.o
```

Output:
- `main.o` = object file (binary)

### Object file contains

- machine instructions
- symbol table (names of functions/variables)
- relocation info (placeholders for addresses)

Useful tool:
```bash
nm main.o
```

---

## 4) Linking (`.o + libs → executable`)

Linker combines your object files and required libraries to produce final executable.

### Why linking is needed?

Your code may call external functions like `printf()`.
`printf()` is not inside your `main.o` — it is in the C standard library.

So linker resolves:

- undefined symbols
- library references
- final addresses for code & globals

### Command

```bash
gcc main.o -o main
```

---

## Static vs Dynamic Linking

### Dynamic linking (default)

- executable uses shared libraries (`.so` files)
- libraries loaded at runtime

Check:
```bash
ldd ./main
```

### Static linking

- library code gets copied into executable
- bigger executable but no `.so` dependency

```bash
gcc -static main.c -o main
```

---

## 5) OS Loader Stage (Runtime)

When you run:
```bash
./main
```

The OS loader:

- maps executable into memory (text/data/bss)
- maps shared libraries
- creates stack (argv/envp)
- prepares heap region
- jumps to entry point `_start`

Then startup code calls `main()`.

Check entry point:
```bash
readelf -h main | grep Entry
```

---

## Useful gcc option: keep intermediate files

```bash
gcc -save-temps main.c -o main
```

This generates `.i`, `.s`, `.o` files automatically.

---

## Quick Interview Summary

- **Preprocess:** expands headers/macros  
- **Compile:** C → Assembly (AST + IR + optimization)  
- **Assemble:** Assembly → Object (`.o`)  
- **Link:** Objects + libs → Executable  
- **Load:** OS maps memory and starts program (`_start → main`)
