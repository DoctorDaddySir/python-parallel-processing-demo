import asyncio
import time
from io_utils import IO_TASK_DURATIONS, async_io_task


async def run_io_async(task_durations=None):
    if task_durations is None:
        task_durations = IO_TASK_DURATIONS

    start_time = time.time()

    tasks = [async_io_task(duration) for duration in task_durations]
    results = await asyncio.gather(*tasks)

    end_time = time.time()
    runtime = end_time - start_time

    return results, runtime


async def main() -> None:
    results, runtime = await run_io_async()
    print("Async I/O results:")
    for result in results:
        print(result)
    print(f"Async I/O benchmark: {runtime:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())