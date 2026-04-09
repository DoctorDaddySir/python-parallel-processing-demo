import time
from multiprocessing import Pool, cpu_count
from prime_utils import count_primes_in_range

RANGES = [
    (100_000, 102_000),
    (102_000, 104_000),
    (104_000, 106_000),
    (106_000, 108_000),
]


def process_range(r):
    return count_primes_in_range(*r)

def main() -> None:
    start_time = time.time()
    end_time = time.time()
    
    with Pool(cpu_count()) as pool:
        results = pool.map(process_range, RANGES)
        
    print("Multiprocessing results:", results)
    print(f"Multiprocessing Results Benchmark: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()