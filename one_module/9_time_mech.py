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
sample_avail = os.path.join(sample_robby, 'only_available_time')


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


#def interval_from_df(data) :
#    # index_number : get indexes of data that has the time value
#    # index_values : get values of index_numbered timesteps
#
#    index_number = []
#    index_values = []
#    for index in range(data.shape[0]) :
#        if str(data.loc[index, '등록일자']) != 'nan' :
#            index_number.append(index)
#            index_values.append(data.loc[index, '등록일자'])
#
#    # interval : list with adjacent - subtracted values of indeX_values
#
#    interval = []
#    for num_index, index in enumerate(range(len(index_values))) :
#        if num_index > 0 :
#            interval.append(minute_interval(index_values[num_index - 1], index_values[num_index]))
#
#    return interval
#

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


# -----------------------------------------------
# make function for time convert
# -----------------------------------------------

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
        return dt - datetime.timedelta(minutes = dt.minute)
        #return datetime.datetime(year = year, month = month, day = day, hour = hour, minute = 0)

    else :
        return dt + datetime.timedelta(hours = 1) - datetime.timedelta(minutes = dt.minute)

#        if hour == 23 :
#            if day < 30 :
#                return datetime.datetime(year = year, month = month, day = day  + 1, hour = 0, minute = 0)
#        else :
#            return datetime.datetime(year = year, month = month, day = day, hour = hour + 1, minute = 0)
#


def round_data(df) :
    #time_jam range (from 0 <= time_interval <= jam_top)
    jam_top = 0


    add_columns = ['overlap', 'time_jam', 'minute_interval', '보정_시간', 'hour_available']
    for add in add_columns :
        df[add] = None

    total_size = df.shape[0]
    interval = interval_from_df(df)
    df.loc[:, 'minute_interval'] = interval

    nan = 0
    for index in range(df.shape[0]) :
        if str(df.loc[index, '등록일자']) != 'nan' :
            print(df.loc[index, '등록일자'])
            print(round_hour(df.loc[index, '등록일자']))
            df.loc[index, '보정_시간'] = datetime_to_date(round_hour(df.loc[index, '등록일자']))
            print('\t', df.loc[index, '보정_시간'])
            if df.loc[index, 'minute_interval'] <= jam_top :
                df.loc[index, 'time_jam'] = 'O'
            else :
                df.loc[index, 'time_jam'] = 'X'

        else :
            nan += 1

    jammed = 0
    overlapped = 0

    drop_index = []
    for index in range(df.shape[0]) :
        if df.loc[index, 'time_jam'] == 'O' :
            drop_index.append(index)
            jammed += 1
            #print(index, '\t', df.loc[index, 'jam'])
        else :
            if str(df.loc[index, '등록일자']) == 'nan' :
                drop_index.append(index)
                df.loc[index, 'overlap'] = 'X'

            else :

                if index > 0 :
                    if df.loc[index, '보정_시간'] == df.loc[index - 1, '보정_시간'] :
                        drop_index.append(index)
                        overlapped += 1
                        df.loc[index, 'overlap'] = 'O'
                    else :
                        df.loc[index, 'overlap'] = 'X'
                        #print(index, '\t', df.loc[index, '보정_시간'], df.loc[index - 1, '보정_시간'])


    for index in range(df.shape[0]) :
        if (df.loc[index, 'time_jam'] == 'O') | (df.loc[index, 'overlap'] == 'O') :
            df.loc[index, 'hour_available'] = 'X'

        else :
            df.loc[index, 'hour_available'] = 'O'

    
    
    df.reset_index(drop = True, inplace = True)

    return df, jammed, overlapped, nan




# -----------------------------------------------
# plot 
# -----------------------------------------------

a = input('round data (y/n)')

sample_round = os.path.join(sample_robby, 'preprocessed',  'rounded')
dich.newfolder(sample_round)

if a == 'y' :
    df = pd.DataFrame(columns = ['excel', 'org_date', 'time-jam', 'overlapped rounded time', 'nan times', 'dropped_date', 'percentage'])
    df_num = 0

    for excel_num, excel in enumerate(os.listdir(sample_avail)) :
        if excel_num > 613:
            os.chdir(sample_avail)
            temp = read_excel(excel)
            total_size = temp.shape[0]

            temp2, jammed, overlapped, nan = round_data(temp)
            os.chdir(sample_round)
            temp2.to_excel(excel)

            df.loc[df_num, :] = [excel, total_size, jammed, overlapped, nan, temp2.shape[0], round((temp2.shape[0] / total_size) * 100, 2)]
            df_num += 1

            print(excel_num, '\n')

    os.chdir(sample_robby)
    df.to_excel('rounded_info_1.xlsx')
            


