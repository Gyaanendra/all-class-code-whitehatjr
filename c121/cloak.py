from typing import final
import cv2 
import time 
import numpy as np 

# to save the output the in .avi 

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter("output.avi",fourcc,120.0,(720,640))

# to start a camera
camera = cv2.VideoCapture(0)
time.sleep(2)
bg = 0

# to capture 60 frames 

for i in range(60):
    ret,bg=camera.read()
    
# to flip the  image
bg = np.flip(bg,axis=1)

# to read and return the frames when cam active 
while camera.isOpened():
    ret,image = camera.read()
    if not ret:
        break
    image  = np.flip(image,axis=1) 
    # to convert image color to hsv from rgb
    hsv =  cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    # to genrate mask to dectect red color
    lred = np.array([0,120,50])
    ured = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lred,ured)
    lred = np.array([170,120,70])
    ured = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lred,ured)
    mask1 =  mask1+mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    res1  = cv2.bitwise_and(image,image,mask=mask2)
    res2  = cv2.bitwise_and(bg,bg,mask=mask2)
    finalres = cv2.addWeighted(res1,1,res2,1,0)
    output_file.write(finalres)
    cv2.imshow("cam",finalres)
    cv2.waitKey(1)
    
camera.release()
out.release()
cv2.destroyAllWindows()
    