#!/usr/bin/python

import sys
from datetime import datetime

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line_str = line.strip()
    lines = line_str.split(',')

    # skip header
    if lines[0] == 'VendorID':
        continue

    weekday_pickup = str((datetime.strptime(lines[1], '%Y-%m-%d %H:%M:%S').weekday()))
    weekday_dropoff = str((datetime.strptime(lines[2], '%Y-%m-%d %H:%M:%S').weekday()))

    line_to_delete = [17,16,14,13,11,8,7,0]

    for variable in line_to_delete: 
        del lines[variable]

    lines.append(weekday_dropoff)

    value = ','.join(lines)

    print '%s\t%s' %(weekday_pickup, value)



