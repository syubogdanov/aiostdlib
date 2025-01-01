from __future__ import annotations

import warnings

from typing import IO, TYPE_CHECKING, Any, BinaryIO, Literal, overload

from aiostdlib.internal.utils.typing import (
    FileDescriptorOrPath,
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
)


if TYPE_CHECKING:
    from collections.abc import Callable


__all__: list[str] = [
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
    "open",
    "open_code",
]


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


@overload
def open(  # noqa: A001
    file: FileDescriptorOrPath,
    mode: OpenTextMode = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> TextIOWrapper: ...


@overload
def open(  # noqa: A001
    file: FileDescriptorOrPath,
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> FileIO: ...


@overload
def open(  # noqa: A001
    file: FileDescriptorOrPath,
    mode: OpenBinaryModeUpdating,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedRandom: ...


@overload
def open(  # noqa: A001
    file: FileDescriptorOrPath,
    mode: OpenBinaryModeWriting,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedWriter: ...


@overload
def open(  # noqa: A001
    file: FileDescriptorOrPath,
    mode: OpenBinaryModeReading,
    buffering: Literal[-1, 1] = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BufferedReader: ...


@overload
def open(  # noqa: A001
    file: FileDescriptorOrPath,
    mode: OpenBinaryMode,
    buffering: int = -1,
    encoding: None = None,
    errors: None = None,
    newline: None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> BinaryIO: ...


@overload
def open(  # noqa: A001
    file: FileDescriptorOrPath,
    mode: str,
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> IO[Any]: ...


def open(  # noqa: A001
    file: FileDescriptorOrPath,
    mode: str = "r",
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,  # noqa: FBT001, FBT002
    opener: Callable[[str, int], int] | None = None,
) -> IO[Any]:
    """Open `file` and return a corresponding file object.

    See Also
    --------
    * `io.open`.
    """
    raise NotImplementedError


def open_code(path: str) -> IO[bytes]:
    """Open the provided file with mode `'rb'`.

    See Also
    --------
    * `io.open_code`.
    """
    detail = "'aiostdlib.io.open_code' may not be using hooks"
    warnings.warn(detail, RuntimeWarning, stacklevel=2)
    return open(path, mode="rb")
