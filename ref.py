from functools import partial
from typing import Any, Callable, Generic, NoReturn, TypeVar, overload

T0 = TypeVar("T0")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")
R = TypeVar("R")


class curry(Generic[T0, T1, R]):
    @overload
    def __init__(self: "curry[T0,NoReturn,R]", fn: Callable[[T0], R]):
        ...

    @overload
    def __init__(self: "curry[T0,T1,R]", fn: Callable[[T0, T1], R]):
        ...

    def __init__(self, fn):
        self.fn = fn

    @overload
    def __call__(self: "curry[T0,NoReturn,R]", x: T0) -> R:
        ...

    @overload
    def __call__(self: "curry[T0,T1,R]", x: T0) -> Callable[[T1], R]:
        ...

    @overload
    def __call__(self: "curry[T0,T1,R]", x0: T0, x1: T1) -> R:
        ...

    def __call__(self, *args):
        try:
            return self.fn(*args)
        except:
            return curry(partial(self.fn, *args))
