import mouse
import time

mouse.click("left") #click left button

pos=mouse.get_position() #get mouse position
print(pos[0],pos[1]) #x,y coordinate

mouse.is_pressed("left") #return a bool that whether left button is pressed

mouse.move(100,100,duration=0) #move 

#mouse listener
mouse.on_click(lambda:print("left button clicked")) #set left button listener
mouse.on_right_click(lambda:print("right button clicked")) #set right button listener
time.sleep(3) #duration: 3  minutes
mouse.unhook_all() #stop listening,remove all listeners

mouse.wheel(-1) #scroll down one time

events=mouse.record() #record mouse events until pressing right button
mouse.play(events[:-1]) #play without right button
