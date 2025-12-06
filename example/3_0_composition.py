from typing import Callable


def compose(f: Callable[[str], str], g: Callable[[str], str]) -> Callable[[str], str]:
    return lambda x: f(g(x))


trim_lower = compose(str.lower, str.strip)

print(trim_lower("   HELLO "))
