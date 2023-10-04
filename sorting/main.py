# standard sort returns sorted copy
cities = ["San Diego", "Philadelphia", "Spokane", "Austin"]
sorted_cities = sorted(cities)

print(cities)
print(sorted_cities)

# Find the n smallest elements
from heapq import nsmallest
subset = nsmallest(2, cities)
print(subset)

# Quick way to find an element
from bisect import bisect_left
subset_left = bisect_left(sorted_cities, "San Diego")
print(subset_left)
print(sorted_cities[2])
