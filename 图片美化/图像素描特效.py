#coding=utf-8
#导入函数库
import cv2
import numpy as np
#np.set_printoptions(threshold=np.inf)  #打印数组中的全部内容
import matplotlib.pyplot as plt
'''
    图像素描处理
'''
#图像素描处理函数构造
def Sketch(img):#参数为原图像
    #图像灰度处理
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #通过高斯滤波过滤噪声
    gaussian = cv2.GaussianBlur(gray, (3,3), 0)
    #通过canny算法提取图像轮过
    canny = cv2.Canny(gaussian, 50, 140)
    #对轮廓图像进行反二进制阈值化处理
    ret, result = cv2.threshold(canny, 90, 255, cv2.THRESH_BINARY_INV)
    return result

plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
#读取图像
img=cv2.imread("student.jpg")
#调用图像素描处理函数，进行图像素描处理
Sketch=Sketch(img)
#BGR转换为RGB显示格式，方便通过matplotlib进行图像显示
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
Sketch=cv2.cvtColor(Sketch,cv2.COLOR_GRAY2BGR)
#图像与原图显示对比
titles = [ '原图像', '图像素描特效']
images = [img, Sketch]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')#关闭坐标轴  设置为on则表示开启坐标轴
plt.show()
