from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import cPickle
import theano
import os
import theano.tensor as T
from network3 import *
from plotdatafitting import plotDataFit
import crater_loader
# uncomment if you do not want graph to show up.
IMAGE_SIZE = 101
EPOCHS = 10
MB_SIZE = 1
ETA = .0005
RUNS = 1
LAMBDA_LENGTH = 1

PICKLE = "Pickle_Stash/GEN3-LReLU-val0.9806-tst0.9805.pkl"
#training_data, validation_data, test_data = network3.load_data_shared()

# PHASE II -- Crater Data
training_data, validation_data, test_data = \
crater_loader.load_crater_data_phaseII_wrapper("101x101.pkl", 101)


if __name__ == "__main__":
    net = cPickle.load(open(PICKLE, 'rb'))
    os.system('rm Pickles/*.pkl')
    net.SGD("GEN2-LReLU", training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=0.0001)
