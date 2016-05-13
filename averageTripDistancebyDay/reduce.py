#!/usr/bin/python

import sys

#current_date_list = [] #dates for one medallion
current_key = None
current_sum_distance = 0 #total
current_count =0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin: 

    key,distance = line.strip().split('\t')
    curdistance = float(distance)
    


    if key == current_key:
        current_sum_distance += curdistance
        current_count += 1

        

    else:
        if current_key:


            average_distance = float(current_sum_distance)/float(current_count)
            #average_number_str = "%.2f" % average_number
            print "%s\t%s,%s,%s" %(current_key,str(current_sum_distance),str(current_count),str(average_distance))
                
        
        current_key = key 
        current_sum_distance = curdistance
        current_count =1 

average_distance = float(current_sum_distance)/float(current_count)
#average_number_str = "%.2f" % average_numbers
print "%s\t%s,%s,%s" %(current_key,str(current_sum_distance),str(current_count),str(average_distance))

