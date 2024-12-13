from asyncio.coroutines import iscoroutinefunction
from asyncio.threads import to_thread
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, TypeVar

from aiostdlib.internal.backports.typing import ParamSpec


__all__: list[str] = ["to_async_if_not"]


P = ParamSpec("P")
R = TypeVar("R")


def to_async_if_not(function: Callable[P, R]) -> Callable[P, Coroutine[Any, Any, Any]]:
    """Make the function asynchronous if it was not.

    See Also
    --------
    * `asyncio.to_thread`.
    """
    if iscoroutinefunction(function):
        return function

    @wraps(function)
    async def run_in_thread(*args: P.args, **kwargs: P.kwargs) -> R:
        return await to_thread(function, *args, **kwargs)

    return run_in_thread
