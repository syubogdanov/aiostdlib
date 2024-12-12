from __future__ import annotations

import sys


__all__: list[str] = ["cache"]


if sys.version_info >= (3, 9):
    from functools import cache

else:
    from functools import lru_cache

    cache = lru_cache(maxsize=None)
