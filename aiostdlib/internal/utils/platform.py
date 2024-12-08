from __future__ import annotations

from functools import lru_cache
from platform import system


__all__: list[str] = ["is_windows"]


@lru_cache(maxsize=None)
def is_windows() -> bool:
    """Check if the platform is `Windows`."""
    return system() == "Windows"
