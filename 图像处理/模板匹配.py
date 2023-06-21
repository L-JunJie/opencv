#coding=utf-8
import cv2
#从磁盘加载输入图像和模板图像，然后显示在我们的屏幕上
image = cv2.imread('../images/dog.jpg')  #加载要匹配的图片
template = cv2.imread('../images/template.PNG')  #加载模板图片
cv2.imshow('image',image)
cv2.imshow('template',template)
#将图像和模板都转换为灰度
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#执行模板匹配
print("[INFO] performing template matching...")
#设置不同的匹配方法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
h,w=template.shape[:2]
for method in methods:
    method = eval(method)
    result = cv2.matchTemplate(imageGray, templateGray,	method)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    #确定起点和终点的（x，y）坐标边界框
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = minLoc
    else:
        top_left = maxLoc
    bottom_right = (top_left[0] + w, top_left[1] + h)
#在图像上绘制边框
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
#显示输出图像
    cv2.imshow('img'+str(method), image)
cv2.waitKey(0)
cv2.destroyAllWindows()