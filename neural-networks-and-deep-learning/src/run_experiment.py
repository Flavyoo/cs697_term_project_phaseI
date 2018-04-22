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
import pickle

# My libraries
import mnist_loader
from crater_network import Network

# Default settings
SIZE = 200
OUTPUT_LAYER = 1

# Default args
EPOCHS = 5
MB_SIZE = 16
ETA = .9
HIDDEN_LAYER = 30
TEST = 'test'
PICKLE_IN = False

if len(args) > 1:
    if args[1] != '.': EPOCHS = int(args[1])
if len(args) > 2:
    if args[2] != '.': MB_SIZE = int(args[2])
if len(args) > 3:
    if args[3] != '.': ETA = float(args[3])
if len(args) > 4:
    if args[4] != '.': HIDDEN_LAYER = int(args[4])
if len(args) > 5:
    if args[5] != '.': TEST = TEST + str(args[5])
if len(args) > 6:
    if args[6] != '.': PICKLE_IN = "epoch.pkl"

PICKLE_DIR = "Pickles/%s" % TEST
os.system("mkdir -p %s" % PICKLE_DIR)

def pickle_it(epoch, dir):
    pickle_out = open("%s/epoch.pkl" % dir, 'wb')
    pickle.dump(epoch, pickle_out)
    pickle_out.close()

def get_pickle():
    pickle_in = open("epoch.pkl", 'rb')
    epoch = pickle.load(pickle_in)
    pickle_in.close()
    return epoch

def deploy_pickle(netwk):
    best = netwk.ranker.best_epoch()
    pickle_it((best.weights, best.biases), PICKLE_DIR)
    os.system("rm -f *.qr")
    os.system("touch %s/%s.qr" % (PICKLE_DIR,best.qr))
    print "BEST EPOCH: %s" % best

def main():
    # Preparing test directories
    print "Preparing test directories"
    os.system("./del")

    # Load the data
    training_data, test_data = load_crater_data_wrapper('scaled-data.pkl')

    # training phase: compute the average darknesses for each digit,
    # based on the training data

    # Make the network
    print "Making Network...."
    print "Parameters: "
    print "  Epochs  = %s" % EPOCHS
    print "  MB_Size = %s" % MB_SIZE
    print "  Eta     = %s" % ETA
    print "  Hid Lyr = %s" % HIDDEN_LAYER
    if PICKLE_IN:
        print "THIS IS IS PICKLE_IN --- %s" % PICKLE_IN
        epoch = get_pickle()
        netwk = Network([SIZE*SIZE,HIDDEN_LAYER,OUTPUT_LAYER], SIZE, epoch)
    else:
        netwk = Network([SIZE*SIZE,HIDDEN_LAYER,OUTPUT_LAYER], SIZE)
    print "Training the Network...."
    netwk.SGD(training_data, EPOCHS, MB_SIZE, ETA, test_data=test_data)

    # testing phase: see how many of the test images are classified
    # correctly
    # Evaluate results
    print "Evaluating test data..."
    eval = netwk.evaluate(test_data)
    os.system("echo %s >> results.csv" % ','.join(map(str, eval)))

    # Getting best epoch and exporting as pickle
    print "Exporting pickle..."
    deploy_pickle(netwk)

    # Print final results
    print eval


if __name__ == "__main__":
    main()
