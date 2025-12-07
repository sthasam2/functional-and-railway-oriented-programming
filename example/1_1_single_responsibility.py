from typing import Set


def trim(email: str) -> str:
    return email.strip()


def normalize(email: str) -> str:
    return email.lower()


def is_valid_length(email: str) -> bool:
    return len(email) >= 5


def is_available(email: str, db: Set[str]) -> bool:
    return email not in db
