# coding=utf-8
import cv2  #导入opencv库
img=cv2.imread('../images/cat_dog.jpg') #加载要显示的图片
cv2.imshow('img',img)     #显示图片
cv2.waitKey(0)           #表示图片显示时间，0表示一直显示
cv2.destroyAllWindows()  #释放内存