from builtins import BlockingIOError  # noqa: A004


__all__: list[str] = ["BlockingIOError", "UnsupportedOperation"]


class UnsupportedOperation(OSError, ValueError):  # noqa: N818
    """Raised when an unsupported operation is called on a stream.

    See Also
    --------
    * `io.UnsupportedOperation`.
    """
