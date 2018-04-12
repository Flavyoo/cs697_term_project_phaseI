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

# My libraries
import mnist_loader
from crater_network import Network


if len(args) > 1:
    EPOCHS = int(args[1])
else:
    EPOCHS = 5
if len(args) > 2:
    MB_SIZE = int(args[2])
else:
    MB_SIZE = 1000
if len(args) > 3:
    ETA = float(args[3])
else:
    ETA = 1


def main():

    # Load the data
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

    # training phase: compute the average darknesses for each digit,
    # based on the training data

    # Make the network
    print "Making Network...."
    netwk = Network([28*28,30,10])
    print "Training the Network...."
    netwk.SGD(training_data, EPOCHS, MB_SIZE, ETA, test_data=validation_data)


    # testing phase: see how many of the test images are classified
    # correctly

    # Evaluate results
    eval = netwk.evaluate(validation_data)


    print eval


if __name__ == "__main__":
    main()
