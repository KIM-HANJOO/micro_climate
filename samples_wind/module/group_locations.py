import os
import sys
from pathlib import Path
import os.path
import datetime

#   < directory paths >
samples_module_dir = Path(os.getcwd())
sample_robby = samples_module_dir.parent
sample_data = os.path.join(sample_robby, 'data')
sample_info = os.path.join(sample_robby, 'info')
sample_plot = os.path.join(sample_robby, 'plot')
sample_typo = os.path.join(sample_robby, 'typo')

main_dir = sample_robby.parent
module_dir = os.path.join(main_dir, 'module')

datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
info_dir = os.path.join(main_dir, 'info_data')


#   add dirs to sys.path

sys.path.append(module_dir)
sys.path.append(self_module)


#   import packages

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

basic functions
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

def leap_year(year) :
    check = 0
    if (int(year) % 4 == 0) :
        if int(year) % 100 != 0 :
            if int(year) % 400 == 0 :
                check = 1
                
    if check == 1 :
        return True
    else :
        return False


def double_size(string) :
    if len(string) == 1 :
        return '0' + string
    else :
        return string
    
class NotAvailableError(Exception) :
    def __init__(self) :
        super().__init__('not available!') 


# -----------------------------------------------
# plot independent informations for each stations
# -----------------------------------------------


#   < directory paths >
samples_module_dir = Path(os.getcwd())
sample_robby = samples_module_dir.parent
sample_data = os.path.join(sample_robby, 'data')
sample_info = os.path.join(sample_robby, 'info')
sample_plot = os.path.join(sample_robby, 'plot')
sample_typo = os.path.join(sample_robby, 'typo')
sample_avail = os.path.join(sample_robby, 'rounded')

plot_zoom = os.path.join(sample_robby, 'plot_zoom')


main_dir = sample_robby.parent
module_dir = os.path.join(main_dir, 'module')

datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
info_dir = os.path.join(main_dir, 'info_data')


# -----------------------------------------------
# define function to link dates
# -----------------------------------------------

def date_to_number(regi_date) :
    start_date = datetime.datetime(2020, 1, 1, 00)
    now_date = datetime.datetime(int(regi_date[ : 4]), int(regi_date[4 : 6]), \
            int(regi_date[6 : 8]), int(regi_date[8, 10]))
    pass

def all_date() :
    start_date = datetime.datetime(2020, 4, 1, 00)
    end_date = datetime.datetime(2021, 12, 31, 23)
    temp_date = start_date
    index_num = 0

    date = []
    index = []

    date_dict = dict()
    inverse_dict = dict()

    while temp_date < end_date :
        temp_string = str(temp_date.year) + double_size(str(temp_date.month)) + \
                double_size(str(temp_date.day)) + double_size(str(temp_date.hour))\
                + '00'
        date.append(temp_string)
        index.append(index_num)

        date_dict[temp_string] = index_num
        inverse_dict[index_num] = temp_string
        
        index_num += 1
        temp_date = temp_date + datetime.timedelta(hours = 1)

    return date_dict, inverse_dict, date

def date_to_datetime(string) :
    string = str(string)
    year = int(string[ : 4])
    month = int(string[4 : 6])
    day = int(string[6 : 8])
    hour = int(string[8 : 10])
    minute = int(string[10 : 12])

    if (hour < 0) | (hour > 24) :
        print(string)
        print(hour)


    return datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute)

def datetime_to_date(datetime) :
    year = str(datetime.year)
    month = double_size(str(datetime.month))
    day = double_size(str(datetime.day))
    hour = double_size(str(datetime.hour))
    minute = double_size(str(datetime.minute))

    return year + month + day + hour + minute  


def minute_interval(datetime1, datetime2) :
    datetime1 = date_to_datetime(datetime1)
    datetime2 = date_to_datetime(datetime2)

    return ((datetime2 - datetime1).seconds // 60)


def interval_from_df(data) :
    # index_number : get indexes of data that has the time value (if no time value : append -1)
    # index_values : get values of index_numbered timesteps

    index_check = []
    index_number = []
    index_values = []
    asc = 0

    for index in range(data.shape[0]) :
        if str(data.loc[index, '등록일자']) != 'nan' :
            index_number.append(index)
            index_values.append(data.loc[index, '보정_시간'])
            index_check.append(asc)
            asc += 1

        else :
            index_check.append(-1)


    # interval : list with adjacent - subtracted values of indeX_values

    interval = []

    for num_index, index in enumerate(index_check) :
        if index == -1 :
            interval.append(-1)
        else :
            if index == 0 :
                interval.append(-1)

            else :
                now_index = index_number[index]
                prev_index = index_number[index - 1]

                interval.append(minute_interval(index_values[prev_index], index_values[now_index]))

    return interval


#    for num_index, index in enumerate(range(len(index_values))) :
#        if num_index > 0 :
#            if index == -1 :
#                interval.append(-1)
#
#            else :
#                interval.append(minute_interval(index_values[num_index - 1], index_values[num_index]))
#
#
#    return interval




def check_avail(string) :
    string = str(string)

    if len(string) != 12 :
        return False

    else :
        if ':' in string :
            return False

        if ' ' in string :
            return False

        if '.' in string :
            return False

        if '/' in string :
            return False

    return True

# -----------------------------------------------
# make date list and date_dict, inverse_dict
# -----------------------------------------------

# date from 2020.04.01 to 2021.12.31
date_dict, inverse_dict, real_date_list = all_date()


def round_hour(dt) :
    # convert string (202004010100) to datetime format
    dt = date_to_datetime(dt)

    # split datetime
    year = dt.year
    month = dt.month
    day = dt.day

    hour = dt.hour
    minute = dt.minute


    # ruturn rounded datetime
    if dt.minute < 30 :
        return datetime.datetime(year = year, month = month, day = day, hour = hour)

    else :
        return datetime.datetime(year = year, month = month, day = day, hour = hour + 1)

# -----------------------------------------------
# make date list and date_dict, inverse_dict
# -----------------------------------------------




import geopandas as gpd
from shapely.geometry import Point, Polygon, LineString

def plot_location(location1, location2, plot_dir) :
    os.chdir(os.path.join(main_dir, 'shape_file', 'EMD_202101'))
    emd = gpd.read_file('TL_SCCO_EMD.shx')

    location1.columns = ['경도', '위도', 'group']
    location2.columns = ['경도', '위도', 'group']

    g_col_1 = 'pink'
    g_col_2 = 'green'
    g_col_3 = 'red'
    g_col_4 = 'blue'

    seoul_emd = emd[emd['EMD_CD'].str.startswith('11')]

    location1['geometry'] = location1.apply(lambda row : Point([row['경도'], row['위도']]), axis = 1)
    location1 = gpd.GeoDataFrame(location1, geometry = 'geometry')
    location1.crs = {'init' : 'epsg:4326'}
    location1 = location1.to_crs({'init' : 'epsg:5179'})
            
    
    location2['geometry'] = location2.apply(lambda row : Point([row['경도'], row['위도']]), axis = 1)
    location2 = gpd.GeoDataFrame(location2, geometry = 'geometry')
    location2.crs = {'init' : 'epsg:4326'}
    location2 = location2.to_crs({'init' : 'epsg:5179'})

    save_name = 'plot_group'
    figsize_set = (9, 9)
    title = 'samples, 32, groups'
    mark_size = 15

    fig = plt.figure(figsize = figsize_set)
    ax = fig.add_subplot(1, 1, 1)


    for index in range(location2.shape[0]) :
        location2.loc[index, '위도'] += 2

    seoul_emd.boundary.plot(ax = ax, color = 'black', linewidth = 0.3)
    # location1
    g1_1 = location2[location2['group'] == 1].loc[:, ['경도', '위도']]
    g1_2 = location2[location2['group'] == 2].loc[:, ['경도', '위도']]
    g1_3 = location2[location2['group'] == 3].loc[:, ['경도', '위도']]
    g1_4 = location2[location2['group'] == 4].loc[:, ['경도', '위도']]


    
    g1_1.plot(ax = ax, color = g_col_1, markersize = mark_size)
    g1_2.plot(ax = ax, color = g_col_2, markersize = mark_size)
    g1_3.plot(ax = ax, color = g_col_3, markersize = mark_size)
    g1_4.plot(ax = ax, color = g_col_4, markersize = mark_size)
    
    # location2
    g2_1 = location2[location2['group'] == 1].loc[:, ['경도', '위도']]
    g2_2 = location2[location2['group'] == 2].loc[:, ['경도', '위도']]
    g2_3 = location2[location2['group'] == 3].loc[:, ['경도', '위도']]
    g2_4 = location2[location2['group'] == 4].loc[:, ['경도', '위도']]
    
    g2_1.plot(ax = ax, color = g_col_1, markersize = mark_size)
    g2_2.plot(ax = ax, color = g_col_2, markersize = mark_size)
    g2_3.plot(ax = ax, color = g_col_3, markersize = mark_size)
    g2_4.plot(ax = ax, color = g_col_4, markersize = mark_size)

    plt.title(title)


    a = input('save and send to discord.bot? (y/n)')

    if a == 'y' :
        os.chdir(plot_dir)
        dlt.savefig(plot_dir, f'{save_name}.png', 400)
        plt.savefig(f'{save_name}.png', dpi = 400, pad_inches = 0, bbox_inches = 'tight')

os.chdir(samples_module_dir)
print(os.listdir(samples_module_dir))
#emd = gpd.read_file('TL_SCCO_EMD.shx')
os.chdir(sample_info)
info_32 = read_excel('samples_32.xlsx')
info_32 = info_32.loc[:, ['경도', '위도']]

os.chdir(plot_zoom)
info_1 = read_excel('info1.xlsx')
info_2 = read_excel('info2.xlsx')

print(info_1.index)
list_1 = info_1.loc[24, :].tolist()
list_2 = info_2.loc[24, :].tolist()

nlist_1 = []
for item in list_1 :
    if item == 'high_fluc' :
        nlist_1.append(1)
    elif item == 'low_fluc' :
        nlist_1.append(2)
    elif item == 'higher_value' :
        nlist_1.append(3)
    elif item == 'lower_value' :
        nlist_1.append(4)


nlist_2 = []
for item in list_2 :
    if item == 'high_fluc' :
        nlist_2.append(1)
    elif item == 'low_fluc' :
        nlist_2.append(2)
    elif item == 'higher_value' :
        nlist_2.append(3)
    elif item == 'lower_value' :
        nlist_2.append(4)

location1 = info_32.copy()
location2 = info_32.copy()

location1['group'] = None
location2['group'] = None

location1.loc[:, 'group'] = nlist_1
location2.loc[:, 'group'] = nlist_2

print(location1)


plot_location(location1, location2, sample_plot)
