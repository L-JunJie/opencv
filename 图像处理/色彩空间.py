#coding=utf-8

import cv2
img=cv2.imread('../images/cat.jpg')  #加载原图
cv2.imshow('img',img)  #显示原图
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)  #将图片转换成hsv色彩空间
cv2.imshow('hsv',hsv)  #显示转换后的图片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #将图片转换成灰度图
cv2.imshow('gray',gray) #显示灰度图
YCrCb=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)   #将图片转换成YCrCb色彩空间
cv2.imshow('YCrCb',YCrCb)
Lab=cv2.cvtColor(img,cv2.COLOR_RGB2Lab)      #将图片转换为Lab色彩空间
cv2.imshow('Lab',Lab)
cv2.waitKey(0)
cv2.destroyAllWindows()