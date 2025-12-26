---
layout: project
title: "Linked List Implementation in C"
description: "A complete implementation of singly and doubly linked lists in C"
---

## Overview

This project implements both singly and doubly linked lists in C, demonstrating fundamental data structure concepts.

## Features

- **Singly Linked List**: Basic linked list with forward traversal
- **Doubly Linked List**: Advanced linked list with bidirectional traversal
- **Operations**: Insert, delete, search, and display
- **Memory Management**: Proper allocation and deallocation

## Code Example

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
```

## How to Use

1. Clone the repository
2. Compile with `gcc -o linked_list linked_list.c`
3. Run with `./linked_list`

## Learning Outcomes

- Understanding pointer concepts
- Memory management in C
- Data structure implementation
- Algorithm design and complexity analysis
