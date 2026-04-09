import time
from prime_utils import count_primes_in_range, RANGES


def run_sequential(ranges=None):
    if ranges is None:
        ranges = RANGES

    start_time = time.time()

    results = []
    for start_range, end_range in ranges:
        prime_count = count_primes_in_range(start_range, end_range)
        results.append(prime_count)

    end_time = time.time()
    runtime = end_time - start_time

    return results, runtime


def main() -> None:
    results, runtime = run_sequential()
    print("Sequential results:", results)
    print(f"Sequential runtime: {runtime:.2f} seconds")


if __name__ == "__main__":
    main()