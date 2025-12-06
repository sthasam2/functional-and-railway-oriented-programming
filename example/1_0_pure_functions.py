from typing import Set

DATABASE: Set[str] = {"test@example.com"}

def trim(email: str) -> str:
    return email.strip()

def lower(email: str) -> str:
    return email.lower()

def validate_length(email: str) -> bool:
    return len(email) >= 5

def exists(email: str) -> bool:
    return email in DATABASE

def signup(email: str) -> str:
    e: str = trim(email)
    e = lower(e)

    if not validate_length(e):
        return "Error: email too short"

    if exists(e):
        return "Error: already registered"

    DATABASE.add(e)
    return "Signup successful"

print(signup("  NEW@example.com "))
