#### Import packages

import pandas as pd
import numpy as np
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#### Visualization of the distributions of tip amounts on different days of week;

#### Reads input files from directory named 'tip_weekday', and output plots will be saved under the same directory;

#### Input files should be of the names 'tip_mon', 'tip_tue', 'tip_wed', 'tip_thurs', 
####'tip_fri', 'tip_sat', 'tip_sun';

#### The file should have two columns: first column is the interval of total amount, 
#### and the second column is number of trips in the corresponding interval. These two columns should be separated by '\t'.

tip0 = pd.read_csv('./tip_weekday/tip_mon', header = None, delimiter='\t')
tip0.columns = ['tip_range', 'Total Number of Trips']
tip0['tip_range'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-infinite')
tip1 = pd.read_csv('./tip_weekday/tip_tue', header = None, delimiter='\t')
tip1.columns = ['tip_range', 'Total Number of Trips']
tip1['tip_range'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-infinite') 
tip2 = pd.read_csv('./tip_weekday/tip_wed', header = None, delimiter='\t')
tip2.columns = ['tip_range', 'Total Number of Trips']
tip2['tip_range'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-infinite') 
tip3 = pd.read_csv('./tip_weekday/tip_thurs', header = None, delimiter='\t')
tip3.columns = ['tip_range', 'Total Number of Trips']
tip3['tip_range'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-infinite') 
tip4 = pd.read_csv('./tip_weekday/tip_fri', header = None, delimiter='\t')
tip4.columns = ['tip_range', 'Total Number of Trips']
tip4['tip_range'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-infinite') 
tip5 = pd.read_csv('./tip_weekday/tip_sat', header = None, delimiter='\t')
tip5.columns = ['tip_range', 'Total Number of Trips']
tip5['tip_range'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-infinite') 
tip6 = pd.read_csv('./tip_weekday/tip_sun', header = None, delimiter='\t')
tip6.columns = ['tip_range', 'Total Number of Trips']
tip6['tip_range'] = ('0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-infinite')

#### For each day of week, a bar-plot will be plotted using the barplot function in seaborn package.
#### Monday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="tip_range", y="Total Number of Trips", data=tip0, palette=sns.diverging_palette(255, 133, l=60, n=9, center='dark'))
plot.set_xlabel('Range of Tip Amount (in dollar)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Tip - Monday', fontsize = 15)
plt.savefig('./tip_weekday/tip_mon.png', dpi=300, bbox_inches='tight')

#### Tuesday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="tip_range", y="Total Number of Trips", data=tip1, palette=sns.cubehelix_palette(9, start=10, rot=0, dark=0.25, light=.95, reverse=True))
plot.set_xlabel('Range of Tip Amount (in dollar)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Tip - Tuesday', fontsize = 15)
plt.savefig('./tip_weekday/tip_tue.png', dpi=300, bbox_inches='tight')

#### Wednesdaay
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="tip_range", y="Total Number of Trips", data=tip2, palette=sns.cubehelix_palette(9, start=0, rot=0, dark=.2, light=.95, reverse=True))
plot.set_xlabel('Range of Tip Amount (in dollar)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Tip - Wednesday', fontsize = 15)
plt.savefig('./tip_weekday/tip_wed.png', dpi=300, bbox_inches='tight')

#### Thursday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="tip_range", y="Total Number of Trips", data=tip3, palette=sns.cubehelix_palette(9, start=2, rot=0, dark=0.25, light=.95, reverse=True))
plot.set_xlabel('Range of Tip Amount (in dollar)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Tip - Thursday', fontsize = 15)
plt.savefig('./tip_weekday/tip_thurs.png', dpi=300, bbox_inches='tight')

#### Friday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="tip_range", y="Total Number of Trips", data=tip4)
plot.set_xlabel('Range of Tip Amount (in dollar)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Tip - Fridayday', fontsize = 15)
plt.savefig('./tip_weekday/tip_fri.png', dpi=300, bbox_inches='tight')

#### Saturday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="tip_range", y="Total Number of Trips", data=tip5, palette=sns.cubehelix_palette(9, reverse=True))
plot.set_xlabel('Range of Tip Amount (in dollar)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Tip - Saturday', fontsize = 15)
plt.savefig('./tip_weekday/tip_sat.png', dpi=300, bbox_inches='tight')

#### Sunday
sns.set(context='notebook', style='darkgrid', font='sans-serif', font_scale=1, color_codes=False, rc=None)
plot = sns.barplot(x="tip_range", y="Total Number of Trips", data=tip6, palette=sns.diverging_palette(255, 133, l=60, n=9, center='dark'))
plot.set_xlabel('Range of Tip Amount (in dollar)')
plot.set_ylabel('Total Number of Trips (in thousands)')
plot.set_yticklabels(['0', '1,000', '2,000', '3,000', '4,000','5,000', '6,000', '7,000', '8,000'])
plt.title('Distribution of Taxi Trips by Tip - Saunday', fontsize = 15)
plt.savefig('./tip_weekday/tip_sun.png', dpi=300, bbox_inches='tight')