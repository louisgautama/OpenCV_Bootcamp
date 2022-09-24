#Color Extraction

import cv2
import numpy as np

path = "Resources/robot.png"

def empty():
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbar", 2, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 27, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 137, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 96, 255, empty)
cv2.createTrackbar("Val Max", "Trackbar", 255, 255, empty)

while True:
    img = cv2.imread(path)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #TrackBar objects
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbar")

    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    lower = np.array([3, 58, 67]) #hue min, saturation min, val min
    upper = np.array([170, 255, 255]) #hue max, saturation max, val max

    mask = cv2.inRange(img_HSV, lower, upper)
    
    img_result = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow("Original", img)
    cv2.imshow("HSV", img_HSV)
    cv2.imshow("mask_img", mask)
    cv2.imshow("img_result", img_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break