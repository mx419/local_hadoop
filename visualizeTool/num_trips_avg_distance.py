#### Import packages
import pandas as pd
import numpy as np
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#### Visualization of the total number of trips on different days of week and the average distance per trip on different days of week;

#### Reads an input file names 'avg_dis' from the current working directory, and output plots will be saved under the current working directory;

#### The file should have two columns separated by '\t': first column is days of week, 
#### and the column contains the total distances, total number of trips, and average distance per trip, separated by comma.
data = pd.read_csv('avg_dis', header = None, delimiter='\t') 
data['total_distance']=[float(i.split(',')[0]) for i in data[1].values]
data['num_trips']=[float(i.split(',')[1]) for i in data[1].values]
data['avg_distance']=[float(i.split(',')[2]) for i in data[1].values]
data.drop(data.columns[[1]], axis = 1,inplace = True)
data.columns = ['day_of_week', 'total_distance', 'num_trips', 'avg_distance']
data['day_of_week'] = ('Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plt.figure(figsize=(20,10))
data.plot(x='day_of_week', y='num_trips', color = 'forestgreen', linewidth=1)
plt.ylabel('Total Number of Trips (in million)')
plt.xlabel('Day of Week')
plt.title('Number of Taxi Trips on Different Days of Week in 2015', fontsize = 10)

plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.yticks([16000000, 17000000, 18000000, 19000000, 20000000, 21000000, 22000000,23000000], [16, 17, 18, 19, 20, 21, 22, 23])
plt.legend(['Taxi trips'], loc='lower center')
plt.savefig('num_trips_dayweek.png', dpi=100)

sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plt.figure(figsize=(20,10))
data.plot(x='day_of_week', y='avg_distance', color = 'mediumslateblue', linewidth=1)
plt.ylabel('Average Distance per Trip (in miles)')
plt.xlabel('Day of Week')
plt.title('Average Distance per Trip on Different Days of Week in 2015', fontsize = 10)

plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
#plt.yticks([16000000, 17000000, 18000000, 19000000, 20000000, 21000000, 22000000,23000000])
plt.legend(['Average distance'], loc='lower center')
plt.savefig('avg_dist.png', dpi=100)