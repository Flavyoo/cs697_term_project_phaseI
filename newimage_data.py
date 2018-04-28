"""
Nikith AnupKumar, Flavio Andrade

This program reads the crater and non-crater images from their directories and
does the following:

1.) Shuffle each set of image files randomly.
2.) Read 70% of crater files, put them in an array, and put their label, 1, in the label array.
4.) Read 70% of the non crater files, put them in an array, and put their label, 0, in the label array.
5.) Steps 3, 4 are repeated for rest of the crater and non crater files.
6.) The images are dumped into a pickle file as a tuple.
"""

import sys
import os
import pickle
import cv2 as cv
import numpy as np
# comment this line out or remove it if you do not have paths module.
from paths import *
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

    training_data = (all_images, labels)






    all_test_images = []
    all_test_labels = []
    newtsl = int(.15 * leng)+tsl
    newntsl = int(.15 * nleng)+ntsl      
    #range from tsl to tsl+.15(length)
    # data for the validation set, 15% crater test
    for image_file in range(tsl, newtsl+1):
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

    # 15% for non crater for testing
    for image_file in range(ntsl, newntsl+1):
        image = cv.imread(src[1] + non_crater_files[image_file])
        # convert to grayscale
        if image is None:
            print "Image Not Valid: 30% Non Crater Testing Set"
            continue;
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image = np.reshape(image, (1, 40000))
        all_test_images = np.append(all_test_images, image, axis=0)
        all_test_labels.append(label[1])

    val_data = (all_test_images, all_test_labels)




    all_test_images = []
    all_test_labels = []
    # data for the testing set, 30% crater test
    for image_file in range(newtsl, leng):
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
    for image_file in range(newntsl, nleng):
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
    all_data = (training_data, val_data, test_data)
    #all_data = ((all_images, labels), (all_test_images, all_test_labels))
    my_file = open(filename, 'wb')
    pickle.dump(all_data, my_file)
    my_file.close()


if __name__ == '__main__':
    # crater and non crater
    #paths = [DEST1, DEST2]
    # make sure to provide your own path
    paths = [CRATER_SCALED_PATH, NON_CRATER_SCLALED_PATH]
    labels = [1, 0]
    readImagesFromPath(paths, labels, "scaled-data.pkl")
