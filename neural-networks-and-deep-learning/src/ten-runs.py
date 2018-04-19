#!/usr/bin/python

import os

for i in range(10):
    os.system("nohup > test%s.out" % i)
