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



#   < new directory paths >
samples_module_dir = Path(os.getcwd())
sample_robby = samples_module_dir.parent
sample_data = os.path.join(sample_robby, 'preprocessed', 'merged')
sample_info = os.path.join(sample_robby, 'preprocessed', 'info')
sample_plot = os.path.join(sample_robby, 'preprocessed', 'plot')
sample_typo = os.path.join(sample_robby, 'preprocessed', 'typo')
sample_time = os.path.join(sample_robby, 'preprocessed', 'time')
sample_only_time = os.path.join(sample_robby, 'preprocessed', 'only_available_time')

main_dir = sample_robby#.parent
module_dir = os.path.join(main_dir, 'module')

datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
info_dir = os.path.join(main_dir, 'info_data')


#   add dirs to sys.path

sys.path.append(module_dir)
sys.path.append(self_module)

#   import self packages

import directory_change as dich
import discordlib_pyplot as dlt


dich.newfolder(sample_data)
dich.newfolder(sample_info)
dich.newfolder(sample_plot)
dich.newfolder(sample_typo)
dich.newfolder(sample_time)
dich.newfolder(sample_only_time)


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

#   < new directory paths >
samples_module_dir = Path(os.getcwd())
sample_robby = samples_module_dir.parent
sample_data = os.path.join(sample_robby, 'preprocessed', 'merged')
sample_info = os.path.join(sample_robby, 'preprocessed', 'info')
sample_plot = os.path.join(sample_robby, 'preprocessed', 'plot')
sample_typo = os.path.join(sample_robby, 'preprocessed', 'typo')
sample_time = os.path.join(sample_robby, 'preprocessed', 'time')
sample_only_time = os.path.join(sample_robby, 'preprocessed', 'only_available_time')
sample_avail = sample_only_time

main_dir = sample_robby#.parent
module_dir = os.path.join(main_dir, 'module')

datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
info_dir = os.path.join(main_dir, 'info_data')


#   add dirs to sys.path

sys.path.append(module_dir)
sys.path.append(self_module)

#   import self packages

import directory_change as dich
import discordlib_pyplot as dlt


dich.newfolder(sample_data)
dich.newfolder(sample_info)
dich.newfolder(sample_plot)
dich.newfolder(sample_typo)
dich.newfolder(sample_time)
dich.newfolder(sample_only_time)

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
            index_values.append(data.loc[index, '등록일자'])
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

# check all stations if there is any wrong formats

a = input('check stations if any have any wrong formats(y/n)')

if a == 'y' :
    for excel_num, excel in enumerate(os.listdir(sample_avail)) :
        os.chdir(sample_avail)
        temp = read_excel(excel)
        for index in range(temp.shape[0]) :
            if not check_avail(temp.loc[index, '등록일자']) :
                print(f"{excel}\t{index}\t{temp.loc[index, '등록일자']}")
        print(f'{excel_num + 1} / {len(os.listdir(sample_avail))}')



a = input('make minutual - timedelta dataframe and plot(y/n)')


if a == 'y' :

    
    real_date_list_num = list(range(len(real_date_list)))
    interval_all = pd.DataFrame(columns = real_date_list_num)
    
    sample_list = []

    for excel_num, excel in enumerate(os.listdir(sample_avail)) :
        if excel_num < 1 :
            os.chdir(sample_avail)
            temp = read_excel(excel)
            
            for index in range(temp.shape[0]) :
                if str(temp.loc[index, '등록일자']) != 'nan' :
                    start_date = temp.loc[index, '등록일자']
                    start_date = round_hour(start_date)
                    break
            
            start_number = -1
            start_date = datetime_to_date(start_date)
            for number, date in enumerate(real_date_list) :
                if str(start_date) == str(date) :
                    start_number = number
                    break
            
#        if start_number == -1 :
#            print('%%%\n' * 1000)
                    

            interval = interval_from_df(temp)
            interval_start = 0

            for col in interval_all :
                if int(col) < start_number :
                    interval_all.loc[excel_num, col] = -1
                else :
                    if interval_start < len(interval) :
                        interval_all.loc[excel_num, col] = interval[interval_start]
                        interval_start += 1
                    else :
                        interval_all.loc[excel_num ,col] = -1

            print(excel_num)
            print(interval_all)


# -----------------------------------------------
# plot temperature information (barplot)
# -----------------------------------------------

    
    fig = plt.figure(figsize = (14, 7))

    interval_col = interval_all.columns.astype(int)

#    x = []
#    for number in range(len(interval_all)) :
#        x.append(1)
    for excel in range(interval_all.shape[0]) :
        for col in interval_all.columns :
            val = int(interval_all.loc[excel, col])
            if (val != -1) & (val != 0) & (val != 60) :
                
                print(col, interval_all.loc[excel, col])
                plt.plot([col, col + 1], [interval_all.loc[excel, col], interval_all.loc[excel, col]], color = 'blue', linewidth = 3)



    plt.title('minute_interval\none sample stations')

    plt.ylabel('minute')
    plt.ylim(0, 300)
    grid_list = [0, 60, 120, 180, 240, 300]
    plt.yticks(grid_list)
    plt.grid()
    os.chdir(sample_plot)
    plt.savefig('scattered_timedelta_2_zoomed.png', dpi = 400)
    dlt.savefig(sample_plot, 'scattered_timedelta_2_zoomed.png', 400)

        


