import math
import time
import resource
import sys

time_start = time.perf_counter()

sys.set_int_max_str_digits(0)

def factorial(n):
  return math.factorial(n)

test_list = list(range(1, 100000))
result = []
for i in range(len(test_list)):
  if test_list[i] % 2 == 0:
    result.append(test_list[i])
print(sum(result))

time_elapsed = (time.perf_counter() - time_start)
memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

print ("%f secs %f MByte" % (time_elapsed,memMb))
