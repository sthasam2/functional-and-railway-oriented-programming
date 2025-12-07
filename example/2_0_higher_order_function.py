from typing import Callable, Set

Validator = Callable[[str], bool]


def min_length(n: int) -> Validator:
    def check(value: str) -> bool:
        return len(value) >= n

    return check


def not_in(db: Set[str]) -> Validator:
    def check(value: str) -> bool:
        return value not in db

    return check


DATABASE: Set[str] = {"test@example.com"}

validators: list[Validator] = [min_length(5), not_in(DATABASE)]
