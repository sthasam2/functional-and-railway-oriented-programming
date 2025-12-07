from typing import Set

DATABASE: Set[str] = {"test@example.com"}


def signup(email: str) -> str:
    # trim
    email = email.strip()

    # lowercase
    email = email.lower()

    # length check
    if len(email) < 5:
        return "Error: email too short"

    # exists check
    if email in DATABASE:
        return "Error: email already registered"

    DATABASE.add(email)
    return "Signup successful"


print(signup("   Test@example.com  "))
