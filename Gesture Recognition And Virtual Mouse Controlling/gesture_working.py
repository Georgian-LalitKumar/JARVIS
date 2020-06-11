# packages to install 
# pip install pynput
# pip install wxpython


import cv2
import numpy as np
lowerBound=np.array([33,80,40])
upperBound= np.array([102,255,255])

cam=cv2.VideoCapture(0)
# it is used to remove noise ,which sometimes gets through the filter
# kernelOpen makes the grp of noise(which apperars white in color here) black which is smaller than the kernel
kernelOpen=np.ones((5,5))
# IT IS OPPOSITE TO kernelOpen makes the grp of noise(which apperars white in color here) WHITE which is smaller than the kernel
kernelClose=np.ones((20,20))

font=cv2.FONT_HERSHEY_COMPLEX
fontScale = 1


while True:
    ret,img=cam.read()
    img=cv2.resize(img,(340,220))

    #converting BGR TO HSV
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #creating The mask(/ a filter /color detector)
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
     #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    
    maskFinal=maskClose
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,conts,-1,(255,0,0),3)
    # putting rectangle around object
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img,str(i+1),(x,y+h),font,fontScale,(0,255,255))
    cv2.imshow("mask",mask)
    cv2.imshow("maskClose",maskClose)
    cv2.imshow("maskopen",maskOpen)
    cv2.imshow("cam",img)
    cv2.waitKey(10)
