numbers = [1, 3, 5, 7, 9]
find = 4

for num in numbers:
    if num == find:
        print(f"Found {find} in the list.")
        break
else:
    # This block will execute only if the loop completed
    print(f"{find} was not found in the list")


count = 5

while count > 0:
    print(count)
    count -= 1
else:
    # this block will execute once the condition in the while statement is no longer True.abs
    print("Liftoff!")
