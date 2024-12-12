from __future__ import annotations

import sys


__all__: list[str] = ["TOMLDecodeError", "loads"]


if sys.version_info >= (3, 11):
    from tomllib import TOMLDecodeError

else:
    class TOMLDecodeError(ValueError):
        """An error raised if a document is not valid TOML."""


if sys.version_info >= (3, 11):
    from tomllib import loads

else:
    from typing import TYPE_CHECKING, Any


    if TYPE_CHECKING:
        from collections.abc import Callable


    def loads(s: str, /, *, parse_float: Callable[[str], Any] = float) -> dict[str, Any]:
        """Parse `TOML` from a string."""
        detail = "'aiostdlib.tomllib' is being developed"
        raise NotImplementedError(detail)
