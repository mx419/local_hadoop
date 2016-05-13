#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = value.split(',')
    distance = float(value[3])
    if distance <= 1:
        print '%s\t0,1\t' %key + str(distance)
    elif distance <= 2:
        print '%s\t1.01,2\t' %key + str(distance)
    elif distance <= 3: 
        print '%s\t2.01,3\t' %key + str(distance)
    elif distance <= 4:
        print '%s\t3.01,4\t' %key + str(distance)
    elif distance <= 5:
        print '%s\t4.01,5\t' %key + str(distance)
    elif distance <= 10:
        print '%s\t5.01,10\t' %key + str(distance)
    elif distance <= 20:
        print '%s\t10.01,20\t' %key + str(distance)
    elif distance <= 30:
    	print '%s\t20.01,30\t' %key + str(distance)
    else:
        print '%s\t30.01,infinite\t' %key + str(distance)
    
