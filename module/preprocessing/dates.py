import os
import sys
from pathlib import Path
import os.path

preprocess_module_dir = Path(os.getcwd())
module_dir = preprocess_module_dir.parent
main_dir = module_dir.parent
datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
plot_dir = os.path.join(main_dir, 'plot')
preprocess_dir = os.path.join(main_dir, 'preprocessed')
serials_dir = os.path.join(preprocess_dir, 'serials')
merged_dir = os.path.join(preprocess_dir, 'merged')

sys.path.append(module_dir)
sys.path.append(self_module)
sys.path.append(preprocess_module_dir)

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
# additional functions to define
# -----------------------------------------------

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

def make_month_df(year) :
    year = int(year)
    month_df = pd.DataFrame(columns = list(range(1, 13)))
    month_df.loc[0, :] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap_year(year) :
        # February has 29 days
        month_df.loc[0, 2] = 29

    return month_df


def days_from_range(range_list) :
    # range_list = [lower, upper]
    lower = str(range_list[0])
    upper = str(range_list[1])
    
    lower_year = int(lower[ : 4])
    lower_month = int(lower[4 : 6])
    lower_day = int(lower[6 : 8])
    lower_hour = int(lower[8 : 10])
    lower_minute = int(lower[10 : 12])

    upper_year = int(upper[ : 4])
    upper_month = int(upper[4 : 6])
    upper_day = int(upper[6 : 8])
    upper_hour = int(lower[8 : 10])
    upper_minute = int(lower[10 : 12])



    all_days = []
    if lower_year == upper_year :
        df = make_month_df(lower_year)

        # accelerating add_month variable(from lower_month to upper_month)
        for add_month in range(lower_month, upper_month + 1) :

            # if identical year, month with lower_date
            if add_month == lower_month :
                temp_month = double_size(f'{add_month}')
                
                # if identical month -> starting from lower day
                for add_day in range(lower_day, df.loc[0, add_month] + 1) :
                    temp_day = double_size(f'{add_day}')

                    # first day, first hour
                    if add_day == lower_day :
                        for add_hour in range(lower_hour, 24) :
                            temp_hour = double_size(f'{add_hour}')
                            if add_hour == lower_hour :
                                for add_minute in range(lower_minute, 60) :
                                    temp_minute = double_size(f'{add_minute}')
                                    all_days.append(f'{lower_year}' + temp_month + temp_day + temp_hour + temp_minute)

                            else :
                                for add_minute in range(60) :
                                    all_days.append(f'{lower_year}' + temp_month + temp_day + temp_hour + temp_minute)
                    else :
                        if add_day > lower_day :
                            for add_hour in range(24) :
                                temp_hour = double_size(f'{add_hour}')
                                for add_minute in range(60) :
                                    temp_minute = double_size(f'{add_minute}')
                                    all_days.append(f'{lower_year}' + temp_month + temp_day + temp_hour + temp_minute)

            # else ; identical year, nonidentical month
            elif (add_month > lower_month) & (add_month < upper_month)  :
                temp_month = double_size(f'{add_month}')

                for add_day in range(1, df.loc[0, add_month + 1]) :
                    temp_day = double_size(f'{add_day}')
                    for add_hour in range(24) :
                        temp_hour = double_size(f'{add_hour}')
                        for add_minute in range(60) :
                            temp_minute = double_size(f'{add_minute}')

                            all_days.append(f'{lower_year}' + temp_month + temp_day + temp_hour + temp_minute)
                            

            # identical month with the upper limit
            elif add_month == upper_month :
                temp_month = double_size(f'{add_month}')

                for add_day in range(1, upper_day + 1) :
                    temp_day = double_size(f'{add_day}')

                    all_days.append(f'{lower_year}' + temp_month + temp_day)
                    
                    if add_day == upper_day :
                        for add_hour in range(0, upper_hour + 1) :
                            temp_hour = double_size(f'{add_hour}')
                            # if last hour (identical hour)
                            if add_hour == upper_hour :
                                for add_minute in range(0, upper_minute + 1) :
                                    temp_minute = double_size(f'{add_minute}')

                                    all_days.append(f'{lower_year}' + temp_month + temp_day + temp_hour + temp_minute)

                            # if not last hour -> range of minute from 0 to 59
                            else :
                                for add_minute in range(60) :
                                    temp_minute = double_size(f'{add_minute}')

                                    all_days.append(f'{lower_year}' + temp_month + temp_day + temp_hour + temp_minute)



    elif lower_year < upper_year :

        # accelerating add_month from lower_month to Dec,
        # continuous add_month from Jan to upper_month

        for add_year in range(lower_year, upper_year + 1) :
            df = make_month_df(add_year)
            # case 1, first year (lower_year)
            if add_year == lower_year :
                for add_month in range(lower_month, 13) :
                    if add_month == lower_month :
                        temp_month = double_size(f'{add_month}')

                        for add_day in range(lower_day, df.loc[0, add_month] + 1) :
                            temp_day = double_size(f'{add_day}')

                            if add_day == lower_day :
                                for add_hour in range(lower_hour, 24) :
                                    temp_hour = double_size(f'{add_hour}')

                                    if add_hour == lower_hour :
                                        for add_minute in range(lower_minute, 60) :
                                            temp_minute = double_size(f'{add_minute}')
                                            all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute)
                                    else :
                                        for add_minute in range(60) :
                                            temp_minute = double_size(f'{add_minute}')
                                            all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute)

                            else :
                                for add_hour in range(24) :
                                    temp_hour = double_size(f'{add_hour}')
                                    for add_minute in range(60) :
                                        temp_minute = double_size(f'{add_minute}')

                                        all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute)

                    elif add_month > lower_month :
                        temp_month = double_size(f'{add_month}')

                        for add_day in range(1, upper_day + 1) :
                            temp_day = double_size(f'{add_day}')

                            for add_hour in range(24) :
                                temp_hour = double_size(f'{add_hour}')
                                for add_minute in range(60) :
                                    temp_minute = double_size(f'{add_minute}')
                                    all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute)
                    
                    # add_month < lower_month -> Error case
                    else :
                        raise NotAvailableError

#                        temp_month = double_size(f'{add_month}')
#
#                        for add_day in range(1, df.loc[0, add_month] + 1) :
#                            temp_day = double_size(f'{add_day}')
#
#                            all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute) 

            # case 2, inbetween bounds
            if (add_year > lower_year) & (add_year < upper_year) :
                for add_month in range(1, 13) :
                    for add_day in range(1, df.loc[0, add_month]) :

                        temp_month = double_size(f'{add_month}')
                        temp_day = double_size(f'{add_day}')

                        for add_hour in range(24) :
                            temp_hour = double_size(f'{add_hour}')

                            for add_minute in range(60) :
                                temp_minute = double_size(f'{add_minute}')

                                all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute)

            elif add_year == upper_year :
                for add_month in range(1, upper_month) :
                    if add_month < upper_month :
                        for add_day in range(1, df.loc[0, add_month]) :

                            temp_month = double_size(f'{add_month}')
                            temp_day = double_size(f'{add_day}')

                            for add_hour in range(24) :
                                temp_hour = double_size(f'{add_hour}')

                                for add_minute in range(60) :
                                    temp_minute = double_size(f'{add_minute}')
                                    
                                    all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute)

                    elif add_month == upper_month :
                        for add_day in range(1, upper_day + 1) :
                            temp_month = double_size(f'{add_month}')
                            temp_day = double_size(f'{add_day}')

                            for add_hour in range(0, upper_hour + 1) :
                                temp_hour = double_size(f'{add_hour}')
                                # if last hour (identical hour)
                                if add_hour == upper_hour :
                                    for add_minute in range(0, upper_minute + 1) :
                                        temp_minute = double_size(f'{add_minute}')

                                        all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute)

                                # if not last hour -> range of minute from 0 to 59
                                else :
                                    for add_minute in range(60) :
                                        temp_minute = double_size(f'{add_minute}')

                                        all_days.append(str(add_year) + temp_month + temp_day + temp_hour + temp_minute)


        return all_days

    else :
        raise NotAvailableError


def mkdir(directory) :
    try :
        if not os.path.exists(directory) :
            os.makedirs(directory)
    except OSError :
        print(f'{directory} not available')


def basis() :
    columns = ['date'] + list(range(60))
    index_from_range = days_from_range([202004010100, 202202202200])
    df = pd.DataFrame(columns = list(range(60)), index = index_from_range)

    return df

# -----------------------------------------------------------------------------
# boxplot for info_count
# -----------------------------------------------------------------------------

group_o = []
group_v = []
os.chdir(merged_dir)
all_num = len(os.listdir(merged_dir))
for excel_num, excel in enumerate(os.listdir(merged_dir)) :
    temp = read_excel(excel) 

    if 'OC3CL' in excel :
        group_o.append(temp.shape[0])
    elif 'V02Q1' in excel :
        group_v.append(temp.shape[0])
    else :
        print('ffffffffffff\n', excel)

    print(f'{excel_num} / {all_num}')
        
            
fig = plt.figure(figsize = [7, 7])
plt.boxplot(group_o, positions = [1])
plt.boxplot(group_v, positions = [2])

plt.xticks([1, 2], ['OC3CL', 'V02Q1'])
plt.title('number of index for stations\nOC3CL(9576), V02Q1(16415)')
plt.plot([-1, 1.5], [9576, 9576])
plt.plot([1.5, 4], [16415, 16415])
plt.xlim(0, 3)
plt.ylabel('index(hours)')

dlt.savefig(plot_dir, 'numbers_of_index_statinos.png', 400)







