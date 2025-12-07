from functools import partial
from typing import Set


def min_length(email: str, n: int) -> bool:
    return len(email) >= n


length5 = partial(min_length, n=5)
print(length5("hello"))


# Dependency injection (injecting db)


def not_in(email: str, db: Set[str]) -> bool:
    return email not in db


availability = partial(not_in, db={"test@example.com"})
print(availability("new@example.com"))
