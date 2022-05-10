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
sample_avail = os.path.join(sample_robby, 'preprocessed', 'only_available_time')


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
    year = int(string[ : 4])
    month = int(string[4 : 6])
    day = int(string[6 : 8])
    hour = int(string[8 : 10])
    minute = int(string[10 : 12])

    if (hour < 0) | (hour > 24) :
        print(string)
        print(hour)


    return datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute)

def minute_interval(datetime1, datetime2) :
    return ((datetime2 - datetime1).seconds // 60)



# -----------------------------------------------
# make date list and date_dict, inverse_dict
# -----------------------------------------------

# date from 2020.04.01 to 2021.12.31
date_dict, inverse_dict, real_date_list = all_date()


# -----------------------------------------------
# make date list and date_dict, inverse_dict
# -----------------------------------------------

# check all stations if there is any wrong formats


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

# make dataframe with columns of date(minute dropped) including excel name
    df = pd.DataFrame(columns = ['excel'] + real_date_list)
    df_num = 0

# make minutual - timedelta dataframe
    excepted = 0

    num_list = [6, 12, 15, 18, 27]
    num_list = [0]

    for excel_num, excel in enumerate(os.listdir(sample_avail)) :
        if excel_num in num_list :
            os.chdir(sample_avail)
            temp = read_excel(excel)

            df.loc[df_num, 'excel'] = excel.replace('.xlsx', '')

            for index in range(temp.shape[0]) :
                if index != 0 :
                    if str(temp.loc[index, '등록일자']) != 'nan' :
                        if str(temp.loc[index - 1, '등록일자']) != 'nan' :
                            if int(str(temp.loc[index, '등록일자'])[8 : 10]) < 25 :
                                if int(str(temp.loc[index - 1, '등록일자'])[8 : 10]) < 25 :


                                    prev_real_date = date_to_datetime(temp.loc[index - 1, '등록일자'])
                                    now_real_date = date_to_datetime(temp.loc[index, '등록일자'])
                                    temp_date = str(temp.loc[index, '등록일자'])[ : 10] + '00'
                                    
                                    print(prev_real_date)
                                    print(now_real_date)
                                    
                                    minute = minute_interval(prev_real_date, now_real_date)
                                    print(minute)
                                
                                
                                    df.loc[df_num, temp_date] = minute

            df_num += 1
            print(excel_num)

    print(df)
    temp_dir = os.path.join(sample_plot, 'preprocessed', 'temperature')
    dich.newfolder(temp_dir)

    os.chdir(os.path.join(sample_plot, 'preprocessed', 'temperature'))
    df.to_excel('time_interval.xlsx')
    print('dataframe saved')


# -----------------------------------------------
# plot temperature information (barplot)
# -----------------------------------------------

    fig = plt.figure(figsize = (14, 7))


    for num_col, col in enumerate(df.columns) :
        if col != 'excel' :
            plt.boxplot(df.loc[:, col].tolist(), positions = [num_col])
            print(f'{col} shown')

    plt.title('minute_interval\nall sample stations')

    plt.savefig('timedelta_minute.png', dpi = 400)
        


