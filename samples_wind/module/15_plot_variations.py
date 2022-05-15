import os
import sys
from pathlib import Path
import os.path
import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statistics


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
    
    summer_date = '20210621'
    winter_date = '20211222'

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
    #print(target_df)

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
    
    #print(len(add_target_date))
    for day in add_target_date :
        target_df.loc[target_edt, '보정_시간'] = day
        target_edt += 1

    for index in range(target_df.shape[0]) :
        target_df.loc[index, '보정_시간'] = str(int(target_df.loc[index, '보정_시간']))

    target_df.sort_values(by = ['보정_시간'], inplace = True, ignore_index = True)

    return target_df

def get_iqr(list1) :
    Q1 = np.percentile(list1, 25)
    Q3 = np.percentile(list1, 75)

    return Q3 - Q1



# -----------------------------------------------
# make date list and date_dict, inverse_dict
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
rounded = sample_rounded

main_dir = sample_robby.parent
module_dir = os.path.join(main_dir, 'module')

datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
info_dir = os.path.join(main_dir, 'info_data')


################################################
# scatterplot of magnitude - variation
################################################

a = input('make scatterplot of magnitude - variation? (y/n)')


summer_date = '20210621'
winter_date = '20211222'

check_list = ['기온', '풍향', '풍속', '초미세먼지', '미세먼지']


if a == 'y' :
# i = 0 : summer, i = 1 : winter
    for i in range(2) :
        for target in check_list :

            target_df = pd.DataFrame(columns = list(range(24)))
            t_num = 0

            for num_excel, excel in enumerate(os.listdir(sample_rounded)) :
                if num_excel > -1 :
                    os.chdir(sample_rounded)
                    temp = read_excel(excel)

                    if i == 0 : # summer
                        temp_day = get_day(temp, summer_date)
                        temp_list = temp_day.loc[:, target].tolist()

                        season = 'summer'
                        season_date = summer_date

                    elif i == 1 : # winter
                        temp_day = get_day(temp, winter_date)
                        temp_list = temp_day.loc[:, target].tolist()

                        season = 'winter'
                        season_date = winter_date

                    target_df.loc[t_num, :] = temp_list
                    t_num += 1
                    print(num_excel)
                    
                    
            # magnitude to variation(iqr)
            mtv_df = pd.DataFrame(columns = list(range(24)), index = ['iqr', 'mean'])
            for col in target_df.columns :
                col_list = [x for x in target_df.loc[:, col] if str(x) != 'nan']

                col_iqr = get_iqr(col_list)
                col_mean = ave(col_list)

                mtv_df.loc['iqr', col] = col_iqr
                mtv_df.loc['mean', col] = col_mean
            

            # get linear regression
            all_mean = mtv_df.loc['mean', :].tolist()
            all_iqr = mtv_df.loc['iqr', :].tolist()

            all_mean_reshaped = np.array(all_mean)#.reshape(1, -1)
            all_iqr_reshaped = np.array(all_iqr)#.reshape(1, -1)

            R_squared = r2_score(all_mean_reshaped, all_iqr_reshaped)
            R_squared = round(R_squared, 2)
#            model = LinearRegression()
#            model.fit(all_mean_reshaped, all_iqr_reshaped)
#            #R_squared = model.score(all_mean_reshaped, all_iqr_reshaped)
#
#            
#            y_pred = model.predict(all_mean_reshaped)
#            R_squared = r2_score(all_iqr_reshaped, y_pred)
#
            
            print(R_squared)

            inc, y_intercept = np.polyfit(all_mean, all_iqr, 1)

            xseq = np.linspace(min(all_mean), max(all_mean), num = 100)

            # draw plot
            fig = plt.figure(figsize = (13, 7))
            for col in mtv_df.columns :
                plt.plot(mtv_df.loc['mean', col], mtv_df.loc['iqr', col], markersize = 5, marker = 'o', color = 'firebrick')

            # plot regression result
            plt.plot(xseq, y_intercept + inc * xseq, color = 'darkblue', lw = 2, label = f'R_squared = {R_squared}')
            plt.legend()


            plt.title(f'{season}, {season_date}\n{target}')
            plt.xlabel('average')
            plt.ylabel('IQR')

            plot_path = os.path.join(sample_plot, 'variation_plot', 'scatterplot_mag_iqr')
            dich.newfolder(plot_path)

            os.chdir(plot_path)
            plt.savefig(f'{season}, {season_date}, {target}', dpi = 400)
            dlt.savefig(plot_path, f'{season}, {season_date}, {target}', 400)

            plt.clf()



################################################
# affect of lux (comparison btw Daytime - Nighttime) 
################################################

# daytime : 6am to 6pm (6 - 18)
# nighttime : 12am to 6am (0 - 6), 6pm to 12am (6 - 23)


a = input('make plot of lux - daytime vs nighttime? (y/n)')


summer_date = '20210621'
winter_date = '20211222'

check_list = ['기온']



if a == 'y' :
# i = 0 : summer, i = 1 : winter
    for i in range(2) :
        for target in check_list :

            target_df = pd.DataFrame(columns = list(range(24)))
            t_num = 0

            for num_excel, excel in enumerate(os.listdir(sample_rounded)) :
                if num_excel > -1 :
                    os.chdir(sample_rounded)
                    temp = read_excel(excel)

                    if i == 0 : # summer
                        temp_day = get_day(temp, summer_date)
                        temp_list = temp_day.loc[:, target].tolist()

                        season = 'summer'
                        season_date = summer_date

                    elif i == 1 : # winter
                        temp_day = get_day(temp, winter_date)
                        temp_list = temp_day.loc[:, target].tolist()

                        season = 'winter'
                        season_date = winter_date

                    target_df.loc[t_num, :] = temp_list
                    t_num += 1
                    print(num_excel)
                    
                    
            # magnitude to variation(iqr)
            mtv_df = pd.DataFrame(columns = list(range(24)), index = ['iqr', 'mean'])
            for col in target_df.columns :
                col_list = [x for x in target_df.loc[:, col] if str(x) != 'nan']

                col_iqr = get_iqr(col_list)
                col_mean = ave(col_list)

                mtv_df.loc['iqr', col] = col_iqr
                mtv_df.loc['mean', col] = col_mean


            daytime_range = [6, 7, 8, 9, 10, 11, 12, 13, 14 ,15, 16, 17]
            nighttime_range = [0, 1, 2, 3, 4, 5, 18, 19, 20, 21, 22, 23]
            daytime_df = mtv_df[daytime_range].copy()
            nighttime_df = mtv_df[nighttime_range].copy()

            print(daytime_df)
            print(nighttime_df)

            daytime_list = daytime_df.loc['iqr', :].tolist()
            nighttime_list = nighttime_df.loc['iqr', :].tolist()


        # boxplot of IQR at daytime / nighttime
            fig = plt.figure(figsize = (5, 9))

            plt.boxplot(daytime_list, positions = [0])
            plt.boxplot(nighttime_list, positions = [1])

            plt.grid()

            plt.title(f'{season}\ndaytime - nighttime')
            plt.xticks([0, 1], ['daytime', 'nighttime'])

            plt.ylabel('boxplot of IQR')

            plot_path = os.path.join(sample_plot, 'variation_plot')
            dich.newfolder(plot_path)

            os.chdir(plot_path)
            plt.savefig(f'{season}, daytime_nighttime', dpi = 400)
            dlt.savefig(plot_path,f'{season}, daytime_nighttime' , 400)

            plt.clf()

        # barplot of IQR at every hour
            fig = plt.figure(figsize = (10, 6))
            
            daytime_hours = daytime_df.columns.astype(int)
            nighttime_hours = nighttime_df.columns.astype(int)

            daytime_values = daytime_df.loc['iqr', :].tolist()
            nighttime_values = nighttime_df.loc['iqr', :].tolist()
            
            plt.bar(daytime_hours, daytime_values, color = 'firebrick')
            plt.bar(nighttime_hours, nighttime_values, color = 'darkblue')

            plt.title(f'{season}\ndaytime - nighttime')

            plt.ylabel('IQR')

            plot_path = os.path.join(sample_plot, 'variation_plot')
            dich.newfolder(plot_path)

            os.chdir(plot_path)
            plt.savefig(f'{season}, daytime_nighttime, barplot', dpi = 400)
            dlt.savefig(plot_path,f'{season}, daytime_nighttime, barplot' , 400)

            plt.clf()

################################################
# Fluctuation of Data (daily)
################################################

# thermal mass (TM) = 1 / fluc = 1 / (fluc_daily * fluc_yearly)
# fluc_daily : max(day) - min(day)
# fluc_yearly : max(year) - min(year)

# time delay (TD) = (min_peak_day + max_peak_day) / 2  * (min_peak_year + max_peak_year) / 2

# thermal mass and time delay should show linear relationship


a = input('thermal mass of fluctuation? (y/n)')


summer_date = '20210621'
winter_date = '20211222'

check_list = ['기온']



if a == 'y' :
# i = 0 : summer, i = 1 : winter
    # dataframe for saving TD infos
    tm_df = pd.DataFrame(columns = ['FM_summer', 'FM_winter', 'FM_year', 'TD_summer', 'TD_winter', 'TD_year', 'FM', 'TD', 'TM', 'summer_ave', 'winter_ave'])
    tm_num_summer = 0
    tm_num_winter = 0
    for i in range(2) :
        for target in check_list :

        # dataframe for plotting fluctuation
            target_df = pd.DataFrame(columns = list(range(24)))
            t_num = 0


            fluc_daily_list = []
            fluc_yearly_list = []

            for num_excel, excel in enumerate(os.listdir(sample_rounded)) :
                if num_excel > -1 :
                    os.chdir(sample_rounded)
                    temp = read_excel(excel)
                    temp_list = temp.loc[:, target].tolist()

                    if i == 0 : # summer
                        if num_excel == 0 :
                            tm_num = tm_num_summer
                        temp_day = get_day(temp, summer_date)
                        temp_day_list = temp_day.loc[:, target].tolist()

                        summer_ave = ave([x for x in temp_day_list if str(x) != 'nan'])

                        season = 'summer'
                        season_date = summer_date

                    elif i == 1 : # winter
                        if num_excel == 0 :
                            tm_num = tm_num_winter
                        temp_day = get_day(temp, winter_date)
                        temp_day_list = temp_day.loc[:, target].tolist()

                        season = 'winter'
                        season_date = winter_date

                        winter_ave = ave([x for x in temp_day_list if str(x) != 'nan'])
                        print(winter_ave)

                    
            # fluctuation _ daily
                    # daily fluctuation summer
                    max_daily = max(temp_day_list)
                    min_daily = min(temp_day_list)

                    # peak time summer
                    min_peak_daily = temp_day_list.index(min(temp_day_list))
                    max_peak_daily = temp_day_list.index(max(temp_day_list))

                    peak_mid_daily = (min_peak_daily + max_peak_daily) / 2
                    fluc_daily = (max_daily - min_daily)
                    fluc_daily_list.append(fluc_daily)
                    
                    if i == 0 : # summer
                        tm_df.loc[tm_num, 'FM_summer'] = fluc_daily
                        tm_df.loc[tm_num, 'TD_summer'] = peak_mid_daily

                    elif i == 1 : # winter
                        tm_df.loc[tm_num, 'FM_winter'] = fluc_daily
                        tm_df.loc[tm_num, 'TD_winter'] = peak_mid_daily



            # fluctuation _ yearly
                    max_yearly = max(temp_list)
                    min_yearly = min(temp_list)

                    # peak time summer
                    min_peak_yearly = temp_list.index(min(temp_list))
                    max_peak_yearly = temp_list.index(max(temp_list))

                    peak_mid_yearly = (min_peak_yearly + max_peak_yearly) / 2
                    fluc_yearly = (max_yearly - min_yearly)

                    tm_df.loc[tm_num, 'FM_year'] = fluc_yearly
                    tm_df.loc[tm_num, 'TD_year'] = peak_mid_yearly

            # define Thermal Mass
                    if i == 0 : # summer comes first
                        tm_df.loc[tm_num, 'summer_ave'] = summer_ave
                        tm_num += 1

                    if i == 1 : # after winter
                        tm_df.loc[tm_num, 'winter_ave'] = winter_ave

                        FM = pow(10, 4) / (tm_df.loc[tm_num, 'FM_summer'] * tm_df.loc[tm_num, 'FM_winter'] * tm_df.loc[tm_num, 'FM_year'])
                        TD = (tm_df.loc[tm_num, 'TD_summer'] * tm_df.loc[tm_num, 'TD_winter'] * tm_df.loc[tm_num, 'TD_year']) * pow(10, -5)
                        TM = FM * TD

                        tm_df.loc[tm_num, 'FM'] = FM
                        tm_df.loc[tm_num, 'TD'] = TD
                        tm_df.loc[tm_num, 'TM'] = TM

                        tm_num += 1


            # save to a dataframe
                    target_df.loc[t_num, :] = temp_day_list
                    t_num += 1
                    print(num_excel)

            fluc_daily_ave = statistics.median(fluc_daily_list)
            target_df['fluc'] = None
            target_df['level'] = None
            target_df.loc[:, 'fluc'] = fluc_daily_list

            for index in range(target_df.shape[0]) :
                if target_df.loc[index, 'fluc'] > fluc_daily_ave :
                    target_df.loc[index, 'level'] = 'high'

                elif target_df.loc[index, 'fluc'] == fluc_daily_ave :
                    target_df.loc[index, 'level'] = 'mid'

                else :
                    target_df.loc[index, 'level'] = 'low'

            

                    
        # low, mid, hight fluctuation
            fig = plt.figure(figsize = (10, 15))

            ax1 = fig.add_subplot(3, 1, 1)
            ax2 = fig.add_subplot(3, 1, 2)
            ax3 = fig.add_subplot(3, 1, 3)

            # ax1, high

            trans = 0.1
            opaque = 0.8

            for index in range(target_df.shape[0]) :
                if target_df.loc[index, 'level'] == 'high' :
                    color = 'firebrick'
                    alpha = opaque
                elif target_df.loc[index, 'level'] == 'mid' :
                    color = 'forestgreen'
                    alpha = trans
                else :
                    color = 'darkblue'
                    alpha = trans

                ax1.plot(list(range(24)), target_df.loc[index, 0 : 23].tolist(), c = color, alpha = alpha)
                

                ax1.set_xticks(list(range(0, 23)))
                ax1.grid()

            # ax2, mid

            trans = 0.1
            opaque = 0.8

            for index in range(target_df.shape[0]) :
                if target_df.loc[index, 'level'] == 'high' :
                    color = 'firebrick'
                    alpha = trans
                elif target_df.loc[index, 'level'] == 'mid' :
                    color = 'forestgreen'
                    alpha = opaque
                else :
                    color = 'darkblue'
                    alpha = trans

                ax2.plot(list(range(24)), target_df.loc[index, 0 : 23].tolist(), c = color, alpha = alpha)
                

                ax2.set_xticks(list(range(0, 23)))
                ax2.grid()

            # ax3, low

            trans = 0.1
            opaque = 0.8

            for index in range(target_df.shape[0]) :
                if target_df.loc[index, 'level'] == 'high' :
                    color = 'firebrick'
                    alpha = trans
                elif target_df.loc[index, 'level'] == 'mid' :
                    color = 'forestgreen'
                    alpha = trans
                else :
                    color = 'darkblue'
                    alpha = opaque

                ax3.plot(list(range(24)), target_df.loc[index, 0 : 23].tolist(), c = color, alpha = alpha)
                

                ax3.set_xticks(list(range(0, 23)))
                ax3.grid()

            plot_path = os.path.join(sample_plot, 'variation_plot')
            dich.newfolder(plot_path)

            os.chdir(plot_path)

            target_df.to_excel(f'fluctuation_by_daily_{season}.xlsx')


            plt.suptitle(f'fluctuation, ref value = {fluc_daily_ave}(degC)\n{season}')
            plt.savefig(f'{season}, fluctuation', dpi = 400)
            dlt.savefig(plot_path,f'{season}, fluctuation', 400)

            plt.clf()

    tm_df.to_excel(f'thermal_mass.xlsx')
    print(tm_df)


a = input('make TM plot? (y/n)')

if a == 'y' :
    plot_path = os.path.join(sample_plot, 'variation_plot')
    dich.newfolder(plot_path)
    os.chdir(plot_path)

    tm_df = read_excel('thermal_mass.xlsx')

    FM_list = tm_df.loc[:, 'FM'].tolist()
    TD_list = tm_df.loc[:, 'TD'].tolist()
    TM_list = tm_df.loc[:, 'TM'].tolist()
    summer_list = tm_df.loc[:, 'summer_ave'].tolist()
    winter_list = tm_df.loc[:, 'winter_ave'].tolist()

    # make plot (FM to TD)

    fig = plt.figure(figsize = (7, 4))

    plt.scatter(FM_list, TD_list, color = 'darkblue', alpha = 0.8)

    plt.title('fluctuation mass to time delay')
    plt.xlabel('fluctuation mass')
    plt.ylabel('time delay')

    plt.savefig('FM_to_TD.png', dpi = 400)
    plt.clf()


    # make plot (FM to TM)

    fig = plt.figure(figsize = (7, 4))

    plt.scatter(FM_list, TM_list, color = 'darkblue', alpha = 0.8)

    plt.title('fluctuation mass to thermal mass')
    plt.xlabel('fluctuation mass')
    plt.ylabel('thermal mass')

    plt.savefig('FM_to_TM.png', dpi = 400)
    plt.clf()

    # make plot (TD to TM)

    fig = plt.figure(figsize = (7, 4))

    plt.scatter(TD_list, TM_list, color = 'darkblue', alpha = 0.8)

    plt.title('time delay to thermal mass')
    plt.xlabel('time delay')
    plt.ylabel('thermal mass')

    plt.savefig('TD_to_TM.png', dpi = 400)
    plt.clf()

    # make plot (TM to summer / winter ave)

    fig = plt.figure(figsize = (7, 13))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)


    ax1.scatter(TM_list, summer_list, color = 'firebrick', alpha = 0.8)

    ax1.set_xlabel('thermal mass')
    ax1.set_ylabel('summer average')

    ax2.scatter(TM_list, winter_list, color = 'darkblue', alpha = 0.8)

    ax2.set_xlabel('thermal mass')
    ax2.set_ylabel('winter average')

    plt.suptitle('thermal mass to magnitude')
    plt.savefig('fluctuation_to_magnitude.png', dpi = 400)
    plt.clf()


    # make plot (FM to summer / winter ave)

    fig = plt.figure(figsize = (7, 13))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)


    ax1.scatter(FM_list, summer_list, color = 'firebrick', alpha = 0.8)

    ax1.set_xlabel('thermal mass')
    ax1.set_ylabel('summer average')

    ax2.scatter(FM_list, winter_list, color = 'darkblue', alpha = 0.8)

    ax2.set_xlabel('thermal mass')
    ax2.set_ylabel('winter average')

    plt.suptitle('fluctuation mass to magnitude')
    plt.savefig('fluctuation_to_magnitude_FM.png', dpi = 400)
    plt.clf()


###############################################
# Fluctuation of Data (yearly)
###############################################






################################################
# Fluctuation to Thermal mass
################################################






