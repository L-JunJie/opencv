#coding=utf-8
#导入函数库
import cv2
import numpy as np
#np.set_printoptions(threshold=np.inf)  #打印数组中的全部内容
import matplotlib.pyplot as plt

'''
    图像光照处理
'''
#图像光照处理函数构造
def illumination(img,lightIntensity):#参数为原图像和光照强度
    h,w=img.shape[0:2]    #获取图像属性
    img1=np.zeros((h,w,3),dtype=img.dtype)    #定义空白图像，存放图像光照处理之后的图片
    x,y=int(h/2),int(w/2)    #确定中心点的位置
    r=min(x,y)    #确定半径
    #通过对原始图像进行遍历，通过光照公式修改像素值，然后进行光照处理
    for i in range(h):
        for j in range(w):
            #计算像素点i，j到中心点的距离的平方
            distance=(x-i)**2+(y-j)**2
            #比较距离与半径的大小，当距离大于半径，不做处理，当距离小于等于半径，设置为光照强度值
            if distance>r**2:
                img1[i,j]=img[i,j]
            else:
                result=int(lightIntensity*(1.0-np.sqrt(distance)/r ))#通过距离来计算光照强度值
                #光照特效处理后的图像三通道值与255取最小，防止溢出(0和结果中选择最大的，结果和255中选择最小的)
                B=min(max(0,img[i,j,0]+result),255)
                G=min(max(0,img[i,j,1]+result),255)
                R=min(max(0,img[i,j,2]+result),255)
                img1[i,j]=[B,G,R]#B\G\R三通道都设置为光照强度值
    return img1

plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
#读取图像
img=cv2.imread("student.jpg")
#调用图像光照处理函数，进行图像光照处理
illumination=illumination(img,150)#传递光照强度为200
#BGR转换为RGB显示格式，方便通过matplotlib进行图像显示
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
illumination=cv2.cvtColor(illumination,cv2.COLOR_BGR2RGB)
#图像与原图显示对比
titles = [ '原图像', '图像光照特效']
images = [img, illumination]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')#关闭坐标轴  设置为on则表示开启坐标轴
plt.show()
