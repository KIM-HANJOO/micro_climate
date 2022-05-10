import os
import sys
from pathlib import Path
import os.path

#   < directory paths >
samples_module_dir = Path(os.getcwd())
sample_robby = samples_module_dir.parent
sample_data = os.path.join(sample_robby, 'data')
sample_info = os.path.join(sample_robby, 'info')
sample_plot = os.path.join(sample_robby, 'plot')
sample_typo = os.path.join(sample_robby, 'typo')
rounded_dir = os.path.join(sample_robby, 'rounded')
zoom_plot = os.path.join(sample_robby, 'plot_zoom')

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


def unite_para_time(excel) :

    for column in excel.columns : 
        if '전송시간' in column :
            time_sent = column

        elif '등록일자' in column :
            time_saved = column

    for num_index, index in enumerate(range(excel.shape[0])) :
        if num_index < 3 :
            excel.loc[index, time_sent] = unite_para_time_unit(excel.loc[index, time_sent])
            
            excel.loc[index, time_saved] = unite_para_time_unit(excel.loc[index, time_sent])
            print(f'{index} done', end = '\r')

    return excel


def unite_para_time_unit(string) :

    split_list = []

    # for format "2020.4.1 1:00"
    if ':' in string :
        if '.' in string :
#            print("format 2020.4.1 1:00")
            
            string_left = string
            for itera in range(2) :
                target_string = '.'
                temp_left = string_left[ : string_left.index(target_string)]
                temp_right = string_left[ string_left.index(target_string) + 1 :]

                if len(temp_left) == 1 :
                    temp_left = '0' + temp_left

                split_list.append(temp_left)
                string_left = temp_right
            
            for itera in range(1) :
                target_string = ' '
                temp_left = string_left[ : string_left.index(target_string)]
                temp_right = string_left[ string_left.index(target_string) + 1 :]

                if len(temp_left) == 1 :
                    temp_left = '0' + temp_left

                split_list.append(temp_left)
                string_left = temp_right
                

            for itera in range(1) :
                target_string = ':'
                temp_left = string_left[ : string_left.index(target_string)]
                temp_right = string_left[ string_left.index(target_string) + 1 :]

                if len(temp_left) == 1 :
                    temp_left = '0' + temp_left

                split_list.append(temp_left)
                string_left = temp_right

            # for left
            split_list.append(string_left)

    else :
        print(string, '\n')

    return ''.join(split_list)


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
# advanced version of template
# -----------------------------------------------
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


summer_hours = []
winter_hours = []

summer_day = '20210621'
winter_day = '20211222'

for hour in range(24) :
    hour_str = double_size(str(hour))
    summer_hours.append(f'{summer_day}{hour_str}00')
    winter_hours.append(f'{winter_day}{hour_str}00')


print(summer_hours)
print(winter_hours)

summer_df = pd.DataFrame(index = summer_hours)
winter_df = pd.DataFrame(index = winter_hours)


target_info = ['기온', '상대습도']

for target in target_info :
    for num_excel, excel in enumerate(os.listdir(rounded_dir)) :
        
        # read excel
        os.chdir(rounded_dir)
        target_col = ['기온', '상대습도', '풍향', '풍속', '보정_시간', 'hour_available']
        df = read_excel(excel)[target_col]
        df.sort_values(by = ['보정_시간'], inplace = True)

#        # pull summer / winter days
#        summer_index = []
#        winter_index = []
#        for num_index, index in enumerate(range(df.shape[0])) :
#            
#            if str(df.loc[index, '보정_시간'])[ : 8] == summer_day :
#                summer_index.append(index)
#
#            if str(df.loc[index, '보정_시간'])[ : 8] == winter_day :
#                winter_index.append(index)
#
#        summer_temp = df.loc[summer_index, : ]
#        winter_temp = df.loc[winter_index, : ]
#
#        summer_avail = summer_temp[summer_temp['hour_available'] == 'O']
#        winter_avail = winter_temp[winter_temp['hour_available'] == 'O']
#
#        summer_avail.reset_index(drop = True, inplace = True)
#        winter_avail.reset_index(drop = True, inplace = True)
#
#        for index in range(summer_avail.shape[0]) :
#            print(summer_avail.loc[index, '보정_시간'])
#            summer_df.loc[str(summer_avail.loc[index, '보정_시간']), excel] = str(summer_avail.loc[index, target])
#
#
#        for index in range(winter_avail.shape[0]) :
#            winter_df.loc[str(winter_avail.loc[index, '보정_시간']), excel] = str(winter_avail.loc[index, target])
#
#        print(f'{target}\t{num_excel}\t{excel}')
#
#
#    # save dataframe
#    os.chdir(zoom_plot)
#
#    summer_df.to_excel(f'{target}_summer_df.xlsx')
#    winter_df.to_excel(f'{target}_winter_df.xlsx')

    # load dataframe

    os.chdir(zoom_plot)

    summer_df = read_excel(f'{target}_summer_df.xlsx')
    winter_df = read_excel(f'{target}_winter_df.xlsx')


    print(summer_df)
    print(winter_df)

    print(summer_df.shape)
    print(winter_df.shape)

    # plot graphs

    fig = plt.figure(figsize = (14, 15))

    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    boxprops = dict(linewidth = 2, color = 'firebrick')

    xticks = []
    for num_index, index in enumerate(summer_df.index) :
        summer_box = [int(x) for x in summer_df.loc[index, :].tolist() if str(x) != 'nan']

        ax1.boxplot(summer_box, boxprops = boxprops, positions = [num_index + 1])
        xticks.append(num_index + 1)

    for num_index, index in enumerate(winter_df.index) :
        winter_box = [int(x) for x in winter_df.loc[index, :].tolist() if str(x) != 'nan']
        ax2.boxplot(winter_box, boxprops = boxprops, positions = [num_index + 1])

    # set tick labels
    xticks = []
    for hour in range(24) :
        xticks.append(double_size(str(hour)))



    ax1.set_xticklabels(xticks, rotation = 0)
    ax2.set_xticklabels(xticks, rotation = 0)


    if target == '기온' :
        ax1.set_ylim(-5, 33)
        ax2.set_ylim(-5, 33)
    elif target == '상대습도' :
        ax1.set_ylim(10, 120)
        ax2.set_ylim(10, 120)

    ax1.set_title('2021/ 06/ 21')
    ax2.set_title('2021/ 12/ 22')

    os.chdir(zoom_plot)
    plt.savefig(f'{target}_summer_winter.png', dpi = 400)
    dlt.savefig(zoom_plot, f'{target}_summer_winter.png', 400)

    plt.clf


    # plot no_zoomed graph

    fig = plt.figure(figsize = (14, 15))

    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    boxprops = dict(linewidth = 2, color = 'firebrick')

    xticks = []
    for num_index, index in enumerate(summer_df.index) :
        summer_box = [int(x) for x in summer_df.loc[index, :].tolist() if str(x) != 'nan']

        ax1.boxplot(summer_box, boxprops = boxprops, positions = [num_index + 1])
        xticks.append(num_index + 1)

    for num_index, index in enumerate(winter_df.index) :
        winter_box = [int(x) for x in winter_df.loc[index, :].tolist() if str(x) != 'nan']
        ax2.boxplot(winter_box, boxprops = boxprops, positions = [num_index + 1])

    # set tick labels
    xticks = []
    for hour in range(24) :
        xticks.append(double_size(str(hour)))



    ax1.set_xticklabels(xticks, rotation = 0)
    ax2.set_xticklabels(xticks, rotation = 0)

    ax1.set_title('2021/ 06/ 21, 2nd')
    ax2.set_title('2021/ 12/ 22, 2nd')

    os.chdir(zoom_plot)
    plt.savefig(f'{target}_summer_winter_zoomed.png', dpi = 400)
    dlt.savefig(zoom_plot, f'{target}_summer_winter_zoomed.png', 400)

    plt.clf
