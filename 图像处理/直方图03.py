#coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/dog.jpg', 0)
# 创建一个掩膜
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:400, 300:600] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])  # 无掩膜
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])  # 有掩膜
plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Original')
plt.subplot(222), plt.imshow(mask, 'gray'), plt.title('Mask')
plt.subplot(223), plt.imshow(masked_img, 'gray'), plt.title('Masked')
plt.subplot(224), plt.plot(hist_full, label='original'),
plt.plot(hist_mask, label='masked'), plt.xlim([0, 256]),
plt.legend(loc=1), plt.title('Hostogram')
plt.show()