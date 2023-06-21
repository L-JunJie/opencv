#coding=utf-8
import cv2
import numpy as np


def detect_circles_demo(image):
    dst = cv2.pyrMeanShiftFiltering(image, 10, 100)#均值偏移滤波
    cv2.imshow("dst", dst)
    cimage = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)#灰度图
    circles = cv2.HoughCircles(cimage, cv2.HOUGH_GRADIENT,
                               1, 20, param1=60, param2=55, minRadius=0)
    circles = np.uint16(np.around(circles))#取整
    for i in circles[0, :]:
        # 在原图上画圆，圆心，半径，颜色，线框
        cv2.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv2.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)#画圆心
    cv2.imshow("circles", image)

src = cv2.imread("../images/circle.png")  #读取图片位置
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input image", src)
detect_circles_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
