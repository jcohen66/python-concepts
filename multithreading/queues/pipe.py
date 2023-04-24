from multiprocessing import Pipe

a, b = Pipe()

a.send([1, "hello", None])
r = b.recv()
print(r)

b.send_bytes(b"thank you")
r = a.recv_bytes()
print(r)

import array

arr1 = array.array("i", range(5))
arr2 = array.array("i", [0] * 10)
a.send_bytes(arr1)
count = b.recv_bytes_into(arr2)
assert count == len(arr1) * arr1.itemsize
print(arr2)
