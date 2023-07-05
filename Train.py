import cv2
import numpy as np
from PIL import Image
import os

# khai báo thư mục dataset

path = 'dataset'


detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#tạo hàm
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in  os.listdir(path)]
    faceSamples=[]
    ids=[]

    for imagePath in  imagePaths:

        PIL_img = Image.open(imagePath).convert('L')
        img_nump = np.array(PIL_img,'uint8')
        # lấy id
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        #lấy hình ảnh
        faces = detector.detectMultiScale(img_nump)

        for(x,y,w,h) in faces:
            faceSamples.append(img_nump[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids
print("\n đang trainning.......")

faces, ids = getImagesAndLabels(path)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))
recognizer.write('trainer/trainer.yml')

print("\n đang trainning xong")