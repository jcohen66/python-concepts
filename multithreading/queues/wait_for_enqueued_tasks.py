import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()
        
# Turn on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send tasks to the worker.
for item in range(30):
    q.put(item)
    
# Block unto; a;; tasks are done.
q.join()
print('All work completed')