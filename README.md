# aiostdlib

[![PyPI Version][shields/pypi/version]][pypi/homepage]
[![PyPI Downloads][shields/pypi/downloads]][pypi/homepage]
[![License][shields/pypi/license]][github/license]
[![Python Version][shields/python/version]][pypi/homepage]

## Key Features

* Provides asynchronous versions of the standard libraries;
* The same API as the Python's standard, blocking API;
* Blocking IO is performed in a separate thread.

## Getting Started

For more, see the [documentation][github/docs].

### Installation

The library is available as [`aiostdlib`][pypi/homepage] on PyPI:

```shell
pip install aiostdlib
```

### Usage

The `aiostdlib` API is the same as the standard library, except that it is asynchronous.

#### builtins

```python
import asyncio

from aiostdlib import builtins


async def main() -> None:
    async with builtins.open("./file.txt", mode="w") as file:
        await file.write("aiostdlib")


if __name__ == "__main__":
    asyncio.run(main())
```

#### json

```python
import asyncio

from aiostdlib import builtins, json


async def main() -> None:
    async with builtins.open("./file.json", mode="w") as file:
        await json.dump(["aiostdlib"], file)


if __name__ == "__main__":
    asyncio.run(main())
```

#### pathlib

```python
import asyncio

from aiostdlib import pathlib


async def main() -> None:
    path = pathlib.Path("file.txt")

    if not await path.exists():
        await path.write_text("aiostdlib")


if __name__ == "__main__":
    asyncio.run(main())
```

#### shutil

```python
import asyncio

from aiostdlib import shutil


async def main() -> None:
    await shutil.rmtree("/tmp/aioshutil")


if __name__ == "__main__":
    asyncio.run(main())
```

#### tarfile

```python
import asyncio

from aiostdlib import tarfile


async def main() -> None:
    if not await tarfile.is_tarfile("./aiostdlib.tar.gz"):
        detail = "The file is not a `tar` archive"
        raise RuntimeError(detail)


if __name__ == "__main__":
    asyncio.run(main())
```

#### tempfile

```python
import asyncio

from aiostdlib import tempfile


async def main() -> None:
    tempdir, path = await asyncio.gather(
        tempfile.gettempdir(),
        tempfile.mkdtemp(),
    )

    if not path.startswith(tempdir):
        detail = "This is strange..."
        raise RuntimeError(detail)


if __name__ == "__main__":
    asyncio.run(main())
```

#### tomllib

```python
import asyncio

from aiostdlib import builtins, tomllib


async def main() -> None:
    async with builtins.open("./file.toml", mode="rb") as file:
        data = await tomllib.load(file)

        if "aiostdlib" not in data:
            detail = "Where is 'aiostdlib'?"
            raise RuntimeError(detail)


if __name__ == "__main__":
    asyncio.run(main())
```

#### zipfile

```python
import asyncio

from aiostdlib import zipfile


async def main() -> None:
    if not await zipfile.is_zipfile("./aiostdlib.zip"):
        detail = "The file is not a `zip` archive"
        raise RuntimeError(detail)


if __name__ == "__main__":
    asyncio.run(main())
```

## License

MIT License, Copyright (c) 2024 Sergei Bogdanov. See [LICENSE][github/license] file.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[github/docs]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/
[github/license]: https://github.com/syubogdanov/aiostdlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/aiostdlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/aiostdlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/aiostdlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/aiostdlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/aiostdlib.svg?color=green
