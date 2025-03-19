# aiostdlib

[![PyPI Version][shields/pypi/version]][pypi/homepage]
[![PyPI Downloads][shields/pypi/downloads]][pypi/homepage]
[![License][shields/pypi/license]][github/license]
[![Python Version][shields/python/version]][pypi/homepage]

> [!WARNING]
> The library is in the pre-alpha stage. Bugs may exist!

## Key Features

* Provides asynchronous version of the standard library;
* The same API as the Python 3.13 standard blocking API;
* Blocking IO is performed in a separate thread.

## Getting Started

### Installation

The library is available as [`aiostdlib`][pypi/homepage] on PyPI:

```shell
pip install aiostdlib
```

### Usage

#### json

For more, see the [documentation][docs/json].

```python
from aiostdlib import json

async def main() -> None:
    with open("aiostdlib.json") as file:
        data = await json.load(file)
```

#### tomllib

For more, see the [documentation][docs/tomllib].

```python
from aiostdlib import tomllib

async def main() -> None:
    with open("aiostdlib.toml", mode="rb") as file:
        data = await tomllib.load(file)
```

## License

MIT License, Copyright (c) 2025 Sergei Y. Bogdanov. See [LICENSE][github/license] file.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[docs/json]: https://aiostdlib.readthedocs.io/en/latest/json.html
[docs/tomllib]: https://aiostdlib.readthedocs.io/en/latest/tomllib.html

[github/license]: https://github.com/syubogdanov/aiostdlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/aiostdlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/aiostdlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/aiostdlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/aiostdlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/aiostdlib.svg?color=green
