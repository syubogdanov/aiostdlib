from aiostdlib.internal.backports.io import (
    DEFAULT_BUFFER_SIZE,
    BlockingIOError,  # noqa: A004
    UnsupportedOperation,
    text_encoding,
)
from aiostdlib.internal.impl.io import (
    BufferedIOBase,
    BufferedRandom,
    BufferedReader,
    BufferedRWPair,
    BufferedWriter,
    BytesIO,
    FileIO,
    IncrementalNewlineDecoder,
    IOBase,
    RawIOBase,
    StringIO,
    TextIOBase,
    TextIOWrapper,
    open,  # noqa: A004
    open_code,
)


__all__: list[str] = [
    "DEFAULT_BUFFER_SIZE",
    "BlockingIOError",
    "BufferedIOBase",
    "BufferedRWPair",
    "BufferedRandom",
    "BufferedReader",
    "BufferedWriter",
    "BytesIO",
    "FileIO",
    "IOBase",
    "IncrementalNewlineDecoder",
    "RawIOBase",
    "StringIO",
    "TextIOBase",
    "TextIOWrapper",
    "UnsupportedOperation",
    "open",
    "open_code",
    "text_encoding",
]

DEFAULT_BUFFER_SIZE.__module__ = __name__

BlockingIOError.__module__ = __name__
UnsupportedOperation.__module__ = __name__

BufferedIOBase.__module__ = __name__
BufferedRWPair.__module__ = __name__
BufferedRandom.__module__ = __name__
BufferedReader.__module__ = __name__
BufferedWriter.__module__ = __name__
BytesIO.__module__ = __name__
FileIO.__module__ = __name__
IOBase.__module__ = __name__
IncrementalNewlineDecoder.__module__ = __name__
RawIOBase.__module__ = __name__
StringIO.__module__ = __name__
TextIOBase.__module__ = __name__
TextIOWrapper.__module__ = __name__

open.__module__ = __name__
open_code.__module__ = __name__
text_encoding.__module__ = __name__
