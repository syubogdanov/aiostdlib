"""Provides a backport to `tomllib`.

Authorship
----------
* MIT License, Copyright (c) 2021 Taneli Hukkinen.

See Also
--------
* `tomllib`.
"""

from __future__ import annotations

from typing import Tuple

from aiostdlib.internal.backports.typing import TypeAlias


Key: TypeAlias = Tuple[str, ...]
Pos: TypeAlias = int
