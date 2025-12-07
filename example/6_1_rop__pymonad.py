from pymonad.either import Left, Right
from pymonad.tools import curry

DATABASE = {"test@example.com"}

# -----------------------------
# Step functions
# -----------------------------


def trim(email: str):
    try:
        return Right(email.strip())
    except Exception as e:
        return Left(f"Error trimming email: {e}")


def lower(email: str):
    try:
        return Right(email.lower())
    except Exception as e:
        return Left(f"Error converting to lowercase: {e}")


@curry(2)
def validate_length(min_len: int, email: str):
    if len(email) < min_len:
        return Left(f"Email too short (min {min_len})")
    return Right(email)


@curry(2)
def validate_available(db: set, email: str):
    if email in db:
        return Left("Email already exists")
    return Right(email)


@curry(2)
def insert(db: set, email: str):
    db.add(email)
    return Right(f"Signup successful: {email}")


# -----------------------------
# Signup pipeline
# -----------------------------


def signup(email: str):
    return (
        Right(email)
        .then(trim)
        .then(lower)
        .then(validate_length(5))
        .then(validate_available(DATABASE))
        .then(insert(DATABASE))
    )


# -----------------------------
# Tests
# -----------------------------

print(signup("   new@ex.com  "))  # Success
print(signup("test@example.com"))  # Failure: already exists
print(signup("abc"))  # Failure: too short
