import argparse
import time
import cv2
import imutils
import sys
from skimage.transform import pyramid_gaussian
import argparse
import cv2
import math
from craters import *
from crater_classifier import *
import numpy as np
import theano.tensor as T
import theano

class Pyramid:
    def __init__(self, image_file_path, step_size, swz, files):
        self.pyramid_image = cv2.imread(image_file_path)
        self.original_image = cv2.imread(image_file_path)
        self.image_shape = self.pyramid_image.shape
        # number of rows
        self.original_width = self.image_shape[0]
        self.height = self.image_shape[0]
        # number of columns
        self.width = self.image_shape[1]
        self.swz = swz
        self.step_size = step_size;
        self.scale = 1.5
        self.crater_list_3_24 = CraterList()
        self.crater_list_3_25 = CraterList()
        with open(files[0], 'rb') as file:
            for row in file:
                entry = map(int, row.strip('\n').split(','))
                self.crater_list_3_24.add(entry[:2], entry[2])

        with open(files[1], 'rb') as file:
            for row in file:
                entry = map(int, row.strip('\n').split(','))
                self.crater_list_3_25.add(entry[:2], entry[2])



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
        self.scale = scale
        for s in range(-6, 6, 2):
            w = int(self.original_width * math.pow(scale, s))
            self.pyramid_image = imutils.resize(self.original_image, width=w)
            self.height = self.pyramid_image.shape[1]
            self.width = self.pyramid_image.shape[0]
            #if self.height < minSize[1] or self.width < minSize[0]:
            #    break
            yield self.pyramid_image

    def runPyramid(self, pickle):
        #layer_image_results = []
        for resized in self.pyramid():
            image_data = [[], [], 1.5, []]
            for (x, y, window) in self.slidingWindow():
                clone = resized.copy()
                clone1 = resized.copy()
                if x + self.swz <= clone.shape[0] and y + self.swz <= clone.shape[1]:
                    cv2.rectangle(clone, (x, y), (x + self.swz, y + self.swz), (0, 255, 255), 3)
                    center_point_x = (self.swz / 2) + x
                    center_point_y = (self.swz / 2) + y
                    if len(image_data[0]) == 0:
                        image = self.crop(x, y, self.swz, self.swz, clone1)
                        image_data[0] = np.reshape(image, (1, self.swz * self.swz))
                        image_data[1] += [(center_point_y,center_point_x)]
                        image_data[3] += [clone.shape[0]]
                    else:
                        image = self.crop(x, y, self.swz, self.swz, clone1)
                        image = np.reshape(image, (1, self.swz * self.swz))
                        image_data[0] = np.append(image_data[0], image, axis=0)
                        image_data[1] += [(center_point_y,center_point_x)]
                        image_data[3] += [clone.shape[0]]
                    cv2.imshow("Window", clone)
                    cv2.waitKey(1)
                    time.sleep(0.025)
            classifier = CraterClassifier(pickle, self.shared(image_data[0]))
            classifications = classifier.get_classifications()
            #print classifications
        return image_data

    def crop(self, x,y,w,h,image):
        image = image[x:x+w, y:y+h]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.normalize(image.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
        image.astype(np.float32)
        return image

    def shared(self, data):
        """Place the data into shared variables.  This allows Theano to copy
        the data to the GPU, if one is available.

        """
        shared_x = theano.shared(
            np.asarray(data, dtype=theano.config.floatX), borrow=True)
        return shared_x

def main():
    pickle = 'Pickles/leaky-ntwk-e0-val0.9741-tst0.9643.pkl'
    image_path = str(sys.argv[1])
    pyramid = Pyramid(image_path, 10, 101, ['gt_tile3_24.csv', 'gt_tile3_25.csv'])
    pyramid.runPyramid(pickle)

if __name__ == '__main__':
    main()
