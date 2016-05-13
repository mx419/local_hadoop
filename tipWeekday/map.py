#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = value.split(',')
    fare = float(value[9])
    if fare <= 1:
        print '%s\t0,1\t' %key + str(fare)
    elif fare <= 2:
        print '%s\t1.01,2\t' %key + str(fare)
    elif fare <= 3: 
        print '%s\t2.01,3\t' %key + str(fare)
    elif fare <= 4:
        print '%s\t3.01,4\t' %key + str(fare)
    elif fare <= 5:
        print '%s\t4.01,5\t' %key + str(fare)
    elif fare <= 6:
        print '%s\t5.01,6\t' %key + str(fare)
    elif fare <= 7:
        print '%s\t6.01,7\t' %key + str(fare)
    else:
        print '%s\t7.01,infinite\t' %key + str(fare)
    
