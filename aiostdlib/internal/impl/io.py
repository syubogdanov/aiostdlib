from aiostdlib.internal.backports.io import (
    DEFAULT_BUFFER_SIZE,
    BlockingIOError,  # noqa: A004
    UnsupportedOperation,
    text_encoding,
)
from aiostdlib.internal.backports.os import SEEK_CUR, SEEK_SET


class IOBase:
    """The base class for all I/O classes.

    See Also
    --------
    * `io.IOBase`.
    """
