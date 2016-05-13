import math
import pandas as pd
import numpy as np
import gmplot

'''
Remember to change the path if needed in main function
This part takes the MapReduce work of drop_off location distribution by weekend and weekday as input.
The output is a two heat map indicating the distribution of the destination of taxi trip by weekend or by weekday.
'''

def data_prepration(data, method = 'origin'):

    # set column's name
    data.columns = ['key', 'counts']
    
    # set columns of area and weekday indicating whether the date is within weekday or weekend
    data['area'] = data['key'].map(lambda x: int(x.split(',')[0]))
    data['weekday'] = data['key'].map(lambda x: int(x.split(',')[1]))

    # split the data into two dataframe
    data_weekday = data[data['weekday'] == 0]
    data_weekend = data[data['weekday'] == 1]

    # rescale on the frequency count 
    if method == 'origin':
        pass
    elif method == 'divide':
        data_weekday['counts'] = data_weekday['counts'].map(lambda x: x/10)
        data_weekend['counts'] = data_weekend['counts'].map(lambda x: x/10)
    elif method == 'log':
        data_weekday['counts'] = data_weekday['counts'].map(lambda x: math.log(x,2))
        data_weekend['counts'] = data_weekend['counts'].map(lambda x: math.log(x,2))

    # round the counts 
    data_weekday['counts'] = data_weekday['counts'].map(lambda x: round(x))
    data_weekend['counts'] = data_weekend['counts'].map(lambda x: round(x))

    # calculate the longitude and latitude from the grid index 
    y_list = np.arange(40.9, 40.7-0.001, -0.001)
    y_center = []
    for i in range(len(y_list)-1):
        y_center.append(np.mean([y_list[i], y_list[i+1]]))
    x_list = np.arange(-74.02, -73.82, 0.001)
    x_center = []
    for i in range(len(x_list)-1):
        x_center.append(np.mean([x_list[i], x_list[i+1]]))
    for i in range(200):
        x_center[i] = round(x_center[i],5)
    for i in range(200):
        y_center[i] = round(y_center[i],5)
    location_dict = {}
    i = 1
    for y in y_center:
        for x in x_center:
            location_dict[i] = [x,y]
            i = i+1
    
    # add the longitude and latitude of the location into dataframe
    data_weekday['longitude'] = data_weekday['area'].map(lambda x: location_dict[x][0])
    data_weekday['latitude'] = data_weekday['area'].map(lambda x: location_dict[x][1])

    data_weekend['longitude'] = data_weekend['area'].map(lambda x: location_dict[x][0])
    data_weekend['latitude'] = data_weekend['area'].map(lambda x: location_dict[x][1])

    # reindex the dataframe
    data_weekday.index = range(data_weekday.shape[0])
    data_weekend.index = range(data_weekend.shape[0])

    # get the longitude list for weekday data
    longitude_list_weekday = []
    for i in range(data_weekday.shape[0]):
        if int(data_weekday['counts'][i]) <= 0:
            pass
        else:
            for j in range(int(data_weekday['counts'][i])):
                longitude_list_weekday.append(data_weekday['longitude'][i])

    # get the longitude list for weekend data
    longitude_list_weekend = []
    for i in range(data_weekend.shape[0]):
        if int(data_weekend['counts'][i]) <= 0:
            pass
        else:
            for j in range(int(data_weekend['counts'][i])):
                longitude_list_weekend.append(data_weekend['longitude'][i])

    # get the latitude list for weekday data
    latitude_list_weekday = []
    for i in range(data_weekday.shape[0]):
        if int(data_weekday['counts'][i]) <= 0:
            pass
        else:
            for j in range(int(data_weekday['counts'][i])):
                latitude_list_weekday.append(data_weekday['latitude'][i])
    # get the latitude list for weekend data
    latitude_list_weekend = []
    for i in range(data_weekend.shape[0]):
        if int(data_weekend['counts'][i]) <= 0:
            pass
        else:
            for j in range(int(data_weekend['counts'][i])):
                latitude_list_weekend.append(data_weekend['latitude'][i])

    return longitude_list_weekend, latitude_list_weekend, longitude_list_weekday, latitude_list_weekday

def gmplot_heatmap(latitude, longitude, label = 'weekday'):

    gmap = gmplot.GoogleMapPlotter(40.75, -73.9655, 13)
    gmap.heatmap(latitude, longitude)
    gmap.draw("./mymap_drop_off_%s.html" %label)


def main():
    path = './drop_off_area/drop_off/part-00000' #change the path here if needed
    data = pd.read_table(path, header = None)

    longitude_list_weekend, latitude_list_weekend, longitude_list_weekday, latitude_list_weekday = data_prepration(data, method = 'devide')

    print longitude_list_weekend
    # plot the heat map for weekend
    gmplot_heatmap(latitude_list_weekend, longitude_list_weekend)

    # plot the heat map for weekday
    gmplot_heatmap(latitude_list_weekday, longitude_list_weekday)

if __name__ == '__main__':
    main()




