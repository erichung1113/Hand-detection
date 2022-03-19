import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_face_mesh=mp.solutions.face_mesh

cap=cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh() as face_mesh:
    while True:
        succ,frame=cap.read()
        if succ:
            frame=cv2.flip(frame,1)
            img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            result=face_mesh.process(img)

            #It only can detect one face ,so I don't use "while" to run all faces
            face_landmarks=result.multi_face_landmarks
            if face_landmarks:
                mp_drawing.draw_landmarks(
                    image=frame, #draw on original picture(BGR)
                    landmark_list=face_landmarks[0] #first face's landmarks
                )
            
            cv2.imshow("windows",frame)
            if(cv2.waitKey(5)==27):
                break

