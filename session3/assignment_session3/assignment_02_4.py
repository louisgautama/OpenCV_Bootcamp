import cv2
import numpy as np


img1 = cv2.imread("Resources/lambo.png")
img2 = cv2.imread("Resources/robot.png")

resized_img1 = cv2.resize(img1,(300,300))
resized_img2 = cv2.resize(img2,(300,300))
img_hor = np.hstack((resized_img1,resized_img2)) #join pictures horizontally
img_ver = np.vstack((resized_img1,resized_img2)) #join pictures vertically



cv2.imshow("Horizontal", img_hor)
cv2.imshow("Vertical", img_ver)
cv2.waitKey(0)