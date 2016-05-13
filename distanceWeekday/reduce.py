#!/usr/bin/python
#change the condition to compute one of 7 days of the week
import sys

intervals = ['0,1', '1.01,2', '2.01,3', '3.01,4', '4.01,5', '5.01,10', '10.01,20', '20.01,30', '30.01,infinite']
intervals_dict = {'0,1':0, '1.01,2':0, '2.01,3':0, '3.01,4':0, '4.01,5':0, '5.01,10':0, '10.01,20':0, '20.01,30':0, '30.01,infinite':0}

for line in sys.stdin:
    line = line.strip()
    key, interval, distance = line.split('\t')
    if key == '6':  # 0-6 represents Mon-Sun
        intervals_dict[interval] += 1

for interval in intervals:
    if intervals_dict[interval] > 0:
        print interval + "\t" + str(intervals_dict[interval])




