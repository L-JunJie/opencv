# 轮廓提取
#coding=utf-8
import cv2


# 转二进制图像
def ToBinray():
    global imgray, binary
    # 1、灰度图
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imgray', imgray)
    # 2、二进制图像
    ret, binary = cv2.threshold(imgray, 127, 255, 0)
    # 阈值 二进制图像
    cv2.imshow('binary', binary)

# 提取轮廓
def GetGontours():
    # 1、根据二值图找到轮廓
    ref_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 轮廓      层级                               轮廓检索模式(推荐此)  轮廓逼近方法
    # 2、画出轮廓
    dst = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    #                           轮廓     第几个(默认-1：所有)   颜色       线条厚度
    cv2.imshow('dst', dst)

if __name__ == '__main__':
    img = cv2.imread('../images/circle.jpg')
    cv2.imshow('img', img)
    ToBinray()  # 转二进制
    GetGontours()  # 提取轮廓
    cv2.waitKey(0)