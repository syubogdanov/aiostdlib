from __future__ import annotations

import asyncio

from typing import TYPE_CHECKING

from backlib.py313 import os as py313_os
from backlib.py313.os.path import (
    basename,
    commonpath,
    commonprefix,
    dirname,
    isabs,
    isreserved,
    join,
    normcase,
    normpath,
    samestat,
    split,
    splitdrive,
    splitext,
    splitroot,
    supports_unicode_filenames,
)
from backlib.py313.stat import S_ISDIR, S_ISLNK, S_ISREG

from aiostdlib.internal.core.asyncio import awaitify
from aiostdlib.internal.stdlib import os


if TYPE_CHECKING:
    from backlib.py313.os import PathLike

    from aiostdlib.internal.utils.typing import AnyStr


__all__: list[str] = [
    "abspath",
    "basename",
    "commonpath",
    "commonprefix",
    "dirname",
    "exists",
    "getatime",
    "getctime",
    "getmtime",
    "getsize",
    "isabs",
    "isdevdrive",
    "isdir",
    "isfile",
    "isjunction",
    "islink",
    "ismount",
    "isreserved",
    "join",
    "lexists",
    "normcase",
    "normpath",
    "realpath",
    "relpath",
    "samefile",
    "sameopenfile",
    "samestat",
    "split",
    "splitdrive",
    "splitext",
    "splitroot",
    "supports_unicode_filenames",
]

__aiostdlib__: str = "aiostdlib.os.path"


async def abspath(path: AnyStr | PathLike[AnyStr]) -> AnyStr:
    """Return a normalized absolutized version of the pathname `path`.

    See Also
    --------
    * `os.path.abspath`.
    """
    awaitified = awaitify(py313_os.path.abspath)
    return await awaitified(path)


async def exists(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path or an open file descriptor.

    See Also
    --------
    * `os.path.exists`.
    """
    try:
        await os.stat(path)
    except (OSError, ValueError):
        return False
    return True


async def getatime(path: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last access of `path`.

    See Also
    --------
    * `os.path.getatime`.
    """
    st = await os.stat(path)
    return st.st_atime


async def getctime(path: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the system's ctime for `path`.

    See Also
    --------
    * `os.path.getctime`.
    """
    st = await os.stat(path)
    return st.st_ctime


async def getmtime(path: int | AnyStr | PathLike[AnyStr]) -> float:
    """Return the time of last modification of `path`.

    See Also
    --------
    * `os.path.getmtime`.
    """
    st = await os.stat(path)
    return st.st_mtime


async def getsize(path: int | AnyStr | PathLike[AnyStr]) -> int:
    """Return the size, in bytes, of `path`.

    See Also
    --------
    * `os.path.getsize`.
    """
    st = await os.stat(path)
    return st.st_size


async def isdevdrive(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is located on a Windows Dev Drive.

    See Also
    --------
    * `os.path.isdevdrive`.
    """
    awaitified = awaitify(py313_os.path.isdevdrive)
    return await awaitified(path)


async def isdir(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an existing directory.

    See Also
    --------
    * `os.path.isdir`.
    """
    try:
        st = await os.stat(path)
    except (OSError, ValueError):
        return False
    return S_ISDIR(st.st_mode)


async def isfile(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` is an existing regular file.

    See Also
    --------
    * `os.path.isfile`.
    """
    try:
        st = await os.stat(path)
    except (OSError, ValueError):
        return False
    return S_ISREG(st.st_mode)


async def isjunction(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a junction.

    See Also
    --------
    * `os.path.isjunction`.
    """
    awaitified = awaitify(py313_os.path.isjunction)
    return await awaitified(path)


async def islink(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing directory entry that is a symbolic link.

    See Also
    --------
    * `os.path.islink`.
    """
    try:
        st = await os.lstat(path)
    except (OSError, ValueError, AttributeError):
        return False
    return S_ISLNK(st.st_mode)


async def ismount(path: int | AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if pathname `path` is a mount point.

    See Also
    --------
    * `os.path.ismount`.
    """
    awaitified = awaitify(py313_os.path.ismount)
    return await awaitified(path)


async def lexists(path: AnyStr | PathLike[AnyStr]) -> bool:
    """Return `True` if `path` refers to an existing path, including broken symbolic links."""
    try:
        await os.lstat(path)
    except (OSError, ValueError):
        return False
    return True


async def realpath(filename: AnyStr | PathLike[AnyStr], *, strict: bool = False) -> AnyStr:
    """Return the canonical path of the specified filename.

    See Also
    --------
    * `os.path.realpath`.
    """
    awaitified = awaitify(py313_os.path.realpath)
    return await awaitified(filename, strict=strict)


async def relpath(
    path: AnyStr | PathLike[AnyStr],
    start: AnyStr | PathLike[AnyStr] | None = None,
) -> AnyStr:
    """Return a relative filepath to `path`.

    See Also
    --------
    * `os.path.relpath`.
    """
    awaitified = awaitify(py313_os.path.relpath)
    return await awaitified(path, start)


async def samefile(
    f1: int | AnyStr | PathLike[AnyStr],
    f2: int | AnyStr | PathLike[AnyStr],
) -> bool:
    """Return `True` if both pathname arguments refer to the same file or directory.

    See Also
    --------
    * `os.path.samefile`
    """
    s1, s2 = await asyncio.gather(os.stat(f1), os.stat(f2))
    return samestat(s1, s2)


async def sameopenfile(fp1: int, fp2: int) -> bool:
    """Return `True` if the file descriptors `fp1` and `fp2` refer to the same file.

    See Also
    --------
    * `os.sameopenfile`.
    """
    s1, s2 = await asyncio.gather(os.fstat(fp1), os.fstat(fp2))
    return samestat(s1, s2)


abspath.__module__ = __aiostdlib__
exists.__module__ = __aiostdlib__
getatime.__module__ = __aiostdlib__
getctime.__module__ = __aiostdlib__
getmtime.__module__ = __aiostdlib__
getsize.__module__ = __aiostdlib__
isdevdrive.__module__ = __aiostdlib__
isdir.__module__ = __aiostdlib__
isfile.__module__ = __aiostdlib__
isjunction.__module__ = __aiostdlib__
islink.__module__ = __aiostdlib__
ismount.__module__ = __aiostdlib__
lexists.__module__ = __aiostdlib__
realpath.__module__ = __aiostdlib__
relpath.__module__ = __aiostdlib__
samefile.__module__ = __aiostdlib__
sameopenfile.__module__ = __aiostdlib__
