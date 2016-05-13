#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    value = value.split(',')
    fare = float(value[10])
    if fare <= 10:
        print '%s\t0,10\t' %key + str(fare)
    elif fare <= 20:
        print '%s\t10.01,20\t' %key + str(fare)
    elif fare <= 30: 
        print '%s\t20.01,30\t' %key + str(fare)
    elif fare <= 40:
        print '%s\t30.01,40\t' %key + str(fare)
    elif fare <= 50:
        print '%s\t40.01,50\t' %key + str(fare)
    elif fare <= 60:
        print '%s\t50.01,60\t' %key + str(fare)
    elif fare <= 70:
        print '%s\t60.01,70\t' %key + str(fare)
    elif fare <= 80:
        print '%s\t70.01,80\t' %key + str(fare)
    else:
        print '%s\t80.01,infinite\t' %key + str(fare)
    
