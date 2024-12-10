from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, TypeVar

from aiostdlib.internal.backports.asyncio import to_thread
from aiostdlib.internal.backports.typing import ParamSpec


if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable


__all__: list[str] = ["to_awaitable"]


P = ParamSpec("P")
R = TypeVar("R")


def to_awaitable(function: Callable[P, R]) -> Callable[P, Awaitable[R]]:
    """Make the function call awaitable.

    See Also
    --------
    * `asyncio.to_thread`.
    """
    @wraps(function)
    async def run_in_thread(*args: P.args, **kwargs: P.kwargs) -> R:
        return await to_thread(function, *args, **kwargs)
    return run_in_thread
