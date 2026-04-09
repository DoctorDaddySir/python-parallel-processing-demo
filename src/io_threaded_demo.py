import time
from concurrent.futures import ThreadPoolExecutor
from io_utils import IO_TASK_DURATIONS, blocking_io_task


def run_io_threaded(task_durations=None):
    if task_durations is None:
        task_durations = IO_TASK_DURATIONS

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(blocking_io_task, task_durations))

    end_time = time.time()
    runtime = end_time - start_time

    return results, runtime


def main() -> None:
    results, runtime = run_io_threaded()
    print("Threaded I/O results:")
    for result in results:
        print(result)
    print(f"Threaded I/O benchmark: {runtime:.2f} seconds")


if __name__ == "__main__":
    main()