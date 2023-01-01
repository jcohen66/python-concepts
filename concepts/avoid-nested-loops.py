from timeit import default_timer as timer

start = timer()
# list_a = [1, 2020, 70]
# list_b = [2, 4, 7, 2000]
# list_c = [3, 70, 7]

list_a = range(0, 200000)
list_b = range(0, 1000)
list_c = range(0, 3)

for a in list_a:
    for b in list_b:
        for c in list_c:
            if a + b + c == 20700007:
                print(a, b, c)
end = timer()
print("Nested loops: ", end - start)

# Using product to collapse nested loops
start = timer()
from itertools import product

for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 20700007:
        print(a, b, c)

end = timer()
print("Product: ", end - start)
