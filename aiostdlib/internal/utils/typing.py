from os import PathLike
from typing import Literal, Protocol, TypeVar, Union

from aiostdlib.internal.backports.typing import Self, TypeAlias


__all__: list[str] = [
    "FileDescriptorOrPath",
    "OpenBinaryMode",
    "OpenBinaryModeReading",
    "OpenBinaryModeUpdating",
    "OpenBinaryModeWriting",
    "OpenTextMode",
    "OpenTextModeReading",
    "OpenTextModeUpdating",
    "OpenTextModeWriting",
    "StrOrBytesPath",
    "SupportsAsyncRead",
    "SupportsAsyncWrite",
    "SupportsRead",
    "SupportsWrite",
]


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


StrOrBytesPath: TypeAlias = Union[str, bytes, PathLike[str], PathLike[bytes]]
FileDescriptorOrPath: TypeAlias = int | StrOrBytesPath


OpenTextModeUpdating: TypeAlias = Literal[
    "r+",
    "+r",
    "rt+",
    "r+t",
    "+rt",
    "tr+",
    "t+r",
    "+tr",
    "w+",
    "+w",
    "wt+",
    "w+t",
    "+wt",
    "tw+",
    "t+w",
    "+tw",
    "a+",
    "+a",
    "at+",
    "a+t",
    "+at",
    "ta+",
    "t+a",
    "+ta",
    "x+",
    "+x",
    "xt+",
    "x+t",
    "+xt",
    "tx+",
    "t+x",
    "+tx",
]
OpenTextModeWriting: TypeAlias = Literal["w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx"]
OpenTextModeReading: TypeAlias = Literal[
    "r",
    "rt",
    "tr",
    "U",
    "rU",
    "Ur",
    "rtU",
    "rUt",
    "Urt",
    "trU",
    "tUr",
    "Utr",
]
OpenTextMode: TypeAlias = OpenTextModeUpdating | OpenTextModeWriting | OpenTextModeReading
OpenBinaryModeUpdating: TypeAlias = Literal[
    "rb+",
    "r+b",
    "+rb",
    "br+",
    "b+r",
    "+br",
    "wb+",
    "w+b",
    "+wb",
    "bw+",
    "b+w",
    "+bw",
    "ab+",
    "a+b",
    "+ab",
    "ba+",
    "b+a",
    "+ba",
    "xb+",
    "x+b",
    "+xb",
    "bx+",
    "b+x",
    "+bx",
]
OpenBinaryModeWriting: TypeAlias = Literal["wb", "bw", "ab", "ba", "xb", "bx"]
OpenBinaryModeReading: TypeAlias = Literal["rb", "br", "rbU", "rUb", "Urb", "brU", "bUr", "Ubr"]
OpenBinaryMode: TypeAlias = OpenBinaryModeUpdating | OpenBinaryModeReading | OpenBinaryModeWriting


class SupportsRead(Protocol[T_co]):
    """An object that provides the `read` method."""

    def read(self: Self, length: int = ..., /) -> T_co:
        """Perform a read operation."""


class SupportsWrite(Protocol[T_contra]):
    """An object that provides the `write` method."""

    def write(self: Self, s: T_contra, /) -> object:
        """Perform a write operation."""


class SupportsAsyncRead(Protocol[T_co]):
    """An object that provides the asynchronous `read` method."""

    async def read(self: Self, length: int = ..., /) -> T_co:
        """Perform a read operation."""


class SupportsAsyncWrite(Protocol[T_contra]):
    """An object that provides the asynchronous `write` method."""

    async def write(self: Self, s: T_contra, /) -> object:
        """Perform a write operation."""
