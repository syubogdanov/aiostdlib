from __future__ import annotations

from functools import lru_cache


__all__: list[str] = ["cache"]


cache = lru_cache(maxsize=None)
