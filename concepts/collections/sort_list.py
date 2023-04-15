lst = ["Mango", 'Pineapple', "Orange", "Apple"]

# method 1
lst.sort()
print(lst)  # ['Apple', 'Mango', 'Orange', 'Pineapple']

# method 2 - generic sorting
new_lst = sorted(lst)
print(new_lst) # ['Apple', 'Mango', 'Orange', 'Pineapple']

# method 3
new_lst = sorted(lst, reverse=True)
print(new_lst)  # ['Apple', 'Mango', 'Orange', 'Pineapple']
