"""Provides a backport to `tomllib`.

Authorship
----------
* MIT License, Copyright (c) 2021 Taneli Hukkinen.

See Also
--------
* `tomllib`.
"""

from __future__ import annotations

from dataclasses import dataclass

from aiostdlib.internal.backports.typing import Self


@dataclass
class TOMLDecodeError(ValueError):
    """An error raised if a document is not valid `TOML`.

    Attributes
    ----------
    * `msg` - The unformatted error message;
    * `doc` - The `TOML` document being parsed;
    * `pos` - The index of `doc` where parsing failed;
    * `lineno` - The line corresponding to `pos`;
    * `colno` - The column corresponding to `pos`.
    """

    msg: str
    doc: str
    pos: int

    def __post_init__(self: Self) -> None:
        """Initialize the object."""
        if not isinstance(self.msg, str):
            detail = "The 'msg' must be 'str'"
            raise TypeError(detail)

        if not isinstance(self.doc, str):
            detail = "The 'doc' must be 'str'"
            raise TypeError(detail)

        if not isinstance(self.pos, int):
            detail = "The 'pos' must be 'int'"
            raise TypeError(detail)

        lineno = self.doc.count("\n", 0, self.pos) + 1

        offset = 1 if lineno == 1 else self.doc.rindex("\n", 0, self.pos)
        colno = lineno + offset

        is_end_of_document = self.pos >= len(self.doc)
        location = "end of document" if is_end_of_document else f"line {lineno}, column {colno}"

        message = f"{self.msg} (at {location})"
        super().__init__(message)

        self.lineno: int = lineno
        self.colno: int = colno
