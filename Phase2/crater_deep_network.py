from collections import Counter

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import cPickle
import theano
import theano.tensor as T

import network3
from network3 import sigmoid, tanh, ReLU, LReLU, ELU, Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer

import crater_loader

IMAGE_SIZE = 100

EPOCHS = 15
MB_SIZE = 1
ETA = .005
RUNS = 1

PICKLE = "Pickles/elu-network%sx%s" % (IMAGE_SIZE, IMAGE_SIZE)

#training_data, validation_data, test_data = network3.load_data_shared()

# PHASE II -- Crater Data
training_data, validation_data, test_data = \
   crater_loader.load_crater_data_phaseII_wrapper("new_100x100.pkl", 100)

def leakyrelu():
    net = None
    for lmbda in [0.0, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]:
        for j in range(RUNS):
            print "num %s, leaky relu, with regularization %s" % (j, lmbda)
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
            net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=lmbda)
    return net

def elu():
    net = None
    for lmbda in [0.0, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]:
        for j in range(RUNS):
            print "num %s, leaky relu, with regularization %s" % (j, lmbda)
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
            net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=lmbda)
    return net

def run_experiments():
    # leakyrelu()
    net = elu()
    cPickle.dump(net, open(PICKLE, 'wb'))
    predictions = net.test_mb_accuracy(0)
