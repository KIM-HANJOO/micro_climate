import os
import sys
from pathlib import Path
import os.path

preprocess_dir = Path(os.getcwd())
module_dir = preprocess_dir.parent
main_dir = module_dir.parent
datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
plot_dir = os.path.join(main_dir, 'plot')

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

def days_from_range(range_list) :
    # range_list = [lower, upper]
    
    month_df = pd.DataFrame(columns = list(range(1, 13)))
    month_df.loc[0, :] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    lower_month = month.day.copy()
    if leap_year(lower[ : 4]) :
        # February has 29 days
        lower_month.loc[0, 2] = 29

    upper_df = month.day.copy()
    if leap_year(upper[ : 4]) :
        # February has 29 days
        upper_df.loc[0, 2] = 29

    lower_year = int(lower[ : 4])
    lower_month = int(lower[4 : 6])
    lower_day = int(lower[6 :])

    upper_year = int(upper[ : 4])
    upper_month = int(upper[4 : 6])
    upper_day = int(upper[6 :])


    all_days = []
    if lower_year == upper_year :

        # accelerating add_month variable(from lower_month to upper_month)
        for add_month in range(lower_month, upper_month + 1) :
            if add_month == lower_month :
                temp_month = double_size(f'{add_month}')
                
                for add_day in range(lower_day, df.loc[0, add_month] + 1) :
                    temp_day = double_size(f'{add_day}')

                    all_days.append(f'{lower_year}' + temp_month + temp_day)

            elif add_month == upper_month :
                temp_month = double_size(f'{add_month}')

                for add_day in range(1, upper_day + 1) :
                    temp_day = double_size(f'{add_day}')

                    all_days.append(f'{lower_year}' + temp_month + temp_day)
            else :
                temp_month = double_size(f'{add_month}')

                for add_day in range(1, df.loc[0, add_month] + 1) :
                    temp_day = double_size(f'{add_day}')

                    all_days.append(f'{lower_year}' + temp_month + temp_day)

    elif lower_year < upper_year :

        # accelerating add_month from lower_month to Dec,
        # continuous add_month from Jan to upper_month

        for add_year in range(lower_year, upper_year + 1) :
            if add_year == lower_year :
                for add_month in range(lower_month, 13) :
                    if add_month == lower_month :
                        temp_month = double_size(f'{add_month}')

                        for add_day in range(lower_day, df.loc[0, add_month] + 1) :
                            temp_day = double_size(f'{add_day}')

                            all_days.append(add_year + temp_month + temp_day)

                    elif add_month > lower_month :
                        temp_month = double_size(f'{add_month}')

                        for add_day in range(1, upper_day + 1) :
                            temp_day = double_size(f'{add_day}')

                            all_days.append(f'{lower_year}' + temp_month + temp_day)
                    else :
                        temp_month = double_size(f'{add_month}')

                        for add_day in range(1, df.loc[0, add_month] + 1) :
                            temp_day = double_size(f'{add_day}')

                            all_days.append(f'{lower_year}' + temp_month + temp_day) 

            if (add_year > lower_year) & (add_year < upper_year) :
                for add_month in range(1, 13) :
                    for add_day in range(1, df.loc[0, add_month]) :

                        temp_month = double_size(f'{add_month}')
                        temp_day = double_size(f'{add_day}')

                        all_days.append(add_year, temp_month, temp_day) 

            elif add_year == upper_year :
                for add_month in range(1, upper_month) :
                    if add_month < upper_month :
                        for add_day in range(1, df.loc[0, add_month]) :

                            temp_month = double_size(f'{add_month}')
                            temp_day = double_size(f'{add_day}')

                            all_days.append(add_year, temp_month, temp_day) 

                    elif add_month == upper_month :
                        for add_day in range(1, upper_day + 1) :
                            temp_month = double_size(f'{add_month}')
                            temp_day = double_size(f'{add_day}')

                            all_days.append(add_year, temp_month, temp_day) 


    else :
        raise NotAvailableError



# -----------------------------------------------
# check infos (parameters) in Smart Seoul datas
# -----------------------------------------------

fig = plt.figure(figsize = (7, 7))

for excel_num, excel in enumerate(os.listdir(datas_dir)) :
    if excel_num == 0 :
        os.chdir(datas_dir)
        temp = read_csv(excel)
        #temp = unite_para_time(temp)
        print(temp.columns)
        print(temp.head())

        target_columns = []

        for column in temp.columns :
            if '풍' in column :
                target_columns.append(column)
            if '풍속' in column :
                if '돌풍' not in column :
                    target_wind_column = column
            if '풍향' in column :
                if '돌풍' not in column :
                    target_wind_column_2 = column

        print(temp[target_columns])
        wind_df = temp[target_columns]
        wind_df.columns = ['angle', 'speed', 'squall_angle', 'squall_speed']

        drop_index = []
        for index in range(wind_df.shape[0]) :
            if wind_df.loc[index, 'angle'] > 360 :
                if wind_df.loc[index, 'speed'] > 10 :
                    drop_index.append(index)

        wind_df.drop(drop_index, inplace = True)
        wind_df.reset_index(drop = True, inplace = True)

        plt.scatter(wind_df.loc[:, 'angle'], wind_df.loc[:, 'speed'])

#        for index in range(wind_df.shape[0]) :
#            plt.scatter([wind_df.loc[index, 'angle'], wind_df.loc[index, 'speed']])


plt.title('wind angle & speed')
plt.xlabel('wind angle(degree)')
plt.ylabel('wind speed(m/s)')
os.chdir(plot_dir)
dlt.savefig(plot_dir, 'wind_scatter.png', 400)
            

        

        






#for excel_num, excel in enumerate(os.listdir(datas_dir)) :
#    if excel_num == 0 :
#        os.chdir(datas_dir)
#        temp = read_csv(excel)
#        temp = unite_para_time(temp)
#        print(temp.head())
#        print(temp.columns)
#
#        target_columns = []
#        for column in temp.columns :
#            if '풍' in column :
#                target_columns.append(column)
#            if '풍속' in column :
#                if '돌풍' not in column :
#                    target_wind_column = column
#            if '풍향' in column :
#                if '돌풍' not in column :
#                    target_wind_column_2 = column
#
#        print(temp[target_columns])
#        wind_temp = temp[target_columns].copy()
#        wind_temp_2 = temp.loc[:, target_wind_column].tolist()
#
#        wind_temp_3 = [x for x in wind_temp_2 if (int(x) < 10) & (int(x) != 0)]
#        wind_temp_4 = [x for x in wind_temp_2 if (int(x) > 10)]
#        wind_temp_5 = [x for x in wind_temp_2 if int(x) == 0]
#
#        wind_direc = temp.loc[:, target_wind_column_2].copy()
#        wind_direc_1 = [x for x in wind_direc if int(x) != 0]
#        wind_direc_2 = [x for x in wind_direc_1 if int(x) < 361]
#
#        plt.hist(wind_direc_2)
#        plt.title(f'wind direction\ntotal = {len(wind_direc)}, target = {len(wind_direc_2)}')
#        #plt.title(f'0 = wind speed\nnumber = {len(wind_temp_5)}')
#
##        for column in wind_temp.columns :
##            for index in range(wind_temp.shape[0]) :
##                if wind_temp.loc[index, column] != 0 :
##                    print(wind_temp.loc[index, column])
#
#
#
#os.chdir(plot_dir)
#dlt.savefig(plot_dir, 'temp.png', 400)
#
#
#
