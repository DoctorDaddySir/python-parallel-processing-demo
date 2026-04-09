import asyncio
import time

IO_TASK_DURATIONS = [1.0, 1.2, 0.8, 1.1, 0.9, 1.3]


def blocking_io_task(duration: float) -> str:
    """
    Simulate a blocking I/O operation, like waiting on a file read, database query, or external API call.
    """
    time.sleep(duration)
    return f"Completer Blocking I/O task in {duration:.1f} seconds"

async def async_io_task(duration: float) -> str:
    """
    Simulate a non-blocking async I/O operation
    """
    await asyncio.sleep(duration)
    return f"Completed async I/O task in {duration:.1f} seconds"