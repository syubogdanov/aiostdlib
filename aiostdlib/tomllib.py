from aiostdlib.internal.backports.tomllib import TOMLDecodeError, loads
from aiostdlib.internal.impl.tomllib import load


__all__: list[str] = ["TOMLDecodeError", "load", "loads"]


TOMLDecodeError.__module__ = __name__

load.__module__ = __name__
loads.__module__ = __name__
