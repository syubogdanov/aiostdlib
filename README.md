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

#### os

For more, see the [documentation][docs/os].

```python
import sys

from aiostdlib import os

async def main() -> None:
    fd = sys.stdout.fileno()
    detail = b"Hello, aiostdlib!"
    await os.write(fd, detail)
```

#### os.path

For more, see the [documentation][docs/os.path].

```python
from aiostdlib import os

async def main() -> None:
    if await os.path.exists("./aiostdlib.txt"):
        await os.unlink("./aiostdlib.txt")
```

#### tomllib

For more, see the [documentation][docs/tomllib].

```python
from aiostdlib import tomllib

async def main() -> None:
    with open("aiostdlib.toml", mode="rb") as file:
        data = await tomllib.load(file)
```

## Environment

* If `AIOSTDLIB_CONCURRENT_WORKERS` is a positive integer, then no more than the specified number of
  threads will be used to execute calls asynchronously. If zero, then threading is not used at all.
  Otherwise, a minimum of `32` and `os.cpu_count() + 4` is the limit.

## License

MIT License, Copyright (c) 2025 Sergei Y. Bogdanov. See [LICENSE][github/license] file.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[docs/json]: https://aiostdlib.readthedocs.io/en/latest/json.html
[docs/os]: https://aiostdlib.readthedocs.io/en/latest/os.html
[docs/os.path]: https://aiostdlib.readthedocs.io/en/latest/os.path.html
[docs/tomllib]: https://aiostdlib.readthedocs.io/en/latest/tomllib.html

[github/license]: https://github.com/syubogdanov/aiostdlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/aiostdlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/aiostdlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/aiostdlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/aiostdlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/aiostdlib.svg?color=green
