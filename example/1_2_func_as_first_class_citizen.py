from typing import Callable, Iterable, Set

Step = Callable[[str], str]

def apply_steps(value: str, steps: Iterable[Step]) -> str:
    for fn in steps:
        value = fn(value)
    return value

DATABASE: Set[str] = {"test@example.com"}

clean_pipeline: list[Step] = [str.strip, str.lower]

def signup(email: str) -> str:
    cleaned: str = apply_steps(email, clean_pipeline)

    if len(cleaned) < 5:
        return "Error: too short"

    if cleaned in DATABASE:
        return "Error: exists"

    DATABASE.add(cleaned)
    return "OK"

print(signup("   MyEmail@EX.com "))
