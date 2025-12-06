from toolz import curry
from typing import Callable, Set


@curry
def min_length(n: int, email: str) -> bool:
    return len(email) >= n


length5: Callable[[str], bool] = min_length(5)

print(length5("hello"))  # True
print(length5("abc"))  # False

# Dependency injection (injecting db)


@curry
def not_in(db: Set[str], email: str) -> bool:
    return email not in db


DATABASE: Set[str] = {"test@example.com"}

is_available: Callable[[str], bool] = not_in(DATABASE)

print(is_available("new@example.com"))  # True
print(is_available("test@example.com"))  # False
