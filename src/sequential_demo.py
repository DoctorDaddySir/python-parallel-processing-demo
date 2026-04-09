import time
from prime_utils import count_primes_in_range

RANGES = [
    (100_000, 102_000),
    (102_000, 104_000),
    (104_000, 106_000),
    (106_000, 108_000),
]

def main() -> None:
    start_time = time.time()
    results = []
    for start_range, end_range  in RANGES:
        prime_count = count_primes_in_range(start_range, end_range)
        results.append(prime_count)

    end_time = time.time()
    print("Sequential results:", results)
    print(f"Sequential Results Benchmark: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()