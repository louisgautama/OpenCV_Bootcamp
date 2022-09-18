#Joining Image
import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
img_hor = np.hstack((img,img)) #join pictures horizontally
img_ver = np.vstack((img,img)) #join pictures vertically

cv2.imshow("Horizontal", img_hor)
cv2.imshow("Vertical", img_ver)
cv2.waitKey(0)