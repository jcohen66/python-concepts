# pip install scheduler
import helper

import schedule
import time


def task():
    print("Doing task ...", helper.get_time())

job = schedule.every().monday.at('15:15').do(task)

print(schedule.get_jobs())

schedule.cancel_job(job)

print(schedule.get_jobs())

while True:
    schedule.run_pending()
    time.sleep(1)