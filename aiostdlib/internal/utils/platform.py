from __future__ import annotations

from functools import cache
from platform import system


__all__: list[str] = ["is_windows"]


@cache
def is_windows() -> bool:
    """Check if the platform is `Windows`."""
    return system() == "Windows"
