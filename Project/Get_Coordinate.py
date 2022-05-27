#mouse monitor
from pynput.mouse import Listener

click_times=0

def clicked(x, y, button, is_press):
    if is_press:
        print(f"({x},{y})") #print x y coordinates
        global click_times
        click_times+=1

listener = Listener(on_click=clicked) #set on_click function

listener.start() #start process

while True:
    if click_times==2: #if get coordinate
        listener.stop() #stop process
        break
