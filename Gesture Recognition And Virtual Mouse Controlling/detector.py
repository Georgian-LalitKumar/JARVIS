import cv2
import numpy as np 

faceDetect=cv2.CascadeClassifier(r'C:\Users\LALIT\Desktop\jarvi\New folder\project\FACE\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read(r'C:\Users\LALIT\Desktop\jarvi\New folder\project\FACE\New folder\recognizer\trainingData.yml')
id=0

fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 255, 255)



while True:
    ret,img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if id==1:
            id="LALIT"
        elif id==2:
            id="Atal VihariBajpaee"
        elif id==3:
            id="Barak Obama"
        elif id==4:
            id="Alan Turing"
        elif id==5:
            id="Devendra Fadnivis"
        elif id==5:
            id="Gejji Mam"
        cv2.putText(img,str(id),(x,y+h),fontFace,fontScale,fontColor)
    cv2.imshow("Face",img)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()