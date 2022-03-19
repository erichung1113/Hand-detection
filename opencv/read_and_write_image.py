import cv2 #import opencv

imgname="hand" #image name
img=cv2.imread(imgname+".jpg") #use opencv to read image(hand.jpg) and put into img

cv2.imshow("window",img) #create a window and show img,firat variable is window's name,second one is picture
cv2.waitKey(0) #wait until hitting keyboard
cv2.destroyAllWindows() #close all windows
cv2.imwrite(imgname+"01.png",img) #export picture
