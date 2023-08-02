import numpy as np

# a = np.zeros((3,3), dtype=np.int64)
a = np.zeros((3,3))
a[:] = 2
print(a.dtype)
a.fill(8)
print(a)
a += 3
print(a)


b = np.arange(1, 10).reshape((3,3))
print(b.dtype)
print(b)

array_sum = a.sum()
array_sum = b.sum(axis=0)
array_sum = b.sum(axis=1)

print(array_sum)

array_product = b.prod()
array_product = b.mean()
print(array_product)

array_max, array_min = b.max(), b.min()
print(array_max, array_min)
# end main