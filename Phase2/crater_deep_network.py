from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import cPickle
import theano
import theano.tensor as T
from network3 import *
from plotdatafitting import plotDataFit
import crater_loader
# uncomment if you do not want graph to show up.
IMAGE_SIZE = 101
EPOCHS = 20
MB_SIZE = 1
ETA = .005
RUNS = 1
LAMBDA_LENGTH = 1

PICKLE = "Pickles/elu-network%sx%s" % (IMAGE_SIZE, IMAGE_SIZE)
#training_data, validation_data, test_data = network3.load_data_shared()

# PHASE II -- Crater Data
training_data, validation_data, test_data = \
crater_loader.load_crater_data_phaseII_wrapper("101x101.pkl", 101)
total_validation_accuracies = []
total_test_accuracies = []


def leakyrelu():
    net = None
    for j in range(RUNS):
        print "num %s, leaky relu, with regularization %s" % (j, 0.00001)
        net = Network([
            ConvPoolLayer(image_shape=(MB_SIZE, 1, IMAGE_SIZE, IMAGE_SIZE),
                          filter_shape=(5, 1, 12, 12),
                          poolsize=(3, 3),
                          activation_fn=LReLU),
            ConvPoolLayer(image_shape=(MB_SIZE, 5, 30, 30),
                          filter_shape=(10, 5, 3, 3),
                          poolsize=(2, 2),
                          activation_fn=LReLU),
            FullyConnectedLayer(n_in=10*14*14, n_out=200, activation_fn=LReLU),
            FullyConnectedLayer(n_in=200, n_out=200, activation_fn=LReLU),
            FullyConnectedLayer(n_in=200, n_out=100, activation_fn=LReLU),
            SoftmaxLayer(n_in=100, n_out=2)], MB_SIZE)
        net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=0.00001)
        total_validation_accuracies.append(net.validation_accuracies)
        total_test_accuracies.append(net.test_accuracies)
    return net

def elu():
    net = None
    for j in range(RUNS):
        print "num %s, leaky relu, with regularization %s" % (j, 0.0001)
        net = Network([
            ConvPoolLayer(image_shape=(MB_SIZE, 1, IMAGE_SIZE, IMAGE_SIZE),
                          filter_shape=(5, 1, 12, 12),
                          poolsize=(3, 3),
                          activation_fn=LReLU),
            ConvPoolLayer(image_shape=(MB_SIZE, 5, 30, 30),
                          filter_shape=(10, 5, 3, 3),
                          poolsize=(2, 2),
                          activation_fn=LReLU),
            FullyConnectedLayer(n_in=10*14*14, n_out=200, activation_fn=LReLU),
            FullyConnectedLayer(n_in=200, n_out=200, activation_fn=LReLU),
            FullyConnectedLayer(n_in=200, n_out=100, activation_fn=LReLU),
            SoftmaxLayer(n_in=100, n_out=2)], MB_SIZE)
        net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=0.0001)
        total_validation_accuracies.append(net.validation_accuracies)
        total_test_accuracies.append(net.test_accuracies)
    return net

def flattenArray(two_d):
    return [element for array in two_d for element in array]

def run_experiments():
    """
    the length of the test and validation accuracies may be different
    so i only save the best validation accuracies, and use the length of
    the resulting array instead of the number of epochs
    """
    #leakyrelu()
    net = leakyrelu()
    #cPickle.dump(net, open(PICKLE, 'wb'))
    #predictions = net.test_mb_accuracy(0)
    tta = flattenArray(total_test_accuracies)
    tva = flattenArray(total_validation_accuracies)
    plotDataFit(tta, tva, len(tta), 1, "leakyrelu_20Epochs");
