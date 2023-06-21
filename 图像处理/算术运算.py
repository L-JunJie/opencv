#coding=utf-8
import cv2

img=cv2.imread('../images/cat_dog.jpg')
# print(img.shape)
cv2.imshow('img',img)
img1=cv2.imread('../images/copywriting.jpg')
img1=cv2.resize(img1,(img.shape[1],img.shape[0])) #将两张图片处理成相同大小
cv2.imshow('img1',img1)
# print(img1.shape)
'''图片像素的算术运算'''
add = cv2.add(img,img1) #两张图片的对应位置像素相加
cv2.imshow("add", add)
sub = cv2.subtract(img,img1)#两张图片对应位置像素相减
cv2.imshow("sub", sub)
multiply = cv2.multiply(img,img1) #两张图片对应位置像素相乘
cv2.imshow("multiply", multiply)
divide = cv2.divide(img,img1)  #两张图片对应位置像素相除
cv2.imshow("divide", divide)
cv2.waitKey(0)
cv2.destroyAllWindows()