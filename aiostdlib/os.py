from aiostdlib.internal.stdlib.os import (
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
    access,
    altsep,
    chdir,
    chmod,
    close,
    closerange,
    curdir,
    defpath,
    devnull,
    error,
    extsep,
    fsdecode,
    fsencode,
    fspath,
    fstat,
    ftruncate,
    get_exec_path,
    getcwd,
    getcwdb,
    isatty,
    linesep,
    link,
    listdir,
    lseek,
    lstat,
    makedirs,
    mkdir,
    name,
    open,
    pardir,
    pathsep,
    read,
    readlink,
    remove,
    removedirs,
    rename,
    renames,
    replace,
    rmdir,
    sep,
    stat,
    stat_result,
    strerror,
    supports_dir_fd,
    supports_effective_ids,
    supports_fd,
    supports_follow_symlinks,
    symlink,
    terminal_size,
    truncate,
    umask,
    unlink,
    urandom,
    write,
)


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
