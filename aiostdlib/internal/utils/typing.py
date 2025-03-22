from abc import abstractmethod
from typing import Protocol, TypeVar, runtime_checkable


T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)


AnyStr = TypeVar("AnyStr", str, bytes)


@runtime_checkable
class Buffer(Protocol):
    """An ABC with one abstract method `__buffer__`."""

    @abstractmethod
    def __buffer__(self, flags: int, /) -> memoryview:
        """Return a memoryview of the buffer."""


@runtime_checkable
class SupportsRead(Protocol[T_co]):
    """An ABC with one abstract method `read`."""

    @abstractmethod
    def read(self, length: int = ..., /) -> T_co:
        """Read and return up to `length` units."""


@runtime_checkable
class SupportsAsyncRead(Protocol[T_co]):
    """An ABC with one abstract asynchronous method `read`."""

    @abstractmethod
    async def read(self, length: int = ..., /) -> T_co:
        """Read and return up to `length` units."""


@runtime_checkable
class SupportsWrite(Protocol[T_contra]):
    """An ABC with one abstract method `write`."""

    @abstractmethod
    def write(self, buffer: T_contra, /) -> int:
        """Write the buffer and return the number of units written."""


@runtime_checkable
class SupportsAsyncWrite(Protocol[T_contra]):
    """An ABC with one abstract asynchronous method `write`."""

    @abstractmethod
    async def write(self, buffer: T_contra, /) -> int:
        """Write the buffer and return the number of units written."""
