#!/usr/bin/python
import os
from sys import argv as args

c = 0
with open(args[1], 'r') as f:
    for line in f:
        if c > 2:
            pid  = line.split(' ')[0]
            print "killing %s" % pid
            os.system("kill %s" % pid)
        c += 1
