# Using while loop

import math
import time
import resource
import sys

time_start = time.perf_counter()

sys.set_int_max_str_digits(0)

def addition(x,y):
    return x + y

test_list = list(range(1, 1000000))

result = 0
i=0
while i < len(test_list) :
      result = addition(result, test_list[i]) 
      i = i + 1 
print(result)

time_elapsed = (time.perf_counter() - time_start)
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0

print ("%f secs %f MByte" % (time_elapsed,memMb))