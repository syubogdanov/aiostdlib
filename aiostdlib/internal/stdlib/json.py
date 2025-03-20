from __future__ import annotations

from typing import TYPE_CHECKING, Any

from backlib.py313.json import JSONDecodeError, JSONDecoder, JSONEncoder, dumps, loads

from aiostdlib.internal.core.asyncio import maybe_awaitify


if TYPE_CHECKING:
    from collections.abc import Callable

    from aiostdlib.internal.utils.typing import (
        AnyStr,
        SupportsAsyncRead,
        SupportsAsyncWrite,
        SupportsRead,
        SupportsWrite,
    )


__all__: list[str] = [
    "JSONDecodeError",
    "JSONDecoder",
    "JSONEncoder",
    "dump",
    "dumps",
    "load",
    "loads",
]

__aiostdlib__: str = "aiostdlib.json"


async def dump(
    obj: Any,
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
    **kwargs: Any,
) -> None:
    """Serialize `obj` as a `JSON` formatted stream to `fp`.

    Notes
    -----
    * `fp.write` is interpreted as IO-bound.

    See Also
    --------
    * `json.dump`.
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

    iterator = encoder.iterencode(obj)
    write = maybe_awaitify(fp.write)

    for chunk in iterator:
        await write(chunk)


async def load(
    fp: SupportsAsyncRead[AnyStr] | SupportsRead[AnyStr],
    *,
    cls: type[JSONDecoder] | None = None,
    object_hook: Callable[[dict[Any, Any]], Any] | None = None,
    parse_float: Callable[[str], Any] | None = None,
    parse_int: Callable[[str], Any] | None = None,
    parse_constant: Callable[[str], Any] | None = None,
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] | None = None,
    **kwargs: Any,
) -> Any:
    """Deserialize `fp` to a Python object.

    Notes
    -----
    * `fp.read` is interpreted as IO-bound.

    See Also
    --------
    * `json.load`.
    """
    read = maybe_awaitify(fp.read)
    contents: AnyStr = await read()

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


dump.__module__ = __aiostdlib__
load.__module__ = __aiostdlib__
