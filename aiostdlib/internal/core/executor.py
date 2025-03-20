from concurrent.futures import Executor, ThreadPoolExecutor
from functools import cache

from aiostdlib.internal.core.workers import workers_count


@cache
def get_thread_executor() -> Executor:
    """Get the `aiostdlib` executor.

    Notes
    -----
    * Use `functools.cache` to imitate a singleton pattern.
    """
    return ThreadPoolExecutor(workers_count())
