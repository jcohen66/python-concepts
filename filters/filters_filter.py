# Using Filter

import math
import time
import resource
import sys

time_start = time.perf_counter()

sys.set_int_max_str_digits(0)

def factorial(n):
   return math.factorial(n)

test_list = list(range(1, 100000))
result = filter(lambda x: x % 2 == 0, test_list)
print(sum((result)))

time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

print ("%f secs %f MByte" % (time_elapsed,memMb))

# Output
2499950000
0.022666 secs 1.087833 MByte
