# pip install scheduler
import helper

import schedule
import time

from schedule import repeat, every

# Using decorator.
@repeat(every(5).seconds, 5, "Mario")
@repeat(every(6).seconds, 5, "Luigi")
def repeat_task(arg1, arg2):
    print("Doing task ...", f'args = {arg1, arg2}', helper.get_time())

def task(arg1, arg2):
    print("Doing task ...", f'args = {arg1, arg2}', helper.get_time())


schedule.every().seconds.do(task, "10", "Luigi")

        
while True:
    schedule.run_pending()
    time.sleep(1)