"""Provides a backport to `json`.

See Also
--------
* `json`.
"""

from aiostdlib.internal.backports.json.py313 import JSONDecoder, JSONEncoder, dumps, loads
from aiostdlib.internal.backports.json.src.errors import JSONDecodeError


__all__: list[str] = ["JSONDecodeError", "JSONDecoder", "JSONEncoder", "dumps", "loads"]
