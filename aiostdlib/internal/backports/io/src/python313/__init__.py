from builtins import BlockingIOError
from typing import Final


__all__: list[str] = ["DEFAULT_BUFFER_SIZE", "BlockingIOError", "UnsupportedOperation"]


DEFAULT_BUFFER_SIZE: Final[int] = 8 * 1024  # bytes


class UnsupportedOperation(OSError, ValueError):
    """Raised when an unsupported operation is called on a stream.

    See Also
    --------
    * `io.UnsupportedOperation`.
    """
