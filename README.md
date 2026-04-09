# Python Concurrency Benchmarks

This project demonstrates how different concurrency models in Python behave under **CPU-bound** and **I/O-bound** workloads.

## Purpose

The goal is to show how to select the appropriate scaling strategy based on the nature of the workload:

- CPU-bound → multiprocessing
- I/O-bound → threading or async

---

## What This Project Covers

### CPU-Bound Workload
A deliberately inefficient prime-number computation is used to simulate a CPU-heavy task.

Compared approaches:
- Sequential execution
- Threading (limited by the GIL)
- Multiprocessing (true parallelism)

### I/O-Bound Workload
Simulated I/O tasks (e.g., API calls, file reads) using timed waits.

Compared approaches:
- Sequential execution
- Threading
- Async (asyncio)

---

## Key Takeaways

- Python’s **GIL prevents true parallelism with threads** for CPU-bound work
- **Multiprocessing** enables parallel execution across CPU cores
- For I/O-bound workloads, both **threading and async improve throughput**
- Choosing the right concurrency model depends on identifying the bottleneck

---

## How to Run

From the project root:

```bash
python src/main.py