"""Provides backports for type hints.

Notes
-----
* This is *the only* module in which dynamic imports are allowed.

See Also
--------
* `typing_extensions`.
"""

from __future__ import annotations

import sys


__all__: list[str] = ["ParamSpec", "Self", "TypeAlias"]


if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self
