from __future__ import annotations

import sys


__all__: list[str] = ["ParamSpec", "Self", "TypeAlias"]


if sys.version_info >= (3, 10):
    from typing import ParamSpec, TypeAlias
else:
    from typing_extensions import ParamSpec, TypeAlias


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self
