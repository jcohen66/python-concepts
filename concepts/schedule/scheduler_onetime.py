# pip install scheduler
import helper

import schedule
import time


def task():
    print("Doing task ...", helper.get_time())
    return schedule.CancelJob

schedule.every(5).minutes.do(task).tag('work', 1)
schedule.every(5).hours.do(task).tag('fun', 1)
schedule.every(5).days.do(task).tag('work', 2)
schedule.every(5).weeks.do(task).tag('fun', 2)

# Filter by tag
fun = schedule.get_jobs('fun')
work = schedule.get_jobs('work')

print(fun)
print(work)

while True:
    schedule.run_pending()
    # schedule.clear('fun')
    time.sleep(1)
    
    print('Jobs: ', len(schedule.get_jobs()))
    schedule.clear()