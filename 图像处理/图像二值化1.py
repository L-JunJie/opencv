#coding=utf-8
'''在这个示例中，我们创建了一个名为`MainWindow`的窗口，并在窗口中添加了一个标签和一个滑块。在窗口的构造函数中，我们加载了一张名为`dog.jpg`的图像，并将其显示在标签中。我们还连接了滑块的值改变事件，以便在滑块值改变时更新图像。

在`update_image`函数中，我们首先获取滑块的值，然后使用OpenCV的`threshold`函数对图像进行二值化。我们将二值化后的图像转换为QImage，并将其设置为标签的图像。注意，我们使用了`QImage.Format_Grayscale8`格式，因为我们的图像是灰度图像。

运行这个示例代码，你将看到一个窗口，其中包含一张灰度图像和一个滑块。你可以通过移动滑块来改变阈值，并观察图像的变化。'''
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建标签和滑块
        self.image_label = QLabel()
        self.threshold_slider = QSlider(Qt.Horizontal)
        self.threshold_slider.setMinimum(0)
        self.threshold_slider.setMaximum(255)
        self.threshold_slider.setValue(127)

        # 创建垂直布局，并将标签和滑块添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.threshold_slider)

        # 设置主窗口的布局
        self.setLayout(layout)

        # 加载图像
        self.image = cv2.imread('../images/dog.jpg', cv2.IMREAD_GRAYSCALE)

        # 显示图像
        self.update_image()

        # 连接滑块的值改变事件
        self.threshold_slider.valueChanged.connect(self.update_image)

    def update_image(self):
        # 获取滑块的值
        threshold_value = self.threshold_slider.value()

        # 对图像进行二值化
        _, binary_image = cv2.threshold(self.image, threshold_value, 255, cv2.THRESH_BINARY)

        # 将OpenCV图像转换为QImage
        height, width = binary_image.shape
        bytes_per_line = width
        q_image = QImage(binary_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

        # 将QImage转换为QPixmap，并设置给标签
        pixmap = QPixmap.fromImage(q_image)
        self.image_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()