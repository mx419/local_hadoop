## User Guide
- DS-GA-1004  Final Project:           
An Exploration of New York Taxi Data 
-- Analysis of Passengers’ Travel Behaviour 

- Team Member:
  - Muhe Xie(mx419) mx419@nyu.edu
  - Junchao Zheng(jz2327) jz2327@nyu.edu
  - Li Ke (lk1818) lk1818@nyu.edu

### Part 1: Environment Setup （Mac or Linux）
1. Install map plot package: gmplot
``` sh
$ pip install gmplot
```
Click [gmplot 1.0.5](https://pypi.python.org/pypi/gmplot/1.0.5) for more detailed information  

2. Install statistical data visualization package: Seaborn (needs numpy,  scipy, matplotlib, pandas be installed first)
``` sh
$ pip install seaborn
```
Click [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/installing.html) for more detailed information  
### Part 2:Data Source
1. NYC Yellow Taxi Data(2015):  http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml 
2. Uber Data: https://github.com/fivethirtyeight/uber-tlc-foil-response
3. id_location_uber.p: hand coded dictionary for uber id, each location ID as the key and the latitude and longitude as value.

### Part 3: How to run the program (based on nyu hpc dumbo)
1. Use map and reduce under basicMapReduce directory to process the data:
* (can set mapreduce.job.reduces=7), the result of a single line includes: (key(which day of the week) \t tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, fare_amount, tip_amount, total_amount,key)
* The result will be the basic input of the most following map reduce functions

2. Map and Reduce under averageTripDistancebyDay directory:
 * Get the total trip number and average trip distance for each day of the week. 
 * The result has 7 lines and 3 columns: each line represent a day of the week, column 1 is the sum of distance, column2 is the total trip number, column3 is the average distance
  
 3. Map and Reduce under distanceWeekday directory:
 * Get the distribution of the distance for each day of the week.
 * Change the if condition to select which day to compute.
 
4. Map and Reduce under tipWeekday directory:
 * Get the distribution of the tip amount for each day of the week.
 * Change the if condition to select which day to compute.

5. Map and Reduce under totalWeekday directory:
 * Get the distribution of the total amount for each day of the week.
 * Change the if condition to select which day to compute.

6. Visualization Code for results of 2-5: visualizeTool directory.

Instruction: Download this directory, cd to visualizeResults Directory,
the input file has already been put and renamed there, just use the commands below:
  * Visualize 2:  
   ```sh
  $ python num_trips_avg_distance.py
  ```
  * Visualize 3:  
   ```sh
  $ python distance_weekday.py
  ```

 * Visualize 4:  
  ```sh
  $ python tipamount_weekday.py
  ```
 * Visualize 5:  
  ```sh
  $ python totalamount_weekday.py
  ```
  
7. gmPlot Directory: the sample generated htmls file are under sampleOutput directory
  * Use map reduce under gmPlot/area and gmPlot/drop_off_area to do the calculation of count number for each square grid. The input for these map-reduces are the output of 1
  * cd to the gmplot_sample directory, put the output of gmPlot/drop_off_area's map reduce to the proper path stated in  gmplot_dropoff.py file, use command: 
  ```sh
  $ python gmplot_dropoff.py
  ```
  * cd to the gmplot_sample directory, put the output of gmPlot/area's map reduce to the proper path stated in gmplot_taxi.py file, use command: 
  ```sh
  $ python gmplot_taxi.py
  ```
  * cd to the gmplot_sample directory, put the id_location_uber.p file and the uber data: uber-raw-data-janjune-15.csv to the proper path stated in gmplot_uber.py file, use command: 
  ```sh
  $ python gmplot_uber.py
  ```
  
  Thanks for your time!















