from __future__ import annotations

from os import PathLike
from typing import Protocol, TypeVar, Union

from aiostdlib.internal.backports.typing import Self, TypeAlias


_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)


StrOrBytesPath: TypeAlias = Union[str, bytes, PathLike[str], PathLike[bytes]]


class SupportsRead(Protocol[_T_co]):
    """An object that provides the `read` method."""

    def read(self: Self, length: int = ..., /) -> _T_co:
        """Perform a read operation."""


class SupportsWrite(Protocol[_T_contra]):
    """An object that provides the `write` method."""

    def write(self: Self, s: _T_contra, /) -> object:
        """Perform a write operation."""


class SupportsAsyncRead(Protocol[_T_co]):
    """An object that provides the asynchronous `read` method."""

    async def read(self: Self, length: int = ..., /) -> _T_co:
        """Perform a read operation."""


class SupportsAsyncWrite(Protocol[_T_contra]):
    """An object that provides the asynchronous `write` method."""

    async def write(self: Self, s: _T_contra, /) -> object:
        """Perform a write operation."""
