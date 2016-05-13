#### Import packages

import pandas as pd
import numpy as np
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#### Visualization of the distributions of total fare amount on different days of week;

#### Reads input files from directory named 'totalamount_weekday', and output plots will be saved under the same directory;

#### Input files should be of the names 'totalmount_mon', 'totalamount_tue', 'totalamount_wed', 'totalamount_thurs', 
####'totalamount_fri', 'totalamount_sat', 'totalamount_sun';

#### The file should have two columns: first column is the interval of total amount, 
#### and the second column is number of trips in the corresponding interval. These two columns should be separated by '\t'.

total0 = pd.read_csv('./totalamount_weekday/totalamount_mon', header = None, delimiter='\t')
total0.columns = ['totalamount_range', 'Total Number of Trips']
total0['totalamount_range'] = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-27', '70-80', '80-infinite')
total1 = pd.read_csv('./totalamount_weekday/totalamount_tue', header = None, delimiter='\t')
total1.columns = ['totalamount_range', 'Total Number of Trips']
total1['totalamount_range'] = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-27', '70-80', '80-infinite') 
total2 = pd.read_csv('./totalamount_weekday/totalamount_wed', header = None, delimiter='\t')
total2.columns = ['totalamount_range', 'Total Number of Trips']
total2['totalamount_range'] = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-27', '70-80', '80-infinite') 
total3 = pd.read_csv('./totalamount_weekday/totalamount_thurs', header = None, delimiter='\t')
total3.columns = ['totalamount_range', 'Total Number of Trips']
total3['totalamount_range'] = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-27', '70-80', '80-infinite') 
total4 = pd.read_csv('./totalamount_weekday/totalamount_fri', header = None, delimiter='\t')
total4.columns = ['totalamount_range', 'Total Number of Trips']
total4['totalamount_range'] = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-27', '70-80', '80-infinite') 
total5 = pd.read_csv('./totalamount_weekday/totalamount_sat', header = None, delimiter='\t')
total5.columns = ['totalamount_range', 'Total Number of Trips']
total5['totalamount_range'] = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-27', '70-80', '80-infinite') 
total6 = pd.read_csv('./totalamount_weekday/totalamount_sun', header = None, delimiter='\t')
total6.columns = ['totalamount_range', 'Total Number of Trips']
total6['totalamount_range'] = ('0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-27', '70-80', '80-infinite')

#### For each day of week, a bar-plot will be plotted using the barplot function in seaborn package.
#### Monday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="totalamount_range", y="Total Number of Trips", data=total0, palette=sns.diverging_palette(255, 133, l=60, n=9, center='dark'))
plot.set_xlabel('Range of Total Trip Amount (in USD)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Total Amount - Monday', fontsize = 15)
plt.savefig('./totalamount_weekday/total_mon.png', dpi=300, bbox_inches='tight')

#### Tuesday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="totalamount_range", y="Total Number of Trips", data=total1, palette=sns.cubehelix_palette(9, start=10, rot=0, dark=0.25, light=.95, reverse=True))
plot.set_xlabel('Range of Total Trip Amount (in USD)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Total Amount - Tuesday', fontsize = 15)
plt.savefig('./totalamount_weekday/total_tue.png', dpi=300, bbox_inches='tight')

#### Wednesdaay
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="totalamount_range", y="Total Number of Trips", data=total2, palette=sns.cubehelix_palette(9, start=0, rot=0, dark=.2, light=.95, reverse=True))
plot.set_xlabel('Range of Total Trip Amount (in USD)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Total Amount - Wednseday', fontsize = 15)
plt.savefig('./totalamount_weekday/total_wed.png', dpi=300, bbox_inches='tight')

#### Thursday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="totalamount_range", y="Total Number of Trips", data=total3, palette=sns.cubehelix_palette(9, start=2, rot=0, dark=0.25, light=.95, reverse=True))
plot.set_xlabel('Range of Total Trip Amount (in USD)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Total Amount - Thursday', fontsize = 15)
plt.savefig('./totalamount_weekday/total_thurs.png', dpi=300, bbox_inches='tight')

#### Friday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="totalamount_range", y="Total Number of Trips", data=total4)
plot.set_xlabel('Range of Total Trip Amount (in USD)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Total Amount - Friday', fontsize = 15)
plt.savefig('./totalamount_weekday/total_fri.png', dpi=300, bbox_inches='tight')

#### Saturday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="totalamount_range", y="Total Number of Trips", data=total5, palette=sns.cubehelix_palette(9, reverse=True))
plot.set_xlabel('Range of Total Trip Amount (in USD)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '2,000', '4,000', '6,000', '8,000','10,000'])
plt.title('Distribution of Taxi Trips by Total Amount - Saturday', fontsize = 15)
plt.savefig('./totalamount_weekday/total_sat.png', dpi=300, bbox_inches='tight')

#### Sunday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="totalamount_range", y="Total Number of Trips", data=total6, palette=sns.diverging_palette(255, 133, l=60, n=9, center='dark'))
plot.set_xlabel('Range of Total Trip Amount (in USD)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Total Amount - Sunday', fontsize = 15)
plt.savefig('./totalamount_weekday/total_sun.png', dpi=300, bbox_inches='tight')