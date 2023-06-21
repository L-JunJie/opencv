#coding=utf-8
import cv2

'''ROI操作'''
src = cv2.imread('../images/dog1.jpg')
cv2.imshow('src', src)
# 获取RIO区域
sample = src[80:120, 250:370]
# 变为灰度图像
gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
# 还原回RGB三通道的
back_sample = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# 变回去
src[80:120, 250:370] = back_sample
cv2.imshow('ROI', src)
cv2.waitKey(0)
'''泛洪填充操作'''
#图像填充
import cv2
import numpy as np
def fill_color_demo(image):
    # 在复制图像上进行操作
    copyimg = image.copy()
    h, w = copyimg.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
    cv2.floodFill(copyimg, mask, (70,30), (0, 255, 255), (70, 70, 70), (70, 70 ,70), cv2.FLOODFILL_FIXED_RANGE)
    cv2.imshow("fill_color_demo", copyimg)
cat = cv2.imread("../images/cat.jpg")
cv2.imshow("img", cat)
fill_color_demo(cat)
cv2.waitKey(0)
cv2.destroyAllWindows()

#二值填充
def fill_binary():
    # 创建一个高400宽400通道为3的黑色图像
    image = np.zeros([400,400,3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv2.imshow("fill_binary", image)
    mask = np.ones([402, 402, 1], np.uint8)
    # mask的指定的位置为零时才填充，不为零不填充
    mask[101:301, 101:301] = 0
    cv2.floodFill(image, mask, (200, 200), (123, 23, 255), cv2.FLOODFILL_MASK_ONLY)
    # cv2.imshow("mask", mask)
    cv2.imshow("filled_binary", image)
fill_binary()
cv2.waitKey(0)
cv2.destroyAllWindows()


