#coding=utf-8
import cv2
import numpy as np
img = cv2.imread('../images/circle01.PNG')
kernel = np.ones((30,30),np.uint8)
erosion_1 = cv2.erode(img,kernel,iterations = 1)
erosion_2 = cv2.erode(img,kernel,iterations = 2)
erosion_3 = cv2.erode(img,kernel,iterations = 3)
res = np.hstack((img,erosion_1,erosion_2,erosion_3))
cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()