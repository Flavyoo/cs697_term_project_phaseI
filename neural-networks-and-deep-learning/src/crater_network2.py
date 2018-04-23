""""
Garret, Euclide

Crater network
This program inherits from the Network class in network.py.
The init function is overwritten to allow for crating the Crater Network and passing an image size.
The evaluate function is overwritten to calculate True Positive, False Positive, False
Negative, True Negative, along with the quality_rate, detect_rate, and false_rateself.
"""

from network import Network
import numpy as np
import random
import os
# Third-party libraries
import cv2 as cv
# Paths
THIS_DIR = os.path.dirname(__file__)
FP_PATH = THIS_DIR + '/FP'
FN_PATH = THIS_DIR + '/FN'
# Size of Images
SIZE = 200

class CraterNetwork(Network):
    """
    Methods from the Network class are inherited.
    """
    def __init__(self, sizes, image_size):
        """The list ``sizes`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron.  The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1.  Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers."""
        super(CraterNetwork, self).__init__(sizes);
        self.im_size = image_size
        self.validating = False

    def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(x, y)`` representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        if test_data:
            n_test = len(test_data)
            print "   Training data size   = %s " % len(training_data)
            print "   Validation data size = %s " % len(test_data)
            self.validating = True # Don't write to TP, FN, FP when validating
        n = len(training_data)
        for j in xrange(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in xrange(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print "Epoch({0}) validation: {1}\n".format(
                    j, self.evaluate(test_data))
            else:
                print "Epoch {0} complete".format(j)
        self.validating = False # Reset validating

    def decide(self, output):
        if output[0] >= .5:
            return 1
        else:
            return 0

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(self.decide(self.feedforward(x)), y)
                        for (x, y) in test_data]

        # Check for and keep track of TP's FP's and FN's
        # Write FP's and FN's to a special directories
        TP = FP = FN = count = 0
        TN = 0
        # what you got = x, what should be  = y
        for ((x, y), (image, gt)) in zip(test_results, test_data):
            count += 1
            if x == 1 and y == 1:
                TP += 1
            elif x == 1 and y == 0:
                FP += 1
                if not self.validating: self.save_Image(FP_PATH, count, image)
            elif x == 0 and y == 1:
                FN += 1
                if not self.validating: self.save_Image(FN_PATH, count, image)
                    
        if (TP + FP ) == 0:
            return TP, FP, FN, '---------', '---------','---------'
        else:
            false_rate = float(FP) / float(TP + FP)

        if (TP + FN ) == 0:
            return TP, FP, FN, '---------', '---------', false_rate
        else:
            detect_rate = float(TP) / float(TP + FN)

        if (TP + FP + FN ) == 0:
            return TP, FP, FN, '---------', detect_rate, false_rate
        else:
            quality_rate = float(TP) / float(TP+FP+FN)
            
        return TP, FP, FN, quality_rate, detect_rate, false_rate
    
    def save_Image(self, path, name, array):
        """Save images to path"""
        # Resize into a 2D array
        shaped_arr = np.reshape((array * 255).astype('uint8'),
                        (self.im_size, self.im_size))
        cv.imwrite("%s/missed_img%s.jpg" % (path, name),shaped_arr)
