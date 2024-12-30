from __future__ import annotations

import sys
import warnings


__all__: list[str] = ["text_encoding"]


def text_encoding(encoding: str | None, stacklevel: int = 2, /) -> str:
    """Return `encoding` if specified else `"locale"` or `"utf-8"`.

    Notes
    -----
    * The `sys.flags.warn_default_encoding` flag is available since Python 3.10. For this reason,
      warnings will not be triggered in Python 3.9.

    See Also
    --------
    * `io.text_encoding`.
    """
    if encoding is not None:
        return encoding

    if sys.version_info >= (3, 10) and sys.flags.warn_default_encoding:
        detail = "The 'encoding' argument is not specified"
        warnings.warn(detail, EncodingWarning, stacklevel=(stacklevel + 1))  # noqa: F821

    return "utf-8" if sys.flags.utf8_mode else "locale"
