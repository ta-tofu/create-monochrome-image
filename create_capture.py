import cv2
import numpy as np


class createCapture():

    def __init__(self):
        # 縦横の値
        self.width = 1280
        self.height = 720
        # RGB の値
        self.red_value = 255
        self.green_value = 255
        self.blue_value = 255
        # 画像の品質
        self.quality_value = 100
        # 出力先のフォルダパス
        self.dist_path = './dist/'

    def set_color(self, red_value: int = 255, green_value: int = 255, blue_value: int = 255):
        self.red_value = red_value
        self.green_value = green_value
        self.blue_value = blue_value

    def set_quality(self, quality_value: int = 100):
        self.quality_value = quality_value

    def create(self, image_name):
        blank = np.zeros((self.height, self.width, 3))
        blank += [self.red_value, self.green_value, self.blue_value][::-1]
        dist_full_path: str = self.dist_path + image_name
        cv2.imwrite(dist_full_path, blank)


if __name__ == '__main__':
    capture_handle = createCapture()
    capture_handle.set_color(0, 255, 0)
    capture_handle.create('green_back.png')
