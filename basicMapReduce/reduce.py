#!/usr/bin/python
from operator import itemgetter
import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    if len(line) > 0:

        print line.strip()

