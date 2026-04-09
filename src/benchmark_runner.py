from sequential_demo import run_sequential
from threaded_demo import run_threaded
from multiprocessing_demo import run_multiprocessing
from prime_utils import RANGES



def print_divider():
    print("=" * 72)


def print_intro():
    print_divider()
    print("PYTHON CONCURRENCY BENCHMARK")
    print_divider()
    print("Story:")
    print("We are benchmarking a deliberately CPU-bound workload.")
    print("The workload counts prime numbers across independent numeric ranges.")
    print()
    print("Goal:")
    print("1. Establish a sequential baseline")
    print("2. Test threading for the same CPU-bound workload")
    print("3. Test multiprocessing to achieve true parallelism")
    print()
    print("Expected takeaway:")
    print("- Sequential provides the baseline")
    print("- Threading should provide little or no improvement for CPU-bound work")
    print("- Multiprocessing should perform better by using multiple CPU cores")
    print_divider()
    print()


def print_section(title):
    print_divider()
    print(title)
    print_divider()


def print_results(label, results, runtime):
    print(f"{label} results: {results}")
    print(f"{label} runtime: {runtime:.4f} seconds")
    print()


def print_summary(sequential_time, threaded_time, multiprocessing_time):
    print_divider()
    print("SUMMARY")
    print_divider()

    print(f"Sequential runtime:      {sequential_time:.4f} seconds")
    print(f"Threaded runtime:        {threaded_time:.4f} seconds")
    print(f"Multiprocessing runtime: {multiprocessing_time:.4f} seconds")
    print()

    threaded_delta = threaded_time - sequential_time
    multiprocessing_delta = sequential_time - multiprocessing_time

    if threaded_delta < 0:
        print(f"Threading improvement vs sequential: {-threaded_delta:.4f} seconds faster")
    else:
        print(f"Threading impact vs sequential:      {threaded_delta:.4f} seconds slower")

    if multiprocessing_delta > 0:
        print(f"Multiprocessing improvement:         {multiprocessing_delta:.4f} seconds faster")
    else:
        print(f"Multiprocessing impact:              {-multiprocessing_delta:.4f} seconds slower")

    print()
    print("Interpretation:")
    print("For CPU-bound work in CPython, threading is limited by the GIL,")
    print("so it often fails to provide meaningful speedup.")
    print("Multiprocessing avoids this limitation by using separate processes,")
    print("allowing work to run across multiple CPU cores.")
    print_divider()


def main():
    print_intro()

    print_section("1. SEQUENTIAL BASELINE")
    sequential_results, sequential_time = run_sequential(RANGES)
    print_results("Sequential", sequential_results, sequential_time)

    print_section("2. THREADED EXECUTION")
    threaded_results, threaded_time = run_threaded(RANGES)
    print_results("Threaded", threaded_results, threaded_time)

    print_section("3. MULTIPROCESSING EXECUTION")
    multiprocessing_results, multiprocessing_time = run_multiprocessing(RANGES)
    print_results("Multiprocessing", multiprocessing_results, multiprocessing_time)

    if sequential_results != threaded_results or sequential_results != multiprocessing_results:
        print("Warning: result mismatch detected between execution strategies.")
        return

    print_summary(sequential_time, threaded_time, multiprocessing_time)


if __name__ == "__main__":
    main()