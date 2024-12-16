from dataclasses import dataclass

from aiostdlib.internal.backports.typing import Self


@dataclass
class JSONDecodeError(ValueError):
    """Subclass of `ValueError`.

    Attributes
    ----------
    * `msg`: The unformatted error message;
    * `doc`: The `JSON` document being parsed;
    * `pos`: The start index of `doc` where parsing failed;
    * `lineno`: The line corresponding to `pos`;
    * `colno`: The column corresponding to `pos`.
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
        colno = self.pos - self.doc.rfind("\n", 0, self.pos)

        message = f"{self.msg}: line {lineno} column {colno} (char {self.pos})"
        super().__init__(message)

        self.lineno: int = lineno
        self.colno: int = colno

    def __reduce__(self: Self) -> tuple[type[Self], tuple[str, str, int]]:
        """Recreate the object when unpickling."""
        return (self.__class__, (self.msg, self.doc, self.pos))
