from __future__ import annotations

import codecs

from typing import TYPE_CHECKING, Any

from aiostdlib.internal.backports.json.src.python313.decoder import JSONDecodeError, JSONDecoder
from aiostdlib.internal.backports.json.src.python313.encoder import JSONEncoder


if TYPE_CHECKING:
    from collections.abc import Callable


__author__ = "Bob Ippolito <bob@redivi.com>"
__version__ = "2.0.9"

__all__ = [
    "JSONDecodeError",
    "JSONDecoder",
    "JSONEncoder",
    "dump",
    "dumps",
    "load",
    "loads",
]


_default_encoder = JSONEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    separators=None,
    default=None,
)


def dumps(  # noqa: PLR0913
    obj: Any,  # noqa: ANN401
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: type[JSONEncoder] | None = None,
    indent: None | int | str = None,
    separators: tuple[str, str] | None = None,
    default: Callable[[Any], Any] | None = None,
    sort_keys: bool = False,
    **kw: Any,  # noqa: ANN401
) -> str:
    """Serialize `obj` to a `JSON` formatted `str`.

    See Also
    --------
    * `json.dumps`.
    """
    # cached encoder
    if (not skipkeys and ensure_ascii and
        check_circular and allow_nan and
        cls is None and indent is None and separators is None and
        default is None and not sort_keys and not kw):
        return _default_encoder.encode(obj)
    if cls is None:
        cls = JSONEncoder
    return cls(
        skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        separators=separators, default=default, sort_keys=sort_keys,
        **kw).encode(obj)


_default_decoder = JSONDecoder(object_hook=None, object_pairs_hook=None)


def detect_encoding(b):
    bstartswith = b.startswith
    if bstartswith((codecs.BOM_UTF32_BE, codecs.BOM_UTF32_LE)):
        return "utf-32"
    if bstartswith((codecs.BOM_UTF16_BE, codecs.BOM_UTF16_LE)):
        return "utf-16"
    if bstartswith(codecs.BOM_UTF8):
        return "utf-8-sig"

    if len(b) >= 4:
        if not b[0]:
            # 00 00 -- -- - utf-32-be
            # 00 XX -- -- - utf-16-be
            return "utf-16-be" if b[1] else "utf-32-be"
        if not b[1]:
            # XX 00 00 00 - utf-32-le
            # XX 00 00 XX - utf-16-le
            # XX 00 XX -- - utf-16-le
            return "utf-16-le" if b[2] or b[3] else "utf-32-le"
    elif len(b) == 2:
        if not b[0]:
            # 00 XX - utf-16-be
            return "utf-16-be"
        if not b[1]:
            # XX 00 - utf-16-le
            return "utf-16-le"
    # default
    return "utf-8"


def loads(  # noqa: C901
    s: str | bytes | bytearray,
    *,
    cls: type[JSONDecoder] | None = None,
    object_hook: Callable[[dict[Any, Any]], Any] | None = None,
    parse_float: Callable[[str], Any] | None = None,
    parse_int: Callable[[str], Any] | None = None,
    parse_constant: Callable[[str], Any] | None = None,
    object_pairs_hook: Callable[[list[tuple[Any, Any]]], Any] | None = None,
    **kw: Any,  # noqa: ANN401
) -> Any:  # noqa: ANN401
    """Deserialize `s` to a Python object.

    See Also
    --------
    * `json.loads`.
    """
    if isinstance(s, str):
        if s.startswith("\ufeff"):
            detail = "Unexpected UTF-8 BOM (decode using utf-8-sig)"
            raise JSONDecodeError(detail, s, 0)
    else:
        if not isinstance(s, (bytes, bytearray)):
            raise TypeError(f"the JSON object must be str, bytes or bytearray, "
                            f"not {s.__class__.__name__}")
        s = s.decode(detect_encoding(s), "surrogatepass")

    if (cls is None and object_hook is None and
            parse_int is None and parse_float is None and
            parse_constant is None and object_pairs_hook is None and not kw):
        return _default_decoder.decode(s)
    if cls is None:
        cls = JSONDecoder
    if object_hook is not None:
        kw["object_hook"] = object_hook
    if object_pairs_hook is not None:
        kw["object_pairs_hook"] = object_pairs_hook
    if parse_float is not None:
        kw["parse_float"] = parse_float
    if parse_int is not None:
        kw["parse_int"] = parse_int
    if parse_constant is not None:
        kw["parse_constant"] = parse_constant
    return cls(**kw).decode(s)
