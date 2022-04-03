import os
import sys
from pathlib import Path
import os.path

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

#os.chdir(main_dir)
#location = read_excel('location.xlsx')
#wind_only = read_excel('wind_only.xlsx')
#
#print(wind_only.head())
#wind_only.columns = ['serials', 'longitude', 'latitude', 'wind']
#location.columns = ['serials', 'longitude', 'latitude']
#print(wind_only.columns)
#print(wind_only['wind'].unique())
#
#serial_list = wind_only['serials'].tolist()
#
#wind_v = [x for x in serial_list if 'V' in x]
#wind_o = [x for x in serial_list if 'O' in x]
#
#print(len(wind_v), len(wind_o), len(serial_list))
#
#
#print(location.head())
#print(location.shape)
#
#
#serial_data = [str(x) for x in os.listdir(serials_dir) if ('O' in x) | ('V' in x)]
#serial_info = location['serials'].tolist()
#serial_info = sorted(serial_info)
#serial_data = sorted(serial_data)
#
#location_v = [x for x in serial_info if 'V' in x]
#location_o = [x for x in serial_info if 'O' in x]
#
#print('group V in additional location data : ', len(location_v))
#print('group O in additional location data : ', len(location_o))
#
#
## list of items both in serial_data and serial_info
#available_serial = []
#serial_no_location = []
#for item in serial_data :
#    check = 0
#    for item2 in serial_info :
#        if item == item2 :
#            check = 1
#    if check == 1 :
#        available_serial.append(item)
#    else :
#        serial_no_location.append(item)
#
#
## list of items only in serial_info 
## stations that have location, but no data
#
#serial_no_data = []
#for item in serial_info :
#    check = 0
#    for item2 in serial_data :
#        if item == item2 :
#            check = 1
#
#    if check == 0 :
#        serial_no_data.append(item)
#
#
## print length of each lists
#print('available_serial', len(available_serial))
#print('serial_no_location', len(serial_no_location))
#print('serial_no_data', len(serial_no_data))
#


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
#
#os.chdir(main_dir)
#location = read_excel('location.xlsx')
#

# ---------------------------------------------
# plot info !
# figsize | color

figsize_set = tuple([9, 9])
mark_color = 'red'
mark_size = 15

# ---------------------------------------------


# ---------------------------------------------
# location ! 

#location = location
title = 'V02Q1 with wind info\n12 stations'
title = 'OC3CL with wind info\n20 stations(27 not available)'
title = 'All stations with wind info\n32 stations(27 not available)'
title = 'Samples\n30 stations'
title = 'Only group_O'
title = '32 samples (latest)'
save_name = 'group_o_all'

# ----------------------------------------------



# clusetering




# ----------------------------------------------
#os.chdir(main_dir)
#wind_only = read_excel('wind_only.xlsx')
#
#wind_only.columns = ['serial', '경도', '위도', 'wind']
#
##wind_v = [x for x in wind_only['serial'] if 'V' in x]
##wind_o = [x for x in wind_only['serial'] if 'O' in x]
#
##wind_v = wind_only['V' in wind_only['serial']]
##wind_o = wind_only['O' in wind_only['serial']]
#
#wind_v_index = []
#wind_o_index = []
#
#for index in range(wind_only.shape[0]) :
#    if 'V' in wind_only.loc[index, 'serial'] :
#        wind_v_index.append(index)
#    else :
#        wind_o_index.append(index)
#
#wind_v = wind_only.loc[wind_v_index, :]
#wind_o = wind_only.loc[wind_o_index, :]
#
#
#print(wind_v.shape, wind_o.shape, wind_only.shape)
#
## ---------------------------------------------
#
## basic set for location (to gpd)
#
#os.chdir(plot_dir)
#samples = read_excel('samples_made_by_kmeans.xlsx')
#
#print(location.columns)
#
#location['geometry'] = location.apply(lambda row : Point([row['경도'], row['위도']]), axis = 1)
#location = gpd.GeoDataFrame(location, geometry = 'geometry')
#location.crs = {'init' : 'epsg:4326'}
#location = location.to_crs({'init' : 'epsg:5179'})
#
##drop_index = []
##for index in range(location.shape[0]) :
##    if location.loc[index, '시리얼번호'] not in samples.loc[0, :].tolist() :
##        drop_index.append(index)
##
##print(len(drop_index), location.shape[0])
#
#drop_index_o = []
#for index in range(location.shape[0]) :
#    if 'V' in location.loc[index, '시리얼번호'] :
#        drop_index_o.append(index)
#
#drop_index_v = []
#for index in range(location.shape[0]) :
#    if 'O' in location.loc[index, '시리얼번호'] :
#        drop_index_v.append(index)
#
#location_v = location.drop(drop_index_v)
#location_v.reset_index(drop = True, inplace = True)
#
#location_o = location.drop(drop_index_o)
#location_o.reset_index(drop = True, inplace = True)
#
#location = location_o
#
os.chdir(os.path.join(main_dir, 'samples_wind', 'info'))
info_32 = read_excel('samples_32.xlsx').loc[:, ['경도', '위도']]
location = info_32

location['geometry'] = location.apply(lambda row : Point([row['경도'], row['위도']]), axis = 1)
location = gpd.GeoDataFrame(location, geometry = 'geometry')
location.crs = {'init' : 'epsg:4326'}
location = location.to_crs({'init' : 'epsg:5179'})


fig = plt.figure(figsize = figsize_set)
ax = fig.add_subplot(1, 1, 1)

seoul_emd.boundary.plot(ax = ax, color = 'black', linewidth = 0.3)
location.plot(ax = ax, color = mark_color, markersize = mark_size)
plt.title(title)


#print(location_v.shape[0])
#print(location_o.shape[0])
a = input('save and send to discord.bot? (y/n)')

save_name = 'sample_32'

if a == 'y' :
    os.chdir(plot_dir)
    dlt.savefig(plot_dir, f'{save_name}.png', 400)
    plt.savefig(f'{save_name}.png', dpi = 400, pad_inches = 0, bbox_inches = 'tight')



#all_location = gpd.read_excel(T

