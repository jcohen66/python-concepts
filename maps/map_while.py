# Using while loop

import math
import time
import resource
import sys

time_start = time.perf_counter()

sys.set_int_max_str_digits(0)

def factorial(n):
   return math.factorial(n)

test_list = list(range(1, 10000))
result = 0
i=0
while i < len(test_list) :
    test_list[i] = factorial(test_list[i])
    i = i + 1 
print(sum(test_list))

time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

print ("%f secs %f MByte" % (time_elapsed,memMb))
