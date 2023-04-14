import time
from contextlib import contextmanager

def kill_time():
    time.sleep(2)
    

@contextmanager
def timer(label: str):
    start: float = time.perf_counter()
    try:
        # Lets the context manager run while
        # performing the timing.
        yield
    finally:
        end: float = time.perf_counter()
        print(f'{label}: {end - start:.3f} secs')
        
with timer('Took ') as t:
    kill_time()