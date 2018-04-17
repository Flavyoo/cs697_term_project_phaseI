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

# Image Size
SIZE = 200
OUTPUT_LAYER = 2

# Default settings
EPOCHS = 5
MB_SIZE = 16
ETA = .9
HIDDEN_LAYER = 30

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
    print "Parameters: "
    print "  Epochs  = %s" % EPOCHS
    print "  MB_Size = %s" % MB_SIZE
    print "  Eta     = %s" % ETA
    print "  Hid Lyr = %s" % HIDDEN_LAYER
    netwk = Network([SIZE*SIZE,HIDDEN_LAYER,OUTPUT_LAYER], SIZE)
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
