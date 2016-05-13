#!/usr/bin/python

import sys
import math

'''
Input:
The MapReduce output at our first step, containing features including pick-up longitude and latitude
Output:
key-value pairs(key, 1) as the key indicating the grid index of the location
'''

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    lines = line.strip().split('\t')[1].strip().split(',')

    try:
        longitude = float(lines[4])
        latitude = float(lines[5])
    except ValueError:
        continue

    if longitude > -73.82 or longitude < -74.02:
        continue
    if latitude > 40.9 or latitude < 40.7:
        continue

    district = int(math.ceil(200*(math.floor((40.9-latitude)/0.001)))+math.ceil((longitude-(-74.02))/0.001))    
    
    print '%s\t%s' %(district, 1)



