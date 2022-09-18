import cv2
import numpy as np

width, height = 595,842

img =  cv2.imread("Resources/docs.jpg")

pts1 = np.float32([[720,28],[1112,21],[749,560],[1222,546]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("docs", img)
cv2.imshow("docs_warp", img_out)

cv2.waitKey(0)