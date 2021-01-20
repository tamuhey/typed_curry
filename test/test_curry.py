from typing import Any, Callable, Dict, OrderedDict

from typed_curry import curry


@curry
def f1(x: int) -> str:
    return str(x)


def test_one():
    ret: str = f1(20)
    assert f1.fn(20) == ret


@curry
def f2(x: int, y: str) -> float:
    return float(x) * float(y)


def test_two():
    x0, x1 = 10, "9"
    _f: Callable[[str], float] = f2(x0)
    y: float = _f(x1)
    assert f2.fn(x0, x1) == y
    y1: float = f2(x0, x1)
    assert y == y1


@curry
def f5(x0: int, x1: dict, x2: list, x3: float, x4: str) -> Dict:
    d: Dict[str, Any] = dict()
    d["x0"] = x0
    d["x1"] = x1
    d["x2"] = x2
    d["x3"] = x3
    d["x4"] = x4
    return d


def test_five():
    x0, x1, x2, x3, x4 = 10, {}, [], 1.2, "foo"

    g0: Callable[[int, dict, list, float, str], dict] = f5
    g1: Callable[[dict, list, float, str], dict] = f5("foo")
