from __future__ import annotations

from contextlib import suppress
from typing import TYPE_CHECKING, Any, overload

from backlib.py313 import os as py313_os
from backlib.py313.os import (
    CLD_CONTINUED,
    CLD_DUMPED,
    CLD_EXITED,
    CLD_KILLED,
    CLD_STOPPED,
    CLD_TRAPPED,
    CLONE_FILES,
    CLONE_FS,
    CLONE_NEWCGROUP,
    CLONE_NEWIPC,
    CLONE_NEWNET,
    CLONE_NEWNS,
    CLONE_NEWPID,
    CLONE_NEWTIME,
    CLONE_NEWUSER,
    CLONE_NEWUTS,
    CLONE_SIGHAND,
    CLONE_SYSVSEM,
    CLONE_THREAD,
    CLONE_VM,
    EFD_CLOEXEC,
    EFD_NONBLOCK,
    EFD_SEMAPHORE,
    F_LOCK,
    F_OK,
    F_TEST,
    F_TLOCK,
    F_ULOCK,
    GRND_NONBLOCK,
    GRND_RANDOM,
    MFD_ALLOW_SEALING,
    MFD_CLOEXEC,
    MFD_HUGE_1GB,
    MFD_HUGE_1MB,
    MFD_HUGE_2GB,
    MFD_HUGE_2MB,
    MFD_HUGE_8MB,
    MFD_HUGE_16GB,
    MFD_HUGE_16MB,
    MFD_HUGE_32MB,
    MFD_HUGE_64KB,
    MFD_HUGE_256MB,
    MFD_HUGE_512KB,
    MFD_HUGE_512MB,
    MFD_HUGE_MASK,
    MFD_HUGE_SHIFT,
    MFD_HUGETLB,
    O_APPEND,
    O_ASYNC,
    O_CLOEXEC,
    O_CREAT,
    O_DIRECT,
    O_DIRECTORY,
    O_DSYNC,
    O_EXCL,
    O_NDELAY,
    O_NOATIME,
    O_NOCTTY,
    O_NOFOLLOW,
    O_NONBLOCK,
    O_PATH,
    O_RDONLY,
    O_RDWR,
    O_RSYNC,
    O_SYNC,
    O_TMPFILE,
    O_TRUNC,
    O_WRONLY,
    P_ALL,
    P_PGID,
    P_PID,
    P_PIDFD,
    PIDFD_NONBLOCK,
    POSIX_FADV_DONTNEED,
    POSIX_FADV_NOREUSE,
    POSIX_FADV_NORMAL,
    POSIX_FADV_RANDOM,
    POSIX_FADV_SEQUENTIAL,
    POSIX_FADV_WILLNEED,
    PRIO_PGRP,
    PRIO_PROCESS,
    PRIO_USER,
    R_OK,
    RTLD_DEEPBIND,
    RTLD_GLOBAL,
    RTLD_LAZY,
    RTLD_LOCAL,
    RTLD_NODELETE,
    RTLD_NOLOAD,
    RTLD_NOW,
    RWF_APPEND,
    RWF_DSYNC,
    RWF_HIPRI,
    RWF_NOWAIT,
    RWF_SYNC,
    SCHED_BATCH,
    SCHED_FIFO,
    SCHED_IDLE,
    SCHED_OTHER,
    SCHED_RESET_ON_FORK,
    SCHED_RR,
    SEEK_CUR,
    SEEK_DATA,
    SEEK_END,
    SEEK_HOLE,
    SEEK_SET,
    SPLICE_F_MORE,
    SPLICE_F_MOVE,
    SPLICE_F_NONBLOCK,
    TFD_CLOEXEC,
    TFD_NONBLOCK,
    TFD_TIMER_ABSTIME,
    TFD_TIMER_CANCEL_ON_SET,
    W_OK,
    WCONTINUED,
    WEXITED,
    WNOHANG,
    WNOWAIT,
    WSTOPPED,
    WUNTRACED,
    X_OK,
    XATTR_CREATE,
    XATTR_REPLACE,
    PathLike,
    altsep,
    curdir,
    defpath,
    devnull,
    error,
    extsep,
    fsdecode,
    fsencode,
    fspath,
    get_exec_path,
    linesep,
    name,
    pardir,
    pathsep,
    sep,
    stat_result,
    strerror,
    terminal_size,
)
from backlib.py313.os.path import split

from aiostdlib.internal.core.asyncio import awaitify


if TYPE_CHECKING:
    from collections.abc import Callable

    from aiostdlib.internal.utils.typing import AnyStr, Buffer


__all__: list[str] = [
    "CLD_CONTINUED",
    "CLD_DUMPED",
    "CLD_EXITED",
    "CLD_KILLED",
    "CLD_STOPPED",
    "CLD_TRAPPED",
    "CLONE_FILES",
    "CLONE_FS",
    "CLONE_NEWCGROUP",
    "CLONE_NEWIPC",
    "CLONE_NEWNET",
    "CLONE_NEWNS",
    "CLONE_NEWPID",
    "CLONE_NEWTIME",
    "CLONE_NEWUSER",
    "CLONE_NEWUTS",
    "CLONE_SIGHAND",
    "CLONE_SYSVSEM",
    "CLONE_THREAD",
    "CLONE_VM",
    "EFD_CLOEXEC",
    "EFD_NONBLOCK",
    "EFD_SEMAPHORE",
    "F_LOCK",
    "F_OK",
    "F_TEST",
    "F_TLOCK",
    "F_ULOCK",
    "GRND_NONBLOCK",
    "GRND_RANDOM",
    "MFD_ALLOW_SEALING",
    "MFD_CLOEXEC",
    "MFD_HUGETLB",
    "MFD_HUGE_1GB",
    "MFD_HUGE_1MB",
    "MFD_HUGE_2GB",
    "MFD_HUGE_2MB",
    "MFD_HUGE_8MB",
    "MFD_HUGE_16GB",
    "MFD_HUGE_16MB",
    "MFD_HUGE_32MB",
    "MFD_HUGE_64KB",
    "MFD_HUGE_256MB",
    "MFD_HUGE_512KB",
    "MFD_HUGE_512MB",
    "MFD_HUGE_MASK",
    "MFD_HUGE_SHIFT",
    "O_APPEND",
    "O_ASYNC",
    "O_CLOEXEC",
    "O_CREAT",
    "O_DIRECT",
    "O_DIRECTORY",
    "O_DSYNC",
    "O_EXCL",
    "O_NDELAY",
    "O_NOATIME",
    "O_NOCTTY",
    "O_NOFOLLOW",
    "O_NONBLOCK",
    "O_PATH",
    "O_RDONLY",
    "O_RDWR",
    "O_RSYNC",
    "O_SYNC",
    "O_TMPFILE",
    "O_TRUNC",
    "O_WRONLY",
    "PIDFD_NONBLOCK",
    "POSIX_FADV_DONTNEED",
    "POSIX_FADV_NOREUSE",
    "POSIX_FADV_NORMAL",
    "POSIX_FADV_RANDOM",
    "POSIX_FADV_SEQUENTIAL",
    "POSIX_FADV_WILLNEED",
    "PRIO_PGRP",
    "PRIO_PROCESS",
    "PRIO_USER",
    "P_ALL",
    "P_PGID",
    "P_PID",
    "P_PIDFD",
    "RTLD_DEEPBIND",
    "RTLD_GLOBAL",
    "RTLD_LAZY",
    "RTLD_LOCAL",
    "RTLD_NODELETE",
    "RTLD_NOLOAD",
    "RTLD_NOW",
    "RWF_APPEND",
    "RWF_DSYNC",
    "RWF_HIPRI",
    "RWF_NOWAIT",
    "RWF_SYNC",
    "R_OK",
    "SCHED_BATCH",
    "SCHED_FIFO",
    "SCHED_IDLE",
    "SCHED_OTHER",
    "SCHED_RESET_ON_FORK",
    "SCHED_RR",
    "SEEK_CUR",
    "SEEK_DATA",
    "SEEK_END",
    "SEEK_HOLE",
    "SEEK_SET",
    "SPLICE_F_MORE",
    "SPLICE_F_MOVE",
    "SPLICE_F_NONBLOCK",
    "TFD_CLOEXEC",
    "TFD_NONBLOCK",
    "TFD_TIMER_ABSTIME",
    "TFD_TIMER_CANCEL_ON_SET",
    "WCONTINUED",
    "WEXITED",
    "WNOHANG",
    "WNOWAIT",
    "WSTOPPED",
    "WUNTRACED",
    "W_OK",
    "XATTR_CREATE",
    "XATTR_REPLACE",
    "X_OK",
    "PathLike",
    "access",
    "altsep",
    "chdir",
    "chmod",
    "close",
    "closerange",
    "curdir",
    "defpath",
    "devnull",
    "error",
    "extsep",
    "fsdecode",
    "fsencode",
    "fspath",
    "fstat",
    "ftruncate",
    "get_exec_path",
    "getcwd",
    "getcwdb",
    "isatty",
    "linesep",
    "link",
    "listdir",
    "lseek",
    "lstat",
    "makedirs",
    "mkdir",
    "name",
    "open",
    "pardir",
    "pathsep",
    "read",
    "readlink",
    "remove",
    "removedirs",
    "rename",
    "renames",
    "replace",
    "rmdir",
    "sep",
    "stat",
    "stat_result",
    "strerror",
    "supports_dir_fd",
    "supports_effective_ids",
    "supports_fd",
    "supports_follow_symlinks",
    "symlink",
    "terminal_size",
    "truncate",
    "umask",
    "unlink",
    "urandom",
    "write",
]

__aiostdlib__: str = "aiostdlib.os"


async def access(
    path: int | AnyStr | PathLike[AnyStr],
    mode: int,
    *,
    dir_fd: int | None = None,
    effective_ids: bool = False,
    follow_symlinks: bool = True,
) -> bool:
    """Use the real uid / gid to test for access to `path`.

    See Also
    --------
    * `os.access`.
    """
    awaitified = awaitify(py313_os.access)
    return await awaitified(
        path,
        mode,
        dir_fd=dir_fd,
        effective_ids=effective_ids,
        follow_symlinks=follow_symlinks,
    )


async def chdir(path: int | AnyStr | PathLike[AnyStr]) -> None:
    """Change the current working directory to path.

    See Also
    --------
    * `os.chdir`.
    """
    awaitified = awaitify(py313_os.chdir)
    return await awaitified(path)


async def chmod(
    path: int | AnyStr | PathLike[AnyStr],
    mode: int,
    *,
    dir_fd: int | None = None,
    follow_symlinks: bool = True,
) -> None:
    """Change the mode of `path` to the numeric `mode`.

    See Also
    --------
    * `os.chmod`.
    """
    awaitified = awaitify(py313_os.chmod)
    return await awaitified(path, mode, dir_fd=dir_fd, follow_symlinks=follow_symlinks)


async def close(fd: int) -> None:
    """Close file descriptor `fd`.

    See Also
    --------
    * `os.close`.
    """
    awaitified = awaitify(py313_os.close)
    return await awaitified(fd)


async def closerange(fd_low: int, fd_high: int, /) -> None:
    """Close all file descriptors from `fd_low` (inclusive) to `fd_high` (exclusive).

    See Also
    --------
    * `os.closerange`.
    """
    awaitified = awaitify(py313_os.closerange)
    return await awaitified(fd_low, fd_high)


async def fstat(fd: int) -> stat_result:
    """Get the status of the file descriptor `fd`.

    See Also
    --------
    * `os.fstat`.
    """
    return await stat(fd)


async def ftruncate(fd: int, length: int, /) -> None:
    """Truncate the file corresponding to file descriptor `fd`.

    See Also
    --------
    * `os.ftruncate`.
    """
    awaitified = awaitify(py313_os.ftruncate)
    return await awaitified(fd, length)


async def getcwd() -> str:
    """Return a string representing the current working directory.

    See Also
    --------
    * `os.getcwd`.
    """
    awaitified = awaitify(py313_os.getcwd)
    return await awaitified()


async def getcwdb() -> bytes:
    """Return a bytestring representing the current working directory.

    See Also
    --------
    * `os.getcwdb`.
    """
    awaitified = awaitify(py313_os.getcwdb)
    return await awaitified()


async def isatty(fd: int, /) -> bool:
    """Return `True` if the file descriptor `fd` is open and connected to a tty(-like) device.

    See Also
    --------
    * `os.isatty`.
    """
    awaitified = awaitify(py313_os.isatty)
    return await awaitified(fd)


async def link(
    src: AnyStr | PathLike[AnyStr],
    dst: AnyStr | PathLike[AnyStr],
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
    follow_symlinks: bool = True,
) -> None:
    """Create a hard link pointing to `src` named `dst`.

    See Also
    --------
    * `os.link`.
    """
    awaitified = awaitify(py313_os.link)
    return await awaitified(
        src,
        dst,
        src_dir_fd=src_dir_fd,
        dst_dir_fd=dst_dir_fd,
        follow_symlinks=follow_symlinks,
    )


@overload
async def listdir(path: int) -> list[str]: ...


@overload
async def listdir(path: bytes | PathLike[bytes]) -> list[bytes]: ...


@overload
async def listdir(path: str | PathLike[str] | None = None) -> list[str]: ...


async def listdir(
    path: int | bytes | str | PathLike[bytes] | PathLike[str] | None = None,
) -> list[bytes] | list[str]:
    """Return a list containing the names of the entries in the directory given by `path`.

    See Also
    --------
    * `os.listdir`.
    """
    awaitified = awaitify(py313_os.listdir)
    return await awaitified(path)


async def lseek(fd: int, position: int, whence: int, /) -> int:
    """Set the current position of file descriptor `fd` to position `pos`, modified by `whence`.

    See Also
    --------
    * `os.lseek`.
    """
    awaitified = awaitify(py313_os.lseek)
    return await awaitified(fd, position, whence)


async def lstat(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> stat_result:
    """Perform the equivalent of an `lstat()` system call on the given path.

    See Also
    --------
    * `os.lstat`.
    """
    return await stat(path, dir_fd=dir_fd, follow_symlinks=False)


async def makedirs(
    name: AnyStr | PathLike[AnyStr],
    mode: int = 0o777,
    exist_ok: bool = False,
) -> None:
    """Recursive directory creation function.

    See Also
    --------
    * `os.makedirs`.
    """
    head, tail = split(name)
    if not tail:
        head, tail = split(head)

    # `aiostdlib.os.path` causes a circular import
    exists = awaitify(py313_os.path.exists)

    if head and tail and not await exists(head):
        with suppress(FileExistsError):
            await makedirs(head, exist_ok=exist_ok)

        if tail == curdir or tail == bytes(curdir, "ASCII"):
            return

    # `aiostdlib.os.path` causes a circular import
    isdir = awaitify(py313_os.path.isdir)

    try:
        await mkdir(name, mode)
    except OSError:
        if not exist_ok or not await isdir(name):
            raise


async def mkdir(
    path: AnyStr | PathLike[AnyStr],
    mode: int = 0o777,
    *,
    dir_fd: int | None = None,
) -> None:
    """Create a directory named `path` with numeric mode `mode`.

    See Also
    --------
    * `os.mkdir`.
    """
    awaitified = awaitify(py313_os.mkdir)
    return await awaitified(path, mode, dir_fd=dir_fd)


async def open(
    path: AnyStr | PathLike[AnyStr],
    flags: int,
    mode: int = 0o777,
    *,
    dir_fd: int | None = None,
) -> int:
    """Open the file `path`, set flags and possibly its mode.

    See Also
    --------
    * `os.open`.
    """
    awaitified = awaitify(py313_os.open)
    return await awaitified(path, flags, mode, dir_fd=dir_fd)


async def read(fd: int, n: int, /) -> bytes:
    """Read at most `n` bytes from file descriptor `fd`.

    See Also
    --------
    * `os.read`.
    """
    awaitified = awaitify(py313_os.read)
    return await awaitified(fd, n)


async def readlink(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> AnyStr:
    """Return a string representing the path to which the symbolic link points.

    See Also
    --------
    * `os.readlink`.
    """
    awaitified = awaitify(py313_os.readlink)
    return await awaitified(path, dir_fd=dir_fd)


async def remove(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> None:
    """Remove the file path.

    See Also
    --------
    * `os.remove`.
    """
    awaitified = awaitify(py313_os.remove)
    return await awaitified(path, dir_fd=dir_fd)


async def removedirs(name: AnyStr | PathLike[AnyStr]) -> None:
    """Remove directories recursively.

    See Also
    --------
    * `os.removedirs`.
    """
    await rmdir(name)

    head, tail = split(name)
    if not tail:
        head, tail = split(head)

    while head and tail:
        try:
            await rmdir(head)
        except OSError:
            break
        head, tail = split(head)


async def rename(
    src: AnyStr | PathLike[AnyStr],
    dst: AnyStr | PathLike[AnyStr],
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
) -> None:
    """Rename the file or directory `src` to `dst`.

    See Also
    --------
    * `os.rename`.
    """
    awaitified = awaitify(py313_os.rename)
    return await awaitified(src, dst, src_dir_fd=src_dir_fd, dst_dir_fd=dst_dir_fd)


async def renames(old: AnyStr | PathLike[AnyStr], new: AnyStr | PathLike[AnyStr]) -> None:
    """Recursive directory or file renaming function.

    See Also
    --------
    * `os.renames`.
    """
    head, tail = split(new)

    # `aiostdlib.os.path` causes a circular import
    exists = awaitify(py313_os.path.exists)

    if head and tail and not await exists(head):
        await makedirs(head)

    await rename(old, new)

    head, tail = split(old)
    if head and tail:
        with suppress(OSError):
            await removedirs(head)


async def replace(
    src: AnyStr | PathLike[AnyStr],
    dst: AnyStr | PathLike[AnyStr],
    *,
    src_dir_fd: int | None = None,
    dst_dir_fd: int | None = None,
) -> None:
    """Rename the file or directory `src` to `dst`.

    See Also
    --------
    * `os.replace`.
    """
    awaitified = awaitify(py313_os.replace)
    return await awaitified(src, dst, src_dir_fd=src_dir_fd, dst_dir_fd=dst_dir_fd)


async def rmdir(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> None:
    """Remove the directory path.

    See Also
    --------
    * `os.rmdir`.
    """
    awaitified = awaitify(py313_os.rmdir)
    return await awaitified(path, dir_fd=dir_fd)


async def stat(
    path: int | AnyStr | PathLike[AnyStr],
    *,
    dir_fd: int | None = None,
    follow_symlinks: bool = True,
) -> stat_result:
    """Get the status of a file or a file descriptor.

    See Also
    --------
    * `os.stat`.
    """
    awaitified = awaitify(py313_os.stat)
    return await awaitified(path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)


async def symlink(
    src: AnyStr | PathLike[AnyStr],
    dst: AnyStr | PathLike[AnyStr],
    target_is_directory: bool = False,
    *,
    dir_fd: int | None = None,
) -> None:
    """Create a symbolic link pointing to `src` named `dst`.

    See Also
    --------
    * `os.symlink`.
    """
    awaitified = awaitify(py313_os.symlink)
    return await awaitified(src, dst, target_is_directory=target_is_directory, dir_fd=dir_fd)


async def truncate(path: int | AnyStr | PathLike[AnyStr], length: int) -> None:
    """Truncate the file corresponding to `path`, so that it is at most `length` bytes in size.

    See Also
    --------
    * `os.truncate`.
    """
    awaitified = awaitify(py313_os.truncate)
    return await awaitified(path, length)


async def umask(mask: int, /) -> int:
    """Set the current numeric umask and return the previous umask.

    See Also
    --------
    * `os.umask`.
    """
    awaitified = awaitify(py313_os.umask)
    return await awaitified(mask)


async def unlink(path: AnyStr | PathLike[AnyStr], *, dir_fd: int | None = None) -> None:
    """Remove the file `path`.

    See Also
    --------
    * `os.unlink`.
    """
    awaitified = awaitify(py313_os.unlink)
    return await awaitified(path, dir_fd=dir_fd)


async def urandom(size: int, /) -> bytes:
    """Return a bytestring of `size` random bytes suitable for cryptographic use.

    See Also
    --------
    * `os.urandom`.
    """
    awaitified = awaitify(py313_os.urandom)
    return await awaitified(size)


async def write(fd: int, buffer: Buffer, /) -> int:
    """Write the bytestring in str to file descriptor fd.

    See Also
    --------
    * `os.write`.
    """
    awaitified = awaitify(py313_os.write)
    return await awaitified(fd, buffer)


supports_dir_fd: set[Callable[..., Any]] = set()

if py313_os.access in py313_os.supports_dir_fd:
    supports_dir_fd.add(access)

if py313_os.chmod in py313_os.supports_dir_fd:
    supports_dir_fd.add(chmod)

if py313_os.stat in py313_os.supports_dir_fd:
    supports_dir_fd.add(stat)

if py313_os.link in py313_os.supports_dir_fd:
    supports_dir_fd.add(link)

if py313_os.mkdir in py313_os.supports_dir_fd:
    supports_dir_fd.add(mkdir)

if py313_os.readlink in py313_os.supports_dir_fd:
    supports_dir_fd.add(readlink)

if py313_os.rename in py313_os.supports_dir_fd:
    supports_dir_fd.add(rename)

if py313_os.symlink in py313_os.supports_dir_fd:
    supports_dir_fd.add(symlink)

if py313_os.unlink in py313_os.supports_dir_fd:
    supports_dir_fd.add(unlink)

if py313_os.rmdir in py313_os.supports_dir_fd:
    supports_dir_fd.add(rmdir)


supports_effective_ids: set[Callable[..., Any]] = set()

if py313_os.access in py313_os.supports_effective_ids:
    supports_effective_ids.add(access)


supports_fd: set[Callable[..., Any]] = set()

if py313_os.chdir in py313_os.supports_fd:
    supports_fd.add(chdir)

if py313_os.chmod in py313_os.supports_fd:
    supports_fd.add(chmod)

if py313_os.chmod in py313_os.supports_fd:
    supports_fd.add(chmod)

if py313_os.listdir in py313_os.supports_fd:
    supports_fd.add(listdir)

if py313_os.stat in py313_os.supports_fd:
    supports_fd.add(stat)

if py313_os.truncate in py313_os.supports_fd:
    supports_fd.add(truncate)


supports_follow_symlinks: set[Callable[..., Any]] = set()

if py313_os.stat in py313_os.supports_follow_symlinks:
    supports_follow_symlinks.add(stat)

if py313_os.chmod in py313_os.supports_follow_symlinks:
    supports_follow_symlinks.add(chmod)

if py313_os.link in py313_os.supports_follow_symlinks:
    supports_follow_symlinks.add(link)

if py313_os.stat in py313_os.supports_follow_symlinks:
    supports_follow_symlinks.add(stat)

if py313_os.stat in py313_os.supports_follow_symlinks:
    supports_follow_symlinks.add(stat)

if py313_os.stat in py313_os.supports_follow_symlinks:
    supports_follow_symlinks.add(stat)


access.__module__ = __aiostdlib__
chdir.__module__ = __aiostdlib__
chmod.__module__ = __aiostdlib__
close.__module__ = __aiostdlib__
closerange.__module__ = __aiostdlib__
fstat.__module__ = __aiostdlib__
ftruncate.__module__ = __aiostdlib__
getcwd.__module__ = __aiostdlib__
getcwdb.__module__ = __aiostdlib__
getcwd.__module__ = __aiostdlib__
getcwdb.__module__ = __aiostdlib__
isatty.__module__ = __aiostdlib__
link.__module__ = __aiostdlib__
listdir.__module__ = __aiostdlib__
lseek.__module__ = __aiostdlib__
lstat.__module__ = __aiostdlib__
makedirs.__module__ = __aiostdlib__
mkdir.__module__ = __aiostdlib__
read.__module__ = __aiostdlib__
readlink.__module__ = __aiostdlib__
remove.__module__ = __aiostdlib__
removedirs.__module__ = __aiostdlib__
rename.__module__ = __aiostdlib__
renames.__module__ = __aiostdlib__
rmdir.__module__ = __aiostdlib__
stat.__module__ = __aiostdlib__
symlink.__module__ = __aiostdlib__
truncate.__module__ = __aiostdlib__
unlink.__module__ = __aiostdlib__
urandom.__module__ = __aiostdlib__
write.__module__ = __aiostdlib__
