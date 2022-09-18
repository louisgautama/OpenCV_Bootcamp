import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)

img[:] = 255,0,0 

# Create a Ellipse
cv2.ellipse(img,(256,256),(100,50),0,0,360,(0,255,0),3)

# Create polygon
pts = np.array([[10,5],[20,30],[70,30],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)

# Create Triangle
pts = np.array([[255,30],[205,150],[305,150]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow('Image', img)
cv2.waitKey(0)
