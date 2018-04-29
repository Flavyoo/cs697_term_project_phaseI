#!/usr/bin/python
"""
run_experiment.py
~~~~~~~~~~~~~~~~~~~~~~
Garret, Euclides

This program reads data from a pickle file using the load_crater_data_wrapper
function to get the training and test data. We create a neural network and run
the Stochastic Gradient Descent algorithm using the training data set to train the network.

Then, the test data is evaluated using the calculated weights and biases from the
Stochastic Gradient Descent Algorithm that was ran.

The results are then printed out.
"""
#### Libraries
# Standard library
from sys import argv as args
import os
from crater_loader import load_crater_data_wrapper
# Our modules
import mnist_loader
from crater_network import Network
from crater_network2 import CraterNetwork
# Image Size
SIZE = 200
OUTPUT_LAYER = 1
# Default settings
EPOCHS = 30
MB_SIZE = 1
ETA = .5
HIDDEN_LAYER = 400

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
    training_data, test_data = load_crater_data_wrapper('scaled-data.pkl')

    # Make the network
    print "Making Network...."
    print "Parameters: "
    print "  Epochs  = %s" % EPOCHS
    print "  MB_Size = %s" % MB_SIZE
    print "  Eta     = %s" % ETA
    print "  Hid Lyr = %s" % HIDDEN_LAYER
    # to use the Network, replace CraterNetwork with Network
    netwk = CraterNetwork([SIZE*SIZE,HIDDEN_LAYER,OUTPUT_LAYER], SIZE)
=======
<<<<<<< HEAD
    # to use the Network, replace CraterNetwork with Network
    netwk = CraterNetwork([SIZE*SIZE,HIDDEN_LAYER, OUTPUT_LAYER], SIZE)
<<<<<<< HEAD
=======
=======
>>>>>>> 9a39fb5b8865f7cd799049059648a4a5b9b01d42
>>>>>>> 6e2040f92b577d2d9e9c39f719efd173fbd1c5ec
>>>>>>> f8cb0ab194b3bbf0395afd78e95d2b1f2b4d9ef2

    print "Training the Network...."
    netwk.SGD(training_data, EPOCHS, MB_SIZE, ETA, test_data=test_data)
    # testing phase: see how many of the test images are classified
    # correctly
    # Evaluate results
    print "Evaluating test data..."
    eval = netwk.evaluate(test_data)
    os.system("echo %s >> results.csv" % ','.join(map(str, eval)))
    print eval

if __name__ == "__main__":
    main()
