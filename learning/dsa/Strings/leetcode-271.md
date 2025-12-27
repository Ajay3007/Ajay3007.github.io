# Leetcode 271. Encode and Decode Strings

Design an algorithm to encode **a list of strings** to **a string**. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```
Machine 2 (receiver) has the function:
```
vector<string> decode(string s) {
  //... your code
  return strs;
}
```
So Machine 1 does:
```
string encoded_string = encode(strs);
```
and Machine 2 does:
```
vector<string> strs2 = decode(encoded_string);
```

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

You are not allowed to solve the problem using any serialize methods (such as `eval`).

**Example 1:**
```
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

**Example 2:**
```
Input: dummy_input = [""]
Output: [""]
```

**Constraints:**

`1 <= strs.length <= 200`
`0 <= strs[i].length <= 200`
`strs[i]` contains any possible characters out of `256` valid ASCII characters.
 

Follow up: Could you write a generalized algorithm to work on any possible set of characters?


# Solution

## Intuition
We need a reversible way to pack a list of arbitrary strings into one string so we can later unpack it exactly.  
A robust approach is to prefix each string with an explicit length field describing how many characters follow; during decoding we read the length first, then read exactly that many characters to recover the original string. This avoids ambiguity caused by characters that could be mistaken for separators.

## Approach
- **Encode:** For every string, compute its length and write a fixed-size binary representation of that length (here 8 bits) followed immediately by the string contents. Concatenate these pairs for all strings to form the encoded string.
- **Decode:** Walk the encoded string from left to right. For each entry read the fixed-size length field (8 characters representing the binary length), convert it back to an integer, then read the next `length` characters as the original string. Repeat until the end of the encoded string.

This scheme is deterministic and unambiguous because every chunk begins with the exact number of bytes that represent the length of the following string.

## Complexity
- Time complexity:  
  Let `n` be number of strings and `L` be the total number of characters across all strings.  
  - **Encode:** O(L + n) — computing lengths and appending each string and its fixed-length header.  
  - **Decode:** O(L + n) — reading each header and extracting each substring.  
  In big-O terms this is **O(L)**.

- Space complexity:  
  - **Encode:** O(L) extra space for the encoded string (plus small fixed overhead per string).  
  - **Decode:** O(L) to store the decoded list of strings (plus O(1) working memory).  
  Overall additional space is **O(L)**.

> **Note:** The current implementation encodes the length using 8 bits (one byte), so it can express lengths from 0..255. If you expect strings longer than 255 characters, increase the header size (e.g., 32 bits) before encoding.

## Code
```cpp
class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        int n = strs.size();
        string enc = "";
        for(int i=0; i<n; i++) {
            int len = strs[i].length();
            bitset<8> bits(len);
            string binaryLen = bits.to_string();
            enc += binaryLen + strs[i];
        }
        return enc;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        int n = s.length();
        int i = 0;
        vector<string> dec;
        while(i<n) {
            string binaryLen = s.substr(i, 8);
            int nextLen = bitset<8>(binaryLen).to_ulong();
            i += 8;
            string curr = s.substr(i, nextLen);
            dec.push_back(curr);
            i += nextLen;
        }
        return dec;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
```