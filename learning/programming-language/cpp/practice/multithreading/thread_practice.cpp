
/*
 * thread_practice.cpp
 * C++ Multithreading Practice Pack (Interview Oriented)
 *
 * Topics:
 * - std::thread
 * - mutex / lock_guard
 * - race condition
 * - atomic
 * - condition_variable
 * - producer-consumer
 * - thread pool (basic)
 * - false sharing demo
 *
 * Compile:
 *   g++ -std=c++17 -O0 -g thread_practice.cpp -o thread_practice -pthread
 *
 * Run:
 *   ./thread_practice
 */

#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <atomic>
#include <queue>
#include <condition_variable>
#include <chrono>
#include <functional>

using namespace std;

/* ============================================================
 * TASK 1: Basic Thread Creation
 * ============================================================ */

void worker(int id) {
    cout << "Thread " << id << " running" << endl;
}

void task1_basic_threads() {
    cout << "\n[TASK 1] Basic Thread Creation\n";

    thread t1(worker, 1);
    thread t2(worker, 2);
    thread t3(worker, 3);

    t1.join();
    t2.join();
    t3.join();
}

/* ============================================================
 * TASK 2: Race Condition Demo (No Lock vs Lock)
 * ============================================================ */

int counter = 0;
mutex counter_mtx;

void inc_no_lock() {
    for (int i = 0; i < 1000000; i++)
        counter++;
}

void inc_with_lock() {
    for (int i = 0; i < 1000000; i++) {
        lock_guard<mutex> lg(counter_mtx);
        counter++;
    }
}

void task2_race_condition() {
    cout << "\n[TASK 2] Race Condition Demo\n";

    vector<thread> v;

    counter = 0;
    v.clear();

    for (int i = 0; i < 10; i++)
        v.emplace_back(inc_no_lock);

    for (auto &t : v)
        t.join();

    cout << "No Lock Counter = " << counter << endl;

    counter = 0;
    v.clear();

    for (int i = 0; i < 10; i++)
        v.emplace_back(inc_with_lock);

    for (auto &t : v)
        t.join();

    cout << "With Lock Counter = " << counter << endl;
}

/* ============================================================
 * TASK 3: Atomic Counter (Lock-Free)
 * ============================================================ */

atomic<int> acnt{0};

void inc_atomic() {
    for (int i = 0; i < 1000000; i++)
        acnt.fetch_add(1, memory_order_relaxed);
}

void task3_atomic() {
    cout << "\n[TASK 3] Atomic Counter\n";

    vector<thread> v;
    acnt = 0;

    for (int i = 0; i < 10; i++)
        v.emplace_back(inc_atomic);

    for (auto &t : v)
        t.join();

    cout << "Atomic Counter = " << acnt << endl;
}

/* ============================================================
 * TASK 4: Producer-Consumer (Condition Variable)
 * ============================================================ */

queue<int> q;
mutex q_mtx;
condition_variable cv;

const int MAX_Q_SIZE = 5;
bool done = false;

void producer() {
    for (int i = 1; i <= 20; i++) {
        unique_lock<mutex> ul(q_mtx);

        cv.wait(ul, [] { return q.size() < MAX_Q_SIZE; });

        q.push(i);
        cout << "Produced: " << i << endl;

        ul.unlock();
        cv.notify_all();

        this_thread::sleep_for(chrono::milliseconds(100));
    }

    unique_lock<mutex> ul(q_mtx);
    done = true;
    ul.unlock();
    cv.notify_all();
}

void consumer() {
    while (true) {
        unique_lock<mutex> ul(q_mtx);

        cv.wait(ul, [] { return !q.empty() || done; });

        if (q.empty() && done)
            break;

        int val = q.front();
        q.pop();

        cout << "Consumed: " << val << endl;

        ul.unlock();
        cv.notify_all();
    }
}

void task4_producer_consumer() {
    cout << "\n[TASK 4] Producer Consumer\n";

    done = false;

    thread p(producer);
    thread c(consumer);

    p.join();
    c.join();
}

/* ============================================================
 * TASK 5: Simple Thread Pool
 * ============================================================ */

class ThreadPool {
private:
    vector<thread> workers;
    queue<function<void()>> tasks;

    mutex pool_mtx;
    condition_variable pool_cv;
    bool stop;

public:
    ThreadPool(int n) : stop(false) {
        for (int i = 0; i < n; i++) {
            workers.emplace_back([this] {
                while (true) {
                    function<void()> task;

                    {
                        unique_lock<mutex> ul(pool_mtx);

                        pool_cv.wait(ul, [this] {
                            return stop || !tasks.empty();
                        });

                        if (stop && tasks.empty())
                            return;

                        task = move(tasks.front());
                        tasks.pop();
                    }

                    task();
                }
            });
        }
    }

    void enqueue(function<void()> f) {
        {
            unique_lock<mutex> ul(pool_mtx);
            tasks.push(move(f));
        }
        pool_cv.notify_one();
    }

    ~ThreadPool() {
        {
            unique_lock<mutex> ul(pool_mtx);
            stop = true;
        }

        pool_cv.notify_all();

        for (auto &t : workers)
            t.join();
    }
};

void task5_thread_pool() {
    cout << "\n[TASK 5] Thread Pool\n";

    ThreadPool pool(4);

    for (int i = 1; i <= 8; i++) {
        pool.enqueue([i] {
            cout << "Task " << i
                 << " executed by thread "
                 << this_thread::get_id() << endl;

            this_thread::sleep_for(chrono::milliseconds(200));
        });
    }
}

/* ============================================================
 * TASK 6: False Sharing Demo
 * ============================================================ */

struct BadCounter {
    atomic<long> a;
    atomic<long> b;
};

struct GoodCounter {
    alignas(64) atomic<long> a;
    alignas(64) atomic<long> b;
};

void task6_false_sharing() {
    cout << "\n[TASK 6] False Sharing Demo\n";

    BadCounter bad;
    bad.a = 0;
    bad.b = 0;

    GoodCounter good;
    good.a = 0;
    good.b = 0;

    auto run_bad = [&] {
        auto start = chrono::high_resolution_clock::now();

        thread t1([&] {
            for (int i = 0; i < 100000000; i++)
                bad.a++;
        });

        thread t2([&] {
            for (int i = 0; i < 100000000; i++)
                bad.b++;
        });

        t1.join();
        t2.join();

        auto end = chrono::high_resolution_clock::now();
        cout << "Bad Counter Time: "
             << chrono::duration_cast<chrono::milliseconds>(end - start).count()
             << " ms\n";
    };

    auto run_good = [&] {
        auto start = chrono::high_resolution_clock::now();

        thread t1([&] {
            for (int i = 0; i < 100000000; i++)
                good.a++;
        });

        thread t2([&] {
            for (int i = 0; i < 100000000; i++)
                good.b++;
        });

        t1.join();
        t2.join();

        auto end = chrono::high_resolution_clock::now();
        cout << "Good Counter Time: "
             << chrono::duration_cast<chrono::milliseconds>(end - start).count()
             << " ms\n";
    };

    run_bad();
    run_good();
}

/* ============================================================
 * MAIN
 * ============================================================ */

int main() {
    cout << "=== C++ MULTITHREADING PRACTICE PACK ===\n";

    task1_basic_threads();
    task2_race_condition();
    task3_atomic();
    task4_producer_consumer();
    task5_thread_pool();
    task6_false_sharing();

    cout << "\n=== DONE ===\n";

    return 0;
}
