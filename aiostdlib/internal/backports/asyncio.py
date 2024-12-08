from __future__ import annotations

import sys

from typing import TYPE_CHECKING


__all__: list[str] = ["to_thread"]


if sys.version_info >= (3, 9):
    from asyncio import to_thread

else:
    from asyncio.events import get_running_loop
    from contextvars import copy_context
    from functools import partial
    from typing import TypeVar

    from aiostdlib.internal.backports.typing import ParamSpec

    if TYPE_CHECKING:
        from collections.abc import Callable


    P = ParamSpec("P")
    R = TypeVar("R")


    async def to_thread(func: Callable[P, R], /, *args: P.args, **kwargs: P.kwargs) -> R:
        """Asynchronously run the function in a separate thread."""
        loop = get_running_loop()
        context = copy_context()
        call = partial(context.run, func, *args, **kwargs)
        return await loop.run_in_executor(None, call)
