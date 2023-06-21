#coding=utf-8
import cv2
# 读入图像
img = cv2.imread("../images/dog.jpg")
cv2.imshow('img',img)
# 高斯模糊，去除噪音点
img = cv2.GaussianBlur(img, (5, 5), 0)
#灰度转化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Canny边缘检测，50为低阈值low，150为高阈值high
canny = cv2.Canny(gray, 50, 150,apertureSize=5)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()