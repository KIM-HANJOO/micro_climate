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



# -----------------------------------------------
# check infos (parameters) in Smart Seoul datas
# -----------------------------------------------

def basis() :
    columns = ['date'] + list(range(60))
    index_from_range = days_from_range([202004010100, 202202202200])
    df = pd.DataFrame(columns = list(range(60)), index = index_from_range)

    return df

#class get_dataframe() :
#    def __init__(self, name) :
#        preprocess_dir = Path(os.getcwd())
#        module_dir = preprocess_dir.parent
#        main_dir = module_dir.parent
#        preprocess_dir = os.path.join(main_dir, 'preprocessed')
#        datas_dir = os.path.join(main_dir, 'datas')
#
#        os.chdir(datas_dir)
#        temp = read_csv(excel)
#
#        serials = temp.loc[:, '시리얼'].tolist()
#
#        for serial in serials :
#            if serial not in os.listdir(preprocess_dir) :
#                pass
#        return


#df = basis()
#print(df.index)
#print(df.shape[0])

def mkdir(directory) :
    try :
        if not os.path.exists(directory) :
            os.makedirs(directory)
    except OSError :
        print(f'{directory} not available')

all_number = len(os.listdir(datas_dir))

a = input('remove_dir?')
if a == 'y' :
    dich.remove_inside_folder(serials_dir)




for excel_num, excel in enumerate(os.listdir(datas_dir)) :
    if excel_num > -1 :
        os.chdir(datas_dir)
        temp = read_csv(excel)

        temp.sort_values(by = ['시리얼'], axis = 0)
        temp.reset_index(drop = True, inplace = True)

        serials = sorted(temp.loc[:, '시리얼'].unique())
        
        all_serials = len(serials)
        os.chdir(serials_dir)

        for num_serial, serial in enumerate(serials) :
            serial = str(serial)
            if serial not in os.listdir(serials_dir) :
                mkdir(os.path.join(serials_dir, serial))
                os.chdir(os.path.join(serials_dir, serial))
            else :
                os.chdir(os.path.join(serials_dir, serial))

            maximum = []
            for excel in os.listdir(os.path.join(serials_dir, serial)) :
                maximum.append(int(excel[ : excel.index('.')]))
            if len(maximum) == 0 :
                cwnum = 1
            else :
                cwnum = max(maximum) + 1

            df = temp[temp['시리얼'] == serial]
            drop_index = df.index
#        df.sort_values(by = ['전송시간'], ignore_index = True, inplace = True)

            df.to_excel(f'{cwnum}.xlsx')
                
#        else :
#            os.chdir(os.path.join(serials_dir, serial)
#            df = read_excel(f'{serial}.xlsx')
#            df = pd.concat([df, temp[temp['시리얼'] == serial]], axis = 0, ignore_index = True)
#            df.reset_index(drop = True, inplace = True)
#
#            df.sort_values(by = ['전송시간'], ignore_index = True, inplace = True)
#            df.to_excel(f'{serial}.xlsx')

            temp.drop(drop_index, inplace = True)
            temp.reset_index(drop = True, inplace = True)

            
            print(f'{excel_num} / {all_number}, perc = {round(excel_num / all_number * 100, 2)}%\t serial : {num_serial} / {all_serials}, perc = {round(num_serial / all_serials * 100, 2)}%\t index_num = {len(temp.index)}')





#
#
#fig = plt.figure(figsize = (7, 7))
#
#for excel_num, excel in enumerate(os.listdir(datas_dir)) :
#    if excel_num == 0 :
#        os.chdir(datas_dir)
#        temp = read_csv(excel)
#        #temp = unite_para_time(temp)
#        print(temp.columns)
#        print(temp.head())
#
#        target_columns = []
#
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
#        wind_df = temp[target_columns]
#        wind_df.columns = ['angle', 'speed', 'squall_angle', 'squall_speed']
#
#        drop_index = []
#        for index in range(wind_df.shape[0]) :
#            if wind_df.loc[index, 'angle'] > 360 :
#                if wind_df.loc[index, 'speed'] > 10 :
#                    drop_index.append(index)
#
#        wind_df.drop(drop_index, inplace = True)
#        wind_df.reset_index(drop = True, inplace = True)
