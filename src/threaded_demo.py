import time
from concurrent.futures import ThreadPoolExecutor
from prime_utils import count_primes_in_range


RANGES = [
    (100_000, 102_000),
    (102_000, 104_000),
    (104_000, 106_000),
    (106_000, 108_000),
]


def main() -> None:
    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(
            executor.map(lambda r: count_primes_in_range(*r), RANGES)
        )

    end_time = time.time()

    print("Threaded results:", results)
    print(f"Threaded runtime: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()