#coding=utf-8
import cv2
#打开摄像头,一般内置为0,外接为1
cap = cv2.VideoCapture(1)
i = 0
#也可写成while True
while True:
    """
    ret：True或者False，代表有没有读取到图片
    frame：表示截取到一帧的图片
    """
    ret,frame = cap.read()
    # 展示图片
    cv2.imshow('capture',frame)
    # 保存图片
    k=cv2.waitKey(1)
    if k==ord('k'):
        x=cv2.imwrite("./image/"+ str(i) + ".jpg",frame) #存储路径
        print(x) #若x为True，则表示保存成功
        i = i + 1
    """
       cv2.waitKey(1)：waitKey()函数功能是不断刷新图像，返回值为当前键盘的值
       OxFF：是一个位掩码，一旦使用了掩码，就可以检查它是否是相应的值
       ord('q')：返回q对应的unicode码对应的值(113)
    """
    if k==ord('q'):
        break
#释放对象和销毁窗口
cap.release()
cv2.destroyAllWindows()