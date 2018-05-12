import argparse
import time
import cv2
import imutils
import sys
from skimage.transform import pyramid_gaussian
import argparse
import cv2
import math

class Pyramid:
    def __init__(self, image_file_path, step_size, swz):
        self.pyramid_image = cv2.imread(image_file_path)
        self.original_image = cv2.imread(image_file_path)
        self.image_shape = self.pyramid_image.shape
        # number of rows
        self.original_width = self.image_shape[0]
        self.width = self.image_shape[0]
        # number of columns
        self.height = self.image_shape[1]
        self.swz = swz
        self.step_size = step_size;

    def slidingWindow(self):
        """
        Create an n x n window that moves across the big image creating smaller
        images to be passed to the convolutional neural network. Sliding windows
        start off small and grow looking for craters that may fit inside the current
        window.
        """
        for y in xrange(0, self.height, self.step_size):
            for x in xrange(0, self.width, self.step_size):
                yield (x, y, self.pyramid_image[y:y + self.swz, x:x + self.swz])

    def pyramid(self, scale=1.5, minSize=(30, 30)):
        for s in range(-6, 4, 2):
            w = int(self.original_width * math.pow(scale, s))
            self.pyramid_image = imutils.resize(self.original_image, width=w)
            self.height = self.pyramid_image.shape[1]
            self.width = self.pyramid_image.shape[0]
            #if self.height < minSize[1] or self.width < minSize[0]:
            #    break
            yield self.pyramid_image

    def runPyramid(self):
        for resized in self.pyramid():
            print resized.shape
            """for (x, y, window) in self.slidingWindow():
                clone = resized.copy()
                if x + self.swz <= clone.shape[0] and y + self.swz <= clone.shape[1]:
                    cv2.rectangle(clone, (x, y), (x + self.swz, y + self.swz), (0, 255, 255), 3)
                    cv2.imshow("Window", clone)
                    cv2.waitKey(1)
                    time.sleep(0.025)"""

def main():
    image_path = str(sys.argv[1])
    pyramid = Pyramid(image_path, 10, 101)
    pyramid.runPyramid()

if __name__ == '__main__':
    main()
