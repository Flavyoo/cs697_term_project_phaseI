"""
craterLoader.py
Flavio Andrade, Nikith AnupKumar
4-16-18

This program reads a pickle file containing training and test data.
Each data set, training and test, is a tuple of the the respective images and their labels.
The training set consists of 70% of the crater and 70% of the non-crater images, and the test
data set consists of 30% of the crater and 30% of the non-crater images.

After the file is read, each image from the data set is turned into a column vector
and put into a tuple consisting of the image itself, and its label. This is done for
the test and the training data. The final values are then returned.

"""

import pickle
import numpy as np

# call this to get image data and label
# take in a string filename
def load_crater_data_wrapper(filename):
    #all_data = [(all_images, labels), (all_test_images, all_test_labels)]
    my_file = open(filename, 'rb')
    training_data, test_data = pickle.load(my_file)
    my_file.close()
    # access the images of the tuple
    training_data_inputs = [np.reshape(x, (40000, 1)) for x in training_data[0]]
    # training data
    trd = zip(training_data_inputs, training_data[1])
    test_data_inputs = [np.reshape(x, (40000, 1)) for x in test_data[0]]
    # test data
    ted = zip(test_data_inputs, test_data[1])
    return (trd, ted)
