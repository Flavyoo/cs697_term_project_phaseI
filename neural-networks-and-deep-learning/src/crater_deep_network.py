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

EPOCHS = 10
MB_SIZE = 10
ETA = .03
training_data, validation_data, test_data = network3.load_data_shared()


def dbl_conv_leakyrelu():
    for lmbda in [0.0, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]:
        for j in range(3):
            print "Conv + Conv + FC num %s, leaky relu, with regularization %s" % (j, lmbda)
            net = Network([
                ConvPoolLayer(image_shape=(MB_SIZE, 1, 28, 28), 
                              filter_shape=(20, 1, 5, 5), 
                              poolsize=(2, 2), 
                              activation_fn=LReLU),
                ConvPoolLayer(image_shape=(MB_SIZE, 20, 12, 12), 
                              filter_shape=(40, 20, 5, 5), 
                              poolsize=(2, 2), 
                              activation_fn=LReLU),
                ConvPoolLayer(image_shape=(MB_SIZE, 20, 12, 12), 
                              filter_shape=(40, 20, 5, 5), 
                              poolsize=(2, 2), 
                              activation_fn=LReLU),
                ConvPoolLayer(image_shape=(MB_SIZE, 20, 12, 12), 
                              filter_shape=(40, 20, 5, 5), 
                              poolsize=(2, 2), 
                              activation_fn=LReLU),
                FullyConnectedLayer(n_in=40*4*4, n_out=100, activation_fn=LReLU),
                SoftmaxLayer(n_in=100, n_out=10)], MB_SIZE)
            net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=lmbda)
            
def dbl_conv_ELU():
    for lmbda in [0.0, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]:
        for j in range(3):
            print "Conv + Conv + FC num %s, leaky relu, with regularization %s" % (j, lmbda)
            net = Network([
                ConvPoolLayer(image_shape=(MB_SIZE, 1, 28, 28), 
                              filter_shape=(20, 1, 5, 5), 
                              poolsize=(2, 2), 
                              activation_fn=ELU),
                ConvPoolLayer(image_shape=(MB_SIZE, 20, 12, 12), 
                              filter_shape=(40, 20, 5, 5), 
                              poolsize=(2, 2), 
                              activation_fn=ELU),
                ConvPoolLayer(image_shape=(MB_SIZE, 1, 28, 28), 
                              filter_shape=(20, 1, 5, 5), 
                              poolsize=(2, 2), 
                              activation_fn=ELU),
                ConvPoolLayer(image_shape=(MB_SIZE, 20, 12, 12), 
                              filter_shape=(40, 20, 5, 5), 
                              poolsize=(2, 2), 
                              activation_fn=ELU),
                FullyConnectedLayer(n_in=40*4*4, n_out=100, activation_fn=ELU),
                SoftmaxLayer(n_in=100, n_out=10)], MB_SIZE)
            net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=lmbda)

def run_experiments():
    dbl_conv_leakyrelu()
    dbl_conv_ELU()
