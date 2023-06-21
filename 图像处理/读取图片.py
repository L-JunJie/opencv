#coding=utf-8

import cv2
img=cv2.imread('../images/cat_dog.jpg',0)
cv2.imshow('img',img)
img1=cv2.imread('../images/cat_dog.jpg',1)
cv2.imshow('img1',img1)
img2=cv2.imread('../images/cat_dog.jpg',-1)
cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()