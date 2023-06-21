#coding=utf-8
import cv2
import numpy as np

'''均值模糊、中值模糊、自定义模糊    模糊是卷积的一种表象'''
def blur_demo(image):  # 均值模糊  去随机噪声有很好的去燥效果
    dst = cv2.blur(image, (25, 6))  # （1, 15）是垂直方向模糊，（15， 1）还水平方向模糊
    cv2.namedWindow('blur_demo', cv2.WINDOW_NORMAL)
    cv2.imshow("blur_demo", dst)
def median_blur_demo(image):  # 中值模糊  对椒盐噪声有很好的去燥效果
    dst = cv2.medianBlur(image, 9)
    cv2.namedWindow('median_blur_demo', cv2.WINDOW_NORMAL)
    cv2.imshow("median_blur_demo", dst)
def custom_blur_demo(image):  # 用户自定义模糊
    kernel = np.ones([6, 6], np.float32) / 25  # 除以25是防止数值溢出
    dst = cv2.filter2D(image, -1, kernel)
    cv2.namedWindow('custom_blur_demo', cv2.WINDOW_NORMAL)
    cv2.imshow("custom_blur_demo", dst)
src = cv2.imread('../images/dog.jpg')
cv2.namedWindow('input_image', cv2.WINDOW_NORMAL)
cv2.imshow('input_image', src)
blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''高斯模糊'''
def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv
def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
        cv2.namedWindow("noise image", cv2.WINDOW_NORMAL)
        cv2.imshow("noise image", image)
        dst = cv2.GaussianBlur(image, (19, 19), 0)  # 高斯模糊
        cv2.namedWindow("Gaussian", cv2.WINDOW_NORMAL)
        cv2.imshow("Gaussian", dst)
src = cv2.imread('../images/dog.jpg')
cv2.namedWindow('input_image', cv2.WINDOW_NORMAL)
cv2.imshow('input_image', src)
gaussian_noise(src)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''边缘保留滤波（EPF）  高斯双边、均值迁移'''
def bi_demo(image):  # 双边滤波
    #  bilateralFilter(src, d, sigmaColor, sigmaSpace)
    # src :处理的图形   d：在过滤期间使用的每个像素邻域的直径。
    # sigmaColor：色彩空间的标准方差，一般尽可能大。  sigmaSpace：坐标空间的标准方差(像素单位)，一般尽可能小。
    dst = cv2.bilateralFilter(image, 0, 100, 15)
    cv2.namedWindow("bi_demo", cv2.WINDOW_NORMAL)
    cv2.imshow("bi_demo", dst)
def shift_demo(image):  # 均值迁移
    # pyrMeanShiftFiltering(src, sp, sr[, dst[, maxLevel[, termcrit]]])
    '''src:输入图像，8位，三通道图像。
      sp:漂移物理空间半径大小。
      sr:漂移色彩空间半径大小。
      dst:和源图象相同大小、相同格式的输出图象。
      maxLevel:金字塔的最大层数。
      termcrit:漂移迭代终止条件。'''

    dst = cv2.pyrMeanShiftFiltering(image, 10, 50)
    cv2.namedWindow("shift_demo", cv2.WINDOW_NORMAL)
    cv2.imshow("shift_demo", dst)
src = cv2.imread('../images/dog.jpg')
cv2.namedWindow('input_image', cv2.WINDOW_NORMAL)
cv2.imshow('input_image', src)
bi_demo(src)
shift_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
