#!/usr/bin/python

'''
Input:
The MapReduce output at our first step, containing features including drop-off longitude and latitude
Output:
key-value pairs((weekday_key, grid_index), 1) as the weekday_key indicating whether it is a weekday or weekend, grid_index indicating the spatial index of the location
'''

import sys
import math

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    weekday, line_info = line.strip().split('\t')

    line_info = line_info.strip().split(',')

    try:
        weekday = int(weekday)
        longitude = float(line_info[6])
        latitude = float(line_info[7])
    except ValueError:
        continue

    if longitude > -73.82 or longitude < -74.02:
        continue
    if latitude > 40.9 or latitude < 40.7:
        continue

    district = int(math.ceil(200*(math.floor((40.9-latitude)/0.001)))+math.ceil((longitude-(-74.02))/0.001))    
    
    if weekday <= 4:
        week_key = 0
    else:
        week_key = 1

    key = str(district) + ',' + str(week_key)
    print '%s\t%s' %(key, 1)



