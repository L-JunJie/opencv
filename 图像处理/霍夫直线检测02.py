# coding=utf-8
# 导入相应的python包
import cv2
import numpy as np

img = cv2.imread('../images/ladder.jpg')# 读取输入图片
# 将彩色图片灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 使用Canny边缘检测
edges = cv2.Canny(gray, 50, 200)
# 进行Hough_line直线检测
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, 10, 1)
# 遍历每一条直线
for i in range(len(lines)):
    cv2.line(img, (lines[i, 0, 0], lines[i, 0, 1]),
             (lines[i, 0, 2], lines[i, 0, 3]), (0, 255, 0), 2)
cv2.imshow("result", img)
cv2.waitKey(0)