import cv2 
import mediapipe as mp
import time

cap=cv2.VideoCapture(0) #use number 0 camera
mpHands=mp.solutions.hands #use hand-detection function
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
HandLmsStyle=mpDraw.DrawingSpec(color=(0,0,255),thickness=5) #landmarks style
HandConStyle=mpDraw.DrawingSpec(color=(0,255,0),thickness=10) #connection style
pTime=0 #previous time
cTime=0 #current time

while True:
    ret,img=cap.read() #ret->capture successfully or not,img->image
    if ret:
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #change BGR to RGB
        result=hands.process(imgRGB) #find hands in image
        imgHeight=img.shape[0]
        imgWidth=img.shape[1]
        
        if result.multi_hand_landmarks: #if it detect hands
            for handLms in result.multi_hand_landmarks: #iterate all hands 
                mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS,HandLmsStyle,HandConStyle)  #draw Landmarks on image
                for i,lm, in enumerate(handLms.landmark): #iterate all point of one hand
                    xPos=int(lm.x*imgWidth) #change into real coordinates
                    yPos=int(lm.y*imgHeight) #change into real coordinates
                    if i==4:
                        cv2.circle(img,(xPos,yPos),20,(56,56,166),cv2.FILLED) #draw circle on forth point
                    print(i,xPos,yPos) #print point number and its coordinates
        
        #caculate fps
        cTime=time.time()
        fps=1/(cTime-pTime) 
        pTime=cTime
        
        cv2.putText(img,f"FPS : {int(fps)}",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3) #diaplay fps on top-left
        cv2.imshow('img',img) #print image
     
    if cv2.waitKey(1)==ord('q'): #delay 1 ms and if press 'q',stop process
        break
