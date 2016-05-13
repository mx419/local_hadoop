import pandas as pd
import numpy as np
import pickle
import gmplot

'''
This part takes the uber data of Jan-June, year 2015 as input.
The output is a two heat map indicating the distribution of the pick-up location of Uber.
'''

def data_preparation(data, uber_dict, method = 'origin'):

    # select the data with location ID <= 263
    data_263 = data[data['locationID'] <= 263]
    data_263['counts'] = data_263.groupby('locationID').count()['Pickup_date']

    data = pd.DataFrame({'index': range(1,264)})
    # get frequency count for each location
    data['counts'] = data_263.groupby('locationID').count()['Pickup_date']
    # fill missing value with 0
    data = data.fillna(0)

    # get latitude and longitude for the location ID
    data['latitude'] = data['index'].map(lambda x: uber_dict[str(x)][0])
    data['longitude'] = data['index'].map(lambda x: uber_dict[str(x)][1])

    # rescale on the frequency count 
    if method == 'origin':
        pass
    elif method == 'divide':
        data['counts'] = data['counts'].map(lambda x: x/10)
    elif method == 'log':
        data['counts'] = data['counts'].map(lambda x: math.log(x,2))

    # round the counts 
    data['counts'] = data['counts'].map(lambda x: round(x))

    # get the longitude list and the latitude list 
    latitude_list = []
    for i in range(data.shape[0]):
        if int(data['counts'][i]) <= 0:
            pass
        else:
            for j in range(int(data['counts'][i])):
                latitude_list.append(data['latitude'][i])

    longitude_list = []
    for i in range(data.shape[0]):
        if int(data['counts'][i]) <= 0:
            pass
        else:
            for j in range(int(data['counts'][i])):
                longitude_list.append(data['longitude'][i])

    return latitude_list, longitude_list

    def gmplot_heatmap(latitude, longitude, label = 'uber'):

        # gmplot heat map
        gmap = gmplot.GoogleMapPlotter(40.75, -73.9655, 13)
        gmap.heatmap(latitude, longitude)
        gmap.draw("./mymap_drop_off_%s.html" %label)

def main():
#change the path here if needed
    path = './uber-trip-data/uber-raw-data-janjune-15.csv'
    data = pd.read_csv(path)
    path_dict = './id_location_uber.p'
    uber_dict = pickle.load(open(path_dict, 'rw'))

    latitude_list, longitude_list = data_preparation(data, uber_dict, method = 'devide')

    gmplot_heatmap(latitude_list, longitude_list, label = 'uberdsdsd')

if __name__ == '__main__':
    main()

