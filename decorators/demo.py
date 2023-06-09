from functools import wraps, cache
from timed import timer


def do_nothing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        return f(args, kwargs)

    return inner


@do_nothing
def alpha(*args, **kwargs):
    """A function for viewing arguments."""
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")


alpha("a", 2, None, x=7, y=11, z=28)
print(alpha.__name__)
print(alpha.__doc__)


@cache
def fibonacci(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError(f"{n} is not a positive integer")

    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@timer
def global_fibonacci(n):
    return fibonacci(n)


for i in range(1, 34):
    nth_term = global_fibonacci(i)
    print(f"fibonacci({i}) = {nth_term}")
