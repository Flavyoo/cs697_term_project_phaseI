#!/usr/bin/python

import os
from sys import argv as args

# Default settins
PICKLES = "Pickles"

# Default args
EPOCHS = 5
MB_SIZE = 16
ETA = .9
HIDDEN_LAYER = 30
NUM_TESTS = 10
PICKLE_IN = "False"

if len(args) > 1:
    if args[1] != '.': EPOCHS = int(args[1])
if len(args) > 2:
    if args[2] != '.': MB_SIZE = int(args[2])
if len(args) > 3:
    if args[3] != '.': ETA = float(args[3])
if len(args) > 4:
    if args[4] != '.': HIDDEN_LAYER = int(args[4])
if len(args) > 5:
    if args[5] != '.': NUM_TESTS = int(args[5])
if len(args) > 6:
    if args[6] != '.': PICKLE_IN = "True"

os.system("rm -f results.csv")
os.system("touch results.csv")
os.system("rm -f test*.out")
os.system("rm -rf %s/test*" % PICKLES)
for i in range(NUM_TESTS):
    print "Running test number %s..." % i
    os.system("nohup ./run_experiment.py %s %s %s %s %s %s > test%s.out &" %
                (EPOCHS, MB_SIZE, ETA, HIDDEN_LAYER, i, PICKLE_IN, i))
