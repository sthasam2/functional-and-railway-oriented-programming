from typing import Set

from returns.curry import curry
from returns.result import Failure, Result, Success

DATABASE: Set[str] = {"test@example.com"}


def trim(email: str) -> Result[str, str]:
    return Success(email.strip())


def lower(email: str) -> Result[str, str]:
    return Success(email.lower())


@curry
def validate_length(min_len: int, email: str) -> Result[str, str]:
    if len(email) < min_len:
        return Failure(f"Too short, must be ≥ {min_len}")
    return Success(email)


@curry
def validate_available(db: Set[str], email: str) -> Result[str, str]:
    if email in db:
        return Failure("Already exists")
    return Success(email)


@curry
def insert(db: Set[str], email: str) -> Result[str, str]:
    db.add(email)
    return Success(f"Signup successful: {email}")


def signup(email: str) -> Result[str, Exception]:
    return trim(email).bind(lower).bind(validate_length(5)).bind(validate_available(DATABASE)).bind(insert(DATABASE))


print(signup("   Hello@EX.com  "))
print(signup("test@example.com"))
print(signup("abc"))
