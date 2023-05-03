from collections import Counter

one = [33,22,11,44,55]
two = [22,12,44,55,33]

print(f"Is two lists are equal: {Counter(one) == Counter(two)}")