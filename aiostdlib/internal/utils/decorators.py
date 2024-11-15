from asyncio import iscoroutinefunction
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, TypeVar

from aiostdlib.internal.backports.asyncio import to_thread
from aiostdlib.internal.backports.typing import ParamSpec


_P = ParamSpec("_P")
_R = TypeVar("_R")


def to_async(function: Callable[_P, _R]) -> Callable[_P, Coroutine[Any, Any, _R]]:
    """Make the function asynchronous."""
    if iscoroutinefunction(function):
        return function

    @wraps(function)
    async def run_in_thread(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        return await to_thread(function, *args, **kwargs)

    return run_in_thread
