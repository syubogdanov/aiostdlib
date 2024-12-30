from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aiostdlib.internal.backports.tomllib import TOMLDecodeError, loads
from aiostdlib.internal.utils.decorators import to_async_if_not
from aiostdlib.internal.utils.typing import SupportsAsyncRead, SupportsRead


if TYPE_CHECKING:
    from collections.abc import Callable


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]


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
    read = to_async_if_not(fp.read)
    bytes_: bytes = await read()

    try:
        string = bytes_.decode()

    except AttributeError:
        detail = "File must be opened in binary mode, e.g. use `open('foo.toml', 'rb')`"
        raise TypeError(detail) from None

    return loads(string, parse_float=parse_float)
