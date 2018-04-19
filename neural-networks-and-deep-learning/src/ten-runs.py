#!/usr/bin/python

import os
from sys import argv as args

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

os.system("rm results.csv")
os.system("touch results.csv")
for i in range(10):
    print "Running test number %s..." % i
    os.system("nohup ./run_experiment.py %s %s %s %s > test%s.out &" %
                (EPOCHS, MB_SIZE, ETA, HIDDEN_LAYER, i))


os.system("jobs")
