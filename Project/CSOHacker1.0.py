'''
CSOHacker 1.0
Operation manaul:
1.open CSO and enter the game
2.run this programe
3.return to the game
4.when you see "detection start" on terminal,please press ESC
5.click left mouse button,notice that don't move your mouse
6.then you will see "successfully"
7.return to the game,and enjoy it
'''

import ctypes,sys,cv2,pyautogui,mss,time
import mediapipe as mp
import numpy as np
from pynput.mouse import Listener

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    mp_drawing=mp.solutions.drawing_utils
    mp_pose=mp.solutions.pose
    pose=mp_pose.Pose(min_detection_confidence=0.8)
    conn=mp_pose.POSE_CONNECTIONS
    drawing_spec1=mp_drawing.DrawingSpec(color=(225,225,225))
    drawing_spec2=mp_drawing.DrawingSpec(color=(225,225,0))

    click=False
    xc,yc=(0,0)
    def clicked(x, y, button, is_press):
        if is_press:
            global click,xc,yc
            xc=x
            yc=y
            click=True

    listener = Listener(on_click=clicked)
    time.sleep(4)
    print("detection start")
    listener.start()
    while True:
        if click:
            listener.stop()
            print("successfully")
            break
    
    lux=xc-300
    luy=yc-300
    
    w=600
    h=600
    monitor={'left':lux,'top':luy,'width':w,'height':h}
    sct=mss.mss()

    while True:
        image=np.array(sct.grab(monitor))
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result=pose.process(image)

        if result.pose_landmarks:
            #mp_drawing.draw_landmarks(image,result.pose_landmarks,conn,drawing_spec2,drawing_spec1)
            for i,lm in enumerate(result.pose_landmarks.landmark):
                xPos=int(lm.x*w)
                yPos=int(lm.y*h)

                if(i==0):
                    Tox=xPos+lux
                    Toy=yPos+luy
                    pyautogui.moveTo(Tox,Toy)
                    pyautogui.click()
                    break
        
        #image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        #cv2.imshow("windows",image)
        if cv2.waitKey(1)==27:
            break
            
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

