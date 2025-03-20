from __future__ import annotations

from typing import TYPE_CHECKING, Any

from backlib.py313.tomllib import TOMLDecodeError, loads

from aiostdlib.internal.core.asyncio import maybe_awaitify


if TYPE_CHECKING:
    from collections.abc import Callable

    from aiostdlib.internal.utils.typing import SupportsAsyncRead, SupportsRead


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]

__aiostdlib__: str = "aiostdlib.tomllib"


async def load(
    fp: SupportsAsyncRead[bytes] | SupportsRead[bytes],
    /,
    *,
    parse_float: Callable[[str], Any] = float,
) -> dict[str, Any]:
    """Read a `TOML` file.

    Notes
    -----
    * `fp.read` is interpreted as IO-bound.

    See Also
    --------
    * `tomllib.load`.
    """
    read = maybe_awaitify(fp.read)
    bytes_: bytes = await read()

    try:
        string = bytes_.decode()

    except AttributeError:
        detail = "File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')`"
        raise TypeError(detail) from None

    return loads(string, parse_float=parse_float)


load.__module__ = __aiostdlib__
