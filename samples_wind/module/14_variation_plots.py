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
sample_plot = os.path.join(sample_robby, 'plot', 'new_plot')
sample_typo = os.path.join(sample_robby, 'typo')
rounded_dir = os.path.join(sample_robby, 'rounded')

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
sample_plot = os.path.join(sample_robby, 'plot', 'new_plot')
sample_typo = os.path.join(sample_robby, 'typo')
sample_avail = os.path.join(sample_robby, 'rounded')



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
# temp function
# -----------------------------------------------

def get_day(df, day) :

    day_list = []

    for index in range(df.shape[0]) :
        date = str(df.loc[index, '보정_시간'])
        if day in date :
            day_list.append(index)

    target_df = df.loc[day_list, :].copy()
    target_df.reset_index(drop = True, inplace = True)

    drop_index = []
    for index in range(target_df.shape[0]) :
        if target_df.loc[index, 'hour_available'] == 'X' :
            drop_index.append(index)

    target_df.drop(drop_index, inplace = True)
    target_df.reset_index(drop = True, inplace = True)


    target_edt = target_df.shape[0]
    print(target_df)

    # add ommitted time to target_df

    add_target_date = []
    for hour in range(24) :
        hour_str = double_size(str(hour))
        target_asc = day + hour_str + '00'

        hour_check = 0
        for index in range(target_df.shape[0]) :
            if target_asc in str(target_df.loc[index, '보정_시간']) :
                hour_check = 1

        if hour_check == 0 :
            add_target_date.append(target_asc)
    
    print(len(add_target_date))
    for day in add_target_date :
        target_df.loc[target_edt, '보정_시간'] = day
        target_edt += 1

    for index in range(target_df.shape[0]) :
        target_df.loc[index, '보정_시간'] = str(int(target_df.loc[index, '보정_시간']))

    target_df.sort_values(by = ['보정_시간'], inplace = True, ignore_index = True)

    return target_df

# -----------------------------------------------
# Split data
# -----------------------------------------------

a = input('basic boxplot(y/k/n)')

if (a == 'y') | (a == 'k') :
    if a == 'y' :
        stations_temperature_summer = pd.DataFrame(columns = list(range(24)))
        stations_temperature_winter = pd.DataFrame(columns = list(range(24)))
        summer_num = 0
        winter_num = 0

        for num_excel, excel in enumerate(os.listdir(rounded_dir)) :

            summer_date = '20210621'
            winter_date = '20211222'

            summer_start = summer_date + '00'
            winter_start = winter_date + '00'

            if num_excel > -1 :
                # only target date
                os.chdir(rounded_dir)
                temp = read_excel(excel)
                summer_day = get_day(temp, summer_date)
                winter_day = get_day(temp, winter_date)

                print(summer_day.shape[0])
                print(winter_day.shape[0])
                
                # make summer dataframe
                for num_index, index in enumerate(range(summer_day.shape[0])) :
                    stations_temperature_summer.loc[summer_num, index] = summer_day.loc[index, '기온']
                summer_num += 1


                # make winter dataframe
                for index in range(winter_day.shape[0]) :
                    stations_temperature_winter.loc[winter_num, index] = winter_day.loc[index, '기온']
                    winter_num += 1



        print(stations_temperature_summer)
        os.chdir(sample_plot)
        stations_temperature_summer.to_excel('basic_boxplot_summer_df.xlsx')

        print(stations_temperature_winter)
        os.chdir(sample_plot)
        stations_temperature_winter.to_excel('basic_boxplot_winter_df.xlsx')

    if a == 'k' :
        os.chdir(sample_plot)
        stations_temperature_summer = read_excel('basic_boxplot_summer_df.xlsx')
        stations_temperature_winter = read_excel('basic_boxplot_winter_df.xlsx')
        


# summer plot
    fig = plt.figure(figsize = (10, 5))

    for num_col, col in enumerate(stations_temperature_summer.columns) :
        temp_list = stations_temperature_summer.loc[:, col].tolist()
        temp_list = [x for x in temp_list if str(x) != 'nan']
        plt.boxplot(temp_list, positions = [num_col + 1])

    plt.xlabel('hour')
    plt.ylabel('temperature')
    plt.title('samples(32) temperature\nsummer(06/21)')
    os.chdir(sample_plot)
    
    plt.savefig('basic_variation_summer.png', dpi = 400)
    dlt.savefig(sample_plot, 'basic_variation_summer.png', 400)




# winter plot
    fig = plt.figure(figsize = (10, 5))

    for num_col, col in enumerate(stations_temperature_winter.columns) :
        temp_list = stations_temperature_winter.loc[:, col].tolist()
        temp_list = [x for x in temp_list if str(x) != 'nan']
        plt.boxplot(temp_list, positions = [num_col + 1])

    plt.xlabel('hour')
    plt.ylabel('temperature')
    plt.title('samples(32) temperature\nwinter(12/22)')
    os.chdir(sample_plot)
    
    plt.savefig('basic_variation_winter.png', dpi = 400)
    dlt.savefig(sample_plot, 'basic_variation_winter.png', 400)


# check average spatial variation
    stations_temperature_winter

