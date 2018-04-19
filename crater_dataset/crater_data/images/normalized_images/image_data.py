import pickle
import cv2 as cv
from paths import *
import sys
import numpy as np
import os
import matplotlib.cm
from matplotlib import pyplot as plt
from imagewrapper import ImageWrapper

np.set_printoptions(threshold=np.nan)

def readImagesFromPath(src, label, filename):
    crater_files = os.listdir(src[0])
    np.random.shuffle(crater_files)
    non_crater_files = os.listdir(src[1])
    np.random.shuffle(non_crater_files)
    leng = len(crater_files)
    nleng = len(non_crater_files)
    # training set length
    # 70 % for crater and 70 % non crater
    tsl = int(.7 * leng)
    # 70 % length of non crater files
    ntsl = int(.7 * nleng)
    all_images = []
    labels = []
    # 70% crater for training set
    for image_file in range(tsl):
        image = cv.imread(src[0] + crater_files[image_file])
        # convert to grayscale
        if image is None:
            print "Image Not Valid: 70% Crater Training Set"
            continue
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        if image_file == 0:
            all_images = np.reshape(image, (1, 40000))
        else:
            image = np.reshape(image, (1, 40000))
            all_images = np.append(all_images, image, axis=0)
        labels.append(label[0])

    # 70 % non crater for training set
    for image_file in range(ntsl):
        image = cv.imread(src[1] + non_crater_files[image_file])
        # convert to grayscale
        if image is None:
            print src[1] + non_crater_files[image_file]
            print "Image Not Valid:70% Non Crater Training Set"
            continue
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image = np.reshape(image, (1, 40000))
        all_images = np.append(all_images, image, axis=0)
        labels.append(label[1])

    traing_data = (all_images, labels)

    all_test_images = []
    all_test_labels = []
    # data for the testing set, 30% crater test
    for image_file in range(tsl, leng):
        image = cv.imread(src[0] + crater_files[image_file])
        # convert to grayscale
        if image is None:
            print src[1] + non_crater_files[image_file]
            print "Image Not Valid: 30% Crater Testing Set"
            continue
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        if image_file == tsl:
            all_test_images = np.reshape(image, (1, 40000))
        else:
            image = np.reshape(image, (1, 40000))
            all_test_images = np.append(all_test_images, image, axis=0)
        all_test_labels.append(label[0])

    # 30% for non crater for testing
    for image_file in range(ntsl, nleng):
        image = cv.imread(src[1] + non_crater_files[image_file])
        # convert to grayscale
        if image is None:
            print "Image Not Valid: 30% Non Crater Testing Set"
            continue;
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image = np.reshape(image, (1, 40000))
        all_test_images = np.append(all_test_images, image, axis=0)
        all_test_labels.append(label[1])

    test_data = (all_test_images, all_test_labels)
    all_data = (traing_data, test_data)
    #all_data = [(all_images, labels), (all_test_images, all_test_labels)]
    my_file = open(filename, 'wb')
    pickle.dump(all_data, my_file)
    my_file.close()


if __name__ == '__main__':
    # crater and non crater
    #paths = [DEST1, DEST2]
    paths = [CRATER_SCALED_PATH, NON_CRATER_SCLALED_PATH]
    labels = [1, 0]
    readImagesFromPath(paths, labels, "scaled-data.pkl")
