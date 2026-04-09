import time
from io_utils import IO_TASK_DURATIONS, blocking_io_task


def run_io_sequential(task_durations=None):
    if task_durations is None:
        task_durations = IO_TASK_DURATIONS

    start_time = time.time()

    results = []
    for duration in task_durations:
        results.append(blocking_io_task(duration))

    end_time = time.time()
    runtime = end_time - start_time

    return results, runtime


def main() -> None:
    results, runtime = run_io_sequential()
    print("Sequential I/O results:")
    for result in results:
        print(result)
    print(f"Sequential I/O runtime: {runtime:.2f} seconds")


if __name__ == "__main__":
    main()