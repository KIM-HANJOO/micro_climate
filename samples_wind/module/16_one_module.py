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

#   import self packages

import directory_change as dich
import discordlib_pyplot as dlt



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
#font_path = "/mnt/c/Users/joo09/Documents/Github/fonts/D2Coding.ttf"
#font = font_manager.FontProperties(fname = font_path).get_name()
#rc('font', family = font)


rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

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
sample_rounded = os.path.join(sample_robby, 'rounded')



main_dir = sample_robby.parent
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
# actual data availability 
# -----------------------------------------------


sample_plot_data = os.path.join(sample_plot, 'data_basics')
dich.newfolder(sample_plot_data)

a = input('plot missing days? (y/n)')

if a == 'y' :

    sample_plot_data = os.path.join(sample_plot, 'data_basics')
    dich.newfolder(sample_plot_data)

    os.chdir(sample_plot)
    data_ava = read_excel('date_availability_forsampels.xlsx')

    for index in range(data_ava.shape[0]) :
        data_ava.loc[index, 'starting'] = str(int(data_ava.loc[index, 'starting']))
        data_ava.loc[index, 'ending'] = str(int(data_ava.loc[index, 'ending']))


    print(data_ava)

    fig = plt.figure(figsize = (10, 6))
    ys, xs, patches = plt.hist(data_ava.loc[:, 'non-available'].tolist(), label = 'missing days', bins = 200)

    for i in range(len(ys)) :
        if ys[i] != 0 :
            if i == 0 :
                x_position = 0.1
            else :
                x_position =  -20

            plt.text(x = xs[i] + x_position, y = ys[i] + 0.1,
                    s = f'{int(ys[i])}', color = 'red')

    plt.title('missing days\n1107 stations')
    plt.xlim(0, 2000)
    plt.xlabel('missing days')
    plt.ylabel('number')
    plt.grid()
    os.chdir(sample_plot_data)
    plt.savefig('missing_days.png', dpi = 400)




a = input('time interval shown (y/n)')

if a == 'y' :
    temp_dir = os.path.join(sample_plot, 'preprocessed', 'temperature')
    os.chdir(temp_dir)
    temp = read_excel('time_interval.xlsx')
    target_index = list(range(2, 10))
    temp = temp.loc[target_index, :]
    temp.reset_index(drop = True, inplace = True)


    fig = plt.figure(figsize = (14, 7))

    for num_col, col in enumerate(temp.columns) :
        if col != 'excel' :
            plt.boxplot(temp.loc[:, col].tolist(), positions = [num_col])
            print(f'{col} shown')

    plt.title('minute_interval\nall sample stations')

    plt.savefig('timedelta_minute.png', dpi = 400)

            



a = input('plot actual days (y/n)')

if a == 'y' :

    start_date = date_to_datetime('202004010000')
    end_date = date_to_datetime('202112312300')
    
    dur = end_date - start_date

    end_timestep = dur.days * 24 + dur.seconds // 3600

    xticks = []
    xticks_datetime = []

    for timestep in range(end_timestep) :
        if timestep % 500 == 0 :
            xticks.append(timestep)
            date_string = datetime_to_date(start_date + datetime.timedelta(hours = timestep))

            ndate = date_string[ : 4] + '/ ' + date_string[4 : 6] + '/ ' + date_string[6 : 8]

            xticks_datetime.append(ndate)



    fig = plt.figure(figsize = (14, 7))

    excel_choice = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150]
    for num_excel, excel in enumerate(os.listdir(sample_rounded)) :
        if num_excel in excel_choice :
            os.chdir(sample_rounded)
            temp = read_excel(excel)


            ahour_list = []
            for index in range(temp.shape[0]) :
                if temp.loc[index, 'hour_available'] == 'O' :
                    time_gap = (date_to_datetime(temp.loc[index, '보정_시간']) - start_date)
#                    print(time_gap.days * 24)
#                    print(time_gap.seconds // 3600)

                    ahour_list.append(time_gap.days * 24 + time_gap.seconds // 3600)

            #print(ahour_list)

            for num_item, item in enumerate(ahour_list) :
                plt.plot([item, item + 1], [num_excel, num_excel], linewidth = 10)

            print(num_excel)

    plt.xticks(xticks, xticks_datetime, rotation = 90)
    plt.title('available hours for each stations')
    plt.ylabel('stations')

    sample_plot_data = os.path.join(sample_plot, 'data_basics')
    dich.newfolder(sample_plot_data)
    os.chdir(sample_plot_data)
    plt.savefig('available_time_in_timesteps.png', dpi = 400)





a = input('plot individual informations (y/n)')

if a == 'y' :
    zoom_plot = os.path.join(sample_plot_data, 'zoom_plot')
    print(zoom_plot)
    dich.newfolder(zoom_plot)
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



    target_info = ['기온', '미세먼지']
    #target_info = ['풍속', '미세먼지']
    target_info = ['풍속']


    for target in target_info :
        summer_df = None
        winter_df = None
        summer_df = pd.DataFrame(index = summer_hours)
        winter_df = pd.DataFrame(index = winter_hours)
        for num_excel, excel in enumerate(os.listdir(sample_rounded)) :
            if num_excel > -1:
                
                # read excel
                os.chdir(sample_rounded)
                target_col = ['기온', '미세먼지', '풍향', '풍속', '보정_시간', 'hour_available']
                print(excel)
                print('###' * 3)
                df = read_excel(excel)
                
                check = 0
                for target_item in target_col :
                    if target_item not in df.columns :
                        check = 1

                if check == 0 :
                    df = df[target_col]
                    df.sort_values(by = ['보정_시간'], inplace = True)


                    # pull summer / winter days
                    summer_index = []
                    winter_index = []
                    for num_index, index in enumerate(range(df.shape[0])) :
                        
                        if str(df.loc[index, '보정_시간'])[ : 8] == summer_day :
                            summer_index.append(index)

                        if str(df.loc[index, '보정_시간'])[ : 8] == winter_day :
                            winter_index.append(index)

                    summer_temp = df.loc[summer_index, : ]
                    winter_temp = df.loc[winter_index, : ]

                    summer_avail = summer_temp[summer_temp['hour_available'] == 'O']
                    winter_avail = winter_temp[winter_temp['hour_available'] == 'O']

                    summer_avail.reset_index(drop = True, inplace = True)
                    winter_avail.reset_index(drop = True, inplace = True)

                    for index in range(summer_avail.shape[0]) :
                        print(summer_avail.loc[index, '보정_시간'])
                        summer_df.loc[str(summer_avail.loc[index, '보정_시간']), excel] = str(summer_avail.loc[index, target])


                    for index in range(winter_avail.shape[0]) :
                        winter_df.loc[str(winter_avail.loc[index, '보정_시간']), excel] = str(winter_avail.loc[index, target])

                    print(f'{target}\t{num_excel}\t{excel}')
                else :
                    print(f'not in _______ {target}\t{num_excel}\t{excel}')


        # save dataframe
        os.chdir(zoom_plot)

        summer_df.to_excel(f'{target}_summer_df.xlsx')
        winter_df.to_excel(f'{target}_winter_df.xlsx')

        # load dataframe

        os.chdir(zoom_plot)
        print(zoom_plot)

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
            summer_box = [int(x) for x in summer_df.loc[index, :].tolist() if (str(x) != 'nan') & (str(x) != 'O')]

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
        elif target == '미세먼지' :
            pass
#        ax1.set_ylim(10, 120)
#        ax2.set_ylim(10, 120)

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

        ax1.set_title(f'{target}\n2021/ 06/ 21')
        ax2.set_title(f'{target}\n2021/ 12/ 22')

        ax1.set_xlabel('hour')
        ax1.set_ylabel(f'{target}')

        ax2.set_xlabel('hour')
        ax2.set_ylabel(f'{target}')

        os.chdir(zoom_plot)
        plt.savefig(f'{target}_summer_winter_zoomed.png', dpi = 400)
        dlt.savefig(zoom_plot, f'{target}_summer_winter_zoomed.png', 400)

        plt.clf
        



#

