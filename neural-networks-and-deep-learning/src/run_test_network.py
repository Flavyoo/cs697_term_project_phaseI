#!/usr/bin/python

"""
run_test_network.py
~~~~~~~~~~~~~~~~~~~~~~

Garrett trying to get network.py running on the digit dataset

Copied from mnist_average_darkness.py

"""

#### Libraries
# Standard library
from sys import argv as args
import os
from crater_loader import load_crater_data_wrapper
# My libraries
import mnist_loader
from crater_network import Network
import numpy as np

NON_CRATER_SIZE = 656
CRATER_SIZE = 323

np.set_printoptions(threshold=np.nan)
# Default settings
EPOCHS = 5
MB_SIZE = 1000
ETA = .1
HIDDEN_LAYER = 100
INPUT_LAYER_SIZE = 200

if len(args) > 1:
    if args[1] != '.': EPOCHS = int(args[1])
if len(args) > 2:
    if args[2] != '.': MB_SIZE = int(args[2])
if len(args) > 3:
    if args[3] != '.': ETA = float(args[3])
if len(args) > 4:
    if args[4] != '.': HIDDEN_LAYER = int(args[4])


def main():

    # Preparing test directories
    print "Preparing test directories"
    os.system("./del")

    # Load the data
    training_data, test_data = load_crater_data_wrapper('data.pkl')

    #training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

    # training phase: compute the average darknesses for each digit,
    # based on the training data

    # Make the network
    print "Making Network...."
    netwk = Network([INPUT_LAYER_SIZE * INPUT_LAYER_SIZE,HIDDEN_LAYER,1])
    print "Training the Network...."
    netwk.SGD(training_data, EPOCHS, MB_SIZE, ETA, test_data=test_data)
    # testing phase: see how many of the test images are classified
    # correctly
    # Evaluate results
    print "Evaluating test data..."
    eval = netwk.evaluate(test_data)
    print eval


if __name__ == "__main__":
    main()
