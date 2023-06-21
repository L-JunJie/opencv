#coding=utf-8
import numpy as np
import cv2
import glob

# 棋盘格尺寸
chessboard_size = (6, 9)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# 生成棋盘格世界坐标系
objp = np.zeros((np.prod(chessboard_size), 3), dtype=np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

# 存储所有图像的世界坐标和图像坐标对应关系
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane.

# 获取所有棋盘格图像
images = glob.glob('.\image\*.jpg')

# 遍历所有棋盘格图像
for fname in images:
    # 读取图像
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 在灰度图像中查找棋盘格角点
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    # 如果找到角点，则添加世界坐标和图像坐标对应关系
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)
        corners2=cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria=criteria)
        # 在棋盘格上绘制角点并显示
        cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)

# 标定相机
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# 评估标定结果
print("Camera matrix:")
print(mtx)
print("Distortion coefficients:")
print(dist)
print("Average reprojection error:")
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error
print(mean_error / len(objpoints))

# 显示标定结果
img = cv2.imread(images[0])
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
