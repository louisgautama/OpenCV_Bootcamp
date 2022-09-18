import cv2
import numpy as np#Joining Image

img1 = cv2.imread("Resources/lambo.png")
crop_img1 = img1[0:200, 200:500]

img2 = cv2.imread("Resources/robot.png")
crop_img2 = img2[0:200, 200:500]

img_hor = np.hstack((crop_img1,crop_img2)) #join pictures horizontally
img_ver = np.vstack((crop_img1,crop_img2)) #join pictures vertically

cv2.imshow("Horizontal", img_hor)
cv2.imshow("Vertical", img_ver)
cv2.waitKey(0)