import os

from functools import cache
from warnings import warn

from aiostdlib.internal.utils.os import cpu_count


@cache
def default_workers_count() -> int:
    """Count the number of workers to use."""
    return min(cpu_count() + 4, 32)


@cache
def workers_count() -> int:
    """Count the number of workers to use.

    Notes
    -----
    * Raises `RuntimeWarning` if `os.environ` variable is broken.
    """
    key = "AIOSTDLIB_CONCURRENT_WORKERS"

    if (var := os.environ.get(key)) is None:
        return default_workers_count()

    try:
        user_limit = int(var)

    except (ValueError, TypeError):
        detail = f"'{key}' is not an integer"
        warn(detail, RuntimeWarning, stacklevel=2)
        return default_workers_count()

    if user_limit < 0:
        detail = f"'{key}' is a negative integer"
        warn(detail, RuntimeWarning, stacklevel=2)
        return default_workers_count()

    return user_limit


@cache
def workers_enabled() -> bool:
    """Check if concurrent workers are enabled."""
    return workers_count() > 0
