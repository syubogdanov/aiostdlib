# aiostdlib

[![PyPI Version][shields/pypi/version]][pypi/homepage]
[![PyPI Downloads][shields/pypi/downloads]][pypi/homepage]
[![License][shields/pypi/license]][github/license]
[![Python Version][shields/python/version]][pypi/homepage]

> [!WARNING]
> The library is in the planning stage.

## Key Features

* Provides asynchronous version of the standard library;
* The same API as the Python's standard, blocking API;
* Blocking IO is performed in a separate thread.

## Getting Started

### Installation

The library is available as [`aiostdlib`][pypi/homepage] on PyPI:

```shell
pip install aiostdlib
```

### Usage

The `aiostdlib` API is the same as the standard library, except that it is asynchronous.

#### builtins

For more, see the [documentation][github/docs/builtins].

```python
import asyncio

from aiostdlib import builtins


async def main() -> None:
    async with builtins.open("./aiostdlib.txt", mode="w") as file:
        await file.write("aiostdlib")


if __name__ == "__main__":
    asyncio.run(main())
```

#### json

For more, see the [documentation][github/docs/json].

```python
import asyncio

from aiostdlib import builtins, json


async def main() -> None:
    async with builtins.open("./aiostdlib.json", mode="w") as file:
        await json.dump(["aiostdlib"], file)


if __name__ == "__main__":
    asyncio.run(main())
```

#### pathlib

For more, see the [documentation][github/docs/pathlib].

```python
import asyncio

from aiostdlib import pathlib


async def main() -> None:
    path = pathlib.Path("./aiostdlib.txt")

    if not await path.exists():
        await path.write_text("aiostdlib")


if __name__ == "__main__":
    asyncio.run(main())
```

#### shutil

For more, see the [documentation][github/docs/shutil].

```python
import asyncio

from aiostdlib import shutil


async def main() -> None:
    await shutil.rmtree("/tmp/aiostdlib/")


if __name__ == "__main__":
    asyncio.run(main())
```

#### tarfile

For more, see the [documentation][github/docs/tarfile].

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

For more, see the [documentation][github/docs/tempfile].

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

For more, see the [documentation][github/docs/tomllib].

```python
import asyncio

from aiostdlib import builtins, tomllib


async def main() -> None:
    async with builtins.open("./aiostdlib.toml", mode="rb") as file:
        data = await tomllib.load(file)

        if "aiostdlib" not in data:
            detail = "Where is 'aiostdlib'?"
            raise RuntimeError(detail)


if __name__ == "__main__":
    asyncio.run(main())
```

#### zipfile

For more, see the [documentation][github/docs/zipfile].

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

[github/docs/builtins]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/builtins.md
[github/docs/json]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/json.md
[github/docs/pathlib]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/pathlib.md
[github/docs/shutil]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/shutil.md
[github/docs/tarfile]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/tarfile.md
[github/docs/tempfile]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/tempfile.md
[github/docs/tomllib]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/tomllib.md
[github/docs/zipfile]: https://github.com/syubogdanov/aiostdlib/tree/main/docs/zipfile.md
[github/license]: https://github.com/syubogdanov/aiostdlib/tree/main/LICENSE

[pypi/homepage]: https://pypi.org/project/aiostdlib/

[shields/pypi/downloads]: https://img.shields.io/pypi/dm/aiostdlib.svg?color=green
[shields/pypi/license]: https://img.shields.io/pypi/l/aiostdlib.svg?color=green
[shields/pypi/version]: https://img.shields.io/pypi/v/aiostdlib.svg?color=green
[shields/python/version]: https://img.shields.io/pypi/pyversions/aiostdlib.svg?color=green
