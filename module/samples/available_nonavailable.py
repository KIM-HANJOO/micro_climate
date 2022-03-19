import os
import sys
from pathlib import Path
import os.path

preprocess_dir = Path(os.getcwd())
module_dir = preprocess_dir.parent
main_dir = module_dir.parent
datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')

preprocessed_dir = os.path.join(main_dir, 'preprocessed')
serials_dir = os.path.join(preprocessed_dir, 'serials')

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
# wind available stations for group_V, group_O
# -----------------------------------------------

os.chdir(main_dir)
location = read_excel('location.xlsx')
wind_only = read_excel('wind_only.xlsx')

print(wind_only.head())
wind_only.columns = ['serials', 'longitude', 'latitude', 'wind']
location.columns = ['serials', 'longitude', 'latitude']
print(wind_only.columns)
print(wind_only['wind'].unique())

serial_list = wind_only['serials'].tolist()

wind_v = [x for x in serial_list if 'V' in x]
wind_o = [x for x in serial_list if 'O' in x]

print(len(wind_v), len(wind_o), len(serial_list))


print(location.head())
print(location.shape)


serial_data = [str(x) for x in os.listdir(serials_dir) if ('O' in x) | ('V' in x)]
serial_info = location['serials'].tolist()
serial_info = sorted(serial_info)
serial_data = sorted(serial_data)

# list of items both in serial_data and serial_info
available_serial = []
serial_no_location = []
for item in serial_data :
    check = 0
    for item2 in serial_info :
        if item == item2 :
            check = 1
    if check == 1 :
        available_serial.append(item)
    else :
        serial_no_location.append(item)


# list of items only in serial_info 
# stations that have location, but no data

serial_no_data = []
for item in serial_info :
    check = 0
    for item2 in serial_data :
        if item == item2 :
            check = 1

    if check == 0 :
        serial_no_data.append(item)


# print length of each lists
print('available_serial', len(available_serial))
print('serial_no_location', len(serial_no_location))
print('serial_no_data', len(serial_no_data))

# check if any of the stations without location info
# have available wind information

print('check if item in serial_no_location has wind info\n')
available_in_serial_no_location = []
df = pd.DataFrame(columns = ['serial', 'available', 'null_perc', 'unique_level'])
df_num = 0

for item in serial_no_location :
    available_check = 'X'
    temp_dir = os.path.join(preprocessed_dir, 'merged')
    os.chdir(temp_dir)
    temp = read_excel(f'{item}.xlsx')
    target_col = []
    for col in temp.columns :
        if '풍향' in col :
            if '돌풍' not in col :
                target_col.append(col)
        if '풍속' in col :
            if '돌풍' not in col :
                target_col.append(col)
                speed_col = col

    print(target_col)
    null_num = 0
    for col in target_col :
        null_num += temp[col].isnull().sum()
        
    all_num = temp.shape[0] * 2

    null_perc = round(null_num / all_num * 100, 2)

    if (null_perc < 80) | ((null_perc > 100) & (null_perc < 180)) :
        for col in target_col :
            if len(temp[speed_col].unique()) > 5 :
                available_in_serial_no_location.append(item)
                available_check = 'O'

    if null_perc > 100 :
        print(null_num, all_num, temp.shape[0])
        
    df.loc[df_num, :] = [item, available_check, null_perc, len(temp[speed_col].unique())]
    df_num += 1


#    print(temp.head())
#    print(temp.columns)
    print(null_perc)
print(available_in_serial_no_location)
os.chdir(main_dir)
df.to_excel('stations_with_data_no_location_availablewind.xlsx')

    
    




# -----------------------------------------------
# Google map plot (API)
# -----------------------------------------------
