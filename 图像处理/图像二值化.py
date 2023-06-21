import cv2
import numpy as np
# 读取图片。
img = cv2.imread("../images/cat_dog.jpg")
cv2.imshow('img',img)
#全局阈值二值化
def image_binarization(img):
    # 将图片转为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # retval, dst = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)
    # 最大类间方差法(大津算法)，thresh会被忽略，自动计算一个阈值
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Global threshold',dst)
    # cv2.imwrite('binary.jpg', dst)

#局部阈值二值化
def image_binarization_part_situation(img):
    '''
    局部二值化
    :return:
    '''
    # 转灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 图像压缩(非必要步骤)
    new_gray = np.uint8((255 * (gray/255.0)**1.4))
    # 二值化
    dst = cv2.adaptiveThreshold(new_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 1)
    # 中值滤波
    cv2.imshow('Local threshold',dst)
    img_median = cv2.medianBlur(dst, 5)
    cv2.imshow('Median filtering',img_median)

image_binarization(img)
image_binarization_part_situation(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img_OpenCV = cv2.imread('sigonghuiye.jpeg')
b, g, r = cv2.split(img_OpenCV)
img_matplotlib = cv2.merge([r, g, b])
cv2.imshow('img1',img_matplotlib)
cv2.imshow('img',img_OpenCV)