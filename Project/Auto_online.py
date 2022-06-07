import datetime
import time
import mouse 

def get_time():
    now = datetime.datetime.now()
    ts = now.strftime('%H%M')
    return ts

def physics():
    mouse.move(521,1050)
    mouse.click()
    time.sleep(2)
    mouse.move(987,81)
    mouse.click()
    time.sleep(7)
    mouse.move(691,739)
    mouse.click()
    time.sleep(2)
    mouse.move(1253,578)
    mouse.click()
    time.sleep(2)
    
    mouse.move(301,22)
    mouse.click()
    time.sleep(2)
    mouse.move(1038,72)
    mouse.click()
    time.sleep(7)
    mouse.move(691,739)
    mouse.click()
    time.sleep(2)
    mouse.move(1253,578)
    mouse.click()

def close():
    mouse.move(1906,8)
    mouse.click()

while True:
    nowTime=get_time()
    print(nowTime)

    if nowTime=="0910":
        physics()
    if nowTime=="1000":
        close()

    time.sleep(60)
