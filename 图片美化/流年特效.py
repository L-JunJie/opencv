#coding=utf-8
#导入函数库
import cv2
import numpy as np
#np.set_printoptions(threshold=np.inf)  #打印数组中的全部内容
import matplotlib.pyplot as plt
'''
    图像流年处理
'''
#图像流年处理函数构造
def chronology(img,weight):
    #获取图像属性
    h,w=img.shape[0:2]
    #定义空白图像，存放图像流年处理之后的图片
    img1=np.zeros((h,w,3),dtype=img.dtype)
    #通过对原始图像进行遍历，通过流年公式修改B通道的像素值，然后进行流连处理
    for i in range(h):
        for j in range(w):
            B=int(np.sqrt(img[i,j,0])*weight)#对通道B的像素值开方，然后乘以权重
            if B>255:
                B=255
            img1[i,j]=[B,img[i,j,1],img[i,j,2]]
    return img1

plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
#读取图像
img=cv2.imread("student.jpg")
#调用图像流年处理函数，进行图像流年处理
chronology=chronology(img,15)#传递权重参数15
#BGR转换为RGB显示格式，方便通过matplotlib进行图像显示
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
chronology=cv2.cvtColor(chronology,cv2.COLOR_BGR2RGB)
#图像与原图显示对比
titles = [ '原图像', '图像流年特效']
images = [img, chronology]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')#关闭坐标轴  设置为on则表示开启坐标轴
plt.show()
