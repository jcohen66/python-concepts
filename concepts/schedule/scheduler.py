# pip install scheduler
import helper

import schedule
import time

from schedule import repeat, every

# Using decorator.
@repeat(every(10).seconds)
def repeat_task():
    print("Doing task ...", helper.get_time())

def task():
    print("Doing task ...", helper.get_time())

schedule.every(5).seconds.do(task)
schedule.every(5).minutes.do(task)
schedule.every(5).hours.do(task)
schedule.every(5).days.do(task)
schedule.every(5).weeks.do(task)

schedule.every().minute.at(':15').do(task)
schedule.every().hour.at(':15').do(task)
schedule.every().day.at('15:15').do(task)
schedule.every().day.at('15:15:40').do(task)

schedule.every().monday.do(task)
schedule.every().monday.at('15:15').do(task)


        
while True:
    schedule.run_pending()
    time.sleep(1)