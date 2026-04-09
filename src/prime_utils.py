# Test Ranges
RANGES = [
    (100_000, 102_000),
    (102_000, 104_000),
    (104_000, 106_000),
    (106_000, 108_000),
]

def is_prime(n: int) -> bool:
    """
    Deliberately inefficient prime checker for demonstration CPU-bound workloads
    """
    if n<2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def count_primes_in_range(start: int, end: int) -> int:
    """
    Count How many prime numbers exist in half-open interval [start, end)
    """
    count = 0
    for n in range(start, end):
        if is_prime(n):
            count += 1

    return count