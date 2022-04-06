'''
CSOHacker 2.0
Operation manaul:
1.open CSO and enter the game
2.run this programe
3.return to the game in 5 seconds
5.enjoy it
'''

import ctypes,sys,cv2,mss,time
import mediapipe as mp
import numpy as np
import pyautogui as pag

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    #get center coordinate
    time.sleep(5)
    cPos=pag.position()
    
    #set detection area 
    lux=cPos.x-300
    luy=cPos.y-300
    w=600
    h=600

    #set mediapipe pose detection
    mp_pose=mp.solutions.pose
    pose=mp_pose.Pose(min_detection_confidence=0.8)

    def get_head_coordinate(x):
        for i,lm in enumerate(x):
            pos=lm
            pos.x=int(pos.x*w)+lux
            pos.y=int(pos.y*h)+luy-30 #adjustive difference
            return pos

    #set screenshot border
    monitor={'left':lux,'top':luy,'width':w,'height':h}
    sct=mss.mss()

    while True:
        #screenshot
        image=np.array(sct.grab(monitor))
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result=pose.process(image) #analyze person

        if result.pose_landmarks: #if there is person in shooting area
            #move to head and click
            head=get_head_coordinate(result.pose_landmarks.landmark)
            pag.click(x=head.x,y=head.y)

            #pag.moveTo(head.x,head.y) #move without shot

        if cv2.waitKey(1)==27:
            break

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

