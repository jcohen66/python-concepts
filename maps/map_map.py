# Using Map

import math
import time
import resource
import sys

time_start = time.perf_counter()

sys.set_int_max_str_digits(0)

def factorial(n):
   return math.factorial(n)

test_list = list(range(1, 10000))
result = map(factorial, test_list)
print(sum((result)))

time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

print ("%f secs %f MByte" % (time_elapsed,memMb))
