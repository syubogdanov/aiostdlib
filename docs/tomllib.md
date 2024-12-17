# `tomllib` — Parse TOML files

> [!NOTE]
> This text is based on *the official Python documentation*.

## About

### *coroutine* tomllib.**load**(*fp, /, \*, parse_float=float*)

Read a TOML file. The first argument should be a readable and binary file object. Return a [dict][dict]. Convert TOML
types to Python using this [conversion table](#conversion-table).

*parse_float* will be called with the string of every TOML float to be decoded. By default, this is equivalent to
`float(num_str)`. This can be used to use another datatype or parser for TOML floats (e.g.
[decimal.Decimal][decimal.Decimal]). The callable must not return a [dict][dict] or a [list][list], else a
[ValueError][ValueError] is raised.

### tomllib.**loads**(*s, /, \*, parse_float=float*)

Load TOML from a [str][str] object. Return a [dict][dict]. Convert TOML types to Python using this
[conversion table](#conversion-table). The parse_float argument has the same meaning as in
[load()](#coroutine-tomllibloadfp---parse_floatfloat).

### *exception* tomllib.**TOMLDecodeError**

Subclass of [ValueError][ValueError].

## Examples

Parsing a TOML file:

```python
from aiostdlib import tomllib

async def main():
    with open("pyproject.toml", "rb") as f:
        data = await tomllib.load(f)
```

Parsing a TOML string:

```python
from aiostdlib import tomllib

toml_str = """
python-version = "3.11.0"
python-implementation = "CPython"
"""

data = tomllib.loads(toml_str)
```

## Conversion Table

| TOML             | Python                                                                           |
|------------------|----------------------------------------------------------------------------------|
| TOML document    | dict                                                                             |
| string           | str                                                                              |
| integer          | int                                                                              |
| float            | float (configurable with *parse_float*)                                          |
| boolean          | bool                                                                             |
| offset date-time | datetime.datetime (`tzinfo` attribute set to an instance of `datetime.timezone`) |
| local date-time  | datetime.datetime (`tzinfo` attribute set to `None`)                             |
| local date       | datetime.date                                                                    |
| local time       | datetime.time                                                                    |
| array            | list                                                                             |
| table            | dict                                                                             |
| inline table     | dict                                                                             |
| array of tables  | list of dicts                                                                    |

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[ValueError]: https://docs.python.org/3/library/exceptions.html#ValueError
[decimal.Decimal]: https://docs.python.org/3/library/decimal.html#decimal.Decimal
[dict]: https://docs.python.org/3/library/stdtypes.html#dict
[list]: https://docs.python.org/3/library/stdtypes.html#list
[str]: https://docs.python.org/3/library/stdtypes.html#str
