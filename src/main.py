import asyncio

from benchmark_runner import main as run_cpu_benchmark
from io_benchmark_runner import main as run_io_benchmark


def print_divider() -> None:
    print("\n" + "#" * 80)
    print("#" * 80)


def print_header() -> None:
    print_divider()
    print("PYTHON CONCURRENCY BENCHMARK SUITE")
    print_divider()
    print("This project demonstrates how workload type influences concurrency strategy.")
    print()
    print("We compare:")
    print("1. CPU-bound workloads")
    print("   - Sequential execution")
    print("   - Threaded execution")
    print("   - Multiprocessing execution")
    print()
    print("2. I/O-bound workloads")
    print("   - Sequential execution")
    print("   - Threaded execution")
    print("   - Async execution")
    print()
    print("Core takeaway:")
    print("- CPU-bound work benefits from multiprocessing")
    print("- I/O-bound work benefits from threading or async")
    print("- The right concurrency model depends on the bottleneck")
    print_divider()


def print_footer() -> None:
    print_divider()
    print("FINAL TAKEAWAYS")
    print_divider()
    print("1. Sequential execution provides a useful baseline.")
    print("2. For CPU-bound work in CPython, threading is limited by the GIL.")
    print("3. Multiprocessing enables true parallelism across CPU cores.")
    print("4. For I/O-bound work, concurrency improves throughput by overlapping wait time.")
    print("5. Async is especially useful when managing many waiting tasks efficiently.")
    print()
    print("Interview framing:")
    print("When scaling systems, I first identify whether the bottleneck is CPU or I/O.")
    print("That determines whether I reach for multiprocessing, threading, async,")
    print("or a queue-based distributed approach.")
    print_divider()


async def main() -> None:
    print_header()

    print("\n\n>>> RUNNING CPU-BOUND BENCHMARKS\n")
    run_cpu_benchmark()

    print("\n\n>>> RUNNING I/O-BOUND BENCHMARKS\n")
    await run_io_benchmark()

    print_footer()


if __name__ == "__main__":
    asyncio.run(main())