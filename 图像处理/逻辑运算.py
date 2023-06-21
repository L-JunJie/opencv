#coding=utf-8
import cv2

img=cv2.imread('../images/cat_dog.jpg')
# print(img.shape)
cv2.imshow('img',img)
img1=cv2.imread('../images/copywriting.jpg')
img1=cv2.resize(img1,(img.shape[1],img.shape[0])) #将两张图片处理成相同大小
cv2.imshow('img1',img1)
'''图片像素的逻辑运算'''
And = cv2.bitwise_and(img,img1) #图片的与运算
cv2.imshow("And", And)
Or = cv2.bitwise_or(img,img1)  #图片的或运算
cv2.imshow("Or", Or)
Not = cv2.bitwise_not(img) #图片的非运算
cv2.imshow("Not", Not)
Xor = cv2.bitwise_xor(img,img1) #图片的异或运算
cv2.imshow("Xor", Xor)
cv2.waitKey(0)
cv2.destroyAllWindows()

