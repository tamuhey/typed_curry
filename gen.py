import black


def gen_header() -> str:
    return """
from functools import partial
from typing import Callable, Generic, NoReturn, TypeVar, overload

"""


class Gen:
    def __init__(self, n: int):
        self.n = n
        self.arg_types = [f"_T{i}" for i in range(n)]
        self.ret_type = "_R"
        self.script = ""
        self.indent = 0

    def __call__(self) -> str:
        self.push(gen_header())
        self.gen_typevar()
        self.gen_curry()
        return self.script

    def push(self, lines: str):
        p = " " * self.indent
        for line in lines.split("\n"):
            self.script += p + line + "\n"

    def gen_typevar(self):
        for t in self.arg_types + [self.ret_type]:
            self.push(f'{t} = TypeVar("{t}")')

    def gen_curry(self):
        types = ", ".join(self.arg_types + [self.ret_type])
        self.push(f"class curry(Generic[{types}]):")
        self.indent += 4

        calls = []
        for i in range(self.n):

            s_arg_type = ", ".join(
                self.arg_types[: i + 1] + ["NoReturn"] * (self.n - i - 1)
            )
            s_self_type = s_arg_type + ", " + self.ret_type

            # __init__
            self.push("@overload")
            self.push(
                f'def __init__(self: "curry[{s_self_type}]", fn: Callable[[{", ".join(self.arg_types[:i+1])}], {self.ret_type}]): ...'
            )

            # __call__
            args = ""
            for j in range(i + 1):
                t = self.arg_types[j]
                args += f", x{j}: {t}"
                calls.append("@overload")
                if i == j:
                    ret_type = self.ret_type
                else:
                    s_curry = ", ".join(
                        self.arg_types[j + 1 : i + 1]
                        + ["NoReturn"] * (self.n - i + j)
                        + [self.ret_type]
                    )
                    ret_type = f'"curry[{s_curry}]"'
                calls.append(
                    f'def __call__(self: "curry[{s_self_type}]" {args}) -> {ret_type}: ...\n'
                )

        self.push(
            """
def __init__(self, fn):
    self.fn = fn"""
        )

        calls.append(
            """
def __call__(self, *args):
    try:
        return self.fn(*args)
    except:
        return curry(partial(self.fn, *args))"""
        )
        for line in calls:
            self.push(line)


if __name__ == "__main__":
    ret = Gen(5)()
    ret = black.format_str(ret, mode=black.Mode())
    print(ret)
