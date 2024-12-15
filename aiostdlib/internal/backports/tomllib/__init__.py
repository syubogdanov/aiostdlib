"""Provides a backport to `tomllib`.

See Also
--------
* `tomllib`.
"""

from aiostdlib.internal.backports.tomllib.py313 import TOMLDecodeError, loads


__all__: list[str] = ["TOMLDecodeError", "loads"]
