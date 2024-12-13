"""Provides a backport to `tomllib`.

Authorship
----------
* MIT License, Copyright (c) 2021 Taneli Hukkinen.

See Also
--------
* `tomllib`.
"""

from aiostdlib.internal.backports.tomllib.errors import TOMLDecodeError
from aiostdlib.internal.backports.tomllib.parser import loads


__all__: list[str] = ["TOMLDecodeError", "loads"]
