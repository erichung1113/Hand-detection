import cv2
import numpy as np

img=np.zeros((600,600,3),np.uint8) #create a picture
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),2) #draw a line
cv2.rectangle(img,(0,0),(400,300),(0,0,255),cv2.FILLED) #draw a rectangle
cv2.circle(img,(300,400),30,(255,0,0),1) #draw a circle 
cv2.putText(img,'Hello',(100,500),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,5,(50,50,50),1) #insert text
cv2.imshow("window",img) #show the picture
cv2.waitKey(0) #wait until hitting keyboard
© 2022 GitHub, Inc.
Terms
Privacy
Security
