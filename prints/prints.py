numbers = [1, 2, 3, 4, 5]

print("Default print:")
print(*numbers)
print(numbers)

print("\nPrint with different end character:")
print(*numbers, end=" <--- End of numbers")

print("\n\nPrint with both different sep and end")
print(*numbers, sep="->", end=" <--- End of numbers")
