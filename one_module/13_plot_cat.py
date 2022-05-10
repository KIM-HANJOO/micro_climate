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

import summer_winter as sw

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

def group_three(df, sort_col, label_col) :
    df.sort_values(by = [sort_col], inplace = True, ignore_index = True)

    bottom = df.loc[0 : 9, label_col].tolist()
    middle = df.loc[10 : 21, label_col].tolist()
    top = df.loc[22 : 31, label_col].tolist()

    return top, middle, bottom

def sum_list(list1, list2) :
    array1 = np.array(list1)
    array2 = np.array(list2)

    return list(array1 + array2)


def devide_list(list1, devider) :

    return list(np.array(list1) / devider)

def variance_list(std_list, cmp_list) :
    diff_array = np.array(cmp_list) - np.array(std_list)
    print('var\t', np.var(diff_array), diff_array[ : 5])
    return np.var(diff_array)

def drop_nan(df) :
    df.reset_index(drop = True, inplace = True)
    drop_index = []
    for index in range(df.shape[0]) :
        for col in df.columns :
            if pd.isna(df.loc[index, col]) :
                if index not in drop_index :
                    drop_index.append(index)
    df.drop(drop_index, axis = 0, inplace = True)
    df.reset_index(drop = True, inplace = True)

    return df, drop_index

def mean_df(df) :
    for num_col, col in enumerate(df.columns) :
        if num_col == 0 :
            summed = df.loc[:, col].tolist()

        else :
            list2 = df.loc[:, col].tolist()
            
            summed = sum_list(summed, list2)

    mean_list = devide_list(summed, df.shape[1])

    return mean_list

def group_four(df, mean_list) :

    max_m = max(mean_list)
    min_m = min(mean_list)

    print('##########')
    print('actual')
    print(max_m, min_m)
    df_label = df.copy()
    df_label.loc['group', :] = None

    print('targets')

    for num_col, col in enumerate(df.columns) :
        target_list = df.loc[:, col].tolist()
        max_t = max(target_list)
        min_t = min(target_list)
        
        print(max_t, min_t)
        if (max_t > max_m) & (min_t < min_m) :
            df_label.loc['group', col] = 'high_fluc'

        elif (max_t < max_m) & (min_t > min_m) :
            df_label.loc['group', col] = 'low_fluc'

        elif (max_t >= max_m) & (min_t >= min_m) :
            df_label.loc['group', col] = 'higher_value'

        elif (max_t <= max_m) & (min_t <= min_m) :
            df_label.loc['group', col] = 'lower_value'

    return df_label


def variance_df(df) :

    print('####\n' * 100)
    print(df.shape)
    # drop nan values in df
    df, drop_index = drop_nan(df)
    print(df.shape)

    # get variance
    for num_col, col in enumerate(df.columns) :
        if num_col == 0 :
            summed = df.loc[:, col].tolist()

        else :
            list2 = df.loc[:, col].tolist()
            
            summed = sum_list(summed, list2)

    mean_list = devide_list(summed, df.shape[1])

    var_df = pd.DataFrame(columns = ['excel', 'var'])
    df_num = 0
    for num_col, col in enumerate(df.columns) :
        var_df.loc[df_num, 'excel'] = col
        var_df.loc[df_num, 'var'] = np.var(df.loc[:, col].tolist())
        #var_df.loc[df_num, 'var'] = variance_list(mean_list, df.loc[:, col].tolist())

        df_num += 1

    print(var_df)
    return var_df, mean_list

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

    
    # load summer, winter - weather stations infos
    if target == '기온' :
        summer, winter = sw.get_summer_winter()
    else :
        summer, winter = sw.get_humidity()

    # load dataframe

    os.chdir(zoom_plot)

    summer_df = read_excel(f'{target}_summer_df.xlsx')
    winter_df = read_excel(f'{target}_winter_df.xlsx')
    
    summer_mean = mean_df(summer_df)
    winter_mean = mean_df(winter_df)

    for index in summer_df.index :
        for col in summer_df.columns :
            summer_df.loc[index, col] = float(summer_df.loc[index, col])

    summer_label = group_four(summer_df, summer)
    winter_label = group_four(winter_df, winter)



    os.chdir(zoom_plot)
    if target == '기온' :
        summer_label.to_excel('info1.xlsx')
        winter_label.to_excel('info2.xlsx')

    # summer

    fig = plt.figure(figsize = (20, 15))

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    # ax1 : high variance  |   ax2 : higher value
    # ax3 : lower value    |   ax4 : lower varince

    print(summer_label)

    #ax1
    num = 0
    for col in summer_df.columns :
        if summer_label.loc['group', col] == 'high_fluc' :
            ax1.plot(summer_df.loc[:, col].tolist(), alpha = 0.8, color = 'red')
            num += 1
        else :
            ax1.plot(summer_df.loc[:, col].tolist(), color = 'grey', alpha = 0.3)
    ax1.plot(summer, color = 'blue', linewidth = 3, alpha = 0.5)
    ax1.set_title(f'high fluctuation, num = {num}')


    #ax2
    num = 0
    for col in summer_df.columns :
        if summer_label.loc['group', col] == 'low_fluc' :
            ax2.plot(summer_df.loc[:, col].tolist(), alpha = 0.8, color = 'red')
            num += 1
        else :
            ax2.plot(summer_df.loc[:, col].tolist(), color = 'grey', alpha = 0.3)
    ax2.plot(summer, color = 'blue', linewidth = 3, alpha = 0.5)
    ax2.set_title(f'low fluctuation, num = {num}')


    #ax3
    num = 0
    for col in summer_df.columns :
        if summer_label.loc['group', col] == 'higher_value' :
            ax3.plot(summer_df.loc[:, col].tolist(), alpha = 0.8, color = 'red')
            num += 1
        else :
            ax3.plot(summer_df.loc[:, col].tolist(), color = 'grey', alpha = 0.3)
    ax3.plot(summer, color = 'blue', linewidth = 3, alpha = 0.5)
    ax3.set_title(f'higher, num = {num}')

    #ax4
    num = 0
    for col in summer_df.columns :
        if summer_label.loc['group', col] == 'lower_value' :
            ax4.plot(summer_df.loc[:, col].tolist(), alpha = 0.8, color = 'red')
            num += 1
        else :
            ax4.plot(summer_df.loc[:, col].tolist(), color = 'grey', alpha = 0.3)
    ax4.plot(summer, color = 'blue', linewidth = 3, alpha = 0.5)
    ax4.set_title(f'lower, num = {num}')

    save_path = os.path.join(zoom_plot, 'summer_four')
    dich.newfolder(save_path)
    os.chdir(save_path)
    plt.savefig(f'{target}_summer_group_four.png', dpi = 400)
    dlt.savefig(zoom_plot, f'{target}_summer_group_four.png', 400)


    # winter


    fig = plt.figure(figsize = (20, 15))

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    # ax1 : high variance  |   ax2 : higher value
    # ax3 : lower value    |   ax4 : lower varince

    print(winter_label)

    #ax1
    num = 0
    for col in winter_df.columns :
        if winter_label.loc['group', col] == 'high_fluc' :
            ax1.plot(winter_df.loc[:, col].tolist(), alpha = 0.8, color = 'red')
            num += 1
        else :
            ax1.plot(winter_df.loc[:, col].tolist(), color = 'grey', alpha = 0.3)
    ax1.plot(winter, color = 'blue', linewidth = 3, alpha = 0.5)
    ax1.set_title(f'high fluctuation, num = {num}')


    #ax2
    num = 0
    for col in winter_df.columns :
        if winter_label.loc['group', col] == 'low_fluc' :
            ax2.plot(winter_df.loc[:, col].tolist(), alpha = 0.8, color = 'red')
            num += 1
        else :
            ax2.plot(winter_df.loc[:, col].tolist(), color = 'grey', alpha = 0.3)
    ax2.plot(winter, color = 'blue', linewidth = 3, alpha = 0.5)
    ax2.set_title(f'low fluctuation, num = {num}')


    #ax3
    num = 0
    for col in winter_df.columns :
        if winter_label.loc['group', col] == 'higher_value' :
            ax3.plot(winter_df.loc[:, col].tolist(), alpha = 0.8, color = 'red')
            num += 1
        else :
            ax3.plot(winter_df.loc[:, col].tolist(), color = 'grey', alpha = 0.3)
    ax3.plot(winter, color = 'blue', linewidth = 3, alpha = 0.5)
    ax3.set_title(f'higher, num = {num}')

    #ax4
    num = 0
    for col in winter_df.columns :
        if winter_label.loc['group', col] == 'lower_value' :
            ax4.plot(winter_df.loc[:, col].tolist(), alpha = 0.8, color = 'red')
            num += 1
        else :
            ax4.plot(winter_df.loc[:, col].tolist(), color = 'grey', alpha = 0.3)
    ax4.plot(winter, color = 'blue', linewidth = 3, alpha = 0.5)
    ax4.set_title(f'lower, num = {num}')

    save_path = os.path.join(zoom_plot, 'winter_four')
    dich.newfolder(save_path)
    os.chdir(save_path)
    plt.savefig(f'{target}_winter_group_four.png', dpi = 400)
    dlt.savefig(zoom_plot, f'{target}_winter_group_four.png', 400)

