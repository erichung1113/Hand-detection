import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose
pose=mp_pose.Pose()
conn=mp_pose.POSE_CONNECTIONS #set which two dots should be connected
drawing_spec1=mp_drawing.DrawingSpec(color=(225,225,225)) #line
drawing_spec2=mp_drawing.DrawingSpec(color=(225,225,0)) #dot

cap=cv2.VideoCapture(0)
while cap.isOpened():
    success,frame=cap.read()
    if success:
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=pose.process(image) #detect pose
        if result.pose_landmarks:
            mp_drawing.draw_landmarks(frame,result.pose_landmarks,conn,drawing_spec2,drawing_spec1) #draw dot and line on each frame
        
        cv2.imshow("windows",frame)
        if cv2.waitKey(5)==27:
            break

cap.release()
