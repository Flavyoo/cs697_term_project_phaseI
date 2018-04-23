#!/usr/bin/python
import os
from sys import argv as args

with open(args[1], 'r') as f:
    for line in f:
        pid  = line.split(' ')[0]
        print "killing %s" % pid
        os.system('kill %s'  % pid)
