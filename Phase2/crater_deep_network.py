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
IMAGE_SIZE = 28
EPOCHS = 50
MB_SIZE = 1
ETA = .0005
RUNS = 1
LAMBDA_LENGTH = 1

PICKLE = "Pickles/elu-network%sx%s" % (IMAGE_SIZE, IMAGE_SIZE)
#training_data, validation_data, test_data = network3.load_data_shared()

# PHASE II -- Crater Data
training_data, validation_data, test_data = \
crater_loader.load_crater_data_phaseII_wrapper("non_rotated_28x28.pkl", IMAGE_SIZE)
total_validation_accuracies = []
total_test_accuracies = []


def leakyrelu():
    net = None
    for j in range(RUNS):
        print "num %s, leaky relu, with regularization %s" % (j, 0.00001)
        net = Network([
            ConvPoolLayer(image_shape=(MB_SIZE, 1, IMAGE_SIZE, IMAGE_SIZE),
                          filter_shape=(5, 1, 15, 15),
                          poolsize=(3, 3),
                          activation_fn=LReLU),
            ConvPoolLayer(image_shape=(MB_SIZE, 5, 29, 29),
                          filter_shape=(10, 5, 2, 2),
                          poolsize=(2, 2),
                          activation_fn=LReLU),
            FullyConnectedLayer(n_in=10*14*14, n_out=200, activation_fn=LReLU),
            FullyConnectedLayer(n_in=200, n_out=200, activation_fn=LReLU),
            FullyConnectedLayer(n_in=200, n_out=100, activation_fn=LReLU),
            SoftmaxLayer(n_in=100, n_out=2)], MB_SIZE)
        net.SGD("leaky", training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=0.001)
        total_validation_accuracies.append(net.validation_accuracies)
        total_test_accuracies.append(net.test_accuracies)
    return net

def elu():
    net = None
    for j in range(RUNS):
        print "num %s, leaky relu, with regularization %s" % (j, 0.0001)
        net = Network([
            ConvPoolLayer(image_shape=(MB_SIZE, 1, IMAGE_SIZE, IMAGE_SIZE),
                          filter_shape=(5, 1, 3, 3),
                          poolsize=(2, 2),
                          activation_fn=LReLU),
            ConvPoolLayer(image_shape=(MB_SIZE, 5, 13, 13),
                          filter_shape=(3, 5, 2, 2),
                          poolsize=(2, 2),
                          activation_fn=LReLU),
            FullyConnectedLayer(n_in=3*6*6, n_out=36, activation_fn=LReLU),
            FullyConnectedLayer(n_in=36, n_out=12, activation_fn=LReLU),
            FullyConnectedLayer(n_in=12, n_out=6, activation_fn=LReLU),
            SoftmaxLayer(n_in=6, n_out=2)], MB_SIZE)
        net.SGD("LReLU_28x28", training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=0.001)
        total_validation_accuracies.append(net.validation_accuracies)
        total_test_accuracies.append(net.test_accuracies)
    return net

def flattenArray(two_d):
    return [element for array in two_d for element in array]

def run_experiments():
    net = elu()
    # tta = flattenArray(total_test_accuracies)
    # tva = flattenArray(total_validation_accuracies)
    # plotDataFit(tta, tva, len(tta), 1, "LReLU_28x28-.0075");
