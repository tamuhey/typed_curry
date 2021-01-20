from functools import partial
from typing import Callable, Generic, NoReturn, TypeVar, overload


_T0 = TypeVar("_T0")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_R = TypeVar("_R")


class curry(Generic[_T0, _T1, _T2, _T3, _T4, _R]):
    @overload
    def __init__(
        self: "curry[_T0, NoReturn, NoReturn, NoReturn, NoReturn, _R]",
        fn: Callable[[_T0], _R],
    ):
        ...

    @overload
    def __init__(
        self: "curry[_T0, _T1, NoReturn, NoReturn, NoReturn, _R]",
        fn: Callable[[_T0, _T1], _R],
    ):
        ...

    @overload
    def __init__(
        self: "curry[_T0, _T1, _T2, NoReturn, NoReturn, _R]",
        fn: Callable[[_T0, _T1, _T2], _R],
    ):
        ...

    @overload
    def __init__(
        self: "curry[_T0, _T1, _T2, _T3, NoReturn, _R]",
        fn: Callable[[_T0, _T1, _T2, _T3], _R],
    ):
        ...

    @overload
    def __init__(
        self: "curry[_T0, _T1, _T2, _T3, _T4, _R]",
        fn: Callable[[_T0, _T1, _T2, _T3, _T4], _R],
    ):
        ...

    def __init__(self, fn):
        self.fn = fn

    @overload
    def __call__(
        self: "curry[_T0, NoReturn, NoReturn, NoReturn, NoReturn, _R]", x0: _T0
    ) -> _R:
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, NoReturn, NoReturn, NoReturn, _R]", x0: _T0
    ) -> "curry[_T1, NoReturn, NoReturn, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, NoReturn, NoReturn, NoReturn, _R]", x0: _T0, x1: _T1
    ) -> _R:
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, NoReturn, NoReturn, _R]", x0: _T0
    ) -> "curry[_T1, _T2, NoReturn, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, NoReturn, NoReturn, _R]", x0: _T0, x1: _T1
    ) -> "curry[_T2, NoReturn, NoReturn, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, NoReturn, NoReturn, _R]", x0: _T0, x1: _T1, x2: _T2
    ) -> _R:
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, NoReturn, _R]", x0: _T0
    ) -> "curry[_T1, _T2, _T3, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, NoReturn, _R]", x0: _T0, x1: _T1
    ) -> "curry[_T2, _T3, NoReturn, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, NoReturn, _R]", x0: _T0, x1: _T1, x2: _T2
    ) -> "curry[_T3, NoReturn, NoReturn, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, NoReturn, _R]",
        x0: _T0,
        x1: _T1,
        x2: _T2,
        x3: _T3,
    ) -> _R:
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, _T4, _R]", x0: _T0
    ) -> "curry[_T1, _T2, _T3, _T4, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, _T4, _R]", x0: _T0, x1: _T1
    ) -> "curry[_T2, _T3, _T4, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, _T4, _R]", x0: _T0, x1: _T1, x2: _T2
    ) -> "curry[_T3, _T4, NoReturn, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, _T4, _R]", x0: _T0, x1: _T1, x2: _T2, x3: _T3
    ) -> "curry[_T4, NoReturn, NoReturn, NoReturn, NoReturn, _R]":
        ...

    @overload
    def __call__(
        self: "curry[_T0, _T1, _T2, _T3, _T4, _R]",
        x0: _T0,
        x1: _T1,
        x2: _T2,
        x3: _T3,
        x4: _T4,
    ) -> _R:
        ...

    def __call__(self, *args):
        try:
            return self.fn(*args)
        except:
            return curry(partial(self.fn, *args))

