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

# one_module.py ends


# -----------------------------------------------
# -----------------------------------------------
# temp1.py starts
# -----------------------------------------------
# -----------------------------------------------

# -----------------------------------------------
# check data times if they are omitted or not 
# -----------------------------------------------

a = input('check data times for omitted infos (y/n)')

if a == 'y' :
    os.chdir(sample_data)
    print(os.listdir(sample_data))


    data_date = pd.DataFrame(columns = ['excel', 'columns_num', 'columns'])
    num_date = 0


    for excel in os.listdir(sample_data) :
        os.chdir(sample_data)
        temp = read_excel(excel)


        print(len(temp.columns))
        data_date.loc[num_date, :] = [excel, len(temp.columns), str(temp.columns)]
        num_date += 1

    os.chdir(sample_plot)
    data_date.to_excel('date_info.xlsx')

    print('done and saved')


# -----------------------------------------------
# typo correcting dictionary
# -----------------------------------------------

merge_columns = dict()

merge_columns['기관명'] = ['기관명', '기관 명']
merge_columns['모델명'] = ['모델명', '모델 명']
merge_columns['시리얼'] = ['시리얼']
merge_columns['전송시간'] = ['전송 시간', '전송시간']
merge_columns['등록일자'] = ['등록일자', '등록 일자']
merge_columns['돌풍풍향'] = ['돌풍 풍향(°)', '돌풍풍향(°)']
merge_columns['돌풍풍속'] = ['돌풍 풍속(m/s)', '돌풍풍속(m/s)']
merge_columns['풍향'] = ['풍향(°)', '풍향 (°)']
merge_columns['풍속'] = ['풍속(m/s)', '풍속 (m/s)']
merge_columns['기온'] = ['기온(℃)', '기온(℃) ', '기온 (℃)', ' 기온(℃) ']
merge_columns['상대습도'] = ['상대습도(%)', '상대습도 (%)', '상대습도( %)']
merge_columns['초미세먼지'] = ['초미세먼지(㎍/㎥)', '초미세먼지 (㎍/㎥)']
merge_columns['미세먼지'] = ['미세먼지(㎍/㎥)', '미세먼지 (㎍/㎥)']
merge_columns['초미세먼지보정'] = ['초미세먼지 보정(㎍/㎥)', '초미세먼지 보정 (㎍/㎥)']
merge_columns['미세먼지보정'] = ['미세먼지 보정(㎍/㎥)', '미세먼지 보정 (㎍/㎥)']

save_columns = list(merge_columns.keys())

save_target = []
for key in merge_columns.keys() :
    for item in merge_columns[key] :
        save_target.append(item)


# -----------------------------------------------
# apply to sample datas
# -----------------------------------------------

print(save_columns)
print(save_target)

print(len(save_columns))
print(len(save_target))

a = input('apply typo correcting to sample datas? (y/n)')

if a == 'y' :
    all_excel = len(os.listdir(sample_data))
    for num_excel, excel in enumerate(os.listdir(sample_data)) :
        os.chdir(sample_data)
        temp = read_excel(excel)

        save = []
        kill = []

        for col in temp.columns :
            check = 0
            for key in save_columns : 
                if col in merge_columns[key] :
                    check = 1
                    break
            
            if check == 1 :
                save.append(col)
            else :
                kill.append(col)

        print(save)
        print(kill)

        print(temp.columns)
        for col in temp.columns :
            if col in save :
                check = 0
                for key in save_columns : 
                    if col in merge_columns[key] :
                        column_change = key
                        check = 1

                if check == 0 :
                    print(f'{col}\tnot matched')

                else :
                    print(f'{col}\t{column_change}')
                    for index in range(temp.shape[0]) :
                        if not pd.isna(temp.loc[index, col]) :
                            temp.loc[index, column_change] = temp.loc[index, col]
                        else :
                            print(f'{index} | {col}, nan')

            
            
            kill_columns = []
            for col in temp.columns :
                if col not in save_columns :
                    kill_columns.append(col)

            temp.drop(kill_columns, axis = 1, inplace = True)
            temp.reset_index(drop = True, inplace = True)
            

            os.chdir(sample_typo)
            temp.to_excel(excel)

            print(f'{num_excel} / {all_excel}\t{round((num_excel / all_excel) * 100, 2)}%\t{len(temp.columns)}')


                


# -----------------------------------------------
# check typo corrected sample datas
# -----------------------------------------------

a = input('check sample datas after typo correcting (y/n)')

if a == 'y' :
    os.chdir(sample_typo)
    print(os.listdir(sample_typo))


    data_date = pd.DataFrame(columns = ['excel', 'columns_num', 'columns'])
    num_date = 0


    for excel in os.listdir(sample_typo) :
        os.chdir(sample_typo)
        temp = read_excel(excel)


        print(len(temp.columns))
        data_date.loc[num_date, :] = [excel, len(temp.columns), str(temp.columns)]
        num_date += 1

    os.chdir(sample_plot)
    data_date.to_excel('date_info_aftertypo.xlsx')

    print('done and saved')




# -----------------------------------------------
# -----------------------------------------------
# temp2.py starts
# -----------------------------------------------
# -----------------------------------------------
# -----------------------------------------------
# unite transmission time format
# -----------------------------------------------

# type of formats

# 2021-10-03 5:03
# 2021-10-03 23:03:10 PM


# drop nan values in ['등록일자']

a = input('drop nan times (y/n)')

if a == 'y' :
    num_all = len(os.listdir(sample_time))
    for num_excel, excel in enumerate(os.listdir(sample_time)) :

        os.chdir(sample_time)
        temp = read_excel(excel)

        temp.dropna(subset = ['등록일자'], inplace = True)
        temp.reset_index(drop = True, inplace = True)

        os.chdir(sample_only_time)
        temp.to_excel(excel)
        print(f'{num_excel + 1} / {num_all}\t{round(((num_excel + 1) / num_all) * 100, 2)}%')


# -----------------------------------------------
# check null values | outliers 
# -----------------------------------------------


# check null values percentages for each information

a = input('check null and outliers?(y/n)')

if a == 'y' :
    import outlier as out
    target_info_list = ['풍속', '풍향', '기온', '상대습도', '초미세먼지', '미세먼지']

    for target_info in target_info_list :

        df_outliers = pd.DataFrame(columns = ['excel', 'total_size', 'null', 'z-score', 'IQR', 'method(min)', 'in-range(min)', 'in-range(max)'])
        num_outliers = 0

        num_all = len(os.listdir(sample_only_time))
        for num_excel, excel in enumerate(os.listdir(sample_only_time)) :
            os.chdir(sample_only_time)
            temp = read_excel(excel)

            if temp.shape[0] == 0 :
                df_outliers.loc[num_outliers, :] = [excel, 0, 'no_index', 'no_index', 'no_index', 'no_index', 'no_index', 'no_index']
                num_outliers += 1

            else :

                null_num = temp[target_info].isnull().sum()
                
                if null_num == temp.shape[0] :
                    df_outliers.loc[num_outliers, :] = [excel, temp.shape[0], null_num, 0, 0, 'none', 0, 0]
                    num_outliers += 1


                else :
                    target = temp[target_info].dropna().tolist()
                    zscore_non, zscore = out.z_score(target, 2)
                    iqr_non, iqr = out.out_box(target, 1.5)

                    z_num = len(zscore)
                    iqr_num = len(iqr)

                    left_num_min = temp.shape[0] - null_num - min(z_num, iqr_num)
                    left_num_max = temp.shape[0] - null_num - max(z_num, iqr_num)

                    if min(z_num, iqr_num) == z_num :
                        method_used = 'z_score'
                    else :
                        method_used = 'iqr'
                        

                    df_outliers.loc[num_outliers, :] = [excel, temp.shape[0], null_num, z_num, iqr_num, method_used, left_num_min, left_num_max]
                    num_outliers += 1
            print(f'{num_excel} / {num_all}')

        os.chdir(os.path.join(sample_plot, 'null_outliers_check'))
        df_outliers.to_excel(f'{target_info}_null_outliers_check.xlsx')
        print(df_outliers)


# -----------------------------------------------
# -----------------------------------------------
# temp3.py starts
# -----------------------------------------------
# -----------------------------------------------
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
sample_plot = os.path.join(sample_plot, 'barplot_info')


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
    start_date = datetime.datetime(2020, 1, 1, 00)
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



    return date_dict, inverse_dict


date_dict, inverse_dict = all_date()




excepted = 0

df = pd.DataFrame(columns = ['excel', 'date', 'hour', 'temperature', 'wind_angle', 'wind_speed', 'fine_dust'])
df_num = 0

for excel_num, excel in enumerate(os.listdir(sample_avail)) :
    os.chdir(sample_avail)
    temp = read_excel(excel)
    if (temp.shape[0] != 0) :
        #print(temp.columns)
        #print(temp.loc[: , ['등록일자', '기온']])

        for index in range(temp.shape[0]) :
            real_date = str(temp.loc[index, '등록일자'])[4 : 8] + ' ' + str(temp.loc[index, '등록일자'])[8 : 10] + '시'
            temp_date = str(temp.loc[index, '등록일자'])[ : 10] + '00'

            if temp_date in date_dict.keys() :
                temp_num = date_dict[temp_date]

            temp_temp = float(str(temp.loc[index,'기온']).replace(',', ''))
            temp_wa = float(temp.loc[index, '풍향'])
            temp_ws = float(temp.loc[index, '풍속'])
            temp_fd = float(temp.loc[index, '미세먼지'])

            if (temp_temp > -15) & (temp_temp < 50) :
                if (temp_wa > -1) & (temp_wa < 361) :
                    if (temp_ws > -1) & (temp_ws < 10) :
                        if temp_fd != 'nan' :

                            df.loc[df_num, :] = [excel, real_date, temp_num, temp_temp, temp_wa, temp_ws, temp_fd]
                            df_num += 1
                            check = 1
            if check == 0 :
                excepted += 1


    print(f'{excel_num + 1}, {len(os.listdir(sample_avail))}')
print(df)

df.sort_values(by = ['hour'], inplace = True, ignore_index = True)


all_hour = df.loc[:, 'hour'].tolist()
real_date = df.loc[:, 'date'].tolist()
all_temperate = df.loc[:, 'temperature'].tolist()
all_wa = df.loc[:, 'wind_angle'].tolist()
all_ws = df.loc[:, 'wind_speed'].tolist()
all_fd = df.loc[:, 'fine_dust'].tolist()

print(min(all_hour))
min_date = inverse_dict[min(all_hour)]
max_date = inverse_dict[max(all_hour)]

fig = plt.figure(figsize = (10, 7))

plt.scatter(all_hour, all_temperate)
#plt.xlim(0, 8760)
#plt.xticks(all_hour, real_date, rotation = 90)
plt.grid()
os.chdir(sample_plot)
plt.title(f'temperature\n{min_date} to {max_date}')
plt.savefig('temp_temperature_all.png', dpi = 400)
dlt.savefig(sample_plot, 'temp_temperature_all', 400)
plt.clf()


df = pd.DataFrame(columns = ['angle', 'speed'])
df.loc[:, 'angle'] = all_wa
df.loc[:, 'speed'] = all_ws
df.sort_values(by = ['angle'], inplace = True, ignore_index = True)

for item in df.loc[:, 'angle'].unique() :
    temp_speed = df[df['angle'] == item].loc[:, 'speed'].tolist()
    plt.boxplot(temp_speed, positions = [item])

#plt.scatter(all_wa, all_ws)
plt.title('wind angle & speed\nx : angle, y : speed')
#plt.grid()
dlt.savefig(sample_plot, 'temp_was_boxplot', 400)
plt.clf()



plt.scatter(all_hour, all_wa)
#plt.xlim(0, 8760)
#plt.xticks(all_hour, real_date, rotation = 90)
plt.grid()
plt.title(f'wind angle\n{min_date} to {max_date}')
dlt.savefig(sample_plot, 'temp_wa_all', 400)
plt.clf()

plt.scatter(all_hour, all_ws)
#plt.xlim(0, 8760)
#plt.xticks(all_hour, real_date, rotation = 90)
plt.grid()
plt.title(f'wind speed\n{min_date} to {max_date}')
dlt.savefig(sample_plot, 'temp_ws_all', 400)
plt.clf()

plt.scatter(all_hour, all_fd)
#plt.xlim(0, 8760)
#plt.xticks(all_hour, real_date, rotation = 90)
plt.grid()
plt.title(f'fine dust\n{min_date} to {max_date}')
dlt.savefig(sample_plot, 'temp_fd_all', 400)
plt.clf()
    




# -----------------------------------------------
# plot wind
# -----------------------------------------------


# -----------------------------------------------
# plot temp
# -----------------------------------------------


# -----------------------------------------------
# plot fine_dust
# -----------------------------------------------
print(df)
print(excepted)

#target_num = len(df.loc[:, 'hour'].unique().tolist())
#
#for num_item, item in enumerate(df.loc[:, 'hour'].unique()) :
#    temp = df[df['hour'] == item].loc[:, 'temperature'].tolist()
#    for temp_item in temp :
#        plt.scatterplot(item, temp_item)
#    #plt.boxplot(temp, positions = [item])
#    print(num_item, '\t', target_num)

# -----------------------------------------------
# -----------------------------------------------
# temp4.py starts
# -----------------------------------------------
# -----------------------------------------------
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
        print(f'{excel_num + 1} / 32')



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
    os.chdir(os.path.join(sample_plot, 'temperature'))
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
        


# -----------------------------------------------
# -----------------------------------------------
# temp5.py starts
# -----------------------------------------------
# -----------------------------------------------

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
        print(f'{excel_num + 1} / 32')



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

        


# -----------------------------------------------
# -----------------------------------------------
# temp6.py starts
# -----------------------------------------------
# -----------------------------------------------


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

sample_round = os.path.join(sample_robby, 'rounded')

if a == 'y' :
    df = pd.DataFrame(columns = ['excel', 'org_date', 'time-jam', 'overlapped rounded time', 'nan times', 'dropped_date', 'percentage'])
    df_num = 0

    for excel_num, excel in enumerate(os.listdir(sample_avail)) :
        if excel_num > -1:
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
            


# -----------------------------------------------
# -----------------------------------------------
# temp7.py starts
# -----------------------------------------------
# -----------------------------------------------


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
        print(f'{excel_num + 1} / 32')



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
            if (val != -1) : #& (val != 0) & (val != 60) & (val % 60 != 0) :
                
                print(col, interval_all.loc[excel, col])
                plt.plot([col, col + 1], [interval_all.loc[excel, col], interval_all.loc[excel, col]], color = 'blue', linewidth = 3)



    plt.title('minute_interval\none sample stations')

    plt.ylabel('minute')
#    plt.ylim(0, 300)
#    grid_list = [0, 60, 120, 180, 240, 300]
#    plt.yticks(grid_list)
    plt.grid()
    os.chdir(sample_plot)
    plt.savefig('scattered_timedelta_rounded.png', dpi = 400)
    dlt.savefig(sample_plot, 'scattered_timedelta_rounded.png', 400)

        


