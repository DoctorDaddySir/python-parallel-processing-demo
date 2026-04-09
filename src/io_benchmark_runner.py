import asyncio

from io_utils import IO_TASK_DURATIONS
from io_sequential_demo import run_io_sequential
from io_threaded_demo import run_io_threaded
from io_async_demo import run_io_async


def print_divider():
    print("=" * 72)


def print_intro():
    print_divider()
    print("PYTHON I/O CONCURRENCY BENCHMARK")
    print_divider()
    print("Story:")
    print("We are benchmarking a simulated I/O-bound workload.")
    print("Each task represents a blocking external wait, such as:")
    print("- a file read")
    print("- a database call")
    print("- an external API request")
    print()
    print("Goal:")
    print("1. Establish a sequential baseline")
    print("2. Test threading on an I/O-bound workload")
    print("3. Test async execution on the same workload")
    print()
    print("Expected takeaway:")
    print("- Sequential execution waits for each I/O task one at a time")
    print("- Threading should improve throughput for blocking I/O")
    print("- Async should also perform well by overlapping waiting time")
    print_divider()
    print()


def print_section(title):
    print_divider()
    print(title)
    print_divider()


def print_results(label, results, runtime):
    print(f"{label} runtime: {runtime:.4f} seconds")
    print(f"{label} completed {len(results)} tasks")
    print()


def print_summary(sequential_time, threaded_time, async_time):
    print_divider()
    print("SUMMARY")
    print_divider()

    print(f"Sequential runtime: {sequential_time:.4f} seconds")
    print(f"Threaded runtime:   {threaded_time:.4f} seconds")
    print(f"Async runtime:      {async_time:.4f} seconds")
    print()

    print("Interpretation:")
    print("For I/O-bound work, concurrency helps because the bottleneck is waiting,")
    print("not CPU computation. While one task is waiting, another can make progress.")
    print("That is why threading and async typically outperform sequential execution")
    print("for network, file, and database-heavy workloads.")
    print_divider()


async def main():
    print_intro()

    print_section("1. SEQUENTIAL I/O BASELINE")
    sequential_results, sequential_time = run_io_sequential(IO_TASK_DURATIONS)
    print_results("Sequential", sequential_results, sequential_time)

    print_section("2. THREADED I/O EXECUTION")
    threaded_results, threaded_time = run_io_threaded(IO_TASK_DURATIONS)
    print_results("Threaded", threaded_results, threaded_time)

    print_section("3. ASYNC I/O EXECUTION")
    async_results, async_time = await run_io_async(IO_TASK_DURATIONS)
    print_results("Async", async_results, async_time)

    print_summary(sequential_time, threaded_time, async_time)


if __name__ == "__main__":
    asyncio.run(main())