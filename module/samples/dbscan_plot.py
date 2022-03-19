import os
import sys
from pathlib import Path
import os.path

from sklearn.cluster import KMeans, k_means, DBSCAN
import geopandas as gpd
from shapely.geometry import Point, Polygon, LineString
from sklearn.neighbors import NearestNeighbors

import shapely.ops
import shapely.wkt
from shapely.geometry import Point, Polygon

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "/mnt/c/Users/joo09/Documents/Github/fonts/D2Coding.ttf"
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

import glob
import math
import random
import scipy.stats
import shutil
import time

preprocess_dir = Path(os.getcwd())
module_dir = preprocess_dir.parent
main_dir = module_dir.parent

preprocessed_dir = os.path.join(main_dir, 'preprocessed')
serials_dir = os.path.join(preprocessed_dir, 'serials')



'''
note
'''
cwdir = os.getcwd()

def read_excel(excel) :
    df = pd.read_excel(excel)
    if 'Unnamed: 0' in df.columns :
        df.drop('Unnamed: 0', axis = 1, inplace = True)

    if 'Unnamed: 0.1' in df.columns :
        df.drop('Unnamed: 0.1', axis = 1, inplace = True)

    return df


def read_csv(excel) :
    #df = pd.read_csv(excel, encoding = "utf-16")
    #df = pd.read_csv(excel, encoding = "ISO-8859-1")
    df = pd.read_csv(excel, encoding = "cp949")
    
    return df

def ave(list1) :
	return sum(list1) / len(list1)

# -----------------------------------------------
# wind available stations for group_V, group_O
# -----------------------------------------------

os.chdir(main_dir)
location = read_excel('location.xlsx')
wind_only = read_excel('wind_only.xlsx')

print(wind_only.head())
wind_only.columns = ['serials', 'longitude', 'latitude', 'wind']
location.columns = ['serials', 'longitude', 'latitude']
print(wind_only.columns)
print(wind_only['wind'].unique())

serial_list = wind_only['serials'].tolist()

wind_v = [x for x in serial_list if 'V' in x]
wind_o = [x for x in serial_list if 'O' in x]

print(len(wind_v), len(wind_o), len(serial_list))


print(location.head())
print(location.shape)


serial_data = [str(x) for x in os.listdir(serials_dir) if ('O' in x) | ('V' in x)]
serial_info = location['serials'].tolist()
serial_info = sorted(serial_info)
serial_data = sorted(serial_data)

location_v = [x for x in serial_info if 'V' in x]
location_o = [x for x in serial_info if 'O' in x]

print('group V in additional location data : ', len(location_v))
print('group O in additional location data : ', len(location_o))


# list of items both in serial_data and serial_info
available_serial = []
serial_no_location = []
for item in serial_data :
    check = 0
    for item2 in serial_info :
        if item == item2 :
            check = 1
    if check == 1 :
        available_serial.append(item)
    else :
        serial_no_location.append(item)


# list of items only in serial_info 
# stations that have location, but no data

serial_no_data = []
for item in serial_info :
    check = 0
    for item2 in serial_data :
        if item == item2 :
            check = 1

    if check == 0 :
        serial_no_data.append(item)


# print length of each lists
print('available_serial', len(available_serial))
print('serial_no_location', len(serial_no_location))
print('serial_no_data', len(serial_no_data))



# check if any of the stations without location info
# have available wind information

## saved in 'main_dir', 'station_with_data_no_location_availablewind.xlsx'




# -----------------------------------------------
# Google map plot (API)
# -----------------------------------------------



shape_file_dir = os.path.join(main_dir, 'shape_file', 'EMD_202101')
plot_dir = os.path.join(main_dir, 'sample_plot')
os.chdir(shape_file_dir)
emd = gpd.read_file('TL_SCCO_EMD.shp')
seoul_emd = emd[emd['EMD_CD'].str.startswith('11')]



os.chdir(main_dir)
location = read_excel('location.xlsx')


# ---------------------------------------------
# plot info !
# figsize | color

figsize_set = tuple([9, 9])
mark_color = 'red'
mark_size = 15

# ---------------------------------------------


# ---------------------------------------------
# location ! 

location = location
title = 'V02Q1 with wind info\n12 stations'
title = 'OC3CL with wind info\n20 stations(27 not available)'
title = 'All stations with wind info\n32 stations(27 not available)'
K = 30
title = f'DBSCAN\neps = 0.08, cluster = 32'
save_name = 'dbscan_32'

# ----------------------------------------------



# clusetering

# data preprocess

data = location.loc[ :, '경도' :'위도']

drop_index = []
for index in range(data.shape[0]) :
    for col in data.columns :
        if str(data.loc[index, col]) == 'nan':
            drop_index.append(index)

data.drop(drop_index, inplace = True)
data.reset_index(drop = True, inplace = True)


# DBSCAN, k-moeans

# find optimal nubmer of eps

minpts = 4

neighbors = NearestNeighbors(n_neighbors = minpts)
neighbors_fit = neighbors.fit(data)
distances, indices = neighbors_fit.kneighbors(data)

distances = np.sort(distances, axis = 0)
distances = distances[:, 1]
plt.plot(distances)
plt.xlabel('stations')
plt.ylabel('nearest distance(eps)')

xticks = []
for num in range(1200) :
    if num % 50 == 0 :
        xticks.append(num)

yticks = []
for num in range(30) :
    if num % 2 == 0 :
        yticks.append(round(num * 0.001, 3))


plt.xlim(920, 1070)
plt.ylim(0.005, 0.01)


#plt.xticks(xticks, xticks, rotation = 90)
#plt.yticks(yticks, yticks)

plt.title('distance from each stations\nto nearest neighbor')
os.chdir(plot_dir)
plt.savefig(f'distances_zoom.png', dpi = 400, pad_inches = 0, bbox_inches = 'tight')

db_model = DBSCAN(eps = 0.008, min_samples = minpts)
predict = pd.DataFrame(db_model.fit_predict(data))
predict.columns = ['predict']

print(predict)
print(predict['predict'].unique())
print(len(predict['predict'].unique()))



data2 = data.copy()
data2.loc[:, 'label'] = predict['predict'].tolist()




# ----------------------------------------------
os.chdir(main_dir)
wind_only = read_excel('wind_only.xlsx')

wind_only.columns = ['serial', '경도', '위도', 'wind']

#wind_v = [x for x in wind_only['serial'] if 'V' in x]
#wind_o = [x for x in wind_only['serial'] if 'O' in x]

#wind_v = wind_only['V' in wind_only['serial']]
#wind_o = wind_only['O' in wind_only['serial']]

wind_v_index = []
wind_o_index = []

for index in range(wind_only.shape[0]) :
    if 'V' in wind_only.loc[index, 'serial'] :
        wind_v_index.append(index)
    else :
        wind_o_index.append(index)

wind_v = wind_only.loc[wind_v_index, :]
wind_o = wind_only.loc[wind_o_index, :]

location = wind_only

print(wind_v.shape, wind_o.shape, wind_only.shape)

# ---------------------------------------------

# basic set for location (to gpd)





fig = plt.figure(figsize = figsize_set)
ax = fig.add_subplot(1, 1, 1)
seoul_emd = emd[emd['EMD_CD'].str.startswith('11')]

seoul_emd.boundary.plot(ax = ax, color = 'black', linewidth = 0.3)
#location.plot(ax = ax, color = mark_color, markersize = mark_size)
plt.title(title)

data.reset_index(drop = True, inplace = True)

data['geometry'] = data.apply(lambda row : Point([row['경도'], row['위도']]), axis = 1)
data = gpd.GeoDataFrame(data, geometry = 'geometry')
data.crs = {'init' : 'epsg:4326'}
data = data.to_crs({'init' : 'epsg:5179'})

# generate polygons

print(data.head())

#gdf = gpd.GeoDataFrame(data, geometry = data['geometry'].apply(shapely.wkt.loads)).dissolve(
#        'label')['geometry'].apply(lambda mp : mp.convex_hull)
#gdf.plot()

def create_polygon(coords, polygon_name) :
    polygon = Polygon(coords)
    gdf = gpd.GeoDataFrame(crs = {'init' : 'epsg:4326'})
    gdf.loc[0, 'name'] = polygon_name
    gdf.loc[0, 'geometry'] = polygon

    return gdf



# plot

data2.reset_index(drop = True, inplace = True)

data2['geometry'] = data2.apply(lambda row : Point([row['경도'], row['위도']]), axis = 1)
data2 = gpd.GeoDataFrame(data2, geometry = 'geometry')
data2.crs = {'init' : 'epsg:4326'}
data2 = data2.to_crs({'init' : 'epsg:5179'})

K = 32
for k in range(K) :
    cluster_now_index = None
    cluster_now_index = []
    for index in range(data2.shape[0]) :
        if data2.loc[index, 'label'] == k :
            cluster_now_index.append(index)

    cluster_now = data2.loc[cluster_now_index, :].copy()
    cluster_now.reset_index(drop = True, inplace = True)

    cluster_now.plot(ax = ax, markersize = 9)

a = input('save and send to discord.bot? (y/n)')

if a == 'y' :
    os.chdir(plot_dir)
#    dlt.savefig(plot_dir, f'{save_name}.png', 400)
    plt.savefig(f'{save_name}.png', dpi = 400, pad_inches = 0, bbox_inches = 'tight')



#all_location = gpd.read_excel(T

