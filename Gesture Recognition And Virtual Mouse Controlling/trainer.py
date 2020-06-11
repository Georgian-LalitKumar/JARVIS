#--------------this is a trainer file----------------------------
#pip install --force-reinstall opencv-contrib-python==4.1.2.30  
import os
import cv2
import numpy as np 
from PIL import Image

#creating a recognizer
recognizer =cv2.face.LBPHFaceRecognizer_create()
path='dataSet'

def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        
    faces=[]    #list for face
    IDs=[]  #list for IDS

    #looping through the images 
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L') #convert ingae into grayscale
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return np.array(IDs),faces

Ids,faces=getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
