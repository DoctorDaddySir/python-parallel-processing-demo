import time
from concurrent.futures import ThreadPoolExecutor
from prime_utils import count_primes_in_range, RANGES


def run_threaded(ranges=None):
    if ranges is None:
        ranges = RANGES

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda r: count_primes_in_range(*r), ranges))

    end_time = time.time()
    runtime = end_time - start_time

    return results, runtime


def main() -> None:
    results, runtime = run_threaded()
    print("Threaded results:", results)
    print(f"Threaded runtime: {runtime:.2f} seconds")


if __name__ == "__main__":
    main()