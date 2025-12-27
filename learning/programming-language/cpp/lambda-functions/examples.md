# Lambda Examples (Runnable C++ files)

This folder contains simple, runnable C++ example programs that accompany the `lambda.md` tutorial.

## Example Source Files and Purpose

- [test_main.cpp](./test_main.cpp) `test_main.cpp` - demonstrate syntax uses of lambda function
- [sort_by_length.cpp](./sort_by_length.cpp) `sort_by_length.cpp` — sort strings by length using a lambda comparator.
- [transform_squares.cpp](./transform_squares.cpp) `transform_squares.cpp` — use `std::transform` with a generic lambda to compute squares.
- [move_capture_thread.cpp](./move_capture_thread.cpp) `move_capture_thread.cpp` — demonstrate move-capture of `std::unique_ptr` into a lambda used by `std::thread`.
- [counter_lambda.cpp](./counter_lambda.cpp) `counter_lambda.cpp` — a function returning a lambda that keeps an internal counter (closure state).


## Build & Run (Linux / macOS / WSL)
Compile each example with `g++` (GNU C++ compiler) and run:

```bash
g++ -std=c++17 test_main.cpp -o test_main
./test_main

g++ -std=c++17 sort_by_length.cpp -o sort_by_length
./sort_by_length

g++ -std=c++17 transform_squares.cpp -o transform_squares
./transform_squares

g++ -std=c++17 move_capture_thread.cpp -pthread -o move_capture_thread
./move_capture_thread

g++ -std=c++17 counter_lambda.cpp -o counter_lambda
./counter_lambda
```

Notes:
- For `move_capture_thread.cpp` you need to link with pthread (`-pthread`).
- All examples use modern C++ and should compile with `-std=c++17` or later.

