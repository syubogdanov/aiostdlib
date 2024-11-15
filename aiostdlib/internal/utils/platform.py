from functools import lru_cache
from platform import system


@lru_cache(maxsize=None)
def is_windows() -> bool:
    """Check if the platform is `Windows`."""
    return system() == "Windows"
