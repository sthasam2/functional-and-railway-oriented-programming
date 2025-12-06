from __future__ import annotations
from typing import Callable, TypeVar, Generic, Optional, Set
from toolz import curry


T = TypeVar("T")
U = TypeVar("U")


class Result(Generic[T]):
    def __init__(
        self, value: Optional[T], is_success: bool, error: Optional[Exception] = None
    ):
        self.value = value
        self.is_success = is_success
        self.error = error

    @classmethod
    def success(cls, v: T) -> "Result[T]":
        return cls(v, True)

    @classmethod
    def failure(cls, e: Exception) -> "Result[T]":
        return cls(None, False, e)

    # Railway switch
    def bind(self, func: Callable[[T], "Result[U]"]) -> "Result[U]":
        if self.is_success:
            return func(self.value)
        return self  # propagate failure

    def __repr__(self) -> str:
        if self.is_success:
            return f"Success({self.value})"
        return f"Failure({self.error})"


DATABASE: Set[str] = {"test@example.com"}


@curry
def trim(email: str) -> Result[str]:
    try:
        return Result.success(email.strip())
    except Exception as e:
        return Result.failure(e)


@curry
def lower(email: str) -> Result[str]:
    try:
        return Result.success(email.lower())
    except Exception as e:
        return Result.failure(e)


@curry
def validate_length(min_len: int, email: str) -> Result[str]:
    try:
        if len(email) < min_len:
            raise ValueError(f"Email too short, must be ≥ {min_len}")
        return Result.success(email)
    except Exception as e:
        return Result.failure(e)


@curry
def validate_available(db: Set[str], email: str) -> Result[str]:
    try:
        if email in db:
            raise ValueError("Email already exists")
        return Result.success(email)
    except Exception as e:
        return Result.failure(e)


def insert(email: str) -> Result[str]:
    try:
        DATABASE.add(email)
        return Result.success(f"Signup successful: {email}")
    except Exception as e:
        return Result.failure(e)


def signup(email: str) -> Result[str]:
    return (
        Result.success(email)
        .bind(trim)
        .bind(lower)
        .bind(validate_length(5))
        .bind(validate_available(DATABASE))
        .bind(insert)
    )


print(signup("   new@EXAMPLE.com  "))  # Success
print(signup("test@example.com"))  # Failure: already exists
print(signup("abc"))  # Failure: too short
