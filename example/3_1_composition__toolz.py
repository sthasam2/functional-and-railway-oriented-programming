from typing import Callable
from toolz import compose

trim_lower: Callable[[str], str] = compose(str.lower, str.strip)

print(trim_lower("   HELLO "))
