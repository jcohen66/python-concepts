# Expensive function
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


# Generator
counter = count_up_to(5)

# iterate over generator
for value in counter:
    print(value)
