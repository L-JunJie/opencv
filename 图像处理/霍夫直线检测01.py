# coding=utf-8
# 导入相应的python包
import cv2
import numpy as np
# 读取输入图片
img = cv2.imread('../images/ladder.jpg')
cv2.imshow('img',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 将彩色图片灰度化
edges = cv2.Canny(gray, 100, 300,apertureSize=5) # 使用Canny边缘检测
cv2.imshow('canny',edges)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 140)# 进行Hough_line直线检测
# print(lines)
# 遍历每一个r和theta
for i in range(len(lines)):
    r, theta = lines[i, 0, 0], lines[i, 0, 1]
    a = np.cos(theta) # 存储cos(theta)的值
    b = np.sin(theta)   # 存储sin(theta)的值
    x0 = a * r   # 存储rcos(theta)的值
    y0 = b * r   # 存储rsin(theta)的值
    x1 = int(x0 + 500 * (-b))  # 存储(rcos(theta)-1000sin(theta))的值
    y1 = int(y0 + 500 * (a))   # 存储(rsin(theta)+1000cos(theta))的值
    x2 = int(x0 - 500 * (-b))  # 存储(rcos(theta)+1000sin(theta))的值
    y2 = int(y0 - 500 * (a))   # 存储(rsin(theta)-1000cos(theta))的值
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2) # 绘制直线结果
cv2.imshow("result", img)
cv2.waitKey(0)
