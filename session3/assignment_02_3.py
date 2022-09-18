import cv2
import numpy as np

haarcascade = "Resources/haarcascade_frontalface_default.xml"

#Detecting Face in Picture
img = cv2.imread('Resources/lena.png')
faceCascade = cv2.CascadeClassifier(haarcascade)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(img_gray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow('Output',img)
cv2.waitKey(0)


#Detecting Face in Video
cap = cv2.VideoCapture("Resources/elon.mp4")

cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    faceCascade = cv2.CascadeClassifier(haarcascade)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow("face",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break