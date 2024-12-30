from aiostdlib.internal.impl.json import (
    JSONDecodeError,
    JSONDecoder,
    JSONEncoder,
    dump,
    dumps,
    load,
    loads,
)


__all__: list[str] = [
    "JSONDecodeError",
    "JSONDecoder",
    "JSONEncoder",
    "dump",
    "dumps",
    "load",
    "loads",
]


JSONDecodeError.__module__ = __name__

JSONDecoder.__module__ = __name__
JSONEncoder.__module__ = __name__

dump.__module__ = __name__
dumps.__module__ = __name__
load.__module__ = __name__
loads.__module__ = __name__
