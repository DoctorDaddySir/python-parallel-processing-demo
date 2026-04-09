import time
from multiprocessing import Pool, cpu_count
from prime_utils import count_primes_in_range, RANGES

def process_range(r):
    return count_primes_in_range(*r)


def run_multiprocessing(ranges=None):
    if ranges is None:
        ranges = RANGES

    start_time = time.time()

    with Pool(cpu_count()) as pool:
        results = pool.map(process_range, ranges)

    end_time = time.time()
    runtime = end_time - start_time

    return results, runtime


def main() -> None:
    results, runtime = run_multiprocessing()
    print("Multiprocessing results:", results)
    print(f"Multiprocessing runtime: {runtime:.2f} seconds")


if __name__ == "__main__":
    main()