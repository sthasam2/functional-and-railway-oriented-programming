from typing import Callable, Set

from toolz import curry, pipe


@curry
def ensure_min_length(min_len: int, email: str) -> str:
    try:
        if len(email) < min_len:
            raise ValueError(f"Email too short, must be ≥ {min_len}")
        return email
    except Exception as e:
        raise ValueError(f"Length validation failed: {e}")


@curry
def ensure_not_exists(db: Set[str], email: str) -> str:
    try:
        if email in db:
            raise ValueError("Email already exists")
        return email
    except Exception as e:
        raise ValueError(f"Availability check failed: {e}")


@curry
def safe_cleanup(step: Callable[[str], str], email: str) -> str:
    try:
        return step(email)
    except Exception as e:
        raise ValueError(f"Cleanup step failed on '{email}': {e}")


DATABASE: Set[str] = {"test@example.com"}


check_length = ensure_min_length(5)
check_available = ensure_not_exists(DATABASE)


trim = safe_cleanup(str.strip)
lower = safe_cleanup(str.lower)


def signup(raw_email: str) -> str:
    try:
        # Cleanup pipeline
        cleaned: str = pipe(raw_email, trim, lower)

        # Run validation in order
        cleaned = check_length(cleaned)
        cleaned = check_available(cleaned)

        DATABASE.add(cleaned)
        return f"Signup successful: {cleaned}"

    except ValueError as e:
        return f"Error: {e}"
