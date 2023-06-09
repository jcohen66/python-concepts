# Functions are first class citizens.
def compose(f, g, x):
    return f(g(x))


compose(print, len, "Hello World!")

import random


def random_power():
    def f(x):
        return x**2

    def g(x):
        return x**3

    def h(x):
        return x**4

    functions = [f, g, h]
    return random.choice(functions)


if __name__ == "__main__":
    for i in range(10):
        p = random_power()
        print(p(3))
