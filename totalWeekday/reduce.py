#!/usr/bin/python

import sys

intervals = ['0,10', '10.01,20', '20.01,30', '30.01,40', '40.01,50', '50.01,60', '60.01,70', '70.01,80', '80.01,infinite']
intervals_dict = {'0,10':0, '10.01,20':0, '20.01,30':0, '30.01,40':0, '40.01,50':0, '50.01,60':0, '60.01,70':0, '70.01,80':0, '80.01,infinite':0}

for line in sys.stdin:
    line = line.strip()
    key, interval, fare = line.split('\t')
    if key == '5': #0-6 represents Mon-Sun
    	intervals_dict[interval] += 1

for interval in intervals:
    if intervals_dict[interval] > 0:
        print interval + "\t" + str(intervals_dict[interval])




