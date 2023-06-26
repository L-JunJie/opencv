#coding=utf-8
#导入函数库
import cv2
import numpy as np
#np.set_printoptions(threshold=np.inf)  #打印数组中的全部内容
import matplotlib.pyplot as plt
'''
    图像浮雕处理
'''
#图像浮雕处理函数构造
def relief(img,Degree):#参数为原图像和浮雕图像程度
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    #图像灰度处理
    h,w=gray.shape[0:2]    #获取图像属性
    img1=np.zeros((h,w),dtype=gray.dtype)    #定义空白图像，存放图像浮雕处理之后的图片
    #通过对原始图像进行遍历，通过浮雕公式修改像素值，然后进行浮雕处理
    for i in range(h):
        for j in range(w-1):
            #前一个像素值
            a=gray[i,j]
            #后一个像素值
            b=gray[i,j+1]
            #新的像素值,防止像素溢出
            img1[i,j]=min(max((int(a)-int(b)+Degree),0),255)
    return img1

plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
#读取图像
img=cv2.imread("student.jpg")
#调用图像浮雕处理函数，进行图像浮雕处理
re=relief(img,160)#设置浮雕图像程度值为160
#BGR转换为RGB显示格式，方便通过matplotlib进行图像显示
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
re=cv2.cvtColor(re,cv2.COLOR_GRAY2BGR)
#图像与原图显示对比
titles = [ '原图像', '图像浮雕特效']
images = [img, re]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')#关闭坐标轴  设置为on则表示开启坐标轴
plt.show()
