def some_expensive_calculation(value):
    return 10 + value


value = some_expensive_calculation(5)
if value > 10:
    print(value)

# Walrus allows to calc and assign the value in one go.
if (value := some_expensive_calculation(5)) > 10:
    print(value)

numbers = [1, 2, 3, 4]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num**2)
print(squared_numbers)

# Use list comprehension instead
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

squared_even_numbers = [num**2 for num in numbers if num % 2 == 0]
print(squared_even_numbers)

my_list = [1, 2, 3, 4]
for index, element in enumerate(my_list):
    print(f"Element {element} is at index {index}")

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
