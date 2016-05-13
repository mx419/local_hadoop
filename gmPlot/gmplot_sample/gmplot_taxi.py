import pandas as pd
import numpy as np
import gmplot
import math

'''
This part takes the MapReduce work of pick-up location distribution as input.
The output is a heat map indicating the distribution of the pick-up location of taxi trip
'''

def data_parapration(data,  method = 'origin'):

    # set columns name
    data.columns = ['area', 'counts']

    # rescale on the frequency count 
    if method == 'origin':
        pass
    elif method == 'divide':
        data['counts'] = data['counts'].map(lambda x: x/10)
    elif method == 'log':
        data['counts'] = data['counts'].map(lambda x: math.log(x,2))

    # round the counts 
    data['counts'] = data['counts'].map(lambda x: round(x))

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
    data['longitude'] = data['area'].map(lambda x: location_dict[x][0])
    data['latitude'] = data['area'].map(lambda x: location_dict[x][1])

    # get the longitude list and the latitude list 
    longitude_list = []
    for i in range(data.shape[0]):
        if int(data['counts'][i]) <= 0:
            pass
        else:
            for j in range(int(data['counts'][i])):
                longitude_list.append(data['longitude'][i])

    latitude_list = []
    for i in range(data.shape[0]):
        if int(data['counts'][i]) <= 0:
            pass
        else:
            for j in range(int(data['counts'][i])):
                latitude_list.append(data['latitude'][i])

    return longitude_list, latitude_list


def gmplot_heatmap(latitude, longitude, label = 'taxi'):

    # gmplot heat map
    gmap = gmplot.GoogleMapPlotter(40.75, -73.9655, 13)
    gmap.heatmap(latitude, longitude)
    gmap.draw("./mymap_drop_off_%s.html" %label)


def main():
    #change path here
    path = './area/area/part-00000'
    data = pd.read_table(path, header = None)

    longitude_list, latitude_list = data_parapration(data,  method = 'divide')

    gmplot_heatmap(longitude_list, latitude_list, label = 'taxi')

if __name__ == '__main__':
    main()

