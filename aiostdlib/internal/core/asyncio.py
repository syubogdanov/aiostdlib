import sys

from asyncio import get_running_loop, iscoroutinefunction
from collections.abc import Awaitable, Callable
from contextvars import copy_context
from functools import partial
from typing import Any, TypeVar

from aiostdlib.internal.core.executor import get_thread_executor
from aiostdlib.internal.core.workers import workers_enabled


if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec


ReturnT = TypeVar("ReturnT")
ParamsT = ParamSpec("ParamsT")


async def to_thread(
    func: Callable[ParamsT, ReturnT],
    /,
    *args: ParamsT.args,
    **kwargs: ParamsT.kwargs,
) -> ReturnT:
    """Asynchronously run function `func` in a separate thread.

    Notes
    -----
    * Uses the `aiostdlib` executor, not the default one.
    """
    loop = get_running_loop()
    context = copy_context()
    executor = get_thread_executor()
    func_call = partial(context.run, func, *args, **kwargs)
    return await loop.run_in_executor(executor, func_call)


async def pseudo_to_thread(
    func: Callable[ParamsT, ReturnT],
    /,
    *args: ParamsT.args,
    **kwargs: ParamsT.kwargs,
) -> ReturnT:
    """Wrap the function in a coroutine, but execute synchronously."""
    return func(*args, **kwargs)


def awaitify(func: Callable[ParamsT, ReturnT]) -> Callable[ParamsT, Awaitable[ReturnT]]:
    """Make function `func` asynchronous."""
    awaitifier = to_thread if workers_enabled() else pseudo_to_thread
    return lambda *args, **kwargs: awaitifier(func, *args, **kwargs)


def maybe_awaitify(func: Callable[ParamsT, ReturnT]) -> Callable[ParamsT, Awaitable[Any]]:
    """Make function `func` asynchronous if it is not already.

    Notes
    -----
    * Use `Awaitable[Any]` as the return type to avoid type-checking issues.
    """
    return func if iscoroutinefunction(func) else awaitify(func)
