#coding=utf-8
import cv2
import numpy as np

img = cv2.imread('../images/circle02.PNG')

kernel = np.ones((35,35),np.uint8)
dilate_1 = cv2.dilate(img,kernel,iterations = 1)
dilate_2 = cv2.dilate(img,kernel,iterations = 2)
dilate_3 = cv2.dilate(img,kernel,iterations = 3)
res = np.hstack((img,dilate_1,dilate_2,dilate_3))
cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
