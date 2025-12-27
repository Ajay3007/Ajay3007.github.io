# Basics of Strings (Foundations)

These are must-know before solving problems.

- Mutable vs Immutable (C++: std::string is mutable)

- Character arrays vs string class

- Common operations: length, substring, concatenation, comparison

- ASCII & Unicode basics

## 📘 1. Mutable vs Immutable Strings

In C++:

### ✅ `std::string` is mutable

You can change characters in place.

```cpp
string s = "hello";
s[0] = 'H';   // modifies original string
```

After modification → `"Hello"`

#### ❌ Character arrays are also mutable (as long as not stored in read-only memory)

```cpp
char arr[] = "hello";
arr[1] = 'a'; // works
```

BUT this is NOT allowed:

```cpp
char* s = "hello";  
s[1] = 'a';   // ❌ undefined behavior (string literal is read-only)
```

### 📌 Takeaway

| Type                  | Mutable? | Notes              |
| --------------------- | -------- | ------------------ |
| `std::string`         | ✅ Yes    | Safe, dynamic size |
| `char arr[]`          | ✓ Yes    | Static size        |
| `char* s = "literal"` | ❌ No     | Read-only memory   |

## 📘 2. Character Arrays vs std::string

### 🔷 Character Array (char[])

- Fixed size

- Ends with \0 (null terminator)

- Needs manual handling

```cpp
char name[10] = "Ajay";
```

If you modify without checking size → risk of overflow.

### 🔶 `std::string` (Recommended)

- Dynamically grows

- Supports many operations

- Easier to use

```cpp
string name = "Ajay";
name += " Gupta";
```

### Differences in memory view:

**Char array:**

```cpp
'A' 'j' 'a' 'y' '\0'
```

**`std::string` internals:**

```cpp
size, capacity, pointer → ['A','j','a','y']
```

### 📌 Conclusion:
Use `std::string` unless you specifically need low-level C-style operations.

## 📘 3. Common String Operations

Let's see the most used methods in DSA.

### 🔹 Length

```cpp
string s = "hello";
int len = s.length();  // or s.size()
```

### 🔹 Substring

```cpp
string s = "abcdef";
string sub = s.substr(1, 3);  
// starts at index 1, length 3 → "bcd"
```

### 🔹 Concatenation

```cpp
string a = "Ajay";
string b = "Gupta";
string c = a + " " + b;
```

### 🔹 Comparison

Lexicographical comparison (dictionary order):

```cpp
string a = "apple";
string b = "banana";
if (a < b) cout << "apple comes first";
```

Character comparison uses **ASCII** values.

### 🔹 Search operations
```cpp
string s = "hello world";
int pos = s.find("world");   // returns 6
```

If not found → returns `string::npos`.

### 🔹 Access characters
```cpp
char ch = s[2];
s[3] = 'x';
```

### 📌 std::to_string() — Overview

Converts numeric values to `std::string`

#### 📘 Example: Convert int to string
```cpp
int x = 42;
string s = to_string(x);  
cout << s;   // "42"
```

#### 📘 Example: Using inside concatenation
```cpp
int age = 25;
string info = "Age = " + to_string(age);
cout << info;
```

#### ⚠️ Precision Issue (Important!)

`to_string(double)` always prints 6 decimal places.
```cpp
to_string(3.1) → "3.100000"
```

If you want precise formatting, use:
```cpp
#include <sstream>

stringstream ss;
ss << fixed << setprecision(2) << 3.14159;
string s = ss.str();    // "3.14"
```

### ✅ stringstream

- A general formatting tool

- Converts any type to string

- Allows custom formatting

- Useful for concatenation, parsing, precision control

**Example:**
```cpp
stringstream ss;
ss << "Value = " << 42;
string s = ss.str();
```

#### ✔ Use stringstream when:

- You need precision control

- You need formatting like:

    * padding

    * width

    * hex / oct / binary

- You're converting multiple types in one stream

- **Example:**
```cpp
ss << "x=" << x << ", y=" << y;
```

## 📘 4. ASCII & Unicode Basics
### 🔹 ASCII

- `0–127` values

- C++ char is typically 1 byte

- Useful for lowercase/uppercase checks

```cpp
char c = 'a';
int val = (int)c;   // 97 (ASCII of 'a')
```

Character manipulation using ASCII:

```cpp
char up = c - 32;   // 'a' → 'A'
```

### 🔹 Unicode

Supports all world languages.

**C++ uses:**

- `char16_t` (UTF-16)

- `char32_t` (UTF-32)

- `wstring` (wide strings)

For DSA interviews:
👉 ASCII-based problems are 95% of what you need
👉 Unicode only matters in advanced parsing tasks