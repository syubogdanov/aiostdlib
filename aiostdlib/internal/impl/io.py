from aiostdlib.internal.backports.io import (
    DEFAULT_BUFFER_SIZE,
    BlockingIOError,  # noqa: A004
    UnsupportedOperation,
    text_encoding,
)
from aiostdlib.internal.backports.os import SEEK_CUR, SEEK_SET
from aiostdlib.internal.backports.typing import Self


class IOBase:
    """The base class for all I/O classes.

    See Also
    --------
    * `io.IOBase`.
    """


class RawIOBase:
    """The base class for raw binary streams.

    See Also
    --------
    * `io.RawIOBase`.
    """


class BufferedIOBase:
    """The base class for binary streams that support some kind of buffering.

    See Also
    --------
    * `io.BufferedIOBase`.
    """


class FileIO:
    """A raw binary stream representing an OS-level file containing bytes data.

    See Also
    --------
    * `io.FileIO`.
    """


class BytesIO:
    """A binary stream using an in-memory bytes buffer.

    See Also
    --------
    * `io.BytesIO`.
    """


class BufferedReader:
    """A buffered binary stream.

    See Also
    --------
    * `io.BufferedReader`.
    """


class BufferedWriter:
    """A buffered binary stream.

    See Also
    --------
    * `io.BufferedWriter`.
    """


class BufferedRandom:
    """A buffered binary stream.

    See Also
    --------
    * `io.BufferedRandom`.
    """


class BufferedRWPair:
    """A buffered binary stream.

    See Also
    --------
    * `io.BufferedRWPair`.
    """


class TextIOBase:
    """The base class for text streams.

    See Also
    --------
    * `io.TextIOBase`.
    """


class TextIOWrapper:
    """A buffered text stream.

    See Also
    --------
    * `io.TextIOWrapper`.
    """


class StringIO:
    """A text stream using an in-memory text buffer.

    See Also
    --------
    * `io.StringIO`.
    """


class IncrementalNewlineDecoder:
    """A helper codec that decodes newlines for universal newlines mode.

    See Also
    --------
    * `io.IncrementalNewlineDecoder`.
    """
