#!/usr/bin/python

#get average distance for each weekday also total number of trips each weekday


import sys


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line_str = line.strip()
    line_strlist = line_str.split('\t')
    if len(line_strlist) ==2:
        original_key,original_value = line_str.split('\t')


        original_value_list = original_value.split(',')
        
        distance = original_value_list[3] #str
        try:
            distance = float(distance)
            if distance>0 and distance<=30:
                print "%s\t%s" % (original_key,str(distance))
        
        except:
            continue
        


