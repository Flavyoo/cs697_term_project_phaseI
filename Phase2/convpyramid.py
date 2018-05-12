import argparse
import time
import cv2
import imutils
import sys
from skimage.transform import pyramid_gaussian
import argparse
import cv2

class Pyramid:
    def __init__(self, image_file_path):
        self.pyramid_image = cv2.imread(image_file_path)
        self.image_shape = self.pyramid_image.shape
        # number of rows
        self.width = self.image_shape[0]
        # number of columns
        self.height = self.image_shape[1]
        self.min_width = 15
        self.min_height = 15
        self.step_size = 10;

    def createSlidingWindow():
        """
        Create an n x n window that moves across the big image creating smaller
        images to be passed to the convolutional neural network. Sliding windows
        start off small and grow looking for craters that may fit inside the current
        window.
        """
        for y in xrange(0, self.height, self.step_size):
            for x in xrange(0, self.width, self.step_size):
                yield()



    def runSlidingWindow():
        pass


def main():
    image_path = str(sys.argv[1])
    pyramid = Pyramid(image_path)

if __name__ == '__main__':
    main()
