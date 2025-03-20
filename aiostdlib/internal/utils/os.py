import os


def cpu_count() -> int:
    """Return the number of logical CPUs in the system.

    Notes
    -----
    * Never returns `None`, unlike `os.cpu_count()`.
    """
    return os.cpu_count() or 1
