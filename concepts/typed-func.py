import time
from typing import Callable

# Parameters are other functions, we
# define them as Callable. 
def calc_time(func: Callable):
    start = time.time()
    func()
    end = time.time()
    print(f"Execution time: {end - start}s")
    
calc_time(lambda: sorted(range(0,1000000)))