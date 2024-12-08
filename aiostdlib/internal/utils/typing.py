from __future__ import annotations

from os import PathLike
from typing import Protocol, TypeVar, Union

from aiostdlib.internal.backports.typing import Self, TypeAlias


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


StrOrBytesPath: TypeAlias = Union[str, bytes, PathLike[str], PathLike[bytes]]


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
