from toolz import pipe

email: str = "   MyEmail@EX.com "
cleaned: str = pipe(email, str.strip, str.lower)

print(cleaned)
