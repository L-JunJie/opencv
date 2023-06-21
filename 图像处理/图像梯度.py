#coding=utf-8
import cv2
import matplotlib.pyplot as plt

#Sobel算子
def sobel(img):
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    cv2.imshow('sobelx',sobelx)
    sobely = cv2.convertScaleAbs(sobely)
    cv2.imshow('sobely', sobely)
    sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
    cv2.imshow('sobelxy', sobelxy)

#Scharr算子
def scharr(img):
    scharrx = cv2.Scharr(img,cv2.CV_64F,1,0)
    scharry = cv2.Scharr(img,cv2.CV_64F,0,1)
    scharrx = cv2.convertScaleAbs(scharrx)
    cv2.imshow('scharrx',scharrx)
    scharry = cv2.convertScaleAbs(scharry)
    cv2.imshow('scharry', scharry)
    scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0)
    cv2.imshow('scharrxy', scharrxy)

#laplacian算子
def laplacian(img):
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    cv2.imshow('laplacian', laplacian)

img = cv2.imread('../images/cat_dog.jpg')
cv2.imshow('Original',img)
sobel(img)
scharr(img)
laplacian(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
# plt.subplot(221)
# b, g, r = cv2.split(img)
# img = cv2.merge([r, g, b])
# plt.imshow(img)
# plt.title('Original')
# plt.xticks([]),plt.yticks([])
#
# # plt.figure(figsize=(10,5))
# plt.subplot(222)
# b, g, r = cv2.split(sobelxy)
# sobelxy = cv2.merge([r, g, b])
# plt.imshow(sobelxy)
# plt.title('Sobel')
# plt.xticks([]),plt.yticks([])
#
# plt.subplot(223)
# b, g, r = cv2.split(scharrxy)
# scharrxy = cv2.merge([r, g, b])
# plt.imshow(scharrxy)
# plt.title('Scharr')
# plt.xticks([]),plt.yticks([])
#
# plt.subplot(224)
# b, g, r = cv2.split(laplacian)
# laplacian = cv2.merge([r, g, b])
# plt.imshow(laplacian)
# plt.title('laplacian')
# plt.xticks([]),plt.yticks([])
#
# plt.show()
