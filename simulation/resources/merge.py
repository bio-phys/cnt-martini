#!/usr/bin/env python

import sys

f = [open(i).readlines() for i in sys.argv[1:]]
print "Merged gro file\n%5d" % (sum([len(i) for i in f]) - 3*len(f))
print "".join(["".join(i[2:-1]) for i in f]),
print f[0][-1]

