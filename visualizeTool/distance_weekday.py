#### Import packages

import pandas as pd
import numpy as np
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#### Visualization of the distributions of trip distaces on different days of week;

#### Reads input files from directory named 'distance_weekday', and output plots will be saved under the same directory;

#### Input files should be of the names 'distance_mon', 'distance_tue', 'distance_wed', 'distance_thurs', 
####'distance_fri', 'distance_sat', 'distance_sun';

#### The file should have two columns: first column is the intervals of trip distances, 
#### and the second column is number of trips in the corresponding interval. These two columns should be separated by '\t'.

dist0 = pd.read_csv('./distance_weekday/distance_mon', header = None, delimiter='\t')
dist0.columns = ['distance_range', 'Total Number of Trips']
dist0['distance'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-10', '10-20', '20-30', '30-infinite')
dist1 = pd.read_csv('./distance_weekday/distance_tue', header = None, delimiter='\t')
dist1.columns = ['distance_range', 'Total Number of Trips']
dist1['distance'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-10', '10-20', '20-30', '30-Inifinite') 
dist2 = pd.read_csv('./distance_weekday/distance_wed', header = None, delimiter='\t')
dist2.columns = ['distance_range', 'Total Number of Trips']
dist2['distance'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-10', '10-20', '20-30', '30-Inifinite') 
dist3 = pd.read_csv('./distance_weekday/distance_thurs', header = None, delimiter='\t')
dist3.columns = ['distance_range', 'Total Number of Trips']
dist3['distance'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-10', '10-20', '20-30', '30-Inifinite') 
dist4 = pd.read_csv('./distance_weekday/distance_fri', header = None, delimiter='\t')
dist4.columns = ['distance_range', 'Total Number of Trips']
dist4['distance'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-10', '10-20', '20-30', '30-Inifinite') 
dist5 = pd.read_csv('./distance_weekday/distance_sat', header = None, delimiter='\t')
dist5.columns = ['distance_range', 'Total Number of Trips']
dist5['distance'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-10', '10-20', '20-30', '30-Inifinite') 
dist6 = pd.read_csv('./distance_weekday/distance_sun', header = None, delimiter='\t')
dist6.columns = ['distance_range', 'Total Number of Trips']
dist6['distance'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-10', '10-20', '20-30', '30-Inifinite')

#### For each day of week, a bar-plot will be plotted using the barplot function in seaborn package.
#### Monday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="distance", y="Total Number of Trips", data=dist0, palette=sns.diverging_palette(255, 133, l=60, n=9, center='dark'))
plot.set_xlabel('Range of Distance (in miles)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Distance - Monday', fontsize = 15)
plt.savefig('./distance_weekday/dist_mon.png', dpi=300, bbox_inches='tight')

#### Tuesday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="distance", y="Total Number of Trips", data=dist1, palette=sns.cubehelix_palette(9, start=10, rot=0, dark=0.25, light=.95, reverse=True))
plot.set_xlabel('Range of Distance (in miles)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Distance - Tuesday', fontsize = 15)
plt.savefig('./distance_weekday/dist_tue.png', dpi=300, bbox_inches='tight')

#### Wednesdaay
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="distance", y="Total Number of Trips", data=dist2, palette=sns.cubehelix_palette(9, start=0, rot=0, dark=.2, light=.95, reverse=True))
plot.set_xlabel('Range of Distance (in miles)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Distance - Wednesday', fontsize = 15)
plt.savefig('./distance_weekday/dist_wed.png', dpi=300, bbox_inches='tight')

#### Thursday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="distance", y="Total Number of Trips", data=dist3, palette=sns.cubehelix_palette(9, start=2, rot=0, dark=0.25, light=.95, reverse=True))
plot.set_xlabel('Range of Distance (in miles)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Distance - Thursday', fontsize = 15)
plt.savefig('./distance_weekday/dist_thurs.png', dpi=300, bbox_inches='tight')

#### Friday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="distance", y="Total Number of Trips", data=dist4)
plot.set_xlabel('Range of Distance (in miles)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Distance - Friday', fontsize = 15)
plt.savefig('./distance_weekday/dist_fri.png', dpi=300, bbox_inches='tight')

#### Saturday
sns.dark_palette("muted purple", input="xkcd")
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="distance", y="Total Number of Trips", data=dist5, palette = sns.cubehelix_palette(9, reverse=True))
plot.set_xlabel('Range of Distance (in miles)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Distance - Saturday', fontsize = 15)
plt.savefig('./distance_weekday/dist_sat.png', dpi=300, bbox_inches='tight')

#### Sunday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="distance", y="Total Number of Trips", data=dist6, palette=sns.diverging_palette(145, 280, s=85, l=25, n=9))
plot.set_xlabel('Range of Distance (in miles)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Distance - Sunday', fontsize = 15)
plt.savefig('./distance_weekday/dist_sun.png', dpi=300, bbox_inches='tight')