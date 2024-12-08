from collections.abc import Awaitable, Callable
from functools import wraps
from typing import TypeVar

from aiostdlib.internal.backports.asyncio import to_thread
from aiostdlib.internal.backports.typing import ParamSpec


P = ParamSpec("P")
R = TypeVar("R")


def to_async(function: Callable[P, R]) -> Callable[P, Awaitable[R]]:
    """Make the function asynchronous.

    See Also
    --------
    * `asyncio.to_thread`.
    """
    @wraps(function)
    async def run_in_thread(*args: P.args, **kwargs: P.kwargs) -> R:
        return await to_thread(function, *args, **kwargs)
    return run_in_thread
