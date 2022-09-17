# Basics functions
import cv2
import numpy as np

# 1. Convert to gray scale

# img = cv2.imread('Resources/lena.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img.shape)
# print(img_gray.shape)
# cv2.imshow('Output',img_gray)
# cv2.waitKey(0)


#Convert to blur
# img = cv2.imread('Resources/lena.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
# cv2.imshow('Color_Img',img)
# cv2.imshow('Gray_Img',img_gray)
# cv2.imshow('Blur_Img',img_blur)
# cv2.waitKey(0)

# 3. convert canny image
# img = cv2.imread('Resources/lena.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
# img_canny = cv2.Canny(img, 100, 100)
# cv2.imshow('Color_Img',img)
# cv2.imshow('Gray_Img',img_gray)d
# cv2.imshow('Blur_Img',img_blur)
# cv2.imshow('Canny_Img',img_canny)
# cv2.waitKey(0)

# 4. Convert to Dialation
kernel = np.ones((5,5), np.uint8)
print(kernel)

img = cv2.imread('Resources/lena.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
img_canny = cv2.Canny(img, 100, 100)
img_dialation = cv2.dilate(img_canny, kernel, iteration = 1)
#Erode
img_eroded = cv2.erode(img_dialation, kernel, iteration = 2)
cv2.imshow('Color_Img',img)
cv2.imshow('Gray_Img',img_gray)
cv2.imshow('Blur_Img',img_blur)
cv2.imshow('Canny_Img',img_canny)
cv2.imshow('Dialate_Img',img_dialation)
cv2.imshow('Erode_Img',img_eroded)
cv2.waitKey(0)


