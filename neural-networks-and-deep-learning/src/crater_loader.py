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
