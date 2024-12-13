from __future__ import annotations

from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    from collections.abc import Callable


__all__: list[str] = ["TOMLDecodeError", "loads"]


class TOMLDecodeError(ValueError):
    """An error raised if a document is not valid `TOML`."""


def loads(s: str, /, *, parse_float: Callable[[str], Any] = float) -> dict[str, Any]:
    """Parse `TOML` from a string."""
    detail = "'aiostdlib.tomllib' is being developed"
    raise NotImplementedError(detail)
