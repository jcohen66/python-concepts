import math

first: float = 0.1
second: float = 0.2
third: float = 0.3

def compare_floats(a: float, b: float, tol: float) -> float:
    absolute: float = abs(a-b)
    print(f"{a} - {b} = {a - b}")
    return absolute < tol

# Custom
print(compare_floats(first + second, third, tol=1e-10))

# Built in
print(math.isclose(first + second, third, rel_tol=1e-10))