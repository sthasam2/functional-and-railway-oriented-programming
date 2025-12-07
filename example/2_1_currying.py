from typing import Callable


def min_length_setter(n: int) -> Callable[[str], bool]:
    def checker(email: str):
        return len(email) >= n

    return checker


length5 = min_length_setter(5)
print(length5("abcde"))
