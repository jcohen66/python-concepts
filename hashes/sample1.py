int_val = 4
str_val = "Python is best"
flt_val = 24.56

print("Integer hash is:", hash(int_val))
print("string hash is:", hash(str_val))
print("Float hash is:", hash(flt_val))

# tuples are immutable
tuple_val = (1, 2, 3, 4, 5)

# lists are mutable so cant be hashed
list_val = [1, 2, 3, 4, 5]

print("Tuple hash is:", hash(tuple_val))
print("List hash is:", hash(list_val))
