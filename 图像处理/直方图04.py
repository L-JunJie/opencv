#coding=utf-8
import cv2
import numpy as np

cap = cv2.VideoCapture(1)

color = ('b', 'g', 'r')
colors = ((255, 0, 0), (0, 255, 0), (0, 0, 255))

if cap.isOpened() is True:  # 检查摄像头是否正常启动
    while (True):
        # frame = cv2.imread('test6.jpg')
        ret, frame = cap.read()
        rows, cols, dpt = frame.shape
        # 尺寸读取出了问题
        # rows = 640
        # cols = 480
        size = rows * cols
        for i, c in enumerate(colors):
            histr = cv2.calcHist([frame], [i], None, [256], [0, 256])
            histr = histr * cols / size
            lines = []
            for j, k in enumerate(histr):
                x = int(j * rows / 255)
                y = cols - int(k * 5)
                cv2.circle(frame, (x, y), 2, c, -1)  # 点显示
                ploy = lines.append([x, y])
            pts = np.array([lines], dtype=np.int32)
            cv2.polylines(frame, pts, 0, c, 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print('cap is not opened!')