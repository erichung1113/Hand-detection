import mediapipe as mp
import cv2
import time

cTime=0
pTime=0

mp_face_detection=mp.solutions.face_detection #import detected tools
mp_drawing=mp.solutions.drawing_utils #import drawing tools

cap=cv2.VideoCapture(0) #capture BGR image

with mp_face_detection.FaceDetection() as face_detection: #open FaceDetection
    while True:
        success,image=cap.read() #get camera frames
        if success:
            image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB) 
            #flip the image horizontally and convert the image BRG image to RGB
            
            results=face_detection.process(image) #need RGB image

            image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)  #convert to original style(BGR)
            
            if results.detections: #it's type is list,means if detected face
                for detection in results.detections: #iterate all faces
                    mp_drawing.draw_detection(image,detection) #mark detected face
            
            #calculate fps
            cTime=time.time()
            fps=1/(cTime-pTime)
            pTime=cTime
            cv2.putText(image,f"FPS : {int(fps)}",(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            #------------

            cv2.imshow("window",image)

            if cv2.waitKey(10)==27: #if press esc
                break

cap.release() 
