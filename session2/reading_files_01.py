#Reading an Image

from difflib import diff_bytes
from unittest.case import DIFF_OMITTED
import cv2

#img = cv2.imread('Resources/lena.png')
#print(img)
#cv2.imshow('Output',img)
#cv2.waitKey(0)


#Reading Videos

#cap = cv2.VideoCapture('Resources/elon.mp4')
#while True:
#    success, img = cap.read()
#    print(img.shape)
#    cv2.imshow('Output',img)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break


#Read Webcam

cap = cv2.VideoCapture(0)

cap.set(3, 640) #set width, id is 3
cap.set(4, 480) #set height, id is 4

while True:
   success, img = cap.read()
   print(img.shape)
   cv2.imshow('Output',img)

   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
