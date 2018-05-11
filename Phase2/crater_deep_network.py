from collections import Counter

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import theano
import theano.tensor as T
import network3
from network3 import sigmoid, tanh, ReLU, LReLU, ELU, Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
import conv
import crater_loader

IMAGE_SIZE = 200
EPOCHS = 10
MB_SIZE = 1
ETA = .03
RUNS = 1

training_data, validation_data, test_data = \
   crater_loader.load_crater_data_phaseII_wrapper("phase2-data-200x200.pkl", 200)

def leakyrelu():
    net = None
    for lmbda in [0.0, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]:
        for j in range(RUNS):
            print "num %s, leaky relu, with regularization %s" % (j, lmbda)
            net = Network([
                ConvPoolLayer(image_shape=(MB_SIZE, 1, IMAGE_SIZE, IMAGE_SIZE),
                              filter_shape=(20, 1, 4, 4),
                              poolsize=(2, 2),
                              activation_fn=LReLU),
                ConvPoolLayer(image_shape=(MB_SIZE, 20, 197, 197),
                              filter_shape=(40, 20, 5, 5),
                              poolsize=(2, 2),
                              activation_fn=LReLU),
                FullyConnectedLayer(n_in=98 * 98, n_out=400, activation_fn=LReLU),
                FullyConnectedLayer(n_in=400, n_out=200, activation_fn=LReLU),
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
                              filter_shape=(20, 1, 5, 5),
                              poolsize=(2, 2),
                              activation_fn=ELU),
                ConvPoolLayer(image_shape=(MB_SIZE, 20, 12, 12),
                              filter_shape=(40, 20, 5, 5),
                              poolsize=(2, 2),
                              activation_fn=ELU),
                FullyConnectedLayer(n_in=40*4*4, n_out=400, activation_fn=ELU),
                FullyConnectedLayer(n_in=400, n_out=200, activation_fn=ELU),
                FullyConnectedLayer(n_in=200, n_out=100, activation_fn=ELU),
                SoftmaxLayer(n_in=100, n_out=2)], MB_SIZE)
            net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=lmbda)
    return net

def run_experiments():
    #conv.omit_FC()
    net = leakyrelu()
    # elu()
