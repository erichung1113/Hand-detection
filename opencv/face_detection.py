import cv2

img=cv2.imread("picture.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #change img into gray
faceCascade=cv2.CascadeClassifier("face_detect.xml") #import trained model

faceRect=faceCascade.detectMultiScale(gray,1.1,100)
#detect face =>(image,reduction factor,number of detected count that determine whether it is face)

print(len(faceRect)) #print how many face that detected

for (x,y,w,h) in faceRect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #draw rectangle of detected face on image

cv2.imshow("windows",img)
cv2.waitKey(0)
