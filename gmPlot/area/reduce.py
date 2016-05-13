#!/usr/bin/python

'''
Input:
The key-value pair from mapper (key, 1)
Output:
add the value with the same key together to produce the frequency count
'''

import sys

current_district = None
current_sum = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    district, count = line.strip().split('\t')
    
    count = int(count)
    
    if district == current_district:
        current_sum += count
    else:
        if current_district:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d" %( current_district, current_sum )
        current_district = district
        current_sum = count

print "%s\t%d" %(current_district, current_sum)

