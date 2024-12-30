from __future__ import annotations

import re

from typing import TYPE_CHECKING, Any

from aiostdlib.internal.backports.json.src.python313 import scanner
from aiostdlib.internal.backports.typing import Self


if TYPE_CHECKING:
    from collections.abc import Callable


__all__ = ["JSONDecodeError", "JSONDecoder"]

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL

NaN = float("nan")
PosInf = float("inf")
NegInf = float("-inf")


class JSONDecodeError(ValueError):
    """Subclass of `ValueError`.

    See Also
    --------
    * `json.JSONDecodeError`.
    """

    # Note that this exception is used from _json
    def __init__(self: Self, msg: str, doc: str, pos: int) -> None:
        lineno = doc.count("\n", 0, pos) + 1
        colno = pos - doc.rfind("\n", 0, pos)
        errmsg = f"{msg}: line {lineno} column {colno} (char {pos})"
        ValueError.__init__(self, errmsg)
        self.msg = msg
        self.doc = doc
        self.pos = pos
        self.lineno = lineno
        self.colno = colno

    def __reduce__(self: Self) -> tuple[type[Self], tuple[str, str, int]]:
        """Return a `tuple` that can be used to recreate the object when it is pickled."""
        return self.__class__, (self.msg, self.doc, self.pos)


_CONSTANTS = {
    "-Infinity": NegInf,
    "Infinity": PosInf,
    "NaN": NaN,
}


HEXDIGITS = re.compile(r"[0-9A-Fa-f]{4}", FLAGS)
STRINGCHUNK = re.compile(r'(.*?)(["\\\x00-\x1f])', FLAGS)
BACKSLASH = {
    '"': '"', "\\": "\\", "/": "/",
    "b": "\b", "f": "\f", "n": "\n", "r": "\r", "t": "\t",
}

def _decode_uXXXX(s, pos):
    esc = HEXDIGITS.match(s, pos + 1)
    if esc is not None:
        try:
            return int(esc.group(), 16)
        except ValueError:
            pass
    msg = "Invalid \\uXXXX escape"
    raise JSONDecodeError(msg, s, pos)

def scanstring(s, end, strict=True):
    """Scan the string s for a JSON string. End is the index of the
    character in s after the quote that started the JSON string.
    Unescapes all valid JSON string escape sequences and raises ValueError
    on attempt to decode an invalid string. If strict is False then literal
    control characters are allowed in the string.

    Returns a tuple of the decoded string and the index of the character in s
    after the end quote.
    """
    chunks = []
    _append = chunks.append
    begin = end - 1
    while 1:
        chunk = STRINGCHUNK.match(s, end)
        if chunk is None:
            detail = "Unterminated string starting at"
            raise JSONDecodeError(detail, s, begin)
        end = chunk.end()
        content, terminator = chunk.groups()
        # Content is contains zero or more unescaped string characters
        if content:
            _append(content)
        # Terminator is the end of string, a literal control character,
        # or a backslash denoting that an escape sequence follows
        if terminator == '"':
            break
        elif terminator != "\\":
            if strict:
                msg = f"Invalid control character {terminator!r} at"
                raise JSONDecodeError(msg, s, end)
            else:
                _append(terminator)
                continue
        try:
            esc = s[end]
        except IndexError:
            detail = "Unterminated string starting at"
            raise JSONDecodeError(detail,s, begin) from None
        # If not a unicode escape sequence, must be in the lookup table
        if esc != "u":
            try:
                char = BACKSLASH[esc]
            except KeyError:
                msg = f"Invalid \\escape: {esc!r}"
                raise JSONDecodeError(msg, s, end) from None
            end += 1
        else:
            uni = _decode_uXXXX(s, end)
            end += 5
            if 0xd800 <= uni <= 0xdbff and s[end:end + 2] == "\\u":
                uni2 = _decode_uXXXX(s, end + 1)
                if 0xdc00 <= uni2 <= 0xdfff:
                    uni = 0x10000 + (((uni - 0xd800) << 10) | (uni2 - 0xdc00))
                    end += 6
            char = chr(uni)
        _append(char)
    return "".join(chunks), end


WHITESPACE = re.compile(r"[ \t\n\r]*", FLAGS)
WHITESPACE_STR = " \t\n\r"


def JSONObject(s_and_end, strict, scan_once, object_hook, object_pairs_hook,
               memo=None):
    s, end = s_and_end
    pairs = []
    pairs_append = pairs.append
    # Backwards compatibility
    if memo is None:
        memo = {}
    memo_get = memo.setdefault
    # Use a slice to prevent IndexError from being raised, the following
    # check will raise a more specific ValueError if the string is empty
    nextchar = s[end:end + 1]
    # Normally we expect nextchar == '"'
    if nextchar != '"':
        if nextchar in WHITESPACE_STR:
            end = WHITESPACE.match(s, end).end()
            nextchar = s[end:end + 1]
        # Trivial empty object
        if nextchar == "}":
            if object_pairs_hook is not None:
                result = object_pairs_hook(pairs)
                return result, end + 1
            pairs = {}
            if object_hook is not None:
                pairs = object_hook(pairs)
            return pairs, end + 1
        elif nextchar != '"':
            detail = "Expecting property name enclosed in double quotes"
            raise JSONDecodeError(detail, s, end)
    end += 1
    while True:
        key, end = scanstring(s, end, strict)
        key = memo_get(key, key)
        # To skip some function call overhead we optimize the fast paths where
        # the JSON key separator is ": " or just ":".
        if s[end:end + 1] != ":":
            end = WHITESPACE.match(s, end).end()
            if s[end:end + 1] != ":":
                detail = "Expecting ':' delimiter"
                raise JSONDecodeError(detail, s, end)
        end += 1

        try:
            if s[end] in WHITESPACE_STR:
                end += 1
                if s[end] in WHITESPACE_STR:
                    end = WHITESPACE.match(s, end + 1).end()
        except IndexError:
            pass

        try:
            value, end = scan_once(s, end)
        except StopIteration as err:
            detail = "Expecting value"
            raise JSONDecodeError(detail, s, err.value) from None
        pairs_append((key, value))
        try:
            nextchar = s[end]
            if nextchar in WHITESPACE_STR:
                end = WHITESPACE.match(s, end + 1).end()
                nextchar = s[end]
        except IndexError:
            nextchar = ""
        end += 1

        if nextchar == "}":
            break
        elif nextchar != ",":
            detail = "Expecting ',' delimiter"
            raise JSONDecodeError(detail, s, end - 1)
        comma_idx = end - 1
        end = WHITESPACE.match(s, end).end()
        nextchar = s[end:end + 1]
        end += 1
        if nextchar != '"':
            if nextchar == "}":
                detail = "Illegal trailing comma before end of object"
                raise JSONDecodeError(detail, s, comma_idx)
            detail = "Expecting property name enclosed in double quotes"
            raise JSONDecodeError(detail, s, end - 1)
    if object_pairs_hook is not None:
        result = object_pairs_hook(pairs)
        return result, end
    pairs = dict(pairs)
    if object_hook is not None:
        pairs = object_hook(pairs)
    return pairs, end

def JSONArray(s_and_end, scan_once):
    s, end = s_and_end
    values = []
    nextchar = s[end:end + 1]
    if nextchar in WHITESPACE_STR:
        end = WHITESPACE.match(s, end + 1).end()
        nextchar = s[end:end + 1]
    # Look-ahead for trivial empty array
    if nextchar == "]":
        return values, end + 1
    _append = values.append
    while True:
        try:
            value, end = scan_once(s, end)
        except StopIteration as err:
            detail = "Expecting value"
            raise JSONDecodeError(detail, s, err.value) from None
        _append(value)
        nextchar = s[end:end + 1]
        if nextchar in WHITESPACE_STR:
            end = WHITESPACE.match(s, end + 1).end()
            nextchar = s[end:end + 1]
        end += 1
        if nextchar == "]":
            break
        elif nextchar != ",":
            detail = "Expecting ',' delimiter"
            raise JSONDecodeError(detail, s, end - 1)
        comma_idx = end - 1
        try:
            if s[end] in WHITESPACE_STR:
                end += 1
                if s[end] in WHITESPACE_STR:
                    end = WHITESPACE.match(s, end + 1).end()
            nextchar = s[end:end + 1]
        except IndexError:
            pass
        if nextchar == "]":
            detail = "Illegal trailing comma before end of array"
            raise JSONDecodeError(detail, s, comma_idx)

    return values, end


class JSONDecoder:
    """`JSON` decoder.

    See Also
    --------
    * `json.JSONDecoder`
    """

    def __init__(
        self: Self,
        *,
        object_hook: Callable[[dict[str, Any]], Any] | None = None,
        parse_float: Callable[[str], Any] | None = None,
        parse_int: Callable[[str], Any] | None = None,
        parse_constant: Callable[[str], Any] | None = None,
        strict: bool = True,
        object_pairs_hook: Callable[[list[tuple[str, Any]]], Any] | None = None,
    ) -> None:
        """Initialize the `JSONDecoder` instance.

        See Also
        --------
        * `json.JSONDecoder`.
        """
        self.object_hook = object_hook
        self.parse_float = parse_float or float
        self.parse_int = parse_int or int
        self.parse_constant = parse_constant or _CONSTANTS.__getitem__
        self.strict = strict
        self.object_pairs_hook = object_pairs_hook
        self.parse_object = JSONObject
        self.parse_array = JSONArray
        self.parse_string = scanstring
        self.memo = {}
        self.scan_once = scanner.make_scanner(self)

    def decode(self: Self, s: str) -> Any:  # noqa: ANN401
        """Return the Python representation of `s`.

        See Also
        --------
        * `json.JSONDecoder.decode`.
        """
        obj, end = self.raw_decode(s, idx=WHITESPACE.match(s, 0).end())
        end = WHITESPACE.match(s, end).end()

        if end != len(s):
            detail = "Extra data"
            raise JSONDecodeError(detail, s, end)

        return obj

    def raw_decode(self: Self, s: str, idx: int = 0) -> tuple[Any, int]:
        """Return a tuple of Python representation and the end index.

        See Also
        --------
        * `json.JSONDecoder.raw_decode`.
        """
        try:
            obj, end = self.scan_once(s, idx)

        except StopIteration as err:
            detail = "Expecting value"
            raise JSONDecodeError(detail, s, err.value) from None

        return obj, end
