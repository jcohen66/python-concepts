import timeit
import random


def test1():
    for i in range(1_000):
        random.random()


def test2():
    # Copy the reference
    random_num = random.random

    for i in range(1_000):
        random_num()


if __name__ in "__main__":
    print("Running tests...")
    dot_not = min(timeit.repeat(test1, repeat=10, number=10_000))
    ref = min(timeit.repeat(test2, repeat=10, number=10_000))
    print(f"Dot notation: {dot_not}")
    print(f"Reference: {ref}")

    percent_faster = (1 - (ref / dot_not)) * 100
    print(f"{(round(percent_faster, 2)):,}% faster")
