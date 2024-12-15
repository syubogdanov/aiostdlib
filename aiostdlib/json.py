from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aiostdlib.internal.backports.json import (
    JSONDecodeError,
    JSONDecoder,
    JSONEncoder,
    dumps,
    loads,
)
from aiostdlib.internal.utils.decorators import to_async_if_not
from aiostdlib.internal.utils.typing import (
    SupportsAsyncRead,
    SupportsAsyncWrite,
    SupportsRead,
    SupportsWrite,
)


if TYPE_CHECKING:
    from collections.abc import Callable


__all__: list[str] = [
    "JSONDecodeError",
    "JSONDecoder",
    "JSONEncoder",
    "dump",
    "dumps",
    "load",
    "loads",
]


async def dump(  # noqa: PLR0913
    obj: Any,  # noqa: ANN401
    fp: SupportsAsyncWrite[str] | SupportsWrite[str],
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: int | str | None = None,
    separators: tuple[str, str] | None = None,
    default: Callable[[Any], Any] | None = None,
    sort_keys: bool = False,
    **kwargs: Any,  # noqa: ANN401
) -> None:
    """Serialize `obj` as a `JSON` formatted stream to `fp`.

    Notes
    -----
    * `fp.write` is interpreted as IO-bound.
    """
    if cls is None:
        cls = JSONEncoder

    encoder = cls(
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        indent=indent,
        separators=separators,
        default=default,
        sort_keys=sort_keys,
        **kwargs,
    )

    iterable = encoder.iterencode(obj)
    write = to_async_if_not(fp.write)

    for chunk in iterable:
        await write(chunk)


async def load(
    fp: SupportsAsyncRead[str | bytes] | SupportsRead[str | bytes],
    *,
    cls: type[JSONDecoder] | None = None,
    object_hook: Callable[[dict[Any, Any]], Any] | None = None,
    parse_float: Callable[[str], Any] | None = None,
    parse_int: Callable[[str], Any] | None = None,
    parse_constant: Callable[[str], Any] | None = None,
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] | None = None,
    **kwargs: Any,  # noqa: ANN401
) -> Any:  # noqa: ANN401
    """Deserialize `fp` to a Python object.

    Notes
    -----
    * `fp.read` is interpreted as IO-bound.
    """
    read = to_async_if_not(fp.read)
    contents: str | bytes = await read()

    return loads(
        contents,
        cls=cls,
        object_hook=object_hook,
        parse_float=parse_float,
        parse_int=parse_int,
        parse_constant=parse_constant,
        object_pairs_hook=object_pairs_hook,
        **kwargs,
    )
