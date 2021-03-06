import os
import sys
from pathlib import Path
import os.path
from sklearn.cluster import KMeans, k_means

preprocess_dir = Path(os.getcwd())
module_dir = preprocess_dir.parent
main_dir = module_dir.parent
datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')

preprocessed_dir = os.path.join(main_dir, 'preprocessed')
serials_dir = os.path.join(preprocessed_dir, 'serials')

sys.path.append(module_dir)
sys.path.append(self_module)
sys.path.append(preprocess_dir)

import directory_change as dich
import discordlib_pyplot as dlt

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

import geopandas as gpd
from shapely.geometry import Point, Polygon, LineString



shape_file_dir = os.path.join(main_dir, 'shape_file', 'EMD_202101')
plot_dir = os.path.join(main_dir, 'sample_plot')
dich.newfolder(plot_dir)

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
title = f'K - means clustering\nK = {K}'
save_name = 'kmeans_30'

# ----------------------------------------------



# clusetering

def cluster_new(data, K) :
    kmeans = KMeans(n_clusters = K, random_state = 0).fit(data)
    info_clu = pd.DataFrame(columns = ['index', 'label', 'center'])
    
    for i in range(profile.shape[0]) :   
        info_clu.loc[i, 'excel'] = profile.loc[i, 'excel']
        info_clu.loc[i, 'label'] = kmeans.labels_[i]
        info_clu.loc[i, 'center'] = kmeans.cluster_centers_[kmeans.labels_[i]]
    
    only_centers = pd.DataFrame(columns = ['cat', 'label', 'count', 'center'])

    for i in range(K) :
        only_centers.loc[i, 'cat'] = name_find(profile.loc[0, 'excel'])
        only_centers.loc[i, 'label'] = i
        only_centers.loc[i, 'center'] = kmeans.cluster_centers_[i]
        
    only_centers.reset_index(drop = True, inplace = True)

    for i in range(only_centers.shape[0]) :
        only_centers.loc[i, 'count'] = info_clu.loc[:, 'label'].tolist().count(i)
    info_clu = info_clu.sort_values(by = 'label')
    return info_clu, only_centers

# DBSCAN, k-means

print(location.columns)

#info_clu, only_centers = cluster_new(location.loc[:, '??????' : '??????'], 10)

drop_index = []
for index in range(location.shape[0]) :
    for col in ['??????', '??????'] :
        if str(location.loc[index, col]) == 'nan':
            drop_index.append(index)
            print(location.loc[index, col])

location.drop(drop_index, inplace = True)
location.reset_index(drop = True, inplace = True)

data = location.loc[ :, '??????' :'??????']

drop_index = []
for index in range(data.shape[0]) :
    for col in data.columns :
        if str(data.loc[index, col]) == 'nan':
            drop_index.append(index)
            print(data.loc[index, col])

data.drop(drop_index, inplace = True)
data.reset_index(drop = True, inplace = True)


print('\n' * 10)
print('############################')
print(location.shape[0], data.shape[0])
print('############################')
print('\n' * 10)
    
print(data.head())
kmeans = KMeans(n_clusters = K, random_state = 0).fit(data)

data.reset_index(drop = True, inplace = True)
data2 = data.copy()
data2.loc[:, 'label'] = kmeans.labels_

print(len(kmeans.labels_), data.shape[0], len(kmeans.cluster_centers_))
#print(kmeans.labels_)
#print(kmeans.cluster_centers_)

def distance(point1, point2) :

    dt = pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2)
    return np.sqrt(dt)


df_sample = pd.DataFrame(columns = list(range(K)))
for k in range(K) :
    if k != -1 :
        cluster_now_index = None
        cluster_now_index = []
        for index in range(location.shape[0]) :
            if kmeans.labels_[index] == k :
                cluster_now_index.append(index)


        print(location.shape[0], max(cluster_now_index))
        cluster_now = location.loc[cluster_now_index, :].copy()
        cluster_now.reset_index(drop = True, inplace = True)

        # find nearest

        center = kmeans.cluster_centers_[k].tolist()

        short_index = -1
        for num, index in enumerate(range(cluster_now.shape[0])) :
            dt = distance(cluster_now.loc[index, '??????' : '??????'].tolist(), center)

            if num == 0 :
                shortest = dt
                short_index = index

            else :
                if float(dt) < float(shortest) :
                    shortest = dt
                    short_index = index
        print(k)
        df_sample.loc[0, k] = cluster_now.loc[short_index, '???????????????']




    






# elbow method

from yellowbrick.cluster import KElbowVisualizer


model = KMeans()
visualizer = KElbowVisualizer(model, k=(15, 45))
visualizer.fit(data)
visualizer.show()
os.chdir(plot_dir)

plt.savefig('elbow.png', dpi = 400, pad_inches = 0, bbox_inches = 'tight')





# ----------------------------------------------
os.chdir(main_dir)
wind_only = read_excel('wind_only.xlsx')

wind_only.columns = ['serial', '??????', '??????', 'wind']

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

import shapely.ops
import shapely.wkt
from shapely.geometry import Point, Polygon




fig = plt.figure(figsize = figsize_set)
ax = fig.add_subplot(1, 1, 1)

#seoul_emd.boundary.plot(ax = ax, color = 'black', linewidth = 0.3)
#location.plot(ax = ax, color = mark_color, markersize = mark_size)
plt.title(title)

data.reset_index(drop = True, inplace = True)

data['geometry'] = data.apply(lambda row : Point([row['??????'], row['??????']]), axis = 1)
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



for k in range(K) :
    cluster_now_index = None
    cluster_now_index = []
    for index in range(data.shape[0]) :
        if kmeans.labels_[index] == k :
            cluster_now_index.append(index)

    print(data.shape[0], max(cluster_now_index))
    cluster_now = data.loc[cluster_now_index, :].copy()
    cluster_now.reset_index(drop = True, inplace = True)
    
    coords = []
    for index in range(cluster_now.shape[0]) :
        coords.append(cluster_now.loc[index, 'geometry'])

    gdf = create_polygon(coords, f'{k}')

#gdf.plot(ax = ax)
        


# plot

for k in range(K) :
    cluster_now_index = None
    cluster_now_index = []
    for index in range(data.shape[0]) :
        if kmeans.labels_[index] == k :
            cluster_now_index.append(index)

    print(data.shape[0], max(cluster_now_index))
    cluster_now = data.loc[cluster_now_index, :].copy()
    cluster_now.reset_index(drop = True, inplace = True)

#    cluster_now.plot(ax = ax, markersize = 9)

print(df_sample)
os.chdir(plot_dir)
df_sample.to_excel('samples_made_by_kmeans.xlsx')
a = input('save and send to discord.bot? (y/n)')

if a == 'y' :
    os.chdir(plot_dir)
    dlt.savefig(plot_dir, f'{save_name}.png', 400)
    plt.savefig(f'{save_name}.png', dpi = 400, pad_inches = 0, bbox_inches = 'tight')



#all_location = gpd.read_excel(T

