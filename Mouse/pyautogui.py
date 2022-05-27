import pyautogui as pag

image_resolution=pag.size() #1920*1080

pos=pag.position() #get mouse position
print(pos.x,pos.y) #x,y coordinate

pag.moveTo(100,100) #move to (100,100)
pag.moveTo(10,10,2) #move to (0,0) in 2 seconds

pag.move(50,0) #move the mouse right 50 pixels

pag.drag(100,200,2,button="left") #drag mouse 100 pixels right and 200 pixels down over 2 seconds while holding down left mouse button

pag.click(x=100,y=200,button="right") #move to (100,200),then click the left mouse button

pag.click(clicks=2) #double-click the left mouse button =below
pag.doubleClick()

pag.scroll(-50) #scroll down 50 clicks(=1 time)

pag.typewrite(['1','3','enter']) #keyboard input
