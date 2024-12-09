from __future__ import annotations

from platform import system

from aiostdlib.internal.backports.functools import cache


__all__: list[str] = ["is_windows"]


@cache
def is_windows() -> bool:
    """Check if the platform is `Windows`."""
    return system() == "Windows"
