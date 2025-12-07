from typing import Set

from returns.curry import curry
from returns.result import Result, safe

DATABASE: Set[str] = {"test@example.com"}

# Safe decorators


@safe
def trim(email: str) -> str:
    return email.strip()


@safe
def lower(email: str) -> str:
    return email.lower()


@curry
@safe
def validate_length(min_len: int, email: str) -> str:
    if len(email) < min_len:
        raise ValueError(f"Too short, must be ≥ {min_len}")
    return email


@curry
@safe
def validate_available(db: Set[str], email: str) -> str:
    if email in db:
        raise ValueError("Already exists")
    return email


@curry
@safe
def insert(db: Set[str], email: str) -> str:
    db.add(email)
    return f"Signup successful: {email}"


def signup(email: str) -> Result[str, Exception]:
    return trim(email).bind(lower).bind(validate_length(5)).bind(validate_available(DATABASE)).bind(insert(DATABASE))


print(signup("   Hello@EX.com  "))  # Success
print(signup("test@example.com"))  # Failure: Already exists
print(signup("abc"))  # Failure: Too short
