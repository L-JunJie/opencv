#coding=utf-8
#导入函数库
import cv2
import numpy as np
#np.set_printoptions(threshold=np.inf)  #打印数组中的全部内容
import matplotlib.pyplot as plt
'''
    图像怀旧处理
'''
#图像光照处理函数构造
def Nostalgia(img):#参数为原图像
    h,w=img.shape[0:2]    #获取图像属性
    img1=np.zeros((h,w,3),dtype=img.dtype)   #定义空白图像，存放图像怀旧处理之后的图片
    #通过对原始图像进行遍历，通过怀旧公式修改像素值，然后进行怀旧处理
    for i in range(h):
        for j in range(w):
            B=0.131*img[i,j,0]+0.534*img[i,j,1]+0.272*img[i,j,2]
            G=0.168*img[i,j,0]+0.686*img[i,j,1]+0.349*img[i,j,2]
            R=0.189*img[i,j,0]+0.769*img[i,j,1]+0.393*img[i,j,2]
            #防止图像溢出
            if B>255:
                B = 255
            if G>255:
                G = 255
            if R>255:
                R = 255
            img1[i,j]=[int(B),int(G),int(R)]#B\G\R三通道都设置为怀旧值
    return img1

plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
#读取图像
img=cv2.imread("student.jpg")
#调用图像怀旧处理函数，进行图像怀旧处理
Nostalgia=Nostalgia(img)
#BGR转换为RGB显示格式，方便通过matplotlib进行图像显示
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
Nostalgia=cv2.cvtColor(Nostalgia,cv2.COLOR_BGR2RGB)
#图像与原图显示对比
titles = [ '原图像', '图像怀旧特效']
images = [img, Nostalgia]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')#关闭坐标轴  设置为on则表示开启坐标轴
plt.show()
