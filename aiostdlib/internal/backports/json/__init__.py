"""Provides a backport to `json`.

See Also
--------
* `json`.
"""

from aiostdlib.internal.backports.json.py313 import (
    JSONDecodeError,
    JSONDecoder,
    JSONEncoder,
    dumps,
    loads,
)


__all__: list[str] = ["JSONDecodeError", "JSONDecoder", "JSONEncoder", "dumps", "loads"]
