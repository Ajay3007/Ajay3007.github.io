# C++ Concepts Explained Using FTP PCAP Analyzer Project

This document explains important C++ concepts used in the FTP PCAP Analyzer project with simple theory, examples, and references to real code.

---

## 1. `struct` – Custom Data Types

### Theory

`struct` is used to create your own data type that groups multiple variables.

### From Project

```cpp
struct Segment {
    uint32_t seq;
    std::vector<uint8_t> data;
};
```

### Explanation

* `Segment` groups TCP sequence number and data.
* Helps represent one TCP packet.

### Why Needed

To store packet information together.

---

## 2. `std::vector` – Dynamic Array

### Theory

`vector` is a resizable array.

### From Project

```cpp
std::vector<Segment>
```

### Explanation

* Stores multiple `Segment` objects.
* Grows automatically.

### Why Needed

We don’t know number of packets in advance.

---

## 3. `std::map` – Key-Value Storage

### Theory

`map` stores data as key → value pairs in sorted order.

### From Project

```cpp
std::map<ConnKey, std::vector<Segment>> sessions;
```

### Explanation

* Key = connection info
* Value = packets for that connection

### Why Needed

To separate multiple TCP connections.

---

## 4. Operator Overloading (`operator<`)

### Theory

Defines how objects are compared.

### From Project

```cpp
bool operator<(const ConnKey& o) const
```

### Explanation

Tells C++ how to compare two connections.

### Why Needed

Required by `std::map`.

---

## 5. References (`&`)

### Theory

A reference is another name for the same variable.

### From Project

```cpp
const ConnKey& o
```

### Explanation

Avoids copying objects.

### Why Needed

Improves performance.

---

## 6. `const` Keyword

### Theory

Prevents modification.

### From Project

```cpp
bool operator<(...) const
```

### Explanation

Guarantees no data change.

---

## 7. Pointers (`*`)

### Theory

Stores memory address.

### From Project

```cpp
const u_char* packet
```

### Explanation

Points to raw packet bytes.

---

## 8. Type Casting

### Theory

Converts one type to another.

### From Project

```cpp
auto ip = (struct ip*)net;
```

### Explanation

Treats raw bytes as IP header.

---

## 9. `auto` Keyword

### Theory

Lets compiler infer type.

### From Project

```cpp
auto tcp = (struct tcphdr*)net;
```

---

## 10. Header Files (`.h`)

### Theory

Used to declare classes/functions.

### From Project

```cpp
#include "pcap_reader.h"
```

---

## 11. Separate Compilation

### Theory

Code is split into multiple files.

### From Project

```
pcap_reader.cpp + pcap_reader.h
```

---

## 12. Namespaces (`std::`)

### Theory

Prevents name conflicts.

### From Project

```cpp
std::map
std::vector
```

---

## 13. File I/O (`ofstream`)

### Theory

Used to write files.

### From Project

```cpp
std::ofstream out(outfile, std::ios::binary);
```

---

## 14. Sorting (`std::sort`)

### Theory

Sorts container elements.

### From Project

```cpp
std::sort(data.begin(), data.end(), ...);
```

---

## 15. Lambda Functions

### Theory

Inline anonymous functions.

### From Project

```cpp
[](auto& a, auto& b) { return a.seq < b.seq; }
```

---

## 16. Command Line Arguments (`argc`, `argv`)

### Theory

Used to get input from terminal.

### From Project

```cpp
int main(int argc, char* argv[])
```

---

## 17. Error Handling (Return Values)

### Theory

Functions return success/failure.

### From Project

```cpp
if (!handle) return false;
```

---

## 18. CMake Build System

### Theory

Automates compilation.

### From Project

```cmake
add_executable(...)
```

---

## 19. Library Linking

### Theory

Connects external libraries.

### From Project

```cmake
target_link_libraries(...)
```

---

## 20. Modular Design

### Theory

Split code by responsibility.

### From Project

* PcapReader → Parsing
* TCPReassembly → Rebuild
* FTPParser → Protocol

---

## Regular Expressions (std::regex) – Parsing FTP PASV Response

### Theory

`std::regex` is used to search text using patterns.

It helps extract structured information from strings.

### From Project

```cpp
regex r("\\((\\d+),(\\d+),(\\d+),(\\d+),(\\d+),(\\d+)\\)");
smatch m;

if (regex_search(s, m, r)) {

    int p1 = stoi(m[5]);
    int p2 = stoi(m[6]);

    port = p1 * 256 + p2;

    return true;
}
```

### Explanation

FTP PASV response looks like:

```bash
227 Entering Passive Mode (192,168,1,5,32,144)
```

The regex matches:

```bash
(number,number,number,number,number,number)
```

Each (\\d+) captures one number.

#### Match Result (smatch)

After matching:

```bash
m[0] → full match
m[1] → first number
...
m[5] → fifth number
m[6] → sixth number
```

#### stoi()

Converts string to integer.

```bash
"32" → 32
```

#### Port Calculation

FTP defines data port as:

```cpp
port = p1 * 256 + p2
```

**Example:**

```
32*256 + 144 = 8336
```

### Why Needed

Without parsing PASV response:

- Data port is unknown

- File packets cannot be captured

- Reconstruction fails

So regex is essential for FTP analysis.

---

## Sorting TCP Segments Using std::sort and Lambda Functions

### Theory

TCP packets may arrive out of order.

To reconstruct a file, packets must be sorted using their sequence numbers.

C++ provides `std::sort` with custom comparison functions.

---

### From Project

```cpp
auto& vec =
    tcp_streams.begin()->second;

sort(vec.begin(), vec.end(),
     [](auto& a, auto& b) {
         return a.seq < b.seq;
     });
```

#### Step 1: Access First Session

```cpp
tcp_streams.begin()->second
```

- `begin()` → first map element

- `second` → value (`vector<Segment>`)

Gets packet list of first connection.

#### Step 2: Reference with auto&

```cpp
auto& vec = ...
```

- `auto` → compiler infers type

- `&` → reference (no copy)

Ensures sorting affects original vector.

#### Step 3: std::sort

```cpp
sort(vec.begin(), vec.end(), comparator);
```

Sorts elements in range.

#### Step 4: Lambda Comparator

```cpp
[](auto& a, auto& b) {
    return a.seq < b.seq;
}
```

- Defines comparison rule.

- Returns `true` if a should come before b.

Here: smaller sequence first.

### Why Needed in Project

TCP packets may be received out of order.

Sorting ensures:

- Correct byte order

- Valid file reconstruction

- No corruption

Without sorting, output file is invalid.

---

## Reading Packets from PCAP Using pcap_next_ex

### Theory

libpcap provides `pcap_next_ex()` to read packets one by one from a capture file or live interface.

Each call returns:

- Packet metadata (header)
- Packet raw bytes (packet)

---

### From Project

```cpp
struct pcap_pkthdr* header;
const u_char* packet;

int ret;

while ((ret = pcap_next_ex(
            handle,
            &header,
            &packet)) >= 0) {

    handlePacket(packet,
                 header->caplen);
}

pcap_close(handle);
```

#### Step 1: Declare Packet Holders

```cpp
struct pcap_pkthdr* header;
const u_char* packet;
```

- `header` → packet metadata

- `packet` → raw bytes

#### Step 2: Call pcap_next_ex

```cpp
ret = pcap_next_ex(handle, &header, &packet);
```

- Reads next packet.

**Return values:**

**Value ->	Meaning**
- 1	-> Packet read
- 0	->Timeout
- -1 ->	Error
- -2 ->	End of file

#### Step 3: Loop Condition
```cpp
while (ret >= 0)
```

- Continues until error or end of file.

#### Step 4: Process Packet

```cpp
handlePacket(packet, header->caplen);
```

- Passes packet data and captured length to parser.

- Uses caplen to avoid reading invalid bytes.

#### Step 5: Close Handle

```cpp
pcap_close(handle);
```

- Releases file and memory resources.

- Prevents memory leaks.

---

## Summary

This project demonstrates practical use of core C++ concepts in a real networking tool:

* Data structures
* Memory handling
* STL containers
* Modular design
* Build systems
* Low-level parsing

Understanding these concepts enables building scalable system software.
