"""Provides a backport to `tomllib`.

Authorship
----------
* MIT License, Copyright (c) 2021 Taneli Hukkinen.

See Also
--------
* `tomllib`.
"""

from aiostdlib.internal.backports.typing import TypeAlias


Key: TypeAlias = tuple[str, ...]
