import argparse
import time
import cv2
import imutils
import sys

class Pyramid:
    def __init__(self, image_file_path):
        self.pyramid_image = cv2.imread(image_file_path)
        self.image_shape = self.pyramid_image.shape
        self.width = self.image_shape[0]
        self.height = self.image_shape[1]
        self.min_width = 15
        self.min_height = 15

    def createSlidingWindow():
        pass

    def runSlidingWindow():
        pass


def main():
    image_path = str(sys.argv[1])
    pyramid = Pyramid(image_path)

if __name__ == '__main__':
    main()
